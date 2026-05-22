## Databases and Processing

Do you like books? If you do, you probably visit book shops or libraries on a regular basis. They’re both quite handy, since filling the world with books makes no sense if there’s no way of easily handling, storing, and finding the books you like – and thus using the knowledge hidden within them.

Books and libraries are like data and databases. Just as a well-organized library enhances the accessibility of knowledge, effective data storage and management systems are crucial for harnessing the power of information in the digital world.

On this page, we’ll explore databases and data processing. Without them, countless innovations we take for granted today would never have happened!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Databases
</edukamu-collapse-hidden-title>

A database is used to define a central system in which data can be stored and queried. In a simplistic sense, the file system on which files are stored is a kind of database; but when we use the term in a professional data context, we usually mean a dedicated system for managing data records rather than files.

Usually, databases are divided into relational and non-relational databases. We’ll focus on them in the second unit, but let’s take this moment to get acquainted with them.

### Relational Databases

Relational databases are commonly used to store and query structured data. The data is stored in tables that represent entities, such as customers, products, or sales orders. Each instance of an entity is assigned a *primary key* that uniquely identifies it; and these keys are used to reference the entity instance in other tables.

For example, a customer's primary key can be referenced in a sales order record to indicate which customer placed the order. This use of keys to reference data entities enables a relational database to be *normalized*; which in part means the elimination of duplicate data values so that, for example, the details of an individual customer are stored only once; not for each sales order the customer places.

The tables are managed and queried using Structured Query Language (SQL), which is based on an ANSI standard, so it's similar across multiple database systems.

<edukamu-image url="/graphics/module1/relational-database.png" alt="Image showing a relational database schema."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

### Non-relational Databases

Non-relational databases are data management systems that don’t apply a relational schema to the data. Non-relational databases are often referred to as NoSQL database, even though some support a variant of the SQL language.

There are four common types of Non-relational database commonly in use.

**1. Key-value databases** in which each record consists of a unique key and an associated value, which can be in any format.

<edukamu-image url="/graphics/module1/key-value-store.png" alt="Image showing a key-value database."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

**2. Document databases**, which are a specific form of key-value database in which the value is a JSON document (which the system is optimized to parse and query)

<edukamu-image url="/graphics/module1/document-store.png" alt="Image showing a document database."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

**3. Column family databases**, which store tabular data comprising rows and columns, but you can divide the columns into groups known as column-families. Each column family holds a set of columns that are logically related together.

<edukamu-image url="/graphics/module1/column-family-store.png" alt="Image showing a column family database."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

**4. Graph databases**, which store entities as nodes with links to define relationships between them.

<edukamu-image url="/graphics/module1/graph.png" alt="Image showing a graph database."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Keep in mind that in a professional setting – such as the one we’re in right now – the term database refers to a system for managing data records rather than just a system on which files are stored.

This is an important point to keep in mind in order to avoid confusions later on. Instead of passive locations, like warehouses, databases should be thought of as networking stations in which information is shared and exchanged constantly.

And what happens in a network? Well, a lot of things, actually, but some kind of *transactions* or *analysis* always take place. That’s also true when talking about data processing, which is traditionally divided into *transactional* and *analytical*.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Transactional Data Processing
</edukamu-collapse-hidden-title>

A transactional data processing system is what most people consider the primary function of business computing. A transactional system records *transactions* that encapsulate specific events that the organization wants to track. A transaction could be financial, such as the movement of money between accounts in a banking system, or it might be part of a retail system, tracking payments for goods and services from customers. Think of a transaction as a small, discrete, unit of work.

Transactional systems are often high-volume, sometimes handling many millions of transactions in a single day. The data being processed has to be accessible very quickly. The work performed by transactional systems is often referred to as Online Transactional Processing (OLTP).

<edukamu-image url="/graphics/module1/transactional-processing.png" alt="Image showing a user reading and writing data in a database."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

OLTP solutions rely on a database system in which data storage is optimized for both read and write operations in order to support transactional workloads in which data records are created, retrieved, updated, and deleted (often referred to as *CRUD* operations). These operations are applied transactionally, in a way that ensures the integrity of the data stored in the database. To accomplish this, OLTP systems enforce transactions that support so-called ACID semantics:
* **Atomicity** – each transaction is treated as a single unit, which succeeds completely or fails completely. For example, a transaction that involved debiting funds from one account and crediting the same amount to another account must complete both actions. If either action can't be completed, then the other action must fail.
* **Consistency** – transactions can only take the data in the database from one valid state to another. To continue the debit and credit example above, the completed state of the transaction must reflect the transfer of funds from one account to the other.
* **Isolation** – concurrent transactions cannot interfere with one another, and must result in a consistent database state. For example, while the transaction to transfer funds from one account to another is in-process, another transaction that checks the balance of these accounts must return consistent results - the balance-checking transaction can't retrieve a value for one account that reflects the balance *before* the transfer, and a value for the other account that reflects the balance *after* the transfer.
* **Durability** – when a transaction has been committed, it will remain committed. After the account transfer transaction has completed, the revised account balances are persisted so that even if the database system were to be switched off, the committed transaction would be reflected when it is switched on again.

OLTP systems are typically used to support live applications that process business data - often referred to as *line of business* (LOB) applications.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Analytical Data Processing
</edukamu-collapse-hidden-title>

Analytical data processing typically uses read-only (or read-mostly) systems that store vast volumes of historical data or business metrics. Analytics can be based on a snapshot of the data at a given point in time, or a series of snapshots.

The specific details for an analytical processing system can vary between solutions, but a common architecture for enterprise-scale analytics looks like this:

<edukamu-image url="/graphics/module1/analytical-processing.png" alt="Diagram showing an analytical database architecture with the numbered elements described below."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

1. Operational data is extracted, transformed, and loaded (ETL) into a data lake for analysis.
2. Data is loaded into a schema of tables - typically in a Spark-based *data lakehouse* with tabular abstractions over files in the data lake, or a *data warehouse* with a fully relational SQL engine.
3. Data in the data warehouse may be aggregated and loaded into an online analytical processing (OLAP) model, or *cube*. Aggregated numeric values (*measures*) from fact tables are calculated for intersections of *dimensions* from dimension tables. For example, sales revenue might be totaled by date, customer, and product.
4. The data in the data lake, data warehouse, and analytical model can be queried to produce reports, visualizations, and dashboards.

*Data lakes* are common in large-scale data analytical processing scenarios, where a large volume of file-based data must be collected and analyzed.

*Data warehouses* are an established way to store data in a relational schema that is optimized for read operations – primarily queries to support reporting and data visualization. *Data Lakehouses* are a more recent innovation that combine the flexible and scalable storage of a data lake with the relational querying semantics of a data warehouse. The table schema may require some denormalization of data in an OLTP data source (introducing some duplication to make queries perform faster).

An OLAP model is an aggregated type of data storage that is optimized for analytical workloads. Data aggregations are across dimensions at different levels, enabling you to *drill up/down* to view aggregations at multiple hierarchical levels; for example to find total sales by region, by city, or for an individual address. Because OLAP data is pre-aggregated, queries to return the summaries it contains can be run quickly.

Different types of user might perform data analytical work at different stages of the overall architecture. For example:
* Data scientists might work directly with data files in a data lake to explore and model data.
* Data Analysts might query tables directly in the data warehouse to produce complex reports and visualizations.
* Business users might consume pre-aggregated data in an analytical model in the form of reports or dashboards.

</edukamu-collapse>
<br>


In essence, analytical and transactional data processing may seem quite similar, but there are a few key differences between the two. Consider the following:

* **Volume and Complexity**: Analytical processing typically deals with large volumes of data and involves complex queries. Transactional processing, while still handling data, focuses on managing individual transactions efficiently.
* **Purpose**: Analytical processing aims to extract insights and support decision-making based on historical data. Transactional processing ensures the consistency and reliability of data in real-time, supporting operational aspects of a system.

In essence, both types of data processing are crucial components of a comprehensive data strategy. Analytical processing looks back and dives deep into historical data for insights, while transactional processing keeps the wheels turning in real-time by managing the constant flow of transactions in a system. The choice between them depends on the specific goals and requirements of the task at hand.

In a digital society, we’re surrounded by technological marvels, even though we tend to take them for granted. Databases and processing are two such concepts; simple on the outside, quite complicated and varied on the inside!

Let’s review this all with an exercise.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercises: Databases and Processing
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/databases-and-processing-question-scroll.yaml" id="01153wq00e6d4306">
<br>

</edukamu-collapse>
<br>


Data is at the core of most software applications and solutions. It can be represented in many formats, stored in files and databases, and used to record transactions or to support analysis and reporting.

Data is the centerpiece of countless innovations, but the same principle also applies to numerous jobs. There are quite a few job roles that can only be fulfilled by those who have decided to become experts at handling data!

Next, we’ll find out how data could employ you too.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
