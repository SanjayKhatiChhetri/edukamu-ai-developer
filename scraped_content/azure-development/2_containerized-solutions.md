## Containerized Solutions

Containerized applications represent a modern approach to software development and deployment, in which applications are packaged along with their dependencies into containers. This method offers several benefits, such as consistency, scalability, and isolation, which are crucial in today's fast-paced and dynamic IT environments.

A container is a standard unit of software that encapsulates the code, runtime, system tools, libraries, and settings - pretty much everything - needed to run an application. This ensures that the application runs quickly and reliably in different computing environments. Containerization is often associated with a so-called microservices architecture in which applications are broken down into smaller, independent pieces that can be deployed and scaled separately.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Advantages of Containerized Solutions
</edukamu-collapse-hidden-title>

Containerized applications offer numerous benefits that align with modern software development practices:

1. **Consistency Across Environments**: Containers encapsulate an application and its dependencies, ensuring that it works uniformly across different computing environments, from a developer's local machine to the production server.
2. **Rapid Deployment and Scaling**: Containers can be started, stopped, and replicated quickly and easily, which is ideal for scaling applications in response to fluctuating demand.
3. **Isolation**: Each container operates in isolation, preventing one application's issues or changes from affecting others. This isolation simplifies dependency management and enhances security.
4. **Resource Efficiency**: Containers share the host system's kernel, so they are more lightweight than virtual machines. This means you can run more applications on the same hardware, improving resource utilization.
5. **Microservices Architecture**: Containerization supports a microservices architecture, where applications are broken into smaller, independent pieces. This can improve application scalability and facilitate continuous integration and deployment (CI/CD).
6. **Portability**: Since containers are not tied to an underlying infrastructure, they can run across different cloud and OS platforms.
7. **DevOps and CI/CD**: Containers integrate well with DevOps practices, enabling consistent, reliable, and frequent deployment of applications.
8. **Easier Management**: Container orchestration tools like Kubernetes automate the deployment, scaling, networking, and management of containers, simplifying operational tasks.

In the context of containerized applications, "orchestration" refers to the automated configuration, coordination, and management of complex computer systems and services. Azure Kubernetes is a prime example of a container orchestration platform. It automates the deployment, scaling, and operations of application containers across clusters of hosts, simplifying the complexity and workload involved in managing large-scale container deployments.

A short introduction to Kubernetes is provided a bit later during the course.

</edukamu-collapse>
<br>

Before we continue, let’s look into a few key concepts you need to understand. First off,
you don’t really ever build a container. Instead, you build a *container image*, which is essentially a static, frozen version of your application. An image is brought to life by the orchestration platform when it starts up your application, essentially spinning up a copy of the image into a *container*. So container images are what you create, containers are the processes that actually run on the server.

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="devisioona-logo">
### Are Containers Still Needed?
</edukamu-collapse-hidden-title>

In the 2010s, the IT world was taken over by a phenomenon called microservices, and containers were the poster child for that evolution. In reality, containers are great for microservices, but the vast majority of applications are too small to benefit from a microservices architecture. It will be simpler and more cost effective to build a traditional “monolith” application than to split it prematurely – the more pieces you have in your application architecture, the more effort you spend developing and maintaining it.

However, containers also serve purposes other than microservices architecture. While those building new applications (“greenfield software”) can choose their technologies and architectures as they best see fitting the cloud, more complicated systems often contain pieces of legacy code (“brownfield”). This code may also come with dependencies: a meticulously configured library here, a specific settings file there.

When deploying an old application into the cloud you may find that while it runs perfectly fine on your machine, it refuses to operate in something as abstract as Azure App Service. Containers’ another key feature, isolation-based consistency, is great in bringing diverse workloads into the same hosting environment, facilitating both security and cost-efficiency.

But again, the discussion comes down to complexity. As you will see in this chapter, container-based solutions come with their own technological demands, and you need to learn quite a bit more to use them. You’re making a tradeoff: Gaining something in terms of scalability and deployability, but sacrificing time and money to build the necessary competence and infrastructure. So you shouldn’t just charge into the world of containers simply because Netflix or Facebook or Spotify does it – unless you’re building a system of the same size and complexity, of course.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
When developing solutions with Microsoft Azure, a service called Azure Container Registry (ACR) is oftentimes used. In essence, it is a tool for storing and managing private container images and managing a private Docker registry. It is designed to work seamlessly with container deployment and orchestration services, particularly within the Azure ecosystem.

Wait, what’s a registry? Essentially, it’s a library of container images. There’s a public Docker registry with lots of pre-made open source images you can use, but for your own applications, you should usually use a private registry unless you specifically want to publish your applications for public consumption.

When discussing registries, container images and ACR, you’ll also become familiar with another new term: dockerfile. A dockerfile is a sequence of commands that is used to build a container image. We’ll discuss this later.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Recap on the Container and ACR Terminology
</edukamu-collapse-hidden-title>

- **Container Image**: A container image is a lightweight, standalone, executable software package that includes everything needed to run a piece of software, including the code, a runtime, libraries, environment variables, and configuration files. 
- **Managed Service**: ACR is a managed service, meaning that Azure handles the infrastructure, scalability, and maintenance of the registry. Users don't need to worry about the underlying servers or storage systems; they can focus on managing their container images.
- **Private Docker Registry**: Unlike public registries like Docker Hub, ACR is private, which means it's intended for storing and managing images that are not meant for public distribution. This aspect is crucial for businesses and organizations that need to maintain control over their container images and ensure security.
- **Docker**: Docker is a platform and tool for building, distributing, and running Docker containers. It has become synonymous with container technology because it was one of the first and most popular container platforms.

In essence, a container image is like a blueprint for a Docker container, detailing what the containerized application needs and how it should run, while Docker itself is the tooling and platform used to manage these images and run the containers.

</edukamu-collapse>
<br>

On this page, we'll get familiar with Azure Container Registry and its main capabilities. We'll also briefly visit Container Instances, before moving on to Container Apps.

Let's get started with ACR, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Container Registry
</edukamu-collapse-hidden-title>

Use the Azure Container Registry (ACR) service with your existing container development and deployment pipelines, or use Azure Container Registry Tasks to build container images in Azure. Build on demand, or fully automate builds with triggers such as source code commits and base image updates.

### Use Cases

Pull images from an Azure container registry to various deployment targets:
- **Scalable orchestration systems** that manage containerized applications across clusters of hosts, including Kubernetes, DC/OS, and Docker Swarm. 
- **Azure services** that support building and running applications at scale, including Azure Kubernetes Service (AKS), App Service, Batch, Service Fabric, and others.

Developers can also push to a container registry as part of a container development workflow. For example, target a container registry from a continuous integration and delivery tool such as Azure Pipelines or Jenkins.

Configure ACR Tasks to automatically rebuild application images when their base images are updated, or automate image builds when your team commits code to a Git repository. Create multi-step tasks to automate building, testing, and patching multiple container images in parallel in the cloud.

### Supported Images and Artifacts

Grouped in a repository, each image is a read-only snapshot of a Docker-compatible container. Azure container registries can include both Windows and Linux images. In addition to Docker container images, Azure Container Registry stores related content formats such as Helm charts and images built to the Open Container Initiative (OCI) Image Format Specification.

Use Azure Container Registry Tasks (ACR Tasks) to streamline building, testing, pushing, and deploying images in Azure. Configure build tasks to automate your container OS and framework patching pipeline, and build images automatically when your team commits code to source control.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### ACR Storage Capabilities
</edukamu-collapse-hidden-title>

Basic, Standard, and Premium Azure container registry tiers benefit from advanced Azure storage features like encryption-at-rest for image data security and geo-redundancy for image data protection.

- **Encryption-at-rest**: All container images in your registry are encrypted at rest. Azure automatically encrypts an image before storing it, and decrypts it on-the-fly when you or your applications and services pull the image.
- **Regional storage**: Azure Container Registry stores data in the region where the registry is created, to help customers meet data residency and compliance requirements. In all regions except Brazil South and Southeast Asia, Azure may also store registry data in a paired region in the same geography. In the Brazil South and Southeast Asia regions, registry data is always confined to the region, to accommodate data residency requirements for those regions.

If a regional outage occurs, the registry data may become unavailable and isn't automatically recovered. Customers who wish to have their registry data stored in multiple regions for better performance across different geographies or who wish to have resiliency in the event of a regional outage should enable geo-replication.

- **Zone redundancy**: A feature of the Premium service tier, zone redundancy uses Azure availability zones to replicate your registry to a minimum of three separate zones in each enabled region.
- **Scalable storage**: Azure Container Registry allows you to create as many repositories, images, layers, or tags as you need, up to the registry [storage limit]( https://learn.microsoft.com/en-us/azure/container-registry/container-registry-skus#_blank)(target="_blank").

High numbers of repositories and tags can impact the performance of your registry. Periodically delete unused repositories, tags, and images as part of your registry maintenance routine. Deleted registry resources like repositories, images, and tags *can't* be recovered after deletion.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Building and Managing Containers
</edukamu-collapse-hidden-title>

ACR Tasks is a suite of features within Azure Container Registry. It provides cloud-based container image building for platforms including Linux, Windows, and Azure Resource Manager, and can automate OS and framework patching for your Docker containers. ACR Tasks enables automated builds triggered by source code updates, updates to a container's base image, or timers.

### Task Scenarios

ACR Tasks supports several scenarios to build and maintain container images and other artifacts.

- **Quick task** - Build and push a single container image to a container registry on-demand, in Azure, without needing a local Docker Engine installation. Think `docker build`, `docker push` in the cloud.
- **Automatically triggered tasks** - Enable one or more *triggers* to build an image:
    - Trigger on source code update
    - Trigger on base image update
    - Trigger on a schedule
- **Multi-step task** - Extend the single image build-and-push capability of ACR Tasks with multi-step, multi-container-based workflows.

Each ACR Task has an associated source code context - the location of a set of source files used to build a container image or other artifact. Example contexts include a Git repository or a local filesystem.

### Quick Tasks

Before you commit your first line of code, ACR Tasks's quick task feature can provide an integrated development experience by offloading your container image builds to Azure. With quick tasks, you can verify your automated build definitions and catch potential problems prior to committing your code.

Using the familiar `docker build` format, the [az acr build](https://learn.microsoft.com/en-us/cli/azure/acr?view=azure-cli-latest#_blank)(target="_blank") command in the Azure CLI takes a context (the set of files to build), sends it to ACR Tasks and, by default, pushes the built image to its registry upon completion.

### Triggering Container Images

Trigger a container image build or multi-step task when code is committed, or a pull request is made or updated, to a Git repository in GitHub or Azure DevOps Services. For example, configure a build task with the Azure CLI command `az acr task create` by specifying a Git repository and optionally a branch and Dockerfile. When your team updates code in the repository, an ACR Tasks-created webhook triggers a build of the container image defined in the repo.

### Image Platforms

By default, ACR Tasks builds images for the Linux OS and the amd64 architecture. Specify the `--platform` tag to build Windows images or Linux images for other architectures. Specify the OS and optionally a supported architecture in OS/architecture format (for example, `--platform Linux/arm`). For ARM architectures, optionally specify a variant in OS/architecture/variant format (for example, `--platform Linux/arm64/v8`):

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**OS**
</edukamu-table-header>
<edukamu-table-header>
**Architecture**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Linux
</edukamu-table-cell>
<edukamu-table-cell>
amd64<br>
arm<br>
arm64<br>
386
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Windows
</edukamu-table-cell>
<edukamu-table-cell>
amd64
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

</edukamu-collapse>
<br>

Azure Container Registry provides several useful features for developers wishing to build, run, and manage containerized applications. Containers encapsulate an application and its dependencies, ensuring consistent operation across different development, testing, and production environments, which in turns ensures smooth operations across large user bases.

Do you still remember Dockerfiles? They were briefly mentioned before, and now it's time to dig a little deeper. As you might recall, they are the script of commands used to build your application.

Before continuing, take a look at the following terminology.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Terminology: Dockerfile Commands
</edukamu-collapse-hidden-title>

On the following sections, you'll come across the following:

1. **FROM**: Specifies the base image from which you are building.
2. **RUN**: Executes commands in a new layer on top of the current image and commits the results.
3. **COPY and ADD**: Used to copy files and directories from the build context or URLs into the image.
4. **CMD and ENTRYPOINT**: Define the default command that will be executed when the container starts.
5. **EXPOSE**: Informs Docker that the container listens on specific network ports at runtime.
6. **ENV**: Sets environment variables within the image.
7. **WORKDIR**: Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY, and ADD instructions that follow it.
8. **LABEL**: Provides metadata about the image.

Remember that you can always return here in case you feel confused with Dockerfile scripts!

</edukamu-collapse>
<br>

All right, let's get to building our own images!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Exploring a Dockerfile
</edukamu-collapse-hidden-title>

A Dockerfile is like a recipe that tells Docker how to make a container image. Just like a recipe lists the steps to make a dish, a Dockerfile lists the steps to create an image of your application. This image is like a packaged version of your application with everything it needs to run.

The built image can later be used to start a container, which is a running instance of your application. Dockerfiles typically include the following information:

- The base or parent image we use to create the new image
- Commands to update the base OS and install other software
- Build artifacts to include, such as a developed application
- Services to expose, such a storage and network configuration
- Command to run when the container is launched

### Creating Dockerfiles

The first step in creating a Dockerfile is choosing a base image that serves as the foundation for your application. For example, if you're building a .NET application, you might choose a Microsoft .NET image as your base.

Dockerfile

```Dockerfile
# Use the .NET 6 runtime as a base image
FROM mcr.microsoft.com/dotnet/runtime:6.0

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the published app to the container's /app directory
COPY bin/Release/net6.0/publish/ .

# Expose port 80 to the outside world
EXPOSE 80

# Set the command to run when the container starts
CMD ["dotnet", "MyApp.dll"]
```

Let's go through each line to see what it does:

- `FROM mcr.microsoft.com/dotnet/runtime:6.0`: This command sets the base image to the .NET 6 runtime, which is needed to run .NET 6 apps.
- `WORKDIR /app`: Sets the working directory to `/app`, which is where app files are copied.
- `COPY bin/Release/net6.0/publish/ .`: Copies the contents of the published app to the container's `/app` directory. We assume that the .NET 6 app has already been built and published to the `bin/Release/net6.0/publish` directory.
- `EXPOSE 80`: Exposes port 80, which is the default HTTP port, to the outside world. Change this line accordingly if your app listens on a different port.
- `CMD ["dotnet", "MyApp.dll"]`: The command to run when the container starts. In this case, we're running the dotnet command with the name of our app's DLL file (`MyApp.dll`). Change this line to match your apps name and entry point.

We're not going to cover the Dockerfile file specification, visit the <edukamu-link url="https://docs.docker.com/engine/reference/builder/" target="_blank">Dockerfile reference</edukamu-link> for more information. Each of these steps creates a cached container image as we build the final container image. These temporary images are layered on top of the previous and presented as single image once all steps complete.

</edukamu-collapse>
<br>

Understanding Dockerfile is crucial for anyone working with Docker and containerized applications. It outlines the steps taken by Docker to package your application into an image, ensuring that it runs consistently across different environments.

<edukamu-tabs theme="edukamu-tabs1">

<edukamu-tabs-tab title="Why Use Docker?">
Using Docker has many benefits. Consider the following:

1. **Environment Consistency**: Docker provides a consistent environment for your application from development through to production, ensuring the software behaves the same way regardless of where it runs.
2. **Simplifying Configuration**: Complex setups, like installing specific versions of languages and dependencies, are defined in the Dockerfile. This avoids the need for lengthy setup instructions and troubleshooting configuration issues.
3. **Isolation:** Docker isolates applications into separate containers, making sure they have their own resources, and their configurations don’t interfere with each other.
4. **Microservices Architecture**: Docker is ideal for breaking down applications into smaller, independent pieces (microservices) that are easier to manage and update.
5. **Rapid Deployment**: Containers created from a Docker image can be started, stopped, and replicated quickly, greatly speeding up deployment and scaling.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="When to Use Docker?">
Docker is suitable for various use scenarios and can be implemented whenever containerized applications are used. Consider the following:

- **Development and Testing**: Docker can be used to create a consistent development environment for your team. It ensures that the application runs in the same environment during development, testing, and production.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Docker is commonly used in CI/CD pipelines for automatically building, testing, and deploying applications.
- **Simplifying Setup for Complex Applications**: Applications that require specific environments or have complex dependencies can be easily managed with Docker.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="Example: Docker and Web Apps">
### Background

Omise is an emerging (and imaginary) online retailer specializing in lifestyle and home products. They aim to build a robust e-commerce platform to handle a wide range of products, ensure seamless user experience, and support an expanding customer base.

### Challenge

Omise’s development team faces the challenge of creating a reliable and scalable e-commerce platform. The application requires a specific tech stack including Python for backend services, a Redis cache for fast data retrieval, and a PostgreSQL database for storing product and user information. Ensuring consistency across various development environments and streamlined deployment processes is crucial.

### Solution: Docker in Development and Deployment

1. **Dockerfile Creation**: Omise's development team crafts a Dockerfile that outlines the environment setup. This file includes instructions to install the required Python version, packages, and configurations to connect with PostgreSQL, an open-source relational database management system.
2. **Local Development Environment**: Each developer on the Omise team uses Docker to pull the image created from the Dockerfile. This ensures that every developer works in an identical environment, mirroring the production setup. It eliminates the so-called "works on my machine" problem, as each container runs in isolation with its dependencies.
3. **Integration with Microservices**: The e-commerce platform is broken down into microservices (e.g., user authentication, product catalog, order processing). Each microservice is containerized using Docker, allowing individual scaling and updates without impacting other services.
4. **Continuous Integration/Continuous Deployment (CI/CD)**: Omise integrates Docker with their CI/CD pipeline. Whenever new code is committed, it triggers an automated process in which Docker images are built and pushed to a registry. These images are then used for automated testing. Successful tests lead to automatic deployment in the production environment.
5. **Production Deployment**: The same Docker images tested in the CI/CD pipeline are deployed on their production servers. This ensures that the tested application is exactly what gets deployed, reducing deployment risks.
6. **Scaling and Load Balancing**: As customer traffic varies, especially during sales or marketing events, Omise uses Docker to easily scale up or down their services. They use orchestration tools like Kubernetes to manage and balance the load across multiple container instances.
7. **Maintenance and Updates**: Omise regularly updates their application for new features and security patches. Docker makes it easier to update a specific service without downtime or affecting other components of the application.

### Outcome

By leveraging Docker, Omise successfully builds and maintains a scalable, efficient, and reliable e-commerce platform. They achieve consistent development environments, streamline deployment processes, and ensure that their application can handle varying loads with ease. This approach not only improves their operational efficiency but also enhances the overall shopping experience for their customers.
</edukamu-tabs-tab>

</edukamu-tabs>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Why Use Docker?
</edukamu-collapse-hidden-title>

Using Docker has many benefits. Consider the following:

1. **Environment Consistency**: Docker provides a consistent environment for your application from development through to production, ensuring the software behaves the same way regardless of where it runs.
2. **Simplifying Configuration**: Complex setups, like installing specific versions of languages and dependencies, are defined in the Dockerfile. This avoids the need for lengthy setup instructions and troubleshooting configuration issues.
3. **Isolation:** Docker isolates applications into separate containers, making sure they have their own resources, and their configurations don’t interfere with each other.
4. **Microservices Architecture**: Docker is ideal for breaking down applications into smaller, independent pieces (microservices) that are easier to manage and update.
5. **Rapid Deployment**: Containers created from a Docker image can be started, stopped, and replicated quickly, greatly speeding up deployment and scaling.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### When to Use Docker?
</edukamu-collapse-hidden-title>

Docker is suitable for various use scenarios and can be implemented whenever containerized applications are used. Consider the following:

- **Development and Testing**: Docker can be used to create a consistent development environment for your team. It ensures that the application runs in the same environment during development, testing, and production.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Docker is commonly used in CI/CD pipelines for automatically building, testing, and deploying applications.
- **Simplifying Setup for Complex Applications**: Applications that require specific environments or have complex dependencies can be easily managed with Docker.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Example: Docker and Web Apps
</edukamu-collapse-hidden-title>

### Background

Omise is an emerging (and imaginary) online retailer specializing in lifestyle and home products. They aim to build a robust e-commerce platform to handle a wide range of products, ensure seamless user experience, and support an expanding customer base.

### Challenge

Omise’s development team faces the challenge of creating a reliable and scalable e-commerce platform. The application requires a specific tech stack including Python for backend services, a Redis cache for fast data retrieval, and a PostgreSQL database for storing product and user information. Ensuring consistency across various development environments and streamlined deployment processes is crucial.

### Solution: Docker in Development and Deployment

1. **Dockerfile Creation**: Omise's development team crafts a Dockerfile that outlines the environment setup. This file includes instructions to install the required Python version, packages, and configurations to connect with PostgreSQL, an open-source relational database management system.
2. **Local Development Environment**: Each developer on the Omise team uses Docker to pull the image created from the Dockerfile. This ensures that every developer works in an identical environment, mirroring the production setup. It eliminates the so-called "works on my machine" problem, as each container runs in isolation with its dependencies.
3. **Integration with Microservices**: The e-commerce platform is broken down into microservices (e.g., user authentication, product catalog, order processing). Each microservice is containerized using Docker, allowing individual scaling and updates without impacting other services.
4. **Continuous Integration/Continuous Deployment (CI/CD)**: Omise integrates Docker with their CI/CD pipeline. Whenever new code is committed, it triggers an automated process in which Docker images are built and pushed to a registry. These images are then used for automated testing. Successful tests lead to automatic deployment in the production environment.
5. **Production Deployment**: The same Docker images tested in the CI/CD pipeline are deployed on their production servers. This ensures that the tested application is exactly what gets deployed, reducing deployment risks.
6. **Scaling and Load Balancing**: As customer traffic varies, especially during sales or marketing events, Omise uses Docker to easily scale up or down their services. They use orchestration tools like Kubernetes to manage and balance the load across multiple container instances.
7. **Maintenance and Updates**: Omise regularly updates their application for new features and security patches. Docker makes it easier to update a specific service without downtime or affecting other components of the application.

### Outcome

By leveraging Docker, Omise successfully builds and maintains a scalable, efficient, and reliable e-commerce platform. They achieve consistent development environments, streamline deployment processes, and ensure that their application can handle varying loads with ease. This approach not only improves their operational efficiency but also enhances the overall shopping experience for their customers.

</edukamu-collapse>
<br> -->

Are you starting to get the hang of Docker? If you are feeling a little confused at this stage, don't blame yourself! In fact, it could be beneficial to take a while to explore the differences of Docker, Azure Blob Storage, and Azure Cosmos DB.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Docker, Cosmos DB, or Blob Storage?
</edukamu-collapse-hidden-title>

Docker, Azure Cosmos DB, and Azure Blob Storage serve different purposes in the realm of cloud computing and application development, each addressing distinct needs:

1. **Docker**:
- **Primary Use**: Docker is a platform for developing, shipping, and running applications inside containers. A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably in different computing environments.
- **Key Features**: Provides an isolated environment for applications (containerization), ensures consistency across various environments, supports microservices architecture, and fits into DevOps practices for continuous integration and deployment (CI/CD).
- **Use Cases**: Ideal for creating consistent development environments, isolating applications for security and dependency management, and simplifying deployment and scaling in cloud environments.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Azure Cosmos DB</span>:
</li>
</ol>
</edukamu-section>
- **Primary Use**: Azure Cosmos DB is a globally distributed, multi-model database service. It's designed for highly available, globally scalable applications with a need for wide-ranging database capabilities.
- **Key Features**: Offers multiple data models and API choices, provides low-latency access to data, supports automatic and instant scalability, and offers comprehensive service level agreements (that concern quality, abailability, and responsibilities related to a service) for throughput, latency, availability, and consistency.
- **Use Cases**: Suitable for applications requiring a scalable, globally-distributed database with rich query capabilities, real-time analytics, and multi-model support like IoT, e-commerce platforms, and gaming.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Azure Blob Storage</span>:
</li>
</ol>
</edukamu-section>
- **Primary Use**: Azure Blob Storage is a scalable cloud object storage solution for unstructured data. It's designed for storing large amounts of data, such as documents, images, or media files.
- **Key Features**: Offers different access tiers (hot, cool, and archive) for cost-effective storage solutions, supports large-scale unstructured data storage, and provides secure and durable storage options.
- **Use Cases**: Ideal for storing large volumes of unstructured data, archival storage, data backup and restore, serving images or documents directly to a browser, and storing data for analysis.


### Key Differences:

- **Purpose**: Docker focuses on application containerization and deployment, Cosmos DB is a multi-model database for structured and semi-structured data, and Blob Storage is for large-scale unstructured data storage.
- **Data Handling**: Docker doesn’t directly handle data storage; it encapsulates application environments. Cosmos DB and Blob Storage, on the other hand, are data storage solutions but with different focuses (structured vs. unstructured data).
- **Scalability and Performance**: Docker impacts how applications are deployed and scaled, while Cosmos DB and Blob Storage offer scalability for data storage and access.

In essence, Docker is for containerizing and running applications, Cosmos DB is for managing diverse and globally distributed databases, and Azure Blob Storage is for storing vast amounts of unstructured data.

</edukamu-collapse>
<br>

The world of data is unbelievably expansive, which you've undoubtedly noticed by now. By keeping in mind the differences between the services covered here, you can start to explore each one further and further, when you get the change to work in Microsoft Azure!

If you already have an active Azure subscription (or a free trial), feel free to complete the following practice!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Build and Run a Container Image with ACR
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this exercise you use ACR Tasks to perform the following actions:

- Create an Azure Container Registry
- Build and push image from a Dockerfile
- Verify the results
- Run the image in the ACR

(Before beginning, make sure you have an active Azure subscription (or a free trial) available on your Microsoft account (personal or business/school). There are detailed instructions for activating a free trial on the *Configuring Web Apps* page.)

### Step 1. Start the Cloud Shell

1. Sign in and navigate to the Azure Portal. Open the Cloud Shell.

<edukamu-image url="/graphics/module2/cloud-shell-menu.png" alt="The location of Cloud Shell launch button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Azure CloudShell is an interactive, browser-accessible shell (a user interface that provides access to various services of an operating system) for managing Azure resources. It provides a ready-to-use environment with a variety of tools installed and is accessible directly within the Azure portal. CloudShell offers two types of shells:

**a. Bash Shell**: For a Linux-based experience, which is great for those familiar with Linux or Unix-like command-line interfaces.

**b. PowerShell**: For a Windows-based experience, which is ideal for those who are comfortable with PowerShell and Windows command-line tools.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
When the shell opens select the Bash environment.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module2/shell-bash-selection.png" alt="Selecting the Bash environment." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>


### Step 2. Create an Azure Container Registry

1. Create a resource group for the registry, replace `< myLocation >` in the following command with a location near you.

Bash

```Bash
az group create --name az204-acr-rg --location <myLocation>
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Create a basic container registry. The registry name must be unique within Azure, and contain 5-50 alphanumeric characters. Replace <code>< myContainerRegistry ></code> in the following command with a unique value.
</li>
</ol>
</edukamu-section>

Bash

```bash
az acr create --resource-group az204-acr-rg \
    --name <myContainerRegistry> --sku Basic
```

**Note**: The command creates a Basic registry, a cost-optimized option for developers learning about Azure Container Registry.


### Step 3. Build and Push Image from a Dockerfile

Now use Azure Container Registry to build and push an image based on a local Dockerfile.

1. Create, or navigate, to a local directory and then use the following command to create the Dockerfile. The Dockerfile contains a single line that references the `hello-world` image hosted at the Microsoft Container Registry.

Bash

```Bash
echo FROM mcr.microsoft.com/hello-world > Dockerfile
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Run the <code>az acr build</code> command, which builds the image and, after the image is successfully built, pushes it to your registry. Replace <code>< myContainerRegistry ></code> with the name you used earlier.
</li>
</ol>
</edukamu-section>

Azure CLI

```bash
az acr build --image sample/hello-world:v1  \
    --registry <myContainerRegistry> \
    --file Dockerfile .
```

Following is a shortened sample of the output from the previous command showing the last few lines with the final results. You can see in the `repository` field the `sample/hello-word` image is listed.

```code
- image:
    registry: <myContainerRegistry>.azurecr.io
    repository: sample/hello-world
    tag: v1
    digest: sha256:92c7f9c92844bbbb5d0a101b22f7c2a7949e40f8ea90c8b3bc396879d95e899a
  runtime-dependency:
    registry: mcr.microsoft.com
    repository: hello-world
    tag: latest
    digest: sha256:92c7f9c92844bbbb5d0a101b22f7c2a7949e40f8ea90c8b3bc396879d95e899a
  git: {}

Run ID: cf1 was successful after 11s
```

### Step 4. Verify the Results

1. Use the `az acr repository list` command to list the repositories in your registry. Replace `< myContainerRegistry >` with the name you used earlier.

Bash

```Bash
az acr repository list --name <myContainerRegistry> --output table
```

Output:

```code
Result
----------------
sample/hello-world
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Use the <code>az acr repository show-tags</code> command to list the tags on the <span style="font-weight: bold;">sample/hello-world</span> repository. Replace <code>< myContainerRegistry ></code> with the name you used earlier.
</li>
</ol>
</edukamu-section>

Bash

```Bash
az acr repository show-tags --name <myContainerRegistry> \
    --repository sample/hello-world --output table
```

Output:

```code
Result
--------
v1
```


### Step 5. Run the Image with ACR

Run the sample/hello-world:v1 container image from your container registry by using the `az acr run` command. The following example uses $Registry to specify the registry where you run the command. Replace `< myContainerRegistry >` with the name you used earlier.

Bash

```Bash
az acr run --registry <myContainerRegistry> \
    --cmd '$Registry/sample/hello-world:v1' /dev/null
```

The `cmd` parameter in this example runs the container in its default configuration, but `cmd` supports other `docker run` parameters or even other `docker` commands.

The following is shortened sample of the output:

```code
Packing source code into tar to upload...
Uploading archived source code from '/tmp/run_archive_ebf74da7fcb04683867b129e2ccad5e1.tar.gz'...
Sending context (1.855 KiB) to registry: mycontainerre...
Queued a run with ID: cab
Waiting for an agent...
2019/03/19 19:01:53 Using acb_vol_60e9a538-b466-475f-9565-80c5b93eaa15 as the home volume
2019/03/19 19:01:53 Creating Docker network: acb_default_network, driver: 'bridge'
2019/03/19 19:01:53 Successfully set up Docker network: acb_default_network
2019/03/19 19:01:53 Setting up Docker configuration...
2019/03/19 19:01:54 Successfully set up Docker configuration
2019/03/19 19:01:54 Logging in to registry: mycontainerregistry008.azurecr.io
2019/03/19 19:01:55 Successfully logged into mycontainerregistry008.azurecr.io
2019/03/19 19:01:55 Executing step ID: acb_step_0. Working directory: '', Network: 'acb_default_network'
2019/03/19 19:01:55 Launching container with name: acb_step_0

Hello from Docker!
This message shows that your installation appears to be working correctly.

2019/03/19 19:01:56 Successfully executed container: acb_step_0
2019/03/19 19:01:56 Step ID: acb_step_0 marked as successful (elapsed time in seconds: 0.843801)

Run ID: cab was successful after 6s
```

</edukamu-collapse>
<br>

In summary, containerized applications provide a modern solution to software deployment challenges, offering significant benefits in terms of consistency, efficiency, security, and scalability, which are essential in today's fast-paced and agile IT environments.

Before moving on to our next topic, it's time for another exercise.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Containerized Solutions
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/containerized-solutions-question-scroll-1.yaml" id="nj2dk3cmn0oqtyx7">
<br>

</edukamu-collapse>
<br>

On the next page, we'll explore a few Azure services built for effectively designing, building, and managing containerized app solutions.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
