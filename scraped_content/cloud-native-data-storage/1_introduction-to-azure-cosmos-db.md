## Introduction to Azure Cosmos DB

Globally distributed databases play an increasingly important, oftentimes even crucial, role in ensuring that ambitious, worldwide services, like social media and global marketplaces, function seamlessly and without errors.

After exploring why such services are needed, it's time to get to know one of them: Microsoft Azure Cosmos DB. As the name suggests, Cosmos DB is an integral part of Microsoft's Azure ecosystem, which makes it the ultimate option for all developers on the platform.

On this page, we'll slowly start delving deeper and deeper into the world of Azure Cosmos DB. You're already familiar with some of its key capabilities, so you have a little head start!

Let's begin with an introduction.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Getting to Know Azure Cosmos DB
</edukamu-collapse-hidden-title>

Azure Cosmos DB is a globally distributed database system that allows you to read and write data from the local replicas of your database and it transparently replicates the data to all the regions associated with your Cosmos account.

After completing this section of the course, you'll be able to:

- Identify the key benefits provided by Azure Cosmos DB.
- Describe the elements in an Azure Cosmos DB account and how they're organized.
- Explain the different consistency levels and choose the correct one for your project.
- Briefly describe the APIs supported in Azure Cosmos DB and choose the appropriate API for your solution.
- Create Azure Cosmos DB resources by using the Azure portal.

### Key Benefits of Azure Cosmos DB

Azure Cosmos DB is a fully managed NoSQL database designed to provide low latency, elastic scalability of throughput, well-defined semantics for data consistency, and high availability.

You can configure your databases to be globally distributed and available in any of the Azure regions. To lower the latency, place the data close to where your users are. Choosing the required regions depends on the global reach of your application and where your users are located.

With Azure Cosmos DB, you can add or remove the regions associated with your account at any time. Your application doesn't need to be paused or redeployed to add or remove a region.

### Key Benefits of Global Distribution

With its novel multi-master replication protocol, every region supports both writes and reads. The multi-master capability also enables:

- Unlimited elastic write and read scalability.
- 99.999% read and write availability all around the world.
- Guaranteed reads and writes served in less than 10 milliseconds at the 99th percentile.

Your application can perform near real-time reads and writes against all the regions you chose for your database. Azure Cosmos DB internally handles the data replication between regions with consistency level guarantees of the level you've selected.

Running a database in multiple regions worldwide increases the availability of a database. If one region is unavailable, other regions automatically handle application requests. Azure Cosmos DB offers 99.999% read and write availability for multi-region databases.

</edukamu-collapse>
<br>


As is the case with every Azure service, Cosmos DB is also dependent on its resources. Your Azure Cosmos DB account contains all your resources that can be used in building applications that work seamlessly worldwide.

The resources are managed at Azure Portal or Azure CLI, both of which we've explored earlier during this micro degree. We'll cover a few additional capabilities of said services in this course, so make sure to recap at this point, if you're feeling insecure!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Exploring Azure Cosmos DB Resources
</edukamu-collapse-hidden-title>

In this section, we'll explore two fundamental concepts of Azure Cosmos DB: databases and containers. They both are essential when it comes to running the service. Let's take a look.

### Containers and Databases

An Azure Cosmos DB container is the fundamental unit of scalability. You can virtually have an unlimited provisioned throughput (RU/s) and storage on a container. Azure Cosmos DB transparently partitions your container using the logical partition key that you specify in order to elastically scale your provisioned throughput and storage.

Currently, you can create a maximum of 50 Azure Cosmos DB accounts under an Azure subscription (this is a soft limit that can be increased via support request). After you create an account under your Azure subscription, you can manage the data in your account by creating databases, containers, and items.

The following image shows the hierarchy of different entities in an Azure Cosmos DB account:

<edukamu-image url="/graphics/module1/cosmos-entities.png" alt="Image showing the hierarchy of Azure Cosmos DB entities: Database accounts are at the top, Databases are grouped under accounts, Containers are grouped under databases." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

You can create one or multiple Azure Cosmos DB databases under your account. A database is analogous to a namespace. A database is the unit of management for a set of Azure Cosmos DB containers.

An Azure Cosmos DB container, on the other hand, is the unit of scalability both for provisioned throughput and storage. A container is horizontally partitioned and then replicated across multiple regions. The items that you add to the container are automatically grouped into logical partitions, which are distributed across physical partitions, based on the partition key. The throughput on a container is evenly distributed across the physical partitions.

When you create a container, you configure throughput in one of the following modes:

- **Dedicated provisioned throughput mode:** The throughput provisioned on a container is exclusively reserved for that container and it's backed by the SLAs.
- **Shared provisioned throughput mode:** These containers share the provisioned throughput with the other containers in the same database (excluding containers that have been configured with dedicated provisioned throughput). In other words, the provisioned throughput on the database is shared among all the “shared throughput” containers.

A container is a schema-agnostic container of items. Items in a container can have arbitrary schemas. For example, an item that represents a person and an item that represents an automobile can be placed in the same container. By default, all items that you add to a container are automatically indexed without requiring explicit index or schema management.

By the way, depending on various factors, such as which API you use, an Azure Cosmos DB item can represent either a document in a collection, a row in a table, or a node or edge in a graph.

</edukamu-collapse>
<br>


Think about your favorite social media applications, or any other service that operates across regions. Its services are fundamentally based on managing and handling data, aren't they? Even though the needs might be different, one factor is crucial for all applications: the consistency of data.

Data consistency refers to the reliability and accuracy of data across a distributed system or database. In the context of databases, it ensures that once a piece of data is updated or modified, all subsequent accesses to that data reflect the latest changes.

In practice, this would mean that users in all regions would be able to interact with the same in-app offers and features at the same time – if the developers so intend.

Different consistency models, such as strong consistency and eventual consistency, allow developers to fine-tune how data updates are propagated across a distributed environment, balancing between reliability and performance based on specific application requirements.

Let's learn how Azure Cosmos DB addresses this question.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Data Consistency
</edukamu-collapse-hidden-title>

Azure Cosmos DB approaches data consistency as a spectrum of choices instead of two extremes. Strong consistency and eventual consistency are at the ends of the spectrum, but there are many consistency choices along the spectrum. Developers can use these options to make precise choices and granular tradeoffs with respect to high availability and performance.

Azure Cosmos DB offers five well-defined levels. From strongest to weakest, the levels are:

- Strong
- Bounded staleness
- Session
- Consistent prefix
- Eventual

Each level provides availability and performance tradeoffs. The following image shows the different consistency levels as a spectrum.

<edukamu-image url="/graphics/module1/five-consistency-levels.png" alt="Image showing data consistency as a spectrum." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

The consistency levels are region-agnostic and are guaranteed for all operations regardless of the region from which the reads and writes are served, the number of regions associated with your Azure Cosmos DB account, or whether your account is configured with a single or multiple write region.

Read consistency applies to a single read operation scoped within a partition-key range or a logical partition. The read operation can be issued by a remote client or a stored procedure.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Choosing the Right Consistency Level
</edukamu-collapse-hidden-title>

Each of the consistency models can be used for specific real-world scenarios. Each provides precise availability and performance tradeoffs and is backed by comprehensive service level agreements (SLA). The following simple considerations help you make the right choice in many common scenarios.

### Default Consistency

You can configure the default consistency level on your Azure Cosmos DB account at any time. The default consistency level configured on your account applies to all Azure Cosmos DB databases and containers under that account. All reads and queries issued against a container or a database use the specified consistency level by default.

Read consistency applies to a single read operation scoped within a logical partition. The read operation can be issued by a remote client or a stored procedure.

Azure Cosmos DB guarantees that 100 percent of read requests meet the consistency guarantee for the consistency level chosen.

### Strong Consistency

Strong consistency offers a linearizability guarantee. Linearizability refers to serving requests concurrently. The reads are guaranteed to return the most recent committed version of an item. A client never sees an uncommitted or partial write. Users are always guaranteed to read the latest committed write.

### Bounded Staleness Consistency

In bounded staleness consistency, the reads are guaranteed to honor the consistent-prefix guarantee. The reads might lag behind writes by at most "K" versions (that is, "updates") of an item or by "T" time interval, whichever is reached first. In other words, when you choose bounded staleness, the "staleness" can be configured in two ways:

- The number of versions (K) of the item
- The time interval (T) reads might lag behind the writes

For a single region account, the minimum value of K and T is 10 write operations or 5 seconds. For multi-region accounts the minimum value of K and T is 100,000 write operations or 300 seconds.

### Session Consistency

In session consistency, within a single client session, reads are guaranteed to honor the consistent-prefix, monotonic reads, monotonic writes, read-your-writes, and write-follows-reads guarantees. This assumes a single "writer" session or sharing the session token for multiple writers.

### Consistent Prefix Consistency

In consistent prefix, updates made as single document writes see eventual consistency. Updates made as a batch within a transaction, are returned consistent to the transaction in which they were committed. Write operations within a transaction of multiple documents are always visible together.

Assume two write operations are performed on documents *Doc 1* and *Doc 2*, within transactions T1 and T2. When client does a read in any replica, the user sees either “*Doc 1* v1 and *Doc 2* v1” or “*Doc 1* v2 and *Doc 2* v2”, but never *“Doc 1* v1 and *Doc 2* v2” or “*Doc 1* v2 and *Doc 2* v1” for the same read or query operation.

Querying is a concept you'll encounter multiple times on this course. In imple terms, it is like asking  specific questions with the goal of getting what you need from a database. Imagine you have a huge cabinet full of files. If you want to find a specific file, like all documents related to a project named "Alpha", you would "query" the cabinet. In databases, this process is done through a query language, which is a set of instructions that tells the database exactly what data you are looking for. So, querying is essentially the way you communicate with a database to retrieve specific data from it.

### Eventual Consistency

In eventual consistency, there's no ordering guarantee for reads. In the absence of any further writes, the replicas eventually converge.

Eventual consistency is the weakest form of consistency because a client may read the values that are older than the ones it read before. Eventual consistency is ideal where the application doesn't require any ordering guarantees. Examples include count of Retweets, Likes, or nonthreaded comments.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
Achieving data consistency is crucial to maintaining the integrity of information, especially in scenarios involving monetary transactions or critical operations.

Different consistency models allow developers to fine-tune how data updates are propagated across a distributed environment, balancing between reliability and performance based on specific application requirements.

In order to take advantage of the data, regardless of the chosen consistency level, there needs to be an elegant way of accessing it. In other words, we need to make the data communicate with the service that uses it.

Do you still remember the term API? Application Programming Interfaces, or APIs, ensure that said communication works effectively.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### APIs and Database Services
</edukamu-collapse-hidden-title>

In the context of database services like Cosmos DB, APIs (Application Programming Interfaces) serve as communication interfaces that allow applications to interact with and manipulate the data stored in the database. These APIs define the set of rules and protocols for requesting and managing data operations.

The following are examples of use scenarios for different APIs:

1. **Data Access:** APIs provide a standardized way for applications to access data stored in the database. Developers use APIs to retrieve, insert, update, or delete records within the database.
2. **Querying:** APIs enable applications to execute queries on the database, allowing for the retrieval of specific data based on defined criteria.
3. **Manipulation of Database Objects:** APIs facilitate the creation and manipulation of database objects, such as tables or documents, allowing developers to define and structure the data schema.
4. **Integration with Application Logic:** APIs play a crucial role in integrating database services with the application logic. They allow developers to seamlessly incorporate data operations into the overall functionality of their applications.

In essence, APIs act as a bridge between the application and the database, providing a set of commands and protocols that enable seamless communication and interaction with the underlying data storage and retrieval mechanisms.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### APIs in Cosmos DB
</edukamu-collapse-hidden-title>

Azure Cosmos DB offers multiple database APIs, which include:

- Azure Cosmos DB for NoSQL
- Azure Cosmos DB for MongoDB
- Azure Cosmos DB for PostgreSQL
- Azure Cosmos DB for Apache Cassandra
- Azure Cosmos DB for Table
- Azure Cosmos DB for Apache Gremlin

By using these APIs, you can model real world data using documents, key-value, graph, and column-family data models. These APIs allow your applications to treat Azure Cosmos DB as if it were various other databases technologies, without the overhead of management, and scaling approaches.

### Choosing an API

If there is an abundance of APIs available, how do you know which one to choose? There are various considerations that help you make the decision. Let's check out a few of them.

API for NoSQL is native to Azure Cosmos DB.

API for MongoDB, PostgreSQL, Cassandra, Gremlin, and Table implement the wire protocol of open-source database engines. These APIs are best suited if the following conditions are true:

- If you have existing MongoDB, PostgreSQL Cassandra, or Gremlin applications
- If you don't want to rewrite your entire data access layer
- If you want to use the open-source developer ecosystem, client-drivers, expertise, and resources for your database

### API for NoSQL

The Azure Cosmos DB API for NoSQL stores data in document format. It offers the best end-to-end experience as we have full control over the interface, service, and the SDK client libraries. Any new feature that is rolled out to Azure Cosmos DB is first available on API for NoSQL accounts. NoSQL accounts provide support for querying items using the Structured Query Language (SQL) syntax.

### API for MongoDB

The Azure Cosmos DB API for MongoDB stores data in a document structure, via BSON format. It's compatible with MongoDB wire protocol; however, it doesn't use any native MongoDB related code. The API for MongoDB is a great choice if you want to use the broader MongoDB ecosystem and skills, without compromising on using Azure Cosmos DB features.

### API for PostgreSQL

Azure Cosmos DB for PostgreSQL is a managed service for running PostgreSQL at any scale, with the Citus open source superpower of distributed tables. It stores data either on a single node, or distributed in a multi-node configuration.

### API for Apache Cassandra

The Azure Cosmos DB API for Cassandra stores data in column-oriented schema. Apache Cassandra offers a highly distributed, horizontally scaling approach to storing large volumes of data while offering a flexible approach to a column-oriented schema. API for Cassandra in Azure Cosmos DB aligns with this philosophy to approaching distributed NoSQL databases. This API for Cassandra is wire protocol compatible with native Apache Cassandra.

### API for Apache Gremlin

The Azure Cosmos DB API for Gremlin allows users to make graph queries and stores data as edges and vertices.

Use the API for Gremlin for scenarios:

- Involving dynamic data
- Involving data with complex relations
- Involving data that is too complex to be modeled with relational databases
- If you want to use the existing Gremlin ecosystem and skills

### API for Table

The Azure Cosmos DB API for Table stores data in key/value format. If you're currently using Azure Table storage, you may see some limitations in latency, scaling, throughput, global distribution, index management, low query performance. API for Table overcomes these limitations and it's recommended to migrate your app if you want to use the benefits of Azure Cosmos DB. API for Table only supports OLTP scenarios.

</edukamu-collapse>
<br>


In essence, APIs facilitate the communications between your application and the database, and without them, no modern app would function effectively.

If the above terminology, such as SQL and NoSQL, seem confusing, don't worry. We'll return to them many times during this course!


<edukamu-note class="edukamu-note-icon-info">
**SQL and NoSQL**

To put it shortly, SQL is a standardized language used for managing and querying relational databases whereas NoSQL refers to a diverse set of database technologies designed for flexible and scalable storage and retrieval of data, including non-relational ones. Please note that even though the word language is mentioned, we're not talking about programming languages, like Python, here.
</edukamu-note>
<br>

Whenever your application wants to access the database, a request is made. This is where an important term, request units, come in. Let's check them out before moving on to the next topic.
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Request Units in Cosmos DB
</edukamu-collapse-hidden-title>

With Azure Cosmos DB, you pay for the throughput you provision and the storage you consume on an hourly basis. Throughput must be provisioned to ensure that sufficient system resources are available for your Azure Cosmos database always.

The cost of all database operations is normalized by Azure Cosmos DB and is expressed by *request units* (or RUs, for short). A request unit represents the system resources such as CPU, IOPS, and memory that are required to perform the database operations supported by Azure Cosmos DB.

The cost to do a point read, which is fetching a single item by its ID and partition key value, for a 1-KB item is 1RU. All other database operations are similarly assigned a cost using RUs. No matter which API you use to interact with your Azure Cosmos container, costs are measured by RUs. Whether the database operation is a write, point read, or query, costs are measured in RUs.

The following image shows the high-level idea of RUs:

<edukamu-image url="/graphics/module1/request-units.png" alt="Image showing how database operations consume request units." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

The type of Azure Cosmos DB account you're using determines the way consumed RUs get charged. There are three modes in which you can create an account:

- **Provisioned throughput mode:** In this mode, you provision the number of RUs for your application on a per-second basis in increments of 100 RUs per second. To scale the provisioned throughput for your application, you can increase or decrease the number of RUs at any time in increments or decrements of 100 RUs. You can make your changes either programmatically or by using the Azure portal. You can provision throughput at container and database granularity level.
- **Serverless mode:** In this mode, you don't have to provision any throughput when creating resources in your Azure Cosmos DB account. At the end of your billing period, you get billed for the number of request units that have been consumed by your database operations.
- **Autoscale mode:** In this mode, you can automatically and instantly scale the throughput (RU/s) of your database or container based on its usage. This scaling operation doesn't affect the availability, latency, throughput, or performance of the workload. This mode is well suited for mission-critical workloads that have variable or unpredictable traffic patterns, and require SLAs on high performance and scale.

</edukamu-collapse>
<br>


Request units are essentially like tokens that help the developers keep track of costs and expenses. Adjusting RUs allows developers to scale the database's capacity to meet the demands of their application's workload.

Now it's time to take a tour around Cosmos DB, which is possible if you have an active Azure subscription or a trial period.

Remember that all exercises marked *Practice* are voluntary, and you can choose whether to complete them or not. They are not mandatory, because they might require software not accessible by everyone or everywhere. If you do have an Azure account, we strongly recommend that you complete them, but they are not a requirement for completing the course.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Exploring Azure Cosmos DB
</edukamu-collapse-hidden-title>

**Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

In this exercise you'll learn how to perform the following actions in the Azure portal:

- Create an Azure Cosmos DB account
- Add a database and a container
- Add data to your database
- Clean up resources

You need an active Azure account to complete this exercise. If you don't already have one, you can sign up for a free trial at <edukamu-link url="https://azure.com/free" target="_blank">https://azure.com/free</edukamu-link>. You'll find more detailed instructions below.

### Step 1. Creating an Azure Cosmos DB Account

1. Log in to the [Azure Portal](https://portal.azure.com/)(target="_blank").
2. From the Azure portal navigation pane, select **+ Create a resource**.
3. Search for **Azure Cosmos DB**, then select **Create/Azure Cosmos DB** to get started.
4. On the **Which API best suits your workload?** page, select **Create** in the **Azure Cosmos DB for NoSQL** box.
5. In the **Create Azure Cosmos DB Account - Azure Cosmos DB for NoSQL** page, enter the basic settings for the new Azure Cosmos DB account.

- **Subscription:** Select the subscription you want to use.
- **Resource Group:** Select **Create new**, then enter *az204-cosmos-rg*.
- **Account Name:** Enter a *unique* name to identify your Azure Cosmos account. The name can only contain lowercase letters, numbers, and the hyphen (-) character. It must be between 3-31 characters in length.
- **Location:** Use the location that is closest to your users to give them the fastest access to the data.
- **Capacity mode:** Select **Serverless**.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold">Review + create</span>.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 7;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Review the account settings, and then select <span style="font-weight: bold">Create</span>. It takes a few minutes to create the account. Wait for the portal page to display <span style="font-weight: bold">Your deployment is complete</span>.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 8;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold">Go to resource</span> to go to the Azure Cosmos DB account page.
</li>
</ol>
</edukamu-section>



### Step 2. Add a Database and a Container

You can use the **Data Explorer** in the Azure portal to create a database and container.

1. Select Data Explorer from the left navigation on your Azure Cosmos DB account page, and then select **New Container**.

<edukamu-image url="/graphics/module1/portal-cosmos-new-container.png" alt="You can add a container using the Data Explorer. Screenshot of Data Explorer in the Azure portal with highlighted New Container button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the <span style="font-weight: bold">New container</span> pane, enter the settings for the new container.
</li>
</ol>
</edukamu-section>
- **Database ID**: Select Create new, and enter *ToDoList*.
- **Container ID**: Enter *Items*.
- **Partition key**: Enter */category*. The samples in this demo use */category* as the partition key.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold">OK</span>. The Data Explorer displays the new database and the container that you created.
</li>
</ol>
</edukamu-section>



### Step 3. Add Data to Your Database

Add data to your new database using Data Explorer.

1. In **Data Explorer**, expand the **ToDoList** database, and expand the **Items** container. Next, select **Items**, and then select **New Item**.

<edukamu-image url="/graphics/module1/portal-cosmos-new-data.png" alt="Create new item in the database." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Add the following structure to the item on the right side of the <span style="font-weight: bold">Items</span> pane:
</li>
</ol>
</edukamu-section>



```JavaScript
{
    "id": "1",
    "category": "personal",
    "name": "groceries",
    "description": "Pick up apples and strawberries.",
    "isComplete": false
}
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold">Save</span>.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold">New Item</span> again and create and save another item with a unique id, and any other properties and values you want. Your items can have any structure, because Azure Cosmos DB doesn't impose any schema on your data.
</li>
</ol>
</edukamu-section>



### Step 4. Clean Up Resources

In order to free space for future practice exercises, you should clean up resources each time you work with Azure.

1. Select *Overview* from the left navigation on your Azure Cosmos DB account page.
2. Select the *az204-cosmos-rg* resource group link in the Essentials group.
3. Select *Delete* resource group and follow the directions to delete the resource group and all of the resources it contains.

Congratulations for completing the first practice exercise of this course!

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step-by-Step Introductions for Activating a Free Azure Trial
</edukamu-collapse-hidden-title>

If you're having trouble activating your free Azure trial needed for accessing services like Azure Cosmos DB, follow the step-by-step instructions below.

**Reminder:** The practical exercises for using Azure Cosmos DB are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

1. Navigate to [Microsoft Azure](https://azure.microsoft.com/en-us/)(target="_blank").
2. Click "Sign in".

<edukamu-image url="/graphics/module1/step-2.jpeg" alt="Screenshot from Microsoft Azure homepage with highlighted Sign in -button at the top of the page." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Sign into your account.
</li>
</ol>
</edukamu-section>


Notice that you need a Microsoft account in order to use activate a free Azure trial. You can either use your organizational account (such as school or work) or create a new one free of charge.

<edukamu-image url="/graphics/module1/step-3.jpeg" alt="Screenshot from Sign in -view with the highlighted Next -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Enter your password.
</li>
</ol>
</edukamu-section>


<edukamu-image url="/graphics/module1/step-4.jpeg" alt="Screenshot from Enter Password -view with the highlighted Sign in -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click the "Subscriptions" icon.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-5.jpeg" alt="Screenshot from Azure services menu with highlighted Subscriptions -icon." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click this "+ Add" icon to add a new Subscription.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-6.jpeg" alt="Screenshot from Subscription -view with highlighted + Add -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 7;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click "Try Azure for free"; We will add a trial subscription in this example.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-7.jpeg" alt="Screenshot from Free trial -view with highlighted Try Azure for free -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 8;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Fill in your details including your phone number for identity verification.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-8.jpeg" alt="Screenshot from personal information fields with highlighted Phone -field." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 9;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click "Text me".
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-9.jpeg" alt="Screenshot from personal information fields with highlighted Text me -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 10;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Type in the code and then click "Verify code".
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-10.jpeg" alt="Screenshot from personal information fields with writted verification code and highlighted Verify code -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 11;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Fill in the rest of the form.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-11.jpeg" alt="Screenshot from personal information fields with highlighted Address line 1 -field." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 12;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Accept Agreements.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-12.jpeg" alt="Screenshot from personal information fields with accepted agreements." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 13;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click "Next".
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-13.jpeg" alt="Screenshot from personal information fields with highlighted Next -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 14;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Fill in your credit card information for Identity Verification (you will not be charged) and click "Sign up".
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-14.jpeg" alt="Screenshot from personal information fields with highlighted Sign up -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

You can find additional information about Microsoft Azure's free trial (also needed for accessing Power Platform) over at <edukamu-link url="https://azure.microsoft.com/en-us/free" target="_blank">Microsoft's website</edukamu-link>.

If setting up a free Azure trial isn't possible for one reason or another, don't worry. You can still follow the practical exercises carefully and complete the courses without exploring Power Platform yourself.

</edukamu-collapse>
<br>


Exploring Azure on your own and with the practice exercises will surely pay off in the long run, making you feel right at home on the platform!

Now it's time for a traditional exercise, though. As usual, you need to complete them in order to advance on this course, so take some time to prepare!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Basics of Azure Cosmos DB
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/introduction-to-azure-cosmos-db-question-scroll-1.yaml" id="o52oveat3f68zi2v">
<br>

</edukamu-collapse>
<br>


We've now taken our first look at Azure Cosmos DB. How are you feeling? Remember that you should take time to recap every now and then in order to set up some APIs, so to say, between your brain and the new knowledge! You’d want the knowledge to be accessible easily, wouldn’t you?

On the next page, we'll get acquainted with NoSQL.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
