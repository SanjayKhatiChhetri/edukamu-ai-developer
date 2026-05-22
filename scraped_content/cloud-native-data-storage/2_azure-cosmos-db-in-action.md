## Azure Cosmos DB in Action

Welcome to the second unit! By now, you should have a clear understanding of what the role of database services are in application development and what differentiates NoSQL databases from their SQL counterparts.

While Microsoft Azure Cosmos DB can be used for both NoSQL and relational database needs, we'll be focusing on the first during this course. That is because, for every aspiring AI developer, NoSQL database solutions will surely become very familiar at some point!

In this unit, we'll get started with Azure Cosmos DB on a practical level. We'll set up some resources, containers, and even simple data solutions. Understanding these basic tools and capabilities makes grasping more evolved concepts in the third unit a lot more accessible.

Without further ado, let's get working with Microsoft Azure Cosmos DB! Essentially, we'll find out about its basic capabilities for client and server-side programming. In a while, these seemingly difficult terms will become clear, so let's begin!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Terminology 1: Server-Side and Client-Side Programming
</edukamu-collapse-hidden-title>

Client-side programming and server-side programming in Azure Cosmos DB refer to the different aspects of application development that involve interactions with the database. Let's explore this briefly.

### Client-Side Programming

**Definition:** Client-side programming in Azure Cosmos DB involves writing code or logic that runs on the *client side*, typically within your application or application server.

**Responsibility:** The client-side is responsible for tasks such as handling user inputs, executing application-specific business logic, and managing the communication with the Azure Cosmos DB service. In other words, it handles the things users write on an application, for example.

**Operations:** Client-side programming includes operations like creating queries, processing query results, and managing the data presentation layer.


### Server-Side Programming

**Definition:** Server-side programming in Azure Cosmos DB involves writing code or logic that runs on the *server side*, within the Cosmos DB service itself.

**Responsibility:** The server-side is responsible for tasks related to data storage, retrieval, and processing within the database. It manages the execution of queries and transactions.

**Operations:** Server-side programming includes defining stored procedures, triggers, and user-defined functions that execute within the database engine. These components help perform complex operations, validations, or modifications directly on the server.


### Key Takeaways

**Client-Side:** Primarily focuses on application-specific logic, user interactions, and managing the flow of data between the application and the Cosmos DB service.

**Server-Side:** Primarily focuses on database-related tasks, ensuring efficient data storage, retrieval, and processing within the Cosmos DB service.

</edukamu-collapse>
<br>


In summary, client-side programming handles application-specific logic, while server-side programming manages database-related tasks within Azure Cosmos DB. Keep this in mind as you advance on this course.

Before getting our hands dirty, let's review a few additional important concepts.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Terminology 2: Software Development Kits
</edukamu-collapse-hidden-title>

Soon, we'll start using Cosmos DB with something called Microsoft .NET SDK v3 for Azure Cosmos DB. In practice, it is a software development kit provided by Microsoft to to facilitate the integration and interaction of .NET applications with Azure Cosmos DB.

Say what? Let's go over the terminology we just encountered.

### 1. SDK (Software Development Kit)

An SDK is a set of tools, libraries, and documentation that enables developers to create applications for a specific software platform, framework, or service. There are SDKs for Android app development, for example.

SDKs provide pre-built functions and utilities that simplify complex tasks, allowing developers to interact with the target platform more efficiently. In essence, SDKs are to thank for making application development a lot more accessible than it was earlier!

### 2. .NET

.NET is a framework that provides a set of tools, libraries, and runtime for building and running applications on various platforms. In the context of software development, a "framework" refers to a pre-established and reusable set of tools, libraries, conventions, and best practices that provide a foundation for building software applications.

.NET facilitates the development of diverse applications, including web, desktop, mobile, cloud, and gaming applications.

### 3. Microsoft .NET SDK v3 for Azure Cosmos DB

This is an SDK tailored for .NET developers who want to build applications that leverage the capabilities of Azure Cosmos DB. Its key features include:

- **API Interaction:** The SDK enables .NET applications to perform operations such as querying, inserting, updating, and deleting data in Azure Cosmos DB.
- **Resource Management:** It provides tools for managing databases, collections, users, and permissions within Azure Cosmos DB.
- **Integration:** The SDK integrates seamlessly with .NET applications, ensuring smooth communication between the application and the Cosmos DB service.
- **Asynchronous Programming:** It supports asynchronous programming patterns, allowing developers to write efficient and responsive applications.

Microsoft regularly updates SDKs to enhance performance, security, and compatibility with the latest features of Azure Cosmos DB. The SDK version in question, v3, is the most current and up-to-date release, with more to come in the future.

</edukamu-collapse>
<br>


Here and there during this course, we'll be using commands written in the C# programming language. They'll be used when illustrating commands, so a basic understanding of the language is extremely helpful.

If you've never worked with C# before, we recommend that you take the crash course presented below. 

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### C# Crash Course
</edukamu-collapse-hidden-title>

The C# programming language allows you to build many types of applications, like:

- Business applications to capture, analyze, and process data
- Dynamic web applications that can be accessed from a web browser
- Games, both 2D and 3D
- Financial and scientific applications
- Cloud-based applications
- Mobile applications

But how do you begin to write an application?

Applications are all made up of many lines of code that work together to achieve a task. By far, the best way to learn how to code is to *write* code. Writing code yourself in each exercise and solving small coding challenges will accelerate your learning.

You'll also begin learning small foundational concepts and build on them with continual practice and exploration.

In this crash course, you'll:

- Write your first lines of C# code.
- Use two different techniques to print a message as output.
- Diagnose errors when code is incorrect.
- Identify different C# syntax elements like operators, classes, and methods.

By the end of this crash course, you'll be able to write C# code to print a message to the standard output of a console, like the Windows Terminal. These lines of code will give you your first look at the C# syntax, and immediately provide invaluable insights.

There is a handy practical introduction to C# available on Microsoft's Learn platform. It requires no subscriptions or signing in, so you can get started immediately! Just follow the instructions on your screen and get acquainted with programming!

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/csharp-write-first/2-exercise-hello-world">Microsoft Learn: Writing Your First Code</edukamu-button
<br>

To understand how your code works, you need to step back and think about what a programming language is. Consider how your code communicates commands to the computer.

### What is a Programming Language?

Programming languages like C# let you write instructions that you want the computer to carry out. Each programming language has its own syntax, but after learning your first programming language and attempting to learn another one, you'll quickly realize that they all share many similar concepts. A programming language's job is to allow a human to express their intent in a human-readable and understandable way. The instructions you write in a programming language are called "source code" or just "code". Software developers write code.

At this point, a developer can update and change the code, but the computer can't understand the code. The code first must be *compiled* into a format that the computer can understand.

### What is a Compilation?

A special program called a **compiler** converts your source code into a different format that the computer's central processing unit (CPU) can execute. When you used the green **Run** button in the previous unit, the code you wrote was first compiled, then executed.

Why does code need to be compiled? Although most programming languages seem cryptic at first, they can be more easily understood by humans than the computer's *preferred* language. The CPU understands instructions that are expressed by turning thousands or millions of tiny switches either on or off. Compilers bridge these two worlds by translating your human-readable instructions into a computer-understandable set of instructions.

### What is a Syntax?

The rules for writing C# code is called syntax. Just like human languages have rules regarding punctuation and sentence structure, computer programming languages also have rules. Those rules define the keywords and operators of C# and how they are put together to form programs.

When you wrote code into the .NET Editor, you may have noticed subtle changes to the color of different words and symbols. Syntax highlighting is a helpful feature that you'll begin to use to easily spot mistakes in your code that don't conform to the syntax rules of C#.

### How did Your Code Work?

Let's focus on the following line of code you wrote:

C#
```C#
Console.WriteLine("Hello World!");
```

When you ran your code, you saw that the message Hello World! was printed to the output console. When the phrase is surrounded by double-quotation marks in your C# code, it's called a **literal string**. In other words, you literally wanted the characters H, e, l, l, o, and so on, sent to the output.

The Console part is called a **class**. Classes "own" methods; or you could say that methods live inside of a class. To visit the method, you must know which class it's in. For now, think of a class as a way to represent an object. In this case, all of the methods that operate on your output console are defined inside of the Console class.

There's also a dot (or period) that separates the class name Console and the method name WriteLine(). The period is the *member access operator*. In other words, the dot is how you "navigate" from the class to one of its methods.

The WriteLine() part is called a **method**. You can always spot a method because it has a set of parentheses after it. Each method has one job. The WriteLine() method's job is to write a line of data to the output console. The data that's printed is sent in between the opening and closing parenthesis as an input parameter. Some methods need input parameters, while others don't. But if you want to invoke a method, you must always use the parentheses after the method's name. The parentheses are known as the *method invocation operator.*

Finally, the semicolon is the *end of statement operator*. A **statement** is a complete instruction in C#. The semicolon tells the compiler that you've finished entering the command.

Don't worry if all of these ideas and terms don't make sense. For now, all you need to remember is that if you want to print a message to the output console:

- Use ```Console.WriteLine("Your message here");```
- Capitalize Console, Write, and Line
- Use the correct *punctuation* because it has a special role in C#
- If you make a mistake, just spot it, fix it and re-run

**Tip:** Create a cheat sheet for yourself until you've memorized certain key commands.

It's important to understand the flow of execution. In other words, your code instructions were executed in order, one line at a time, until there were no more instructions to execute. Some instructions will require the CPU to wait before it can continue. Other instructions can be used to change the flow of execution.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Challenge: Problem Solving and Code
</edukamu-collapse-hidden-title>

Using your newly gained knowledge, try to complete the following challenge using the emulator available over at Microsoft Learn.

Your job is to write code in the .NET Editor to display two messages. Follow the instructions below and try to come up with a solution.

1. Select all of the code in the .NET Editor, and press Delete or Backspace to delete it.
2. Write new code that produces the following output:

```
This is the first line.
This is the second line.
```

Previously, you learned how to display a message in just one line of code, and you learned how to display a message using multiple lines of code. Use both techniques for this challenge. It doesn't matter which technique you apply to which line, and it doesn't matter how many ways you split one of the messages into multiple lines of code. That's your choice.

No matter how you do it, your code should produce the specified output - there are more solutions than one!

You'll find an example solution below.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Challenge: Example Solution
</edukamu-collapse-hidden-title>

The following code is one possible solution for the challenge from the previous unit.

C#

```C#
Console.WriteLine("This is the first line.");

Console.Write("This is ");
Console.Write("the second ");
Console.Write("line.");
```

Remember that this code is just *one possible solution*, among many possible ways to achieve the same result. However, you should have used both the Console.WriteLine() and Console.Write(String) methods to produce the desired output.

```
This is the first line.
This is the second line.
```

If you were successful, congratulations! If not, review the solutions described here and try to come up with one of your own before moving on. Programming is as much about problem solving as it is about writing code!

We hope you enjoyed the crash course presented here!

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
The C# language examples presented during this course are more complicated than the ones covered in the crash course, but this basic knowledge will certainly come in handy as you move forward on this course. Spend all the time you need with the examples presented and try to understand them – this way you'll not only learn about global database services but also reinforce your programming skills!

Now that we've established the basics, let's move straight on to Cosmos DB. If at any point something becomes unclear, feel free to return to the terminology sections above.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Exploring Microsoft .NET SDK v3 for Azure Cosmos DB
</edukamu-collapse-hidden-title>

Soon, we'll set up some resources using the SDK we just covered. Below are examples showing some of the key operations you should be familiar with in order to create more complicated resources. If you're new to software development, you can just follow the examples provided later.

### CosmosClient

The CosmosClient allows for creating, reading, updating, and deleting databases, containers, and documents within the Azure Cosmos DB service. It serves as the entry point for developers to connect their applications with the Cosmos DB service and perform various database operations.

It creates a new CosmosClient with a connection string. CosmosClient is thread-safe. It's recommended to maintain a single instance of CosmosClient per lifetime of the application that enables efficient connection management and performance.

```C#
CosmosClient client = new CosmosClient(endpoint, key);
```


### Database Examples

#### 1. Creating a Database

The ```CosmosClient.CreateDatabaseIfNotExistsAsync``` checks if a database exists, and if it doesn't, creates it. Only the database id is used to verify if there's an existing database.

C#

```C#
// An object containing relevant information about the response
DatabaseResponse databaseResponse = await client.CreateDatabaseIfNotExistsAsync(databaseId, 10000);
```

#### 2. Reading a Database by ID

This command reads a database from the Azure Cosmos DB service as an asynchronous operation.

C#

```C#
DatabaseResponse readResponse = await database.ReadAsync();
```

#### 3. Deleting a Database

This command deletes a Database as an asynchronous operation.

C#

```C#
await database.DeleteAsync();
```

### Container Examples

#### 1. Creating a Container

The ```Database.CreateContainerIfNotExistsAsync``` method checks if a container exists, and if it doesn't, it creates it. Only the container id is used to verify if there's an existing container.

C#

```C#
// Set throughput to the minimum value of 400 RU/s
ContainerResponse simpleContainer = await database.CreateContainerIfNotExistsAsync(
    id: containerId,
    partitionKeyPath: partitionKey,
    throughput: 400);
```

#### 2. Getting a Container by ID

C#

```C#
Container container = database.GetContainer(containerId);
ContainerProperties containerProperties = await container.ReadContainerAsync();
```

#### 3. Deleting a Container

A command to delete a Container as an asynchronous operation.

C#

```C#
await database.GetContainer(containerId).DeleteContainerAsync();
```

### Item Examples

#### 1. Creating an Item

Use the ```Container.CreateItemAsync``` method to create an item. The method requires a JSON serializable object that must contain an id property, and a partitionKey.

C#

```C#
ItemResponse<SalesOrder> response = await container.CreateItemAsync(salesOrder, new PartitionKey(salesOrder.AccountNumber));
```

#### 2. Reading an Item

Use the ```Container.ReadItemAsync``` method to read an item. The method requires type to serialize the item to along with an id property, and a partitionKey.

C#

```C#
string id = "[id]";
string accountNumber = "[partition-key]";
ItemResponse<SalesOrder> response = await container.ReadItemAsync(id, new PartitionKey(accountNumber));
```

#### 3. Querying an Item

The ```Container.GetItemQueryIterator``` method creates a query for items under a container in an Azure Cosmos database using a SQL statement with parameterized values. It returns a FeedIterator.

C#

```C#
QueryDefinition query = new QueryDefinition(
    "select * from sales s where s.AccountNumber = @AccountInput ")
    .WithParameter("@AccountInput", "Account1");

FeedIterator<SalesOrder> resultSet = container.GetItemQueryIterator<SalesOrder>(
    query,
    requestOptions: new QueryRequestOptions()
    {
        PartitionKey = new PartitionKey("Account1"),
        MaxItemCount = 1
    });
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Using the SDK to Create Resources in Azure Cosmos DB
</edukamu-collapse-hidden-title>

**Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

In this exercise you create a console app to perform the following operations in Azure Cosmos DB:

- Connect to an Azure Cosmos DB account
- Create a database
- Create a container

**Prerequisites:**

- An Azure account with an active subscription. If you don't already have one, you can sign up for a free trial at <edukamu-link url="https://azure.com/free" target="_blank">https://azure.com/free</edukamu-link>.
- Visual Studio Code on one of the supported platforms.
- The C# extension for Visual Studio Code.

In this practice exercise, we'll use the programming language C#. Even if you're not familiar with it, don't worry - you can get by just by following an example!


### Step 1. Setting Up Azure

#### 1. Connecting to Azure

a. Start Visual Studio Code and open a terminal window by selecting **Terminal** from the top application bar, then choosing **New Terminal**.

b. Sign in to Azure by using the following command. A browser window should open letting you choose which account to sign in with.

```az login```

#### 2. Create Resources in Azure

a. Create a resource group for the resources needed for this exercise. Replace `< myLocation >` with a region near you.

```
az group create --location <myLocation> --name az204-cosmos-rg
```

b. Create the Azure Cosmos DB account. Replace `< myCosmosDBacct >` with a *unique* name to identify your Azure Cosmos DB account. The name can only contain lowercase letters, numbers, and the hyphen (-) character. It must be between 3-31 characters in length. *This command takes a few minutes to complete*.

```
az cosmosdb create --name <myCosmosDBacct> --resource-group az204-cosmos-rg
```

c. Retrieve the primary key for the account by using the following command. Record the primaryMasterKey from the command results it will be used in the code.

```PowerShell
# Retrieve the primary key
az cosmosdb keys list --name <myCosmosDBacct> --resource-group az204-cosmos-rg
```
<br>
<br>


### Step 2. Setting up the Console Application

Now that the needed resources are deployed to Azure the next step is to set up the console application using the same terminal window in Visual Studio Code.

a. Create a folder for the project and change in to the folder.

```PowerShell
md az204-cosmos
cd az204-cosmos
```

b. Create the .NET console app.

```dotnet new console```

c. Open the current folder in Visual Studio Code using the following command. The -r option opens the folder without launching a new Visual Studio Code window.

```code . -r```

d. Select the *Program.cs* file in the **Explorer** pane to open the file in the editor.
<br>
<br>


### Step 3. Building the Console App

It's time to start adding the packages and code to the project. Ready?

#### 1. Adding Packages and Using Statements

a. Open the terminal in Visual Studio Code and use the following command to add the Microsoft.Azure.Cosmos package to the project.

```dotnet add package Microsoft.Azure.Cosmos```

b. Delete any existing code in the Program.cs file and add the using Microsoft.Azure.Cosmos statement.

C#

```C#
using Microsoft.Azure.Cosmos;
```

#### 2. Adding Code and Connecting to Azure Cosmos DB

a. Add the following code snippet after the using statement. The code snippet adds constants and variables into the class and adds some error checking. Be sure to replace the placeholder values for EndpointUri and PrimaryKey following the directions in the code comments.

```C#
C#
public class Program
{
    // Replace <documentEndpoint> with the information created earlier
    private static readonly string EndpointUri = "<documentEndpoint>";

    // Set variable to the Primary Key from earlier.
    private static readonly string PrimaryKey = "<your primary key>";

    // The Cosmos client instance
    private CosmosClient cosmosClient;

    // The database we will create
    private Database database;

    // The container we will create.
    private Container container;

    // The names of the database and container we will create
    private string databaseId = "az204Database";
    private string containerId = "az204Container";

    public static async Task Main(string[] args)
    {
        try
        {
            Console.WriteLine("Beginning operations...\n");
            Program p = new Program();
            await p.CosmosAsync();

        }
        catch (CosmosException de)
        {
            Exception baseException = de.GetBaseException();
            Console.WriteLine("{0} error occurred: {1}", de.StatusCode, de);
        }
        catch (Exception e)
        {
            Console.WriteLine("Error: {0}", e);
        }
        finally
        {
            Console.WriteLine("End of program, press any key to exit.");
            Console.ReadKey();
        }
    }
    //The sample code below gets added below this line
}
```

b. Below the Main method, add a new asynchronous task called CosmosAsync, which instantiates our new CosmosClient and adds code to call the methods you add later to create a database and a container.

C#

```C#
public async Task CosmosAsync()
{
    // Create a new instance of the Cosmos Client
    this.cosmosClient = new CosmosClient(EndpointUri, PrimaryKey);

    // Runs the CreateDatabaseAsync method
    await this.CreateDatabaseAsync();

    // Run the CreateContainerAsync method
    await this.CreateContainerAsync();
}
```

#### 3. Creating a Database

Copy and paste the CreateDatabaseAsync method after the CosmosAsync method. CreateDatabaseAsync creates a new database with ID az204Database if it doesn't already exist.

C#

```C#
private async Task CreateDatabaseAsync()
{
    // Create a new database using the cosmosClient
    this.database = await this.cosmosClient.CreateDatabaseIfNotExistsAsync(databaseId);
    Console.WriteLine("Created Database: {0}\n", this.database.Id);
}
```

#### 4. Creating a Container

Copy and paste the CreateContainerAsync method below the CreateDatabaseAsync method.

C#

```C#
private async Task CreateContainerAsync()
{
    // Create a new container
    this.container = await this.database.CreateContainerIfNotExistsAsync(containerId, "/LastName");
    Console.WriteLine("Created Container: {0}\n", this.container.Id);
}
```

#### 5. Running the Application

a. Save your work and, in a terminal in Visual Studio Code, run the dotnet build command to check for any errors. If the build is successful run the dotnet run command. The console displays the following messages.

```
Beginning operations...

Created Database: az204Database

Created Container: az204Container

End of program, press any key to exit.
```

b. Verify the results by opening the Azure portal, navigating to your Azure Cosmos DB resource, and use the **Data Explorer** to view the database and container.

#### 6. Cleaning Up Azure Resources

You can now safely delete the *az204-cosmos-rg* resource group from your account by running the following command.

```az group delete --name az204-cosmos-rg --no-wait```

</edukamu-collapse>
<br>


Did you manage to make it until the end? In the previous practice exercise, we set up a simple database to be used in Azure Cosmos DB. It is the very first step when starting to use the service, even though, with no real-life application to connect to, such maneuvers might seem difficult to understand.

Let's break down the process, shall we? Take time to go through the following section carefully. It is important that you understand what happens beneath the surface here, since it will make it easier to grasp the upcoming contents of this course.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Breaking Down the Process
</edukamu-collapse-hidden-title>

Let's break down the previous practice exercise, step by step.

### Step 1. Adding Packages and Using Statements:

- **Package Addition:** The dotnet add package Microsoft.Azure.Cosmos command adds the necessary package (Microsoft.Azure.Cosmos) to the project. This package provides the Azure Cosmos DB SDK for .NET, enabling interaction with Azure Cosmos DB.
- **Using Statements:** The using Microsoft.Azure.Cosmos; statement allows the code to reference types from the Azure Cosmos DB SDK without using fully qualified type names.


### Step 2. Adding Code and Connecting to Azure Cosmos DB:

- **Setting Constants and Variables:** Constants like EndpointUri and PrimaryKey are provided by Azure Cosmos DB and are specific to your Cosmos DB account. These are used to authenticate and connect to the Cosmos DB account.
- **CosmosClient Initialization:** The CosmosClient is instantiated using the provided EndpointUri and PrimaryKey. It serves as the entry point for interacting with Azure Cosmos DB.
- **Database and Container Information:** Constants like databaseId and containerId represent the names of the database and container that will be created.
- **Main Method:** The Main method is the entry point of the application. It instantiates the Program class and calls the CosmosAsync method.


### Step 3. Creating a Database (CreateDatabaseAsync Method):

- **Database Creation**: The CreateDatabaseAsync method uses the cosmosClient to create a new database with the specified ID (az204Database) if it doesn't already exist.
- **Real-life Scenario**: In a real-world scenario, creating a database might correspond to setting up a logical partition for different types of data. For example, a retail application might have separate databases for customer data, product catalog, and order information.


### Step 4. Creating a Container (CreateContainerAsync Method):

- **Container Creation:** The CreateContainerAsync method creates a new container within the database. It uses the /LastName path as the partition key, which determines how data is distributed across partitions.
- **Real-life Scenario:** In a business application, creating a container is analogous to defining a logical grouping of related documents. For instance, in an e-commerce platform, a container might be used for storing customer information, and the partition key could be based on the customer's last name.


### Step 5. Running the Application:

- **Execution:** The application is built and run using the dotnet build and dotnet run commands. The console output confirms the creation of the database and container.
- **Verification:** The results are verified in the Azure portal using the Data Explorer, ensuring that the specified database and container have been successfully created.
- **Real-life Scenario:** In a production environment, running the application would correspond to the deployment of a service that initializes the database and container upon startup.

In summary, the exercise demonstrates how to set up a .NET console application to connect to Azure Cosmos DB, create a database, and define a container. The real-life scenarios highlight the relevance of these actions in managing and organizing data in a cloud-based NoSQL database like Azure Cosmos DB.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Concrete Example: Worldwide Online Store
</edukamu-collapse-hidden-title>

Consider an e-commerce platform in which customer data, order details, and product information need efficient and scalable management:

1. **Database Creation:** A database named "eCommerceDB" is created to store all related data.
2. **Container Setup:** Within the database, containers like "CustomerData" and "OrderDetails" are established to logically group data.
3. **Partitioning:** Partition keys, such as customer ID for "CustomerData" and order ID for "OrderDetails," are chosen to distribute data evenly across physical partitions.
4. **Application Connection:** The e-commerce application connects to Azure Cosmos DB using the provided SDK, allowing seamless integration for data operations.

By following these steps, the e-commerce platform ensures organized data storage, efficient retrieval, and scalability to handle growing customer and transaction volumes.

</edukamu-collapse>
<br>


The process we just reviewed is a simplified example of a process that countless application developers, online retailers, and others have completed in order to start modernizing their databases and implementing adaptable, highly scalable NoSQL solutions with Azure Cosmos DB.

This section might have been a lot to take in, so feel free to rest for a while after completing the exercise below.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Setting Up Azure Cosmos DB
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/azure-cosmos-db-in-action-question-scroll-1.yaml" id="5ggr2uvw3wslf50o">
<br>

</edukamu-collapse>
<br>


On the next page, we'll build on the knowledge and expertise we gained on this one. After you've given your brain some time to relax and regroup, feel free to move on!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
