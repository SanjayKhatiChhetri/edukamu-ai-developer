## Physical Infrastructure

Excuse me, infrastructure? How is it relevant? What does it mean in this context? These are all good questions that you may be thinking of right now. In short, cloud infrastructure is the collection of hardware and software elements that, once combined, form the platform. Infrastructure components include hardware, such as computing power, and software, like so-called virtualization resources offering emulation capabilities.

First, we’ll focus on the core architectural elements of Azure, often divided into physical infrastructure and management infrastructure.


<edukamu-section class="slate-section slate-blue">
<!-- ### Physical Infrastructure /Sama otsikko toistuu-->

The physical infrastructure for Azure starts with datacenters. Conceptually, the datacenters are the same as large corporate datacenters. They’re facilities with resources arranged in racks, with dedicated power, cooling, and networking infrastructure.

As a global cloud provider, Azure has datacenters around the world. However, these individual datacenters aren’t directly accessible. Datacenters are grouped into Azure Regions or Azure Availability Zones that are designed to help you achieve resiliency and reliability for your business-critical workloads.

The [Global infrastructure](https://datacenters.microsoft.com/globe/explore)(target="_blank") site gives you a chance to interactively explore the underlying Azure infrastructure.

Throughout your journey with Microsoft Azure, you will hear and use terms like Regions, Availability Zones, Resources, Subscriptions, and more. They’re all examples of infrastructure. Next, let’s look at regions and region pairs.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Regions
</edukamu-collapse-hidden-title>

A region is a geographical area on the planet that contains at least one, but potentially multiple datacenters that are nearby and networked together with a low-latency network. Azure intelligently assigns and controls the resources within each region to ensure workloads are appropriately balanced.

When you deploy a resource in Azure, you will often need to choose the region where you want your resource deployed.

**Note**: Some services or virtual machine (VM) features are only available in certain regions, such as specific VM sizes or storage types. 

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Availability Zones
</edukamu-collapse-hidden-title>

Availability zones are physically separate datacenters within an Azure region. Each availability zone is made up of one or more datacenters equipped with independent power, cooling, and networking. An availability zone is set up to be an isolation boundary. If one zone goes down, the other continues working. Availability zones are connected through high-speed, private fiber-optic networks.

<edukamu-image url="/graphics/module1/availability-zones.png" alt="Diagram showing three datacenters connected in a single Azure region representing an availability zone." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

**Important to notice**: To ensure resiliency, a minimum of three separate availability zones are present in all availability zone-enabled regions. However, not all Azure Regions currently support availability zones.

You want to ensure your services and data are redundant so you can protect your information in case of failure. When you host your infrastructure, setting up your own redundancy requires that you create duplicate hardware environments. Azure can help make your app highly available through availability zones.

You can use availability zones to run mission-critical applications and build high-availability into your application architecture by co-locating your compute, storage, networking, and data resources within an availability zone and replicating in other availability zones. Keep in mind that there could be a cost to duplicating your services and transferring data between availability zones.

Availability zones are primarily for VMs, managed disks, load balancers, and SQL databases. Azure services that support availability zones fall into three categories:

* **Zonal services**: You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
* **Zone-redundant services**: The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database).
* **Non-regional services**: Services are always available from Azure geographies and are resilient to zone-wide outages as well as region-wide outages.

Even with the additional resiliency that availability zones provide, it’s possible that an event could be so large that it impacts multiple availability zones in a single region. To provide even further resilience, Azure has Region Pairs.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Region Pairs
</edukamu-collapse-hidden-title>

Most Azure regions are paired with another region within the same geography (such as US, Europe, or Asia) at least 300 miles away. This approach allows for the replication of resources across a geography that helps reduce the likelihood of interruptions because of events such as natural disasters, civil unrest, power outages, or physical network outages that affect an entire region. For example, if a region in a pair was affected by a natural disaster, services would automatically fail over to the other region in its region pair.

**Important**: Not all Azure services automatically replicate data or automatically fall back from a failed region to cross-replicate to another enabled region. In these scenarios, recovery and replication must be configured by the customer.

Examples of region pairs in Azure are West US paired with East US and South-East Asia paired with East Asia. Because the pair of regions are directly connected and far enough apart to be isolated from regional disasters, you can use them to provide reliable services and data redundancy.

<edukamu-image url="/graphics/module1/region-pairs.png" alt="Diagram showing the relationship between geography, region pair, region, and availability zone." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

**Important**: Most directions are paired in two directions, meaning they are the backup for the region that provides a backup for them (West US and East US back each other up). However, some regions, such as West India and Brazil South, are paired in only one direction. In a one-direction pairing, the Primary region does not provide backup for its secondary region. 

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Sovereign Regions
</edukamu-collapse-hidden-title>

In addition to regular regions, Azure also has sovereign regions. Sovereign regions are instances of Azure that are isolated from the main instance of Azure. You may need to use a sovereign region for compliance or legal purposes.

</edukamu-collapse>

Even though cloud services may seem daunting at first, understanding their key concepts and infrastructure makes them easier to understand. We now have a basic understanding of the physical infrastructure of Azure. In the following section, we’ll get familiar with the management.

<br>
<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Azure Basics
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-quiz url="/exercises/module1/physical-infrastructure-text-quiz.yaml" theme="text-quiz-no-answer-colors" id="3363j1d62q2o1do3"/>
<br>

<edukamu-text-quiz url="/exercises/module1/physical-infrastructure-text-quiz-2.yaml" theme="text-quiz-no-answer-colors" id="bxp2vv8p1o7bbd86"/>
<br>

<edukamu-text-quiz url="/exercises/module1/physical-infrastructure-text-quiz-3.yaml" theme="text-quiz-no-answer-colors" id="q687656z9tyneg21"/>
<br>

<edukamu-text-quiz url="/exercises/module1/physical-infrastructure-text-quiz-4.yaml" theme="text-quiz-no-answer-colors" id="lf5126vn5ecdm7n1"/>
<br>

</edukamu-collapse>
<br>

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
