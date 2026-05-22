## Deploying Azure AI Containers

Microsoft Azure’s AI Services can be seamlessly integrated into all kinds of intelligent solutions and systems, but sometimes even that is not enough. Sometimes, we need even greater flexibility and control over our AI workloads, which is when we must take an entirely different approach – in other words, we need containers.

We’ve worked with containers on multiple occasions throughout this study program, so you should already be familiar with them. (If not, there’s a short recap coming up shortly, so no worries!)

Containers are lightweight, portable, and scalable units that can encapsulate your AI models, dependencies, and applications. By containerizing Azure AI services, you can achieve consistency in deployment across various environments, manage dependencies with ease, and ensure seamless scalability.

<edukamu-note class="edukamu-note-icon-info">
**Recap: Containers**

Containerized development, unlike traditional methods, separates applications from specific hardware and software configurations. Containers encapsulate applications and dependencies, ensuring consistent performance across environments. They offer scalability, isolation, and enhanced security, simplifying deployment and resource optimization, making them a superior choice for modern software development.
</edukamu-note>
<br>

Let’s check out how Azure AI Services benefits from a containerized approach.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Getting Started with Azure AI Services Containers
</edukamu-collapse-hidden-title>

Containers enable you to host Azure AI services either on-premises or in Azure. For example, if your application uses sensitive data in an on-premises SQL Server to call an Azure AI services service, you can deploy Azure AI services in containers on the same network. Now your data can stay on your local network and not be passed to the cloud. Deploying Azure AI services in a container on-premises will also decrease the latency between the service and your local data, which can improve performance.

When you deploy a software service, it must be hosted in an environment that provides the hardware, operating system, and supporting runtime components on which the service depends.

Azure AI services is provided as a cloud service, in which the service software is hosted in an Azure data center that provides the underlying runtime services, operating system, and hardware. However, you can also deploy some Azure AI services in a container, which encapsulates the necessary runtime components, and which is in turn deployed in a container host that provides the underlying operating system and hardware.

<edukamu-image url="/graphics/module1/containers.png" alt="Diagram of a container host with 4 containers.">
<br>

### What are Containers?

A container comprises an application or service and the runtime components needed to run it, while abstracting the underlying operating system and hardware. In practice, this abstraction results in two significant benefits:

- Containers are portable across hosts, which may be running different operating systems or use different hardware - making it easier to move an application and all its dependencies.
- A single container host can support multiple isolated containers, each with its own specific runtime configuration - making it easier to consolidate multiple applications that have different configuration requirement.

A container is encapsulated in a *container image* that defines the software and configuration it must support. Images can be stored in a central registry, such as *Docker Hub*, or you can maintain a set of images in your own registry.


### Container Deployment

To use a container, you typically pull the container image from a registry and deploy it to a container host, specifying any required configuration settings. The container host can be in the cloud, in a private network, or on your local computer. For example:

- A Docker server.
- An Azure Container Instance (ACI).
- An Azure Kubernetes Service (AKS) cluster.

(As you might remember, Docker is an open source solution for container development and management that includes a server engine that you can use to host containers. There are versions of the Docker server for common operating systems, including Microsoft Windows and Linux.)

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Using Azure AI Containers
</edukamu-collapse-hidden-title>

There are container images for Azure AI services in the Microsoft Container Registry that you can use to deploy a containerized service that encapsulates an individual Azure AI services service API.

To deploy and use an Azure AI services container, the following three activities must occur:

1. The container image for the specific Azure AI services API you want to use is downloaded and deployed to a container host, such as a local Docker server, an Azure Container Instance (ACI), or Azure Kubernetes Service (AKS).
2. Client applications submit data to the endpoint provided by the containerized service, and retrieve results just as they would from an Azure AI services cloud resource in Azure.
3. Periodically, usage metrics for the containerized service are sent to an Azure AI services resource in Azure in order to calculate billing for the service.

<edukamu-image url="/graphics/module1/ai-services-container.png" alt="A diagram of an Azure AI services container deployed to a container host and consumed by a client application.">
<br>

Even when using a container, you must provision an Azure AI services resource in Azure for billing purposes. Client applications send their requests to the containerized service, meaning that potentially sensitive data is not sent to the Azure AI services endpoint in Azure; but the container must be able to connect to the Azure AI services resource in Azure periodically to send usage metrics for billing.

### Azure AI Services Container Images

Each container provides a subset of Azure AI services functionality. For example, not all features of the Azure AI Language service are in a single container. Language detection, translation, and sentiment analysis are each separate container images. However, the setup steps are similar for each container.

#### a. Language Containers

For the AI Language service, which we’ll cover on the next page, the core features map to separate images:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Feature**
</edukamu-table-header>
<edukamu-table-header>
**Image**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Key Phrase Extraction
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/azure-cognitive-services/textanalytics/keyphrase
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Language Detection
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/azure-cognitive-services/textanalytics/language
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Sentiment Analysis v3 (English)
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/azure-cognitive-services/textanalytics/sentiment:3.0-en
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Text Language Detection
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/textanalytics/language/about
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Text Analytics for health
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/textanalytics/healthcare/about
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Translator
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/translator/text-translation/about
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

#### b. Speech Containers

<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Feature**
</edukamu-table-header>
<edukamu-table-header>
**Image**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Speech to text
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/speechservices/speech-to-text/about
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Custom Speech to text
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/speechservices/custom-speech-to-text/about
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Neural Text to speech
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/speechservices/neural-text-to-speech/about
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Speech language detection
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/speechservices/language-detection/about
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

#### c. Vision Containers

<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Feature**
</edukamu-table-header>
<edukamu-table-header>
**Image**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Read OCR
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/vision/read/about
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Spatial analysis
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/vision/spatial-analysis/about
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


#### d. Decision Containers

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Feature**
</edukamu-table-header>
<edukamu-table-header>
**Image**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Anomaly Detector
</edukamu-table-cell>
<edukamu-table-cell>
mcr.microsoft.com/product/azure-cognitive-services/decision/anomaly-detector/about
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

You can use the Docker pull command to download container images to work with them directly from your machine. Some of the containers are in a "Gated" public preview state, and you need to explicitly request access to use them. Other

(While AI-based speech, vision, and decision services are also available within Microsoft Azure, we will not be focusing on them on this course. They will be mentioned here and there, though, so it’s good to be aware of their existence and basic capabilities.)


### Configuring Azure AI Services Containers

When you deploy an Azure AI services container image to a host, you must specify three settings: ApiKey, Billing, and Eula.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Setting**
</edukamu-table-header>
<edukamu-table-header>
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
ApiKey
</edukamu-table-cell>
<edukamu-table-cell>
Key from your deployed Azure AI service; used for billing.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Billing
</edukamu-table-cell>
<edukamu-table-cell>
Endpoint URI from your deployed Azure AI service; used for billing.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Eula
</edukamu-table-cell>
<edukamu-table-cell>
Value of **accept** to state you accept the license for the container.
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

After your Azure AI services container is deployed, applications consume the containerized Azure AI services endpoint rather than the default Azure endpoint. The client application must be configured with the appropriate endpoint for your container, but does not need to provide a subscription key to be authenticated. You can implement your own authentication solution and apply network security restrictions as appropriate for your specific application scenario.

</edukamu-collapse>
<br>

Containers encapsulate applications and their dependencies into standardized units that include everything needed to run the application, regardless of the host system. This eliminates many of the inconsistencies and configuration-related challenges associated with traditional development.

Containers can be easily moved between development, testing, and production environments, ensuring consistent behavior across the entire software development life cycle. This makes them especially useful for developing AI-based solutions.

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Using Azure AI Services Containers
</edukamu-collapse-hidden-title>

**Reminder:** Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practical exercise, you’ll get to set up and use an Azure AI Services container. 

This exercise uses a virtual machine, provided by Microsoft, on Microsoft’s Learn platform. In order to set up the lab environment, please navigate to the Microsoft Learn platform.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/investigate-container-for-use-with-ai-services/4-exercise-use-container">Microsoft Learn: Lab Environment</edukamu-button>
<br>

Please notice that you need to sign into your Microsoft account (personal or professional) in order to use the Lab environment.

After signing in, you can launch the Lab environment by clicking on the button illustrated in the image below.

<edukamu-image url="/graphics/module1/lab-ohje.png" alt="Picture illustrating the lab button on Microsoft Learn." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

The lab environment (Virtual Machine) will launch in a separate window. You’ll find detailed instructions on signing in, getting started, and completing the practice exercise on the right.

<edukamu-image url="/graphics/module1/lab-ohje-2.png" alt="Picture illustrating the lab environment." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

Good luck!

</edukamu-collapse>
<br> -->

Containers are quite handy when it comes to application development – including apps that rely on artificial intelligence!

In order to make it all more concrete, let’s check out how our imaginary e-commerce platform, Omise, could use containerized Azure AI Services in order to enhance their business.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Scenario: Shopping Assistant and Containers
</edukamu-collapse-hidden-title>

Generative AI provides incredible opportunities for all kinds of services, among them e-commerce platforms. Intelligent and quick-witted shopping assistants, communicating just like humans, can make shopping experiences a lot more interesting and rewarding – even when browsing the virtual shelves alone!

Let’s see how our imaginary e-commerce platform Omise could create such a service by implementing Azure AI Services containers.

### Objective: Create a Generative AI Shopping Assistant

#### Step 1: Defining the Project

Omise starts by defining the goals and scope of the project. It determines what specific tasks the generative AI shopping assistant should perform, such as providing product recommendations, answering customer queries, or generating product descriptions.

#### Step 2: Choosing Azure AI Services

Omise selects the Azure AI Services that are suitable for the project. This could include Azure AI Services for natural language processing (NLP), Azure Machine Learning for training custom models, and any other relevant services.

#### Step 3: Developing the AI Model

Omise creates and trains the AI model that will serve as the generative shopping assistant. Depending on its requirements, Omise might use pre-trained models from Azure AI Services or train a custom model using Azure Machine Learning.

#### Step 4: Containerizing the AI Model

Omise uses Docker to containerize the AI model and its dependencies. This involves creating a Dockerfile that specifies the necessary environment setup, dependencies, and code for the AI model.

#### Step 5: Pushing the Container to Azure Container Registry (ACR)

Omise stores the container image in Azure Container Registry (ACR). ACR is a private container registry that securely stores and manages Docker container images.

#### Step 6: Setting Up Azure Kubernetes Service (AKS)

Omise deploys and configures Azure Kubernetes Service (AKS) to manage containerized applications. AKS provides scalability and orchestration capabilities for the AI shopping assistant.

#### Step 7: Deploying the AI Container

Omise deploys the containerized AI model on AKS. This involves creating Kubernetes pods, services, and deployments to run and manage the containers. Omise can also scale the number of replicas based on demand.

#### Step 8: Integrating with Omise

Omise integrates the generative AI shopping assistant with the Omise e-commerce platform. This may involve API integration, webhook notifications, or direct communication with the platform's backend.

#### Step 9: Testing and Monitoring

Omise thoroughly tests the AI shopping assistant to ensure it performs as expected. It implements monitoring and logging to track its performance and gather insights for future improvements.

#### Step 10: Improving the Service

Omise continuously refines and improves the AI model based on user feedback and performance metrics. Azure Machine Learning can help automate model retraining and deployment.

As Omise's e-commerce platform grows, it uses AKS to scale the AI shopping assistant horizontally by adding more containers to handle increased traffic and demand. Omise also implements security best practices and compliance measures to protect customer data and ensure that the AI shopping assistant adheres to regulatory requirements.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-orange">
By following the (simplified) steps described above, Omise would be able develop and deploy a generative AI shopping assistant using Azure AI Services in containers. This assistant would enhance the shopping experience, provide personalized recommendations, and improve customer engagement on the e-commerce platform.

Now, before continuing, take some time to go through the above example one more time. Think about it carefully, and try to come up with explanations on how Azure AI Services containers can improve the following aspects of development:

1. isolation and portability
2. scalability
3. resource efficiency
4. deployment consistency
5. version control
6. management.

After coming up with your suggestions, check out the model answer below!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Model Answer: Advantages of Containerization 
</edukamu-collapse-hidden-title>

### 1. Isolation and Portability

Containers encapsulate the AI model, its dependencies, and runtime environment into a single, isolated unit. This isolation ensures that the AI model operates consistently across different environments, from development to production, addressing the "it works on my machine" problem. Containers are highly portable, meaning that the same containerized AI model can be run on different infrastructure without modification.

### 2. Scalability

Containers enable easy scaling of the AI shopping assistant. With container orchestration tools like Kubernetes on Azure Kubernetes Service (AKS), you can dynamically deploy multiple instances (replicas) of the containerized AI model to handle increased workloads. In our example scenario, this scalability is crucial for accommodating varying customer traffic during peak shopping periods.

### 3. Resource Efficiency

Containers are lightweight and share the host operating system, maximizing resource efficiency. This efficiency is particularly important in a cloud environment like Azure, as it helps optimize infrastructure costs and ensures efficient use of available resources.

### 4. Deployment Consistency

By containerizing the AI model and its dependencies, you achieve deployment consistency. This consistency simplifies the deployment process across development, testing, and production environments, reducing the chances of configuration-related issues and streamlining the deployment pipeline.

### 5. Version Control and Rollback

Containers allow for version control, making it easy to manage different versions of the AI model. In case a newer version introduces unforeseen issues, you can quickly roll back to a previous containerized version to maintain system stability.

### 6. Management

Managing containerized applications, including updates and scaling, is made more manageable through container orchestration platforms like Kubernetes on AKS. These platforms provide centralized control and automation for containerized workloads.

</edukamu-collapse>
<br>


In summary, containers provide Omise with a consistent, scalable, and efficient way to package, deploy, and manage the generative AI shopping assistant. They facilitate the seamless integration of AI capabilities into the e-commerce platform, ensuring that the shopping assistant performs reliably and efficiently across various stages of development and production.

Next, let’s recap with a traditional exercise, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Containerized Azure AI Services
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/deploying-azure-ai-containers-question-scroll-1.yaml" id="djbuwmn9zocm273c">
<br>

</edukamu-collapse>


How are you doing so far? Remember that you can advance on this course at your own pace – there’s no need to rush! Make sure to take little breaks from time to time in order to give your brain some time to adjust and regroup.

Our next topic is a service called Azure AI Language. We’ll spend most of the second unit exploring it, so make sure to pay extra attention on the next page!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
