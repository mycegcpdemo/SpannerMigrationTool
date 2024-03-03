# Load data into Spanner in a multithreading manner

## TL;DR
This Python application writes data into Spanner and makes use of google.cloud Spanner, multiprocessing.dummy, time and 
json libraries to read data from a JSON file containing the list of objects mentioned above and writing it to Spanner in 
a multi threaded batch fashion.Testing data was generated using the python libraries Faker and Faker-Schema.  
A “Faker Schema” was created using the Client provided SQL schema using the exact / approximate data types for instance 
TimeStamp/Date types were replaced with Date type in order to facilitate a speedily resolution to this issue. 
All other data types remain the same.  Faker Generated a list of 10,000 dictionary objects each representing a row in 
Client’s table with 295 columns.


## Best practices for loading data into Spanner

### Key terminologies to be aware of:

Partitions refers to the number of batches you separate your data into before loading. Less partitions the better.

A Mutation represents a sequence of inserts, updates, deletes, and so on that can be applied atomically to different rows and tables in a Cloud Spanner database. Max number of mutations per batch is 20,000.  It is key to Note that even though an insert is typically thought of as 1 mutation this is not true. It is the number of inserts times the number of columns. 
So for Real Estate Webmaster One insert counts as 295 mutation. Therefore Max number of inserts per batch for REW’s workload is 66 inserts or less.

A Batch object is a container for mutation operations. 

Interleaved table is a table that you declare to be a child of another table because you want the rows of the child table to be physically stored together with the associated parent row. As mentioned above, the prefix of the primary key of a child table must be the primary key of the parent table.

### Performance guidelines for bulk loading:

You can achieve optimal bulk loading performance by following a few guidelines:

Minimize the number of splits that are involved in each write transaction. Performance is maximized because write throughput is maximized when fewer splits are involved in a transaction.

Maximize the use of partitioning to distribute writing the partitions across worker tasks.

Cloud Spanner uses load-based splitting to evenly distribute your data load across nodes. After a few minutes of high load, Cloud Spanner introduces split boundaries between rows of non-interleaved tables. In general, if your data load is well-distributed and you follow best practices for schema design and bulk loading, your write throughput should double every few minutes until you saturate the available CPU resources in your instance.

Partition your data by primary key
To get optimal write throughput for bulk loads, partition your data by primary key with this pattern:
Each partition contains a range of consecutive rows, as determined by the key columns.
Each commit contains data for only a single partition.
We recommend that the number of partitions be 10 times the number of nodes in your Cloud Spanner instance. 

To assign rows to partitions:
- Sort your data by primary key.
- Divide the data into 10 * (number of nodes) separate, equally sized partitions.
- Create and assign a separate worker task to each partition. Creating the worker tasks happens in your application. 

As you load data, Cloud Spanner creates and updates splits to balance the load on the nodes in your instance. During this process, you may experience temporary drops in throughput.

Example
You have a regional configuration with 3 nodes. You have 90,000 rows in a non-interleaved table. The primary keys in the table range from 1 to 90000.

Rows: 90,000 rows
Nodes: 3
Partitions: 10 * 3 = 30
Rows per partition: 90000 / 30 = 3000.
The first partition includes the key range 1 to 3000. The second partition includes the key range 3001 to 6000. The 30th partition includes the key range 87001 to 90000. (You should not use sequential keys in a large table.)

Each worker task sends the writes for a single partition. Within each partition, you should write the rows sequentially by primary key. Writing rows randomly, with respect to the primary key, should also provide reasonably high throughput. Measuring test runs will give you insight into which approach provides the best performance for your dataset.

### Migration from MySQL to Spanner - Solution Document
Link to our Solution document that goes in depth on how to migrate your OLTP MySQL database to Cloud Spanner:
https://cloud.google.com/solutions/migrating-mysql-to-spanner

## Solution explanation

Testing Data

Testing data was generated using the python libraries Faker and Faker-Schema.  A “Faker Schema” was created using the Client provided SQL schema using the exact / approximate data types for instance TimeStamp/Date types were replaced with Date type in order to facilitate a speedily resolution to this issue. All other data types remain the same.  Faker Generated a list of 10,000 dictionary objects each representing a row in Client’s table with 295 columns.

Writing Data to Spanner

The Python application that writes data into Spanner makes use of google.cloud Spanner, multiprocessing.dummy, time and json libraries to read data from a JSON file containing the list of objects mentioned above and writing it to Spanner in a multi-threaded batch fashion.  

Steps:
- The application reads in the entire list into memory, it creates a list of tuples where each tuple holds the values or a corresponding object.  
- This list of tuples is then sorted according the the primary key of the database, 
- Next it is divided into batches of mostly equal sizes based on the math calculated on the number of mutations allowed based on the number of rows we are attempting to load (Please refer to Key Terminologies section for definition/math). 
- A function is called in a multi-threaded  manner and passed two parameters:
  - First parameter:  a function that writes to the Spanner in batch mode
  - List of sorted batches of tuples each containing a row of data to be written




