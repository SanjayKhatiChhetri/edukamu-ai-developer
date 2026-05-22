## Configuring Web Apps

When it comes to developing web apps, configurations should be made a top priority. In order to make your applications function well and securely in accordance with specific business requirements, this important process should not be overlooked.

In Azure App Service, app settings are like special notes you give to your web app. Think of it as giving your app a note with important information like a secret code (API key) or a direction (database connection info).

If your app needs to access a database each time an user completes an action on your site, you'd write the database address and password on this "note". Your app would then read this note to know where and how to connect to the database, without you having to put this sensitive info directly in your app's code.

As such, configuring web apps is as much about security as it is about the ease of use. Let's dig in, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Configuring Application Settings
</edukamu-collapse-hidden-title>

In App Service, app settings are variables passed as environment variables to the application code. For Linux apps and custom containers, App Service passes app settings to the container using the `--env` flag to set the environment variable in the container.

Application settings can be accessed by navigating to your app's management page and selecting **Configuration > Application Settings**.

<edukamu-image url="/graphics/module1/configure-app-settings.png" alt="Navigating to Configuration > Application settings.">
<br>

For ASP.NET and ASP.NET Core developers, setting app settings in App Service are like setting them in `< appSettings >` in *Web.config* or *appsettings.json*, but the values in App Service override the ones in *Web.config* or *appsettings.json*. You can keep development settings (for example, local MySQL password) in *Web.config* or *appsettings.json* and production secrets (for example, Azure MySQL database password) safely in App Service. The same code uses your development settings when you debug locally, and it uses your production secrets when deployed to Azure.

App settings are always encrypted when stored (encrypted-at-rest).

### Adding and Editing Settings

To add a new app setting, select **New application setting**. If you're using deployment slots you can specify if your setting is swappable or not. In the dialog, you can stick the setting to the current slot.

<edukamu-image url="/graphics/module1/app-configure-slotsetting.png" alt="Selecting deployment slot setting to stick the setting to the current slot.">
<br>

To edit a setting, select the **Edit** button on the right side.

When finished, select **Update**. Don't forget to select **Save** back in the **Configuration** page.

### Connection Strings

For ASP.NET and ASP.NET Core developers, the values you set in App Service override the ones in Web.config. For other language stacks, it's better to use app settings instead, because connection strings require special formatting in the variable keys in order to access the values. Connection strings are always encrypted when stored (encrypted-at-rest).

**Tip**: There is one case in which you may want to use connection strings instead of app settings for non-.NET languages: certain Azure database types are backed up along with the app only if you configure a connection string for the database in your App Service app.

Adding and editing connection strings follow the same principles as other app settings and they can also be tied to deployment slots. An example of connection strings in JSON formatting that you would use for bulk adding or editing:

JSON

```JSON
[
  {
    "name": "name-1",
    "value": "conn-string-1",
    "type": "SQLServer",
    "slotSetting": false
  },
  {
    "name": "name-2",
    "value": "conn-string-2",
    "type": "PostgreSQL",
    "slotSetting": false
  },
  ...
]
```

### Configuring General Settings

In the **Configuration > General** settings section you can configure some common settings for your app. Some settings require you to scale up to higher pricing tiers.

A list of the currently available settings:

- **Stack settings**: The software stack to run the app, including the language and SDK versions. For Linux apps and custom container apps, you can also set an optional start-up command or file.

<edukamu-image url="/graphics/module1/open-general-linux.png" alt="Establishing the stack settings that include the programming language.">
<br>

- **Platform settings: Lets you configure settings for the hosting platform, including**:
    - **Bitness**: 32-bit or 64-bit.
    - **WebSocket protocol**: For ASP.NET SignalR or socket.io, for example.
    - **Always On**: Keep the app loaded even when there's no traffic. By default, **Always On** isn't enabled and the app is unloaded after 20 minutes without any incoming requests. It's required for continuous WebJobs or for WebJobs that are triggered using a CRON expression.
    - **Managed pipeline version**: The IIS pipeline mode. Set it to **Classic** if you have a legacy app that requires an older version of IIS.
    - **HTTP version**: Set to 2.0 to enable support for HTTPS/2 protocol.
    - **ARR affinity**: In a multi-instance deployment, ensure that the client is routed to the same instance for the life of the session. You can set this option to **Off** for stateless applications.
    - **Debugging**: Enable remote debugging for ASP.NET, ASP.NET Core, or Node.js apps. This option turns off automatically after 48 hours.
    - **Incoming client certificates**: require client certificates in mutual authentication. TLS mutual authentication is used to restrict access to your app by enabling different types of authentication for it.

</edukamu-collapse>
<br>

Remember to check out the settings and tools explored on this course regularly, if you have an active Azure subscription. There is a free Azure trial available for everyone, and you can activate your by following the step-by-step instructions below.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step-by-Step Guide for Activating a Free Azure Trial
</edukamu-collapse-hidden-title>

If you're having trouble activating your free Azure trial needed for accessing Microsoft Azure, follow the step-by-step instructions below.

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

1. Navigate to <edukamu-link url="https://azure.microsoft.com/en-us/" target="_blank">Microsoft Azure</edukamu-link>.
2. Click "Sign in".

<edukamu-image url="/graphics/module1/step-2.jpeg" alt="Screenshot from Microsoft Azure homepage with highlighted Sign in -button at the top of the page." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Sign in to your account.
</li>
</ol>
</edukamu-section>

Notice that you need a Microsoft account in order to use activate a free Azure trial. You can either use your organizational account (such as school or work) or create a new one free of charge.

<edukamu-image url="/graphics/module1/step-3.jpeg" alt="Screenshot from Sign in -view with the highlighted Next -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Enter your password.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-4.jpeg" alt="Screenshot from Enter Password -view with the highlighted Sign in -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click the "Subscriptions" icon.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-5.jpeg" alt="Screenshot from Azure services menu with highlighted Subscriptions -icon." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click this "+ Add" icon to add a new Subscription.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-6.jpeg" alt="Screenshot from Subscription -view with highlighted + Add -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 7;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click "Try Azure for free"; We will add a trial subscription in this example.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-7.jpeg" alt="Screenshot from Free trial -view with highlighted Try Azure for free -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 8;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Fill in your details including your phone number for identity verification.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-8.jpeg" alt="Screenshot from personal information fields with highlighted Phone -field." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 9;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click "Text me".
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-9.jpeg" alt="Screenshot from personal information fields with highlighted Text me -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 10;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Type in the code and then click "Verify code".
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-10.jpeg" alt="Screenshot from personal information fields with written verification code and highlighted Verify code -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 11;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Fill in the rest of the form.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-11.jpeg" alt="Screenshot from personal information fields with highlighted Address line 1 -field." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 12;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Accept Agreements.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-12.jpeg" alt="Screenshot from personal information fields with accepted agreements." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 13;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click "Next".
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-13.jpeg" alt="Screenshot from personal information fields with highlighted Next -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 14;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Fill in your credit card information for Identity Verification (you will not be charged) and click "Sign up".
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/step-14.jpeg" alt="Screenshot from personal information fields with highlighted Sign up -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

You can find additional information about Microsoft Azure's free trial (also needed for accessing Power Platform) over at <edukamu-link url="https://azure.microsoft.com/en-us/free" target="_blank">Microsoft's website</edukamu-link>.

If setting up a free Azure trial isn't possible for one reason or another, don't worry. You can still follow the practical exercises carefully and complete the courses without exploring Microsoft Azure yourself.

</edukamu-collapse>
<br>

It's not mandatory to explore Azure on your own during this course, but we highly recommend that you do so if you have the opportunity!

All right, let's move on to something called *path mappings*. This curious term refers to settings that define how paths (URLs) in your web app are handled. They essentially tell the web server which folder to look in for certain types of files or requests.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Configuring Path Mappings
</edukamu-collapse-hidden-title>

In the **Configuration > Path mappings** section you can configure handler mappings, and virtual application and directory mappings. The **Path mappings** page displays different options based on the OS and/or application type (uncontainerized/containerized).

Uncontainerized apps in Azure App Service are traditional web applications running directly on Azure's managed Windows servers. They don't use containers, so the app runs directly on the infrastructure provided by Azure.

Containerized apps, often associated with Linux in Azure App Service, are applications that are packaged with all their dependencies into containers. These containers are then run on Azure's Linux-based infrastructure. Containerization allows for greater consistency across environments and can simplify deployment and scaling.

</edukamu-collapse>
<br>

You could, for example set a path mapping to direct all requests for images (like "/images") to a specific folder in your app. This allows for more organized and efficient handling of different types of content and requests in your application. From the user's perspective, this would greatly improve the smoothness of the user experience.

When configuring a web app with Azure App Service, *diagnostic logging* is another important perspective to consider. In practice, it is a feature that records information about the operation of a web app while security certificates can significantly improve the security of your app - and, in consequence, the users.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Diagnostic Logging
</edukamu-collapse-hidden-title>

There are built-in diagnostics to assist with debugging an App Service app.

These logs can include data about HTTP traffic, server errors, and other system events. This information is crucial for troubleshooting issues, monitoring the app’s performance, and understanding how users interact with the app.

The following table shows the types of logging, the platforms supported, and where the logs can be stored and located for accessing the information.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="13,33%">
**Type**
</edukamu-table-header>
<edukamu-table-header width="13,33%">
**Platform**
</edukamu-table-header>
<edukamu-table-header width="13,33%">
**Location**
</edukamu-table-header>
<edukamu-table-header width="60%">
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Application logging
</edukamu-table-cell>
<edukamu-table-cell>
Windows, Linux
</edukamu-table-cell>
<edukamu-table-cell>
App Service file system and/or Azure Storage blobs
</edukamu-table-cell>
<edukamu-table-cell>
Logs messages generated by your application code. The messages are generated by the web framework you choose, or from your application code directly using the standard logging pattern of your language. Each message is assigned one of the following categories: **Critical**, **Error**, **Warning**, **Info**, **Debug**, and **Trace**.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Web server logging
</edukamu-table-cell>
<edukamu-table-cell>
Windows
</edukamu-table-cell>
<edukamu-table-cell>
App Service file system or Azure Storage blobs
</edukamu-table-cell>
<edukamu-table-cell>
Raw HTTP request data in the W3C extended log file format. Each log message includes data like the HTTP method, resource URI, client IP, client port, user agent, response code, and so on.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Detailed error logging
</edukamu-table-cell>
<edukamu-table-cell>
Windows
</edukamu-table-cell>
<edukamu-table-cell>
App Service file system
</edukamu-table-cell>
<edukamu-table-cell>
Copies of the *.html* error pages that would have been sent to the client browser. For security reasons, detailed error pages shouldn't be sent to clients in production, but App Service can save the error page each time an application error occurs that has HTTP code 400 or greater.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Failed request tracing
</edukamu-table-cell>
<edukamu-table-cell>
Windows
</edukamu-table-cell>
<edukamu-table-cell>
App Service file system
</edukamu-table-cell>
<edukamu-table-cell>
Detailed tracing information on failed requests, including a trace of the IIS components used to process the request and the time taken in each component. One folder is generated for each failed request, which contains the XML log file, and the XSL stylesheet to view the log file with.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Deployment logging
</edukamu-table-cell>
<edukamu-table-cell>
Windows, Linux
</edukamu-table-cell>
<edukamu-table-cell>
App Service file system
</edukamu-table-cell>
<edukamu-table-cell>
Helps determine why a deployment failed. Deployment logging happens automatically and there are no configurable settings for deployment logging.
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
### Security Certifications
</edukamu-collapse-hidden-title>

Imagine being asked to help secure information being transmitted between your company’s app and the customer. Azure App Service has tools that let you create, upload, or import a private certificate or a public certificate into App Service.

A certificate uploaded into an app is stored in a deployment unit that is bound to the app service plan's resource group and region combination (internally called a webspace). This makes the certificate accessible to other apps in the same resource group and region combination.

The table below details the options you have for adding certificates in App Service:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Option**
</edukamu-table-header>
<edukamu-table-header>
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Create a free App Service managed certificate
</edukamu-table-cell>
<edukamu-table-cell>
A private certificate that's free of charge and easy to use if you just need to secure your custom domain in App Service.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Purchase an App Service certificate
</edukamu-table-cell>
<edukamu-table-cell>
A private certificate that's managed by Azure. It combines the simplicity of automated certificate management and the flexibility of renewal and export options.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Import a certificate from Key Vault
</edukamu-table-cell>
<edukamu-table-cell>
Useful if you use Azure Key Vault to manage your certificates.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Upload a private certificate
</edukamu-table-cell>
<edukamu-table-cell>
If you already have a private certificate from a third-party provider, you can upload it.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Upload a public certificate
</edukamu-table-cell>
<edukamu-table-cell>
Public certificates aren't used to secure custom domains, but you can load them into your code if you need them to access remote resources.
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
Diagnostic logging and security certificates are essential for the optimal functioning of web apps. 

Diagnostic logging plays a crucial role in monitoring and troubleshooting, allowing developers to track the app’s performance and quickly identify and rectify any issues, while security certificates provide encryption for data transmitted between the user and the server. This encryption is vital for protecting sensitive user information and building user trust, which is integral to the overall effectiveness and reliability of web applications.

While you might be tempted to think that configuring web apps is something you'd only do when setting up the application, this is not the full story. In reality, configurations might vary over time, as new features are added and new compliance requirements enforced.

With this being the case, it's vital to think of configurations as something that affect the apps entire life cycle, not just the beginning.

It's time for another exercise. We've covered some pretty challenging concepts here, so take some time to recap!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Configuring Web Apps
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/configuring-web-apps-question-scroll-1.yaml" id="ghnyspktmkt7k293">
<br>

</edukamu-collapse>
<br>

Azure App Service is suitable for both newcomers and experienced developers, since it includes a wide array of tools and capabilities for all imaginable use cases.

In this course, we won't dig deep into the details, but we'll still cover a lot. During the previous courses, we've used practical exercises from time to time to consolidate the knowledge, and this course is no exception - it's time for the first practical exercise!

Please remember that completing the practical exercises is not a requirement for completing the course.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Deploying an ASP.NET Web App with Azure App Service
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

In this exercise, you'll deploy your very own ASP.NET web application with Azure App Service. In order to get started, please make sure that you have 1) an Azure account with an active subscription (trial or paid) and 2) a GitHub account.

In this quickstart, you learn how to create and deploy your first ASP.NET web app to Azure App Service. App Service supports various versions of .NET apps, and provides a highly scalable, self-patching web hosting service. ASP.NET web apps are cross-platform and can be hosted on Linux or Windows, which makes them a great alternative for everyone developing their first web apps.

Let's get started, shall we? Before beginning, make sure you are signed into Azure and GitHub.

### Step 1. Forking a Demo Project

In this step, you'll fork a demo project in order to deploy it. Forking refers to creating a personal copy of someone else's project. This allows you to freely experiment with changes without affecting the original project. In this exercise, forking involves creating your own copy of a sample .NET Core application from Microsoft's repository in GitHub.

(This example uses the .NET 7.0 framework.)

1. Navigate to GitHub (.NET 7.0 Sample App).

<edukamu-button url="https://github.com/Azure-Samples/dotnetcore-docs-hello-world" target="_blank">GitHub: .NET 7.0 Sample</edukamu-button>
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select the <span style="font-weight: bold">Fork</span> button in the upper right on the GitHub page.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select the <span style="font-weight: bold">Owner</span> and leave the default <span style="font-weight: bold">Repository name</span>.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold">Create fork</span>.
</li>
</ol>
</edukamu-section>

After completing the steps above, you can freely use the example app you just forked from Microsoft's repository. (This is also an example of the benefits of commaborative platforms, such as GitHub!)

The second thing to do is publish the web app.


### Step 2. Publishing Your App

The AZD template (a template used in Azure App Service) contains files that will generate the following required resources for your application to run in App service:
- A new resource group to contain all of the Azure resources for the service.
- A new App Service plan that specifies the location, size, and features of the web server farm that hosts your app.
- A new App Service app instance to run the deployed application.

Follow these steps to create your App Service resources and publish your project:

1. Navigate to **Azure Portal**. Type **app services** in the search. Under **Services**, select **App Services**.

<edukamu-image url="/graphics/module1/portal-search.png" alt="Screenshot of portal search in the Azure portal." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the <span style="font-weight: bold">App Services</span> page, select + <span style="font-weight: bold">Create</span>.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the <span style="font-weight: bold">Basics</span> tab:
</li>
</ol>
</edukamu-section>
- Under **Resource group**, select **Create new**. Type *myResourceGroup* for the name.
- Under **Name**, type a globally unique name for your web app.
- Under **Publish**, select *Code*.
- Under **Runtime stack** select *.NET 7 (STS)*.
- Select an **Operating System**, and a **Region** you want to serve your app from.
- Under **App Service Plan**, select **Create new** and type *myAppServicePlan* for the name.
- Under **Pricing plan**, select **Free F1**.

<edukamu-image url="/graphics/module1/app-service-details-net-70.png" alt="Screenshot of new App Service app configuration for .NET 7 in the Azure portal." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select the <span style="font-weight: bold">Next: Deployment</span> > button at the bottom of the page.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the <span style="font-weight: bold">Deployment</span> tab, under <span style="font-weight: bold">GitHub Actions settings</span> make sure <span style="font-weight: bold">Continuous deployment</span> is <span style="font-style: italic">Enable</span>.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Under <span style="font-weight: bold">GitHub Actions details</span>, authenticate with your GitHub account, and select the following options:
</li>
</ol>
</edukamu-section>
- For **Organization** select the organization where you have forked the demo project.
- For **Repository** select the *dotnetcore-docs-hello-world* project.
- For **Branch** select *master*.

<edukamu-image url="/graphics/module1/app-service-deploy-60.png" alt="Screenshot of the deployment options for an app using the .NET 6 runtime." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 7;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select the <span style="font-weight: bold">Review + create</span> button at the bottom of the page.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 8;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
After validation runs, select the <span style="font-weight: bold">Create</span> button at the bottom of the page.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 9;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
After deployment is complete, select <span style="font-weight: bold">Go to resource</span>.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/next-steps.png" alt="Screenshot of the next step of going to the resource." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 10;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Browse to the deployed application in your web browser at the URL <code>http://< app-name >.azurewebsites.net</code>.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/browse-dotnet-70.png" alt="Screenshot of the deployed .NET 7.0 sample app." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Your app should now be live!


### Step 3. Managing Your App

To manage your web app, go to the Azure portal, and search for and select **App Services**.

<edukamu-image url="/graphics/module1/app-services.png" alt="Screenshot of the Azure portal - Select App Services option.">
<br>

On the **App Services** page, select the name of your web app.

<edukamu-image url="/graphics/module1/select-app-service.png" alt="Screenshot of the Azure portal - App Services page with an example web app selected.">
<br>

The **Overview** page for your web app, contains options for basic management like browse, stop, start, restart, and delete. The left menu provides further pages for configuring your app.

<edukamu-image url="/graphics/module1/web-app-overview-page.png" alt="Screenshot of the Azure portal - App Service overview page.">
<br>

Please take all the time you want browsing the options!

</edukamu-collapse>
<br>

Deploying web apps with Azure App Service doesn't seem that difficult, does it? In a real-life scenario, the steps taken would be quite a bit more complicated, of course, but the same basic principles apply!

Whenever you are ready, feel free to move on to Azure Functions.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
