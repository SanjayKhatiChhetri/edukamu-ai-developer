## Managing with Azure Arc

Azure is a highly capable platform that can quickly get complicated without the right tools. That is why it includes a versatile resource manager (ARM, Azure Resource Manager) for all your managing and deployment needs.

Azure Resource Manager (ARM) is the deployment and management service for Azure. It provides a management layer that enables you to create, update, and delete resources in your Azure account. Anytime you do anything with your Azure resources, ARM is involved.

With ARM you can control access, use tags and logs, and modify all your resources in one, unified panel. In essence, ARM is a block of code that defines the infrastructure and configuration of your project. There are multiple templates available, and you can also modify them to create a solution that works for you.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Capabilities of ARM
</edukamu-collapse-hidden-title>

With Azure Resource Manager, you can:

* Manage your infrastructure through declarative templates rather than scripts. A Resource Manager template is a JSON file that defines what you want to deploy to Azure.
* Deploy, manage, and monitor all the resources for your solution as a group, rather than handling these resources individually.
* Re-deploy your solution throughout the development life-cycle and have confidence your resources are deployed in a consistent state.
* Define the dependencies between resources, so they're deployed in the correct order.
* Apply access control to all services because RBAC is natively integrated into the management platform.
* Apply tags to resources to logically organize all the resources in your subscription.
* Clarify your organization's billing by viewing costs for a group of resources that share the same tag.

The following video provides an overview of how you can use different Azure tools with ARM to manage your environment:

<!-- Tähän video osoitteesta: https://learn.microsoft.com/en-us/training/modules/describe-features-tools-manage-deploy-azure-resources/4-describe-azure-resource-manager-azure-arm-templates      -->
<iframe width="640" height="360" src="https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed-one-stream.html?id=d257e6ec-abab-47f4-a209-22049e7a40b4&locale=en-us&embedUrl=%2Ftraining%2Fmodules%2Fdescribe-features-tools-manage-deploy-azure-resources%2F4-describe-azure-resource-manager-azure-arm-templates" frameborder="0" allowfullscreen></iframe>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### ARM Templates
</edukamu-collapse-hidden-title>

Infrastructure as code is a concept where you manage your infrastructure as lines of code. Leveraging Azure Cloud Shell, Azure PowerShell, or the Azure CLI are some examples of using code to deploy cloud infrastructure. ARM templates are another example of infrastructure as code at work.

By using ARM templates, you can describe the resources you want to use in a declarative JSON format. With an ARM template, the deployment code is verified before any code is run. This ensures that the resources will be created and connected correctly. The template then orchestrates the creation of those resources in parallel. That is, if you need 50 instances of the same resource, all 50 instances are created at the same time.

Ultimately, the developer, DevOps professional, or IT professional needs only to define the desired state and configuration of each resource in the ARM template, and the template does the rest. Templates can even execute PowerShell and Bash scripts before or after the resource has been set up.

</edukamu-collapse>

</edukamu-collapse>


But what about scenarios in which you have multiple projects? What if you need to connect on-premises resources to the cloud in a so-called hybrid environment? That’s where the previously mentioned Azure Arc comes to play.

<edukamu-section class="slate-section slate-blue">
In utilizing Azure Resource Manager (ARM), Arc lets you extend your Azure compliance and monitoring to your hybrid and multi-cloud configurations. Azure Arc simplifies governance and management by delivering a consistent multi-cloud and on-premises management platform.

Azure Arc provides a centralized, unified way to:

* manage your entire environment together by projecting your existing non-Azure resources into ARM.
* manage multi-cloud and hybrid virtual machines, Kubernetes clusters, and databases as if they are running in Azure.
* use familiar Azure services and management capabilities, regardless of where they live.
* continue using traditional ITOps while introducing DevOps practices to support new cloud and native patterns in your environment.
* configure custom locations as an abstraction layer on top of Azure Arc-enabled Kubernetes clusters and cluster extensions.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### What Can Azure Arc Do Outside of Azure?
</edukamu-collapse-hidden-title>

Currently, Azure Arc allows you to manage the following resource types hosted outside of Azure:

* Servers
* Kubernetes clusters
* Azure data services
* SQL Server
* Virtual machines (preview).

</edukamu-collapse>

As you can see, there are many tools specifically designed to help you manage projects and resources. You will surely get to use them in the future if you ever work with Azure!
<br>
<br>
You’re going strong, keep at it! Now that we have an understanding of project management on Azure, we can move on to governance. How do you govern projects that grow beyond just one subscription? How can you scale the resources? What about testing environments? Let’s move on an find out!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
