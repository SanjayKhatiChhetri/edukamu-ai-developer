## Exploring Non-relational Data

After digging deep into the realms of relational data, it's essential to recognize that not all data conforms to the tidy rows and columns we've come to associate with traditional databases.

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### YRITYS: Scenarios from Real Life
</edukamu-collapse-hidden-title>

Placeholder: Tähän tulee teksti, jossa kerrotaan tosielämän tilanteista.

</edukamu-collapse>
<br> -->

Although most companies prefer relational databases, in which the data is organized in related tables and managed by using Structured Query Language (SQL), this is not always possible. Non-relational databases embrace the unstructured and semi-structured world of data, providing more scalable and adaptable solutions.

Azure Blob Storage is a service that enables you to store massive amounts of unstructured data as binary large objects, or blobs, in the cloud. Blob, an acronym for *Binary Large Object*, represents a fundamental unit of data in Azure Blob Storage. Unlike traditional databases that organize information into structured tables, blob storage embraces the concept of object storage, allowing you to store and retrieve data in its native format, regardless of its type or size.

As such, Azure Blob Storage is the ideal option for handling non-relational data.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Blob Storage
</edukamu-collapse-hidden-title>

Azure Blob Storage is as a versatile and scalable solution designed to handle vast amounts of unstructured data. Whether dealing with images, videos, documents, or any other type of file, it provides a secure and efficient means to store, manage, and access your data in the cloud.

Blobs are an efficient way to store data files in a format that is optimized for cloud-based storage, and applications can read and write them by using the Azure blob storage API.

<edukamu-image url="/graphics/module2/azure-blob-storage.png" alt="An Azure blob storage container with two blobs."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

In an Azure storage account, you store blobs in *containers*. A container provides a convenient way of grouping related blobs together. You control who can read and write blobs inside a container at the container level.

Within a container, you can organize blobs in a hierarchy of virtual folders, similar to files in a file system on disk. However, by default, these folders are simply a way of using a "/" character in a blob name to organize the blobs into namespaces. The folders are purely virtual, and you can't perform folder-level operations to control access or perform bulk operations.

Azure Blob Storage supports three different types of blob:
* **Block blobs**. A block blob is handled as a set of blocks. Each block can vary in size, up to 4000 MiB. A block blob can contain up to 190.7 TiB (4000 MiB X 50,000 blocks), giving a maximum size of over 5000 MiB. The block is the smallest amount of data that can be read or written as an individual unit. Block blobs are best used to store discrete, large, binary objects that change infrequently.
* **Page blobs**. A page blob is organized as a collection of fixed size 512-byte pages. A page blob is optimized to support random read and write operations; you can fetch and store data for a single page if necessary. A page blob can hold up to 8 TB of data. Azure uses page blobs to implement virtual disk storage for virtual machines.
* **Append blobs**. An append blob is a block blob optimized to support append operations. You can only add blocks to the end of an append blob; updating or deleting existing blocks isn't supported. Each block can vary in size, up to 4 MB. The maximum size of an append blob is just over 195 GB.

Blob storage provides three access tiers, which help to balance access latency and storage cost:
* *The Hot tier* is the default. You use this tier for blobs that are accessed frequently. The blob data is stored on high-performance media.
* *The Cool tier* has lower performance and incurs reduced storage charges compared to the Hot tier. Use the Cool tier for data that is accessed infrequently. It's common for newly created blobs to be accessed frequently initially, but less so as time passes. In these situations, you can create the blob in the Hot tier, but migrate it to the Cool tier later. You can migrate a blob from the Cool tier back to the Hot tier.
* The *Archive* tier provides the lowest storage cost, but with increased latency. The Archive tier is intended for historical data that mustn't be lost, but is required only rarely. Blobs in the Archive tier are effectively stored in an offline state. Typical reading latency for the Hot and Cool tiers is a few milliseconds, but for the Archive tier, it can take hours for the data to become available. To retrieve a blob from the Archive tier, you must change the access tier to Hot or Cool. The blob will then be rehydrated. You can read the blob only when the rehydration process is complete.

You can create lifecycle management policies for blobs in a storage account. A lifecycle management policy can automatically move a blob from Hot to Cool, and then to the Archive tier, as it ages and is used less frequently (policy is based on the number of days since modification). A lifecycle management policy can also arrange to delete outdated blobs.

</edukamu-collapse>
<br>


Azure Blob Storage is an excellent choice for companies facing diverse data storage needs, particularly when dealing with large volumes of unstructured data. By using it, companies can benefit from a reliable, scalable, and cost-efficient solution for managing their unstructured data in the cloud.

Sometimes, however, even Azure blob storage can fall short, which is when even more advanced data solutions come to play. Azure Data Lake Storage Gen2 offers specialized features tailored for analytics, big data processing, and advanced data management.

Let's take a look, shall we?


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Data Lake Storage Gen2
</edukamu-collapse-hidden-title>

Azure Data Lake Store (Gen1) is a separate service for hierarchical data storage for analytical data lakes, often used by so-called *big data* analytical solutions that work with structured, semi-structured, and unstructured data stored in files.

Azure Data Lake Storage Gen2, on the other hand, is a newer version of this service that is integrated into Azure Storage; enabling you to take advantage of the scalability of blob storage and the cost-control of storage tiers, combined with the hierarchical file system capabilities and compatibility with major analytics systems of Azure Data Lake Store.

<edukamu-image url="/graphics/module2/azure-data-lake.png" alt="An Azure blob storage container with a hierarchical namespace."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Systems like Hadoop in Azure HDInsight, Azure Databricks, and Azure Synapse Analytics can mount a distributed file system hosted in Azure Data Lake Store Gen2 and use it to process huge volumes of data.

To create an Azure Data Lake Store Gen2 files system, you must enable the **Hierarchical Namespace** option of an Azure Storage account. You can do this when initially creating the storage account, or you can upgrade an existing Azure Storage account to support Data Lake Gen2. Be aware however that upgrading is a one-way process – after upgrading a storage account to support a hierarchical namespace for blob storage, you can’t revert it to a flat namespace.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
In general, Azure Data Lake Storage Gen2 should be considered in the following scenarios:

* Your data landscape involves complex analytics workloads that require advanced features.
* Fine-grained access control is essential for compliance and security.
* You need a hierarchical namespace to organize and navigate through extensive datasets more efficiently.
* Integration with Azure Databricks or other advanced analytics services is a priority.

Remember that every case is unique, and so is every company: while theoretical best practices and recommendations are useful, it's still important to assess each use scenario separately – this is crucial to remember if you do end up working with data.

And if you do, you might be assigned to handle an array of computers and other in-house devices. That's when sharing files safely and securely becomes incremental – and, consequently, when Azure Files shines. After briefly covering Azure Files, we'll shortly review one more NoSQL storage service, Azure Tables, to wrap up this section.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Files
</edukamu-collapse-hidden-title>

Many on-premises systems comprising a network of in-house computers make use of file shares. A file share enables you to store a file on one computer, and grant access to that file to users and applications running on other computers. This strategy can work well for computers in the same local area network but doesn't scale well as the number of users increases, or if users are located at different sites.

Azure Files is essentially a way to create cloud-based network shares, such as you typically find in on-premises organizations to make documents and other files available to multiple users. By hosting file shares in Azure, organizations can eliminate hardware costs and maintenance overhead, and benefit from high availability and scalable cloud storage for files.

<edukamu-image url="/graphics/module2/azure-files.png" alt="An Azure storage account with an Azure Files share."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

You create Azure File storage in a storage account. Azure Files enables you to share up to 100 TB of data in a single storage account. This data can be distributed across any number of file shares in the account. The maximum size of a single file is 1 TB, but you can set quotas to limit the size of each share below this figure. Currently, Azure File Storage supports up to 2000 concurrent connections per shared file.

After you've created a storage account, you can upload files to Azure File Storage using the Azure portal, or tools such as the *AzCopy* utility. You can also use the Azure File Sync service to synchronize locally cached copies of shared files with the data in Azure File Storage.

Azure File Storage offers two performance tiers. The *Standard* tier uses hard disk-based hardware in a datacenter, and the *Premium* tier uses solid-state disks. The Premium tier offers greater throughput, but is charged at a higher rate.

Azure Files supports two common network file sharing protocols:
* *Server Message Block* (SMB) file sharing is commonly used across multiple operating systems (Windows, Linux, macOS).
* *Network File System* (NFS) shares are used by some Linux and macOS versions. To create an NFS share, you must use a premium tier storage account and create and configure a virtual network through which access to the share can be controlled.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Tables
</edukamu-collapse-hidden-title>

Azure Table Storage is a NoSQL storage solution that makes use of tables containing *key/value* data items. Each item is represented by a row that contains columns for the data fields that need to be stored.

<edukamu-image url="/graphics/module2/azure-tables.png" alt="An Azure storage account with Azure tables."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

However, don't be misled into thinking that an Azure Table Storage table is like a table in a relational database. An Azure Table enables you to store semi-structured data. All rows in a table must have a unique key (composed of a partition key and a row key), and when you modify data in a table, a timestamp column records the date and time the modification was made; but other than that, the columns in each row can vary.

Azure Table Storage tables have no concept of foreign keys, relationships, stored procedures, views, or other objects you might find in a relational database. Data in Azure Table storage is usually denormalized, with each row holding the entire data for a logical entity. For example, a table holding customer information might store the first name, last name, one or more telephone numbers, and one or more addresses for each customer. The number of fields in each row can be different, depending on the number of telephone numbers and addresses for each customer, and the details recorded for each address. In a relational database, this information would be split across multiple rows in several tables.

To help ensure fast access, Azure Table Storage splits a table into partitions. Partitioning is a mechanism for grouping related rows, based on a common property or partition key. Rows that share the same partition key will be stored together. Partitioning not only helps to organize data, it can also improve scalability and performance in the following ways:
* Partitions are independent from each other and can grow or shrink as rows are added to, or removed from, a partition. A table can contain any number of partitions.
* When you search for data, you can include the partition key in the search criteria. This helps to narrow down the volume of data to be examined and improves performance by reducing the amount of I/O (input and output operations or *reads* and *writes*) needed to locate the data.

The key in an Azure Table Storage table comprises two elements; the partition key that identifies the partition containing the row, and a row key that is unique to each row in the same partition. Items in the same partition are stored in row key order. If an application adds a new row to a table, Azure ensures that the row is placed in the correct position in the table. This scheme enables an application to quickly perform *point* queries that identify a single row, and *range* queries that fetch a contiguous block of rows in a partition.

</edukamu-collapse>
<br>


We've now explored various Azure Services for handling non-relational data. This being the case, it's the perfect time to remind you to take full advantage of your active Azure subscription, if you have one. You should explore Azure to your heart's content and try out the services we cover on this course – it will make them much easier to understand in the long run!

If you do have an Azure subscription, you can also try your hand at the practice exercises scattered here and there on the course, as you know. The next one is coming up now!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Explore Azure Storage
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

If you have an active Azure subscription, you can explore the services we just covered over at Microsoft’s Learn platform.

<edukamu-button url="https://microsoftlearning.github.io/DP-900T00A-Azure-Data-Fundamentals/Instructions/Labs/dp900-02-storage-lab.html">Practice: Explore Azure Storage (Microsoft Learn)</edukamu-button>
<br>

If you aren't able to access Azure, don't worry. These practice exercises are not a requirement for completing this course.

</edukamu-collapse>
<br>


Now, as usual, it's time to review your knowledge with an exercise. You know the drill: Answer each question correctly before moving on. Good luck!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Non-relational Data
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/exploring-non-relational-data-question-scroll.yaml" id="vqmt25hp14v8dj8m">
<br>

</edukamu-collapse>
<br>


We're not done with non-relational data just yet! In fact, there's one more service to cover, and it's an important one for aspiring AI developers!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
