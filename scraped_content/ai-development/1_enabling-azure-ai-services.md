## Enabling Azure AI Services

Azure AI Services are cloud-based services that are available whenever and wherever you need them. In order to use them, they need to be enabled. 

As you might remember, the majority of Azure services work as resources, which practically means that the developers must activate them before starting to work with them. In other words, we’re talking about resource management.

On this page, we’ll learn everything we need about this process. We’ll begin with an overview of the resources available and make our way to provisioning.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Resources in Azure AI Services
</edukamu-collapse-hidden-title>
Azure AI services are cloud-based services that encapsulate AI capabilities. Rather than a single product, you should think of AI services as a set of individual services that you can use as building blocks to compose sophisticated, intelligent applications.

AI services includes a wide range of individual services across multiple categories, as shown in the following table.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Language**
</edukamu-table-header>
<edukamu-table-header>
**Speech**
</edukamu-table-header>
<edukamu-table-header>
**Vision**
</edukamu-table-header>
<edukamu-table-header>
**Decision**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Azure AI Language
</edukamu-table-cell>
<edukamu-table-cell>
Azure AI Speech
</edukamu-table-cell>
<edukamu-table-cell>
Azure AI Computer Vision
</edukamu-table-cell>
<edukamu-table-cell>
Azure AI Anomaly Detector
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Azure AI Translator
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
Azure AI Custom Vision
</edukamu-table-cell>
<edukamu-table-cell>
Azure AI Content Moderator
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
Azure AI Face
</edukamu-table-cell>
<edukamu-table-cell>
Azure AI Personalizer
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

You can use AI services to build your own AI solutions to provide out-of-the-box solutions for common AI scenarios. Azure AI services include:

- **Azure AI Document Intelligence** - An optical character recognition (OCR) solution that can extract semantic meaning from forms, such as invoices, receipts, and others. 
- **Azure AI Immersive Reader** - A reading solution that supports people of all ages and abilities.

- **Azure AI Search** - A cloud-scale search solution that uses AI services to extract insights from data and documents.

- **Azure OpenAI** - An Azure AI Service that provides access to the capabilities of OpenAI GPT-4.

While the details of each AI service can vary, the approach to provisioning and consuming them is generally the same.

In this section, you will learn how to:

- Create Azure AI services resources in an Azure subscription.
- Identify endpoints, keys, and locations required to consume an AI services resource.
- Use a REST API to consume an AI service.
- Use an SDK to consume an AI service.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Provisioning Service Resources
</edukamu-collapse-hidden-title>

Azure AI services include a wide range of AI capabilities that you can use in your applications. To use any of the AI services, you need to create appropriate resources in an Azure subscription to define an endpoint where the service can be consumed, provide access keys for authenticated access, and to manage billing for your application's usage of the service.

### Options for Azure Resources

For many of the available AI services, you can choose between the following provisioning options:

#### 1. Multi-service Resources

You can provision an **AI services** resource that supports multiple different AI services. For example, you could create a single resource that enables you to use the **Azure AI Language**, **Azure AI Vision**, **Azure AI Speech**, and other services.

This approach enables you to manage a single set of access credentials to consume multiple services at a single endpoint, and with a single point of billing for usage of all services.

#### 2. Single-service Resources

Each AI service can be provisioned individually, for example by creating discrete **AI Language** and **AI Vision** resources in your Azure subscription.

This approach enables you to use separate endpoints for each service (for example to provision them in different geographical regions) and to manage access credentials for each service independently. It also enables you to manage billing separately for each service.

Single-service resources generally offer a free tier (with usage restrictions), making them a good choice to try out a service before using it in a production application.


### Training and Prediction Resources

While most AI services can be used through a single Azure resource, some offer (or require) separate resources for model *training* and *prediction*. This enables you to manage billing for training custom models separately from model consumption by applications, and in most cases enables you to use a dedicated service-specific resource to train a model, but a generic **AI services** resource to make the model available to applications for inferencing.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Defining Endpoints and Keys
</edukamu-collapse-hidden-title>

When you provision an Azure AI services service resource in your Azure subscription, you are defining an endpoint through which the service can be consumed by an application.

To consume the service through the endpoint, applications require the following information:

- **The endpoint URI.** This is the HTTP address at which the REST interface for the service can be accessed. Most AI services software development kits (SDKs) use the endpoint URI to initiate a connection to the endpoint.

- **A subscription key.** Access to the endpoint is restricted based on a subscription key. Client applications must provide a valid key to consume the service. When you provision an AI services resource, two keys are created - applications can use either key. You can also regenerate the keys as required to control access to your resource.

- **The resource location.** When you provision a resource in Azure, you generally assign it to a location, which determines the Azure data center in which the resource is defined. While most SDKs use the endpoint URI to connect to the service, some require the location.

</edukamu-collapse>
<br>

There are endless ways to use Azure AI Services, and each developer has their own preferences. You can, for example, choose to use an API, an SDK, or both in tandem with each other. Making the choice depends on the scenario at hand. Let’s take a look.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### APIs or SDKs?
</edukamu-collapse-hidden-title>

Azure AI Services can utilize both REST APIs and SDKs, and how they are used depends largely on the specific requirements of your project and your personal or team's proficiency with these technologies.

### REST API

REST APIs: Representational State Transfer (REST) APIs are a set of rules and standards used for creating web services. They are language-agnostic, meaning they can be used with any programming language that can make HTTP requests and parse HTTP responses. 

REST APIs are often chosen for their simplicity and the ease of integrating with different platforms and languages. They're especially useful for developers who are working in a language for which an SDK is not available or when they need to perform a limited set of operations that can be easily handled with simple HTTP requests.

### SDK

SDKs are collections of software tools and libraries designed to help developers create applications in a specific programming language or for a specific platform. Azure AI Services provide SDKs for various programming languages like Python, .NET, Java, etc. 

SDKs typically offer a more streamlined and language-specific way to interact with the service, handling much of the boilerplate code and complexity behind the scenes, making development faster and often more robust.

In practice, you might use the two in tandem or choose one over the other depending on the situation:

- **In Tandem:** In a complex application, you might find that for most tasks, the SDK provides all the functionality you need in a convenient package, but for certain specific actions, direct API calls might be more efficient or offer additional control.
- **Choosing One:** For simpler applications, or when just getting started, you might choose to stick exclusively with the SDK for ease of use or the REST API for its universality and simplicity.

</edukamu-collapse>
<br>

In summary, whether you use REST APIs, SDKs, or a combination of both with Azure AI Services depends on your project's needs, your team's skill set, and the specific functionalities you wish to implement. Both are powerful tools and can be very effective whether used separately or in tandem.

Next, we’ll briefly summarize the main capabilities of REST APIs and SDKS within Microsoft Azure.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Using REST APIs
</edukamu-collapse-hidden-title>

Azure AI services provide REST application programming interfaces (APIs) that client applications can use to consume services. In most cases, service functions can be called by submitting data in JSON format over an HTTP request, which may be a POST, PUT, or GET request depending on the specific function being called. The results of the function are returned to the client as an HTTP response, often with JSON contents that encapsulate the output data from the function.

<edukamu-image url="/graphics/module1/rest-api.png" alt="Diagram of an app submitting a JSON request to an Azure AI services REST API and receiving a JSON response.">
<br>

The use of REST interfaces with an HTTP endpoint means that any programming language or tool capable of submitting and receiving JSON over HTTP can be used to consume AI services. You can use common programming languages such as Microsoft C#, Python, and JavaScript; as well as utilities such as Postman and cURL, which can be useful for testing.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Using SDKs
</edukamu-collapse-hidden-title>

You can develop an application that uses Azure AI services using REST interfaces, but it's easier to build more complex solutions by using native libraries for the programming language in which you're developing the application.

<edukamu-image url="/graphics/module1/sdk.png" alt="A diagram of an app submitting a call to an Azure AI services resource through a language-specific SDK, which abstracts the JSON request and response.">
<br>

Software development kits (SDKs) for common programming languages abstract the REST interfaces for most AI services. SDK availability varies by individual AI services, but for most services there's an SDK for languages such as:

- Microsoft C# (.NET Core)
- Python
- JavaScript (Node.js)
- Go
- Java

Each SDK includes packages that you can install in order to use service-specific libraries in your code, and online documentation to help you determine the appropriate classes, methods, and parameters used to work with the service.

</edukamu-collapse>
<br>

Getting started with Azure AI Services is relatively simple, even though the tools on offer range from basic features to advanced, cutting-edge capabilities. There are many decisions that have to be made before getting started – one of the most important being whether to use APIs, SDKs, or even both.

After the following exercise, we’ll start deploying the Azure AI capabilities covered so far.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Enabling AI Services
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module1/enabling-azure-ai-services-text-poll-1.yaml" id="797g9iv44rm5fp3a">

<edukamu-text-poll url="/exercises/module1/enabling-azure-ai-services-text-poll-2.yaml" id="c2wjxkaui2c6vfbg">

<edukamu-text-poll url="/exercises/module1/enabling-azure-ai-services-text-poll-3.yaml" id="62ps6c0973l1fbdi">

<edukamu-text-poll url="/exercises/module1/enabling-azure-ai-services-text-poll-4.yaml" id="8kd1cdgrw42ak32v">

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/1/enabling-azure-ai-services?question=797g9iv44rm5fp3a">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

Do you still remember containers from the previous courses? If you do, you already have an upper hand, since they’re our next topic! More precisely, we’ll explore how Azure AI Services can also be deployed as containers.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
