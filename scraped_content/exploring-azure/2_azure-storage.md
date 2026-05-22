<edukamu-video content="/videos/devai-1-unit2-video.yaml"/>
<br>

## Azure Storage

In the modern age more and more information is stored in data. We all carry it with us in our smartphones, laptops, and external storage devices, but it can also be stored in cloud. Imagine a huge corporation with multiple offices around the world. They all require access to the same data, and, luckily, Azure helps make is possible.

<!-- <edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="aineisto">
### YRITYS: Scenarios from Real Life
</edukamu-collapse-hidden-title>

Placeholder: Tähän tulee teksti, jossa kerrotaan tosielämän tilanteista.

</edukamu-collapse>
<br> -->

Azure Storage is a modern data storage solution that helps keep all your data safe and available. Be it large scale data objects, disk storage used by virtual machines, or reliable messaging service, there is a solution available.

The following video introduces the different storage services available in Azure Storage.

<!-- Tähän video osoitteesta: https://learn.microsoft.com/en-us/training/modules/describe-azure-storage-services/2-accounts    -->
<iframe width="640" height="360" src="https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed-one-stream.html?id=477e6b92-9bc6-425d-90fe-2468ab8ab0f1&locale=en-us&embedUrl=%2Ftraining%2Fmodules%2Fdescribe-azure-storage-services%2F2-accounts" frameborder="0" allowfullscreen></iframe>
<br>

An Azure account is needed in order to use the Storage service. When creating a storage account, you will start by picking the storage account type. The type of account determines the storage services and redundancy options and has an impact on the use cases. 

A storage account provides a unique namespace for your Azure Storage data that's accessible from anywhere in the world over HTTP or HTTPS. Data in this account is secure, highly available, durable, and massively scalable.

“That all sounds promising”, you might think, “but there are risks. How can I be sure my data is safe since I don’t have a physical copy on me?” That’s a fair question, and the answer is Azure Storage Redundancy. 

Have a glance on the following information. You should be aware of storage redundancy options on Azure, but they are not something we will focus on for too long on this course. Afterwards, we’ll dig a little deeper into the storage services.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Storage Redundancy
</edukamu-collapse-hidden-title>

Azure Storage always stores multiple copies of your data so that it's protected from planned and unplanned events such as transient hardware failures, network or power outages, and natural disasters. Redundancy ensures that your storage account meets its availability and durability targets even in the face of failures.

When deciding which redundancy option is best for your scenario, consider the tradeoffs between lower costs and higher availability. The factors that help determine which redundancy option you should choose include:

* How your data is replicated in the primary region.
* Whether your data is replicated to a second region that is geographically distant to the primary region, to protect against regional disasters.
* Whether your application requires read access to the replicated data in the secondary region if the primary region becomes unavailable.


### 1. Redundancy in the primary region

Data in an Azure Storage account is always replicated three times in the primary region. Azure Storage offers two options for how your data is replicated in the primary region, locally redundant storage (LRS) and zone-redundant storage (ZRS).

#### Locally redundant storage

Locally redundant storage (LRS) replicates your data three times within a single data center in the primary region. LRS provides at least 11 nines of durability (99.999999999%) of objects over a given year.

<edukamu-image url="/graphics/module2/locally-redundant-storage.png" alt="Diagram showing the structure used for locally redundant storage." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

LRS is the lowest-cost redundancy option and offers the least durability compared to other options. LRS protects your data against server rack and drive failures. However, if a disaster such as fire or flooding occurs within the data center, all replicas of a storage account using LRS may be lost or unrecoverable. To mitigate this risk, Microsoft recommends using zone-redundant storage (ZRS), geo-redundant storage (GRS), or geo-zone-redundant storage (GZRS).

#### Zone-redundant storage

For Availability Zone-enabled Regions, zone-redundant storage (ZRS) replicates your Azure Storage data synchronously across three Azure availability zones in the primary region. ZRS offers durability for Azure Storage data objects of at least 12 nines (99.9999999999%) over a given year.

<edukamu-image url="/graphics/module2/zone-redundant-storage.png" alt="Diagram showing ZRS, with a copy of data stored in each of three availability zones." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

With ZRS, your data is still accessible for both read and write operations even if a zone becomes unavailable. No remounting of Azure file shares from the connected clients is required. If a zone becomes unavailable, Azure undertakes networking updates, such as DNS repointing. These updates may affect your application if you access data before the updates have completed.

Microsoft recommends using ZRS in the primary region for scenarios that require high availability. ZRS is also recommended for restricting replication of data within a country or region to meet data governance requirements.


### 2. Redundancy in a secondary region

For applications requiring high durability, you can choose to additionally copy the data in your storage account to a secondary region that is hundreds of miles away from the primary region. If the data in your storage account is copied to a secondary region, then your data is durable even in the event of a catastrophic failure that prevents the data in the primary region from being recovered.

When you create a storage account, you select the primary region for the account. The paired secondary region is based on Azure Region Pairs, and can't be changed.

Azure Storage offers two options for copying your data to a secondary region: geo-redundant storage (GRS) and geo-zone-redundant storage (GZRS). GRS is similar to running LRS in two regions, and GZRS is similar to running ZRS in the primary region and LRS in the secondary region.

By default, data in the secondary region isn't available for read or write access unless there's a failover to the secondary region. If the primary region becomes unavailable, you can choose to fail over to the secondary region. After the failover has completed, the secondary region becomes the primary region, and you can again read and write data.

#### Geo-redundant storage

GRS copies your data synchronously three times within a single physical location in the primary region using LRS. It then copies your data asynchronously to a single physical location in the secondary region (the region pair) using LRS. GRS offers durability for Azure Storage data objects of at least 16 nines (99.99999999999999%) over a given year.

<edukamu-image url="/graphics/module2/geo-redundant-storage.png" alt="Diagram showing GRS, with primary region LRS replicating data to LRS in a second region." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

#### Geo-zone-redundant storage

GZRS combines the high availability provided by redundancy across availability zones with protection from regional outages provided by geo-replication. Data in a GZRS storage account is copied across three Azure availability zones in the primary region (similar to ZRS) and is also replicated to a secondary geographic region, using LRS, for protection from regional disasters. Microsoft recommends using GZRS for applications requiring maximum consistency, durability, and availability, excellent performance, and resilience for disaster recovery.

GZRS is designed to provide at least 16 nines (99.99999999999999%) of durability of objects over a given year.

<edukamu-image url="/graphics/module2/geo-zone-redundant-storage.png" alt="Diagram showing GZRS, with primary region ZRS replicating data to LRS in a second region." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

</edukamu-collapse>
<br>

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1.png" alt="Edukamu-progress-in-a-module-image">
