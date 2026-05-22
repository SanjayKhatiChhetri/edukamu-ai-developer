---
title: "Course 5: Cloud Native Data Storage"
layout: default
nav_order: 7
parent: Courses
---

# Course 5: Cloud Native Data Storage

**URL:** [https://cs.edukamu.fi/cloud-native-data-storage](https://cs.edukamu.fi/cloud-native-data-storage)  
**Sections:** 12  

---

## Table of Contents

- **Unit 1:** Components Of Cosmos Db For Nosql | Empowering Global Applications | Exploring Global Databases ...
- **Unit 2:** Azure Cosmos Db In Action | Implementing Nosql Solutions | Migrating Data ...
- **Unit 3:** Advanced Capabilities Of Azure Cosmos Db | Configuring The Sdk | Connecting To A Nosql Database ...

---

## Unit 1

### Components Of Cosmos Db For Nosql

**TL;DR:** In many modern applications, data needs to be handled and managed in real-time in order to provide a seamless, continuous user experience regardless of traffic or geographical location. NoSQL services, such as Azure Cosmos DB, enable developers to accomplish such feats, no matter how unbelievable they might seem.

**Topics covered:**
- Core Components of Azure Cosmos DB for NoSQL
- Accounts
- Databases
- Containers
- Items
- Partition & Partition Keys
- Basic Resources
- Accounts
- Databases
- Containers

**Key Terms:**

| Term | Definition |
|------|-----------|
| path | of /department/name, then the partition key **value** of this document would be information-technology. Behind the scenes, Azure Cosmos DB for NoSQL automatically manages the... |
| Reminder: | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |
| Note: | Only the options in the Basics tab are required to create an Azure Cosmos DB account. |
| Note: | A lab is essentially a virtual machine (VM) containing the client tools you need, along with the exercise instructions. |
| Tip: | Alternatively, if you would like to use a development environment on your own computer, you can use this <edukamu-link... |
| Note: | However, if you choose to provision throughput at the database level, configuring the database may require additional steps. This is explored deeper in other Azure Cosmos DB for... |
| Note: | JavaScript Object Notation (JSON) is an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of... |

**Key Points:**
- The globally unique name of your account.
- The location (Azure region) for the account.
- Capacity mode (provisioned throughput or serverless).
- A unique name for the container with the database
- The path for the partition key value
- *Optional*: provisioned throughput if not inferred from database provisioning.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Empowering Global Applications

**TL;DR:** In our modern, increasingly digital societies, endless amounts of data are being processed each day. As we've learned during the earlier courses of this micro degree, data is the backbone of all modern applications: be it your favorite weather app, a local event-sharing hub, or an international e-commerce platform, they all run on data.

**Topics covered:**
- 1. Global Accessibility
- 2. Diverse Data Models
- 3. On-demand Scalability
- 4. Consistency Tailored to Needs
- Use Case: Data and Global E-commerce
- Case 1: Latency in Global Sales
- Case 2: Data Availability
- Case 3: Traffic Spikes
- Case 4: Problems Modernizing
- Exercise: Global Applications, Global Solutions

**Key Terms:**

| Term | Definition |
|------|-----------|
| Scenario: | Consider a social media platform with users spanning continents. Users all around Asia, Europe, Africa, Oceania, and the Americas demand real-time updates and interactions.... |
| Solution: | Globally distributed databases, like Azure Cosmos DB, ensure that data is stored and served from multiple regions, reducing latency and enhancing user experience on a global... |
| Scenario: | Imagine a content management system handling articles, images, and user profiles. Each type of data requires a unique structure and handling method. A rigid, one-size-fits-all... |
| Solution: | Multi-model databases, such as Azure Cosmos DB, support various data models like document, key-value, graph, and column-family. This flexibility empowers developers to choose the... |
| Scenario: | Picture an e-commerce platform launching a flash sale, resulting in an overwhelming surge of user traffic. Traditional databases may struggle to scale rapidly, leading to... |
| Solution: | Elastic scalability is a hallmark of services like Azure Cosmos DB. It allows developers to seamlessly scale resources, both in terms of throughput and storage, ensuring... |
| Scenario: | In a banking application processing money transaction, maintaining data integrity is paramount. On the other hand, a movie streaming service optimizing for low-latency access... |
| Solution: | Globally distributed databases offer different consistency models, allowing developers to align database behavior with specific application requirements. Aspiring developers must... |
| Scenario: | Consider a social media platform with users spanning continents. Users all around Asia, Europe, Africa, Oceania, and the Americas demand real-time updates and interactions.... |
| Solution: | Globally distributed databases, like Azure Cosmos DB, ensure that data is stored and served from multiple regions, reducing latency and enhancing user experience on a global... |

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Exploring Global Databases

**TL;DR:** Modern applications are specialized on handling use cases and scenarios deemed impossible just a few generations ago. From high-quality streaming to live-feeds across social medias, all apps and solutions we take for granted these days run on data.

**Topics covered:**
- SQL or NoSQL?
- SQL (Structured Query Language) Databases
- NoSQL (Not Only Structured Query Language) Databases
- Comparison: SQL vs. NoSQL
- Scenario: Streaming and NoSQL
- Azure Cosmos DB for NoSQL
- What is a NoSQL Database?
- NoSQL Database with Document Data Model
- JSON Documents
- Summary: Azure Cosmos DB for NoSQL

**Key Terms:**

| Term | Definition |
|------|-----------|
| Structured Data | SQL databases handle structured data with predefined schemas, ensuring data consistency and integrity. |
| ACID Properties | Transactions in SQL databases follow ACID properties, providing a high level of data reliability. |
| Normalization | Emphasizes normalization to eliminate redundancy in data storage. |
| Flexible Schema | NoSQL databases allow dynamic and evolving data models, accommodating changes without a predefined schema. |
| Scalability | Designed for horizontal scalability, making them suitable for applications with unpredictable workloads and growing datasets. |
| Diverse Data Models | Support various data models like document-oriented, key-value pairs, column-family, and graph databases. |
| Criteria | </edukamu-table-header> |
| SQL Databases | </edukamu-table-header> |
| NoSQL Databases | </edukamu-table-header> |
| 1. Dynamic and Evolving Data: | Streaming services often encounter rapidly changing data, with new content, user interactions, and preferences emerging continuously. NoSQL's flexible schema - in other words, the... |

**Key Points:**
- Data with many different sources and forms.
- Dynamic data schemas that store different types of data.
- Using high-velocity and/or real-time data.
- Not enforcing a specific schema.
- Guaranteed speed at any scale—even through bursts—with instant, limitless elasticity, fast reads, and multi-master writes, anywhere in the world.
- Fast, flexible app development with SDKs for popular languages, a native NoSQL API along with APIs for MongoDB, Cassandra, and Gremlin, and no-ETL (extract, transform, load) analytics.
- Ready for mission-critical applications with guaranteed business continuity, 99.999-percent availability, and enterprise-grade security.
- Fully managed and cost-effective serverless database with instant, automatic scaling that responds to application needs.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Introduction To Azure Cosmos Db

**TL;DR:** Globally distributed databases play an increasingly important, oftentimes even crucial, role in ensuring that ambitious, worldwide services, like social media and global marketplaces, function seamlessly and without errors.

**Topics covered:**
- Getting to Know Azure Cosmos DB
- Key Benefits of Azure Cosmos DB
- Key Benefits of Global Distribution
- Exploring Azure Cosmos DB Resources
- Containers and Databases
- Data Consistency
- Choosing the Right Consistency Level
- Default Consistency
- Strong Consistency
- Bounded Staleness Consistency

**Key Terms:**

| Term | Definition |
|------|-----------|
| Dedicated provisioned throughput mode: | The throughput provisioned on a container is exclusively reserved for that container and it's backed by the SLAs. |
| Shared provisioned throughput mode: | These containers share the provisioned throughput with the other containers in the same database (excluding containers that have been configured with dedicated provisioned... |
| Data Access: | APIs provide a standardized way for applications to access data stored in the database. Developers use APIs to retrieve, insert, update, or delete records within the database. |
| Querying: | APIs enable applications to execute queries on the database, allowing for the retrieval of specific data based on defined criteria. |
| Manipulation of Database Objects: | APIs facilitate the creation and manipulation of database objects, such as tables or documents, allowing developers to define and structure the data schema. |
| Integration with Application Logic: | APIs play a crucial role in integrating database services with the application logic. They allow developers to seamlessly incorporate data operations into the overall... |
| SQL and NoSQL | To put it shortly, SQL is a standardized language used for managing and querying relational databases whereas NoSQL refers to a diverse set of database technologies designed for... |
| Provisioned throughput mode: | In this mode, you provision the number of RUs for your application on a per-second basis in increments of 100 RUs per second. To scale the provisioned throughput for your... |
| Serverless mode: | In this mode, you don't have to provision any throughput when creating resources in your Azure Cosmos DB account. At the end of your billing period, you get billed for the number... |
| Autoscale mode: | In this mode, you can automatically and instantly scale the throughput (RU/s) of your database or container based on its usage. This scaling operation doesn't affect the... |

**Key Points:**
- Identify the key benefits provided by Azure Cosmos DB.
- Describe the elements in an Azure Cosmos DB account and how they're organized.
- Explain the different consistency levels and choose the correct one for your project.
- Briefly describe the APIs supported in Azure Cosmos DB and choose the appropriate API for your solution.
- Create Azure Cosmos DB resources by using the Azure portal.
- Unlimited elastic write and read scalability.
- 99.999% read and write availability all around the world.
- Guaranteed reads and writes served in less than 10 milliseconds at the 99th percentile.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 2

### Azure Cosmos Db In Action

**TL;DR:** Welcome to the second unit! By now, you should have a clear understanding of what the role of database services are in application development and what differentiates NoSQL databases from their SQL counterparts.

**Topics covered:**
- Terminology 1: Server-Side and Client-Side Programming
- Client-Side Programming
- Server-Side Programming
- Key Takeaways
- Terminology 2: Software Development Kits
- 1. SDK (Software Development Kit)
- 2. .NET
- 3. Microsoft .NET SDK v3 for Azure Cosmos DB
- C# Crash Course
- What is a Programming Language?

**Key Terms:**

| Term | Definition |
|------|-----------|
| Definition: | Client-side programming in Azure Cosmos DB involves writing code or logic that runs on the *client side*, typically within your application or application server. |
| Responsibility: | The client-side is responsible for tasks such as handling user inputs, executing application-specific business logic, and managing the communication with the Azure Cosmos DB... |
| Operations: | Client-side programming includes operations like creating queries, processing query results, and managing the data presentation layer. |
| Definition: | Server-side programming in Azure Cosmos DB involves writing code or logic that runs on the *server side*, within the Cosmos DB service itself. |
| Responsibility: | The server-side is responsible for tasks related to data storage, retrieval, and processing within the database. It manages the execution of queries and transactions. |
| Operations: | Server-side programming includes defining stored procedures, triggers, and user-defined functions that execute within the database engine. These components help perform complex... |
| Client-Side: | Primarily focuses on application-specific logic, user interactions, and managing the flow of data between the application and the Cosmos DB service. |
| Server-Side: | Primarily focuses on database-related tasks, ensuring efficient data storage, retrieval, and processing within the Cosmos DB service. |
| API Interaction: | The SDK enables .NET applications to perform operations such as querying, inserting, updating, and deleting data in Azure Cosmos DB. |
| Resource Management: | It provides tools for managing databases, collections, users, and permissions within Azure Cosmos DB. |

**Key Points:**
- API Interaction: The SDK enables .NET applications to perform operations such as querying, inserting, updating, and deleting data in Azure Cosmos DB.
- Resource Management: It provides tools for managing databases, collections, users, and permissions within Azure Cosmos DB.
- Integration: The SDK integrates seamlessly with .NET applications, ensuring smooth communication between the application and the Cosmos DB service.
- Asynchronous Programming: It supports asynchronous programming patterns, allowing developers to write efficient and responsive applications.
- Business applications to capture, analyze, and process data
- Dynamic web applications that can be accessed from a web browser
- Financial and scientific applications
- Write your first lines of C# code.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Implementing Nosql Solutions

**TL;DR:** Each NoSQL database is unique, and so is the use scenario. That's why developers using platforms like Azure Cosmos DB should pay extra close attention to not only the planning, but also the implementation of such services.

**Topics covered:**
- Understanding Serverless Throughput
- Use Cases for Azure Cosmos DB Serverless
- Comparing Serverless and Provisioned Throughput
- 1. Provisioned Throughput:
- 2. Serverless:
- Understanding Autoscale and Standard Throughput
- Autoscale Throughput
- Standard Throughput
- Comparing Autoscale and Standard Throughput
- 1. Comparing Workloads

**Key Terms:**

| Term | Definition |
|------|-----------|
| Model: | Traditional model in which you pre-allocate a fixed amount of throughput measured in Request Units per Second (RU/s) for a container or a database. |
| Billing: | You are billed based on the provisioned RU/s, regardless of actual usage. This means you pay for the provisioned capacity, whether or not you fully utilize it. |
| Predictability: | Offers predictable performance because you have a dedicated amount of throughput reserved for your use. |
| Model: | A consumption-based model in which you don't need to pre-allocate or provision a specific amount of throughput. Instead, you pay for the actual resources consumed by your... |
| Billing: | You are billed based on the actual number of RU/s consumed by your requests. This model is suitable for scenarios with unpredictable or intermittent workloads. |
| Cost-Efficiency: | Cost-efficient for workloads with varying demand as you only pay for what you use, making it suitable for scenarios where usage patterns are sporadic. |
| Automatic Scaling: | Scales automatically based on demand without the need for manual provisioning. |
| Fixed Capacity: | The provisioned throughput remains fixed unless manually adjusted. |
| Predictable Performance: | Offers predictable and consistent performance because you're guaranteed the provisioned number of resources. |
| Cost Implications: | You pay for the provisioned throughput, regardless of whether the actual usage is lower than the provisioned amount. |

**Key Points:**
- A new application with hard to forecast users loads
- A new prototype application within your organization
- Serverless compute integration with a service like Azure Functions
- Just getting started with Azure Cosmos DB as a new developer
- Low traffic application that doesn’t send or receive numerous data
- Model: Traditional model in which you pre-allocate a fixed amount of throughput measured in Request Units per Second (RU/s) for a container or a database.
- Billing: You are billed based on the provisioned RU/s, regardless of actual usage. This means you pay for the provisioned capacity, whether or not you fully utilize it.
- Predictability: Offers predictable performance because you have a dedicated amount of throughput reserved for your use.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Migrating Data

**TL;DR:** After carefully assessing the specific needs of a use scenario, planning resources, and creating an implementation strategy, it's time to start thinking about data. Or, in other words, about bringing our precious data over into a brand-new NoSQL database.

**Topics covered:**
- 1. Migrating Data with Azure Data Factory
- Setup Process
- Reading from Azure Cosmos DB
- Writing to Azure Cosmos DB
- 2. Migrating Data with Stream Analytics
- Writing to Azure Cosmos DB
- 3. Migrating Data with Azure Cosmos DB Spark Connectors
- Setup Process
- Reading from Azure Cosmos DB
- Writing to Azure Cosmos DB

**Key Terms:**

| Term | Definition |
|------|-----------|
| Azure Data Factory | is a native service to extract data, transform it, and load it across sinks and stores in an entirely serverless fashion. From a data integration perspective, this means you can... |
| linked service | within Azure Data Factory. This type of linked service is supported both as a source of data ingest and as a target (**sink**) of data output. For both, the configuration is... |
| source | activity has a configuration JSON object that we can use to set properties such as the query: |
| sink | activity also had a configuration JSON object: |
| Azure Stream Analytics | is a real-time event-processing engine designed to process fast streaming data from multiple sources simultaneously. It can aggregate, analyze, transform, and even move data... |
| upserted | to Azure Cosmos DB for NoSQL based on the value of the **id** field. Items are typically inserted into Azure Cosmos DB for NoSQL. If an item already exists with the same unique... |
| Azure Synapse Analytics | and **Azure Synapse Link** for **Azure Cosmos DB**, you can create a cloud-native hybrid transactional and analytical processing (HTAP) to run analytics over your data in Azure... |
| Synapse Link | is enabled at the account level. This can be accomplished using the Azure portal or by using the Azure CLI: |
| Note: | The next Python examples should be performed within your Azure Synapse Analytics workspace. Keep this in mind if you plan on trying the following on your own. |
| Reminder: | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Planning Nosql Solutions

**TL;DR:** So far on this course, we've explored NoSQL services, such as Azure Cosmos DB for NoSQL, from various perspectives, and also tried setting up a brand-new database. Now, it's time to delve deeper into NoSQL database implementation.

**Topics covered:**
- Step 1. Understanding Throughput
- Container-Level Throughput Provisioning
- Database-Level Throughput Provisioning
- Mixed-Throughput Provisioning
- Evaluating Throughput Requirements
- Configuring Output
- Estimating ad-hoc RU/s Consumption
- Step 2. Planning Data Storage
- Migrating Existing Workloads
- Step 3. Configuring Time-to-live (TTL)

**Key Terms:**

| Term | Definition |
|------|-----------|
| Note | While there are others available, this is the most commonly used method of manual throughput provisioning. |
| Write Single Document | </edukamu-table-cell> |
| Top Query #1 | </edukamu-table-cell> |
| Top Query #2 | </edukamu-table-cell> |
| Top Query #3 | </edukamu-table-cell> |
| Total RU/s | </edukamu-table-cell> |
| Tip: | You can also run a proof of concept application, and use the request charge property of the SDK to measure the real-world RU charge of running the operations that you intend to... |
| Tip: | The maximum TTL value is 2147483647. |

**Key Points:**
- Number of read operations per second
- Number of write operations per second
- Whether you expect to perform near real-time analytics
- The anticipated size of documents

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 3

### Advanced Capabilities Of Azure Cosmos Db

**TL;DR:** So far on this course, we've explored global database services from many perspectives. While our focus has been on Azure Cosmos DB, the contents we're covered largely apply to all NoSQL services that empower global applications we've learned to take for granted.

**Topics covered:**
- 1. Data Modeling in Azure Cosmos DB
- NoSQL Data Modeling
- Partitioning in NoSQL Databases
- Why Partition?
- Types of Partitioning
- Data Modeling and Partitioning in Azure Cosmos DB
- Data Modeling
- Partitioning
- Scenario: E-Commerce Application
- 2. Indexing in Azure Cosmos DB

**Key Terms:**

| Term | Definition |
|------|-----------|
| NoSQL vs. Traditional Relational Databases: | Unlike traditional relational databases that use tables, rows, and columns, NoSQL databases can store and manage various types of data like documents, key-value pairs, wide-column... |
| Schema-less Nature: | NoSQL databases are often schema-less, meaning you don't have to define the structure of your data before you store it. This allows for more flexibility in the types of data you... |
| Focus on Application Needs: | In NoSQL, data modeling is more focused on how the data will be used by the application. You design your data model based on the queries you'll run and the way your application... |
| Scalability: | As your database grows, partitioning helps manage large amounts of data efficiently by distributing it across multiple servers or locations. |
| Performance: | It improves performance by allowing parallel processing and reducing the load on any single server. |
| Availability: | If one partition has issues, the others can still function, improving the overall availability of your database. |
| Horizontal Partitioning (Sharding): | This involves distributing rows of a database table across multiple partitions. Each partition holds a subset of the data based on a partition key, like splitting a list of... |
| Vertical Partitioning: | This involves dividing a database into different partitions based on columns. For example, storing customer contact details in one partition and their order history in another. |
| Functional Partitioning: | Dividing data based on functionality, like separating user data from application logs. |
| Speeds Up Data Retrieval: | Just as a catalog in a library helps you find a book quickly, an index in a database enables faster data retrieval. |

**Key Points:**
- Scalability: As your database grows, partitioning helps manage large amounts of data efficiently by distributing it across multiple servers or locations.
- Performance: It improves performance by allowing parallel processing and reducing the load on any single server.
- Availability: If one partition has issues, the others can still function, improving the overall availability of your database.
- Horizontal Partitioning (Sharding): This involves distributing rows of a database table across multiple partitions. Each partition holds a subset of the data based on a partition key, like splitting...
- Vertical Partitioning: This involves dividing a database into different partitions based on columns. For example, storing customer contact details in one partition and their order history in another.
- Functional Partitioning: Dividing data based on functionality, like separating user data from application logs.
- Speeds Up Data Retrieval: Just as a catalog in a library helps you find a book quickly, an index in a database enables faster data retrieval.
- Efficiency: Without indexing, a database must perform a full scan, which is time-consuming and inefficient, especially with large datasets.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Configuring The Sdk

**TL;DR:** As we've noticed over the course of this micro degree, software development on Microsoft Azure is not just about creating applications, but also about crafting them to perform optimally and seamlessly integrate with essential services. When working with Azure Cosmos DB and different SDKs, customization becomes key.

**Topics covered:**
- Terminology 1: Threading
- Terminology 2: Parallelism
- Terminology 3: Logging
- Enabling Offline Development
- Azure Cosmos DB Emulator
- Configuring the SDK to Connect to the Emulator
- Handling Connection Errors
- Built-in Retry
- Implementing Threading and Parallelism
- Avoiding Resource-related Timeouts

**Key Terms:**

| Term | Definition |
|------|-----------|
| Docker | container image. |
| Microsoft Docs | website and supports various APIs depending on the platform. The NoSQL API is universally supported across all platforms. |
| pull | the image from mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator. |
| Tip: | You can start the emulator using the /Key option to generate a new key instead of using the default key. |
| CosmosClient | like you typically would for a cloud-based account. |
| Tip: | Try to always use the latest version of the SDK. The retry logic that is built-in is constantly being improved in newer releases. |
| 429 | Too many requests |
| 449 | Concurrency error |
| 500 | Unexpected service error |
| 503 | Service unavailable |

**Key Points:**
- 500: Unexpected service error

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Connecting To A Nosql Database

**TL;DR:** Welcome to the third and final unit of this course!

**Topics covered:**
- Connecting NoSQL with SDKs
- Step 1. Configuration
- Step 2. Initialization
- Step 3. Authentication
- Step 4. Communication
- Step 5. Error Handling
- Introduction to Azure Cosmos DB for NoSQL SDKs
- Understanding the SDK
- Importing from Package Managers
- Importing NuGet Packages

**Key Terms:**

| Term | Definition |
|------|-----------|
| Example: | Imagine entering your Wi-Fi password on your phone so that it securely connects to the Internet. |
| Example: | After setting up your phone for Wi-Fi, it's like turning on your web browser to access the Internet. |
| Example: | After connecting to Wi-Fi, your phone might use a security key or password to ensure it's allowed to access the Internet using the network. |
| Example: | After connecting to the Internet, you can do things like searching for information, watching videos, or updating social media on your phone using a web browser of your choice. |
| Example: | If a webpage doesn't load, your web browser might show an error message or try to reload the page without crashing. |
| Microsoft.Azure.Cosmos | library is the latest version of the .NET SDK for Azure Cosmos DB for NoSQL. |
| CosmosClient | </edukamu-table-cell> |
| Database | </edukamu-table-cell> |
| Container | </edukamu-table-cell> |
| nuget | to make it easier to import the library into a .NET application. |

**Key Points:**
- A constructor that takes a single string value representing the connection string for the account.
- A constructor that takes two string values representing the endpoint and a key for the account.
- Retrieve an existing database using the name
- Create a new database passing in a unique database name
- Have the SDK check for the existence of the database and either create or retrieve it automatically
- Retrieve an existing container using just the name
- Create a new container passing in a unique container name, partition key path, and the amount of throughput to manually provision
- Have the SDK check for the existence of the container and either create or retrieve it automatically

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Summary

**TL;DR:** Congratulations on reaching the summary of the Getting Started with Cloud Native Data Storage course! As stated at the beginning, you must complete every assignment in order to pass this course. Therefore please go to Course progress page by pressing the button below (*or the progress icon in the top right corner*), and check that you have indeed c...

**Topics covered:**
- Unit 1: Getting Started with Global Database Services
- Unit 2: Configuring NoSQL Solutions
- Unit 3: Exploring Azure Cosmos DB
- Course Feedback

**Key Points:**
- What are SQL and NoSQL databases? What differentiates them?
- What are examples of possible challenges surrounding global-scale data solutions?
- How would you summarize Azure Cosmos DB?
- What are the key capabilities of Azure Cosmos DB?
- What should be considered when planning NoSQL solutions?
- What options are there for data migration in Azure Cosmos DB?
- How would you describe an SDK?
- In what ways are SDKs and NoSQL databases connected?

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Quick-Reference Glossary

| Term | Definition | Section |
|------|-----------|---------|
| path | of /department/name, then the partition key **value** of this document would be information-technology. Behind the scenes, Azure Cosmos DB for NoSQL automatically manages the... | Components Of Cosmos Db For Nosql |
| Reminder: | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... | Components Of Cosmos Db For Nosql |
| Note: | Only the options in the Basics tab are required to create an Azure Cosmos DB account. | Components Of Cosmos Db For Nosql |
| Tip: | Alternatively, if you would like to use a development environment on your own computer, you can use this <edukamu-link... | Components Of Cosmos Db For Nosql |
| Scenario: | Consider a social media platform with users spanning continents. Users all around Asia, Europe, Africa, Oceania, and the Americas demand real-time updates and interactions.... | Empowering Global Applications |
| Solution: | Globally distributed databases, like Azure Cosmos DB, ensure that data is stored and served from multiple regions, reducing latency and enhancing user experience on a global... | Empowering Global Applications |
| Structured Data | SQL databases handle structured data with predefined schemas, ensuring data consistency and integrity. | Exploring Global Databases |
| ACID Properties | Transactions in SQL databases follow ACID properties, providing a high level of data reliability. | Exploring Global Databases |
| Normalization | Emphasizes normalization to eliminate redundancy in data storage. | Exploring Global Databases |
| Flexible Schema | NoSQL databases allow dynamic and evolving data models, accommodating changes without a predefined schema. | Exploring Global Databases |
| Scalability | Designed for horizontal scalability, making them suitable for applications with unpredictable workloads and growing datasets. | Exploring Global Databases |
| Diverse Data Models | Support various data models like document-oriented, key-value pairs, column-family, and graph databases. | Exploring Global Databases |
| Criteria | </edukamu-table-header> | Exploring Global Databases |
| SQL Databases | </edukamu-table-header> | Exploring Global Databases |
| NoSQL Databases | </edukamu-table-header> | Exploring Global Databases |
| 1. Dynamic and Evolving Data: | Streaming services often encounter rapidly changing data, with new content, user interactions, and preferences emerging continuously. NoSQL's flexible schema - in other words, the... | Exploring Global Databases |
| Dedicated provisioned throughput mode: | The throughput provisioned on a container is exclusively reserved for that container and it's backed by the SLAs. | Introduction To Azure Cosmos Db |
| Shared provisioned throughput mode: | These containers share the provisioned throughput with the other containers in the same database (excluding containers that have been configured with dedicated provisioned... | Introduction To Azure Cosmos Db |
| Data Access: | APIs provide a standardized way for applications to access data stored in the database. Developers use APIs to retrieve, insert, update, or delete records within the database. | Introduction To Azure Cosmos Db |
| Querying: | APIs enable applications to execute queries on the database, allowing for the retrieval of specific data based on defined criteria. | Introduction To Azure Cosmos Db |
| Manipulation of Database Objects: | APIs facilitate the creation and manipulation of database objects, such as tables or documents, allowing developers to define and structure the data schema. | Introduction To Azure Cosmos Db |
| Integration with Application Logic: | APIs play a crucial role in integrating database services with the application logic. They allow developers to seamlessly incorporate data operations into the overall... | Introduction To Azure Cosmos Db |
| SQL and NoSQL | To put it shortly, SQL is a standardized language used for managing and querying relational databases whereas NoSQL refers to a diverse set of database technologies designed for... | Introduction To Azure Cosmos Db |
| Provisioned throughput mode: | In this mode, you provision the number of RUs for your application on a per-second basis in increments of 100 RUs per second. To scale the provisioned throughput for your... | Introduction To Azure Cosmos Db |
| Serverless mode: | In this mode, you don't have to provision any throughput when creating resources in your Azure Cosmos DB account. At the end of your billing period, you get billed for the number... | Introduction To Azure Cosmos Db |
| Autoscale mode: | In this mode, you can automatically and instantly scale the throughput (RU/s) of your database or container based on its usage. This scaling operation doesn't affect the... | Introduction To Azure Cosmos Db |
| Definition: | Client-side programming in Azure Cosmos DB involves writing code or logic that runs on the *client side*, typically within your application or application server. | Azure Cosmos Db In Action |
| Responsibility: | The client-side is responsible for tasks such as handling user inputs, executing application-specific business logic, and managing the communication with the Azure Cosmos DB... | Azure Cosmos Db In Action |
| Operations: | Client-side programming includes operations like creating queries, processing query results, and managing the data presentation layer. | Azure Cosmos Db In Action |
| Client-Side: | Primarily focuses on application-specific logic, user interactions, and managing the flow of data between the application and the Cosmos DB service. | Azure Cosmos Db In Action |
| Server-Side: | Primarily focuses on database-related tasks, ensuring efficient data storage, retrieval, and processing within the Cosmos DB service. | Azure Cosmos Db In Action |
| API Interaction: | The SDK enables .NET applications to perform operations such as querying, inserting, updating, and deleting data in Azure Cosmos DB. | Azure Cosmos Db In Action |
| Resource Management: | It provides tools for managing databases, collections, users, and permissions within Azure Cosmos DB. | Azure Cosmos Db In Action |
| Model: | Traditional model in which you pre-allocate a fixed amount of throughput measured in Request Units per Second (RU/s) for a container or a database. | Implementing Nosql Solutions |
| Billing: | You are billed based on the provisioned RU/s, regardless of actual usage. This means you pay for the provisioned capacity, whether or not you fully utilize it. | Implementing Nosql Solutions |
| Predictability: | Offers predictable performance because you have a dedicated amount of throughput reserved for your use. | Implementing Nosql Solutions |
| Cost-Efficiency: | Cost-efficient for workloads with varying demand as you only pay for what you use, making it suitable for scenarios where usage patterns are sporadic. | Implementing Nosql Solutions |
| Automatic Scaling: | Scales automatically based on demand without the need for manual provisioning. | Implementing Nosql Solutions |
| Fixed Capacity: | The provisioned throughput remains fixed unless manually adjusted. | Implementing Nosql Solutions |
| Predictable Performance: | Offers predictable and consistent performance because you're guaranteed the provisioned number of resources. | Implementing Nosql Solutions |
| Cost Implications: | You pay for the provisioned throughput, regardless of whether the actual usage is lower than the provisioned amount. | Implementing Nosql Solutions |
| Azure Data Factory | is a native service to extract data, transform it, and load it across sinks and stores in an entirely serverless fashion. From a data integration perspective, this means you can... | Migrating Data |
| linked service | within Azure Data Factory. This type of linked service is supported both as a source of data ingest and as a target (**sink**) of data output. For both, the configuration is... | Migrating Data |
| source | activity has a configuration JSON object that we can use to set properties such as the query: | Migrating Data |
| sink | activity also had a configuration JSON object: | Migrating Data |
| Azure Stream Analytics | is a real-time event-processing engine designed to process fast streaming data from multiple sources simultaneously. It can aggregate, analyze, transform, and even move data... | Migrating Data |
| upserted | to Azure Cosmos DB for NoSQL based on the value of the **id** field. Items are typically inserted into Azure Cosmos DB for NoSQL. If an item already exists with the same unique... | Migrating Data |
| Azure Synapse Analytics | and **Azure Synapse Link** for **Azure Cosmos DB**, you can create a cloud-native hybrid transactional and analytical processing (HTAP) to run analytics over your data in Azure... | Migrating Data |
| Synapse Link | is enabled at the account level. This can be accomplished using the Azure portal or by using the Azure CLI: | Migrating Data |
| Note | While there are others available, this is the most commonly used method of manual throughput provisioning. | Planning Nosql Solutions |
| Write Single Document | </edukamu-table-cell> | Planning Nosql Solutions |
| Top Query #1 | </edukamu-table-cell> | Planning Nosql Solutions |
| Top Query #2 | </edukamu-table-cell> | Planning Nosql Solutions |
| Top Query #3 | </edukamu-table-cell> | Planning Nosql Solutions |
| Total RU/s | </edukamu-table-cell> | Planning Nosql Solutions |
| NoSQL vs. Traditional Relational Databases: | Unlike traditional relational databases that use tables, rows, and columns, NoSQL databases can store and manage various types of data like documents, key-value pairs, wide-column... | Advanced Capabilities Of Azure Cosmos Db |
| Schema-less Nature: | NoSQL databases are often schema-less, meaning you don't have to define the structure of your data before you store it. This allows for more flexibility in the types of data you... | Advanced Capabilities Of Azure Cosmos Db |
| Focus on Application Needs: | In NoSQL, data modeling is more focused on how the data will be used by the application. You design your data model based on the queries you'll run and the way your application... | Advanced Capabilities Of Azure Cosmos Db |
| Scalability: | As your database grows, partitioning helps manage large amounts of data efficiently by distributing it across multiple servers or locations. | Advanced Capabilities Of Azure Cosmos Db |
| Performance: | It improves performance by allowing parallel processing and reducing the load on any single server. | Advanced Capabilities Of Azure Cosmos Db |
| Availability: | If one partition has issues, the others can still function, improving the overall availability of your database. | Advanced Capabilities Of Azure Cosmos Db |
| Horizontal Partitioning (Sharding): | This involves distributing rows of a database table across multiple partitions. Each partition holds a subset of the data based on a partition key, like splitting a list of... | Advanced Capabilities Of Azure Cosmos Db |
| Vertical Partitioning: | This involves dividing a database into different partitions based on columns. For example, storing customer contact details in one partition and their order history in another. | Advanced Capabilities Of Azure Cosmos Db |
| Functional Partitioning: | Dividing data based on functionality, like separating user data from application logs. | Advanced Capabilities Of Azure Cosmos Db |
| Speeds Up Data Retrieval: | Just as a catalog in a library helps you find a book quickly, an index in a database enables faster data retrieval. | Advanced Capabilities Of Azure Cosmos Db |
| Docker | container image. | Configuring The Sdk |
| Microsoft Docs | website and supports various APIs depending on the platform. The NoSQL API is universally supported across all platforms. | Configuring The Sdk |
| pull | the image from mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator. | Configuring The Sdk |
| CosmosClient | like you typically would for a cloud-based account. | Configuring The Sdk |
| 429 | Too many requests | Configuring The Sdk |
| 449 | Concurrency error | Configuring The Sdk |
| 500 | Unexpected service error | Configuring The Sdk |
| 503 | Service unavailable | Configuring The Sdk |
| Example: | Imagine entering your Wi-Fi password on your phone so that it securely connects to the Internet. | Connecting To A Nosql Database |
| Microsoft.Azure.Cosmos | library is the latest version of the .NET SDK for Azure Cosmos DB for NoSQL. | Connecting To A Nosql Database |
| Database | </edukamu-table-cell> | Connecting To A Nosql Database |
| Container | </edukamu-table-cell> | Connecting To A Nosql Database |
| nuget | to make it easier to import the library into a .NET application. | Connecting To A Nosql Database |

---

*Auto-generated by `generate_diary.py` — re-run to refresh after re-scraping.*
