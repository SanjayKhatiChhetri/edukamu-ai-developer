## Connecting to a NoSQL Database

Welcome to the third and final unit of this course!

After thoroughly inspecting the basic capabilities and use scenarios of global database solutions, such as Azure Cosmos DB, and learning about the possibilities offered by NoSQL databases, it's time to implement everything we've learned into action.

In this unit, we'll set up a NoSQL database with Azure Cosmos DB. We'll get acquainted with a software development kit (SDK) used in the process and look at various ways in which it can be configured. Later, we'll wrap up the course by further exploring a few more advanced possibilities available within Microsoft Azure Cosmos DB.

This page, however, is all about connecting to Azure Cosmos DB for NoSQL with SDKs. Let's review what this means in practice.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Connecting NoSQL with SDKs
</edukamu-collapse-hidden-title>

When talking about connecting to Azure Cosmos DB for NoSQL with SDKs, we're referring to the process of establishing a connection and communication between a .NET application and an Azure Cosmos DB NoSQL database using a software development kit (or SDK) called Microsoft.Azure.Cosmos.NET.

In simpler terms, it involves configuring and utilizing the SDK to interact with the Azure Cosmos DB service.

Let's break down the process before exploring it further:

### Step 1. Configuration

Developers use the SDK to configure connection parameters, such as Cosmos DB account credentials, endpoint URIs, and other settings required to establish a secure and authenticated connection.

Think of this like setting up your phone to connect to the Internet. Developers use the SDK (a set of tools) to tell the application how to connect securely to the Cosmos DB or another NoSQL service.

**Example:** Imagine entering your Wi-Fi password on your phone so that it securely connects to the Internet.

### Step 2. Initialization

The application initializes an instance of the CosmosClient class from the SDK. This client represents the main entry point for interacting with the Azure Cosmos DB service.

Now that the application knows how to connect, it creates a special tool (in this case, an instance of the CosmosClient class) that acts like a front door to the Cosmos DB service.

**Example:** After setting up your phone for Wi-Fi, it's like turning on your web browser to access the Internet.

### Step 3. Authentication

The SDK handles authentication mechanisms, ensuring that the provided credentials are valid and secure. This often involves using keys or tokens to authenticate the application with the Cosmos DB service.

In essence, the SDK takes care of making sure the application is who it says it is. It's like using a special key or token to prove that your phone is allowed to use the internet.

**Example:** After connecting to Wi-Fi, your phone might use a security key or password to ensure it's allowed to access the Internet using the network.

### Step 4. Communication

With a successfully established connection, the application can use the SDK to perform various operations on the Cosmos DB database. This includes tasks such as querying, inserting, updating, or deleting documents, as well as other administrative operations.

In practice, now that everything is set up and secure, the application can talk to the Cosmos DB service. It can ask questions, add new information, update things, or even delete stuff using the tools provided by the SDK.

**Example:** After connecting to the Internet, you can do things like searching for information, watching videos, or updating social media on your phone using a web browser of your choice.

### Step 5. Error Handling

The SDK provides mechanisms for handling errors that may occur during the communication process, ensuring robustness in the application's interactions with the Cosmos DB service.

Sometimes things may go wrong, like a webpage not loading. The SDK helps the application deal with these issues, ensuring it can recover from problems.

**Example:** If a webpage doesn't load, your web browser might show an error message or try to reload the page without crashing.

By connecting to Azure Cosmos DB using the SDK, developers can seamlessly integrate NoSQL database capabilities into their .NET applications, enabling efficient data storage, retrieval, and management. This connection facilitates the creation of dynamic and scalable applications that leverage the features of Azure Cosmos DB for handling diverse data requirements.

In simpler terms, it's like preparing your phone to securely connect to the internet, opening a browser to access the web, making sure it's allowed to use the internet, doing things online, and handling any issues that may come up along the way.

</edukamu-collapse>
<br>


Essentially, SDKs are like little toolboxes that provide developers with various capabilities, in this case making it easier to connect, configure, and communicate with the Azure Cosmos DB service.

(If you feel like refreshing your memory about SDKs and .NET, feel free to circle back to the terminology sections on the **Azure Cosmos DB in Action** page.)

Without further ado, let's get started with the SDKs!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Cosmos DB for NoSQL SDKs
</edukamu-collapse-hidden-title>

There are various SDKs available to connect to the Azure Cosmos DB for NoSQL from many popular programming languages including, but not limited to:

- .NET (C#)
- Java
- Python
- JavaScript (Node.js).

For this section, you will explore and get hands-on with the .NET SDK for the Azure Cosmos DB for NoSQL.

### Understanding the SDK

The **Microsoft.Azure.Cosmos** library is the latest version of the .NET SDK for Azure Cosmos DB for NoSQL.

The library is open-source and hosted online on GitHub at **azure/azure-cosmos-dotnet-v3**. The open-source project conforms to the Microsoft Open Source Code of Conduct and accepts contributions and suggestions from the community.

The Microsoft.Azure.Cosmos library includes a namespace of the same name with common classes that you will explore later in this course including, but not limited to:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
Class
</edukamu-table-header>
<edukamu-table-header width="70%">
Description
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Microsoft.Azure.Cosmos.**CosmosClient**
</edukamu-table-cell>
<edukamu-table-cell>
Client-side logical representation of an Azure Cosmos DB account and the primary class used for the SDK
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Microsoft.Azure.Cosmos.**Database**
</edukamu-table-cell>
<edukamu-table-cell>
Logically represents a database client-side and includes common operations for database management
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Microsoft.Azure.Cosmos.**Container**
</edukamu-table-cell>
<edukamu-table-cell>
Logically represents a container client-side and includes common operations for container management
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


The Microsoft.Azure.Cosmos .NET SDK, which we've just started exploring, is a powerful and versatile tool for interfacing Azure Cosmos DB for NoSQL data storage. Designed to streamline the development process, this SDK is an essential component when setting up and interacting with the service within the .NET framework.

As mentioned earlier, .NET is just one of the programming languages that can be used with the SDKs and Cosmos DB. We've chosen to use it since, while being among the easiest to understand, it's still a capable choice.

Next, we'll delve deeper into the process by reviewing package managers, online accounts, and connectivity modes.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Importing from Package Managers
</edukamu-collapse-hidden-title>

The Microsoft.Azure.Cosmos library, including all of its previous versions, are hosted on **nuget** to make it easier to import the library into a .NET application.

Package managers are tools that help manage dependencies in software projects by handling the installation, configuration, and updating of external libraries or packages.

NuGet is a popular package manager for .NET that simplifies the process of adding external libraries or packages to a .NET project. In simpler terms, this means that developers can easily import and use the "Microsoft.Azure.Cosmos" library in their .NET applications by including a reference to it through NuGet. They can simply specify the library as a dependency in their project, and NuGet takes care of fetching and incorporating the required files.

### Importing NuGet Packages

To import a NuGet package into a .NET application, you must use the .NET CLI. The CLI includes a dotnet add command that is used to add a resource to a .NET project. To specifically add a NuGet package, you must do one of the following things:

#### 1. Import the Latest Package Version

Invoke the dotnet add package command with only the name of the package. For example, this command will import the latest stable version of the Microsoft.Azure.**Cosmos** library.

Bash

```Bash
dotnet add package Microsoft.Azure.Cosmos
```

**Tip:** All commands displayed on this section will only import stable versions of the package. If a newer preview of the package is available, it will import the older stable version. If no stable version is available, it will not import the package at all.

#### 2. Import a Specific Version of the Package

Invoke the dotnet add package command with only the name of the package. For example, this command will import the latest stable version of the Microsoft.Azure.**Cosmos** library.

Bash

```Bash
dotnet add package Microsoft.Azure.Cosmos
```

### .NET Project Files

Once imported, the package specification will be added to the **csproj** file for the .NET project. The project file uses the XML format and a new element named **PackageReference** is created within the **ItemGroup** element with the name of the package and the version. In this example, the **3.22.1** version of the **Microsoft.Azure.Cosmos** library was imported into the project from NuGet.

XML

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="Microsoft.Azure.Cosmos" Version="3.22.1" />
  </ItemGroup>
</Project>
```

**Note:** The version of the package will be added whether you specfied it in the import command or not. If you did not specify a package version, the version of the latest stable package that was imported is specified in the project file.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
Connecting your application to an online database is akin to plugging in a cable to establish a connection. Once connected, you can inquire about the database, learning about its unique name and various locations.

After connecting, managing databases involves either finding an existing one or creating a new one. Within a database, data is organized into containers, analogous to folders. Managing these containers involves tasks like finding existing ones, creating new ones, or letting the toolbox take care of it seamlessly.

Next, let's explore this process from a more technical point of view.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Connecting to an Online Account
</edukamu-collapse-hidden-title>

Once the Microsoft.Azure.Cosmos library is imported, you can begin using the namespaces and classes within your .NET project.

Before using the library, you should import the **Microsoft.Azure.Cosmos** namespace using a **directive**. The using directive allows you to use types within the namespace without being forced to fully qualify each type.

C#

```C#
using Microsoft.Azure.Cosmos;
```

### 1. Using the CosmosClient Class

The two most common ways to create an instance for the **CosmosClient** class is to instantiate it with one of the following two constructors:

- A constructor that takes a single string value representing the connection string for the account.
- A constructor that takes two string values representing the endpoint and a key for the account.

You can also use the CosmosClient class with the Microsoft identity platform directly for Microsoft Entra authentication, but that is beyond the scope of this course.

#### a. Using Connection Strings

The **CosmosClient** class has a constructor that only takes a single string value. Pass in the connection string of the account to use this constructor. This example uses a connection string in the

```C#
AccountEndpoint=<account-endpoint>;AccountKey=<account-key>
```

format with the fictional endpoint and key.

C#

```C#
string connectionString = "AccountEndpoint=https-://dp420.documents.azure.com:443/;AccountKey=fDR2ci9QgkdkvERTQ==";

CosmosClient client = new (connectionString);
```

#### b. Using Endpoints and Keys

C#

```C#
string endpoint = "https¬://dp420.documents.azure.com:443/";
string key = "fDR2ci9QgkdkvERTQ==";

CosmosClient client = new (endpoint, key);
```

### 2. Reading Account Properties

Once the client instance is instantiated, you can use various methods directly. For example, you can asynchronously invoke the **ReadAccountAsync** method to get an object of type **AccountProperties** with various properties.

C#

```C#
AccountProperties account = await client.ReadAccountAsync();
```

The **AccountProperties** class includes useful properties such as, but not limited to:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
Property
</edukamu-table-header>
<edukamu-table-header>
Description
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**Id**
</edukamu-table-cell>
<edukamu-table-cell>
Gets the unique name of the account
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**ReadableRegions**
</edukamu-table-cell>
<edukamu-table-cell>
Gets a list of readable locations for the account
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**WritableRegions**
</edukamu-table-cell>
<edukamu-table-cell>
Gets a list of writable locations for the account
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Consistency**
</edukamu-table-cell>
<edukamu-table-cell>
Gets the default consistency level for the account
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section>
<br>

### 3. Interacting with Databases

Once you have a client instance, you can retrieve or create a database using one of three methods:

- Retrieve an existing database using the name
- Create a new database passing in a unique database name
- Have the SDK check for the existence of the database and either create or retrieve it automatically

Any of these three methods will return an instance of type **Database** that you can use to interact with the database.

#### a. Retrieving Existing Databases

C#

```C#
Database database = client.GetDatabase("cosmicworks");
```

#### b. Creating Additional Databases

C#

```C#
Database database = await client.CreateDatabaseAsync("cosmicworks");
```

#### c. Creating the First Database

C#

```C#
Database database = await client.CreateDatabaseIfNotExistsAsync("cosmicworks");
```

### 4. Interacting with Containers

Now that you have a database instance, you can retrieve or create a container using one of three methods:

- Retrieve an existing container using just the name
- Create a new container passing in a unique container name, partition key path, and the amount of throughput to manually provision
- Have the SDK check for the existence of the container and either create or retrieve it automatically

Any of these three methods will return an instance of type Container that you can use to interact with the container.

#### a. Retrieving Existing Containers

C#

```C#
Container container = database.GetContainer("products");
```

#### b. Creating Additional Containers

C#

```C#
Container container = await database.CreateContainerAsync(
    "products",
    "/categoryId",
    400
);
```

#### c. Creating the First Container

C#

```C#
Container container = await database.CreateContainerIfNotExistsAsync(
    "products",
    "/categoryId",
    400
);
```

</edukamu-collapse>
<br>


In essence, the above is like opening a toolbox, establishing a connection to an online database, discovering information about the database, and efficiently organizing data within databases and containers using different tools as needed.

The process described is not the only option to address this specific use scenario, however, but it's an effective one while remaining relatively simple.

Next, we'll explore connectivity modes, which basically means setting up the way your application interacts with Azure Cosmos DB, establishing and maintaining connections.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Configuring Connectivity Methods
</edukamu-collapse-hidden-title>

The **CosmosClientOptions** class provides a range of options that you can configure for the client when it connects to an account. These options include, but are not limited to:

- The mode used to connect to the account
- Custom consistency level used specifically for the client instance
- The preferred account region[s]

### Overriding Default Client Options

When connecting to an Azure Cosmos DB account using the **CosmosClient** class, there are a few assumptions that the client makes:

- That you will want to connect to the first writable (primary) region of your account
- That you will use the default consistency level for the account with your read requests
- That you will connect directly to data nodes for requests

To configure the client, you will need to create an instance of the **CosmosClientOptions** class and pass in that instance as the last parameter to the **CosmosClient** constructor. Here are two examples using the constructors discussed earlier.

You can either use the constructor that takes in an endpoint and key:

C#

```C#
CosmosClientOptions options = new ();

CosmosClient client = new (endpoint, key, options);
```

Or, use the constructor that takes in a connection string:

C#

```C#
CosmosClientOptions options = new ();

CosmosClient client = new (connectionString, options);
```

### Changing Connection Modes

Within the **CosmosClientOptions** class, you can set the **ConnectionMode** property to one of two possible enumerable values:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="25%">
Value
</edukamu-table-header>
<edukamu-table-header width="75%">
Description
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**Gateway**
</edukamu-table-cell>
<edukamu-table-cell>
All requests are routed through the Azure Cosmos DB gateway as a proxy
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Direct**
</edukamu-table-cell>
<edukamu-table-cell>
The gateway is only used in initialization and to cache addresses for direct connectivity to data nodes
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section>
<br>

The default setting is to use the **Direct** connection mode. This example configures the client to use the default settings.

C#

```C#
CosmosClientOptions options = new ()
{
    ConnectionMode = ConnectionMode.Direct
};
```

You can optionally configure the client to always use the gateway as a proxy for requests. This example configures the client to use the **Gateway** connection mode.

C#

```C#
CosmosClientOptions options = new ()
{
    ConnectionMode = ConnectionMode.Gateway
};
```

### Changing Consistency Levels

Every Azure Cosmos DB for NoSQL account has a default consistency level configured. Individual clients can configure a different consistency level for all read requests made with the client. This example illustrates a client configured to use **eventual** consistency.

C#

```C#
CosmosClientOptions options = new ()
{
    ConsistencyLevel = ConsistencyLevel.Eventual
};
```

The **ConsistencyLevel** enumeration has multiple potential values including:

- Bounded Staleness
- ConsistentPrefix
- Eventual
- Session
- Strong

The **ConsistencyLevel** setting is only used to only weaken the consistency level for reads. It cannot be strengthened or applied to writes.

### Setting Application Region(s)

By default, the client will use the first writable region for requests. This is typically referred to as the primary region. You can use either the **CosmosClientOptions.ApplicationRegion** or **CosmosClientOptions.ApplicationPreferredRegions** to override this behavior.

The **ApplicationRegion** property sets the single preferred region that the client will connect to for operations. If the configured region is unavailable, the client will default to the fallback priority list set on the account to determine the next region to use. In this example, the preferred region is configured to **West US**.

C#

```C#
CosmosClientOptions options = new ()
{
    ApplicationRegion = "westus"
};
```

If your account is not configured for multi-region write, the client will always use the single writable region for write operations and this setting will only impact read operations.

If you would like to create a custom failover/priority list for the client to use for operations, you can use the **ApplicationPreferredRegions** property with a list of regions. This example uses a custom list configured to try **West US** first and then **East US**.

C#

```C#
CosmosClientOptions options = new CosmosClientOptions()
{
    ApplicationPreferredRegions = new List<string> { "westus", "eastus" }
};
```

</edukamu-collapse>
<br>


Configuring connectivity mode is about tailoring the way your application communicates with Cosmos DB. It is based on factors like network configuration, location, and performance requirements.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Using Azure Cosmos DB with SDK
</edukamu-collapse-hidden-title>

**Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

This practice exercise also requires a lab environment to be completed. You'll once again get to use a Windows-based virtual machine provided by Microsoft. You'll also be provided step-by-step instructions on connecting to Azure Cosmos DB with an SDK.

You can access the lab environment by navigating to Microsoft Learn and using the button to activate the lab.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/use-azure-cosmos-db-sql-api-sdk/7-exercise-connect-to">Lab: Using Azure Cosmos DB with the SDK</edukamu-button>
<br>

Should you run any issues, please refer to the more detailed instructions on the page *Components of Cosmos DB for NoSQL*.

If you decide to take on the practice exercise, good luck! Enjoy the process!

</edukamu-collapse>
<br>


The process we've reviewed on this page involves connecting to Azure Cosmos DB with a software development kit. The process is quite advanced technically, and while we've tried to make it as clear and easy to understand as possible, you might still feel a little confused at this point.

If this is the care, don't worry! Have a look at the following instead.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Simplified Process Review
</edukamu-collapse-hidden-title>

Imagine you're developing an e-commerce platform, and you decide to use Azure Cosmos DB to store product information. Connecting to Azure Cosmos DB with the SDK is like setting up a streamlined communication channel between your e-commerce application and the Cosmos DB service.

In this scenario, the steps we've covered on this page would essentially mean the following.

**Importing from Package Manager:** You use a package manager to bring in the Azure Cosmos DB SDK, which is like getting a specialized toolkit for handling data operations. It's akin to equipping your application with the right tools to interact with the Cosmos DB service.

**Connecting to an Online Account:** You specify the details of your Cosmos DB account, such as its endpoint and access key. It's similar to providing your application with a secure key to access a physical "Cosmos DB warehouse" where all your product data is stored.

**Configuring Connectivity Mode:** Here, you decide how your application will communicate with Cosmos DB. It's like choosing the best route for your delivery trucks. If your products are frequently updated, you might opt for a mode that ensures real-time communication, ensuring your customers always see the latest product information.

Once these steps are completed, your e-commerce application can seamlessly read product details, update inventory, and add new items to the Cosmos DB "shelves."

The SDK acts as the bridge, facilitating smooth communication between your application and the NoSQL database. This ensures that your online store operates efficiently, providing customers with accurate and up-to-date product information.

</edukamu-collapse>
<br>


Do take some time to recap and review before completing the exercise below, since we'll keep using the SDK on the next page. It's important to make sure you understand everything explored so far before moving on.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Azure Cosmos DB and SDKs
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/connecting-to-a-nosql-database-question-scroll-1.yaml" id="02csnevy2wlojvuu">
<br>

</edukamu-collapse>
<br>


We've now reviewed setting up connections between NoSQL services like Azure Cosmos DB and an application using a software development kit. On the next page, we'll check out what we can do *to* the SDK to make it perfectly suitable for specific use scenarios.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
