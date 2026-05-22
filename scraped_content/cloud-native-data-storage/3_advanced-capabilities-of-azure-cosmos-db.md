## Advanced Capabilities of Azure Cosmos DB

So far on this course, we've explored global database services from many perspectives. While our focus has been on Azure Cosmos DB, the contents we're covered largely apply to all NoSQL services that empower global applications we've learned to take for granted.

In this third unit, we've learned about SDKs and the possibilities they offer when used in tandem with Azure Cosmos DB, and now it's time to familiarize ourselves with a few advanced capabilities of the very service.

While we won't dig deep into the technical details, you'll certainly get a good overview on the numerous capabilities covered here.

In total, we have four topics: 1) data modeling, 2) indexing strategies, 3) replication strategies, and 4) DevOps. We'll tackle them one by one, reviewing the *whys* and *whats* of each one. First, we'll explore the topic at hand on a general level, after which we'll look at Azure Cosmos DB's capabilities before ending with a practical, real-life example.

After this section, you'll know a lot more about Azure Cosmos DB. Let's get started!

### 1. Data Modeling in Azure Cosmos DB

Data modeling is the process of creating a data structure that best suits the needs of your application. It's like planning how to organize your data, similar to deciding how to organize files in a cabinet for easy access and efficient storage.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### NoSQL Data Modeling
</edukamu-collapse-hidden-title>

**NoSQL vs. Traditional Relational Databases:** Unlike traditional relational databases that use tables, rows, and columns, NoSQL databases can store and manage various types of data like documents, key-value pairs, wide-column stores, or graphs. This flexibility allows NoSQL to handle large volumes of unstructured or semi-structured data.

**Schema-less Nature:** NoSQL databases are often schema-less, meaning you don't have to define the structure of your data before you store it. This allows for more flexibility in the types of data you can store and how you can change it over time.

**Focus on Application Needs:** In NoSQL, data modeling is more focused on how the data will be used by the application. You design your data model based on the queries you'll run and the way your application interacts with the data, rather than trying to fit your data into a predefined structure.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Partitioning in NoSQL Databases
</edukamu-collapse-hidden-title>

Partitioning is about dividing your database into smaller, more manageable pieces, called partitions. It's like dividing a large set of files into different folders, each folder representing a partition.

### Why Partition?

- **Scalability:** As your database grows, partitioning helps manage large amounts of data efficiently by distributing it across multiple servers or locations.
- **Performance:** It improves performance by allowing parallel processing and reducing the load on any single server.
- **Availability:** If one partition has issues, the others can still function, improving the overall availability of your database.

### Types of Partitioning

- **Horizontal Partitioning (Sharding):** This involves distributing rows of a database table across multiple partitions. Each partition holds a subset of the data based on a partition key, like splitting a list of customers by region.
- **Vertical Partitioning:** This involves dividing a database into different partitions based on columns. For example, storing customer contact details in one partition and their order history in another.
- **Functional Partitioning:** Dividing data based on functionality, like separating user data from application logs.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Data Modeling and Partitioning in Azure Cosmos DB
</edukamu-collapse-hidden-title>

### Data Modeling

Imagine you're organizing a library. In a traditional library (like a relational database), books are sorted strictly by categories and authors. In Azure Cosmos DB, a NoSQL database, you have more flexibility. You can group books not just by category or author, but also by popularity, reader age group, or even language. This flexibility comes from Azure Cosmos DB's schema-less nature, which allows you to store and manage diverse types of data, like documents, key-value pairs, and so on.

### Partitioning

Now, think about how you'd arrange these books in multiple rooms (partitions) for easy access and management. In Azure Cosmos DB, partitioning is like deciding which room will hold which books based on a specific characteristic, like genre or author. This way, when someone wants a book on cooking, you know exactly which room to go to. This improves performance and makes it easier to manage large volumes of data.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Scenario: E-Commerce Application
</edukamu-collapse-hidden-title>

Consider an e-commerce application. In Azure Cosmos DB, you might model your data to include entities like products, customers, and orders. For partitioning, you could divide the product data based on categories (like electronics, clothing, etc.), and customer data could be partitioned by geographical location. This setup ensures efficient data retrieval and management, enhancing user experience and application performance.

By using Azure Cosmos DB, you're adopting a flexible approach to organize and manage your data, tailored to the specific needs and usage patterns of your application. This flexibility is crucial for modern, dynamic applications that handle diverse data types and require scalable, high-performance data storage solutions.

</edukamu-collapse>
<br>


Understanding data modeling and partitioning is essential for professional Azure developers as they lay the foundation for working with NoSQL databases, especially in cloud environments like Azure Cosmos DB.

Next, let’s shift our focus to indexing.

### 2. Indexing in Azure Cosmos DB

Indexing in Azure Cosmos DB can be understood as organizing a library's catalog system. In a library, a catalog helps you find books without searching every shelf. Similarly, indexing in a database like Azure Cosmos DB helps quickly locate data without scanning the entire database.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Indexing in NoSQL Databases
</edukamu-collapse-hidden-title>

Indexing in databases like Azure Cosmos DB is akin to a library's catalog system. It's a method that enhances data retrieval efficiency by avoiding the need to search through the entire database for a specific piece of information.

### Why is Indexing Important?

- **Speeds Up Data Retrieval:** Just as a catalog in a library helps you find a book quickly, an index in a database enables faster data retrieval.
- **Efficiency:** Without indexing, a database must perform a full scan, which is time-consuming and inefficient, especially with large datasets.
- **Optimizes Performance:** Indexing is crucial for optimizing the performance of query operations, ensuring that applications accessing the database remain fast and responsive.

### Azure Cosmos DB's Indexing Mechanism

Azure Cosmos DB uses an "inverted index" model, in which each node in the index tree has metadata indicating which items in the index match that specific node. This structure allows for efficient data operations. The database automatically indexes every property of each item by default, ensuring good and predictable query performance from the start.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Example: Indexing in Azure Cosmos DB
</edukamu-collapse-hidden-title>

Every Azure Cosmos DB for NoSQL container has a built-in policy that determines how each item should be indexed. By default, this policy dictates that create, update, or delete operations for any item should update the index and that the index should include all properties of every item. This intelligent default is excellent at the start of many solutions as you get good and predictable query performance without having to dive too deeply into tuning an index.

Let’s review an example of the default policy in action.

Here, we have a JSON object representing a product named **Touring-1000 Blue** with three tags (**bike**, **touring**, and **blue**). You should pay attention to the number of things in the *tags* array.

JSON

```JSON
{
  "name": "Touring-1000 Blue",
  "tags": [
    {
      "name": "bike"
    },
    {
      "name": "touring"
    },
    {
      "name": "blue"
    }
  ]
}
```

If we were to represent this JSON object as a tree, this representation would include traversal paths for both the **name** property and its value (**Touring-1000 Blue**). The tree also contains three traversal paths for the three objects in the *tags* array, each with a leaf node for their **name** properties and respective values.

<edukamu-image url="/graphics/module3/2-tour-tree.png" alt="Visual tree representation of the Touring-1000 Blue JSON object." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; max-width: 80%;">
<br>

As a counterpoint, here is another JSON object representing a product named **Mountain-400-W Silver** that only contains two tags (**bike** and **silver**). This object is also unique in that it includes a sku property with a value of **BK-M38S-38**.

JSON

```JSON
{
  "name": "Mountain-400-W Silver",  
  "sku": "BK-M38S-38",
  "tags": [
    {
      "name": "bike"
    },
    {
      "name": "silver"
    }
  ]
}
```

The tree representation for this JSON object includes simple traversal paths for the **name** and **sku** properties. It also contains two traversal paths for the two objects in the **tags** array and corresponding leaf nodes for their **name** properties and respective values.

<edukamu-image url="/graphics/module3/2-mountain-tree.png" alt="Visual tree representation of the Mountain-400-W Silver JSON object." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; max-width: 80%;">
<br>

To conceptualize our container’s index, we tend to think of the index as a union of all trees for each item in the container. Altogether, this creates an **inverted index** which gives our database engine something fast and efficient to traverse when performing query operations. Each node in the tree has metadata indicating which items in our index matches that specific node.

<edukamu-image url="/graphics/module3/2-inverted-tree.png" alt="Inverted index for both the Touring-1000 Blue and Mountain-400-W Silver JSON objects." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

To illustrate this example, consider the following SQL query:

SQL

```SQL
SELECT * FROM products p WHERE p.sku = 'BK-M38S-38'
```

Instead of traversing through each item individually, the search engine will traverse the inverted index. For this query, let’s walk through a sample traversal:

1. First, the search engine will start at the root. As of now, all items match.
2. Next, the search will traverse the **sku** property. Now, only the #2 item matches.
3. Finally, the search will end at the **BK-M38S-28** node. Still, only the #2 item matches.

The search results are that the #2 item (**Mountain-400-W Silver**) matches, and the SQL query will return all fields from this item.

<edukamu-image url="/graphics/module3/2-search-tree-01.png" alt="Example of a search traversal of the inverted index highlighting only the sku property and BK-M38S-38 value path." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Scenario: Indexing and E-Commerce
</edukamu-collapse-hidden-title>

Let's return to our e-commerce platform example. In this scenario, Azure Cosmos DB can index product data, like names, categories, or SKUs (Stock Keeping Units), and customer data such as names and locations.

### How Indexing Helps?

- **Product Searches:** When a customer searches for a specific product by SKU, the indexing system allows the database to quickly locate this product without scanning all items.
- **Efficient Querying:** Consider a SQL query looking for a product by SKU. Azure Cosmos DB uses the indexed tree to traverse directly to the SKU property and quickly returns the matching product, drastically reducing the query time.

Indexing in Azure Cosmos DB plays a crucial role in maintaining high performance and efficiency, especially in dynamic and data-intensive applications like e-commerce platforms.

</edukamu-collapse>
<br>


If you would only be able to choose one action with which to optimize your database, indexing would be a great pick. It can significantly boost processes like querying and searching, which in turn helps make your applications a lot more comfortable to use.

Another advanced capability worth considering is replication.

### 3. Replication in Azure Cosmos DB

Replication in the context of Azure Cosmos DB and NoSQL databases refers to the process of copying and maintaining database objects, like data, in multiple locations for the purposes of redundancy, scalability, and performance.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Replication in NoSQL Databases
</edukamu-collapse-hidden-title>

Modern applications require a data platform that is always online and near end users. Azure Cosmos DB is globally distributed by its design-allowing scenarios where data can be at data centers closer to end-users and scenarios where data is still available despite regional outages. In essence, we're talking about replication.

Replication involves creating and maintaining multiple copies of the same data across different servers or locations. This process is critical for several reasons:

- **High Availability:** By replicating data across multiple servers or regions, the database ensures that if one server or location fails, the data remains accessible from other locations. This redundancy is crucial for maintaining continuous access to the database.
- **Data Durability:** Replication protects against data loss. Having multiple copies means that even if one copy is damaged or lost, others remain intact.
- **Improved Read Performance:** When data is replicated in different geographical locations, users can access the data from the nearest server, reducing latency and increasing the speed of data retrieval.
- **Load Distribution:** Replication allows the database to handle more read queries by distributing them across multiple servers, thereby balancing the load and preventing any single server from being overwhelmed.

In general NoSQL databases, replication is an integral part of their architecture, especially given their focus on handling large volumes of data and high-traffic applications. NoSQL databases typically provide various replication strategies to cater to different needs, such as master-slave replication or peer-to-peer replication.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Replication in Azure Cosmos DB
</edukamu-collapse-hidden-title>

Azure Cosmos DB takes replication to a global level. It not only replicates data across servers within a data center but also across multiple geographic regions. This global distribution is managed automatically by Azure Cosmos DB, ensuring that data is always synchronized and up-to-date across all replicas.

Azure Cosmos DB supports a process called global scale-out, which is fundamental when it comes to replicating. In this context, the term refers to the capability to expand the database's capacity and performance across multiple geographic regions. It's about distributing your database's workload and data globally to meet the demands of a widely distributed user base.

At the minimal configuration, every container has a partition key path defined. This path points to a key-value pair in each JSON item. The value of the partition key is then used to distribute data within a region. Effectively, each container in Azure Cosmos DB will distribute data using the partition key's value to various physical partitions within the same region.

However, physical partition isn’t really a single physical machine or device. The actual implementation of a physical partition is as a replica set. A replica set is a group of replicas that can dynamically grow and shrink to meet the needs of the database platform.

Each replica set will have other geographically distant replica sets that manage the same partition keys if data is distributed globally. These replica sets can then forward data to other replica sets in different regions to create replica copies of the data.

<edukamu-image url="/graphics/module3/2-replica-sets.png" alt="Diagram of three replica sets with data replicated between them." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

An Azure Cosmos DB account replicates data within a region (local distribution) among different replica sets servicing various partition key values. Replica sets that manage the same partition key value are referred to as a partition set as they will forward data between each other (global distribution).

<edukamu-image url="/graphics/module3/2-partition-sets.png" alt="Diagram of local and global distribution among replica and partition sets." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**Note:** The direction that data flows between replica sets is contingent on whether the account is configured with a single-write region or with multi-region write enabled.

For existing Azure Cosmos DB accounts, the Replicate data globally pane is used to add or remove regions. Each region is added using a map, and then replication only occurs once the changes are saved. This pane can also be used to remove existing regions where data is currently replicated.

<edukamu-image url="/graphics/module3/3-replication-map.png" alt="Replicate data globally pane in the Azure portal with a map control." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Scenario: Replication and E-Commerce
</edukamu-collapse-hidden-title>

Let’s once again revisit the example of a global e-commerce platform that serves millions of customers around the world. The platform has a vast product catalog, customer data, and transaction records, all stored in a database. As such, replication is vital.

If you were to choose not to implement a replication strategy, you would risk the following:

- If all your data is stored in a single data center, customers far from that center might experience slow load times or delays in processing transactions.
- In the event of a data center outage or failure, your entire platform could go offline, leading to lost sales and customer dissatisfaction.

On the other hand, an efficient replication strategy would largely mitigate the risks described above. Here's how:

### 1. Data Duplication Across Regions

- You replicate your data across multiple Azure Cosmos DB instances located in different regions worldwide.
- Each region has an exact copy of your data, including product listings, customer information, and order histories.
- In case something happens to one copy, the others are still available. Most probably your customers wouldn't even notice anything unusual.

### 2. Improved Accessibility and Performance

- Customers access data from the nearest replica. For example, a customer in Europe accesses data from a European data center, while a customer in the USA accesses data from a US-based center.
- This proximity reduces latency, leading to faster page loads, quicker searches, and a smoother overall shopping experience.

### 3. High Availability and Disaster Recovery

- If one data center experiences an issue, the system automatically reroutes users to the nearest operational replica.
- Your e-commerce platform remains operational even if an entire data center goes down, ensuring continuous service availability.

### 4. Real-Time Synchronization

- All replicas are kept in sync. When a product's price is updated or a new product added in one region, it's immediately reflected across all replicas.
- Customers see consistent product information and inventory levels, regardless of their location.

### 5. Scalability

- During high-traffic events like flash sales, replication allows you to manage increased load efficiently. More replicas can be added to handle the surge without degrading performance.

### Conclusion

In this e-commerce scenario, replication ensures that customers worldwide enjoy a fast and reliable shopping experience. It also provides the platform with resilience against data loss or downtime due to regional failures.

</edukamu-collapse>
<br>


In summary, replication in Azure Cosmos DB and NoSQL databases is lot more than a feature for data redundancy; it's a comprehensive strategy that enhances data availability, performance, and user experience, especially in distributed and globally scaled applications.

Strategies like indexing and replicating greatly complement each other, as you may have noticed already. They can further be boosted with a series of strategies and actions often referred to as DevOps. It is also the last topic of this course.

### 4. DevOps in Azure Cosmos DB

In the context of NoSQL databases, the term DevOps involves practices and tools that improve the efficiency, reliability, and speed of database management and application development. In other words, it's not a single approach, but rather a combination of many different measures that can be taken in order to improve the operations of a database.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### DevOps in NoSQL Databases
</edukamu-collapse-hidden-title>

DevOps, a blend of 'Development' and 'Operations', in the context of NoSQL databases, is a set of practices and philosophies aimed at unifying software development (Dev) and software operation (Ops).

The primary goal of DevOps is to shorten the systems development cycle while delivering features, fixes, and updates frequently in close alignment with business objectives. For NoSQL databases, this translates into:

1. **Automation of Database Tasks:** DevOps includes actions for automating routine database tasks like backups, scaling, and performance tuning. This is crucial for maintaining the health and performance of the database.
2. **Integration with CI/CD Pipelines:** Continuous Integration (CI) and Continuous Deployment (CD) are fundamental to DevOps. They involve automating the software release process, from initial development to deployment. In the context of NoSQL databases, this could mean automating database updates, schema changes, or data migrations as part of the software release process.
3. **Real-Time Monitoring and Logging:** Effective monitoring and logging are essential for maintaining the health of the database. This includes tracking performance metrics, setting up alerts for anomalies, and logging activities for future analysis.

DevOps is crucial for NoSQL databases as it enables rapid deployment and scaling to handle large data volumes and high throughput efficiently. The practices ensure enhanced reliability and performance through continuous integration and automated testing, while also promoting proactive monitoring and maintenance, crucial for early issue detection and resolution.

DevOps also adds to the flexibility and reliability of a global database, thus complementing strategies like indexing and replicating, which is essential in managing the dynamic and varied data models typical of NoSQL databases.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### DevOps in Azure Cosmos DB
</edukamu-collapse-hidden-title>

Azure Cosmos DB incorporates DevOps in many ways. The following examples are among the most prominent capabilities, but the list is by no means comprehensive.

1. **Azure CLI for Database Management:** The Azure Command Line Interface (CLI) is a powerful tool in managing Azure Cosmos DB. It allows for scripting and automation of various database management tasks, like creating and managing database accounts, databases, and containers.
2. **Indexing and Throughput Management:** DevOps in Azure Cosmos DB involves managing indexing policies and configuring throughput settings using the CLI. This optimizes database performance based on the application's requirements and workload patterns.
3. **Failover and Region Management:** Ensuring high availability and global distribution, Azure Cosmos DB integrates failover management into its DevOps practices. The CLI can be used to initiate failovers and manage geographic regions, thereby enhancing data resilience and availability.
4. **Template-Driven Resource Deployment:** Using Azure Resource Manager templates, Azure Cosmos DB supports automated, template-driven deployment of resources. This enables consistent and error-free deployments, crucial for maintaining the reliability and efficiency of the database in a production environment.

In order to explore the capabilities listed above a bit further, let's briefly review Azure CLI, or Azure CLI (Command Line Interface) from DevOps' point of view.

The Azure CLI is a suite of commands used to administratively manage Azure resources across various platforms and operating systems. The Azure CLI ships with a set of commands tailored specifically to manage Azure Cosmos DB resources. These commands cover the most common administrative scenarios for Azure Cosmos DB accounts, and any underlying resources.

When talking about global databases and DevOps, something called *region failover priority* is worth looking into. In simple terms, we're talking about the predefined order in which operations are transferred to different geographic regions in the event of a regional outage or failure. This is a key aspect of ensuring high availability and disaster recovery.

Azure CLI is extremely useful when it comes to configuring region failover priorities.

### Region Failover Priority and Azure CLI

By setting failover priorities, NoSQL services like Azure Cosmos DB can automatically switch to a secondary region without interruption, maintaining service continuity and data availability. This automated failover process is integral to maintaining robust and resilient cloud-based applications and services.

The **az cosmosdb update** command is used to change the characteristics of an Azure Cosmos DB account. These characteristics includes changing the regions, modifying failover priorities, and enabling multi-region writes.

Let's assume that we have an Azure Cosmos DB account that we created in the **East US** region using this command. We will use this account as an assumption throughout the next set of examples.

Azure CLI

```PowerShell
az cosmosdb create \
    --name '<account-name>' \
    --resource-group '<resource-group>' \
    --locations regionName='eastus'
```

### 1. Adding Account Regions with Azure CLI

Assuming that our Azure Cosmos DB account only contains data in a single region (**East US**), we can add more regions using the **az cosmosdb update** command. When adding new regions, it's important to configure the failover priorities of each region using the unique syntax for this command. In this example, we configured the **East US** region as the first priority, replicated data to the **West US** region and set it as the second priority, and then finally replicated data to the **Central US** region and set it as the third priority for failover.

Azure CLI

```PowerShell
az cosmosdb update \
    --name '<account-name>' \
    --resource-group '<resource-group>' \
    --locations regionName='eastus' failoverPriority=0 isZoneRedundant=False \
    --locations regionName='westus2' failoverPriority=1 isZoneRedundant=False \
    --locations regionName='centralus' failoverPriority=2 isZoneRedundant=False
```

**Note:** When performing any operation involving an account region, you cannot make any other changes to your account and must wait for the operation to complete.

### 2. Enabling Automatic Failover with Azure CLI

Even though we have data replicated across multiple regions, we still need to enable the automatic failover mechanisms in Azure Cosmos DB. The **--enable-automatic-failover** argument takes a boolean value to enable or disable this feature. This example enables the feature using the priorities we set in previous examples.

Azure CLI

```PowerShell
az cosmosdb update \
    --name '<account-name>' \
    --resource-group '<resource-group>' \
    --enable-automatic-failover 'true'
```

### 3. Changing Failover Priorities with Azure CLI

As of now, the Azure Cosmos DB account is configured for automatic failover with the following priorities:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
Region
</edukamu-table-header>
<edukamu-table-header>
Failover Priority
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**East US**
</edukamu-table-cell>
<edukamu-table-cell>
0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**West US**
</edukamu-table-cell>
<edukamu-table-cell>
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Central US**
</edukamu-table-cell>
<edukamu-table-cell>
2
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section>
<br>

To change the priority values, use the **az cosmosdb failover-priority-change** command with the **failover-policies** argument. The **failover-policies** argument has a unique

```PowerShell
**<region-name>=<value>**
```

syntax. In this example, the **West US 2** and **Central US** regions will switch priorities.

Azure CLI

```PowerShell
az cosmosdb failover-priority-change \
    --name '<account-name>' \
    --resource-group '<resource-group>' \
    --failover-policies 'eastus=0' 'centralus=1' 'westus2=2'
```

**Note:** Even if you are not changing the priorities of every region, you must include all regions in the failover-policies argument.

The Azure Cosmos DB account would then be configured for automatic failover with these new priority values:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
Region
</edukamu-table-header>
<edukamu-table-header>
Failover Priority
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**East US**
</edukamu-table-cell>
<edukamu-table-cell>
0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Central US**
</edukamu-table-cell>
<edukamu-table-cell>
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**West US 2**
</edukamu-table-cell>
<edukamu-table-cell>
2
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section>
<br>

### 4. Enabling Multi-region Write with Azure CLI

The **az cosmosdb update** command can be used with the **--enable-multiple-write-locations** argument to enable or disable multi-region writes using a boolean value. In this example, multi-region writes is enabled on our account.

Azure CLI

```PowerShell
az cosmosdb update \
    --name '<account-name>' \
    --resource-group '<resource-group>' \
    --enable-multiple-write-locations 'true'
```

These are just a few example of the use cases of Azure CLI. And there's a lot more to DevOps than just Azure CLI! It's a whole sphere of different capabilities and options aimed at making your applications shine on a global scale.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Scenario: DevOps and E-Commerce
</edukamu-collapse-hidden-title>

In our e-commerce scenario, DevOps on Azure Cosmos DB could be utilized for streamlining product catalog update processes. Suppose the platform frequently updates its product listings, prices, and descriptions. Using Azure CLI, the development team could automate the deployment of these updates, ensuring they're consistently applied across all regions.

Additionally, region failover priorities could be set to ensure if the primary region faces downtime, the service seamlessly switches to a secondary region, maintaining uninterrupted access for customers worldwide. This automation would not only save time but also minimize errors and enhance customer experience.

Also, consider the following DevOps options for a global e-commerce platform:

1. **Automated Product Catalog Updates:** Utilize Azure CLI scripts to automate the updating of product listings, including prices and descriptions, across all database instances.
2. **Continuous Deployment:** Integrate these scripts into a CI/CD pipeline, ensuring that any changes in the product catalog are automatically deployed after passing the necessary tests.
3. **Setting Failover Priorities:** Configure region failover priorities within Azure Cosmos DB to ensure that if the primary region experiences an outage, the system automatically switches to a secondary, pre-defined region.
4. **Monitoring and Feedback Loop:** Implement monitoring tools to track the performance and health of the database, providing feedback for continuous improvement in the database management process.

In addition to these, DevOps provides capabilities for creating and managing resources, adjusting throughput, and configuring indexing policies, to name a few.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
In summary, DevOps is a set of practices combining software development (Dev) and IT operations (Ops), focusing on automating and integrating processes for efficient, reliable, and quick software delivery. It emphasizes continuous improvement, collaboration, and high operational standards.

On this page, we've explored a small portion of Azure Cosmos DB's capabilities, covering 1) data modeling for flexible and efficient data organization, 2) indexing strategies for rapid data retrieval, 3) replication strategies for high availability and global distribution, and 4) DevOps practices for streamlined management and automation. Each of these areas demonstrates the depth of Azure Cosmos DB's features, offering a vast landscape for further discovery and mastery in managing modern, scalable, and resilient data-driven applications.

The technical specifications of the topics discussed here are beyond the scope of this course, but having foundational knowledge of the advanced capabilities of Azure Cosmos DB will surely turn out quite handy in the future – especially if you continue on your path towards Azure development.

It's time for the last exercise of this course! Take some time to answer the following questions one by one. After that, it's time for the summary.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Advanced Capabilities of Azure Cosmos DB
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-of-azure-cosmos-db-text-poll-1.yaml" id="aues17fqflht8g0e">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-of-azure-cosmos-db-text-poll-2.yaml" id="tb16yq8yvqzj3ql4">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-of-azure-cosmos-db-text-poll-3.yaml" id="2xkh3izaljhpc3ti">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-of-azure-cosmos-db-text-poll-4.yaml" id="id2ie8j3t67mddky">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-of-azure-cosmos-db-text-poll-5.yaml" id="xu5j9bsa9nubb01o">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-of-azure-cosmos-db-text-poll-6.yaml" id="z0vjw61hhbrehs0z">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-of-azure-cosmos-db-text-poll-7.yaml" id="4thiilw802ej194d">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-of-azure-cosmos-db-text-poll-8.yaml" id="6t6nppkzvtsembig">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-of-azure-cosmos-db-text-poll-9.yaml" id="o32xnugll6tm2lo1">

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/3/advanced-capabilities-of-azure-cosmos-db?question=aues17fqflht8g0e">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


Azure Cosmos DB is packed with contemporary tools, services, and capabilities that make managing global databases effortless and cost-effective. On this course, we've taken an in-depth look at the platform's offerings from various perspectives.

It's time to review what we've learned.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
