## Comparing Container Services

Containerized applications are an ideal solution when you need a highly scalable, consistent, and efficient way to deploy and manage applications across different environments or when application portability and compatibility across various platforms and infrastructure are priorities.

By now we've reviewed the nature and capabilities of containerized applications, and now it's time to find out about their implementation. How exactly does that happen? Let's start with an overview, after which we'll compare a few useful services.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### From Development to Deployment
</edukamu-collapse-hidden-title>

Containerized applications are implemented using a process that packages an application and its dependencies into a container. This container can then be run on any compatible system without the need for additional configuration. Here's an overview of how containerized applications are typically implemented:

1. **Development of the Application**:
- The first step is developing the application. This involves writing code in the preferred programming language and creating a suitable environment for the application to run.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Containerization</span>:
</li>
</ol>
</edukamu-section>
- Creating a Container Image: The application and its dependencies are packaged into a container image. This is done using a tool like Docker. A Dockerfile is created which includes instructions on how the image should be built.
- Building the Image: The Dockerfile is used to build the container image. The image contains the application code, runtime, libraries, and any other necessary components.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Registry Storage</span>:
</li>
</ol>
</edukamu-section>
- Once the container image is created, it is stored in a container registry. A container registry is a repository for storing container images. Azure Container Registry (ACR) is an example of a managed, private Docker registry service that stores container images securely.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Deployment</span>:
</li>
</ol>
</edukamu-section>
- The container image can be deployed to a container orchestration platform. This platform manages the lifecycle of containers, ensuring they are running and scaling as needed.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Monitoring and Maintenance</span>:
</li>
</ol>
</edukamu-section>
- Once deployed, the containerized applications are monitored and maintained. This involves ensuring they are running efficiently, updating them as needed, and scaling them based on demand.

In summary, containerized applications are implemented by developing the application, packaging it into a container image, storing this image in a registry like ACR, deploying it using a service like Azure Container Apps, and monitoring it to ensure smooth operations throughout the lifecycle. This process enhances scalability, portability, and consistency across different environments.

</edukamu-collapse>
<br>

Azure Container Apps is a service in Azure that simplifies the deployment and management of containerized applications. It allows you to run containers without managing the underlying infrastructure and provides features such as automatic scaling, networking, and CI/CD integration.

On this page, we'll get acquainted with two Azure tools offered for building containerized solutions: Container Instances, which we'll visit briefly, and Container Apps, with which we'll spend a little more time.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Container Instances
</edukamu-collapse-hidden-title>

Azure Container Instances (ACI) is a great solution for any scenario that can operate in isolated containers, including simple applications, task automation, and build jobs. Here are some of the benefits:

- **Fast startup**: ACI can start containers in Azure in seconds, without the need to provision and manage VMs
- **Container access**: ACI enables exposing your container groups directly to the internet with an IP address and a fully qualified domain name (FQDN)
- **Hypervisor-level security**: Isolate your application as completely as it would be in a VM
- **Customer data**: The ACI service stores the minimum customer data required to ensure your container groups are running as expected
- **Custom sizes**: ACI provides optimum utilization by allowing exact specifications of CPU cores and memory
- **Persistent storage**: Mount Azure Files shares directly to a container to retrieve and persist state
- **Linux and Windows**: Schedule both Windows and Linux containers using the same API.

For scenarios where you need full container orchestration, including service discovery across multiple containers, automatic scaling, and coordinated application upgrades, we recommend Azure Kubernetes Service (AKS).

### Container Groups

The top-level resource in Azure Container Instances is the *container group*. A container group is a collection of containers that get scheduled on the same host machine. The containers in a container group share a lifecycle, resources, local network, and storage volumes. It's similar in concept to a *pod* in Kubernetes.

The following diagram shows an example of a container group that includes multiple containers:

<edukamu-image url="/graphics/module2/container-groups-example.png" alt="Example container group with two containers, one listening on port 80 and the other listening on port 5000." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

This example container group:

- Is scheduled on a single host machine.
- Is assigned a DNS name label.
- Exposes a single public IP address, with one exposed port.
- Consists of two containers. One container listens on port 80, while the other listens on port 5000.
- Includes two Azure file shares as volume mounts, and each container mounts one of the shares locally.

**Note**: Multi-container groups currently support only Linux containers. For Windows containers, Azure Container Instances only supports deployment of a single instance.

### Deployment

There are two common ways to deploy a multi-container group: use a Resource Manager template or a YAML file. A Resource Manager template is recommended when you need to deploy more Azure service resources (for example, an Azure Files share) when you deploy the container instances. Due to the YAML format's more concise nature, a YAML file is recommended when your deployment includes only container instances.

### Resource Allocation

Azure Container Instances allocates resources such as CPUs, memory, and optionally GPUs (preview) to a container group by adding the resource requests of the instances in the group. Using CPU resources as an example, if you create a container group with two instances, each requesting one CPU, then the container group is allocated two CPUs.

### Networking

Container groups share an IP address and a port namespace on that IP address. To enable external clients to reach a container within the group, you must expose the port on the IP address and from the container. Because containers within the group share a port namespace, port mapping isn't supported. Containers within a group can reach each other via localhost on the ports that they exposed, even if those ports aren't exposed externally on the group's IP address.

### Storage

You can specify external volumes to mount within a container group. You can map those volumes into specific paths within the individual containers in a group. Supported volumes include:

- Azure file share
- Secret
- Empty directory
- Cloned git repo

### Common Scenarios

Multi-container groups are useful in cases where you want to divide a single functional task into a few container images. These images might be delivered by different teams and have separate resource requirements.

Example usage could include:

- A container serving a web application and a container pulling the latest content from source control.
- An application container and a logging container. The logging container collects the logs and metrics output by the main application and writes them to long-term storage.
- An application container and a monitoring container. The monitoring container periodically makes a request to the application to ensure that it's running and responding correctly, and raises an alert if it's not.
- A front-end container and a back-end container. The front end might serve a web application, with the back end running a service to retrieve data.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Container Apps
</edukamu-collapse-hidden-title>

Azure Container Apps enables you to run microservices and containerized applications on a serverless platform that runs on top of Azure Kubernetes Service. Common uses of Azure Container Apps include:

- Deploying API endpoints
- Hosting background processing applications
- Handling event-driven processing
- Running microservices

With Azure Container Apps, you can:

- Run multiple container revisions and manage the container app's application lifecycle.
- Autoscale your apps based on any KEDA-supported scale trigger. Most applications can scale to zero. (Applications that scale on CPU or memory load can't scale to zero.)
- Enable HTTPS ingress without having to manage other Azure infrastructure.
- Split traffic across multiple versions of an application for Blue/Green deployments and A/B testing scenarios.
- Use internal ingress and service discovery for secure internal-only endpoints with built-in DNS-based service discovery.
- Build microservices with Dapr and access its rich set of APIs.
- Run containers from any registry, public or private, including Docker Hub and Azure Container Registry (ACR).
- Use the Azure CLI extension, Azure portal or ARM templates to manage your applications.
- Provide an existing virtual network when creating an environment for your container apps.
- Securely manage secrets directly in your application.
- Monitor logs using Azure Log Analytics.

### Azure Container Apps Environments

Individual container apps are deployed to a single Container Apps environment, which acts as a secure boundary around groups of container apps. Container Apps in the same environment are deployed in the same virtual network and write logs to the same Log Analytics workspace. You may provide an existing virtual network when you create an environment.

Reasons to deploy container apps to the same environment include situations when you need to:

- Manage related services
- Deploy different applications to the same virtual network
- Instrument Dapr applications that communicate via the Dapr service invocation API
- Have applications to share the same Dapr configuration
- Have applications share the same log analytics workspace

Reasons to deploy container apps to different environments include situations when you want to ensure:

- Two applications never share the same compute resources
- Two Dapr applications can't communicate via the Dapr service invocation API

### Microservices with Azure Container Apps

Microservice architectures allow you to independently develop, upgrade, version, and scale core areas of functionality in an overall system. Azure Container Apps provides the foundation for deploying microservices featuring:

- Independent scaling, versioning, and upgrades
- Service discovery
- Native Dapr integration

### Dapr Integration

Dapr is a service for building distributed applications, providing an event-driven, portable runtime that simplifies the process of developing microservices. It offers a set of APIs for commonly used capabilities in distributed applications, such as state management, service-to-service invocation, and pub/sub messaging, enabling developers to focus more on business logic and less on architectural concerns.

Dapr is designed to be platform-agnostic, working both in the cloud and on-premises, and it can be used with various programming languages and frameworks, enhancing the flexibility and scalability of microservices development. As such, it is also a great choice when building containerized apps on Azure.

When you implement a system composed of microservices, function calls are spread across the network. To support the distributed nature of microservices, you need to account for failures, retries, and timeouts. While Container Apps features the building blocks for running microservices, use of Dapr provides an even richer microservices programming model. Dapr includes features like observability, pub/sub, and service-to-service invocation with mutual TLS, retries, and more.

</edukamu-collapse>
<br>

Azure Container Instances (ACI) and Azure Container Apps are both Azure services designed to run containerized applications. Although they may seem similar on the surface, they cater to different use cases and offer distinct features.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Container Instances or Container Apps?
</edukamu-collapse-hidden-title>

### Azure Container Instances (ACI)

Azure Container Instances is a service that offers the simplest, quickest way to run a container in Azure without having to manage any virtual machines or adopt additional services. It is primarily designed for single-container scenarios and short-lived processes.

#### Key Features

- **Simplicity and Speed**: ACI is ideal for situations in which you want to quickly run a container without orchestration, making it perfect for simple applications or tasks.
- **Serverless**: It operates in a serverless environment, meaning you don’t have to manage the underlying infrastructure.
- **Per-second Billing**: You're billed on a per-second basis, which is cost-effective for short-lived containers.

Azure Container Instances is a cost-effective solution for overnight data processing. By deploying processing software with ACI, companies can efficiently handle large datasets each night without the need for complex orchestration or infrastructure management, benefiting from ACI's per-second billing and ease of use.

### Azure Container Apps

Azure Container Apps is designed for running microservices and containerized applications that require more robust orchestration and scaling capabilities. It is built on top of Kubernetes and offers serverless container orchestration.

#### Key Features

- **Microservices and Orchestration**: It's suitable for more complex applications, especially those based on microservices architecture.
- **Automatic Scaling**: It offers auto-scaling capabilities, including scaling to zero, which is ideal for fluctuating workloads.
- **Networking and HTTP Routing**: It provides advanced networking features and the ability to route HTTP requests to different containers.

Azure Container Apps would be an ideal solution for hosting a web application composed of multiple microservices that interact with each other and in which each service can scale independently based on demand. E-commerce sites are a prime example of such use case.

### How to Choose?

- **Simplicity vs. Complexity**: Use ACI for straightforward, single-container tasks that don’t need advanced orchestration. Choose Azure Container Apps for more complex, multi-container applications, especially those needing auto-scaling and orchestration.
- **Short-term vs. Long-term Workloads**: ACI is more suited for short-lived, ad-hoc tasks or batch jobs, while Azure Container Apps is better for long-term, persistent applications.
- **Orchestration Needs**: If your application requires Kubernetes-like orchestration features, Azure Container Apps is the go-to choice.

</edukamu-collapse>
<br>

In summary, if your needs are simple and short-term, or if you're running isolated tasks, ACI is likely sufficient. For more complex applications, especially those built around microservices that benefit from Kubernetes-style orchestration and scaling, Azure Container Apps is the more suitable option.

But what, in fact, is Kubernetes - often colloquially referred to just as “k8s”? Let's take a quick look.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Kubernetes Service
</edukamu-collapse-hidden-title>

Azure Kubernetes Service (AKS) is a managed container orchestration service provided by Microsoft Azure and built on the open-source Kubernetes system, which automates the deployment, scaling, and operations of application containers across clusters of hosts. In essence, AKS simplifies the process of deploying, managing, and scaling containerized applications using Kubernetes.

<edukamu-note class="edukamu-note-icon-info">
The Kubernetes system is an open-source platform that group containers, the building blocks of an application, into logical units for easy management. Originally developed by Google and now maintained by the Cloud Native Computing Foundation, Kubernetes is widely used for orchestrating container environments due to its efficiency, scalability, and robust ecosystem.

</edukamu-note>
<br>

Azure Kubernetes service offers the following key capabilities:

1. **Container Orchestration**: AKS provides an environment for deploying, managing, and scaling your containerized applications using Kubernetes without the complexity of handling the whole Kubernetes infrastructure.
2. **Automated Scaling**: AKS supports auto-scaling of applications, allowing for efficient resource utilization and handling of varying loads.
3. **High Availability**: AKS ensures high availability and reliability of applications by maintaining and managing the health of the nodes in the cluster.
4. **Microservices Architecture**: Ideal for applications based on microservices architecture, AKS allows for independent scaling and updating of microservices.
5. **Integration with Azure Ecosystem**: AKS seamlessly integrates with other Azure services, providing a comprehensive solution for cloud-based application management.

Azure Kubernetes Service can be used in many scenarios, including, but not limited to, the following:

### 1. Complex Applications Requiring Orchestration

Applications that require complex workflows, inter-service communication, and persistent storage greatly benefit from AKS's orchestration capabilities.

### 2. Enterprise Level Deployment and Management

For enterprises looking for a robust solution for deploying and managing containerized applications at scale, AKS provides the necessary tools and integrations.

### 3. Development and DevOps Pipelines

AKS fits well into CI/CD pipelines, offering consistent environments for development, testing, and production with Kubernetes as the backbone.

In conclusion, Azure Kubernetes Service (AKS) is a powerful solution for those looking to leverage Kubernetes' container orchestration capabilities without the overhead of managing the Kubernetes infrastructure.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
The technical specifications of Azure Kubernetes are beyond the scope of this course, but you should remember that it's especially suited for complex, scalable, and high-availability applications and fits seamlessly into the broader Azure ecosystem of container services.

In the context of containerized applications, AKS is used to automate various aspects of container management, including provisioning, upgrading, and scaling resources without taking the system offline. In addition to this, AKS also supports the Docker system explored before.

Companies developing AI solutions can leverage the capabilities of AKS in order to make their applications more manageable. It can therefore also be used with services like Azure Container Instances and Container Apps, the latter of which we'll use to implement a containerized app solution on the next page!

Before taking the leap from theory to practice, it's time for another exercise.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Comparing Container Services
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module2/comparing-container-services-text-poll-1.yaml" id="ztw9swzx6jabp7r3">

<edukamu-text-poll url="/exercises/module2/comparing-container-services-text-poll-2.yaml" id="vsg7ecq4qq6xdwzz">

<edukamu-text-poll url="/exercises/module2/comparing-container-services-text-poll-3.yaml" id="bvaafvr860p8yozg">

<edukamu-text-poll url="/exercises/module2/comparing-container-services-text-poll-4.yaml" id="2fz34c0pp3um7e16">
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/2/comparing-container-services?question=ztw9swzx6jabp7r3">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

How was it? Are you starting to get the hang of containerized solutions? On the next page, we'll look at how containerized solutions are implemented. Take a small break before moving on and remember that you should also recap from time to time!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
