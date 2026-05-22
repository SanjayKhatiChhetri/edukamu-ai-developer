# Course 1: Exploring Microsoft Azure

**URL:** [https://cs.edukamu.fi/exploring-azure](https://cs.edukamu.fi/exploring-azure)  
**Sections:** 15  

---

## Table of Contents

- **Unit 1:** Basics Of Azure | Computing Service | Management Infrastructure ...
- **Unit 2:** Authentication And Authorization | Azure Storage | Conditional Access ...
- **Unit 3:** Cost Management | Governance And Compliance | Managing With Azure Arc ...

---

## Unit 1

### Basics Of Azure

**TL;DR:** <edukamu-video content="/videos/devai-1-unit1-video.yaml"/>
<br>

**Topics covered:**
- Video: Why Study Azure Fundamentals?
- Transcription: Why study Azure Fundamentals?
- Service Type 1: Infrastructure as a Service (IaaS)
- Cloud Service 2: Platform as a Service (PaaS)
- Cloud Service 3: Software as a Service (SaaS)
- Benefits of Azure
- What Can I Do with Azure?
- YRITYKSEN NIMI: Career in the Cloud
- Azure Accounts

**Key Terms:**

| Term | Definition |
|------|-----------|
| Be ready for the future | Continuous innovation from Microsoft supports your development today and your product visions for tomorrow. |
| Build on your terms | You have choices. With a commitment to open source, and support for all languages and frameworks, you can build how you want and deploy where you want. |
| Operate hybrid seamlessly | On-premises, in the cloud, and at the edge, we'll meet you where you are. Integrate and manage your environments with tools and services designed for a hybrid cloud solution. |
| Trust your cloud | Get security from the ground up, backed by a team of experts, and proactive compliance trusted by enterprises, governments, and startups. |

**Key Points:**
- Lift-and-shift migration: You’re setting up cloud resources similar to your on-prem datacenter, and then simply moving the things running on-prem to running on the IaaS infrastructure.
- Testing and development: You have established configurations for development and test environments that you need to rapidly replicate. You can start up or shut down the different environments rapidly...
- Development framework: PaaS provides a framework that developers can build upon to develop or customize cloud-based applications. Similar to the way you create an Excel macro, PaaS lets developers...
- Analytics or business intelligence: Tools provided as a service with PaaS allow organizations to analyze and mine their data, finding insights and patterns and predicting outcomes to improve...
- Business productivity applications.
- Be ready for the future: Continuous innovation from Microsoft supports your development today and your product visions for tomorrow.
- Build on your terms: You have choices. With a commitment to open source, and support for all languages and frameworks, you can build how you want and deploy where you want.
- Operate hybrid seamlessly: On-premises, in the cloud, and at the edge, we'll meet you where you are. Integrate and manage your environments with tools and services designed for a hybrid cloud...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Computing Service

**TL;DR:** In this page, you will be introduced to the computing services of Azure. Our focus will be on three such services, namely virtual machines, containers, and Azure functions.

**Topics covered:**
- Azure Virtual Machines
- Azure Virtual Desktop
- Azure Containers
- Azure Functions
- Azure App Service
- Exercise: Computing on Azure

**Key Terms:**

| Term | Definition |
|------|-----------|
| When extending your datacenter to the cloud | An organization can extend the capabilities of its own on-premises network by creating a virtual network in Azure and adding VMs to that virtual network. Applications like... |
| During disaster recovery | As with running certain types of applications in the cloud and extending an on-premises network to the cloud, you can get significant cost savings by using an IaaS-based approach... |

**Key Points:**
- Total control over the operating system (OS).
- The ability to run custom software.
- To use custom hosting configurations.
- During testing and development. VMs provide a quick and easy way to create different OS and application configurations. Test and development personnel can then easily delete the VMs when they no...
- When running applications in the cloud. The ability to run certain applications in the public cloud as opposed to creating a traditional infrastructure to run them can provide substantial economic...
- When extending your datacenter to the cloud: An organization can extend the capabilities of its own on-premises network by creating a virtual network in Azure and adding VMs to that virtual network....
- During disaster recovery: As with running certain types of applications in the cloud and extending an on-premises network to the cloud, you can get significant cost savings by using an IaaS-based...
- Deployment and management are integrated into the platform.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Management Infrastructure

**TL;DR:** While physical infrastructure is quite concrete and therefore simple on the surface, the management infrastructure is a little bit more abstract. It includes Azure resources and resource groups, subscriptions, and accounts. Understanding the hierarchical organization will help you plan your projects and products within Azure.

**Topics covered:**
- Azure Resources and Resource Groups
- Azure Management Groups
- Management Group and Subscription Hierarchy

**Key Points:**
- Create a hierarchy that applies a policy. You could limit VM locations to the US West Region in a group called Production. This policy will inherit onto all the subscriptions that are descendants of...
- Provide user access to multiple subscriptions. By moving multiple subscriptions under a management group, you can create one Azure role-based access control (Azure RBAC) assignment on the management...
- 10,000 management groups can be supported in a single directory.
- A management group tree can support up to six levels of depth. This limit doesn't include the root level or the subscription level.
- Each management group and subscription can support only one parent.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Physical Infrastructure

**TL;DR:** Excuse me, infrastructure? How is it relevant? What does it mean in this context? These are all good questions that you may be thinking of right now. In short, cloud infrastructure is the collection of hardware and software elements that, once combined, form the platform. Infrastructure components include hardware, such as computing power, and soft...

**Topics covered:**
- Regions
- Availability Zones
- Region Pairs
- Sovereign Regions
- Exercise: Azure Basics

**Key Terms:**

| Term | Definition |
|------|-----------|
| Note | Some services or virtual machine (VM) features are only available in certain regions, such as specific VM sizes or storage types. |
| Important to notice | To ensure resiliency, a minimum of three separate availability zones are present in all availability zone-enabled regions. However, not all Azure Regions currently support... |
| Zonal services | You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses). |
| Zone-redundant services | The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database). |
| Non-regional services | Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages. |
| Important | Not all Azure services automatically replicate data or automatically fall back from a failed region to cross-replicate to another enabled region. In these scenarios, recovery and... |
| Important | Most directions are paired in two directions, meaning they are the backup for the region that provides a backup for them (West US and East US back each other up). However, some... |

**Key Points:**
- Zonal services: You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
- Zone-redundant services: The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database).
- Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Virtual Networking

**TL;DR:** Azure virtual networks and virtual subnets enable Azure resources, such as the previously discussed virtual machines or VMs, web apps, and databases, to communicate with each other, with users on the internet, and with your on-premises client computers. You can think of an Azure network as an extension of your on-premises network with resources tha...

**Topics covered:**
- Azure Virtual Private Networks
- VPN gateways
- Azure ExpressRoute
- Azure DNS
- Exercise: Knowledge Check 1

**Key Terms:**

| Term | Definition |
|------|-----------|
| Important | You can't use Azure DNS to buy a domain name. For an annual fee, you can buy a domain name by using App Service domains or a third-party domain name registrar. Once purchased,... |

**Key Points:**
- communicating between Azure resources
- communicating with on-premises resources
- Public endpoints have a public IP address and can be accessed from anywhere in the world.
- Private endpoints exist within a virtual network and have a private IP address from within the address space of that virtual network.
- Connect on-premises datacenters to virtual networks through a site-to-site connection.
- Connect individual devices to virtual networks through a point-to-site connection.
- Connect virtual networks to other virtual networks through a network-to-network connection.
- Policy-based VPN gateways specify statically the IP address of packets that should be encrypted through each tunnel. This type of device evaluates every data packet against those sets of IP addresses...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 2

### Authentication And Authorization

**TL;DR:** Azure makes sure that only authorized people have access to the stored data. That’s not all, though, as Azure’s authorization and authentication practices in place go well beyond.

**Topics covered:**
- Secure Login with Azure AD
- Who Can Use Azure AD?
- What Services Does Azure AD Offer?
- Azure Authentication Methods
- Passwordless Authentication
- Exercise: Storage and Safety

**Key Terms:**

| Term | Definition |
|------|-----------|
| Authentication | This includes verifying identity to access applications and resources. It also includes providing functionality such as self-service password reset, multifactor authentication, a... |
| Single sign-on | Single sign-on (SSO) enables you to remember only one username and one password to access multiple applications. A single identity is tied to a user, which simplifies the security... |
| Application management | You can manage your cloud and on-premises apps by using Azure AD. Features like Application Proxy, SaaS apps, the My Apps portal, and single sign-on provide a better user... |
| Device management | Along with accounts for individual people, Azure AD supports the registration of devices. Registration enables devices to be managed through tools like Microsoft Intune. It also... |

**Key Points:**
- IT administrators. Administrators can use Azure AD to control access to applications and resources based on their business requirements.
- App developers. Developers can use Azure AD to provide a standards-based approach for adding functionality to applications that they build, such as adding SSO functionality to an app or enabling an...
- Users. Users can manage their identities and take maintenance actions like self-service password reset.
- Online service subscribers. Microsoft 365, Microsoft Office 365, Azure, and Microsoft Dynamics CRM Online subscribers are already using Azure AD to authenticate into their account.
- Authentication: This includes verifying identity to access applications and resources. It also includes providing functionality such as self-service password reset, multifactor authentication, a...
- Single sign-on: Single sign-on (SSO) enables you to remember only one username and one password to access multiple applications. A single identity is tied to a user, which simplifies the security...
- Application management: You can manage your cloud and on-premises apps by using Azure AD. Features like Application Proxy, SaaS apps, the My Apps portal, and single sign-on provide a better user...
- Device management: Along with accounts for individual people, Azure AD supports the registration of devices. Registration enables devices to be managed through tools like Microsoft Intune. It also...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Azure Storage

**TL;DR:** <edukamu-video content="/videos/devai-1-unit2-video.yaml"/>
<br>

**Topics covered:**
- YRITYS: Scenarios from Real Life
- Azure Storage Redundancy
- 1. Redundancy in the primary region
- 2. Redundancy in a secondary region

**Key Points:**
- How your data is replicated in the primary region.
- Whether your data is replicated to a second region that is geographically distant to the primary region, to protect against regional disasters.
- Whether your application requires read access to the replicated data in the secondary region if the primary region becomes unavailable.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Conditional Access

**TL;DR:** Conditional Access is a tool that Azure Active Directory uses to allow (or deny) access to resources based on identity signals. These signals include who the user is, where the user is, and what device the user is requesting access from.

**Topics covered:**
- When to Use Conditional Access?
- Azure External Identities
- Role-based Access Control
- How is Role-based Access Control Applied to Resources?
- How is Azure RBAC Enforced?
- Practice: Azure Services
- Exercise: Knowledge Check 2
- YRITYS: Taking it a Step Further

**Key Points:**
- empower users to be productive wherever and whenever
- protect the organization's assets.
- require multifactor authentication (MFA) to access an application depending on the requester’s role, location, or network. For example, you could require MFA for administrators but not regular users...
- require access to services only through approved client applications. For example, you could limit which email applications are able to connect to your email service.
- require users to access your application only from managed devices. A managed device is a device that meets your standards for security and compliance.
- lock access from untrusted sources, such as access from unknown or unexpected locations.
- A management group (a collection of multiple subscriptions).
- When you assign the Owner role to a user at the management group scope, that user can manage everything in all subscriptions within the management group.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Data Migration

**TL;DR:** In addition to keeping your data safe and accessible, Azure also helps you bring your existing data over from different services. It’s easy to migrate to Azure, as you will soon find out.

**Topics covered:**
- Azure Migrate
- Azure Data Box
- AzCopy
- Azure Storage Explorer
- Azure File Sync

**Key Terms:**

| Term | Definition |
|------|-----------|
| Unified migration platform | A single portal to start, run, and track your migration to Azure. |
| Range of tools | A range of tools for assessment and migration. Azure Migrate tools include Azure Migrate: Discovery and assessment and Azure Migrate: Server Migration. Azure Migrate also... |
| Assessment and migration | In the Azure Migrate hub, you can assess and migrate your on-premises infrastructure to Azure. |
| Important | Synchronizing blobs or files with AzCopy is one-direction synchronization. When you synchronize, you designated the source and destination, and AzCopy will copy files or blobs in... |

**Key Points:**
- Unified migration platform: A single portal to start, run, and track your migration to Azure.
- Range of tools: A range of tools for assessment and migration. Azure Migrate tools include Azure Migrate: Discovery and assessment and Azure Migrate: Server Migration. Azure Migrate also integrates...
- Assessment and migration: In the Azure Migrate hub, you can assess and migrate your on-premises infrastructure to Azure.
- use any protocol that's available on Windows Server to access your data locally, including SMB, NFS, and FTPS.
- have as many caches as you need across the world.
- replace a failed local server by installing Azure File Sync on a new server in the same datacenter.
- configure cloud tiering so the most frequently accessed files are replicated locally, while infrequently accessed files are kept in the cloud until requested.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Storage Services

**TL;DR:** As you just learned, Azure can also take care of all your data storage needs. The data is kept safe and secure, but easily accessible for you and your colleagues. In this section we’ll learn more about Azure Storage and the services it provides.

**Topics covered:**
- Blob Storage
- Accessing Blob Storage
- Azure Files
- Queue Storage
- Disk Storage

**Key Terms:**

| Term | Definition |
|------|-----------|
| Shared access | Azure file shares support the industry standard SMB and NFS protocols, meaning you can seamlessly replace your on-premises file shares with Azure file shares without worrying... |
| Fully managed | Azure file shares can be created without the need to manage hardware or an OS. This means you don't have to deal with patching the server OS with critical security upgrades or... |
| Scripting and tooling | PowerShell cmdlets and Azure CLI can be used to create, mount, and manage Azure file shares as part of the administration of Azure applications. You can create and manage Azure... |
| Resiliency | Azure Files has been built from the ground up to always be available. Replacing on-premises file shares with Azure Files means you don't have to wake up in the middle of the night... |
| Familiar programmability | Applications running in Azure can access data in the share via file system I/O APIs. Developers can therefore leverage their existing code and skills to migrate existing... |

**Key Points:**
- Durability and availability. Redundancy ensures that your data is safe if transient hardware failures occur. You can also opt to replicate data across data centers or geographical regions for...
- Security. All data written to an Azure storage account is encrypted by the service. Azure Storage provides you with fine-grained control over who has access to your data.
- Scalability. Azure Storage is designed to be massively scalable to meet the data storage and performance needs of today's applications.
- Manageability. Azure handles hardware maintenance, updates, and critical issues for you.
- Accessibility. Data in Azure Storage is accessible from anywhere in the world over HTTP or HTTPS. Microsoft provides client libraries for Azure Storage in a variety of languages, including .NET,...
- Serving images or documents directly to a browser.
- Storing files for distributed access.
- Storing data for backup and restore, disaster recovery, and archiving.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 3

### Cost Management

**TL;DR:** Managing costs is vital for every enterprise, no matter how great or small. With its cloud-based, hassle-free services, Azure has the potential to help you save large sums of money, and soon you will know how.

**Topics covered:**
- What is Cost Management?
- Cost Alerts
- Budgets
- Resource Tags
- Managing Resource Tags
- Practice: Projects and Costs
- Exercise: Knowledge Check 3

**Key Terms:**

| Term | Definition |
|------|-----------|
| Budget alerts | Budget alerts notify you when spending, based on usage or cost, reaches or exceeds the amount defined in the alert condition of the budget. |
| Credit alerts | Credit alerts notify you when your Azure credit monetary commitments are consumed. |
| Department spending quota alerts | Department spending quota alerts notify you when department spending reaches a fixed threshold of the quota. |
| Resource management | Tags enable you to locate and act on resources that are associated with specific workloads, environments, business units, and owners. |
| Cost management and optimization | Tags enable you to group resources so that you can report on costs, allocate internal cost centers, track budgets, and forecast estimated cost. |
| Operations management | Tags enable you to group resources according to how critical their availability is to your business. This grouping helps you formulate service-level agreements (SLAs). An SLA is... |
| Security | Tags enable you to classify data by its security level, such as public or confidential. |
| Governance and regulatory compliance | Tags enable you to identify resources that align with governance or regulatory compliance requirements, such as ISO 27001. Tags can also be part of your standards enforcement... |
| Workload optimization and automation | Tags can help you visualize all of the resources that participate in complex deployments. For example, you might tag a resource with its associated workload or application name... |

**Key Points:**
- Budget alerts: Budget alerts notify you when spending, based on usage or cost, reaches or exceeds the amount defined in the alert condition of the budget.
- Credit alerts: Credit alerts notify you when your Azure credit monetary commitments are consumed.
- Department spending quota alerts: Department spending quota alerts notify you when department spending reaches a fixed threshold of the quota.
- Resource management Tags enable you to locate and act on resources that are associated with specific workloads, environments, business units, and owners.
- Cost management and optimization Tags enable you to group resources so that you can report on costs, allocate internal cost centers, track budgets, and forecast estimated cost.
- Operations management Tags enable you to group resources according to how critical their availability is to your business. This grouping helps you formulate service-level agreements (SLAs). An SLA is...
- Security Tags enable you to classify data by its security level, such as public or confidential.
- Governance and regulatory compliance Tags enable you to identify resources that align with governance or regulatory compliance requirements, such as ISO 27001. Tags can also be part of your standards...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Governance And Compliance

**TL;DR:** Let’s imagine you’re running a project on Azure. It all goes well – you have your resources in place, data secured, and a few motivated employees working with you towards the same goals. Actually, it’s going so well that you will soon find yourself in a situation in which you have to expand the project.

**Topics covered:**
- Azure Blueprints
- Azure Blueprints and Deployments
- Azure Policy and Initiatives
- Azure Policy Initiatives
- Azure Resource Lock
- Managing Resource Locks
- Modifying Resources
- Service Trust Portal
- Azure Advisor
- Azure Service Health

**Key Terms:**

| Term | Definition |
|------|-----------|
| Reliability | is used to ensure and improve the continuity of your business-critical applications. |
| Security | is used to detect threats and vulnerabilities that might lead to security breaches. |
| Performance | is used to improve the speed of your applications. |
| Operational Excellence | is used to help you achieve process and workflow efficiency, resource manageability, and deployment best practices. |
| Cost | is used to optimize and reduce your overall Azure spending. |
| Azure Status | is a broad picture of the status of Azure globally. Azure status informs you of service outages in Azure on the Azure Status page. The page is a global view of the health of all... |
| Service Health | provides a narrower view of Azure services and regions. It focuses on the Azure services and regions you're using. This is the best place to look for service impacting... |
| Resource Health | is a tailored view of your actual Azure resources. It provides information about the health of your individual cloud resources, such as a specific virtual machine instance. Using... |

**Key Points:**
- Delete means authorized users can still read and modify a resource, but they can't delete the resource.
- ReadOnly means authorized users can read a resource, but they can't delete or update the resource. Applying this lock is similar to restricting all authorized users to the permissions granted by the...
- Reliability is used to ensure and improve the continuity of your business-critical applications.
- Security is used to detect threats and vulnerabilities that might lead to security breaches.
- Performance is used to improve the speed of your applications.
- Operational Excellence is used to help you achieve process and workflow efficiency, resource manageability, and deployment best practices.
- Cost is used to optimize and reduce your overall Azure spending.
- Azure Status is a broad picture of the status of Azure globally. Azure status informs you of service outages in Azure on the Azure Status page. The page is a global view of the health of all Azure...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Managing With Azure Arc

**TL;DR:** Azure is a highly capable platform that can quickly get complicated without the right tools. That is why it includes a versatile resource manager (ARM, Azure Resource Manager) for all your managing and deployment needs.

**Topics covered:**
- Capabilities of ARM
- ARM Templates
- What Can Azure Arc Do Outside of Azure?

**Key Points:**
- Manage your infrastructure through declarative templates rather than scripts. A Resource Manager template is a JSON file that defines what you want to deploy to Azure.
- Deploy, manage, and monitor all the resources for your solution as a group, rather than handling these resources individually.
- Re-deploy your solution throughout the development life-cycle and have confidence your resources are deployed in a consistent state.
- Define the dependencies between resources, so they're deployed in the correct order.
- Apply access control to all services because RBAC is natively integrated into the management platform.
- Apply tags to resources to logically organize all the resources in your subscription.
- Clarify your organization's billing by viewing costs for a group of resources that share the same tag.
- manage your entire environment together by projecting your existing non-Azure resources into ARM.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Project Management In Azure

**TL;DR:** <edukamu-video content="/videos/devai-1-unit3-video.yaml"/>
<br>

**Topics covered:**
- Sovelto Eduhouse: Career in the Cloud
- Azure Portal
- Alternative: Azure Cloud Shell
- Alternative: Azure PowerShell?
- Azure CLI

**Key Points:**
- build, manage, and monitor everything from simple web apps to complex cloud deployments
- create custom dashboards for an organized view of resources
- configure accessibility options for an optimal experience.
- It is a browser-based shell experience, with no local installation or configuration required.
- It is authenticated to your Azure credentials, so when you log in it inherently knows who you are and what permissions you have.
- You choose the shell you’re most familiar with; Azure Cloud Shell supports both Azure PowerShell and the Azure CLI (which uses Bash).
- The routine setup, teardown, and maintenance of a single resource or multiple connected resources.
- The deployment of an entire infrastructure, which might contain dozens or hundreds of resources, from imperative code.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Summary

**TL;DR:** Congratulations on reaching the summary of the Exploring Microsoft Azure course!

**Topics covered:**
- Conversation: Representing the World with Azure
- Unit 1: Introduction to Azure
- Unit 2: Data, Storage, and Safety
- Unit 3: Governance and Cost Management
- Course Feedback

**Key Points:**
- How would you describe Azure in a few sentences?
- Can you describe the infrastructure of Azure?
- What are VMs? Why are they useful?
- What services does Azure Storage offer?
- How does Azure keep your data safe?
- What is the meaning of conditional access?
- What can you do with Azure Portal?
- How can Azure Arc help you manage projects?

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Quick-Reference Glossary

| Term | Definition | Section |
|------|-----------|---------|
| Be ready for the future | Continuous innovation from Microsoft supports your development today and your product visions for tomorrow. | Basics Of Azure |
| Build on your terms | You have choices. With a commitment to open source, and support for all languages and frameworks, you can build how you want and deploy where you want. | Basics Of Azure |
| Operate hybrid seamlessly | On-premises, in the cloud, and at the edge, we'll meet you where you are. Integrate and manage your environments with tools and services designed for a hybrid cloud solution. | Basics Of Azure |
| Trust your cloud | Get security from the ground up, backed by a team of experts, and proactive compliance trusted by enterprises, governments, and startups. | Basics Of Azure |
| When extending your datacenter to the cloud | An organization can extend the capabilities of its own on-premises network by creating a virtual network in Azure and adding VMs to that virtual network. Applications like... | Computing Service |
| During disaster recovery | As with running certain types of applications in the cloud and extending an on-premises network to the cloud, you can get significant cost savings by using an IaaS-based approach... | Computing Service |
| Note | Some services or virtual machine (VM) features are only available in certain regions, such as specific VM sizes or storage types. | Physical Infrastructure |
| Important to notice | To ensure resiliency, a minimum of three separate availability zones are present in all availability zone-enabled regions. However, not all Azure Regions currently support... | Physical Infrastructure |
| Zonal services | You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses). | Physical Infrastructure |
| Zone-redundant services | The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database). | Physical Infrastructure |
| Non-regional services | Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages. | Physical Infrastructure |
| Important | Not all Azure services automatically replicate data or automatically fall back from a failed region to cross-replicate to another enabled region. In these scenarios, recovery and... | Physical Infrastructure |
| Authentication | This includes verifying identity to access applications and resources. It also includes providing functionality such as self-service password reset, multifactor authentication, a... | Authentication And Authorization |
| Single sign-on | Single sign-on (SSO) enables you to remember only one username and one password to access multiple applications. A single identity is tied to a user, which simplifies the security... | Authentication And Authorization |
| Application management | You can manage your cloud and on-premises apps by using Azure AD. Features like Application Proxy, SaaS apps, the My Apps portal, and single sign-on provide a better user... | Authentication And Authorization |
| Device management | Along with accounts for individual people, Azure AD supports the registration of devices. Registration enables devices to be managed through tools like Microsoft Intune. It also... | Authentication And Authorization |
| Unified migration platform | A single portal to start, run, and track your migration to Azure. | Data Migration |
| Range of tools | A range of tools for assessment and migration. Azure Migrate tools include Azure Migrate: Discovery and assessment and Azure Migrate: Server Migration. Azure Migrate also... | Data Migration |
| Assessment and migration | In the Azure Migrate hub, you can assess and migrate your on-premises infrastructure to Azure. | Data Migration |
| Shared access | Azure file shares support the industry standard SMB and NFS protocols, meaning you can seamlessly replace your on-premises file shares with Azure file shares without worrying... | Storage Services |
| Fully managed | Azure file shares can be created without the need to manage hardware or an OS. This means you don't have to deal with patching the server OS with critical security upgrades or... | Storage Services |
| Scripting and tooling | PowerShell cmdlets and Azure CLI can be used to create, mount, and manage Azure file shares as part of the administration of Azure applications. You can create and manage Azure... | Storage Services |
| Resiliency | Azure Files has been built from the ground up to always be available. Replacing on-premises file shares with Azure Files means you don't have to wake up in the middle of the night... | Storage Services |
| Familiar programmability | Applications running in Azure can access data in the share via file system I/O APIs. Developers can therefore leverage their existing code and skills to migrate existing... | Storage Services |
| Budget alerts | Budget alerts notify you when spending, based on usage or cost, reaches or exceeds the amount defined in the alert condition of the budget. | Cost Management |
| Credit alerts | Credit alerts notify you when your Azure credit monetary commitments are consumed. | Cost Management |
| Department spending quota alerts | Department spending quota alerts notify you when department spending reaches a fixed threshold of the quota. | Cost Management |
| Resource management | Tags enable you to locate and act on resources that are associated with specific workloads, environments, business units, and owners. | Cost Management |
| Cost management and optimization | Tags enable you to group resources so that you can report on costs, allocate internal cost centers, track budgets, and forecast estimated cost. | Cost Management |
| Operations management | Tags enable you to group resources according to how critical their availability is to your business. This grouping helps you formulate service-level agreements (SLAs). An SLA is... | Cost Management |
| Security | Tags enable you to classify data by its security level, such as public or confidential. | Cost Management |
| Governance and regulatory compliance | Tags enable you to identify resources that align with governance or regulatory compliance requirements, such as ISO 27001. Tags can also be part of your standards enforcement... | Cost Management |
| Workload optimization and automation | Tags can help you visualize all of the resources that participate in complex deployments. For example, you might tag a resource with its associated workload or application name... | Cost Management |
| Reliability | is used to ensure and improve the continuity of your business-critical applications. | Governance And Compliance |
| Performance | is used to improve the speed of your applications. | Governance And Compliance |
| Operational Excellence | is used to help you achieve process and workflow efficiency, resource manageability, and deployment best practices. | Governance And Compliance |
| Cost | is used to optimize and reduce your overall Azure spending. | Governance And Compliance |
| Azure Status | is a broad picture of the status of Azure globally. Azure status informs you of service outages in Azure on the Azure Status page. The page is a global view of the health of all... | Governance And Compliance |
| Service Health | provides a narrower view of Azure services and regions. It focuses on the Azure services and regions you're using. This is the best place to look for service impacting... | Governance And Compliance |
| Resource Health | is a tailored view of your actual Azure resources. It provides information about the health of your individual cloud resources, such as a specific virtual machine instance. Using... | Governance And Compliance |

---

*Auto-generated by `generate_diary.py` — re-run to refresh after re-scraping.*
