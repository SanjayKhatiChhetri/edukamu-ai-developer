## Storage Services

As you just learned, Azure can also take care of all your data storage needs. The data is kept safe and secure, but easily accessible for you and your colleagues. In this section we’ll learn more about Azure Storage and the services it provides.

<edukamu-section class="slate-section slate-blue">
As an Azure Storage user, you will get to enjoy many kinds of benefits, such as the following.

* **Durability and availability**. Redundancy ensures that your data is safe if transient hardware failures occur. You can also opt to replicate data across data centers or geographical regions for additional protection from local catastrophes or natural disasters. Data replicated in this way remains highly available if an unexpected outage occurs.
* **Security**. All data written to an Azure storage account is encrypted by the service. Azure Storage provides you with fine-grained control over who has access to your data.
* **Scalability**. Azure Storage is designed to be massively scalable to meet the data storage and performance needs of today's applications.
* **Manageability**. Azure handles hardware maintenance, updates, and critical issues for you.
* **Accessibility**. Data in Azure Storage is accessible from anywhere in the world over HTTP or HTTPS. Microsoft provides client libraries for Azure Storage in a variety of languages, including .NET, Java, Node.js, Python, PHP, Ruby, Go, and others, as well as a mature REST API. Azure Storage supports scripting in Azure PowerShell or Azure CLI. And the Azure portal and Azure Storage Explorer offer easy visual solutions for working with your data.
</edukamu-section>
<br>

The following are the main data services available for Azure Storage users. Some of them might be a little tough to grasp, but there’s no hurry – take your time!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Blob Storage
</edukamu-collapse-hidden-title>

Azure Blob Storage is an object storage solution for the cloud. It can store massive amounts of data, such as text or binary data. Azure Blob Storage is unstructured, meaning that there are no restrictions on the kinds of data it can hold. Blob Storage can manage thousands of simultaneous uploads, massive amounts of video data, constantly growing log files, and can be reached from anywhere with an internet connection.

Blobs aren't limited to common file formats. A blob could contain gigabytes of binary data streamed from a scientific instrument, an encrypted message for another application, or data in a custom format for an app you're developing. One advantage of blob storage over disk storage is that it doesn't require developers to think about or manage disks. Data is uploaded as blobs, and Azure takes care of the physical storage needs.

Blob storage is ideal for:

* Serving images or documents directly to a browser.
* Storing files for distributed access.
* Streaming video and audio.
* Storing data for backup and restore, disaster recovery, and archiving.
* Storing data for analysis by an on-premises or Azure-hosted service.

### Accessing Blob Storage

Objects in Blob storage can be accessed from anywhere in the world via HTTP or HTTPS. Users or client applications can access blobs via URLs, the Azure Storage REST API, Azure PowerShell, Azure CLI, or an Azure Storage client library. The storage client libraries are available for multiple languages, including .NET, Java, Node.js, Python, PHP, and Ruby.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Files
</edukamu-collapse-hidden-title>

Azure Files offers fully managed file shares in the cloud that are accessible via the industry standard Server Message Block (SMB) or Network File System (NFS) protocols. Azure Files file shares can be mounted concurrently by cloud or on-premises deployments. SMB Azure file shares are accessible from Windows, Linux, and macOS clients. NFS Azure Files shares are accessible from Linux or macOS clients. Additionally, SMB Azure file shares can be cached on Windows Servers with Azure File Sync for fast access near where the data is being used.

Azure Files key benefits:

* **Shared access**: Azure file shares support the industry standard SMB and NFS protocols, meaning you can seamlessly replace your on-premises file shares with Azure file shares without worrying about application compatibility.
* **Fully managed**: Azure file shares can be created without the need to manage hardware or an OS. This means you don't have to deal with patching the server OS with critical security upgrades or replacing faulty hard disks.
* **Scripting and tooling**: PowerShell cmdlets and Azure CLI can be used to create, mount, and manage Azure file shares as part of the administration of Azure applications. You can create and manage Azure file shares using Azure portal and Azure Storage Explorer.
* **Resiliency**: Azure Files has been built from the ground up to always be available. Replacing on-premises file shares with Azure Files means you don't have to wake up in the middle of the night to deal with local power outages or network issues.
* **Familiar programmability**: Applications running in Azure can access data in the share via file system I/O APIs. Developers can therefore leverage their existing code and skills to migrate existing applications. In addition to System IO APIs, you can use Azure Storage Client Libraries or the Azure Storage REST API.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Queue Storage
</edukamu-collapse-hidden-title>

Azure Queue Storage is a service for storing large numbers of messages. Once stored, you can access the messages from anywhere in the world via authenticated calls using HTTP or HTTPS. A queue can contain as many messages as your storage account has room for (potentially millions). Each individual message can be up to 64 KB in size. Queues are commonly used to create a backlog of work to process asynchronously.

Queue storage can be combined with compute functions like Azure Functions to take an action when a message is received. For example, you want to perform an action after a customer uploads a form to your website. You could have the submit button on the website trigger a message to the Queue storage. Then, you could use Azure Functions to trigger an action once the message was received.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Disk Storage
</edukamu-collapse-hidden-title>

Disk storage, or Azure managed disks, are block-level storage volumes managed by Azure for use with Azure VMs. Conceptually, they’re the same as a physical disk, but they’re virtualized – offering greater resiliency and availability than a physical disk. With managed disks, all you have to do is provision the disk, and Azure will take care of the rest.

</edukamu-collapse>

How does it seem so far? Azure offers quite an expansive catalog of services for all your storage needs, as you can see!  
<br>
<br>
Next, let's see how Azure addresses all your data migration needs.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
