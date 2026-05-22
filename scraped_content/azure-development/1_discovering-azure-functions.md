## Discovering Azure Functions

Imagine you were developing an online retail platform that requires real-time inventory updates and order processing. Here, Azure Functions could be used to handle new order notifications, automatically updating inventory levels and sending confirmation emails to customers.

The serverless approach provided by Azure Functions means you wouldn't need to manage a dedicated server for these tasks. The main advantages are scalability, as the service can handle varying loads efficiently, and cost-effectiveness, since you only pay for the resources used during the function's execution, not for idle server time.

On this page, we'll get acquainted with the main capabilities of Azure Functions.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Getting Started with Azure Functions
</edukamu-collapse-hidden-title>

Azure **Functions** is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaining servers, the cloud infrastructure provides all the up-to-date resources needed to keep your applications running.

We often build systems to react to a series of critical events. Whether you're building a web API, responding to database changes, processing IoT data streams, or even managing message queues - every application needs a way to run some code as these events occur.

Azure Functions supports *triggers*, which are ways to start execution of your code, and *bindings*, which are ways to simplify coding for input and output data. There are other integration and automation services in Azure and they all can solve integration problems and automate business processes. They can all define input, actions, conditions, and output.

There is another service quite similar to Azure Functions within the Azure platform, Logic Apps. Although they might seem the same on the outside, there are some notable differences.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">

</edukamu-table-header>
<edukamu-table-header width="40%">
**Azure Functions**
</edukamu-table-header>
<edukamu-table-header width="40%">
**Logic Apps**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**Development**
</edukamu-table-cell>
<edukamu-table-cell>
Code-first (imperative)
</edukamu-table-cell>
<edukamu-table-cell>
Designer-first (declarative)
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Connectivity**
</edukamu-table-cell>
<edukamu-table-cell>
About a dozen built-in binding types, write code for custom bindings
</edukamu-table-cell>
<edukamu-table-cell>
Large collection of connectors, Enterprise Integration Pack for B2B scenarios, build custom connectors
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Actions**
</edukamu-table-cell>
<edukamu-table-cell>
Each activity is an Azure function; write code for activity functions
</edukamu-table-cell>
<edukamu-table-cell>
Large collection of ready-made actions
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Monitoring**
</edukamu-table-cell>
<edukamu-table-cell>
Azure Application Insights
</edukamu-table-cell>
<edukamu-table-cell>
Azure portal, Azure Monitor logs
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Management**
</edukamu-table-cell>
<edukamu-table-cell>
REST API, Visual Studio
</edukamu-table-cell>
<edukamu-table-cell>
Azure portal, REST API, PowerShell, Visual Studio
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Execution context**
</edukamu-table-cell>
<edukamu-table-cell>
Runs in Azure, or locally
</edukamu-table-cell>
<edukamu-table-cell>
Runs in Azure, locally, or on premises
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

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Managing Hosting
</edukamu-collapse-hidden-title>

When you create a function app in Azure, you must choose a hosting plan for your app. There are three basic hosting plans available for Azure Functions: Consumption plan, Premium plan, and App service plan (Dedicated). All hosting plans are generally available (GA) on both Linux and Windows virtual machines.

The hosting plan you choose dictates the following behaviors:

- How your function app is scaled.
- The resources available to each function app instance.
- Support for advanced functionality, such as Azure Virtual Network connectivity.

Following is a summary of the benefits of the three main hosting plans for Functions:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Plan**
</edukamu-table-header>
<edukamu-table-header width="80%">
**Benefits**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**Consumption plan**
</edukamu-table-cell>
<edukamu-table-cell>
This is the default hosting plan. It scales automatically and you only pay for compute resources when your functions are running. Instances of the Functions host are dynamically added and removed based on the number of incoming events.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Premium plan**
</edukamu-table-cell>
<edukamu-table-cell>
Automatically scales based on demand using pre-warmed workers, which run applications with no delay after being idle, runs on more powerful instances, and connects to virtual networks.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Dedicated plan**
</edukamu-table-cell>
<edukamu-table-cell>
Run your functions within an App Service plan at regular App Service plan rates. Best for long-running scenarios where [Durable Functions](https://learn.microsoft.com/en-us/azure/azure-functions/durable/durable-functions-overview?tabs=in-process%2Cnodejs-v3%2Cv1-model&pivots=csharp)(target="_blank") can't be used.
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

There are two other hosting options, which provide the highest amount of control and isolation in which to run your function apps.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Hosting option**
</edukamu-table-header>
<edukamu-table-header width="80%">
**Details**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**ASE**
</edukamu-table-cell>
<edukamu-table-cell>
<edukamu-link url="https://learn.microsoft.com/en-us/azure/app-service/environment/intro" target="_blank">App Service Environment (ASE)</edukamu-link> is an App Service feature that provides a fully isolated and dedicated environment for securely running App Service apps at high scale.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Kubernetes** (<edukamu-link url="https://learn.microsoft.com/en-us/azure/azure-functions/functions-kubernetes-keda" target="_blank">Direct</edukamu-link> or <edukamu-link url="https://learn.microsoft.com/en-us/azure/app-service/overview-arc-integration" target="_blank">Azure Arc</edukamu-link>)
</edukamu-table-cell>
<edukamu-table-cell>
Kubernetes provides a fully isolated and dedicated environment running on top of the Kubernetes platform.
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

On any plan, a function app requires a general Azure Storage account, which supports Azure Blob, Queue, Files, and Table storage. This is because Functions rely on Azure Storage for operations such as managing triggers and logging function executions, but some storage accounts don't support queues and tables.

The same storage account used by your function app can also be used by your triggers and bindings to store your application data. However, for storage-intensive operations, you should use a separate storage account.

</edukamu-collapse>
<br>

By implementing Azure Functions, developers can easily manage tasks such as the following:

1. **Order Processing in E-Commerce**: When a customer places an order, an Azure Function is triggered to update the inventory database and send a confirmation email.
2. **File Processing**: An Azure Function can be set up to trigger when a file is uploaded to Azure Blob Storage, processing or converting the file (like resizing an image).
3. **Scheduled Data Cleanup**: An Azure Function can run on a schedule to clean up or archive old data from a database, optimizing performance.

One of the most beneficial features of Azure Functions is their serverless nature, which reduces the need for infrastructure management. Scaling still needs to be considered, however.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Scaling Azure Functions
</edukamu-collapse-hidden-title>

Azure Functions scaling refers to the automatic adjustment of resources allocated to handle the load on serverless functions. When demand increases, Azure Functions can automatically create more instances of the function to distribute the workload. Conversely, it reduces resources when demand decreases.

In essence, Azure Functions uses a component called the scale controller to monitor the rate of events and determine whether to scale out or scale in. The scale controller uses heuristics for each trigger type. For example, when you're using an Azure Queue storage trigger, it scales based on the queue length and the age of the oldest queue message.

The unit of scale for Azure Functions is the function app. When the function app is scaled out, more resources are allocated to run multiple instances of the Azure Functions host. Conversely, as compute demand is reduced, the scale controller removes function host instances. The number of instances is eventually "scaled in" to zero when no functions are running within a function app.

<edukamu-image url="/graphics/module1/central-listener.png" alt="Scale controller monitoring events and creating instances." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**Note**: After your function app has been idle for a number of minutes, the platform may scale the number of instances on which your app runs in to zero. The next request has the added latency of scaling from zero to one. This latency is referred to as a *cold start*.


### Scaling Behaviors

Scaling can vary on many factors, and scale differently based on the trigger and language selected. There are a few intricacies of scaling behaviors to be aware of:

- **Maximum instances**: A single function app only scales out to a maximum of 200 instances. A single instance may process more than one message or request at a time though, so there isn't a set limit on number of concurrent executions.
- **New instance rate**: For HTTP triggers, new instances are allocated, at most, once per second. For non-HTTP triggers, new instances are allocated, at most, once every 30 seconds.

You may wish to restrict the maximum number of instances an app used to scale out. This is most common for cases where a downstream component like a database has limited throughput. By default, Consumption plan functions scale out to as many as 200 instances, and Premium plan functions scales out to as many as 100 instances. You can specify a lower maximum for a specific app by modifying the `functionAppScaleLimit` value. The `functionAppScaleLimit` can be set to 0 or null for unrestricted, or a valid value between 1 and the app maximum.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
Scaling ensures that Azure Functions are handled effectively, which in turn helps optimize both performance and cost-effectiveness. You don't have to manually scale resources; Azure manages this dynamically, providing a responsive and economical solution for handling varying application demands.

Azure Functions support multiple programming languages and integrate seamlessly with other Azure services, making them a flexible and powerful tool for a wide range of applications.

Regardless of the programming languages and other variables, all functions share a few core technical concepts and components. Let's wrap up this section by exploring them.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Understanding Azure Functions
</edukamu-collapse-hidden-title>

A **function** contains two important pieces - your code, which can be written in various languages, and some config, the *function.json* file. For compiled languages, this config file is generated automatically from annotations in your code. For scripting languages, you must provide the config file yourself.

The *function.json* file defines the function's trigger, bindings, and other configuration settings. Every function has one and only one trigger. The runtime uses this config file to determine the events to monitor and how to pass data into and return data from a function execution. Following is an example *function.json* file.

JSON

```JSON
{
    "disabled":false,
    "bindings":[
        // ... bindings here
        {
            "type": "bindingType",
            "direction": "in",
            "name": "myParamName",
            // ... more depending on binding
        }
    ]
}
```

The `bindings` property is where you configure both triggers and bindings. Each binding shares a few common settings and some settings that are specific to a particular type of binding. Every binding requires the following settings:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="15%">
**Property**
</edukamu-table-header>
<edukamu-table-header width="15%">
**Types**
</edukamu-table-header>
<edukamu-table-header width="70%">
**Comments**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
`type`
</edukamu-table-cell>
<edukamu-table-cell>
string
</edukamu-table-cell>
<edukamu-table-cell>
Name of binding. For example, `queueTrigger`.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
`direction`
</edukamu-table-cell>
<edukamu-table-cell>
string
</edukamu-table-cell>
<edukamu-table-cell>
Indicates whether the binding is for receiving data into the function or sending data from the function. For example, `in` or `out`.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
`name`
</edukamu-table-cell>
<edukamu-table-cell>
string
</edukamu-table-cell>
<edukamu-table-cell>
The name that is used for the bound data in the function. For example, `myQueue`.
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

### Function Apps

A function app provides an execution context in Azure in which your functions run. As such, it's the unit of deployment and management for your functions. A function app is composed of one or more individual functions that are managed, deployed, and scaled together. All of the functions in a function app share the same pricing plan, deployment method, and runtime version. Think of a function app as a way to organize and collectively manage your functions.

**Note**: In Functions 2.x all functions in a function app must be authored in the same language. In previous versions of the Azure Functions runtime, this wasn't required.

### Local Development

Functions make it easy to use your favorite code editor and development tools to create and test functions on your local computer. Your local functions can connect to live Azure services, and you can debug them on your local computer using the full Functions runtime.

The way in which you develop functions on your local computer depends on your language and tooling preferences.

However, you should not mix local development with portal development in the same function app. When you create and publish functions from a local project, you should not try to maintain or modify project code in the portal.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Functions in Practice: Triggers and Binding
</edukamu-collapse-hidden-title>

Triggers cause a function to run. A trigger defines how a function is invoked and a function must have exactly one trigger. Triggers have associated data, which is often provided as the payload of the function.

Binding to a function is a way of declaratively connecting another resource to the function; bindings may be connected as *input bindings*, *output bindings*, or both. Data from bindings is provided to the function as parameters.

You can mix and match different bindings to suit your needs. Bindings are optional and a function might have one or multiple input and/or output bindings.

Triggers and bindings let you avoid hardcoding access to other services. Your function receives data (for example, the content of a queue message) in function parameters. You send data (for example, to create a queue message) by using the return value of the function.

### Defining Triggers and Bindings

Triggers and bindings are defined differently depending on the development language. Have a look:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Language**
</edukamu-table-header>
<edukamu-table-header>
**Triggers and bindings are configured by...**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
C# class library
</edukamu-table-cell>
<edukamu-table-cell>
decorating methods and parameters with C# attributes
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Java
</edukamu-table-cell>
<edukamu-table-cell>
decorating methods and parameters with Java annotations
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
JavaScript/PowerShell/Python/TypeScript
</edukamu-table-cell>
<edukamu-table-cell>
updating *function.json* schema
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

(Soon, we'll review an example function in the C# programming language.)

For languages that rely on *function.json*, the portal provides a UI for adding bindings in the **Integration** tab. You can also edit the file directly in the portal in the **Code** + **test** tab of your function.

In .NET and Java, the parameter type defines the data type for input data. For instance, use string to bind to the text of a queue trigger, a byte array to read as binary, and a custom type to de-serialize to an object. Since .NET class library functions and Java functions don't rely on *function.json* for binding definitions, they can't be created and edited in the portal. C# portal editing is based on C# script, which uses *function.json* instead of attributes.

For languages that are dynamically typed such as JavaScript, use the `dataType` property in the *function.json* file. For example, to read the content of an HTTP request in binary format, set `dataType` to `binary`:

```Code
{
    "dataType": "binary",
    "type": "httpTrigger",
    "name": "req",
    "direction": "in"
}
```

Other options for `dataType` are `stream` and `string`.

### Binding Direction

All triggers and bindings have a direction property in the *function.json* file:

- For triggers, the direction is always `in`
- Input and output bindings use `in` and `out`
- Some bindings support a special direction `inout`. If you use `inout`, only the **Advanced editor** is available via the **Integrate** tab in the portal.

When you use attributes in a class library to configure triggers and bindings, the direction is provided in an attribute constructor or inferred from the parameter type.

### Example: Functions Trigger and Binding

Suppose you want to write a new row to Azure Table storage whenever a new message appears in Azure Queue storage. This scenario can be implemented using an Azure Queue storage trigger and an Azure Table storage output binding.

Here's a *function.json* file for this scenario.

JSON

```JSON
{
  "bindings": [
    {
      "type": "queueTrigger",
      "direction": "in",
      "name": "order",
      "queueName": "myqueue-items",
      "connection": "MY_STORAGE_ACCT_APP_SETTING"
    },
    {
      "type": "table",
      "direction": "out",
      "name": "$return",
      "tableName": "outTable",
      "connection": "MY_TABLE_STORAGE_ACCT_APP_SETTING"
    }
  ]
}
```

The first element in the `bindings` array is the Queue storage trigger. The `type` and `direction` properties identify the trigger. The `name` property identifies the function parameter that receives the queue message content. The name of the queue to monitor is in `queueName`, and the connection string is in the app setting identified by `connection`.

The second element in the `bindings` array is the Azure Table Storage output binding. The `type` and `direction` properties identify the binding. The `name` property specifies how the function provides the new table row, in this case by using the function return value. The name of the table is in `tableName`, and the connection string is in the app setting identified by `connection`.

### Example: C# Script

Here's C# script code that works with this trigger and binding. Notice that the name of the parameter that provides the queue message content is `order`; this name is required because the name property value in *function.json* is `order`.

C#

```C#
#r "Newtonsoft.Json"

using Microsoft.Extensions.Logging;
using Newtonsoft.Json.Linq;

// From an incoming queue message that is a JSON object, add fields and write to Table storage
// The method return value creates a new row in Table Storage
public static Person Run(JObject order, ILogger log)
{
    return new Person() { 
            PartitionKey = "Orders", 
            RowKey = Guid.NewGuid().ToString(),  
            Name = order["Name"].ToString(),
            MobileNumber = order["MobileNumber"].ToString() };  
}

public class Person
{
    public string PartitionKey { get; set; }
    public string RowKey { get; set; }
    public string Name { get; set; }
    public string MobileNumber { get; set; }
}
```

</edukamu-collapse>
<br>

By using triggers and bindings, developers can streamline the process of accessing data from databases, storage, and other services, which in turn helps reduce the need of writing all-new code manually.

Before you take on the exercise below, stop for a while and think back to the development projects in which you've participated before, no matter how big or small. Did you use Azure Functions? If yes, how? And if not, in what instanced could they have been used?

Of course it's possible that you've used different software altogether before, which is also completely fine! Either way, understanding the capabilities of Microsoft Azure will certainly be helpful in the future.

Now it's time to complete the last exercise of the first unit!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Azure Functions
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/discovering-azure-functions-question-scroll-1.yaml" id="tt2x7wvuaxf7sv13">
<br>

</edukamu-collapse>
<br>

You've reached the end of the first unit, well done!

How are you feeling right now? After exploring web apps and functions, are you slowly starting to get the hang of Azure development? Even if the practical side of things might seem a little confusing right now, you're constantly developing your skills and knowledge, so keep on going!

Remember to take little breaks from time to time in order to let your brain rest and process the new information.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
