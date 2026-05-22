## Components of Cosmos DB for NoSQL

In many modern applications, data needs to be handled and managed in real-time in order to provide a seamless, continuous user experience regardless of traffic or geographical location. NoSQL services, such as Azure Cosmos DB, enable developers to accomplish such feats, no matter how unbelievable they might seem.

On the previous page, we started exploring Azure Cosmos DB for NoSQL, Microsoft's offering for all developers' NoSQL needs. Now, it's time to focus on the components core components. Afterwards, we'll consider a few resource-related questions and basic operations of the service.

Let's get to it, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Core Components of Azure Cosmos DB for NoSQL
</edukamu-collapse-hidden-title>

To begin using Azure Cosmos DB, you first create various resources in Azure such as accounts, databases, containers, and items.

<edukamu-image url="/graphics/module1/3-resource-hierarchy.png" alt="Diagram showing how an Azure Cosmos DB for NoSQL account is the parent resource to a database, which is itself a parent resource to a container." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; max-width: 70%;">
<br>

### Accounts

Accounts are the fundamental units of distribution and high availability. At the account level, you can configure the region\[s\] for your data in Azure Cosmos DB for NoSQL. Accounts also contain the globally unique DNS name used for API requests. You can also set the default consistency level for requests at the account level. You can manage or create accounts using the Azure portal, Azure Resource Manager templates, the Azure CLI, or Azure PowerShell.

(Azure CLI (Command-Line Interface) and Azure PowerShell are command-line tools provided by Microsoft Azure for interacting with and managing Azure resources in the cloud. Both offer similar capabilities, allowing users to create, configure, and manage Azure resources such as virtual machines, storage accounts, and databases, and you'll encounter them here and there on this course.)

### Databases

Each account can contain one or more Databases. A database is a logical unit of management for containers in Azure Cosmos DB for NoSQL.

### Containers

Containers are the fundamental unit of scalability in Azure Cosmos DB for NoSQL. With Azure Cosmos DB, you provision throughput at the container level. You can also optionally configure an indexing policy or a default time-to-live value at the container level. Azure Cosmos DB for NoSQL will automatically and transparently partition the data in a container.

### Items

The NoSQL API for Azure Cosmos DB stores individual documents in JSON format as items within the container. Azure Cosmos DB for NoSQL natively supports JSON files and can provide fast and predictable performance because write operations on JSON documents are atomic.

<edukamu-image url="/graphics/module1/3-item-hierarchy.png" alt="Diagram showing various items stored in a container." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; max-width: 70%;">
<br>

</edukamu-collapse>
<br>


Even though services like Azure Cosmos DB for NoSQL are immensely powerful, they can't handle all data at once. This is where a process called partitioning comes in.

Partition refers to a logical division of data within a database. It involves splitting a large dataset into smaller, more manageable pieces called partitions. Each partition is then stored and managed independently. The goal of partitioning is to distribute the data across different physical resources, enabling parallel processing and improving the overall performance and scalability of the database.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Partition & Partition Keys
</edukamu-collapse-hidden-title>

<iframe width="640" height="360" src="https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed-one-stream.html?id=8035d1e3-ff9c-4f26-96c6-1782b8274676&locale=en-us&embedUrl=%2Ftraining%2Fmodules%2Fintroduction-to-azure-cosmos-db-sql-api%2F3-how-does-work" frameborder="0" allowfullscreen></iframe>
<br>

Every Azure Cosmos DB for NoSQL container is required to specify **a partition key path**. Behind the scenes, Azure Cosmos DB for NoSQL uses this path to logically partition data using **partition key values**. For example, consider the following JSON document:

```JavaScript
{
  "id": "35b5bf7d-5f0e-4209-b7cb-8c5c70c3bb59",
  "deviceDisplayName": "shared-printer",
  "acquiredYear": 2019,
  "department": {
    "name": "information-technology",
    "metadata": {
      "location": "floor-5-unit-27"
    }
  },
  "queuedDocuments": [
    {
      "sender": "user-293749329",
      "sentTime": "2019-07-26T05:12:37",
      "pages": 5,
      "spoolRef": "3f4b759c-3230-4269-a88e-de7620ad91c0"
    },
    {
      "device": {
        "type": "mobile"
      },
      "sentTime": "2019-11-12T13:08:42",
      "spoolRefs": [
        "6a86682c-be5a-4a4a-bacd-96c4d1c7ece6",
        "79e78fe2-93aa-4688-89db-a7278b034aa6"
      ]
    }
  ]
}
```

If your container specifies a partition key **path** of /department/name, then the partition key **value** of this document would be information-technology. Behind the scenes, Azure Cosmos DB for NoSQL automatically manages the physical resources necessary to support your data workload.

</edukamu-collapse>
<br>


In Azure Cosmos DB, automatic partitioning allows users to designate a partition key for efficient item storage across multiple partitions, demanding careful consideration for optimal design based on query patterns and data distribution.

Selecting a partition key path for a container can be one of the most important design decisions for a new workload, so take your time whenever you use the service in a professional setting!

Next, we'll take a more practical approach to Cosmos DB for NoSQL. We'll start by reviewing basic resources and operations.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Basic Resources
</edukamu-collapse-hidden-title>

An Azure Cosmos DB for NoSQL account is composed of a basic hierarchy of resources that include:

- An account
- One or more databases
- One or more containers
- Many items

<edukamu-image url="/graphics/module1/2-hiearchy.png" alt="Diagram explaining the hierarchy of Azure Cosmos DB resources including an account, then a child set of databases, child set of containers, and then finally a child set of items." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; padding: 1%; max-width: 50%;">
<br>

Let's explore each item in this hierarchy.

### Accounts

Each tenant of the Azure Cosmos DB service is created by provisioning a database account. Accounts are the fundamental units of distribution and high availability. At the account level, you can configure the region\[s\] for your data in Azure Cosmos DB for NoSQL. Accounts also contain the globally unique DNS name used for API requests.

<edukamu-image url="/graphics/module1/2-account.png" alt="Diagram explaining the resource hierarchy with account highlighted and associated with a DNS name and key." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; padding: 1%;">
<br>

### Databases

A database is a logical unit of management for containers in Azure Cosmos DB for NoSQL. An Azure Cosmos DB database manages users, permissions, and containers. Within the database, you can find one or more containers. You can also elect to provision throughput for your data here at the database level.

<edukamu-image url="/graphics/module1/2-database-diag.png" alt="Diagram explaining the resource hierarchy with database highlighted and multiple example child containers." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; padding: 1%; max-width: 80%;">
<br>

### Containers

Containers are the fundamental unit of scalability in Azure Cosmos DB for NoSQL. Typically, you provision throughput at the container level. Azure Cosmos DB for NoSQL will automatically and transparently partition the data in a container. You can also optionally configure an indexing policy or a default time-to-live value at the container level.

<edukamu-image url="/graphics/module1/2-container-diag.png" alt="Diagram explaining the resource hierarchy with a set of containers highlighted." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; padding: 1%; max-width: 50%;">
<br>

### Items

An Azure Cosmos DB for NoSQL resource container is a schema-agnostic container of arbitrary user-generated JSON items. The NoSQL API for Azure Cosmos DB stores individual documents in JSON format as items within the container. Azure Cosmos DB for NoSQL natively supports JSON files and can provide fast and predictable performance because write operations on JSON documents are atomic.

Tip: Containers can also store JavaScript based stored procedures, triggers and user-defined-functions (UDFs).

<edukamu-image url="/graphics/module1/2-item.png" alt="Diagram explaining the resource hierarchy with items highlighted and other example children resources of containers." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; padding: 1%;">
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Setting Up an Account
</edukamu-collapse-hidden-title>

**Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

Let's take a look at account creation in Azure Cosmos DB. First, we'll review some basic information. Please notice that, as is the case with the most Microsoft Azure services, Cosmos DB also offers a free experience that you can use to explore the tools offered and covered on this course.

When creating a new account in the portal, you must first select an API for your workload. The API selection cannot be changed after the account is created. For the remainder of this section, we will assume that the NoSQL API has been selected.

<edukamu-image url="/graphics/module1/3-select-api.png" alt="Screenshot showing the select API option in the portal with a list of all current APIs including SQL, MongoDB, Graph, Table, and Cassandra." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

Next, the Azure portal will use a step-by-step wizard with tabs for various configuration options. Here you can configure options such as:

- The globally unique name of your account.
- The location (Azure region) for the account.
- Capacity mode (provisioned throughput or serverless).

<edukamu-image url="/graphics/module1/3-account-wizard.png" alt="Screenshot showing the wizard with various tabs and options for creating a new Azure Cosmos DB for NoSQL account." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

**Note:** Only the options in the Basics tab are required to create an Azure Cosmos DB account.

It's time to set up your Azure Cosmos DB account! Make sure to read the information below carefully before getting started.

### Using Microsoft Lab

Using Microsoft Azure Cosmos DB requires a lab environment, which can be accessed using your favorite browser. You can explore the lab environment free of charge.

**Note:** A lab is essentially a virtual machine (VM) containing the client tools you need, along with the exercise instructions.

However, notice, that labs include paid elements and may not be available everywhere. We recommend that you complete the practice exercises, but they are not a requirement for completing the course, as stressed earlier.

Microsoft provides this lab experience and related content for educational purposes. All presented information is owned by Microsoft and intended solely for learning about the covered products and services in this course.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/try-azure-cosmos-db-sql-api/4-exercise-create-account?launch-lab=true">Lab: Setting Up Azure Cosmos DB</edukamu-button>
<br>

(After opening the link, activate the Lab environment by clicking on the button shown below and filling in the information. According to current usage, it might take a few minutes for your lab to be set up.)

<edukamu-image url="/graphics/module1/lab.png" alt="Image displaying the button for activating Microsoft's lab environment." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

The lab will open into a new browser window and should look familiar if you've ever used Windows 11 before. Please notice the password on the right-hand side.

<edukamu-image url="/graphics/module1/lab-2.png" alt="Image displaying an activated lab environment with a sign-in screen." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

After signing in, this is what the lab environment looks like. Notice the detailed instructions on the right-hand side.

<edukamu-image url="/graphics/module1/lab-3.png" alt="Image displaying an activated lab environment after signing in." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

Notice that using the lab environment requires a Microsoft account with an active Azure trial subscription.  

**Tip:** Alternatively, if you would like to use a development environment on your own computer, you can use this <edukamu-link url="https://github.com/microsoftlearning/dp-420-cosmos-db-dev/blob/main/instructions/00-setup-environment.md" target="_blank">setup guide</edukamu-link> and follow these <edukamu-link url="https://github.com/microsoftlearning/dp-420-cosmos-db-dev/blob/main/instructions/01-create-account.md" target="_blank">exercise instructions</edukamu-link>. The setup guide is designed for multiple development exercises and may include software that is not required for this specific exercise.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
Were you able to create an account to be used with Azure Cosmos DB? If you did, great! That way you'll gain an upper hand by exploring all the services we cover on this course.

If you can't create an account for some reason, don't worry. Just focus on carefully going through the course contents – the practices don't include anything that isn't covered in the theory sections!

All right, let's review a few things that you should keep in mind as you use Azure Cosmos DB, whether it be now or in the future.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Setting Up Resources
</edukamu-collapse-hidden-title>

### Creating Databases

Databases are logical units of management in Azure Cosmos DB for NoSQL, and don't require much to create. You only need a unique database name within the account to create a new database.

**Note:** However, if you choose to provision throughput at the database level, configuring the database may require additional steps. This is explored deeper in other Azure Cosmos DB for NoSQL topics.

### Creating Containers

Containers are the primary unit of scalability in Azure Cosmos DB for NoSQL. When creating a container, you should specify:

- The parent database
- A unique name for the container with the database
- The path for the partition key value
- *Optional*: provisioned throughput if not inferred from database provisioning.

The Azure Cosmos DB service will automatically and transparently partition your data based on the value of the partition key for each individual item.

### Creating Simple Items

Once the database and container resources exist, you are ready to create your first item. In Azure Cosmos DB for NoSQL, an item is a JSON document.

**Note:** JavaScript Object Notation (JSON) is an open standard file format, and data interchange format, that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and array data types (or any other serializable value).

JSON is a language-independent data format with well-defined data types and near universal support across a diverse range of services and programing languages. Here is an example of a JSON document that could be an item in an Azure Cosmos DB account:

```JavaScript
{
  "id": "0012D555-C7DE",
  "type": "customer",
  "fullName": "Franklin Ye",
  "title": null,
  "emailAddress": "fye@cosmic.works",
  "creationDate": "2014-02-05",
  "addresses": [
    {
      "addressLine": "1796 Westbury Drive",
      "cityStateZip": "Melton, VIC 3337 AU"
    },
    {
      "addressLine": "9505 Hargate Court",
      "cityStateZip": "Bellflower, CA 90706 US"
    }
  ],
  "password": {
    "hash": "GQF7qjEgMk=",
    "salt": "12C0F5A5"
  },
  "salesOrderCount": 2
}
```

</edukamu-collapse>
<br>


Azure Cosmos DB for NoSQL might still seem quite confusing at this point, but the main thing is to understand why the service is used. There will be plenty of information on the how department during the following units.

It's time to complete the last exercise of the first unit!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Cosmos DB for NoSQL
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/components-of-cosmos-db-for-nosql-question-scroll-1.yaml" id="on7fes2obcurzbsh">
<br>

</edukamu-collapse>
<br>


That's the first unit in the bag, awesome job!

During the following units, we'll encounter some pretty technical concepts. While we'll be trying to keep things practical, using Cosmos DB requires a strong base on which to build, which is why we recommend that you take a moment to review everything we've covered so far before moving on.

Take your time and remember to enjoy the learning process. See you in the second unit!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
