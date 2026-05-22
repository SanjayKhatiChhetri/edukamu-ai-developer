## Getting Started with Azure App Service

Web apps are constantly becoming more and more popular across all imaginable fields. From online shopping to social media, from healthcare to agriculture, web apps are providing us with the means to access what we need, when we need it. And Azure App Service empowers us to create such solutions.

Azure App Service stands out for its seamless integration, scalability, and support for a variety of programming languages and frameworks - in addition to its ability to integrate with various services. In this section, we'll review the fundamental aspects of Azure App Service.

<edukamu-note class="edukamu-note-icon-info">
### When to Use Azure App Service?

Azure App Service is suitable for situations in which you need to quickly and efficiently build, deploy, and scale web or mobile applications. It's particularly beneficial when you need:

1. **Rapid Development**: You need to develop and deploy applications quickly.
2. **Scalability**: You require automatic scaling to handle fluctuating traffic.
3. **Multi-language Support**: Your project involves using various programming languages.
4. **Serverless Architecture**: You want to focus on app development without managing infrastructure.
5. **Integration Requirements**: You need to integrate with other Azure services or external applications.
6. **Continuous Deployment**: You're implementing a CI/CD pipeline for regular updates and testing.
</edukamu-note>
<br>

Azure App Service is would be the ideal fit for hosting an e-commerce platform, developing a content management system (like a blogging environment) or implementing SaaS applications (Software as a Service), like Microsoft Office 365.

As always, we'll start with a little introduction, building on the knowledge we gained on the previous page.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure App Service
</edukamu-collapse-hidden-title>

Azure App Service is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends. You can develop in your favorite programming language or framework. Applications run and scale with ease on both Windows and Linux-based environments.

HTTP-based services operate using the Hypertext Transfer Protocol (HTTP), which is the foundation of data communication on the World Wide Web. 

In the context of Azure App Service, this implies that the service is designed to handle HTTP requests and responses. This is essential for web applications, APIs, and mobile back ends, which rely on HTTP for client-server communication. Essentially, Azure App Service is built to support and manage applications that communicate over the web using HTTP.

### Azure App Service Features

#### 1. Built-in Autoscaling

Baked into Azure App Service is the ability to scale up/down or scale out/in. Depending on the usage of the web app, you can scale the resources of the underlying machine that is hosting your web app up/down. Resources include the number of cores or the amount of RAM available. Scaling out/in is the ability to increase, or decrease, the number of machine instances that are running your web app.

#### 2. Continuous Integration/Deployment Support

The Azure portal provides out-of-the-box continuous integration and deployment with Azure DevOps Services, GitHub, Bitbucket, FTP, or a local Git repository on your development machine. Connect your web app with any of the above sources and App Service will do the rest for you by auto-syncing code and any future changes on the code into the web app.

#### 3. Deployment Slots

When you deploy your web app you can use a separate deployment slot instead of the default production slot when you're running in the Standard App Service Plan tier or better. Deployment slots are live apps with their own host names. App content and configurations elements can be swapped between two deployment slots, including the production slot.

#### 4. Linux Support

App Service can also host web apps natively on Linux for supported application stacks. It can also run custom Linux containers (also known as Web App for Containers). App Service on Linux supports many language specific built-in images. Just deploy your code. Supported languages and frameworks include: Node.js, Java (JRE 8 & JRE 11), PHP, Python, .NET, and Ruby. If the runtime your application requires isn't supported in the built-in images, you can deploy it with a custom container.

The languages, and their supported versions, are updated regularly. You can retrieve the current list by using the following command in the Cloud Shell.

Bash

```Bash
az webapp list-runtimes --os-type linux
```

### App Service Limitations

Like all services, Azure App Service on Linux does have some limitations:

- The Azure portal shows only features that currently work for Linux apps. As features are enabled, they're activated on the portal.
- When deployed to built-in images, your code and content are allocated a storage volume for web content, backed by Azure Storage. The disk latency of this volume is higher and more variable than the latency of the container filesystem. Apps that require heavy read-only access to content files may benefit from the custom container option, which places files in the container filesystem instead of on the content volume.

</edukamu-collapse>
<br>

When using Azure App Service, each development team has to make decisions regarding deployment, or deployment pipelines. The term refers to the automated process of moving code from development stages through to production. This typically involves steps like building the application from source code, running tests, and deploying to various environments (development, staging, production).

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Deploying to App Service
</edukamu-collapse-hidden-title>

Every development team has unique requirements that can make implementing an efficient deployment pipeline difficult on any cloud service. App Service supports both automated and manual deployment.

### Automated Deployment

Automated deployment, or continuous deployment, is a process used to push out new features and bug fixes in a fast and repetitive pattern with minimal effect on end users.

Azure supports automated deployment directly from several sources. The following options are available:

- **Azure DevOps Services**: You can push your code to Azure DevOps Services, build your code in the cloud, run the tests, generate a release from the code, and finally, push your code to an Azure Web App. 
- **GitHub**: Azure supports automated deployment directly from GitHub. When you connect your GitHub repository to Azure for automated deployment, any changes you push to your production branch on GitHub are automatically deployed for you. 
- **Bitbucket**: With its similarities to GitHub, you can configure an automated deployment with Bitbucket.

### Manual Deployment

There are a few options that you can use to manually push your code to Azure:

- **Git**: App Service web apps feature a Git URL that you can add as a remote repository. Pushing to the remote repository deploys your app.
- **CLI**: `webapp up` is a feature of the `az` command-line interface that packages your app and deploys it. Unlike other deployment methods, `az webapp up` can create a new App Service web app for you if you haven't already created one. 
- **Zip deploy**: Use `curl` or a similar HTTP utility to send a ZIP of your application files to App Service.
- **FTP/S**: FTP or FTPS is a traditional way of pushing your code to many hosting environments, including App Service.

### Deployment Slots

In the context of Azure App Service, deployment slots are feature that allows you to have multiple environments for your web app. Each slot is like a separate web app instance, with its own URL. You can use these slots to manage different versions of your app (like staging, testing, or production versions) and swap them seamlessly without downtime.

Whenever possible, use deployment slots when deploying a new production build. When using a Standard App Service Plan tier or better, you can deploy your app to a staging environment and then swap your staging and production slots. The swap operation warms up the necessary worker instances to match your production scale, thus eliminating downtime.

</edukamu-collapse>
<br>

Using deployment slots is particularly useful for testing changes in a live-like environment before making them public, ensuring stability and minimizing risks when updating your application.

Let's explore this with a short example.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Example: Deployment Slots in Action
</edukamu-collapse-hidden-title>

When you swap two slots (for example, from a staging slot to the production slot), App Service does the following to ensure that the target slot doesn't experience downtime:

1. Apply the following settings from the target slot (for example, the production slot) to all instances of the source slot:
  - Slot-specific app settings and connection strings, if applicable.
  - Continuous deployment settings, if enabled.
  - App Service authentication settings, if enabled.

Any of these cases trigger all instances in the source slot to restart. During **swap with preview**, this marks the end of the first phase. The swap operation is paused, and you can validate that the source slot works correctly with the target slot's settings.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Wait for every instance in the source slot to complete its restart. If any instance fails to restart, the swap operation reverts all changes to the source slot and stops the operation.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
If local cache is enabled, trigger local cache initialization by making an HTTP request to the application root ("/") on each instance of the source slot. Wait until each instance returns any HTTP response. Local cache initialization causes another restart on each instance.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
If auto swap is enabled with custom warm-up, trigger Application Initiation by making an HTTP request to the application root ("/") on each instance of the source slot.
</li>
</ol>
</edukamu-section>
  - If `applicationInitialization` isn't specified, trigger an HTTP request to the application root of the source slot on each instance.
  - If an instance returns any HTTP response, it's considered to be warmed up.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
If all instances on the source slot are warmed up successfully, swap the two slots by switching the routing rules for the two slots. After this step, the target slot (for example, the production slot) has the app that's previously warmed up in the source slot.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Now that the source slot has the pre-swap app previously in the target slot, perform the same operation by applying all settings and restarting the instances.
</li>
</ol>
</edukamu-section>

At any point of the swap operation, all work of initializing the swapped apps happens on the source slot. The target slot remains online while the source slot is being prepared and warmed up, regardless of where the swap succeeds or fails. To swap a staging slot with the production slot, make sure that the production slot is always the target slot. This way, the swap operation doesn't affect your production app.

When you clone configuration from another deployment slot, the cloned configuration is editable. Some configuration elements follow the content across a swap (not slot specific), whereas other configuration elements stay in the same slot after a swap (slot specific). The following table shows the settings that change when you swap slots.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Settings that are swapped**
</edukamu-table-header>
<edukamu-table-header>
**Settings that aren't swapped**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
General settings, such as framework version, 32/64-bit, web sockets
</edukamu-table-cell>
<edukamu-table-cell>
Publishing endpoints
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
App settings (can be configured to stick to a slot)
</edukamu-table-cell>
<edukamu-table-cell>
Custom domain names
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Connection strings (can be configured to stick to a slot)
</edukamu-table-cell>
<edukamu-table-cell>
Non-public certificates and TLS/SSL settings
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Handler mappings
</edukamu-table-cell>
<edukamu-table-cell>
Scale settings
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Public certificates
</edukamu-table-cell>
<edukamu-table-cell>
WebJobs schedulers
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
WebJobs content
</edukamu-table-cell>
<edukamu-table-cell>
IP restrictions
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Hybrid connections *
</edukamu-table-cell>
<edukamu-table-cell>
Always On
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Azure Content Delivery Network *
</edukamu-table-cell>
<edukamu-table-cell>
Diagnostic log settings
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Service endpoints *
</edukamu-table-cell>
<edukamu-table-cell>
Cross-origin resource sharing (CORS)
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Path mappings
</edukamu-table-cell>
<edukamu-table-cell>
Virtual network integration
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
Managed identities
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
Settings that end with the suffix _EXTENSION_VERSION
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

Features marked with an asterisk (*) are planned to be unswapped.

</edukamu-collapse>
<br>

When developing intelligent solutions, authentication and authorization are key concepts that have to bee taken into account at every stage. Sometimes, even setting up secure protocols can take time and effort, but this is not the case with Azure App Service, which includes many built-in features for the task.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Authorization and Authentication in Azure App Service
</edukamu-collapse-hidden-title>

Azure App Service provides built-in authentication and authorization support, so you can sign in users and access data by writing minimal, or no code in your web app, RESTful API, mobile back end, and Azure Functions.

You're not required to use App Service for authentication and authorization. Many web frameworks are bundled with security features, and you can use them if you like. If you need more flexibility than App Service provides, you can also write your own utilities.

The built-in authentication feature for App Service and Azure Functions can save you time and effort by providing out-of-the-box authentication with federated identity providers, allowing you to focus on the rest of your application.

- Azure App Service allows you to integrate various auth capabilities into your web app or API without implementing them yourself.
- It’s built directly into the platform and doesn’t require any particular language, SDK, security expertise, or code.
- You can integrate with multiple login providers. For example, Microsoft Entra ID, Facebook, Google, Twitter.

App Service uses federated identity, in which a third-party identity provider manages the user identities and authentication flow for you. The following identity providers are available by default:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Provider**
</edukamu-table-header>
<edukamu-table-header>
**Sign-in endpoint**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Microsoft identity platform
</edukamu-table-cell>
<edukamu-table-cell>
`/.auth/login/aad`
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Facebook
</edukamu-table-cell>
<edukamu-table-cell>
`/.auth/login/facebook`
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Google
</edukamu-table-cell>
<edukamu-table-cell>
`/.auth/login/google`
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Twitter
</edukamu-table-cell>
<edukamu-table-cell>
`/.auth/login/twitter`
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Any OpenID Connect provider
</edukamu-table-cell>
<edukamu-table-cell>
`/.auth/login/< providerName >`
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
GitHub
</edukamu-table-cell>
<edukamu-table-cell>
`/.auth/login/github`
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

When you enable authentication and authorization with one of these providers, its sign-in endpoint is available for user authentication and for validation of authentication tokens from the provider. You can provide your users with any number of these sign-in options.

### How it Works?

The authentication and authorization module runs in the same sandbox as your application code. When it's enabled, every incoming HTTP request passes through it before being handled by your application code. This module handles several things for your app:

- Authenticates users and clients with the specified identity provider(s)
- Validates, stores, and refreshes OAuth tokens issued by the configured identity provider(s)
- Manages the authenticated session
- Injects identity information into HTTP request headers

The module runs separately from your application code and can be configured using Azure Resource Manager settings or using a configuration file. No SDKs, specific programming languages, or changes to your application code are required.

### Authentication Flows

The authentication flow is the same for all providers, but differs depending on whether you want to sign in with the provider's SDK.

- Without provider SDK: The application delegates federated sign-in to App Service. This is typically the case with browser apps, which can present the provider's login page to the user. The server code manages the sign-in process, so it's also called *server-directed flow* or *server flow*.
- With provider SDK: The application signs users in to the provider manually and then submits the authentication token to App Service for validation. This is typically the case with browser-less apps, which can't present the provider's sign-in page to the user. The application code manages the sign-in process, so it's also called *client-directed flow* or *client flow*. This applies to REST APIs, Azure Functions, JavaScript browser clients, and native mobile apps that sign users in using the provider's SDK.

The following table shows the steps of the authentication flow.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Step**
</edukamu-table-header>
<edukamu-table-header>
**Without provider SDK**
</edukamu-table-header>
<edukamu-table-header>
**With provider SDK**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Sign user in
</edukamu-table-cell>
<edukamu-table-cell>
Redirects client to `/.auth/login/< provider >.`
</edukamu-table-cell>
<edukamu-table-cell>
Client code signs user in directly with provider's SDK and receives an authentication token. For information, see the provider's documentation.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Post-authentication
</edukamu-table-cell>
<edukamu-table-cell>
Provider redirects client to `/.auth/login/< provider >/callback`.
</edukamu-table-cell>
<edukamu-table-cell>
Client code posts token from provider to `/.auth/login/< provider >` for validation.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Establish authenticated session
</edukamu-table-cell>
<edukamu-table-cell>
App Service adds authenticated cookie to response.
</edukamu-table-cell>
<edukamu-table-cell>
App Service returns its own authentication token to client code.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Serve authenticated content
</edukamu-table-cell>
<edukamu-table-cell>
Client includes authentication cookie in subsequent requests (automatically handled by browser).
</edukamu-table-cell>
<edukamu-table-cell>
Client code presents authentication token in X-ZUMO-AUTH header (automatically handled by Mobile Apps client SDKs).
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

For client browsers, App Service can automatically direct all unauthenticated users to `/.auth/login/< provider >`. You can also present users with one or more `/.auth/login/< provider >` links to sign in to your app using their provider of choice.

In the Azure portal, you can configure App Service with many behaviors when an incoming request isn't authenticated.

- **Allow unauthenticated requests**: This option defers authorization of unauthenticated traffic to your application code. For authenticated requests, App Service also passes along authentication information in the HTTP headers. This option provides more flexibility in handling anonymous requests. It lets you present multiple sign-in providers to your users.
- **Require authentication**: This option rejects any unauthenticated traffic to your application. This rejection can be a redirect action to one of the configured identity providers. In these cases, a browser client is redirected to `/.auth/login/< provider >` for the provider you choose. If the anonymous request comes from a native mobile app, the returned response is an `HTTP 401 Unauthorized`. You can also configure the rejection to be an `HTTP 401 Unauthorized` or `HTTP 403 Forbidden` for all requests.

Restricting access in this way applies to all calls to your app, which may not be desirable for apps wanting a publicly available home page, as in many single-page applications. Take this into account when using Azure App Service's built-in authentication and authorization features.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
During this course, we'll often come across the concept of "sandboxes". In the context of solution development, it refers to a secure and isolated environment in which your application code runs. It's essentially a boundary set by Azure to ensure that your app operates safely and doesn't interfere with the underlying infrastructure or other apps.

Sandboxes are also useful when it comes to testing and implementing new features, such as different networking capabilities.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure App Service and Networking
</edukamu-collapse-hidden-title>

By default, apps hosted in App Service are accessible directly through the internet and can reach only internet-hosted endpoints. But for many applications, you need to control the inbound and outbound network traffic.

There are two main deployment types for Azure App Service. The multitenant public service hosts App Service plans in the Free, Shared, Basic, Standard, Premium, PremiumV2, and PremiumV3 pricing SKUs. There's also the single-tenant App Service Environment (ASE) hosts Isolated SKU App Service plans directly in your Azure virtual network.

### Networking Features

Azure App Service is a distributed system. The roles that handle incoming HTTP or HTTPS requests are called front ends. The roles that host the customer workload are called workers. All the roles in an App Service deployment exist in a multi-tenant network. Because there are many different customers in the same App Service scale unit, you can't connect the App Service network directly to your network.

Instead of connecting the networks, you need features to handle the various aspects of application communication. The features that handle requests to your app can't be used to solve problems when you're making calls from your app. Likewise, the features that solve problems for calls from your app can't be used to solve problems to your app.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Inbound features**
</edukamu-table-header>
<edukamu-table-header>
**Outbound features**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
App-assigned address
</edukamu-table-cell>
<edukamu-table-cell>
Hybrid Connections
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Access restrictions
</edukamu-table-cell>
<edukamu-table-cell>
Gateway-required virtual network integration
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Service endpoints
</edukamu-table-cell>
<edukamu-table-cell>
Virtual network integration
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Private endpoints
</edukamu-table-cell>
<edukamu-table-cell>

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

You can mix the features to solve your problems with a few exceptions. The following inbound use cases are examples of how to use App Service networking features to control traffic inbound to your app.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Inbound use case**
</edukamu-table-header>
<edukamu-table-header>
**Feature**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Support IP-based SSL needs for your app
</edukamu-table-cell>
<edukamu-table-cell>
App-assigned address
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Support unshared dedicated inbound address for your app
</edukamu-table-cell>
<edukamu-table-cell>
App-assigned address
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Restrict access to your app from a set of well-defined addresses
</edukamu-table-cell>
<edukamu-table-cell>
Access restrictions
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

### Default Networking Behavior

Azure App Service scale units support many customers in each deployment. The Free and Shared SKU plans host customer workloads on multitenant workers. The Basic and higher plans host customer workloads that are dedicated to only one App Service plan. If you have a Standard App Service plan, all the apps in that plan run on the same worker. If you scale out the worker, all the apps in that App Service plan are replicated on a new worker for each instance in your App Service plan.

### Outbound Addresses

The worker VMs are broken down in large part by the App Service plans. The Free, Shared, Basic, Standard, and Premium plans all use the same worker VM type. The PremiumV2 plan uses another VM type. PremiumV3 uses yet another VM type. When you change the VM family, you get a different set of outbound addresses.

There are many addresses that are used for outbound calls. The outbound addresses used by your app for making outbound calls are listed in the properties for your app. These addresses are shared by all the apps running on the same worker VM family in the App Service deployment. If you want to see all the addresses that your app might use in a scale unit, there's a property called `possibleOutboundIpAddresses` that lists them.

</edukamu-collapse>
<br>

Whenever there's a need to develop modern, global, and scalable applications quickly and reliably, Azure App Service is among the best options to consider. The features we've covered on this page are all accessible through Azure Portal, which makes them simple to find and use.

On the next page, we'll find out how Azure App Services are configured. Before moving on, it's time for another exercise.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Azure App Service
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/getting-started-with-azure-app-service-question-scroll-1.yaml" id="2t7is45i0t3gj655">
<br>

</edukamu-collapse>
<br>

Configuring Azure App Service encompasses many quite advanced settings, such as installing certificates and enabling web diagnostics. On the next page, we'll take a look at the process.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
