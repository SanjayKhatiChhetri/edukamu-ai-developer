## Configuring the SDK

As we've noticed over the course of this micro degree, software development on Microsoft Azure is not just about creating applications, but also about crafting them to perform optimally and seamlessly integrate with essential services. When working with Azure Cosmos DB and different SDKs, customization becomes key.

Imagine you have a toolbox, and in this toolbox, you find not just the tools but also a manual on how to tweak those tools for different tasks, *your* specific tasks. This is precisely what configuring the Azure Cosmos DB SDK for .NET is all about – and it is exactly what we'll be focusing on next.

This process isn't just for the tech-savvy wizards; it's for everyday developers who want their applications to shine. Configuring the SDK allows you to tailor it to your team's needs, troubleshoot any hiccups, make things run faster, and even enable offline development for further flexibility.

On this page, we'll learn about configuring the software development kit we addressed before and make it perfectly suitable for every use scenario.

First, however, let's review a few important concepts.

<edukamu-tabs theme="edukamu-tabs1">

<edukamu-tabs-tab title="Terminology 1: Threading">
In our current context, threading is like having multiple hands working on different tasks at the same time. Imagine you're cooking in the kitchen – one person is chopping vegetables, another is stirring the pot, and yet another is setting the table.

Threading in the SDK allows your application to efficiently handle multiple tasks simultaneously, making sure everything gets done without waiting for one task to finish before starting another.

In simpler terms, it's like having a multitasking chef in your kitchen, ensuring that your application can process various requests or operations without slowing down.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="Terminology 2: Parallelism">
Parallelism is a bit like teamwork. When you have a big task, you can divide it among team members, and each member works on their part simultaneously. Similarly, in the context of Azure Cosmos DB and the .NET SDK, parallelism enables your application to break down a complex job into smaller tasks and work on them concurrently.

Think of it as assembling a puzzle with friends – everyone works on their corner, and the puzzle comes together faster. With parallelism in the SDK, your application becomes more efficient, handling tasks concurrently to deliver quicker results.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="Terminology 3: Logging">
Logging is like keeping a journal of what happens in your application. When you're on a road trip, you might jot down notes about interesting places you visit. In the SDK, logging allows your application to keep track of its activities – what operations it performs, any issues it encounters, or milestones it achieves.

In practical terms, it's akin to having a travel diary for your application, helping developers understand its journey, identify and fix problems, and improve performance. It's a valuable tool for troubleshooting and gaining insights into how your application interacts with Azure Cosmos DB.
</edukamu-tabs-tab>

</edukamu-tabs>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Terminology 1: Threading
</edukamu-collapse-hidden-title>

In our current context, threading is like having multiple hands working on different tasks at the same time. Imagine you're cooking in the kitchen – one person is chopping vegetables, another is stirring the pot, and yet another is setting the table.

Threading in the SDK allows your application to efficiently handle multiple tasks simultaneously, making sure everything gets done without waiting for one task to finish before starting another.

In simpler terms, it's like having a multitasking chef in your kitchen, ensuring that your application can process various requests or operations without slowing down.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Terminology 2: Parallelism
</edukamu-collapse-hidden-title>

Parallelism is a bit like teamwork. When you have a big task, you can divide it among team members, and each member works on their part simultaneously. Similarly, in the context of Azure Cosmos DB and the .NET SDK, parallelism enables your application to break down a complex job into smaller tasks and work on them concurrently.

Think of it as assembling a puzzle with friends – everyone works on their corner, and the puzzle comes together faster. With parallelism in the SDK, your application becomes more efficient, handling tasks concurrently to deliver quicker results.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Terminology 3: Logging
</edukamu-collapse-hidden-title>

Logging is like keeping a journal of what happens in your application. When you're on a road trip, you might jot down notes about interesting places you visit. In the SDK, logging allows your application to keep track of its activities – what operations it performs, any issues it encounters, or milestones it achieves.

In practical terms, it's akin to having a travel diary for your application, helping developers understand its journey, identify and fix problems, and improve performance. It's a valuable tool for troubleshooting and gaining insights into how your application interacts with Azure Cosmos DB.

</edukamu-collapse>
<br> -->


Just like adjusting the settings on your favorite app, configuring the Azure Cosmos DB SDK for .NET lets you fine-tune your development experience, ensuring your applications are finely crafted for success. Keep the above concepts in mind as we delve deeper into this interesting topic.

We'll start with enabling offline development and handling connection errors. Then, well move on to threading, parallelism, and logging. We'll be using the C# language again, so make sure to take your time with the contents of this page.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Enabling Offline Development
</edukamu-collapse-hidden-title>

As you begin to use Azure Cosmos DB across multiple projects, there will eventually be a need to use and test Azure Cosmos DB in a local environment where you can validate new code quickly without creating a new instance in the cloud. The Azure Cosmos DB emulator is a great tool for common Dev+Test workflows that developers may need to implement on their local machine.

### Azure Cosmos DB Emulator

The Azure Cosmos DB Emulator is a local, offline version of the Azure Cosmos DB service. It allows developers to test and develop applications without needing an internet connection or access to the actual Azure Cosmos DB service.

The emulator provides a simulated environment that replicates the functionality of Azure Cosmos DB, allowing developers to create and manage databases, containers, and documents locally on their development machines.

The emulator is available to run in **Windows**, **Linux**, or as a **Docker** container image.

The emulator is available as a download from the **Microsoft Docs** website and supports various APIs depending on the platform. The NoSQL API is universally supported across all platforms.

The Docker container image for the emulator is published to the Microsoft Container Registry and is syndicated across various container registries such as **Docker Hub**. To obtain the Docker container image from Docker Hub, use the Docker CLI to **pull** the image from mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator.

Bash

```Bash
docker pull mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator
```

### Configuring the SDK to Connect to the Emulator

The Azure Cosmos DB emulator uses the same APIs as the cloud service, so connecting to the emulator is not different from connecting to the cloud service. The emulator uses a single fixed account with a static authentication key that is the same across all instances.

First, the emulator's endpoint is

```bash
https://localhost:<port>/
```

using SSL with the default port set to 8081. In C# code, you can configure this endpoint as a string variable using this example line of code.

C#

```C#
string endpoint = "https://localhost:8081/";
```

The emulator's key is a static well-known authentication key. The default value for this key is C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==. In C# code, you can save this key as a variable using this example line of code.

C#

```C#
string key = "C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==";
```

**Tip:** You can start the emulator using the /Key option to generate a new key instead of using the default key.

Once those variables are set, create the **CosmosClient** like you typically would for a cloud-based account.

C#

```C#
CosmosClient client = new (endpoint, key);
```

And just like that, the Azure Cosmos DB is enabled, which allows you to continue testing and developing whenever and wherever you are, no matter the Internet conditions.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Handling Connection Errors
</edukamu-collapse-hidden-title>

While most of your requests are fine, there are some scenarios in which a request can fail for a temporary reason. In these scenarios, it's both normal and expected for you to retry your request after a reasonable amount of time.

### Built-in Retry

A transient error is an error that has an underlying cause that soon resolves itself. Applications that connect to your database should be built to expect these transient errors. The Azure Cosmos DB for NoSQL SDK for .NET has built-in logic to handle common transient failures for read and query requests. The SDK does NOT automatically retry write requests as they are not idempotent.

**Tip:** Try to always use the latest version of the SDK. The retry logic that is built-in is constantly being improved in newer releases.

If you are writing an application that experiences a write failure, it is up to your application code to implement retry logic which is considered a best practice.

As an application developer, it's important to understand the HTTP status codes where retrying your request makes sense. These codes include, but are not limited to:

- **429**: Too many requests
- **449**: Concurrency error
- **500**: Unexpected service error
- **503**: Service unavailable

**Tip:** If you experience 50x errors indicating issues with service availability, you can file an Azure support issue to receive technical support or report an issue.

There are HTTP error codes, such as **400 (bad request)**, **401 (not authorized)**, **403 (forbidden)**, and **404 (not found)** that indicate a failure client-side that should be fixed in application code and not retried.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
The SDK we're using to connect Azure Cosmos DB and a .NET application is quite flexible, as you see. Remember that this is not the only possible combination, as there are other NoSQL solutions and SDKs available as well. Microsoft Azure, with its vast pool of tools and services, is among the most versatile, though, while still remaining accessible for newcomers as well.

All right, it's time to get familiar with threading, parallelism, and logging!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Implementing Threading and Parallelism
</edukamu-collapse-hidden-title>

While the SDK implements thread-safe types and some degrees of parallelism, there are best practices that you can implement in your application code to ensure that the SDK has the best performance it can possibly have in your workload.

### Avoiding Resource-related Timeouts

Many times request timeouts occur due to high CPU or port utilization on client machines rather than a service-side issue. It is important to monitor resource utilization on client machines and scale-out appropriately to avoid SDK errors or retries due to local resource exhaustion.

### Using async/await in .NET

The C# language in .NET has a series of Task-based features to asynchronously invoke SDK client methods. For example, the **CreateDatabaseIfNotExistsAsync** method is invoked asynchronously using the following syntax.

C#

```C#
Database database = await client.CreateDatabaseIfNotExistsAsync("cosmicworks");
```

This syntax uses the **await** keyword to run the task asynchronously and return the result into the indicated variable. Using the asynchronous keywords allows the SDK to manage requests simultaneously in an efficient manner.

Avoid blocking the asynchronous execution using **Task.Wait** or **Task.Result** such as in the example code below.

C#

```C#
Database database = client.CreateDatabaseIfNotExistsAsync("cosmicworks").Result;
```

### Using Built-in Iterators Instead of LINQ

LINQ methods such as **ToList** will eagerly and synchronously drain a query while blocking any other calls from executing. For example, this invocation of ToList() will block all other calls and potentially retrieve a large set of data:

C#

```C#
container.GetItemLinqQueryable<T>()
    .Where(i => i.categoryId == 2)
    .ToList<T>();
```

The SDK includes methods such as

```C#
ToFeedIterator<T>
```

that asynchronously retrieves the results of a query without blocking other calls. This example illustrates the same scenario but using the special iterator instead of **ToList**.

C#

```C#
container.GetItemLinqQueryable<T>()
    .Where(i => i.categoryId == 2)
    .ToFeedIterator<T>();
```

### Configuring Max Concurrency, Parallelism, and Buffered Item Counts

When issuing a query from the SDK, the QueryRequestOptions includes a set of properties to tune a query's performance.

### Max Item Count

All query results in Azure Cosmos DB for NoSQL are returned as "pages" of results. This property indicates the number of items you would like to return in each "page". The service default is 100 items per page of results. You can set this value to **-1** to set a dynamic page size.

In this example, the **MaxItemCount** property is set to a value of **500**.

C#

```C#
QueryRequestOptions options = new ()
{
    MaxItemCount = 500
};
```

**Tip:** If you use a **MaxItemCount** of -1, you should ensure the total response doesn't exceed the service limit for response size. For instance, the max response size is 4 MB.

### Max Concurrency

**MaxConcurrency** specifies the number of concurrent operations ran client side during parallel query execution. If set to **1**, parallelism is effectively disabled. If set to **-1**, the SDK manages this setting. Ideally, you would set this value to the number of physical partitions for your container.

In this example, the *MaxConcurrency* property is set to a value of 5.

C#

```C#
QueryRequestOptions options = new ()
{
    MaxConcurrency = 5
};
```

### Max Buffered Item Count

The **MaxBufferedItemCount** property sets the maximum number of items that are buffered client-side during a parallel query execution. If set to -1, the SDK manages this setting. The ideal value for this setting will largely depend on the characteristics of your client machine.

In this example, the **MaxBufferedItemCount** property is set to a value of **5,000**.

C#

```C#
QueryRequestOptions options = new ()
{
    MaxBufferedItemCount = 5000
};
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Configuring Logging
</edukamu-collapse-hidden-title>

There are many scenarios in which you may wish to log the HTTP requests that the Azure Cosmos DB for NoSQL SDK performs "under the hood." The SDK includes a fluent client builder class that simplifies the process of injecting custom handlers into the HTTP requests and responses. You can take advantage of this functionality to build a simple logging mechanism.

### Client Builder

The **Microsoft.Azure.Cosmos.Fluent.CosmosClientBuilder** class is a builder class that fluently configures a new client instance. It comes with multiple methods that are used as an alternative to the **CosmosClientOptions** class including, but not limited to:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
Method
</edukamu-table-header>
<edukamu-table-header>
Description
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
WithApplicationRegion or WithApplicationPreferredRegions
</edukamu-table-cell>
<edukamu-table-cell>
Configures preferred region[s]
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
WithConnectionModeDirect and WithConnectionModeGateway
</edukamu-table-cell>
<edukamu-table-cell>
Sets connection mode
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
WithConsistencyLevel
</edukamu-table-cell>
<edukamu-table-cell>
Overrides consistency level
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section>
<br>

To use the builder, first you must add a using directive to the Microsoft.Azure.Cosmos.Fluent namespace.

C#

```C#
using Microsoft.Azure.Cosmos.Fluent;
```

Now, you can create a new instance of the **CosmosClientBuilder** class passing in a connection string or endpoint+key pair as constructor parameters.

C#

```C#
CosmosClientBuilder builder = new (connectionString);

CosmosClientBuilder builder = new (endpoint, key);
```

At this point, you can add any fluent methods to configure the client. Once you are done with fluent methods, you can invoke the **Build** method to create an instance of type **CosmosClient**.

### Creating a Custom Log Handler

To log HTTP requests, you will need to create a new class that inherits from the abstract **RequestHandler** class. In the handler, you can add logic before and after the HTTP request is sent. For this example, we will create a handler that performs the following workflow when an HTTP request is sent:

1. Writes the HTTP method and URI of the originating request to the console
2. Sends the request to the base implementation and stores the response in a variable
3. Writes the HTTP status code number and description to the console
4. Returns the response

### Custom RequestHandler Implementation

To implement this, we need to create a new class that inherits from **RequestHandler**.

C#

```C#
public class LogHandler : RequestHandler
{   
}
```

The abstract class includes a **SendAsync** method that should be overridden to inject new logic around requests.

C#

```C#
public override async Task<ResponseMessage> SendAsync(RequestMessage request, CancellationToken cancellationToken)
{
}
```

Within the **SendAsync** method, the **RequestUri** and **Method** properties of the **RequestMessage** parameter are printed to the console. Then, the base **SendAsync** method is invoked to send the actual request and store the response in a local variable.

C#

```C#
Console.WriteLine($"[{request.Method.Method}]\t{request.RequestUri}");

ResponseMessage response = await base.SendAsync(request, cancellationToken);
```

After the response is stored in a local variable, the **StatusCode** of the response is printed in both numeric and string format. Then the response is returned as the result of the asynchronous method.

C#

```C#
Console.WriteLine($"[{Convert.ToInt32(response.StatusCode)}]\t{response.StatusCode}");

return response;
```

Here is the code for the complete class.

C#

```C#
public class LogHandler : RequestHandler
{    
    public override async Task<ResponseMessage> SendAsync(RequestMessage request, CancellationToken cancellationToken)
    {
        Console.WriteLine($"[{request.Method.Method}]\t{request.RequestUri}");

        ResponseMessage response = await base.SendAsync(request, cancellationToken);
        
        Console.WriteLine($"[{Convert.ToInt32(response.StatusCode)}]\t{response.StatusCode}");
        
        return response;
    }
}
```

### Custom RequestHandler Implementation (Client)

Once the request handler implementation is ready, invoke the **AddCustomHandler** method of the **CosmosClientBuilder** instance passing in a new instance of the custom request handler.

C#

```C#
builder.AddCustomHandlers(new LogHandler());
```

Here is the code for the complete creation of the client using the builder.

C#

```C#
CosmosClientBuilder builder = new (endpoint, key);

builder.AddCustomHandlers(new LogHandler());

CosmosClient client = builder.Build();
```

### Testing the Custom Logger

Let's assume we have a fictional scenario where we use our client instance to invoke the **CreateDatabaseIfNotExistsAsync** method. The client instance should check for the existence of the database first, and if it doesn't find the database, it will create a new one using the specified name.

For this fictional scenario, we will use this example line of code to invoke the **CreateDatabaseIfNotExistsAsync** method.

C#

```C#
Database result = await client.CreateDatabaseIfNotExistsAsync("cosmicworks");
```

When you run the application for the first time, the logger will output that it performed the following actions:

1. Sent a HTTP GET *request* to query for your specific database at the

```C#
dbs/<database-name>
```

endpoint.
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Received a <span style="font-style: italic">response</span> of 404 that the database was not found.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Sent a HTTP <span style="font-weight: bold">POST</span> <span style="font-style: italic">request</span> with the database details in the body of the request to the dbs/ endpoint.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Received a <span style="font-style: italic">response</span> of <span style="font-weight: bold">201</span> indicating that the database has been created with the database's details in the response body.
</li>
</ol>
</edukamu-section>


```Bash
[GET]   dbs/cosmicworks
[404]   NotFound
[POST]  dbs/
[201]   Created
```

If you ran the application again, the logger would output a much shorter workflow:

1. Sent a HTTP GET *request* to query for your specific database at the

```C#
dbs/<database-name>
```

endpoint.
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Received a <span style="font-style: italic">response</span> of 200 indicating that the database has been found with the database's details in the response body.
</li>
</ol>
</edukamu-section>


```Bash
[GET]   dbs/cosmicworks
[200]   OK
```

</edukamu-collapse>
<br>


Configuring a software development kit opens numerous opportunities for all developers. By leveraging capabilities such as offline development, logging, and parallelism, the development process can be improved significantly.

There are endless ways of configuring SDKs, naturally, but the ones we've explored here should give you an idea of all the possibilities hidden within these marvelous toolboxes.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Configuring the SDK for Offline Development
</edukamu-collapse-hidden-title>

**Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

This practice exercise also requires a lab environment to be completed. You'll once again get to use a Windows-based virtual machine provided by Microsoft. You'll also be provided step-by-step instructions on configuring the SDK for offline development.

You can access the lab environment by navigating to Microsoft Learn and using the button to activate the lab.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/configure-azure-cosmos-db-sql-api-sdk/6-exercise-for-offline-development">Lab: Configuring the Azure Cosmos DB for NoSQL SDK for Offline Development</edukamu-button>
<br>

Should you run any issues, please refer back to the more detailed instructions on the page *Components of Cosmos DB for NoSQL*.

If you decide to take on the practice exercise, good luck! Enjoy the process!

</edukamu-collapse>
<br>


After carefully recapping and reviewing the contents explored on this page, it's time to complete another exercise.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Configuring SDKs
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/configuring-the-sdk-question-scroll-1.yaml" id="gkbhxbuqnyp18sew">
<br>

</edukamu-collapse>
<br>


How are you feeling at this stage? Are you starting to understand the Azure Cosmos DB service and its main capabilities? Before moving on, take a little pause and summarize NoSQL services in your head (or on a piece of paper!). What are they? What are they used for?

On the next page, we'll briefly review a few advanced capabilities of Microsoft Azure Cosmos DB. It's also the last topic of this course!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
