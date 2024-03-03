from helper_classes.generate_fake_data import OutputFile
from helper_classes.spanner_operations import SpannerOperations

# Create a json and csv files with fake data
fake_data_json = OutputFile()
fake_data_json.create_fakedata_json()
fake_data_json.create_fakedata_csv()

# Create a table in Spanner database
table = SpannerOperations()
table.create_table()

# verify that our table is created by listing the tables in the Spanner database
tables = table.list_tables()
print("Tables in database: ")
for row in tables:
    print(row[0])

# Divide sorted_list into batches of lists of 66 rows each
def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

sorted_list = table.get_sorted_list()
batches = list(chunks(sorted_list, 66))

# Use multithreading to write batches of 66 rows into a Spanner table in a timely fashion
# This approach takes on average 24 seconds to load 10,000 rows into a Spanner table.
result = table.multithreaded_spanner_write(batches)
print(result)

