## Computing Services 

In this page, you will be introduced to the computing services of Azure. Our focus will be on three such services, namely virtual machines, containers, and Azure functions. 

In short, virtual machines are services that let you emulate other services. You might, for example, switch on your computer, fire up a virtual machine and run a Linux operating system virtually on your Windows terminal. 

Containers, in turn, are packages of software containing all necessary elements to run in any environment. Azure functions is a serverless solution designed for reducing the need for infrastructure, therefore minimizing costs. 

Next, we’ll take a closer look at the three.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Virtual Machines
</edukamu-collapse-hidden-title>

With Azure Virtual Machines (VMs), you can create and use VMs in the cloud. VMs provide infrastructure as a service (IaaS) in the form of a virtualized server and can be used in many ways. Just like a physical computer, you can customize all of the software running on your VM. VMs are an ideal choice when you need:

* Total control over the operating system (OS).
* The ability to run custom software.
* To use custom hosting configurations.

An Azure VM gives you the flexibility of virtualization without having to buy and maintain the physical hardware that runs the VM. However, as an IaaS offering, you still need to configure, update, and maintain the software that runs on the VM.

You can even create or use an already created image to rapidly provision VMs. You can create and provision a VM in minutes when you select a preconfigured VM image. An image is a template used to create a VM and may already include an OS and other software, like development tools or web hosting environments.

Some common examples or use cases for virtual machines include:

* **During testing and development**. VMs provide a quick and easy way to create different OS and application configurations. Test and development personnel can then easily delete the VMs when they no longer need them.
* **When running applications in the cloud**. The ability to run certain applications in the public cloud as opposed to creating a traditional infrastructure to run them can provide substantial economic benefits. For example, an application might need to handle fluctuations in demand. Shutting down VMs when you don't need them or quickly starting them up to meet a sudden increase in demand means you pay only for the resources you use.
* **When extending your datacenter to the cloud**: An organization can extend the capabilities of its own on-premises network by creating a virtual network in Azure and adding VMs to that virtual network. Applications like SharePoint can then run on an Azure VM instead of running locally. This arrangement makes it easier or less expensive to deploy than in an on-premises environment.
* **During disaster recovery**: As with running certain types of applications in the cloud and extending an on-premises network to the cloud, you can get significant cost savings by using an IaaS-based approach to disaster recovery. If a primary datacenter fails, you can create VMs running on Azure to run your critical applications and then shut them down when the primary datacenter becomes operational again.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Virtual Desktop
</edukamu-collapse-hidden-title>

Another type of virtual machine is the Azure Virtual Desktop. Azure Virtual Desktop is a desktop and application virtualization service that runs on the cloud. It enables you to use a cloud-hosted version of Windows from any location. Azure Virtual Desktop works across devices and operating systems, and works with apps that you can use to access remote desktops or most modern browsers.

The following video gives you an overview of Azure Virtual Desktop:

<!-- Tähän video osoitteesta: https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/4-virtual-desktop    -->
<iframe width="640" height="360" src="https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed-one-stream.html?id=04978efb-d8e5-4352-bcb4-45399a988a69&locale=en-us&embedUrl=%2Ftraining%2Fmodules%2Fdescribe-azure-compute-networking-services%2F4-virtual-desktop" frameborder="0" allowfullscreen></iframe>
<br>

</edukamu-collapse>
</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Containers
</edukamu-collapse-hidden-title>

While virtual machines are an excellent way to reduce costs versus the investments that are necessary for physical hardware, they're still limited to a single operating system per virtual machine. If you want to run multiple instances of an application on a single host machine, containers are an excellent choice.

Containers are a virtualization environment. Much like running multiple virtual machines on a single physical host, you can run multiple containers on a single physical or virtual host. Unlike virtual machines, you don't manage the operating system for a container. Virtual machines appear to be an instance of an operating system that you can connect to and manage. Containers are lightweight and designed to be created, scaled out, and stopped dynamically. It's possible to create and deploy virtual machines as application demand increases, but containers are a lighter weight, more agile method. Containers are designed to allow you to respond to changes on demand. With containers, you can quickly restart if there's a crash or hardware interruption. One of the most popular container engines is Docker, which is supported by Azure.

The following video highlights several of the important differences between virtual machines and containers:

<!-- Tähän video osoitteesta: https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/5-containers     -->
<iframe width="640" height="360" src="https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed-one-stream.html?id=7aa48d3f-4304-4a18-9861-eaf9d4bebd26&locale=en-us&embedUrl=%2Ftraining%2Fmodules%2Fdescribe-azure-compute-networking-services%2F5-containers" frameborder="0" allowfullscreen></iframe>
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Functions
</edukamu-collapse-hidden-title>

Azure Functions is an event-driven, serverless compute option that doesn’t require maintaining virtual machines or containers. If you build an app using VMs or containers, those resources have to be “running” in order for your app to function. With Azure Functions, an event wakes the function, alleviating the need to keep resources provisioned when there are no events.

Video below will demonstrate you serverless computing in Azure:

<!-- Tähän video osoitteesta: https://learn.microsoft.com/en-us/training/modules/describe-azure-compute-networking-services/6-functions      -->
<iframe width="640" height="360" src="https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed-one-stream.html?id=bd90a678-3c03-4e0f-9470-f6f0626373e0&locale=en-us&embedUrl=%2Ftraining%2Fmodules%2Fdescribe-azure-compute-networking-services%2F6-functions" frameborder="0" allowfullscreen></iframe>
<br>

</edukamu-collapse>

<edukamu-section class="slate-section slate-blue">
If you are looking  to host your application on Azure, you might initially turn to a virtual machine (VM) or containers. Both VMs and containers provide excellent hosting solutions. VMs give you maximum control of the hosting environment and allow you to configure it exactly how you want. 

VMs also may be the most familiar hosting method if you’re new to the cloud. Containers, with the ability to isolate and individually manage different aspects of the hosting solution, can also be a robust and compelling option.

There are, however, other hosting options from which to choose as well with Azure, including Azure App Service.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure App Service
</edukamu-collapse-hidden-title>

App Service enables you to build and host web apps, background jobs, mobile back-ends, and RESTful APIs in the programming language of your choice without managing infrastructure. It offers automatic scaling and high availability. App Service supports Windows and Linux. It enables automated deployments from GitHub, Azure DevOps, or any Git repo to support a continuous deployment model.

Azure App Service is a robust hosting option that you can use to host your apps in Azure. Azure App Service lets you focus on building and maintaining your app, and Azure focuses on keeping the environment up and running.

Azure App Service is an HTTP-based service for hosting web applications, REST APIs, and mobile back ends. It supports multiple languages, including .NET, .NET Core, Java, Ruby, Node.js, PHP, or Python. It also supports both Windows and Linux environments.

With App Service, you can host most common app service styles like:

* Web apps
* API apps
* WebJobs
* Mobile apps

App Service handles most of the infrastructure decisions you deal with in hosting web-accessible apps:

* Deployment and management are integrated into the platform.
* Endpoints can be secured.
* Sites can be scaled quickly to handle high traffic loads.
* The built-in load balancing and traffic manager provide high availability.

All of these app styles are hosted in the same infrastructure and share these benefits. This flexibility makes App Service the ideal choice to host web-oriented applications.

</edukamu-collapse>
<br>


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Computing on Azure
</edukamu-collapse-hidden-title>
<edukamu-question-scroll url="/exercises/module1/computing-service-question-scroll.yaml" id="2k72ftrf8002pgi8"/>
<br>
</edukamu-collapse>
<br>

Virtual machines and containers are effective and might even help save costs significantly. That’s not all Azure is capable of, though, since it’s networking capabilities are also quite impressive. They’re also our next topic.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
