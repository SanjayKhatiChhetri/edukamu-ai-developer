## Exploring API Management

After spending some time with the security features of Azure, it's time to revisit an old topic we've come across multiple times during this program - application programming interfaces, or APIs for short.

In short, APIs are mechanisms that make it possible for two software components to communicate with each other. Essentially, this means two instances "talking" to each other in order to exchange information: You might for example use your phone to find about the weather forecast for tomorrow. The app you use would use an API to connect to a weather service's database in order to fill your request.

Since APIs are vital for all developing projects,  Azure includes a service for managing these all-important interfaces. On this page, we'll get to know Azure API Management and its main capabilities. While API Management isn’t strictly necessary for any application – you could just expose your APIs as HTTP endpoints from your App Service or your containers –
most real-world applications with significant API capabilities use an API Management layer to ensure that this critical piece of architecture is as solid, secure, and speedy as possible.

As always, it's best to start with a little introduction.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure API Management
</edukamu-collapse-hidden-title>

API Management provides the core functionality to ensure a successful API program through developer engagement, business insights, analytics, security, and protection. Each API consists of one or more operations, and each API can be added to one or more products. To use an API, developers subscribe to a product that contains that API, and then they can call the API's operation, subject to any usage policies that may be in effect.

### API Management Components

Azure API Management is made up of an *API gateway*, a *management plane*, and a *developer portal*. These components are Azure-hosted and fully managed by default. API Management is available in various [tiers](https://learn.microsoft.com/en-us/azure/api-management/api-management-features)(target="_blank") differing in capacity and features.

- The **API gateway** is the endpoint that:
    - Accepts API calls and routes them to appropriate backends
    - Verifies API keys and other credentials presented with requests
    - Enforces usage quotas and rate limits
    - Transforms requests and responses specified in policy statements
    - Caches responses to improve response latency and minimize the load on backend services
    - Emits logs, metrics, and traces for monitoring, reporting, and troubleshooting
- The **management plane** is the administrative interface where you set up your API program. Use it to:
    - Provision and configure API Management service settings
    - Define or import API schema
    - Package APIs into products
    - Set up policies like quotas or transformations on the APIs
    - Get insights from analytics
    - Manage users
- The **Developer portal** is an automatically generated, fully customizable website with the documentation of your APIs. Using the developer portal, developers can:
    - Read API documentation
    - Call an API via the interactive console
    - Create an account and subscribe to get API keys
    - Access analytics on their own usage
    - Download API definitions
    - Manage API keys


### Products

Products are how APIs are surfaced to developers. Products in API Management have one or more APIs, and are configured with a title, description, and terms of use. Products can be Open or Protected. Protected products must be subscribed to before they can be used, while open products can be used without a subscription. Subscription approval is configured at the product level and can either require administrator approval, or be autoapproved.

### Groups

Groups are used to manage the visibility of products to developers. API Management has the following immutable system groups:

- **Administrators** - Manage API Management service instances and create the APIs, operations, and products that are used by developers. Azure subscription administrators are members of this group.
- **Developers** - Authenticated developer portal users that build applications using your APIs. Developers are granted access to the developer portal and build applications that call the operations of an API.
- **Guests** - Unauthenticated developer portal users. They can be granted certain read-only access, like the ability to view APIs but not call them.

In addition to these system groups, administrators can create custom groups or use external groups in associated Microsoft Entra tenants.

### Developers

Developers represent the user accounts in an API Management service instance. Developers can be created or invited to join by administrators, or they can sign up from the Developer portal. Each developer is a member of one or more groups, and can subscribe to the products that grant visibility to those groups.

### Policies

Policies are a collection of statements that are executed sequentially on the request or response of an API. Popular statements include format conversion from XML to JSON and call rate limiting to restrict the number of incoming calls from a developer, and many other policies are available.

Policy expressions can be used as attribute values or text values in any of the API Management policies, unless the policy specifies otherwise. Some policies such as the Control flow and Set variable policies are based on policy expressions.

Policies can be applied at different scopes, depending on your needs: global (all APIs), a product, a specific API, or an API operation.

</edukamu-collapse>
<br>

The API Management service allows developers to control some of the operating principles of your APIs as well as define and import API schemas, manage users, explore analytics, and a host of other things. Depending on your previous experiences, this "API talk" might sound a bit abstract or even confusing, so please take your time as you follow exploring this section!

The next feature we're about to cover is an important one. We're talking about API gateways, which refers to the part of API Management that routes requests from clients to services. Without these gateways, the weather app we used as an example before simply wouldn't function!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### API Gateways
</edukamu-collapse-hidden-title>

Your solution may contain several front- and back-end services. In this scenario, how does a client know what endpoints to call? What happens when new services are introduced, or existing services are refactored? How do services handle SSL termination, authentication, and other concerns?

The API Management gateway (also called data plane or runtime) is the service component that's responsible for proxying API requests, applying policies, and collecting telemetry.

An API gateway sits between clients and services. It acts as a reverse proxy, routing requests from clients to services. It may also perform various cross-cutting tasks such as authentication, SSL termination, and rate limiting. If you don't deploy a gateway, clients must send requests directly to back-end services. However, there are some potential problems with exposing services directly to clients:

- It can result in complex client code. The client must keep track of multiple endpoints, and handle failures in a resilient way.
- It creates coupling between the client and the backend. The client needs to know how the individual services are decomposed. That makes it harder to maintain the client and also harder to refactor services.
- A single operation might require calls to multiple services.
- Each public-facing service must handle concerns such as authentication, SSL, and client rate limiting.
- Services must expose a client-friendly protocol such as HTTP or WebSocket. This limits the choice of communication protocols.
- Services with public endpoints are a potential attack surface, and must be hardened.

A gateway helps to address these issues by decoupling clients from services.

### Managed or Self-hosted

API Management offers both managed and self-hosted gateways:

- **Managed** - The managed gateway is the default gateway component that is deployed in Azure for every API Management instance in every service tier. With the managed gateway, all API traffic flows through Azure regardless of where backends implementing the APIs are hosted.
- **Self-hosted** - The self-hosted gateway is an optional, containerized version of the default managed gateway. It's useful for hybrid and multicloud scenarios where there's a requirement to run the gateways off of Azure in the same environments where API backends are hosted. The self-hosted gateway enables customers with hybrid IT infrastructure to manage APIs hosted on-premises and across clouds from a single API Management service in Azure.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
In Azure API Management, policies allow the publisher to change the behavior of the API through configuration. Policies are a collection of statements that are executed on the request or response of an API. 

Policies allow you a measure of centralized configuration without actually touching the code. For example, you could perform some validation or transformation on the inbound request. While logic like this is more limited than what you would do if you actually can change the code, the ability to make these changes instantly at the API Management level allows you to support experiments, upgrades and other situations even without deploying a new version of the code. 

Similarly, a typical outbound policy scenario is *response caching*. Perhaps you know that your e-commerce application doesn’t really need real-time information on pricing – a one-minute delay may well be acceptable. If you implement this caching at API Management level, your application will see only one request for your pricing API – no matter how many customers are served. This allows you to leverage logical caching to conserve compute and data resources, a key practice to cutting costs in a pay-as-you-go cloud environment.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Understanding API Management Policies
</edukamu-collapse-hidden-title>

Policies are applied inside the gateway that sits between the API consumer and the managed API. The gateway receives all requests and usually forwards them unaltered to the underlying API. However a policy can apply changes to both the inbound request and outbound response. Policy expressions can be used as attribute values or text values in any of the API Management policies, unless the policy specifies otherwise.

### Policy Configuration

The policy definition is a simple XML document that describes a sequence of inbound and outbound statements. The XML can be edited directly in the definition window.

The configuration is divided into `inbound`, `backend`, `outbound`, and `on-error`. The series of specified policy statements is executed in order for a request and a response.

XML

<edukamu-image url="/graphics/module3/2024-02-06-policy-conf-code-example.svg" alt="" style="">
<br>

If there's an error during the processing of a request, any remaining steps in the `inbound`, `backend`, or `outbound` sections are skipped and execution jumps to the statements in the `on-error` section. By placing policy statements in the `on-error` section you can review the error by using the `context.LastError` property, inspect and customize the error response using the `set-body` policy, and configure what happens if an error occurs.

### Policy Expressions

Unless the policy specifies otherwise, policy expressions can be used as attribute values or text values in any of the API Management policies. A policy expression is either:

- a single C# statement enclosed in `@(expression)`, or
- a multi-statement C# code block, enclosed in `@{expression}`, that returns a value.

Each expression has access to the implicitly provided `context` variable and an allowed subset of .NET Framework types.

Policy expressions provide a sophisticated means to control traffic and modify API behavior without requiring you to write specialized code or modify backend services.

The following example uses policy expressions and the set-header policy to add user data to the incoming request. The added header includes the user ID associated with the subscription key in the request, and the region where the gateway processing the request is hosted.

XML

```XML
<policies>
    <inbound>
        <base />
        <set-header name="x-request-context-data" exists-action="override">
            <value>@(context.User.Id)</value>
            <value>@(context.Deployment.Region)</value>
      </set-header>
    </inbound>
</policies>
```

### Applying Policies for Different Scopes

If you have a policy at the global level and a policy configured for an API, then whenever that particular API is used both policies are applied. API Management allows for deterministic ordering of combined policy statements via the base element.

XML

<edukamu-image url="/graphics/module3/2024-02-06-applying-policies-code-example.svg" alt="" style="">
<br>

In the previous example policy definition, The `cross-domain` statement would execute first. The `find-and-replace` policy would execute after any policies at a broader scope.

### Filtering Response Content

The policy defined in following example demonstrates how to filter data elements from the response payload based on the product associated with the request.

The snippet assumes that response content is formatted as JSON and contains root-level properties named "minutely", "hourly", "daily", "flags".

XML

<edukamu-image url="/graphics/module3/2024-02-06-filtering-response-content-code-example.svg" alt="" style="">
<br>

</edukamu-collapse>
<br>

The examples in the previous section included some quite complicated examples, but try your best to understand them.

If you're looking for a real challenge, please take a look at the following. If you feel like you're note (yet!) at the level required, feel free to skip the advanced policies presented below.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Advanced Policies
</edukamu-collapse-hidden-title>

In this section, we'll review the following API Management policies:

- Control flow - Conditionally applies policy statements based on the results of the evaluation of Boolean expressions.
- Forward request - Forwards the request to the backend service.
- Limit concurrency - Prevents enclosed policies from executing by more than the specified number of requests at a time.
- Log to Event Hub - Sends messages in the specified format to an Event Hub defined by a Logger entity.
- Mock response - Aborts pipeline execution and returns a mocked response directly to the caller.
- Retry - Retries execution of the enclosed policy statements, if and until the condition is met. Execution will repeat at the specified time intervals and up to the specified retry count.

### Control Flow

The `choose` policy applies enclosed policy statements based on the outcome of evaluation of boolean expressions, similar to an if-then-else or a switch construct in a programming language.

XML

<edukamu-image url="/graphics/module3/2024-02-06-control-flow-code-example.svg" alt="" style="">
<br>

The control flow policy must contain at least one `< when />` element. The `< otherwise />` element is optional. Conditions in `< when />` elements are evaluated in order of their appearance within the policy. Policy statement(s) enclosed within the first `< when />` element with condition attribute equals true will be applied. Policies enclosed within the `< otherwise />` element, if present, will be applied if all of the `< when />` element condition attributes are false.


### Forward Request

The `forward-request` policy forwards the incoming request to the backend service specified in the request context. The backend service URL is specified in the API settings and can be changed using the set backend service policy.

Removing this policy results in the request not being forwarded to the backend service and the policies in the outbound section are evaluated immediately upon the successful completion of the policies in the inbound section.

XML

<edukamu-image url="/graphics/module3/2024-02-06-forward-req-code-example.svg" alt="" style="">
<br>


### Limit Concurrency

The `limit-concurrency` policy prevents enclosed policies from executing by more than the specified number of requests at any time. Upon exceeding that number, new requests will fail immediately with a *429 Too Many Requests* status code.

XML

<edukamu-image url="/graphics/module3/2024-02-06-limit-concurrency-code-example.svg" alt="" style="">
<br>


### Log to Event Hub

The `log-to-eventhub` policy sends messages in the specified format to an Event Hub defined by a Logger entity. As its name implies, the policy is used for saving selected request or response context information for online or offline analysis.

XML

```XML
<log-to-eventhub logger-id="id of the logger entity" partition-id="index of the partition where messages are sent" partition-key="value used for partition assignment">
  Expression returning a string to be logged
</log-to-eventhub>
```


### Mock Response

The `mock-response`, as the name implies, is used to mock APIs and operations. It aborts normal pipeline execution and returns a mocked response to the caller. The policy always tries to return responses of highest fidelity. It prefers response content examples, whenever available. It generates sample responses from schemas, when schemas are provided and examples are not. If neither examples or schemas are found, responses with no content are returned.

XML

<edukamu-image url="/graphics/module3/2024-02-06-mock-response-code-example.svg" alt="" style="">
<br>


### Retry

The `retry` policy executes its child policies once and then retries their execution until the retry `condition` becomes `false` or retry count is exhausted.

XML

<edukamu-image url="/graphics/module3/2024-02-06-mock-response-retry-code-example.svg" alt="" style="">
<br>


### Return Response

The `return-response` policy aborts pipeline execution and returns either a default or custom response to the caller. Default response is `200 OK` with no body. Custom response can be specified via a context variable or policy statements. When both are provided, the response contained within the context variable is modified by the policy statements before being returned to the caller.

XML

<edukamu-image url="/graphics/module3/2024-02-06-mock-response-return-response-code-example.svg" alt="" style="">
<br>

</edukamu-collapse>
<br>


When you publish APIs through API Management, it's easy and common to secure access to those APIs by using subscription keys. It's not only about security, since without a key, any request sent to an API is immediately rejected.

Next up, securing access to APIs.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### APIs and Subscriptions
</edukamu-collapse-hidden-title>

Developers who need to consume oublicly published APIs must include a valid subscription key in HTTP requests when they make calls to those APIs. Otherwise, the calls are rejected immediately by the API Management gateway. They aren't forwarded to the back-end services.

To get a subscription key for accessing APIs, a subscription is required. A subscription is essentially a named container for a pair of subscription keys. Developers who need to consume the published APIs can get subscriptions. And they don't need approval from API publishers. API publishers can also create subscriptions directly for API consumers.

**Note**: API Management also supports other mechanisms for securing access to APIs, including: OAuth2.0, Client certificates, and IP allow listing.

### Subscriptions and Keys

A subscription key is a unique auto-generated key that can be passed through in the headers of the client request or as a query string parameter. The key is directly related to a subscription, which can be scoped to different areas. Subscriptions give you granular control over permissions and policies.

The three main subscription scopes are:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
**Scope**
</edukamu-table-header>
<edukamu-table-header width="70%">
**Details**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
All APIs
</edukamu-table-cell>
<edukamu-table-cell>
Applies to every API accessible from the gateway.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Single API
</edukamu-table-cell>
<edukamu-table-cell>
This scope applies to a single imported API and all of its endpoints.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Product
</edukamu-table-cell>
<edukamu-table-cell>
A product is a collection of one or more APIs that you configure in API Management. You can assign APIs to more than one product. Products can have different access rules, usage quotas, and terms of use.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

Applications that call a protected API must include the key in every request.

You can regenerate these subscription keys at any time, for example, if you suspect that a key has been shared with unauthorized users.

<edukamu-image url="/graphics/module3/subscription-keys.png" alt="Image showing the Subscriptions screen with highlighted sections of primary key and secondary key." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Every subscription has two keys, a primary and a secondary. Having two keys makes it easier when you do need to regenerate a key. For example, if you want to change the primary key and avoid downtime, use the secondary key in your apps.

For products where subscriptions are enabled, clients must supply a key when making calls to APIs in that product. Developers can obtain a key by submitting a subscription request. If you approve the request, you must send them the subscription key securely, for example, in an encrypted message. This step is a core part of the API Management workflow.

### Subscription Keys and API Calls

Applications must include a valid key in all HTTP requests when they make calls to API endpoints that are protected by a subscription. Keys can be passed in the request header, or as a query string in the URL.

The default header name is **Ocp-Apim-Subscription-Key**, and the default query string is **subscription-key**.

To test out your API calls, you can use the developer portal, or command-line tools, such as **curl**. Here's an example of a `GET` request using the developer portal, which shows the subscription key header:

<edukamu-image url="/graphics/module3/key-header-portal.png" alt="Call A P I from developer portal." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Here's how you can pass a key in the request header using **curl**:

Bash

<edukamu-image url="/graphics/module3/2024-02-06-curl-key-req-code-example.svg" alt="" style="">
<br>

Here's an example curl command that passes a key in the URL as a query string:

Bash

<edukamu-image url="/graphics/module3/2024-02-06-curl-key-pass-code-example.svg" alt="" style="">
<br>

If the key is not passed in the header, or as a query string in the URL, you'll get a 401 Access Denied response from the API gateway.

</edukamu-collapse>
<br>


In summary, subscription keys are used to ensure that the application has the right to access an API, and thus, data. If the process described above seems a little confusing, don't worry.  In the next section, we’ll look into the life cycle of an API call in more detail, which should make things clearer.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### API Calls in Detail
</edukamu-collapse-hidden-title>

In this section, we'll take a detailed look at API calls. We'll use the weather app example which we've already come across a few times during this program. This time, let's include the role of subscription keys.

<edukamu-image url="/graphics/module3/weather-api.png" alt="An illustration showing a weather app making an API call to a weather service database using Azure API Management." style="max-width: 80%;">
<br>

Making an API call involves sending a request to an Application Programming Interface (API) to retrieve data or trigger actions defined by that API. An API acts as an intermediary that allows two software applications to communicate with each other. Here's a detailed summary of what happens when an API is used, using a weather app as an example:

1. **User Action**: The process begins with a user action, such as opening a weather app to check the forecast or current weather conditions.
2. **API Call Preparation**: In response, the weather app prepares an API call. This involves constructing an HTTP request targeted at the weather service’s API. The request includes elements like the API endpoint URL, a request method (typically GET for retrieving data), and any necessary headers.
3. **Incorporating Subscription Keys**: To authenticate the request, the app includes a subscription key in the request header. Subscription keys are unique identifiers provided by the API provider (in this case, the weather service). They serve as an access token, granting the app permission to use the API. By including this key, the app proves its identity and authorization to the API.
4. **Sending the Request**: The app sends the request to the weather service's API. The request travels over the internet to the API's server.
5. **API Server Processing**: The API server receives the request and first validates the subscription key. If the key is valid and has the necessary permissions, the server processes the request, fetching the requested weather data from its databases or other data sources.
6. **Response Creation and Transmission**: The API packages the requested weather data (or an error message if something went wrong, like an invalid key) into a response, typically formatted in JSON or XML. This response is then sent back to the weather app.
7. **App Processes the Response**: Upon receiving the response, the weather app decodes the data. If the response indicates a successful request, the app parses the JSON or XML to extract the weather information.
8. **Displaying Data to the User**: Finally, the weather app updates its user interface with the received information, such as temperature, weather conditions, or forecasts, for the user to view.

Subscription keys play a crucial role in authenticating the API request. They ensure that only authorized users or applications can access the API, helping the API provider to manage usage, enforce quotas, or bill clients. They are a critical component of API security and access management, especially in commercial APIs where access needs to be controlled and monitored.

</edukamu-collapse>
<br>

In summary, making an API call is a multi-step process involving user interaction, request preparation and transmission, server-side processing, and response handling. In our weather app example, the API serves as a bridge between the app and the weather data source, allowing the app to fetch and display weather data without needing to have direct access to the primary data source.

Subscription keys are a simple approach to authentication and authorization. They are not the only way of securing APIs, though, and more security-conscious applications may need to avoid them to reduce the risk of a security credential – the API key – falling into the wrong hands.

Other authentication approaches include certificates – a cryptographic approach to identifying the caller – as well as Entra ID, which ties in nicely with Managed Identities discussed earlier. These more advanced authentication types are beyond the scope of this course, but for most enterprise applications, you should definitely look into them.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Creating a Backend API
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practice exercise, we'll set up a backend API. Application programming interfaces like this can be used to interact with back-end services, such as servers.

Follow the instructions carefully!

### Step 1. Start the Cloud Shell

This step should already be familiar from the previous exercises.

1. Sign in to the Azure Portal and open the **Cloud Shell**.
2. When the shell opens, select the **Bash** environment.


### Step 2. Create an API Management Instance

1. Let's set some variables for the CLI commands to use to reduce the amount of retyping. Replace `< myLocation >` with a region that makes sense for you. The APIM name needs to be a globally unique name, and the following script generates a random string. Replace `< myEmail >` with an email address you can access.

Bash

```Bash
myApiName=az204-apim-$RANDOM
myLocation=<myLocation>
myEmail=<myEmail>
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Create a resource group. The following commands create a resource group named <code>az204-apim-rg</code>.
</li>
</ol>
</edukamu-section>

Bash

```Bash
az group create --name az204-apim-rg --location $myLocation
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Create an APIM instance. The <code>az apim create</code> command is used to create the instance. The <code>--sku-name Consumption</code> option is used to speed up the process for the walkthrough.
</li>
</ol>
</edukamu-section>

Bash

```Bash
az apim create -n $myApiName \
    --location $myLocation \
    --publisher-email $myEmail  \
    --resource-group az204-apim-rg \
    --publisher-name AZ204-APIM-Exercise \
    --sku-name Consumption
```

**Note**: The operation should be complete in about five minutes, so please be patient!

### Step 3. Import a Backend API

This section shows how to import and publish an OpenAPI specification backend API.

1. In the Azure portal, search for and select **API Management services**.
2. On the **API Management** screen, select the API Management instance you created.
3. Select **APIs** in the **API management service** navigation pane.

<edukamu-image url="/graphics/module3/select-apis-navigation-pane.png" alt="Select APIs in the service navigation pane.">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold;">OpenAPI</span> from the list and select <span style="font-weight: bold;">Full</span> in the pop-up.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module3/create-api.png" alt="The OpenAPI dialog box. Fields are detailed in the following table." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Use the values from the table below to fill out the form. You can leave any fields not mentioned their default value.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Setting**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Value**
</edukamu-table-header>
<edukamu-table-header width="60%">
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**OpenAPI Specification**
</edukamu-table-cell>
<edukamu-table-cell>
`https://conferenceapi.azurewebsites.net?format=json`
</edukamu-table-cell>
<edukamu-table-cell>
References the service implementing the API, requests are forwarded to this address. Most of the necessary information in the form is automatically populated after you enter this.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Display name**
</edukamu-table-cell>
<edukamu-table-cell>
*Demo Conference API*
</edukamu-table-cell>
<edukamu-table-cell>
This name is displayed in the Developer portal.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Name**
</edukamu-table-cell>
<edukamu-table-cell>
*demo-conference-api*
</edukamu-table-cell>
<edukamu-table-cell>
Provides a unique name for the API.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Description**
</edukamu-table-cell>
<edukamu-table-cell>
Automatically populated
</edukamu-table-cell>
<edukamu-table-cell>
Provide an optional description of the API.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**API URL suffix**
</edukamu-table-cell>
<edukamu-table-cell>
*conference*
</edukamu-table-cell>
<edukamu-table-cell>
The suffix is appended to the base URL for the API management service. API Management distinguishes APIs by their suffix and therefore the suffix must be unique for every API for a given publisher.
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

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold;">Create</span>.
</li>
</ol>
</edukamu-section>



### Step 4. Configure Backend Settings

The *Demo Conference API* is created and a backend needs to be specified.

1. Select **Settings** in the blade to the right and enter `https://conferenceapi.azurewebsites.net/` in the **Web service URL** field.
2. Deselect the **Subscription required** checkbox.

<edukamu-image url="/graphics/module3/api-settings-backend.png" alt="Specify the backend URL for the API." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold;">Save</span>.
</li>
</ol>
</edukamu-section>



### Step 5. Test the API

Now that the API has been imported and the backend configured it's time to test the API.

1. Select **Test**.

<edukamu-image url="/graphics/module3/select-test.png" alt="Select test in the right pane." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Select **GetSpeakers**. The page shows **Query parameters** and **Headers**, if any. The `Ocp-Apim-Subscription-Key` is filled in automatically for the subscription key associated with this API.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold;">Send</span>.
</li>
</ol>
</edukamu-section>

Backend responds with **200 OK** and some data.


### Step 6. Clean Up Azure Resources (Optional)

When you're finished with the resources you created in this exercise you can use the command below to delete the resource group and all related resources.

Bash

```Bash
az group delete --name az204-apim-rg
```

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
The versatility and utility make APIs indispensable in the modern, increasingly digital ecosystem. Application programming interfaces are activated countless time a day in all kinds of applications and services, be it checking the weather, making a financial transaction, or simply accessing a map.

Securing the APIs is also crucial when it comes to ensuring the success of a solution. With Azure's built in API management capabilities, all these tasks can be handled relatively easily.

It's time to test out our new knowledge with an exercise. Don't forget to recap before tackling it!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: API Management
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/exploring-api-management-question-scroll-1.yaml" id="6gmb2f8p1bgxvz6y">
<br>

</edukamu-collapse>
<br>

How are you feeling at this stage? We've now covered our two main topics of the third unit. There's still something left to explore on this course, though. Let's check out some advanced development capabilities offered by Azure!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
