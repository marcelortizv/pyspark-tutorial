# Spark tutorial with pyspark

## Why learn Spark?
Spark is currently one of the most popular tools for big data analytics. 
You might have heard of other tools such as Hadoop. 
Hadoop is a slightly older technology although still in use by some companies.
Spark is generally faster than Hadoop, which is why Spark has become more 
popular over the last few years.

There are many other big data tools and systems, each with its own use case. For example,
there are database system like Apache Cassandra and SQL query engines like Presto. 
But Spark is still one of the most popular tools for analyzing large data sets.

Here is an outline of the topics we are covering in this lesson:

* What is big data?
* Review of the hardware behind big data
* Introduction to distributed systems
* Brief history of Spark and big data
* Common Spark use cases
* Other technologies in the big data ecosystem

### What is Big Data?

First of all, it is necessary to learn about four key hardware components. Understanding these
components helps determine whether you are working on a "big data" problem or if it's easier
to analyze the data locally on your own computer.

* CPU (Central Processing Unit)

The CPU is the "brain" of the computer. Every process on your computer is eventually 
handled by your CPU. This includes calculations and also instructions for the other 
components of the compute. It is 200x faster than memory

* Memory (RAM)

When your program runs, data gets temporarily stored in memory before getting sent to 
the CPU. Memory is ephemeral storage - when your computer shuts down, 
the data in the memory is lost. It is 15x faster than SSD.

* Storage (SSD or Magnetic Disk)

Storage is used for keeping data over long periods of time. When a program runs, 
the CPU will direct the memory to temporarily load data from long-term storage.
It is 20x faster than network.

* Network (LAN or the Internet)

Network is the gateway for anything that you need that isn't stored on your computer. 
The network could connect to other computers in the same room (a Local Area Network) or 
to a computer on the other side of the world, connected over the internet.

* Other Numbers to Know?

You may have noticed a few other numbers involving the L1 and L2 Cache, mutex locking, 
and branch mispredicts. 
 

So, the main bottleneck when you have a large dataset (already downloaded locally) is the
memory! If a dataset is larger than the size of your RAM, 
you might still be able to analyze the data on a single computer. By default, 
the Python pandas library will read in an entire dataset from disk into memory. 
If the dataset is larger than your computer's memory, the program won't work.

However, the Python pandas library can read in a file in smaller chunks. Thus, 
if you were going to calculate summary statistics about the dataset such as a 
sum or count, you could read in a part of the dataset at a time and accumulate 
the sum or count.

```python
with pd.read_csv("tmp.sv", sep="|", chunksize=4) as reader:
    reader
    for chunk in reader:
        print(chunk)
```

Therefore, this is why there is no simple definition for big data, but if you understand
the capabilities of your computer, then you can decide when you have a big data and when it 
makes sense to use Spark.

### How is Spark related to Hadoop?
Spark contains libraries for data analysis, machine learning, graph analysis, 
and streaming live data. Spark is generally faster than Hadoop. This is because 
Hadoop writes intermediate results to disk whereas Spark tries to keep intermediate 
results in memory whenever possible.

The Hadoop ecosystem includes a distributed file storage system called HDFS 
(Hadoop Distributed File System). Spark, on the other hand, does not include 
a file storage system. You can use Spark on top of HDFS but you do not have to. 
Spark can read in data from other sources as well such as Amazon S3.

MapReduce is a programming technique for manipulating large data sets. 
"Hadoop MapReduce" is a specific implementation of this programming technique.

The technique works by first dividing up a large dataset and distributing the 
data across a cluster. In the map step, each data is analyzed and converted into a 
(key, value) pair. Then these key-value pairs are shuffled across the cluster so that all keys are on the same machine. In the reduce step, the values with the same keys are combined together.

While Spark doesn't implement MapReduce, you can write Spark programs that behave 
in a similar way to the map-reduce paradigm.

### Spark Use Cases and Resources

Here are a few resources about different Spark use cases:

* Data Analytics
* Machine Learning
* Streaming
* Graph Analytics
