<edukamu-video content="/videos/devai-6-unit2-video.yaml"/>
<br>

## Handling Unstructured Data

Welcome to the second unit of this course!

Over the course of this study program, we've explored solution development on Microsoft Azure from multiple perspectives, including those of data, AI, and even cloud-computing. In this unit, we'll start tying all these component together.

Implementing data solutions with Microsoft Azure is the foundation of this unit. We won't only cover data, though, since we'll swiftly move from data management strategies to exploring how it can be used in uncontainerized solutions. (Do you still remember what that means?)

Let's get started by taking an overview at how data, cloud services, and solution development are tied together in Microsoft Azure. This will help you see beyond the details, understand the big picture, and connect the dots as we continue exploring the platform.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### The Big Picture: Cloud, Data, and Azure Solutions
</edukamu-collapse-hidden-title>

In a modern, increasingly digital society, developing robust and scalable applications for all kinds of use cases has become incremental. Cloud services, data solutions, and other aspects included in this exciting field are extensive enough to provide work opportunities for countless specialized professionals, but understanding the big picture is crucial for all aspiring Azure Developers.

How are data, cloud-services and Azure working together to make our modern lifestyle possible? Why are we covering such a large amount of different tools and services on this course? Let's find out!

### Cloud, Data, and Azure

In the world of modern solution development, Microsoft Azure is an all-encompassing platform, combining data management, cloud services, and application development into a cohesive ecosystem. This integration is crucial in today's digital landscape, where the ability to handle vast amounts of data and develop scalable applications rapidly is paramount.

At the core of this integration is the concept of cloud services, which are services available over the Internet, hosted in Microsoft Azure's data centers. These services range from computing power and storage solutions to machine learning and analytics capabilities, all accessible without the need to manage physical hardware.

In the sphere of data, Azure provides robust solutions for both structured and unstructured data, which we've explored earlier during this program. Unstructured data, which includes files like images, videos, logs, and more, doesn't fit neatly into traditional database models. This is where tools like **Azure Blob Storage** (the first major topic of this unit) shines, offering a highly scalable, secure, and cost-effective platform for storing large volumes of unstructured data. Blob Storage allows applications to access data worldwide with high availability and redundancy, ensuring data integrity and security.

On the application development front, Azure facilitates the creation, deployment, and scaling of applications through services like Azure App Services. However, a significant development in recent years has been the rise of (our second major topic) **containerized solutions** – an approach in which applications are packaged with all their dependencies into containers.

This relatively new development method ensures consistency across environments, from development to production, and simplifies deployment and scaling. **Azure Container Instances** and **Azure Container Apps** are prime examples, providing a serverless platform for running containers, thus reducing the need for infrastructure management. This allows developers to focus on the actual application rather than on the details of the servers hosting them.

Let's take a concrete example: your favorite video streaming service. This service requires a robust backend to store and stream a large library of video content. Here, Azure Blob Storage can be used to store the video files, offering high throughput and streaming capabilities. On the front end, the service uses Azure Container Apps to host the application logic, managing user requests, processing video streams, and handling user authentication. The containerized nature of the application allows for easy updates, scaling based on user demand, and ensures that the service remains highly available.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="devisioona-logo">
### Real-World Data in Azure
</edukamu-collapse-hidden-title>

When you look at the case studies for enterprise data solutions, you may be scared by their scale: everything seems so epic and complex. While enterprise data warehousing – the practice of collecting at least a snapshot of all enterprise data into one place – is a daunting topic indeed, the good part is that very few developers really need to address all that in a single project.

As we build our solutions, one crucial part of the conversation is the *application architecture*. These words are often used loosely, and “architecture” can mean different things to different people. The simplest architectural question is “Which Azure Services are we using?”. After a compute service has been chosen, the next critical element is the required data storage.

The data storage solution is often quite definitive in describing the application. A slow but cheap data store may lend itself to a batch-oriented once-per-night analysis run but would stagger under the load of a B2C web store. A powerful dynamic datastore such as Azure Cosmos DB is an excellent building block for a quickly reacting SaaS user interface, but probably way too expensive for a analysis application dealing with terabytes of data storage.

Depending on how you count, Azure has at least ten different services for data storage. This course just scratches the surface, but in reality, the most common services suffice for the vast majority of applications. When choosing between the data stores, you shouldn’t hesitate to try and challenge each of them. While almost everything can run on almost any data store, there are significant benefits to be reaped by choosing the right one for each task.

In many cases, cloud data stores are cheap enough that you can also use several different services to support a complex application, just keeping in mind that you need to have a comprehensive operations story for each of them – it simply wouldn’t do to run a business-critical application without being confident about basic things such as backup/restore capabilities!

</edukamu-collapse>
<br>

In summary, the synergy of data solutions like Azure Blob Storage and containerized solutions like Azure Container Apps within Microsoft Azure provides a comprehensive platform for businesses to manage their data and develop scalable, efficient applications. Azure's integrated environment simplifies complex processes, making it easier for organizations to focus on innovation and growth.

On this unit, we'll focus on Azure Blob Storage and containerized solutions. Let's start with the former!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Blob Storage
</edukamu-collapse-hidden-title>

Azure Blob storage is Microsoft's object storage solution for the cloud. Blob storage is optimized for storing massive amounts of unstructured data. Unstructured data is data that doesn't adhere to a particular data model or definition, such as text or binary data.

Blob storage is designed for:

- Serving images or documents directly to a browser.
- Storing files for distributed access.
- Streaming video and audio.
- Writing to log files.
- Storing data for backup and restore, disaster recovery, and archiving.
- Storing data for analysis by an on-premises or Azure-hosted service.

Users or client applications can access objects in Blob storage via HTTP/HTTPS, from anywhere in the world. Objects in Blob storage are accessible via the Azure Storage REST API, Azure PowerShell, Azure CLI, or an Azure Storage client library.

An Azure Storage account is the top-level container for all of your Azure Blob storage. The storage account provides a unique namespace for your Azure Storage data that is accessible from anywhere in the world over HTTP or HTTPS.

### Performance Tiers

Azure Storage offers two performance levels of storage accounts, standard and premium. Each performance level supports different features and has its own pricing model.

- **Standard**: This is the standard general-purpose v2 account and is recommended for most scenarios using Azure Storage.
- **Premium**: Premium accounts offer higher performance by using solid-state drives. If you create a premium account you can choose between three account types, block blobs, page blobs, or file shares.

The following table describes the types of storage accounts recommended by Microsoft for most scenarios using Blob storage.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Storage account type**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Performance tier**
</edukamu-table-header>
<edukamu-table-header width="60%">
**Usage**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
General-purpose v2
</edukamu-table-cell>
<edukamu-table-cell>
Standard
</edukamu-table-cell>
<edukamu-table-cell>
Standard storage account type for blobs, file shares, queues, and tables. Recommended for most scenarios using Blob Storage or one of the other Azure Storage services.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Block blob
</edukamu-table-cell>
<edukamu-table-cell>
Premium
</edukamu-table-cell>
<edukamu-table-cell>
Premium storage account type for block blobs and append blobs. Recommended for scenarios with high transaction rates or that use smaller objects or require consistently low storage latency
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Page blobs
</edukamu-table-cell>
<edukamu-table-cell>
Premium
</edukamu-table-cell>
<edukamu-table-cell>
Premium storage account type for page blobs only.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<edukamu-section class="edukamu-included-only-in-mobile">
<edukamu-section class="edukamu-kuvateksti">
The Table above is horizontally scrollable.
</edukamu-section>
</edukamu-section>
<br>

Azure Storage provides different options for accessing block blob data based on usage patterns. Each access tier in Azure Storage is optimized for a particular pattern of data usage. By selecting the right access tier for your needs, you can store your block blob data in the most cost-effective manner.

The available access tiers are:

- The **Hot** access tier, which is optimized for frequent access of objects in the storage account. The Hot tier has the highest storage costs, but the lowest access costs. New storage accounts are created in the hot tier by default.
- The **Cool** access tier, which is optimized for storing large amounts of data that is infrequently accessed and stored for at least 30 days. The Cool tier has lower storage costs and higher access costs compared to the Hot tier.
- The **Cold** access tier, which is optimized for storing data that is infrequently accessed and stored for a minimum of 90 days. The cold tier has lower storage costs and higher access costs compared to the cool tier.
- The **Archive** tier, which is available only for individual block blobs. The archive tier is optimized for data that can tolerate several hours of retrieval latency and remains in the Archive tier for at least 180 days. The archive tier is the most cost-effective option for storing data, but accessing that data is more expensive than accessing data in the hot or cool tiers.

If there's a change in the usage pattern of your data, you can switch between these access tiers at any time.

</edukamu-collapse>
<br>

If you've studied on Microsoft Skills for Jobs before, you might have come across Azure Blob Storage on various occasions. In this course, however, we'll take a more comprehensive look into the platform.

Generally, there are two main data solutions available in Microsoft Azure: 1) Azure Blob Storage and 2) Azure Cosmos DB, on which we focused in the previous course. They are both highly capable solutions, but they cater to different needs. Let's review this question before moving on.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Blob Storage or Azure Cosmos DB?
</edukamu-collapse-hidden-title>

Azure Blob Storage and Azure Cosmos DB are both Azure services for data storage, but they serve different purposes and are optimized for different use cases. Understanding their differences is key to choosing the right one for your needs.

Let's review a few key differences.

### 1. Data Type and Structure

- **Azure Blob Storage**: Optimized for storing unstructured data. This includes files like images, videos, audio, logs, or large datasets that don't fit into a traditional database schema. It's excellent for binary or text data storage.
- **Azure Cosmos DB**: A NoSQL database service designed for structured, semi-structured, or unstructured data. It's ideal for applications that require complex querying, reliable indexing, and rapid development with JSON documents or other NoSQL models (like key-value, graph, or column-family data models).

### 2. Performance and Scalability

- **Blob Storage**: Offers high throughput and massive scalability, suitable for large-scale storage requirements. However, it doesn't provide the advanced querying capabilities of a database.
- **Cosmos DB**: Delivers low-latency and high-availability performance, with turnkey global distribution. It's designed to scale horizontally to meet high-performance requirements.

### 3. Data Access and Transaction Support

- **Blob Storage**: Provides simple REST-based object storage with a straightforward access model but lacks advanced transactional capabilities or complex query support.
- **Cosmos DB**: Supports advanced querying with SQL-like syntax, multiple well-defined consistency models, and transactional processing, making it suitable for applications that need complex data processing.

### 4. Pricing Model

- **Blob Storage**: Generally more cost-effective for large volumes of data that doesn't require frequent read/write operations. You pay for storage space and the data transfer.
- **Cosmos DB**: Priced based on Request Units (RUs) and storage consumed. It can be more expensive than Blob Storage, especially for high throughput scenarios.

### 5. Use Case Scenarios

- **Blob Storage**: Ideal for backup and restore, archiving, and disaster recovery scenarios, and any application that deals with large volumes of unstructured data.
- **Cosmos DB**: Best for web, mobile, gaming applications, IoT, and any application that requires a scalable, globally-distributed database with multi-model support.

In summary, choose Azure Blob Storage for large-scale unstructured data storage needs, especially when cost is a consideration. Opt for Azure Cosmos DB when you need a high-performance, globally-distributed database with rich query capabilities and multi-model support.

Keep in mind that the choice will largely depend on the specific requirements of your application, including the type of data you're storing, the performance needs, scalability requirements, and budget constraints. In other words, the use scenario should be carefully considered before making the choice.

</edukamu-collapse>
<br>

On this course, we won't focus on NoSQL database solutions, but don't forget that all Azure services are highly integrable: Cosmos DB and Blob Storage don't cancel each other out, but should rather be used in tandem with each other - according to the use case, of course.

All right, let's continue getting to know Azure Blob Storage. We'll first explore its main resource types, important considerations before setting up the service, and security features.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Resource Types in Blob Storage
</edukamu-collapse-hidden-title>

Blob storage offers three types of resources:

- The **storage account**.
- A **container** in the storage account.
- A **blob** in a container.

### 1. Storage Accounts

A storage account provides a unique namespace in Azure for your data. Every object that you store in Azure Storage has an address that includes your unique account name. The combination of the account name and the Azure Storage blob endpoint forms the base address for the objects in your storage account.

For example, if your storage account is named *mystorageaccount*, then the default endpoint for Blob storage is:

`http://mystorageaccount.blob.core.windows.net`

### 2. Containers

A container organizes a set of blobs, similar to a directory in a file system. A storage account can include an unlimited number of containers, and a container can store an unlimited number of blobs.

A container name must be a valid DNS name, as it forms part of the unique URI (Uniform resource identifier) used to address the container or its blobs. Follow these rules when naming a container:

- Container names can be between 3 and 63 characters long.
- Container names must start with a letter or number, and can contain only lowercase letters, numbers, and the dash (-) character.
- Two or more consecutive dash characters aren't permitted in container names.

The URI for a container is similar to:

`https://myaccount.blob.core.windows.net/mycontainer`

<edukamu-note class="edukamu-note-icon-info">
### What are URIs?

A URI, or <span style="font-style: italic;">Uniform Resource Identifier</span>, is a string of characters used to identify a resource on the internet or a network. It's a generic term that encompasses both URLs (Uniform Resource Locators) and URNs (Uniform Resource Names).

URLs are commonly used in web browsers to locate web pages and other resources on the Internet. Unlike URLs, URNs do not imply availability or location but are used to uniquely identify an entity. For example, an ISBN number for a book is a type of URN.
</edukamu-note>
<br>

### 3. Blobs within Containers

Azure Storage supports three types of blobs:

- **Block blobs** store text and binary data. Block blobs are made up of blocks of data that can be managed individually. Block blobs can store up to about 190.7 TiB.
- **Append blobs** are made up of blocks like block blobs, but are optimized for append operations. Append blobs are ideal for scenarios such as logging data from virtual machines.
- **Page blobs** store random access files up to 8 TB in size. Page blobs store virtual hard drive (VHD) files and serve as disks for Azure virtual machines.

The URI for a blob is similar to:

`https://myaccount.blob.core.windows.net/mycontainer/myblo`

or

`https://myaccount.blob.core.windows.net/mycontainer/myvirtualdirectory/myblob`

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Security Features of Blob Storage
</edukamu-collapse-hidden-title>

Azure Storage provides a comprehensive set of security capabilities that together enable developers to build secure applications:

- All data (including metadata) written to Azure Storage is automatically encrypted using Storage Service Encryption (SSE).
- Microsoft Entra ID and Role-Based Access Control (RBAC) are supported for Azure Storage for both resource management operations and data operations, as follows:
    - You can assign RBAC roles scoped to the storage account to security principals and use Microsoft Entra ID to authorize resource management operations such as key management.
    - Microsoft Entra integration is supported for blob and queue data operations. You can assign RBAC roles scoped to a subscription, resource group, storage account, or an individual container or queue to a security principal or a managed identity for Azure resources.
- Data can be secured in transit between an application and Azure by using Client-Side Encryption, HTTPS, or SMB 3.0.
- OS and data disks used by Azure virtual machines can be encrypted using Azure Disk Encryption.
- Delegated access to the data objects in Azure Storage can be granted using a shared access signature.

### Encrypting Data at Rest

Azure Storage automatically encrypts your data when persisting it to the cloud. Encryption protects your data and helps you meet your organizational security and compliance commitments. Data in Azure Storage is encrypted and decrypted transparently using 256-bit AES encryption, one of the strongest block ciphers available, and is FIPS 140-2 compliant. Azure Storage encryption is similar to BitLocker encryption on Windows.

Azure Storage encryption is enabled for all new and existing storage accounts and can't be disabled. Because your data is secured by default, you don't need to modify your code or applications to take advantage of Azure Storage encryption.

Storage accounts are encrypted regardless of their performance tier (standard or premium) or deployment model (Azure Resource Manager or classic). All Azure Storage redundancy options support encryption, and all copies of a storage account are encrypted. All Azure Storage resources are encrypted, including blobs, disks, files, queues, and tables. All object metadata is also encrypted.

Encryption doesn't affect Azure Storage performance. There's no extra cost for Azure Storage encryption.

### Encrypting Key Management

You can rely on Microsoft-managed keys for the encryption of your storage account, or you can manage encryption with your own keys. If you choose to manage encryption with your own keys, you have two options:

- You can specify a *customer-managed* key to use for encrypting and decrypting all data in the storage account. A customer-managed key is used to encrypt all data in all services in your storage account.
- You can specify a *customer-provided* key on Blob storage operations. A client making a read or write request against Blob storage can include an encryption key on the request for granular control over how blob data is encrypted and decrypted.

The following table compares key management options for Azure Storage encryption.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="25%">

</edukamu-table-header>
<edukamu-table-header width="25%">
**Microsoft-managed keys**
</edukamu-table-header>
<edukamu-table-header width="25%">
**Customer-managed keys**
</edukamu-table-header>
<edukamu-table-header width="25%">
**Customer-provided keys**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Encryption/decryption operations
</edukamu-table-cell>
<edukamu-table-cell>
Azure
</edukamu-table-cell>
<edukamu-table-cell>
Azure
</edukamu-table-cell>
<edukamu-table-cell>
Azure
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Azure Storage services supported
</edukamu-table-cell>
<edukamu-table-cell>
All
</edukamu-table-cell>
<edukamu-table-cell>
Blob storage, Azure Files
</edukamu-table-cell>
<edukamu-table-cell>
Blob storage
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Key storage
</edukamu-table-cell>
<edukamu-table-cell>
Microsoft key store
</edukamu-table-cell>
<edukamu-table-cell>
Azure Key Vault
</edukamu-table-cell>
<edukamu-table-cell>
Azure Key Vault or any other key store
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Key rotation responsibility
</edukamu-table-cell>
<edukamu-table-cell>
Microsoft
</edukamu-table-cell>
<edukamu-table-cell>
Customer
</edukamu-table-cell>
<edukamu-table-cell>
Customer
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Key usage
</edukamu-table-cell>
<edukamu-table-cell>
Microsoft
</edukamu-table-cell>
<edukamu-table-cell>
Azure portal, Storage Resource Provider REST API, Azure Storage management libraries, PowerShell, CLI
</edukamu-table-cell>
<edukamu-table-cell>
Azure Storage REST API (Blob storage), Azure Storage client libraries
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Key access
</edukamu-table-cell>
<edukamu-table-cell>
Microsoft only
</edukamu-table-cell>
<edukamu-table-cell>
Microsoft, Customer
</edukamu-table-cell>
<edukamu-table-cell>
Customer only
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<edukamu-section class="edukamu-included-only-in-mobile">
<edukamu-section class="edukamu-kuvateksti">
The Table above is horizontally scrollable.
</edukamu-section>
</edukamu-section>
<br>

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
Azure Blob Storage is a great choice for many scenarios to provide robust and secure data solutions for companies of all sizes. Some of the most prominent use cases include, but are not limited to, the following:

## 1. Streaming Services

In on-demand music or video services, Azure Blob Storage can be used to store large multimedia files. The platform can leverage Blob Storage for its high throughput and massive scalability to stream media files efficiently to users around the world. It's capable of handling large volumes of unstructured data, like movies and music tracks, and ensures they are delivered with high availability and minimal latency.

## 2. Backup Solutions for Enterprises

In this scenario, Blob Storage serves as a reliable and secure destination for storing backups of critical business data and applications. Enterprises can use Blob Storage to archive large volumes of data, taking advantage of its durability and redundancy features. The data can be efficiently backed up to the cloud, ensuring protection against data loss due to system failures, natural disasters, or other disruptions.

## 3. Big Data Analytics

Azure Blob Storage can be used as a data lake to store vast amounts of raw data in its native format. This is ideal for organizations that need to collect and store diverse data sets, such as logs, sensor data, or social media feeds, for big data analytics. Data scientists and analysts can then run analytics tools and big data processing frameworks over this data.

In many cases, companies decide to adopt Azure Blob Storage as their business and user bases grow, increasing the need for robust, reliable, and highly capable data solutions.

Hosting static websites is another area in which this data solution shines.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Static Website Hosting with Blob Storage
</edukamu-collapse-hidden-title>

Static websites are websites that consist of fixed content displaying the same information to all visitors. Unlike dynamic websites, they typically can't cater to a single user's needs, but are simple to set up, fast to use, and easy to host. For example, a restaurant's website showcasing its menu and location would be a static website.

You can serve static content (HTML, CSS, JavaScript, and image files) directly from a storage container named $web. Hosting your content in Azure Storage enables you to use serverless architectures that include Azure Functions and other Platform as a service (PaaS) services. Azure Storage static website hosting is a great option in cases where you don't require a web server to render content.

Static websites have some limitations. For example, If you want to configure headers, you have to use Azure Content Delivery Network (Azure CDN). There's no way to configure headers as part of the static website feature itself. Also, Authentication (AuthN) and Authorization (AuthZ) aren't supported. If these features are important for your scenario, consider using Azure Static Web Apps.

### Enabling Static Web Hosting

Static website hosting is a feature that you have to enable on the storage account. When you configure your account for static website hosting, Azure Storage automatically creates a container named `$web`. The `$web` container contains the files for your static website.

To enable static website hosting:

1. Locate your storage account in the Azure portal and display the account overview.
2. Select **Static website** to display the configuration page.
3. Select **Enabled** to enable static website hosting for the account.
4. In the **Index document name** field, specify a default index page. For example, index.html.
5. In the **Error document path** field, specify a default error page. For example, 404.html.
6. Select **Save**.

<edukamu-image url="/graphics/module2/enable-static-website-hosting.png" alt="Screenshot showing the locations of the fields to enable and configure static website hosting." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

You can modify the public access level of the `$web` container, but making this modification has no impact on the primary static website endpoint because these files are served through anonymous access requests. That means public (read-only) access to all files.

While the primary static website endpoint isn't affected, a change to the public access level does impact the primary blob service endpoint.

For example, if you change the public access level of the `$web` container from Private (no anonymous access) to Blob (anonymous read access for blobs only), then the level of public access to the primary static website endpoint `https://contosoblobaccount.z22.web.core.windows.net/index.html` doesn't change.

However, the public access to the primary blob service endpoint `https://contosoblobaccount.blob.core.windows.net/$web/index.html` does change from private to public. Now users can open that file by using either of these two endpoints.

Disabling public access on a storage account by using the public access setting of the storage account doesn't affect static websites that are hosted in that storage account. For more information, see Remediate anonymous public read access to blob data (Azure Resource Manager deployments).

You can make your static website available via a custom domain.

It's easier to enable HTTP access for your custom domain, because Azure Storage natively supports it. To enable HTTPS, you have to use Azure CDN because Azure Storage doesn't yet natively support HTTPS with custom domains.

</edukamu-collapse>
<br>

If you've browsed the Internet today, it's highly likely that you've visited at least a few static websites. Some of those sites might well be hosted with Azure Blob Storage!

After exploring the main features of Azure Blob Storage, it's a great time for an exercise.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Azure Blob Storage
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/handling-unstructured-data-question-scroll-1.yaml" id="41tnv6lgzggzet1u">
<br>

</edukamu-collapse>
<br>

We're now well on our way towards mastering Azure Blob Storage! On the next page, we'll explore its capabilities for ensuring data availability.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1.png" alt="Edukamu-progress-in-a-module-image">
