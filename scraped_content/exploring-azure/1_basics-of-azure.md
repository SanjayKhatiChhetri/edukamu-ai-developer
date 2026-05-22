<edukamu-video content="/videos/devai-1-unit1-video.yaml"/>
<br>

## Basics of Azure

Welcome to the first chapter of the course. In this section, you will get acquainted with Microsoft Azure and its services. We’ll start with the basics, so don’t worry, if you haven’t used the platform before. You will soon find your way around!

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="sovelto-eduhouse-logo">
### Video: Why Study Azure Fundamentals?
</edukamu-collapse-hidden-title>

<edukamu-section class="edukamu-video-reunat">
<edukamu-video content="/videos/devai-1-eduhouse-why-start-with-fundamentals-video.yaml"/>
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="sovelto-eduhouse-logo">
### Transcription: Why study Azure Fundamentals?
</edukamu-collapse-hidden-title>

"Now, you might ask, 'Why start with Azure Fundamentals? Why is it so crucial?' The answer lies at the very core of cloud technology. Azure Fundamentals is not just a course; it's the foundation upon which all cloud skills are built. Whether you're looking to specialize further in the cloud or just seeking to enhance your current role with cloud expertise, understanding the basics of Azure is essential. It gives you the language, the tools, and the concepts needed to navigate and excel in the cloud-centric world we live in. By starting with Azure Fundamentals, you're not just learning a part of the cloud; you're grasping the whole ecosystem, enabling you to make informed decisions and pave a way forward in your career or personal growth in technology."

</edukamu-collapse>
<br>

</edukamu-collapse>
<br>


What is Microsoft Azure anyway? Unfortunately, there are no short answers, since it’s a lot of things. In essence, it’s a cloud-based platform that’s full of different opportunities, possibilities, and solutions for all cloud-computing needs – be it an entrepreneur just starting their business or a huge multinational conglomerate dominating their field, Azure has the solution.

Before exploring Azure, it might be beneficial to review cloud-based services and service types. More specifically, we’ll get acquainted with the characteristics that make them special!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Service Type 1: Infrastructure as a Service (IaaS)
</edukamu-collapse-hidden-title>

Infrastructure as a service (IaaS) is the most flexible category of cloud services, as it provides you the maximum amount of control for your cloud resources. In an IaaS model, the cloud provider is responsible for maintaining the hardware, network connectivity (to the internet), and physical security. You’re responsible for everything else: operating system installation, configuration, and maintenance; network configuration; database and storage configuration; and so on. With IaaS, you’re essentially renting the hardware in a cloud datacenter, but what you do with that hardware is up to you.

#### Shared Responsibility Model

The shared responsibility model applies to all the cloud service types. IaaS places the largest share of responsibility with you. The cloud provider is responsible for maintaining the physical infrastructure and its access to the internet. You’re responsible for installation and configuration, patching and updates, and security.

<edukamu-image url="/graphics/module1/shared-responsibility-b3829bfe.svg" alt="Diagram showing the responsibilities of the shared responsibility model.">
<br>

#### Use Scenarios

Some common scenarios where IaaS might make sense include:

- Lift-and-shift migration: You’re setting up cloud resources similar to your on-prem datacenter, and then simply moving the things running on-prem to running on the IaaS infrastructure.
- Testing and development: You have established configurations for development and test environments that you need to rapidly replicate. You can start up or shut down the different environments rapidly with an IaaS structure, while maintaining complete control.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Cloud Service 2: Platform as a Service (PaaS)
</edukamu-collapse-hidden-title>

Platform as a service (PaaS) is a middle ground between renting space in a datacenter (infrastructure as a service) and paying for a complete and deployed solution (software as a service). In a PaaS environment, the cloud provider maintains the physical infrastructure, physical security, and connection to the internet. They also maintain the operating systems, middleware, development tools, and business intelligence services that make up a cloud solution. In a PaaS scenario, you don't have to worry about the licensing or patching for operating systems and databases.

PaaS is well suited to provide a complete development environment without the headache of maintaining all the development infrastructure.

#### Shared Responsibility Model

The shared responsibility model applies to all the cloud service types. PaaS splits the responsibility between you and the cloud provider. The cloud provider is responsible for maintaining the physical infrastructure and its access to the internet, just like in IaaS. In the PaaS model, the cloud provider will also maintain the operating systems, databases, and development tools. Think of PaaS like using a domain joined machine: IT maintains the device with regular updates, patches, and refreshes.

Depending on the configuration, you or the cloud provider may be responsible for networking settings and connectivity within your cloud environment, network and application security, and the directory infrastructure.

<edukamu-image url="/graphics/module1/shared-responsibility-b3829bfe.svg" alt="Diagram showing the responsibilities of the shared responsibility model.">
<br>

#### Use Scenarios
Some common scenarios where PaaS might make sense include:

- Development framework: PaaS provides a framework that developers can build upon to develop or customize cloud-based applications. Similar to the way you create an Excel macro, PaaS lets developers create applications using built-in software components. Cloud features such as scalability, high-availability, and multi-tenant capability are included, reducing the amount of coding that developers must do.

- Analytics or business intelligence: Tools provided as a service with PaaS allow organizations to analyze and mine their data, finding insights and patterns and predicting outcomes to improve forecasting, product design decisions, investment returns, and other business decisions.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Cloud Service 3: Software as a Service (SaaS)
</edukamu-collapse-hidden-title>

Software as a service (SaaS) is the most complete cloud service model from a product perspective. With SaaS, you’re essentially renting or using a fully developed application. Email, financial software, messaging applications, and connectivity software are all common examples of a SaaS implementation.

While the SaaS model may be the least flexible, it’s also the easiest to get up and running. It requires the least amount of technical knowledge or expertise to fully employ.

#### Shared Responsibility Model

The shared responsibility model applies to all the cloud service types. SaaS is the model that places the most responsibility with the cloud provider and the least responsibility with the user. In a SaaS environment you’re responsible for the data that you put into the system, the devices that you allow to connect to the system, and the users that have access. Nearly everything else falls to the cloud provider. The cloud provider is responsible for physical security of the data centers, power, network connectivity, and application development and patching.

<edukamu-image url="/graphics/module1/shared-responsibility-b3829bfe.svg" alt="Diagram showing the responsibilities of the shared responsibility model.">
<br>

#### Use Scenarios

Some common scenarios for SaaS are:

- Email and messaging.

- Business productivity applications.

- Finance and expense tracking.

</edukamu-collapse>

While the preceding sections focus on Microsoft Azure, it's important to acknowledge the vast and diverse landscape of cloud computing. Numerous providers offer a wide array of cloud-based services, often employing similar foundational technologies and architectural principles. 

After this brief introduction, it’s time to start getting to know Azure!

As the name suggests, the platform is developed and managed by Microsoft. Initially released all the way in 2008, Azure has grown and expanded over the years, and, as of 2023, it contains all kinds of services ranging from virtual machinery to website hosting.

If you’ve completed Elements of Cloud and Cybersecurity, also available here on Edukamu, you should be familiar with concepts like cloud, PaaS, and SaaS, which also belong to the Azure portfolio. Please take a moment to review your cloud terminology if you feel uncertain at this point.

But what can you do with Azure, in concrete, you may ask? Get comfy, watch the following video, and find out!

<!-- Tähän video osoitteesta: https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/2-what-microsoft-azure   -->
<iframe width="640" height="360" src="https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed-one-stream.html?id=c27bf1d6-d1b6-410e-a271-e7ae999f2434&locale=en-us&embedUrl=%2Ftraining%2Fmodules%2Fdescribe-core-architectural-components-of-azure%2F2-what-microsoft-azure" frameborder="0" allowfullscreen></iframe>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Benefits of Azure
</edukamu-collapse-hidden-title>

With help from Azure, you have everything you need to build your next great solution. The following lists several of the benefits that Azure provides, so you can easily invent with purpose:

* **Be ready for the future**: Continuous innovation from Microsoft supports your development today and your product visions for tomorrow.
* **Build on your terms**: You have choices. With a commitment to open source, and support for all languages and frameworks, you can build how you want and deploy where you want.
* **Operate hybrid seamlessly**: On-premises, in the cloud, and at the edge, we'll meet you where you are. Integrate and manage your environments with tools and services designed for a hybrid cloud solution.
* **Trust your cloud**: Get security from the ground up, backed by a team of experts, and proactive compliance trusted by enterprises, governments, and startups.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### What Can I Do with Azure?
</edukamu-collapse-hidden-title>

Azure provides more than 100 services that enable you to do everything from running your existing applications on virtual machines to exploring new software paradigms, such as intelligent bots and mixed reality.

Many teams start exploring the cloud by moving their existing applications to virtual machines (VMs) that run in Azure. Migrating your existing apps to VMs is a good start, but the cloud is much more than a different place to run your VMs.

For example, Azure provides artificial intelligence (AI) and machine-learning (ML) services that can naturally communicate with your users through vision, hearing, and speech. It also provides storage solutions that dynamically grow to accommodate massive amounts of data. Azure services enable solutions that aren't feasible without the power of the cloud.

</edukamu-collapse>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### YRITYKSEN NIMI: Career in the Cloud
</edukamu-collapse-hidden-title>

Hello, future data professional! At YRITYS, we work with services like Microsoft Azure every day, solving problems and improving the business of our clients and customers.

Thorough expertise on Microsoft Azure will greatly enhance your future prospects, and companies like ours are always looking for new talents!

On the following video, Nimi Niminen, Ammattinimike at Yritys talks about his/her job and career in the world of data.

VIDEO

If you’re interested in working with us, you can share your details with us after reaching the end of the course! Now, do your best on the course!

</edukamu-collapse>
<br> -->


<edukamu-section class="slate-section slate-blue">
How does it seem? Still a bit blurry? Don’t worry, your vision of Azure will surely get clearer as you advance on this course. 

Before we move forward, take a moment to learn a bit about Azure Accounts. You should also create your own, as it will come handy during this course.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Accounts
</edukamu-collapse-hidden-title>

To create and use Azure services, you need an Azure subscription. When you're working with your own applications and business needs, you need to create an Azure account, and a subscription will be created for you. After you've created an Azure account, you're free to create additional subscriptions. For example, your company might use a single Azure account for your business and separate subscriptions for development, marketing, and sales departments. After you've created an Azure subscription, you can start creating Azure resources within each subscription.

<edukamu-image url="/graphics/module1/azure-accounts.png" alt="Diagram showing the different levels of account scope: Azure account, subscriptions, resource groups and resources." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

If you're new to Azure, you can sign up for a free account on the Azure website to start exploring at no cost to you. When you're ready, you can choose to upgrade your free account. You can also create a new subscription that enables you to start paying for Azure services you need beyond the limits of a free account.

The Azure free account is an excellent way for new users to get started and explore. To sign up, you need a phone number, a credit card, and a Microsoft or GitHub account. The credit card information is used for identity verification only. You won't be charged for any services until you upgrade to a paid subscription.

The Azure free account includes:

* Free access to popular Azure products for 12 months.
* A credit to use for the first 30 days.
* Access to more than 25 products that are always free.

Well, what to do if you want to create an Azure account? You can purchase Azure access directly from Microsoft by signing up on the Azure website or through a Microsoft representative. You can also purchase Azure access through a Microsoft partner. Cloud Solution Provider partners offer a range of complete managed-cloud solutions for Azure.

<!-- Tähän video osoitteesta: https://learn.microsoft.com/en-us/training/modules/describe-core-architectural-components-of-azure/3-get-started-azure-accounts    -->
<iframe width="640" height="360" src="https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed-one-stream.html?id=ac3ad75e-6841-4b66-b3b2-19c85b0e36c3&locale=en-us&embedUrl=%2Ftraining%2Fmodules%2Fdescribe-core-architectural-components-of-azure%2F3-get-started-azure-accounts" frameborder="0" allowfullscreen></iframe>
<br>

</edukamu-collapse>
<br>

All set? Great, let’s move on to Azure infrastructure!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1.png" alt="Edukamu-progress-in-a-module-image">
