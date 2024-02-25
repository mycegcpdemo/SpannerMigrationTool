import json
import os
from dotenv import load_dotenv
from faker import Faker
from faker.providers import BaseProvider
from faker.providers import address, date_time, company, python
from faker_schema.faker_schema import FakerSchema
from faker_schema.schema_loader import load_json_from_file


# create a date provider
class Provider(BaseProvider):
    def spanner_date(self):
        return '2019-02-02'


class OutputFile:
    load_dotenv()
    csv_file = os.getenv('CSV_LISTING')
    json_file = os.getenv('JSON_LISTING')
    faker_schema = os.getenv('FAKERSCHEMA')
    fake = Faker()
    # then add the new provider to faker instance
    fake.add_provider(Provider)
    fake.add_provider(address)
    fake.add_provider(date_time)
    fake.add_provider(company)
    fake.add_provider(python)
    fake.pyfloat(left_digits=None, right_digits=None, positive=True)
    # Load the Fake Schema so Faker knows how to generate the fake data
    schema = load_json_from_file(faker_schema)
    faker = FakerSchema(faker=fake)

    def create_fakedata_json(self):
        f = open(self.json_file, "w")

        # list to hold dictionary objects of REW data
        dict_list = []

        # Create how many rows your want
        i = 0
        while i < 10000:
            data = self.faker.generate_fake(self.schema)
            dict_list.append(data)
            i = i + 1

        f.write(json.dumps(dict_list))
        f.close()
    def create_fakedata_csv(self):
        # How to create a Comma seperated CSV:
        f = open(self.csv_file, "w")
        i = 0
        while i < 100:
            data = self.faker.generate_fake(self.schema)
            for k, v in data.items():
                if (isinstance(v, int)):
                    f.write(str(v) + ", ")
                elif (isinstance(v, float)):
                    f.write(str(v) + ", ")
                else:
                    # f.write('"' + str(v) + '"' + ", ")
                    f.write(str(v) + ", ")

            f.write("\n")
            i = i + 1
        f.close()
