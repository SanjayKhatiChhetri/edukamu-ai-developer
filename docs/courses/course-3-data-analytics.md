---
title: "Course 3: Exploring Data and Analytics"
layout: default
nav_order: 5
parent: Courses
---

# Course 3: Exploring Data and Analytics

**URL:** [https://cs.edukamu.fi/exploring-data-and-analytics](https://cs.edukamu.fi/exploring-data-and-analytics)  
**Sections:** 12  

---

## Table of Contents

- **Unit 1:** Data Roles And Services | Databases And Processing | Identifying Data
- **Unit 2:** Adopting Cloud Services | Exploring Non Relational Data | Exploring Relational Data ...
- **Unit 3:** Data Visualization | Large Scale Analytics | Real Time Analytics ...

---

## Unit 1

### Data Roles And Services

**TL;DR:** In today's digital age information is power, and professionals skilled in harnessing and interpreting data are in high demand across diverse industries.

**Topics covered:**
- The Rise of Data-Driven Jobs
- 1. Data as a Strategic Asset
- 2. Technological Advancements
- 3. Digital Transformation
- 4. Emergence of Data Governance and Security
- Elisa: Career in the World of Data
- Data-Driven Jobs and Roles
- 1. Database Administrators
- 2. Data Engineers
- 3. Data Analysts

**Key Terms:**

| Term | Definition |
|------|-----------|
| Database administrators | manage databases, assigning permissions to users, storing backup copies of data and restore data in the event of a failure. |
| Data engineers | manage infrastructure and processes for data integration across the organization, applying data cleaning routines, identifying data governance rules, and implementing pipelines to... |
| Data analysts | explore and analyze data to create visualizations and charts that enable organizations to make informed decisions. |
| Note | The roles described here represent the key data-related roles found in most medium to large organizations. There are additional data-related roles not mentioned here, such as... |
| Azure SQL Database | a fully managed platform-as-a-service (PaaS) database hosted in Azure |
| Azure SQL Managed Instance | a hosted instance of SQL Server with automated maintenance, which allows more flexible configuration than Azure SQL DB but with more administrative responsibility for the owner. |
| Azure SQL VM | a virtual machine with an installation of SQL Server, allowing maximum configurability with full management responsibility. |
| Azure Database for MySQL | a simple-to-use open-source database management system that is commonly used in *Linux*, *Apache*, *MySQL*, and *PHP* (LAMP) stack apps. |
| Azure Database for MariaDB | a newer database management system, created by the original developers of MySQL. The database engine has since been rewritten and optimized to improve performance. MariaDB offers... |
| Azure Database for PostgreSQL | a hybrid relational-object database. You can store data in relational tables, but a PostgreSQL database also enables you to store custom data types, with their own non-relational... |

**Key Points:**
- Database administrators manage databases, assigning permissions to users, storing backup copies of data and restore data in the event of a failure.
- Data engineers manage infrastructure and processes for data integration across the organization, applying data cleaning routines, identifying data governance rules, and implementing pipelines to...
- Data analysts explore and analyze data to create visualizations and charts that enable organizations to make informed decisions.
- Azure SQL Database – a fully managed platform-as-a-service (PaaS) database hosted in Azure
- Azure SQL Managed Instance – a hosted instance of SQL Server with automated maintenance, which allows more flexible configuration than Azure SQL DB but with more administrative responsibility for the...
- Azure SQL VM – a virtual machine with an installation of SQL Server, allowing maximum configurability with full management responsibility.
- Azure Database for MySQL - a simple-to-use open-source database management system that is commonly used in *Linux*, *Apache*, *MySQL*, and *PHP* (LAMP) stack apps.
- Azure Database for MariaDB - a newer database management system, created by the original developers of MySQL. The database engine has since been rewritten and optimized to improve performance....

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Databases And Processing

**TL;DR:** Do you like books? If you do, you probably visit book shops or libraries on a regular basis. They’re both quite handy, since filling the world with books makes no sense if there’s no way of easily handling, storing, and finding the books you like – and thus using the knowledge hidden within them.

**Topics covered:**
- Introduction to Databases
- Relational Databases
- Non-relational Databases
- Transactional Data Processing
- Analytical Data Processing
- Exercises: Databases and Processing

**Key Terms:**

| Term | Definition |
|------|-----------|
| 1. Key-value databases | in which each record consists of a unique key and an associated value, which can be in any format. |
| Atomicity | each transaction is treated as a single unit, which succeeds completely or fails completely. For example, a transaction that involved debiting funds from one account and crediting... |
| Consistency | transactions can only take the data in the database from one valid state to another. To continue the debit and credit example above, the completed state of the transaction must... |
| Isolation | concurrent transactions cannot interfere with one another, and must result in a consistent database state. For example, while the transaction to transfer funds from one account to... |
| Durability | when a transaction has been committed, it will remain committed. After the account transfer transaction has completed, the revised account balances are persisted so that even if... |
| Volume and Complexity | Analytical processing typically deals with large volumes of data and involves complex queries. Transactional processing, while still handling data, focuses on managing individual... |
| Purpose | Analytical processing aims to extract insights and support decision-making based on historical data. Transactional processing ensures the consistency and reliability of data in... |

**Key Points:**
- Atomicity – each transaction is treated as a single unit, which succeeds completely or fails completely. For example, a transaction that involved debiting funds from one account and crediting the...
- Consistency – transactions can only take the data in the database from one valid state to another. To continue the debit and credit example above, the completed state of the transaction must reflect...
- Isolation – concurrent transactions cannot interfere with one another, and must result in a consistent database state. For example, while the transaction to transfer funds from one account to another...
- Durability – when a transaction has been committed, it will remain committed. After the account transfer transaction has completed, the revised account balances are persisted so that even if the...
- Data scientists might work directly with data files in a data lake to explore and model data.
- Data Analysts might query tables directly in the data warehouse to produce complex reports and visualizations.
- Business users might consume pre-aggregated data in an analytical model in the form of reports or dashboards.
- Volume and Complexity: Analytical processing typically deals with large volumes of data and involves complex queries. Transactional processing, while still handling data, focuses on managing...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Identifying Data

**TL;DR:** <edukamu-video content="/videos/devai-3-unit1-video.yaml"/>
<br>

**Topics covered:**
- Why is Data so Important?
- 1. E-Commerce Insights
- 2. Healthcare Analytics
- 3. Smart Cities and IoT
- 4. Social Media Engagement
- 5. Financial Decision-Making
- How to Classify Data?
- 1. Structured Data
- 2. Semi-structured Data
- 3. Unstructured Data

**Key Terms:**

| Term | Definition |
|------|-----------|
| Note | JSON is just one of many ways in which semi-structured data can be represented. The point here is not to provide a detailed examination of JSON syntax, but rather to illustrate... |

**Key Points:**
- The type of data being stored (structured, semi-structured, or unstructured).
- The applications and services that will need to read, write, and process the data.
- The need for the data files to be readable by humans, or optimized for efficient storage and processing.
- *Avro* is a row-based format. It was created by Apache. Each record contains a header that describes the structure of the data in the record. This header is stored as JSON. The data is stored as...
- *ORC* (Optimized Row Columnar format) organizes data into columns rather than rows. It was developed by HortonWorks for optimizing read and write operations in Apache Hive (Hive is a data warehouse...
- *Parquet* is another columnar data format. It was created by Cloudera and Twitter. A Parquet file contains row groups. Data for each column is stored together in the same row group. Each row group...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 2

### Adopting Cloud Services

**TL;DR:** Microsoft Azure is full of cutting-edge services that facilitate smooth, efficient operations for companies of all sizes and specializations. But what about those who are not used to working online – let alone relying on cloud services?

**Topics covered:**
- Introduction to Azure SQL Database Managed Instance
- Use Cases
- Business Benefits
- Introduction to Azure SQL Database
- 1. Single Database
- 2. Elastic Pool
- Use Cases
- Business Benefits
- Azure Services for Open-source Databases
- Azure Database for MySQL

**Key Terms:**

| Term | Definition |
|------|-----------|
| Note | A SQL Database server is a logical construct that acts as a central administrative point for multiple single or pooled databases, logins, firewall rules, auditing rules, threat... |
| Note | You can use the Data Migration Assistant to detect compatibility issues with your databases that can impact database functionality in Azure SQL Database. |
| Note | If you are not familiar with the services described above, there's no need to worry. You can still review the materials below, but we won't be using the three during this course. |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |

**Key Points:**
- Modern cloud applications that need to use the latest stable SQL Server features.
- Applications that require high availability.
- Systems with a variable load that need the database server to scale up and down quickly.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Exploring Non Relational Data

**TL;DR:** After digging deep into the realms of relational data, it's essential to recognize that not all data conforms to the tidy rows and columns we've come to associate with traditional databases.

**Topics covered:**
- YRITYS: Scenarios from Real Life
- Introduction to Azure Blob Storage
- Introduction to Azure Data Lake Storage Gen2
- Introduction to Azure Files
- Introduction to Azure Tables
- Practice: Explore Azure Storage
- Exercise: Non-relational Data

**Key Terms:**

| Term | Definition |
|------|-----------|
| Hierarchical Namespace | option of an Azure Storage account. You can do this when initially creating the storage account, or you can upgrade an existing Azure Storage account to support Data Lake Gen2. Be... |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |

**Key Points:**
- Block blobs. A block blob is handled as a set of blocks. Each block can vary in size, up to 4000 MiB. A block blob can contain up to 190.7 TiB (4000 MiB X 50,000 blocks), giving a maximum size of...
- Page blobs. A page blob is organized as a collection of fixed size 512-byte pages. A page blob is optimized to support random read and write operations; you can fetch and store data for a single page...
- Append blobs. An append blob is a block blob optimized to support append operations. You can only add blocks to the end of an append blob; updating or deleting existing blocks isn't supported. Each...
- *The Hot tier* is the default. You use this tier for blobs that are accessed frequently. The blob data is stored on high-performance media.
- *The Cool tier* has lower performance and incurs reduced storage charges compared to the Hot tier. Use the Cool tier for data that is accessed infrequently. It's common for newly created blobs to be...
- The *Archive* tier provides the lowest storage cost, but with increased latency. The Archive tier is intended for historical data that mustn't be lost, but is required only rarely. Blobs in the...
- Your data landscape involves complex analytics workloads that require advanced features.
- Fine-grained access control is essential for compliance and security.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Exploring Relational Data

**TL;DR:** <edukamu-video content="/videos/devai-3-unit2-video.yaml"/>
<br>

**Topics covered:**
- Two Types of Data
- Relational Data: A Structured Foundation
- Non-Relational Data: Embracing Diversity
- Understanding Relational Data
- Schemas and Data
- Relational Data and Normalization
- Scenario: Improving Data Processing
- 1. Views
- 2. Stored Procedures
- 3. Indexes

**Key Terms:**

| Term | Definition |
|------|-----------|
| Relational Data | * **Structure**: Organized into tables with predefined schema. |
| Schema | Strict and fixed structure, enforced by the database. |
| Relationships | Emphasizes relationships between tables using primary and foreign keys. |
| Query Language | Utilizes SQL (Structured Query Language) for data manipulation. |
| Examples | MySQL, PostgreSQL, Microsoft SQL Server. |
| Non-relational Data | * **Structure**: Diverse structures, including key-value pairs, documents, columns, or graphs. |
| Schema | Flexible, dynamic, and may vary within the dataset. |
| Relationships | Relationships are often implicit, with no strict dependencies. |
| Query Language | NoSQL databases use varied query languages, not necessarily SQL. |
| Examples | MongoDB (document store), Cassandra (column-family store), Redis (key-value store). |

**Key Points:**
- Structure: Organized into tables with predefined schema.
- Schema: Strict and fixed structure, enforced by the database.
- Relationships: Emphasizes relationships between tables using primary and foreign keys.
- Query Language: Utilizes SQL (Structured Query Language) for data manipulation.
- Examples: MySQL, PostgreSQL, Microsoft SQL Server.
- Structure: Diverse structures, including key-value pairs, documents, columns, or graphs.
- Schema: Flexible, dynamic, and may vary within the dataset.
- Relationships: Relationships are often implicit, with no strict dependencies.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Fundamentals Of Azure Cosmos Db

**TL;DR:** Microsoft Azure contains numerous services for handling all kinds of data in every imaginable scenario, as you've noticed. But when we're talking about global enterprises that serve large numbers of customers, we need something special. Something that is capable of handling tremendous amounts of data and moving it effectively around the globe.

**Topics covered:**
- Introduction to Azure Cosmos DB
- When to use Cosmos DB?
- Azure Cosmos DB for NoSQL
- Azure Cosmos DB for MongoDB
- Azure Cosmos DB for PostgreSQL
- Azure Cosmos DB for Table
- Azure Cosmos DB for Apache Cassandra
- Azure Cosmos DB for Apache Gremlin
- 1. Multi-Model Flexibility
- 2. Automatic Scaling

**Key Terms:**

| Term | Definition |
|------|-----------|
| Note | Just a reminder; an API is an Application Programming Interface. Database management systems (and other software frameworks) provide a set of APIs that developers can use to write... |
| find | method to query the **products** collection in the **db** object: |
| Employees | table like this: |
| find | method to query the **products** collection in the **db** object: |
| Employees | table like this: |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |

**Key Points:**
- *IoT and telematics*. These systems typically ingest large amounts of data in frequent bursts of activity. Cosmos DB can accept and store this information quickly. The data can then be used by...
- *Retail and marketing*. Microsoft uses Cosmos DB for its own e-commerce platforms that run as part of Windows Store and Xbox Live. It's also used in the retail industry for storing catalog data and...
- *Gaming*. The database tier is a crucial component of gaming applications. Modern games perform graphical processing on mobile/console clients, but rely on the cloud to deliver customized and...
- *Web and mobile applications*. Azure Cosmos DB is commonly used within web and mobile applications, and is well suited for modeling social interactions, integrating with third-party services, and for...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Relational Databases In Azure

**TL;DR:** In a world filled with data, everything needs to be kept tidy and secure, stored in an orderly manner. Luckily, Microsoft Azure provides a powerful platform for managing and leveraging relational databases.

**Topics covered:**
- Introduction to Azure SQL
- 1. DDL Statements
- 2. DCL Statements
- 3. DML Statements
- Azure SQL Capabilities
- Comparing Azure SQL Services
- SQL Server and Azure Virtual Machines
- Exercise: Introduction to Relational Databases

**Key Terms:**

| Term | Definition |
|------|-----------|
| DROP | to accomplish almost everything that you need to do with a database. Although these SQL statements are part of the SQL standard, many database management systems also have their... |
| Note | The SQL code examples in this course are based on the Transact-SQL dialect, unless otherwise indicated. The syntax for other dialects is generally similar but may vary in some... |
| Warning | The DROP statement is very powerful. When you drop a table, all the rows in that table are lost. Unless you have a backup, you won't be able to retrieve this data. |
| Note | Columns marked as NOT NULL are referred to as mandatory columns. If you omit the NOT NULL clause, you can create rows that don't contain a value in the column. An empty column in... |
| Warning | SQL doesn't provide are you sure? prompts, so be careful when using DELETE or UPDATE without a WHERE clause because you can lose or modify a lot of data. |
| Customer | table where the **City** column value is "Seattle": |
| ORDER BY | clause. The data will be sorted by the specified column: |
| JOIN | clause. Joins indicate how the rows in one table are connected with rows in the other to determine what data to return. A typical join condition matches a foreign key from one... |
| Customer | and **Order** tables. The query makes use of table *aliases* to abbreviate the table names when specifying which columns to retrieve in the **SELECT** clause and which columns to... |
| Address | column in the **Customer** table for rows that have the value 1 in the **ID** column. All other rows are left unchanged: |

**Key Points:**
- *Transact-SQL (T-SQL)*. This version of SQL is used by Microsoft SQL Server and Azure SQL services.
- *pgSQL*. This is the dialect, with extensions implemented in PostgreSQL.
- *PL/SQL*. This is the dialect used by Oracle. PL/SQL stands for Procedural Language/SQL.
- Data Definition Language (DDL)
- Data Manipulation Language (DML)
- SQL Server on Azure Virtual Machines (VMs) - A virtual machine running in Azure with an installation of SQL Server. The use of a VM makes this option an infrastructure-as-a-service (IaaS) solution...
- Azure SQL Managed Instance - A platform-as-a-service (PaaS) option that provides near-100% compatibility with on-premises SQL Server instances while abstracting the underlying hardware and operating...
- Azure SQL Database - A fully managed, highly scalable PaaS database service that is designed for the cloud. This service includes the core database-level capabilities of on-premises SQL Server, and...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 3

### Data Visualization

**TL;DR:** Now that we've explored the foundations of data analytics, it's time to focus on a crucial aspect that transforms raw insights into comprehensible narratives: data visualization. While data analytics empowers us to uncover patterns and trends, data visualization is the art of presenting this information visually, making complex data more accessible...

**Topics covered:**
- Elisa: Career in the World of Data
- Basic Principles of Data Visualization
- Introduction to Microsoft Power BI
- Data Modeling
- Tables and Schema
- Attribute Hierarchies
- Data Visualizations
- Tables and Text
- Bar and Column Charts
- Line Charts

**Key Terms:**

| Term | Definition |
|------|-----------|
| Clarity and Simplicity | * **Principle**: Keep it simple. Avoid unnecessary complexity that can confuse the audience. |
| Why it matters | Simplicity enhances understanding, ensuring that the audience quickly grasps the intended message without being overwhelmed by intricate details. |
| Principle | Tailor visualizations to your audience's expertise and interests. |
| Why it matters | Different people and customers have varying levels of technical proficiency, so aligning visualizations with their needs ensures maximum impact. |
| Principle | Choose the right type of visualization for the data being presented. |
| Why it matters | Different types of data (e.g., trends, comparisons, distributions) are best represented using specific visual elements (e.g., line charts, bar graphs, pie charts). |
| Principle | Use color purposefully to highlight key points or trends. |
| Why it matters | Well-chosen colors can draw attention to critical information, aiding in the interpretation of the data. |
| Principle | Incorporate interactive elements for user engagement. |
| Why it matters | Interactive dashboards allow users to explore data on their own, fostering a deeper understanding and facilitating more informed decisions. |

**Key Points:**
- Principle: Tailor visualizations to your audience's expertise and interests.
- Why it matters: Different people and customers have varying levels of technical proficiency, so aligning visualizations with their needs ensures maximum impact.
- Principle: Choose the right type of visualization for the data being presented.
- Why it matters: Different types of data (e.g., trends, comparisons, distributions) are best represented using specific visual elements (e.g., line charts, bar graphs, pie charts).
- Principle: Use color purposefully to highlight key points or trends.
- Why it matters: Well-chosen colors can draw attention to critical information, aiding in the interpretation of the data.
- Principle: Incorporate interactive elements for user engagement.
- Why it matters: Interactive dashboards allow users to explore data on their own, fostering a deeper understanding and facilitating more informed decisions.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Large Scale Analytics

**TL;DR:** <edukamu-video content="/videos/devai-3-unit3-video.yaml"/>
<br>

**Topics covered:**
- Introduction to Large-scale Analytics
- Scenario: Data and AI
- Data Warehousing Architecture
- Data Ingestion Pipelines
- Analytical Data Stores
- Data Warehouses
- Data Lakehouses
- Platform-as-a-service Solutions (PaaS)
- 1. Azure Synapse Analytics
- 2. Azure Databricks

**Key Terms:**

| Term | Definition |
|------|-----------|
| Data ingestion and processing | data from one or more transactional data stores, files, real-time streams, or other sources is loaded into a data lake or a relational data warehouse. The load operation usually... |
| Analytical data store | data stores for large scale analytics include relational *data warehouses*, filesystem based *data lakes*, and hybrid architectures that combine features of data warehouses and... |
| Analytical data model | while data analysts and data scientists can work with the data directly in the analytical data store, it’s common to create one or more data models that pre-aggregate the data to... |
| Data visualization | data analysts consume data from analytical models, and directly from analytical stores to create reports, dashboards, and other visualizations. Additionally, users in an... |
| Note | Each of these services can be thought of as an analytical data store, in the sense that they provide a schema and interface through which the data can be queried. In many cases... |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. |

**Key Points:**
- An extensive range of deeply integrated analytics in the industry.
- Shared experiences across experiences that are familiar and easy to learn.
- Developers can easily access and reuse all assets.
- A unified data lake that allows you to retain the data where it is while using your preferred analytics tools.
- Centralized administration and governance across all experiences.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Real Time Analytics

**TL;DR:** When developing effective business models in the digital age, data analytics is the key to success and improvement. In the fast-paced landscape of data-driven decision-making, however, traditional large-scale analytics faces challenges in keeping up with the need for instant insights. At times, we need something different, something dynamic and res...

**Topics covered:**
- Large-scale vs. Real-time
- Key Differences
- Batch and Stream Processing
- Batch Processing
- Stream Processing
- Understanding the Difference
- Combining Batch and Stream Processing
- Understanding Stream Processing Architecture
- Real-time analytics in Azure
- Sources for Stream Processing

**Key Terms:**

| Term | Definition |
|------|-----------|
| Time Sensitivity | * Large-Scale Analytics: Primarily concerned with processing historical data in batches |
| Processing Paradigm | * Large-Scale Analytics: Relies on batch processing, suitable for complex queries and comprehensive reports |
| Use Cases | * Large-Scale Analytics: Ideal for in-depth trend analysis, historical reporting, and business intelligence |
| Data Freshness | * Large-Scale Analytics: Provides insights based on historical snapshots |
| Azure Stream Analytics | A platform-as-a-service (PaaS) solution that you can use to define *streaming jobs* that ingest data from a streaming source, apply a perpetual query, and write the results to an... |
| Spark Structured Streaming | An open-source library that enables you to develop complex streaming solutions on Apache Spark based services, including **Azure Synapse Analytics**, **Azure Databricks**, and... |
| Azure Data Explorer | A high-performance database and analytics service that is optimized for ingesting and querying batch or streaming data with a time-series element, and which can be used as a... |
| Azure Event Hubs | A data ingestion service that you can use to manage queues of event data, ensuring that each event is processed in order, exactly once. |
| Azure IoT Hub | A data ingestion service that is similar to Azure Event Hubs, but which is optimized for managing event data from *Internet-of-things* (IoT) devices. |
| Azure Data Lake Store Gen 2 | A highly scalable storage service that is often used in *batch processing* scenarios, but which can also be used as a source of streaming data. |

**Key Points:**
- Large-Scale Analytics: Relies on batch processing, suitable for complex queries and comprehensive reports
- Real-Time Analytics: Embraces streaming processing, allowing for immediate insights and rapid decision-making
- Large-Scale Analytics: Ideal for in-depth trend analysis, historical reporting, and business intelligence
- Real-Time Analytics: Suitable for scenarios demanding instant response, such as fraud detection, IoT applications, and dynamic pricing
- Large-Scale Analytics: Provides insights based on historical snapshots
- Real-Time Analytics: Offers a real-time view of the current state, enabling proactive decision-making
- *Batch processing*, in which multiple data records are collected and stored before being processed together in a single operation.
- *Stream processing*, in which a source of data is constantly monitored and processed in real time as new data events occur.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Summary

**TL;DR:** Congratulations on reaching the summary of the Exploring Microsoft Azure course!

**Topics covered:**
- Conversation: Representing the World with Azure
- Unit 1: Foundational Data Concepts
- Unit 2: Relational and Non-relational Data
- Unit 3: Data Analytics in Azure
- Course Feedback

**Key Points:**
- What is data and why is it important?
- What are the main purposes of databases?
- What are some main job roles associated directly with data?
- How would you describe relational and non-relational data?
- Which tools does Microsoft Azure offer for handling databases?
- What are the core functions of Azure Cosmos DB?
- What is the difference between large-scale and real-time analytics?
- What aspects should businesses consider when choosing data analytics methods?

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Quick-Reference Glossary

| Term | Definition | Section |
|------|-----------|---------|
| Database administrators | manage databases, assigning permissions to users, storing backup copies of data and restore data in the event of a failure. | Data Roles And Services |
| Data engineers | manage infrastructure and processes for data integration across the organization, applying data cleaning routines, identifying data governance rules, and implementing pipelines to... | Data Roles And Services |
| Data analysts | explore and analyze data to create visualizations and charts that enable organizations to make informed decisions. | Data Roles And Services |
| Note | The roles described here represent the key data-related roles found in most medium to large organizations. There are additional data-related roles not mentioned here, such as... | Data Roles And Services |
| Azure SQL Database | a fully managed platform-as-a-service (PaaS) database hosted in Azure | Data Roles And Services |
| Azure SQL Managed Instance | a hosted instance of SQL Server with automated maintenance, which allows more flexible configuration than Azure SQL DB but with more administrative responsibility for the owner. | Data Roles And Services |
| Azure SQL VM | a virtual machine with an installation of SQL Server, allowing maximum configurability with full management responsibility. | Data Roles And Services |
| Azure Database for MySQL | a simple-to-use open-source database management system that is commonly used in *Linux*, *Apache*, *MySQL*, and *PHP* (LAMP) stack apps. | Data Roles And Services |
| Azure Database for MariaDB | a newer database management system, created by the original developers of MySQL. The database engine has since been rewritten and optimized to improve performance. MariaDB offers... | Data Roles And Services |
| Azure Database for PostgreSQL | a hybrid relational-object database. You can store data in relational tables, but a PostgreSQL database also enables you to store custom data types, with their own non-relational... | Data Roles And Services |
| 1. Key-value databases | in which each record consists of a unique key and an associated value, which can be in any format. | Databases And Processing |
| Atomicity | each transaction is treated as a single unit, which succeeds completely or fails completely. For example, a transaction that involved debiting funds from one account and crediting... | Databases And Processing |
| Consistency | transactions can only take the data in the database from one valid state to another. To continue the debit and credit example above, the completed state of the transaction must... | Databases And Processing |
| Isolation | concurrent transactions cannot interfere with one another, and must result in a consistent database state. For example, while the transaction to transfer funds from one account to... | Databases And Processing |
| Durability | when a transaction has been committed, it will remain committed. After the account transfer transaction has completed, the revised account balances are persisted so that even if... | Databases And Processing |
| Volume and Complexity | Analytical processing typically deals with large volumes of data and involves complex queries. Transactional processing, while still handling data, focuses on managing individual... | Databases And Processing |
| Purpose | Analytical processing aims to extract insights and support decision-making based on historical data. Transactional processing ensures the consistency and reliability of data in... | Databases And Processing |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... | Adopting Cloud Services |
| Hierarchical Namespace | option of an Azure Storage account. You can do this when initially creating the storage account, or you can upgrade an existing Azure Storage account to support Data Lake Gen2. Be... | Exploring Non Relational Data |
| Relational Data | * **Structure**: Organized into tables with predefined schema. | Exploring Relational Data |
| Schema | Strict and fixed structure, enforced by the database. | Exploring Relational Data |
| Relationships | Emphasizes relationships between tables using primary and foreign keys. | Exploring Relational Data |
| Query Language | Utilizes SQL (Structured Query Language) for data manipulation. | Exploring Relational Data |
| Examples | MySQL, PostgreSQL, Microsoft SQL Server. | Exploring Relational Data |
| Non-relational Data | * **Structure**: Diverse structures, including key-value pairs, documents, columns, or graphs. | Exploring Relational Data |
| find | method to query the **products** collection in the **db** object: | Fundamentals Of Azure Cosmos Db |
| Employees | table like this: | Fundamentals Of Azure Cosmos Db |
| DROP | to accomplish almost everything that you need to do with a database. Although these SQL statements are part of the SQL standard, many database management systems also have their... | Relational Databases In Azure |
| Warning | The DROP statement is very powerful. When you drop a table, all the rows in that table are lost. Unless you have a backup, you won't be able to retrieve this data. | Relational Databases In Azure |
| Customer | table where the **City** column value is "Seattle": | Relational Databases In Azure |
| ORDER BY | clause. The data will be sorted by the specified column: | Relational Databases In Azure |
| JOIN | clause. Joins indicate how the rows in one table are connected with rows in the other to determine what data to return. A typical join condition matches a foreign key from one... | Relational Databases In Azure |
| Address | column in the **Customer** table for rows that have the value 1 in the **ID** column. All other rows are left unchanged: | Relational Databases In Azure |
| Clarity and Simplicity | * **Principle**: Keep it simple. Avoid unnecessary complexity that can confuse the audience. | Data Visualization |
| Why it matters | Simplicity enhances understanding, ensuring that the audience quickly grasps the intended message without being overwhelmed by intricate details. | Data Visualization |
| Principle | Tailor visualizations to your audience's expertise and interests. | Data Visualization |
| Data ingestion and processing | data from one or more transactional data stores, files, real-time streams, or other sources is loaded into a data lake or a relational data warehouse. The load operation usually... | Large Scale Analytics |
| Analytical data store | data stores for large scale analytics include relational *data warehouses*, filesystem based *data lakes*, and hybrid architectures that combine features of data warehouses and... | Large Scale Analytics |
| Analytical data model | while data analysts and data scientists can work with the data directly in the analytical data store, it’s common to create one or more data models that pre-aggregate the data to... | Large Scale Analytics |
| Data visualization | data analysts consume data from analytical models, and directly from analytical stores to create reports, dashboards, and other visualizations. Additionally, users in an... | Large Scale Analytics |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. | Large Scale Analytics |
| Time Sensitivity | * Large-Scale Analytics: Primarily concerned with processing historical data in batches | Real Time Analytics |
| Processing Paradigm | * Large-Scale Analytics: Relies on batch processing, suitable for complex queries and comprehensive reports | Real Time Analytics |
| Use Cases | * Large-Scale Analytics: Ideal for in-depth trend analysis, historical reporting, and business intelligence | Real Time Analytics |
| Data Freshness | * Large-Scale Analytics: Provides insights based on historical snapshots | Real Time Analytics |
| Azure Stream Analytics | A platform-as-a-service (PaaS) solution that you can use to define *streaming jobs* that ingest data from a streaming source, apply a perpetual query, and write the results to an... | Real Time Analytics |
| Spark Structured Streaming | An open-source library that enables you to develop complex streaming solutions on Apache Spark based services, including **Azure Synapse Analytics**, **Azure Databricks**, and... | Real Time Analytics |
| Azure Data Explorer | A high-performance database and analytics service that is optimized for ingesting and querying batch or streaming data with a time-series element, and which can be used as a... | Real Time Analytics |
| Azure Event Hubs | A data ingestion service that you can use to manage queues of event data, ensuring that each event is processed in order, exactly once. | Real Time Analytics |
| Azure IoT Hub | A data ingestion service that is similar to Azure Event Hubs, but which is optimized for managing event data from *Internet-of-things* (IoT) devices. | Real Time Analytics |
| Azure Data Lake Store Gen 2 | A highly scalable storage service that is often used in *batch processing* scenarios, but which can also be used as a source of streaming data. | Real Time Analytics |

---

*Auto-generated by `generate_diary.py` — re-run to refresh after re-scraping.*
