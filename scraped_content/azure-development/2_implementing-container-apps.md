## Implementing Container Apps

After exploring a few Azure services on offer for building and managing containerized solutions, it's time to take a while to learn about their implementation. 

In this section, we'll closely explore Azure Container Apps. We'll start with containers and make our way to authentication and authorization before wrapping up with revisions and Dapr integration. 

Without further ado, let's get started by exploring containers in Azure Container Apps!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Understanding Containers 
</edukamu-collapse-hidden-title>

Azure Container Apps manages the details of Kubernetes and container orchestration for you. Containers in Azure Container Apps can use any runtime, programming language, or development stack of your choice.

<edukamu-image url="graphics/module2/azure-container-apps-containers.png" alt="Diagram showing how containers for an Azure Container App are grouped together in pods inside revision snapshots." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Azure Container Apps supports any Linux-based x86-64 (`linux/amd64`) container image. There's no required base container image, and if a container crashes it automatically restarts.

### Configuration

The following code is an example of the `containers` array in the `properties.template` section of a container app resource template. The excerpt shows some of the available configuration options when setting up a container when using Azure Resource Manager (ARM) templates. Changes to the template ARM configuration section trigger a new container app revision.

JSON

```JSON
"containers": [
  {
       "name": "main",
       "image": "[parameters('container_image')]",
    "env": [
      {
        "name": "HTTP_PORT",
        "value": "80"
      },
      {
        "name": "SECRET_VAL",
        "secretRef": "mysecret"
      }
    ],
    "resources": {
      "cpu": 0.5,
      "memory": "1Gi"
    },
    "volumeMounts": [
      {
        "mountPath": "/myfiles",
        "volumeName": "azure-files-volume"
      }
    ]
    "probes":[
        {
            "type":"liveness",
            "httpGet":{
            "path":"/health",
            "port":8080,
            "httpHeaders":[
                {
                    "name":"Custom-Header",
                    "value":"liveness probe"
                }]
            },
            "initialDelaySeconds":7,
            "periodSeconds":3
// file is truncated for brevity
```

### Multiple Containers

You can define multiple containers in a single container app to implement the sidecar pattern. The containers in a container app share hard disk and network resources and experience the same application lifecycle.

The "sidecar pattern" refers to a design pattern in which a helper service is attached to a primary application container, much like a sidecar is attached to a motorcycle. This helper service, or "sidecar," extends or enhances the functionality of the main container without altering its core logic.

Examples of sidecar containers include:

- An agent that reads logs from the primary app container on a shared volume and forwards them to a logging service.
- A background process that refreshes a cache used by the primary app container in a shared volume.

**Note**: Running multiple containers in a single container app is an advanced use case. In most situations where you want to run multiple containers, such as when implementing a microservice architecture, deploy each service as a separate container app.

To run multiple containers in a container app, add more than one container in the containers array of the container app template.

### Container Registries

You can deploy images hosted on private registries by providing credentials in the Container Apps configuration.

To use a container registry, you define the required fields in registries array in the properties.configuration section of the container app resource template. The passwordSecretRef field identifies the name of the secret in the secrets array name where you defined the password.

JSON

```JSON
{
  ...
  "registries": [{
    "server": "docker.io",
    "username": "my-registry-user-name",
    "passwordSecretRef": "my-password-secret-name"
  }]
}
```

With the registry information added, the saved credentials can be used to pull a container image from the private registry when your app is deployed.

### Limitations

Azure Container Apps has the following limitations:
- **Privileged containers**: Azure Container Apps can't run privileged containers. If your program attempts to run a process that requires root access, the application inside the container experiences a runtime error. 
- **Operating system**: Linux-based (`linux/amd64`) container images are required. 

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Implementing Authentication and Authorization
</edukamu-collapse-hidden-title>

Azure Container Apps provides built-in authentication and authorization features to secure your external ingress-enabled container app with minimal or no code. The built-in authentication feature for Container Apps can save you time and effort by providing out-of-the-box authentication with federated identity providers, allowing you to focus on the rest of your application.

- Azure Container Apps provides access to various built-in authentication providers.
- The built-in auth features don’t require any particular language, SDK, security expertise, or even any code that you have to write.

This feature should only be used with HTTPS. Ensure `allowInsecure` is disabled on your container app's ingress configuration. You can configure your container app for authentication with or without restricting access to your site content and APIs.

- To restrict app access only to authenticated users, set its *Restrict access* setting to **Require authentication**.
- To authenticate but not restrict access, set its *Restrict access* setting to **Allow unauthenticated** access.

### Identity Providers

Container Apps uses federated identity, in which a third-party identity provider manages the user identities and authentication flow for you. The following identity providers are available by default:

### Provider

- Microsoft Identity Platform
- Facebook
- GitHub
- Google
- Twitter
- Any OpenID Connect provider

When you use one of these providers, the sign-in endpoint is available for user authentication and authentication token validation from the provider. You can provide your users with any number of these provider options.

### Feature Architecture

The authentication and authorization middleware component is a feature of the platform that runs as a sidecar container on each replica in your application. When enabled, every incoming HTTP request passes through the security layer before being handled by your application.

<edukamu-image url="/graphics/module1/container-apps-authorization-architecture.png" alt="Diagram showing requests being intercepted by a sidecar container interacting with identity providers before allowing traffic to the app container." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

The platform middleware handles several things for your app:

- Authenticates users and clients with the specified identity provider(s)
- Manages the authenticated session
- Injects identity information into HTTP request headers

The authentication and authorization module runs in a separate container, isolated from your application code. As the security container doesn't run in-process, no direct integration with specific language frameworks is possible. However, relevant information your app needs is provided in request headers.

### Authentication Flow

The authentication flow is the same for all providers, but differs depending on whether you want to sign in with the provider's SDK:

- **Without provider SDK** (server-directed flow or server flow): The application delegates federated sign-in to Container Apps. Delegation is typically the case with browser apps, which presents the provider's sign-in page to the user.
- **With provider SDK** (client-directed flow or client flow): The application signs users in to the provider manually and then submits the authentication token to Container Apps for validation. This approach is typical for browser-less apps that don't present the provider's sign-in page to the user. An example is a native mobile app that signs users in using the provider's SDK.

</edukamu-collapse>
<br>

Although Azure Container Apps, like all services, has its limitations, it is suitable for numerous use cases. As you've just learned, authentication and authorization practices are also built into the service, making the developers' life a lot easier.

There's one important aspect left to cover on this second unit, and that's Dapr integration. In this context, Dapr (Distributed Application Runtime) is a portable, event-driven runtime that simplifies building microservices. Thanks to APIs, it can be used with Container Apps.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Integrating Dapr and Azure Container Apps
</edukamu-collapse-hidden-title>

The Distributed Application Runtime (Dapr) is a set of incrementally adoptable features that simplify the authoring of distributed, microservice-based applications. Dapr provides capabilities for enabling application intercommunication through messaging via pub/sub or reliable and secure service-to-service calls.

Dapr is an open source, [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/projects/dapr/)(target="_blank") project. The CNCF is part of the Linux Foundation and provides support, oversight, and direction for fast-growing, cloud native projects. As an alternative to deploying and managing the Dapr OSS project yourself, the Container Apps platform:

- Provides a managed and supported Dapr integration
- Handles Dapr version upgrades seamlessly
- Exposes a simplified Dapr interaction model to increase developer productivity

### Dapr APIs

<edukamu-image url="/graphics/module2/azure-container-apps-distributed-application-runtime-building-blocks.png" alt="Image visualize the Dapr A P I. The content has been described below.">
<br>

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Dapr API**
</edukamu-table-header>
<edukamu-table-header>
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Service-to-service invocation
</edukamu-table-cell>
<edukamu-table-cell>
Discover services and perform reliable, direct service-to-service calls with automatic mTLS authentication and encryption.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
State management
</edukamu-table-cell>
<edukamu-table-cell>
Provides state management capabilities for transactions and CRUD operations.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Pub/sub
</edukamu-table-cell>
<edukamu-table-cell>
Allows publisher and subscriber container apps to intercommunicate via an intermediary message broker.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Bindings
</edukamu-table-cell>
<edukamu-table-cell>
Trigger your applications based on events.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Actors
</edukamu-table-cell>
<edukamu-table-cell>
Dapr actors are message-driven, single-threaded, units of work designed to quickly scale. For example, in burst-heavy workload situations.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Observability
</edukamu-table-cell>
<edukamu-table-cell>
Send tracing information to an Application Insights backend.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Secrets
</edukamu-table-cell>
<edukamu-table-cell>
Access secrets from your application code or reference secure values in your Dapr components.
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

### Dapr Core Concepts

The following example based on the Pub/sub API is used to illustrate core concepts related to Dapr in Azure Container Apps.

<edukamu-image url="/graphics/module2/distributed-application-runtime-container-apps.png" alt="Diagram that shows the Dapr pub/sub A P I and how it works in Container Apps." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="10%">
**Label**
</edukamu-table-header>
<edukamu-table-header width="30%">
**Dapr settings**
</edukamu-table-header>
<edukamu-table-header width="60%">
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
1
</edukamu-table-cell>
<edukamu-table-cell>
Container Apps with Dapr enabled
</edukamu-table-cell>
<edukamu-table-cell>
Dapr is enabled at the container app level by configuring a set of Dapr arguments. These values apply to all revisions of a given container app when running in multiple revisions mode.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
2
</edukamu-table-cell>
<edukamu-table-cell>
Dapr
</edukamu-table-cell>
<edukamu-table-cell>
The fully managed Dapr APIs are exposed to each container app through a Dapr sidecar. The Dapr APIs can be invoked from your container app via HTTP or gRPC. The Dapr sidecar runs on HTTP port 3500 and gRPC port 50001.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
3
</edukamu-table-cell>
<edukamu-table-cell>
Dapr component configuration
</edukamu-table-cell>
<edukamu-table-cell>
Dapr uses a modular design where functionality is delivered as a component. Dapr components can be shared across multiple container apps. The Dapr app identifiers provided in the scopes array dictate which dapr-enabled container apps load a given component at runtime.
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

### Dapr Enablement

You can configure Dapr using various arguments and annotations based on the runtime context. Azure Container Apps provides three channels through which you can configure Dapr:

- Container Apps CLI
- Infrastructure as Code (IaC) templates, as in Bicep or Azure Resource Manager (ARM) templates
- The Azure portal

### Dapr Components and Scopes

Dapr uses a modular design where functionality is delivered as a component. The use of Dapr components is optional and dictated exclusively by the needs of your application.

Dapr components in container apps are environment-level resources that:

- Can provide a pluggable abstraction model for connecting to supporting external services.
- Can be shared across container apps or scoped to specific container apps.
- Can use Dapr secrets to securely retrieve configuration metadata.

By default, all Dapr-enabled container apps within the same environment load the full set of deployed components. To ensure components are loaded at runtime by only the appropriate container apps, application scopes should be used.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
Dapr enables developers to write microservices that can run on the cloud and edge, enhancing the development of scalable, resilient applications. 

Ride-sharing applications, that have been rising in popularity over the last few years, often rely on Dapr or similar services. Dapr simplifies the development of such services by managing ride and driver states, enabling real-time updates, and facilitating an event-driven architecture. This results in efficient matching of riders with drivers and timely updates, improving overall service efficiency.

Now it's your turn to practice deploying a container app in Azure! Make sure to complete the practice exercise if you have an active Azure subscription (or a free trial).
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Deploying a Container App
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

In this exercise you create a secure Container Apps environment and deploy container app. Follow the instructions below closely!

### Step 1. Preparing an Environment

1. Sign in to the Azure portal and open the Cloud Shell.

<edukamu-image url="/graphics/module2/cloud-shell-menu.png" alt="The location of Cloud Shell launch button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
After the shell opens be sure to select the Bash environment.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module2/shell-bash-selection.png" alt="Selecting the Bash environment." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Install the Azure Container Apps extension for the CLI.
</li>
</ol>
</edukamu-section>

Bash

```Bash
az extension add --name containerapp --upgrade
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Register the <code>Microsoft.App</code> namespace.
</li>
</ol>
</edukamu-section>

**Note**: Azure Container Apps resources have migrated from the Microsoft.Web namespace to the Microsoft.App namespace. Keep this in mind if you've used these services before.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Register the <code>Microsoft.OperationalInsights</code> provider for the Azure Monitor Log Analytics workspace if you haven't used it before.
</li>
</ol>
</edukamu-section>

Bash

```Bash
az provider register --namespace Microsoft.OperationalInsights
```

**Note**: Registering the Microsoft.App namespace and Microsoft.OperationalInsights can each take a few minutes to complete, so wait patiently.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Set environment variables used later in this exercise. Replace <code>< location ></code> with a region near you.
</li>
</ol>
</edukamu-section>

Bash
```Bash
myRG=az204-appcont-rg
myLocation=<location>
myAppContEnv=az204-env-$RANDOM
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 7;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Create the resource group for your container app.
</li>
</ol>
</edukamu-section>

Bash

```Bash
az group create \
    --name $myRG \
    --location $myLocation
```

With the CLI upgraded and a new resource group available, you can create a Container Apps environment and deploy your container app.


### Step 2. Creating an Environment

An environment in Azure Container Apps creates a secure boundary around a group of container apps. Container Apps deployed to the same environment are deployed in the same virtual network and write logs to the same Log Analytics workspace.

Create an environment by using the `az containerapp env create` command.

Bash

```Bash
az containerapp env create \
    --name $myAppContEnv \
    --resource-group $myRG \
    --location $myLocation
```

### Step 3. Creating a Container App

After the container app environment finishes deployment, you can deploy a container image to Azure Container Apps.

Deploy a sample app container image by using the `containerapp create` command.

Bash

```Bash
az containerapp create \
    --name my-container-app \
    --resource-group $myRG \
    --environment $myAppContEnv \
    --image mcr.microsoft.com/azuredocs/containerapps-helloworld:latest \
    --target-port 80 \
    --ingress 'external' \
    --query properties.configuration.ingress.fqdn
```


### Step 4. Verifying Deployment

Select the link returned by the `az containerapp create` command to verify the container app is running.

<edukamu-image url="/graphics/module2/azure-container-apps-exercise.png" alt="Screenshot showing the sample app running in a browser." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

### Step 5. Clean Up Resources (Optional)

When no longer needed, you can use the `az group delete` command to remove the resource group, the container app, and other resources stored there.

Bash

```Bash
az group delete --name $myRG
```

Cleaning resources is a recommended action every now and then.

</edukamu-collapse>
<br>


We've now covered every topic of the second unit! As such, it's the perfect time for an exercise.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Implementing Container Apps
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/implementing-container-apps-question-scroll-1.yaml" id="os9rzfbg0jhvglzf">
<br>

</edukamu-collapse>
<br>

Remember to take small pauses every now and then. You should only move forward once you feel rested and confident in your new knowledge.

Whenever you're ready, feel free to jump into the third unit!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3-4-5.png" alt="Edukamu-progress-in-a-module-image">
