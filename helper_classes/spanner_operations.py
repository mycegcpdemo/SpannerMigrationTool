import json
import logging
import os
import time
from dotenv import load_dotenv

from helper_classes.sp_table import SpannerTable
from helper_classes.spanner_columns import SpannerColumns
from google.cloud import spanner
from multiprocessing.dummy import Pool as ThreadPool
from google.cloud.spanner_v1 import database


class SpannerOperations:
    load_dotenv()
    json_file = os.getenv('JSON_LISTING')
    spanner_table = os.getenv('SPANNER_TABLE')
    spanner_client = spanner.Client()
    instance = spanner_client.instance(os.getenv('SPANNER_INSTANCE'))
    database = instance.database(os.getenv('SPANNER_DB'))
    columns = SpannerColumns().columns

    def get_sorted_list(self):
        # Open file containing list of json objects with each object representing a row of 295 items.
        rew_data = open(self.json_file, "r")
        # Read file into a list and close the file
        listings = rew_data.readlines()
        rew_data.close()

        # Load the first entry which contains the entire JSON string to be deserialize
        list_of_objects = json.loads(listings[0])

        # Sanity check to verify we are loading the number of row we created used the fake data tool
        # print("\n Number of rows to be written into Spanner: " + str(len(list_of_objects)) + "\n")

        # extract values from dictionary objects in the list then convert each item to a tuple and store all items in a list
        list_to_load = [tuple(d.values()) for d in list_of_objects]

        # Sort id key in batches before load. further increase speed by using Threads.
        sorted_list = sorted(list_to_load, key=lambda k: k[0])

        return sorted_list


    # Divide sorted_list into batches of lists of 66 rows each and pass each of those into multiprocessor pool.map(
    # batching(),sorted_list)
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    batch_lists = list(chunks(get_sorted_list(), 66))

    def write_to_spanner(self, batches):
        with database.batch() as batch:
            batch.insert_or_update(
                table='LISTINGS',
                columns=self.columns,
                values=batches)

    def multithreaded_spanner_write(self):
        print("Number of sorted lists to be written to Spanner: ", len(self.batch_lists))
        t1 = time.time()
        # make the Pool of workers
        p = ThreadPool(4)
        result = p.map(self.write_to_spanner, self.batch_lists)
        print(result)
        p.close()
        p.join()
        load_time = "Time taken to load 10,000 rows into Spanner: " + time.time() - t1
        return load_time

    def create_table(self):
        table = SpannerTable()
        operation = self.database.update_ddl([table.table])
        print("Waiting for operation to complete...")
        try:
            result = operation.result()
            return result
        except Exception as e:
            logging.error(f"Received Error: {e}")

    def list_tables(self):
        with self.database.snapshot() as snapshot:
            try:
                results = snapshot.execute_sql(
                    "SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_schema = ''"
                )
                return results
            except Exception as e:
                print(f"Received Error: {e}")

            print("Tables in database: ")
            for row in results:
                print(row[0])
