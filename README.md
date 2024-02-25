# Load data into Spanner in a multithreading manner

## TL;DR
This Python application that writes data into Spanner makes use of google.cloud Spanner, multiprocessing.dummy, time and 
json libraries to read data from a JSON file containing the list of objects mentioned above and writing it to Spanner in 
a multi threaded batch fashion.Testing data was generated using the python libraries Faker and Faker-Schema.  
A “Faker Schema” was created using the Client provided SQL schema using the exact / approximate data types for instance 
TimeStamp/Date types were replaced with Date type in order to facilitate a speedily resolution to this issue. 
All other data types remain the same.  Faker Generated a list of 10,000 dictionary objects each representing a row in 
Client’s table with 295 columns.


Users would first need to export the MySQL database table contents as a csv file and then use this tool to import it into 
spanner in a multi threaded manner.



