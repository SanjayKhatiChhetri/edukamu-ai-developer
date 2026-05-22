---
title: "Course 6: Azure Development"
layout: default
nav_order: 8
parent: Courses
---

# Course 6: Azure Development

**URL:** [https://cs.edukamu.fi/azure-development](https://cs.edukamu.fi/azure-development)  
**Sections:** 14  

---

## Table of Contents

- **Unit 1:** Configuring Web Apps | Discovering Azure Functions | Getting Started With Azure App Service ...
- **Unit 2:** Comparing Container Services | Containerized Solutions | Ensuring Data Availability ...
- **Unit 3:** Advanced Capabilities | Enhancing Security | Exploring Api Management ...

---

## Unit 1

### Configuring Web Apps

**TL;DR:** When it comes to developing web apps, configurations should be made a top priority. In order to make your applications function well and securely in accordance with specific business requirements, this important process should not be overlooked.

**Topics covered:**
- Configuring Application Settings
- Adding and Editing Settings
- Connection Strings
- Configuring General Settings
- Step-by-Step Guide for Activating a Free Azure Trial
- Configuring Path Mappings
- Diagnostic Logging
- Security Certifications
- Exercise: Configuring Web Apps
- Practice: Deploying an ASP.NET Web App with Azure App Service

**Key Terms:**

| Term | Definition |
|------|-----------|
| Edit | button on the right side. |
| Save | back in the **Configuration** page. |
| Tip | There is one case in which you may want to use connection strings instead of app settings for non-.NET languages: certain Azure database types are backed up along with the app... |
| Configuration > General | settings section you can configure some common settings for your app. Some settings require you to scale up to higher pricing tiers. |
| Stack settings | The software stack to run the app, including the language and SDK versions. For Linux apps and custom container apps, you can also set an optional start-up command or file. |
| Bitness | 32-bit or 64-bit. |
| WebSocket protocol | For ASP.NET SignalR or socket.io, for example. |
| Always On | Keep the app loaded even when there's no traffic. By default, **Always On** isn't enabled and the app is unloaded after 20 minutes without any incoming requests. It's required for... |
| Managed pipeline version | The IIS pipeline mode. Set it to **Classic** if you have a legacy app that requires an older version of IIS. |
| HTTP version | Set to 2.0 to enable support for HTTPS/2 protocol. |

**Key Points:**
- Stack settings: The software stack to run the app, including the language and SDK versions. For Linux apps and custom container apps, you can also set an optional start-up command or file.
- Platform settings: Lets you configure settings for the hosting platform, including:
- A new resource group to contain all of the Azure resources for the service.
- A new App Service plan that specifies the location, size, and features of the web server farm that hosts your app.
- A new App Service app instance to run the deployed application.
- Under Resource group, select Create new. Type *myResourceGroup* for the name.
- Under Name, type a globally unique name for your web app.
- Under Publish, select *Code*.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Discovering Azure Functions

**TL;DR:** Imagine you were developing an online retail platform that requires real-time inventory updates and order processing. Here, Azure Functions could be used to handle new order notifications, automatically updating inventory levels and sending confirmation emails to customers.

**Topics covered:**
- Getting Started with Azure Functions
- Managing Hosting
- Scaling Azure Functions
- Scaling Behaviors
- Understanding Azure Functions
- Function Apps
- Local Development
- Functions in Practice: Triggers and Binding
- Defining Triggers and Bindings
- Binding Direction

**Key Terms:**

| Term | Definition |
|------|-----------|
| Functions | is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaining servers, the... |
| Azure Functions | </edukamu-table-header> |
| Logic Apps | </edukamu-table-header> |
| Development | </edukamu-table-cell> |
| Connectivity | </edukamu-table-cell> |
| Actions | </edukamu-table-cell> |
| Monitoring | </edukamu-table-cell> |
| Management | </edukamu-table-cell> |
| Execution context | </edukamu-table-cell> |
| Plan | </edukamu-table-header> |

**Key Points:**
- How your function app is scaled.
- The resources available to each function app instance.
- Support for advanced functionality, such as Azure Virtual Network connectivity.
- Maximum instances: A single function app only scales out to a maximum of 200 instances. A single instance may process more than one message or request at a time though, so there isn't a set limit on...
- New instance rate: For HTTP triggers, new instances are allocated, at most, once per second. For non-HTTP triggers, new instances are allocated, at most, once every 30 seconds.
- For triggers, the direction is always `in`
- Input and output bindings use `in` and `out`
- Some bindings support a special direction `inout`. If you use `inout`, only the Advanced editor is available via the Integrate tab in the portal.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Getting Started With Azure App Service

**TL;DR:** Web apps are constantly becoming more and more popular across all imaginable fields. From online shopping to social media, from healthcare to agriculture, web apps are providing us with the means to access what we need, when we need it. And Azure App Service empowers us to create such solutions.

**Topics covered:**
- When to Use Azure App Service?
- Introduction to Azure App Service
- Azure App Service Features
- App Service Limitations
- Deploying to App Service
- Automated Deployment
- Manual Deployment
- Deployment Slots
- Example: Deployment Slots in Action
- Authorization and Authentication in Azure App Service

**Key Terms:**

| Term | Definition |
|------|-----------|
| Rapid Development | You need to develop and deploy applications quickly. |
| Scalability | You require automatic scaling to handle fluctuating traffic. |
| Multi-language Support | Your project involves using various programming languages. |
| Serverless Architecture | You want to focus on app development without managing infrastructure. |
| Integration Requirements | You need to integrate with other Azure services or external applications. |
| Continuous Deployment | You're implementing a CI/CD pipeline for regular updates and testing. |
| Azure DevOps Services | You can push your code to Azure DevOps Services, build your code in the cloud, run the tests, generate a release from the code, and finally, push your code to an Azure Web App. |
| GitHub | Azure supports automated deployment directly from GitHub. When you connect your GitHub repository to Azure for automated deployment, any changes you push to your production branch... |
| Bitbucket | With its similarities to GitHub, you can configure an automated deployment with Bitbucket. |
| Git | App Service web apps feature a Git URL that you can add as a remote repository. Pushing to the remote repository deploys your app. |

**Key Points:**
- The Azure portal shows only features that currently work for Linux apps. As features are enabled, they're activated on the portal.
- When deployed to built-in images, your code and content are allocated a storage volume for web content, backed by Azure Storage. The disk latency of this volume is higher and more variable than the...
- Azure DevOps Services: You can push your code to Azure DevOps Services, build your code in the cloud, run the tests, generate a release from the code, and finally, push your code to an Azure Web App.
- GitHub: Azure supports automated deployment directly from GitHub. When you connect your GitHub repository to Azure for automated deployment, any changes you push to your production branch on GitHub...
- Bitbucket: With its similarities to GitHub, you can configure an automated deployment with Bitbucket.
- Git: App Service web apps feature a Git URL that you can add as a remote repository. Pushing to the remote repository deploys your app.
- CLI: `webapp up` is a feature of the `az` command-line interface that packages your app and deploys it. Unlike other deployment methods, `az webapp up` can create a new App Service web app for you if...
- Zip deploy: Use `curl` or a similar HTTP utility to send a ZIP of your application files to App Service.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Introduction To Azure Ai Development

**TL;DR:** <edukamu-video content="/videos/devai-6-unit1-video.yaml"/>
<br>

**Topics covered:**
- Business Perspective: Why is the Cloud so Important?
- C# Crash Course
- What is a Programming Language?
- What is a Compilation?
- What is a Syntax?
- How did Your Code Work?
- Challenge: Problem Solving and Code
- Challenge: Example Solution
- Terminology
- Terminology

**Key Terms:**

| Term | Definition |
|------|-----------|
| compiler | converts your source code into a different format that the computer's central processing unit (CPU) can execute. When you used the green **Run** button in the previous unit, the... |
| statement | is a complete instruction in C#. The semicolon tells the compiler that you've finished entering the command. |
| Tip | Create a cheat sheet for yourself until you've memorized certain key commands. |
| Web Apps | Web applications are software applications that run on a web server and are accessed through a web browser. They offer interactive user experiences and can handle various tasks,... |
| Mobile Back Ends | This refers to the server-side infrastructure for mobile apps. It handles the app's data processing, storage, security, and integrates business logic. Mobile back ends are... |
| RESTful APIs | Representational State Transfer (REST) APIs are a set of rules and standards used to build web services. They allow different software applications to communicate over the... |
| HTTP Requests | An Azure Function can be triggered by an HTTP request, such as a user submitting a form on a website. This could initiate a function to process the form data, verify it, and store... |
| Database Changes | A function can be set to trigger on changes in a database, like a new entry being added. This can be used for real-time data processing, like sending a confirmation email to a... |
| Message Queue Triggers | Azure Functions can respond to messages added to Azure queues (a service for storing large numbers of messages). For instance, a function could be triggered when a message is... |
| Web Apps | Web applications are software applications that run on a web server and are accessed through a web browser. They offer interactive user experiences and can handle various tasks,... |

**Key Points:**
- Business applications to capture, analyze, and process data
- Dynamic web applications that can be accessed from a web browser
- Financial and scientific applications
- Write your first lines of C# code.
- Use two different techniques to print a message as output.
- Diagnose errors when code is incorrect.
- Identify different C# syntax elements like operators, classes, and methods.
- Use ```Console.WriteLine("Your message here");```

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 2

### Comparing Container Services

**TL;DR:** Containerized applications are an ideal solution when you need a highly scalable, consistent, and efficient way to deploy and manage applications across different environments or when application portability and compatibility across various platforms and infrastructure are priorities.

**Topics covered:**
- From Development to Deployment
- Introduction to Azure Container Instances
- Container Groups
- Deployment
- Resource Allocation
- Networking
- Storage
- Common Scenarios
- Introduction to Azure Container Apps
- Azure Container Apps Environments

**Key Terms:**

| Term | Definition |
|------|-----------|
| Development of the Application | The first step is developing the application. This involves writing code in the preferred programming language and creating a suitable environment for the application to run. |
| Fast startup | ACI can start containers in Azure in seconds, without the need to provision and manage VMs |
| Container access | ACI enables exposing your container groups directly to the internet with an IP address and a fully qualified domain name (FQDN) |
| Hypervisor-level security | Isolate your application as completely as it would be in a VM |
| Customer data | The ACI service stores the minimum customer data required to ensure your container groups are running as expected |
| Custom sizes | ACI provides optimum utilization by allowing exact specifications of CPU cores and memory |
| Persistent storage | Mount Azure Files shares directly to a container to retrieve and persist state |
| Linux and Windows | Schedule both Windows and Linux containers using the same API. |
| Note | Multi-container groups currently support only Linux containers. For Windows containers, Azure Container Instances only supports deployment of a single instance. |
| Simplicity and Speed | ACI is ideal for situations in which you want to quickly run a container without orchestration, making it perfect for simple applications or tasks. |

**Key Points:**
- The first step is developing the application. This involves writing code in the preferred programming language and creating a suitable environment for the application to run.
- Creating a Container Image: The application and its dependencies are packaged into a container image. This is done using a tool like Docker. A Dockerfile is created which includes instructions on how...
- Building the Image: The Dockerfile is used to build the container image. The image contains the application code, runtime, libraries, and any other necessary components.
- Once the container image is created, it is stored in a container registry. A container registry is a repository for storing container images. Azure Container Registry (ACR) is an example of a...
- The container image can be deployed to a container orchestration platform. This platform manages the lifecycle of containers, ensuring they are running and scaling as needed.
- Once deployed, the containerized applications are monitored and maintained. This involves ensuring they are running efficiently, updating them as needed, and scaling them based on demand.
- Fast startup: ACI can start containers in Azure in seconds, without the need to provision and manage VMs
- Container access: ACI enables exposing your container groups directly to the internet with an IP address and a fully qualified domain name (FQDN)

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Containerized Solutions

**TL;DR:** Containerized applications represent a modern approach to software development and deployment, in which applications are packaged along with their dependencies into containers. This method offers several benefits, such as consistency, scalability, and isolation, which are crucial in today's fast-paced and dynamic IT environments.

**Topics covered:**
- Advantages of Containerized Solutions
- Are Containers Still Needed?
- Recap on the Container and ACR Terminology
- Introduction to Azure Container Registry
- Use Cases
- Supported Images and Artifacts
- ACR Storage Capabilities
- Building and Managing Containers
- Task Scenarios
- Quick Tasks

**Key Terms:**

| Term | Definition |
|------|-----------|
| Consistency Across Environments | Containers encapsulate an application and its dependencies, ensuring that it works uniformly across different computing environments, from a developer's local machine to the... |
| Rapid Deployment and Scaling | Containers can be started, stopped, and replicated quickly and easily, which is ideal for scaling applications in response to fluctuating demand. |
| Isolation | Each container operates in isolation, preventing one application's issues or changes from affecting others. This isolation simplifies dependency management and enhances security. |
| Resource Efficiency | Containers share the host system's kernel, so they are more lightweight than virtual machines. This means you can run more applications on the same hardware, improving resource... |
| Microservices Architecture | Containerization supports a microservices architecture, where applications are broken into smaller, independent pieces. This can improve application scalability and facilitate... |
| Portability | Since containers are not tied to an underlying infrastructure, they can run across different cloud and OS platforms. |
| DevOps and CI/CD | Containers integrate well with DevOps practices, enabling consistent, reliable, and frequent deployment of applications. |
| Easier Management | Container orchestration tools like Kubernetes automate the deployment, scaling, networking, and management of containers, simplifying operational tasks. |
| Container Image | A container image is a lightweight, standalone, executable software package that includes everything needed to run a piece of software, including the code, a runtime, libraries,... |
| Managed Service | ACR is a managed service, meaning that Azure handles the infrastructure, scalability, and maintenance of the registry. Users don't need to worry about the underlying servers or... |

**Key Points:**
- Container Image: A container image is a lightweight, standalone, executable software package that includes everything needed to run a piece of software, including the code, a runtime, libraries,...
- Managed Service: ACR is a managed service, meaning that Azure handles the infrastructure, scalability, and maintenance of the registry. Users don't need to worry about the underlying servers or...
- Private Docker Registry: Unlike public registries like Docker Hub, ACR is private, which means it's intended for storing and managing images that are not meant for public distribution. This aspect is...
- Docker: Docker is a platform and tool for building, distributing, and running Docker containers. It has become synonymous with container technology because it was one of the first and most popular...
- Scalable orchestration systems that manage containerized applications across clusters of hosts, including Kubernetes, DC/OS, and Docker Swarm.
- Azure services that support building and running applications at scale, including Azure Kubernetes Service (AKS), App Service, Batch, Service Fabric, and others.
- Encryption-at-rest: All container images in your registry are encrypted at rest. Azure automatically encrypts an image before storing it, and decrypts it on-the-fly when you or your applications and...
- Regional storage: Azure Container Registry stores data in the region where the registry is created, to help customers meet data residency and compliance requirements. In all regions except Brazil...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Ensuring Data Availability

**TL;DR:** Have you ever wondered why database solutions are so important? As you know, data is the foundation of all modern applications, but what is the most important duty of a database? It's naturally difficult to determine just one, but ensuring data availability would be a great pick.

**Topics covered:**
- Introduction to Blob Storage Lifecycles
- Access Tiers
- Managing the Data Lifecycle
- Discovering Lifecycle Policies
- Rules
- Rule Filters
- Rule Actions
- Implementing Lifecycle Policies
- Azure Portal
- 1. Azure Portal List View

**Key Terms:**

| Term | Definition |
|------|-----------|
| Hot | Optimized for storing data that is accessed frequently. |
| Cool | Optimized for storing data that is infrequently accessed and stored for a minimum of 30 days. |
| Cold tier | Optimized for storing data that is infrequently accessed and stored for a minimum of 90 days. The cold tier has lower storage costs and higher access costs compared to the cool... |
| Archive | Optimized for storing data that is rarely accessed and stored for at least 180 days with flexible latency requirements, on the order of hours. |
| Note | Data stored in a premium block blob storage account cannot be tiered to Hot, Cool, or Archive using Set Blob Tier or using Azure Blob Storage lifecycle management. To move data,... |
| Cost Management | Storing all data in the highest performance (and cost) tier can be prohibitively expensive, especially as data volumes grow. |
| Performance Optimization | Ensuring frequently accessed data is readily available, while archiving or deleting stale data, optimizes performance. |
| Regulatory Compliance | Certain industries have specific requirements for data retention and deletion, making lifecycle management essential for compliance. |
| Parameter name | </edukamu-table-header> |
| Parameter type | </edukamu-table-header> |

**Key Points:**
- Hot - Optimized for storing data that is accessed frequently.
- Cool - Optimized for storing data that is infrequently accessed and stored for a minimum of 30 days.
- Cold tier - Optimized for storing data that is infrequently accessed and stored for a minimum of 90 days. The cold tier has lower storage costs and higher access costs compared to the cool tier.
- Archive - Optimized for storing data that is rarely accessed and stored for at least 180 days with flexible latency requirements, on the order of hours.
- The access tier can be set on a blob during or after upload.
- Only the hot and cool access tiers can be set at the account level. The archive access tier can only be set at the blob level.
- Data in the cool access tier has slightly lower availability, but still has high durability, retrieval latency, and throughput characteristics similar to hot data.
- Data in the archive access tier is stored offline. The archive tier offers the lowest storage costs but also the highest access costs and latency.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Handling Unstructured Data

**TL;DR:** <edukamu-video content="/videos/devai-6-unit2-video.yaml"/>
<br>

**Topics covered:**
- The Big Picture: Cloud, Data, and Azure Solutions
- Cloud, Data, and Azure
- Real-World Data in Azure
- Introduction to Azure Blob Storage
- Performance Tiers
- Azure Blob Storage or Azure Cosmos DB?
- 1. Data Type and Structure
- 2. Performance and Scalability
- 3. Data Access and Transaction Support
- 4. Pricing Model

**Key Terms:**

| Term | Definition |
|------|-----------|
| Azure Blob Storage | (the first major topic of this unit) shines, offering a highly scalable, secure, and cost-effective platform for storing large volumes of unstructured data. Blob Storage allows... |
| containerized solutions | an approach in which applications are packaged with all their dependencies into containers. |
| Azure Container Instances | and **Azure Container Apps** are prime examples, providing a serverless platform for running containers, thus reducing the need for infrastructure management. This allows... |
| Standard | This is the standard general-purpose v2 account and is recommended for most scenarios using Azure Storage. |
| Premium | Premium accounts offer higher performance by using solid-state drives. If you create a premium account you can choose between three account types, block blobs, page blobs, or file... |
| Storage account type | </edukamu-table-header> |
| Performance tier | </edukamu-table-header> |
| Usage | </edukamu-table-header> |
| Hot | access tier, which is optimized for frequent access of objects in the storage account. The Hot tier has the highest storage costs, but the lowest access costs. New storage... |
| Cool | access tier, which is optimized for storing large amounts of data that is infrequently accessed and stored for at least 30 days. The Cool tier has lower storage costs and higher... |

**Key Points:**
- Serving images or documents directly to a browser.
- Storing files for distributed access.
- Storing data for backup and restore, disaster recovery, and archiving.
- Storing data for analysis by an on-premises or Azure-hosted service.
- Standard: This is the standard general-purpose v2 account and is recommended for most scenarios using Azure Storage.
- Premium: Premium accounts offer higher performance by using solid-state drives. If you create a premium account you can choose between three account types, block blobs, page blobs, or file shares.
- The Hot access tier, which is optimized for frequent access of objects in the storage account. The Hot tier has the highest storage costs, but the lowest access costs. New storage accounts are...
- The Cool access tier, which is optimized for storing large amounts of data that is infrequently accessed and stored for at least 30 days. The Cool tier has lower storage costs and higher access costs...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Implementing Container Apps

**TL;DR:** After exploring a few Azure services on offer for building and managing containerized solutions, it's time to take a while to learn about their implementation.

**Topics covered:**
- Understanding Containers
- Configuration
- Multiple Containers
- Container Registries
- Limitations
- Implementing Authentication and Authorization
- Identity Providers
- Provider
- Feature Architecture
- Authentication Flow

**Key Terms:**

| Term | Definition |
|------|-----------|
| Note | Running multiple containers in a single container app is an advanced use case. In most situations where you want to run multiple containers, such as when implementing a... |
| Privileged containers | Azure Container Apps can't run privileged containers. If your program attempts to run a process that requires root access, the application inside the container experiences a... |
| Operating system | Linux-based (`linux/amd64`) container images are required. |
| Without provider SDK | (server-directed flow or server flow): The application delegates federated sign-in to Container Apps. Delegation is typically the case with browser apps, which presents the... |
| With provider SDK | (client-directed flow or client flow): The application signs users in to the provider manually and then submits the authentication token to Container Apps for validation. This... |
| Dapr API | </edukamu-table-header> |
| Description | </edukamu-table-header> |
| Label | </edukamu-table-header> |
| Dapr settings | </edukamu-table-header> |
| Description | </edukamu-table-header> |

**Key Points:**
- An agent that reads logs from the primary app container on a shared volume and forwards them to a logging service.
- A background process that refreshes a cache used by the primary app container in a shared volume.
- Privileged containers: Azure Container Apps can't run privileged containers. If your program attempts to run a process that requires root access, the application inside the container experiences a...
- Operating system: Linux-based (`linux/amd64`) container images are required.
- Azure Container Apps provides access to various built-in authentication providers.
- The built-in auth features don’t require any particular language, SDK, security expertise, or even any code that you have to write.
- To restrict app access only to authenticated users, set its *Restrict access* setting to Require authentication.
- To authenticate but not restrict access, set its *Restrict access* setting to Allow unauthenticated access.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 3

### Advanced Capabilities

**TL;DR:** On this course, we've explained some of the most widely adapted capabilities Microsoft Azure offers for developers. While our goal has been building a strong foundational understanding of the overall process, many neat features are simply beyond the scope of this course, as they require advanced knowledge and experience working with Azure.

**Topics covered:**
- 1. Event-Based Solutions
- Key Aspects of Event-Based Solutions
- Difference from Message-Based Solutions
- Event-Based Solutions in Azure
- Introduction to Azure Event Grid
- Events
- Event Sources
- Topics
- Event Subscriptions
- Event Handlers

**Key Terms:**

| Term | Definition |
|------|-----------|
| Asynchronous Processing | Event-based systems allow for asynchronous processing, which means that the system generating the event does not wait for a response from the receiver. This decoupling of... |
| Event Publishers and Subscribers | In an event-driven architecture, there are publishers (or producers) that generate events, and subscribers (or consumers) that listen and react to these events. |
| Loose Coupling | Event-based architectures promote loose coupling between services. The producer of the event does not need to know about the consumers, making the system more modular and easier... |
| Scalability and Resilience | These systems can handle high volumes of events and are resilient to failures, as the event processing is often distributed among multiple consumers. |
| Azure Event Grid | An event-routing service which helps build applications with event-based architectures. It supports system events from Azure services and custom events. |
| Azure Event Hubs | A big data streaming platform and event ingestion service, capable of receiving and processing millions of events per second. |
| Event sources | Where the event took place? |
| Topics | The endpoint where publishers send events. |
| Event subscriptions | The endpoint or built-in mechanism to route events, sometimes to more than one handler. Subscriptions are also used by handlers to intelligently filter incoming events. |
| Event handlers | The app or service reacting to the event. |

**Key Points:**
- Event sources - Where the event took place?
- Topics - The endpoint where publishers send events.
- Event subscriptions - The endpoint or built-in mechanism to route events, sometimes to more than one handler. Subscriptions are also used by handlers to intelligently filter incoming events.
- Event handlers - The app or service reacting to the event.
- Trigger: Each time a product is sold on Omise's platform, an event is generated.
- Process: This event is sent to Azure Event Grid, which then routes the event to various subscribers.
- Subscribers: One subscriber could be the inventory management system, which updates the inventory count in real-time.
- Trigger: When the inventory level for a product falls below a certain threshold, the inventory management system generates a 'Low Stock' event.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Enhancing Security

**TL;DR:** <edukamu-video content="/videos/devai-6-unit3-video.yaml"/>
<br>

**Topics covered:**
- Real-World View: Non-functional Requirements May Seem Boring, but They are Still Critical.
- Introduction to Azure Key Vault
- Key Benefits of Azure Key Vault
- Introduction to Azure App Configuration
- Using App Configuration
- Introduction to Managed Identities
- When to Use Managed Identities?
- Azure Key Vault Best Practices
- Authentication
- Encryption of Data in Transit

**Key Terms:**

| Term | Definition |
|------|-----------|
| Secrets Management | Azure Key Vault can be used to Securely store and tightly control access to tokens, passwords, certificates, API keys, and other secrets. |
| Key Management | Azure Key Vault can also be used as a Key Management solution. Azure Key Vault makes it easy to create and control the encryption keys used to encrypt your data. |
| Certificate Management | Azure Key Vault is also a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for... |
| Centralized application secrets | Centralizing storage of application secrets in Azure Key Vault allows you to control their distribution. For example, instead of storing the connection string in the app's code... |
| Securely store secrets and keys | Access to a key vault requires proper authentication and authorization before a caller (user or application) can get access. Authentication is done via Microsoft Entra ID.... |
| Monitor access and use | You can monitor activity by enabling logging for your vaults. You have control over your logs and you may secure them by restricting access and you may also delete logs that you... |
| Simplified administration of application secrets | Security information must be secured, it must follow a life cycle, and it must be highly available. Azure Key Vault simplifies the process of meeting these requirements by: |
| Supported programming languages and framework: | .NET Core and ASP.NET Core |
| system-assigned managed identity | is enabled directly on an Azure service instance. When the identity is enabled, Azure creates an identity for the instance in the Microsoft Entra tenant that's trusted by the... |
| user-assigned managed identity | is created as a standalone Azure resource. Through a create process, Azure creates an identity in the Microsoft Entra tenant that's trusted by the subscription in use. After the... |

**Key Points:**
- Security: The system must be safe from external misuse and/or attacks
- Performance: The system must be fast enough to fill its purpose, whether that’s for a background batch system or for an interactive user interface
- Usability: The system must be easy enough to use
- Resilience and reliability: The system must be able to automatically recover from normal errors (e.g., invalid input) and be easily-enough recoverable from catastrophic failures (e.g., erroneous...
- Observability: There must be a way to know what the system is doing, which errors occur and how the system is performing
- Cost-effectiveness: The system should run at the minimal reasonable cost without impacting performance or reliability
- Configurability: The most frequently changed configuration settings must be settable in a way that is least disturbing to the continuous operation of the system
- Integrability: It must be possible to incorporate data into the system as well as out of it

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Exploring Api Management

**TL;DR:** After spending some time with the security features of Azure, it's time to revisit an old topic we've come across multiple times during this program - application programming interfaces, or APIs for short.

**Topics covered:**
- Introduction to Azure API Management
- API Management Components
- Products
- Groups
- Developers
- Policies
- API Gateways
- Managed or Self-hosted
- Understanding API Management Policies
- Policy Configuration

**Key Terms:**

| Term | Definition |
|------|-----------|
| API gateway | is the endpoint that: |
| management plane | is the administrative interface where you set up your API program. Use it to: |
| Developer portal | is an automatically generated, fully customizable website with the documentation of your APIs. Using the developer portal, developers can: |
| Administrators | Manage API Management service instances and create the APIs, operations, and products that are used by developers. Azure subscription administrators are members of this group. |
| Developers | Authenticated developer portal users that build applications using your APIs. Developers are granted access to the developer portal and build applications that call the operations... |
| Guests | Unauthenticated developer portal users. They can be granted certain read-only access, like the ability to view APIs but not call them. |
| Managed | The managed gateway is the default gateway component that is deployed in Azure for every API Management instance in every service tier. With the managed gateway, all API traffic... |
| Self-hosted | The self-hosted gateway is an optional, containerized version of the default managed gateway. It's useful for hybrid and multicloud scenarios where there's a requirement to run... |
| Note | API Management also supports other mechanisms for securing access to APIs, including: OAuth2.0, Client certificates, and IP allow listing. |
| Scope | </edukamu-table-header> |

**Key Points:**
- The API gateway is the endpoint that:
- The management plane is the administrative interface where you set up your API program. Use it to:
- The Developer portal is an automatically generated, fully customizable website with the documentation of your APIs. Using the developer portal, developers can:
- Administrators - Manage API Management service instances and create the APIs, operations, and products that are used by developers. Azure subscription administrators are members of this group.
- Developers - Authenticated developer portal users that build applications using your APIs. Developers are granted access to the developer portal and build applications that call the operations of an...
- Guests - Unauthenticated developer portal users. They can be granted certain read-only access, like the ability to view APIs but not call them.
- It can result in complex client code. The client must keep track of multiple endpoints, and handle failures in a resilient way.
- It creates coupling between the client and the backend. The client needs to know how the individual services are decomposed. That makes it harder to maintain the client and also harder to refactor...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Securing App Configurations

**TL;DR:** After a brief overview of Azure App Configuration on the previous page, it's time to get to know the service a bit better.

**Topics covered:**
- Paired Keys and Values
- Keys
- Designing Key Namespaces
- Version Key Values
- Query Key Values
- Values
- Managing Application Features with App Configuration
- Basic Concepts
- Feature Flag Usage in Code
- Feature Flag Declaration

**Key Terms:**

| Term | Definition |
|------|-----------|
| Feature flag | A feature flag is a variable with a binary state of on or off. The feature flag also has an associated code block. The state of the feature flag triggers whether the code block... |
| Feature manager | A feature manager is an application package that handles the lifecycle of all the feature flags in an application. The feature manager typically provides extra functionality, such... |
| Filter | A filter is a rule for evaluating the state of a feature flag. A user group, a device or browser type, a geographic location, and a time window are all examples of what a filter... |
| system-assigned identity | is tied to your configuration store. It's deleted if your configuration store is deleted. A configuration store can only have one system-assigned identity. |
| user-assigned identity | is a standalone Azure resource that can be assigned to your configuration store. A configuration store can have multiple user-assigned identities. |

**Key Points:**
- Easier to read. Instead of one long sequence of characters, delimiters in a hierarchical key name function as spaces in a sentence.
- Easier to manage. A key name hierarchy represents logical groups of configuration data.
- Easier to use. It's simpler to write a query that pattern-matches keys in a hierarchical structure and retrieves only a portion of configuration data.
- Feature flag: A feature flag is a variable with a binary state of on or off. The feature flag also has an associated code block. The state of the feature flag triggers whether the code block runs or...
- Feature manager: A feature manager is an application package that handles the lifecycle of all the feature flags in an application. The feature manager typically provides extra functionality, such as...
- Filter: A filter is a rule for evaluating the state of a feature flag. A user group, a device or browser type, a geographic location, and a time window are all examples of what a filter can represent.
- An application that makes use of feature flags.
- A separate repository that stores the feature flags and their current states.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Summary

**TL;DR:** Congratulations on reaching the summary of the Getting Started with Azure Development course! As stated at the beginning, you must complete every assignment in order to pass this course. Therefore please go to Course progress page by pressing the button below (*or the progress icon in the top right corner*), and check that you have indeed completed...

**Topics covered:**
- Unit 1: Foundations of Azure Development
- Unit 2: Implementing Data Solutions
- Unit 3: Advanced Concepts and Best Practices
- Course Feedback

**Key Points:**
- What are so-called web apps? How do they differ from other types of applications?
- What are Azure Functions? Give a few examples.
- What kind of solutions can be developed with Azure App Service?
- What is unstructured data and how can it be handled with Azure?
- How would you describe containerized app solutions?
- In what ways can Azure developers ensure data availability?
- What are the main functions of Azure App Configuration?
- Why is API management important when developing solutions?

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Quick-Reference Glossary

| Term | Definition | Section |
|------|-----------|---------|
| Edit | button on the right side. | Configuring Web Apps |
| Save | back in the **Configuration** page. | Configuring Web Apps |
| Tip | There is one case in which you may want to use connection strings instead of app settings for non-.NET languages: certain Azure database types are backed up along with the app... | Configuring Web Apps |
| Configuration > General | settings section you can configure some common settings for your app. Some settings require you to scale up to higher pricing tiers. | Configuring Web Apps |
| Stack settings | The software stack to run the app, including the language and SDK versions. For Linux apps and custom container apps, you can also set an optional start-up command or file. | Configuring Web Apps |
| Bitness | 32-bit or 64-bit. | Configuring Web Apps |
| WebSocket protocol | For ASP.NET SignalR or socket.io, for example. | Configuring Web Apps |
| Always On | Keep the app loaded even when there's no traffic. By default, **Always On** isn't enabled and the app is unloaded after 20 minutes without any incoming requests. It's required for... | Configuring Web Apps |
| Managed pipeline version | The IIS pipeline mode. Set it to **Classic** if you have a legacy app that requires an older version of IIS. | Configuring Web Apps |
| HTTP version | Set to 2.0 to enable support for HTTPS/2 protocol. | Configuring Web Apps |
| Functions | is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead of worrying about deploying and maintaining servers, the... | Discovering Azure Functions |
| Azure Functions | </edukamu-table-header> | Discovering Azure Functions |
| Logic Apps | </edukamu-table-header> | Discovering Azure Functions |
| Development | </edukamu-table-cell> | Discovering Azure Functions |
| Connectivity | </edukamu-table-cell> | Discovering Azure Functions |
| Actions | </edukamu-table-cell> | Discovering Azure Functions |
| Monitoring | </edukamu-table-cell> | Discovering Azure Functions |
| Management | </edukamu-table-cell> | Discovering Azure Functions |
| Execution context | </edukamu-table-cell> | Discovering Azure Functions |
| Plan | </edukamu-table-header> | Discovering Azure Functions |
| Rapid Development | You need to develop and deploy applications quickly. | Getting Started With Azure App Service |
| Scalability | You require automatic scaling to handle fluctuating traffic. | Getting Started With Azure App Service |
| Multi-language Support | Your project involves using various programming languages. | Getting Started With Azure App Service |
| Serverless Architecture | You want to focus on app development without managing infrastructure. | Getting Started With Azure App Service |
| Integration Requirements | You need to integrate with other Azure services or external applications. | Getting Started With Azure App Service |
| Continuous Deployment | You're implementing a CI/CD pipeline for regular updates and testing. | Getting Started With Azure App Service |
| Azure DevOps Services | You can push your code to Azure DevOps Services, build your code in the cloud, run the tests, generate a release from the code, and finally, push your code to an Azure Web App. | Getting Started With Azure App Service |
| GitHub | Azure supports automated deployment directly from GitHub. When you connect your GitHub repository to Azure for automated deployment, any changes you push to your production branch... | Getting Started With Azure App Service |
| Bitbucket | With its similarities to GitHub, you can configure an automated deployment with Bitbucket. | Getting Started With Azure App Service |
| Git | App Service web apps feature a Git URL that you can add as a remote repository. Pushing to the remote repository deploys your app. | Getting Started With Azure App Service |
| compiler | converts your source code into a different format that the computer's central processing unit (CPU) can execute. When you used the green **Run** button in the previous unit, the... | Introduction To Azure Ai Development |
| statement | is a complete instruction in C#. The semicolon tells the compiler that you've finished entering the command. | Introduction To Azure Ai Development |
| Web Apps | Web applications are software applications that run on a web server and are accessed through a web browser. They offer interactive user experiences and can handle various tasks,... | Introduction To Azure Ai Development |
| Mobile Back Ends | This refers to the server-side infrastructure for mobile apps. It handles the app's data processing, storage, security, and integrates business logic. Mobile back ends are... | Introduction To Azure Ai Development |
| RESTful APIs | Representational State Transfer (REST) APIs are a set of rules and standards used to build web services. They allow different software applications to communicate over the... | Introduction To Azure Ai Development |
| HTTP Requests | An Azure Function can be triggered by an HTTP request, such as a user submitting a form on a website. This could initiate a function to process the form data, verify it, and store... | Introduction To Azure Ai Development |
| Database Changes | A function can be set to trigger on changes in a database, like a new entry being added. This can be used for real-time data processing, like sending a confirmation email to a... | Introduction To Azure Ai Development |
| Message Queue Triggers | Azure Functions can respond to messages added to Azure queues (a service for storing large numbers of messages). For instance, a function could be triggered when a message is... | Introduction To Azure Ai Development |
| Development of the Application | The first step is developing the application. This involves writing code in the preferred programming language and creating a suitable environment for the application to run. | Comparing Container Services |
| Fast startup | ACI can start containers in Azure in seconds, without the need to provision and manage VMs | Comparing Container Services |
| Container access | ACI enables exposing your container groups directly to the internet with an IP address and a fully qualified domain name (FQDN) | Comparing Container Services |
| Hypervisor-level security | Isolate your application as completely as it would be in a VM | Comparing Container Services |
| Customer data | The ACI service stores the minimum customer data required to ensure your container groups are running as expected | Comparing Container Services |
| Custom sizes | ACI provides optimum utilization by allowing exact specifications of CPU cores and memory | Comparing Container Services |
| Persistent storage | Mount Azure Files shares directly to a container to retrieve and persist state | Comparing Container Services |
| Linux and Windows | Schedule both Windows and Linux containers using the same API. | Comparing Container Services |
| Note | Multi-container groups currently support only Linux containers. For Windows containers, Azure Container Instances only supports deployment of a single instance. | Comparing Container Services |
| Simplicity and Speed | ACI is ideal for situations in which you want to quickly run a container without orchestration, making it perfect for simple applications or tasks. | Comparing Container Services |
| Consistency Across Environments | Containers encapsulate an application and its dependencies, ensuring that it works uniformly across different computing environments, from a developer's local machine to the... | Containerized Solutions |
| Rapid Deployment and Scaling | Containers can be started, stopped, and replicated quickly and easily, which is ideal for scaling applications in response to fluctuating demand. | Containerized Solutions |
| Isolation | Each container operates in isolation, preventing one application's issues or changes from affecting others. This isolation simplifies dependency management and enhances security. | Containerized Solutions |
| Resource Efficiency | Containers share the host system's kernel, so they are more lightweight than virtual machines. This means you can run more applications on the same hardware, improving resource... | Containerized Solutions |
| Microservices Architecture | Containerization supports a microservices architecture, where applications are broken into smaller, independent pieces. This can improve application scalability and facilitate... | Containerized Solutions |
| Portability | Since containers are not tied to an underlying infrastructure, they can run across different cloud and OS platforms. | Containerized Solutions |
| DevOps and CI/CD | Containers integrate well with DevOps practices, enabling consistent, reliable, and frequent deployment of applications. | Containerized Solutions |
| Easier Management | Container orchestration tools like Kubernetes automate the deployment, scaling, networking, and management of containers, simplifying operational tasks. | Containerized Solutions |
| Container Image | A container image is a lightweight, standalone, executable software package that includes everything needed to run a piece of software, including the code, a runtime, libraries,... | Containerized Solutions |
| Managed Service | ACR is a managed service, meaning that Azure handles the infrastructure, scalability, and maintenance of the registry. Users don't need to worry about the underlying servers or... | Containerized Solutions |
| Hot | Optimized for storing data that is accessed frequently. | Ensuring Data Availability |
| Cool | Optimized for storing data that is infrequently accessed and stored for a minimum of 30 days. | Ensuring Data Availability |
| Cold tier | Optimized for storing data that is infrequently accessed and stored for a minimum of 90 days. The cold tier has lower storage costs and higher access costs compared to the cool... | Ensuring Data Availability |
| Archive | Optimized for storing data that is rarely accessed and stored for at least 180 days with flexible latency requirements, on the order of hours. | Ensuring Data Availability |
| Cost Management | Storing all data in the highest performance (and cost) tier can be prohibitively expensive, especially as data volumes grow. | Ensuring Data Availability |
| Performance Optimization | Ensuring frequently accessed data is readily available, while archiving or deleting stale data, optimizes performance. | Ensuring Data Availability |
| Regulatory Compliance | Certain industries have specific requirements for data retention and deletion, making lifecycle management essential for compliance. | Ensuring Data Availability |
| Parameter name | </edukamu-table-header> | Ensuring Data Availability |
| Parameter type | </edukamu-table-header> | Ensuring Data Availability |
| Azure Blob Storage | (the first major topic of this unit) shines, offering a highly scalable, secure, and cost-effective platform for storing large volumes of unstructured data. Blob Storage allows... | Handling Unstructured Data |
| containerized solutions | an approach in which applications are packaged with all their dependencies into containers. | Handling Unstructured Data |
| Azure Container Instances | and **Azure Container Apps** are prime examples, providing a serverless platform for running containers, thus reducing the need for infrastructure management. This allows... | Handling Unstructured Data |
| Standard | This is the standard general-purpose v2 account and is recommended for most scenarios using Azure Storage. | Handling Unstructured Data |
| Premium | Premium accounts offer higher performance by using solid-state drives. If you create a premium account you can choose between three account types, block blobs, page blobs, or file... | Handling Unstructured Data |
| Storage account type | </edukamu-table-header> | Handling Unstructured Data |
| Performance tier | </edukamu-table-header> | Handling Unstructured Data |
| Usage | </edukamu-table-header> | Handling Unstructured Data |
| Privileged containers | Azure Container Apps can't run privileged containers. If your program attempts to run a process that requires root access, the application inside the container experiences a... | Implementing Container Apps |
| Operating system | Linux-based (`linux/amd64`) container images are required. | Implementing Container Apps |
| Without provider SDK | (server-directed flow or server flow): The application delegates federated sign-in to Container Apps. Delegation is typically the case with browser apps, which presents the... | Implementing Container Apps |
| With provider SDK | (client-directed flow or client flow): The application signs users in to the provider manually and then submits the authentication token to Container Apps for validation. This... | Implementing Container Apps |
| Dapr API | </edukamu-table-header> | Implementing Container Apps |
| Description | </edukamu-table-header> | Implementing Container Apps |
| Label | </edukamu-table-header> | Implementing Container Apps |
| Dapr settings | </edukamu-table-header> | Implementing Container Apps |
| Asynchronous Processing | Event-based systems allow for asynchronous processing, which means that the system generating the event does not wait for a response from the receiver. This decoupling of... | Advanced Capabilities |
| Event Publishers and Subscribers | In an event-driven architecture, there are publishers (or producers) that generate events, and subscribers (or consumers) that listen and react to these events. | Advanced Capabilities |
| Loose Coupling | Event-based architectures promote loose coupling between services. The producer of the event does not need to know about the consumers, making the system more modular and easier... | Advanced Capabilities |
| Scalability and Resilience | These systems can handle high volumes of events and are resilient to failures, as the event processing is often distributed among multiple consumers. | Advanced Capabilities |
| Azure Event Grid | An event-routing service which helps build applications with event-based architectures. It supports system events from Azure services and custom events. | Advanced Capabilities |
| Azure Event Hubs | A big data streaming platform and event ingestion service, capable of receiving and processing millions of events per second. | Advanced Capabilities |
| Event sources | Where the event took place? | Advanced Capabilities |
| Topics | The endpoint where publishers send events. | Advanced Capabilities |
| Event subscriptions | The endpoint or built-in mechanism to route events, sometimes to more than one handler. Subscriptions are also used by handlers to intelligently filter incoming events. | Advanced Capabilities |
| Event handlers | The app or service reacting to the event. | Advanced Capabilities |
| Secrets Management | Azure Key Vault can be used to Securely store and tightly control access to tokens, passwords, certificates, API keys, and other secrets. | Enhancing Security |
| Key Management | Azure Key Vault can also be used as a Key Management solution. Azure Key Vault makes it easy to create and control the encryption keys used to encrypt your data. | Enhancing Security |
| Certificate Management | Azure Key Vault is also a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for... | Enhancing Security |
| Centralized application secrets | Centralizing storage of application secrets in Azure Key Vault allows you to control their distribution. For example, instead of storing the connection string in the app's code... | Enhancing Security |
| Securely store secrets and keys | Access to a key vault requires proper authentication and authorization before a caller (user or application) can get access. Authentication is done via Microsoft Entra ID.... | Enhancing Security |
| Monitor access and use | You can monitor activity by enabling logging for your vaults. You have control over your logs and you may secure them by restricting access and you may also delete logs that you... | Enhancing Security |
| Simplified administration of application secrets | Security information must be secured, it must follow a life cycle, and it must be highly available. Azure Key Vault simplifies the process of meeting these requirements by: | Enhancing Security |
| Supported programming languages and framework: | .NET Core and ASP.NET Core | Enhancing Security |
| system-assigned managed identity | is enabled directly on an Azure service instance. When the identity is enabled, Azure creates an identity for the instance in the Microsoft Entra tenant that's trusted by the... | Enhancing Security |
| user-assigned managed identity | is created as a standalone Azure resource. Through a create process, Azure creates an identity in the Microsoft Entra tenant that's trusted by the subscription in use. After the... | Enhancing Security |
| API gateway | is the endpoint that: | Exploring Api Management |
| management plane | is the administrative interface where you set up your API program. Use it to: | Exploring Api Management |
| Developer portal | is an automatically generated, fully customizable website with the documentation of your APIs. Using the developer portal, developers can: | Exploring Api Management |
| Administrators | Manage API Management service instances and create the APIs, operations, and products that are used by developers. Azure subscription administrators are members of this group. | Exploring Api Management |
| Developers | Authenticated developer portal users that build applications using your APIs. Developers are granted access to the developer portal and build applications that call the operations... | Exploring Api Management |
| Guests | Unauthenticated developer portal users. They can be granted certain read-only access, like the ability to view APIs but not call them. | Exploring Api Management |
| Managed | The managed gateway is the default gateway component that is deployed in Azure for every API Management instance in every service tier. With the managed gateway, all API traffic... | Exploring Api Management |
| Self-hosted | The self-hosted gateway is an optional, containerized version of the default managed gateway. It's useful for hybrid and multicloud scenarios where there's a requirement to run... | Exploring Api Management |
| Scope | </edukamu-table-header> | Exploring Api Management |
| Feature flag | A feature flag is a variable with a binary state of on or off. The feature flag also has an associated code block. The state of the feature flag triggers whether the code block... | Securing App Configurations |
| Feature manager | A feature manager is an application package that handles the lifecycle of all the feature flags in an application. The feature manager typically provides extra functionality, such... | Securing App Configurations |
| Filter | A filter is a rule for evaluating the state of a feature flag. A user group, a device or browser type, a geographic location, and a time window are all examples of what a filter... | Securing App Configurations |
| system-assigned identity | is tied to your configuration store. It's deleted if your configuration store is deleted. A configuration store can only have one system-assigned identity. | Securing App Configurations |
| user-assigned identity | is a standalone Azure resource that can be assigned to your configuration store. A configuration store can have multiple user-assigned identities. | Securing App Configurations |

---

*Auto-generated by `generate_diary.py` — re-run to refresh after re-scraping.*
