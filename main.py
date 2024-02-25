from helper_classes.create_spanner_table import CreateSpannerTable
from helper_classes.generate_fake_data import OutputFile
from helper_classes.spanner_operations import SpannerOperations


# Create a json and csv files with fake data
# fake_data_json = OutputFile()
# fake_data_json.create_fakedata_json()
# fake_data_json.create_fakedata_csv()

# Create a table in Spanner database
# table = CreateSpannerTable()
# print(table.create_table())
table = SpannerOperations()
# table.create_table()

# verify that our table is created by listing the tables in the Spanner database
tables = table.list_tables()
print("Tables in database: ")
for row in tables:
    print(row[0])
