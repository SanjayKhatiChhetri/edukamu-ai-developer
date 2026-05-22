## Cost Management

Managing costs is vital for every enterprise, no matter how great or small. With its cloud-based, hassle-free services, Azure has the potential to help you save large sums of money, and soon you will know how.

This is the last topic of this course, so keep on going!

Let’s start by watching the following video.

<!-- Tähän video osoitteesta: https://learn.microsoft.com/en-us/training/modules/describe-cost-management-azure/2-describe-factors-affect-costs-azure?ns-enrollment-type=learningpath&ns-enrollment-id=learn.wwl.describe-azure-management-governance      -->
<iframe width="640" height="360" src="https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed-one-stream.html?id=ef760ebd-b3c1-44d8-9628-2b54c45fcbfe&locale=en-us&embedUrl=%2Ftraining%2Fmodules%2Fdescribe-cost-management-azure%2F2-describe-factors-affect-costs-azure" frameborder="0" allowfullscreen></iframe>
<br>

Azure shifts development costs from the capital expense (CapEx) of building out and maintaining infrastructure and facilities to an operational expense (OpEx) of renting infrastructure as you need it, whether it’s compute, storage, networking, or something entirely different.

<edukamu-flashcard url="/exercises/module3/cost-management-flashcard.yaml" id="9sx7n9rdz1arbp7u" />
<br>

<edukamu-section class="slate-section slate-blue">
### What is Cost Management?

Cost Management provides the ability to quickly check Azure resource costs, create alerts based on resource spend, and create budgets that can be used to automate management of resources.

Cost analysis is a subset of Cost Management that provides a quick visual for your Azure costs. Using cost analysis, you can quickly view the total cost in a variety of different ways, including by billing cycle, region, resource, and so on.

<edukamu-image url="/graphics/module3/cost-analysis.png" alt="Screenshot of initial view of cost analysis in the Azure portal." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>

</edukamu-section>
<br>

You use cost analysis to explore and analyze your organizational costs. You can view aggregated costs by organization to understand where costs are accrued and to identify spending trends. And you can see accumulated costs over time to estimate monthly, quarterly, or even yearly cost trends against a budget.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Cost Alerts
</edukamu-collapse-hidden-title>

Cost alerts provide a single location to quickly check on all of the different alert types that may show up in the Cost Management service. The three types of alerts that may show up are:

* **Budget alerts**: Budget alerts notify you when spending, based on usage or cost, reaches or exceeds the amount defined in the alert condition of the budget. 
* **Credit alerts**: Credit alerts notify you when your Azure credit monetary commitments are consumed. 
* **Department spending quota alerts**: Department spending quota alerts notify you when department spending reaches a fixed threshold of the quota. 

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Budgets
</edukamu-collapse-hidden-title>

A budget is where you set a spending limit for Azure. You can set budgets based on a subscription, resource group, service type, or other criteria. When you set a budget, you will also set a budget alert. When the budget hits the budget alert level, it will trigger a budget alert that shows up in the cost alerts area. If configured, budget alerts will also send an email notification that a budget alert threshold has been triggered. 

</edukamu-collapse>
<br>

### Resource Tags

As your cloud usage grows, it's increasingly important to stay organized. A good organization strategy helps you understand your cloud usage and can help you manage costs.

One way to organize related resources is to place them in their own subscriptions. You can also use resource groups to manage related resources. Resource tags are another way to organize resources. Tags provide extra information, or metadata, about your resources. This metadata is useful for:

* **Resource management** Tags enable you to locate and act on resources that are associated with specific workloads, environments, business units, and owners.
* **Cost management and optimization** Tags enable you to group resources so that you can report on costs, allocate internal cost centers, track budgets, and forecast estimated cost.
* **Operations management** Tags enable you to group resources according to how critical their availability is to your business. This grouping helps you formulate service-level agreements (SLAs). An SLA is an uptime or performance guarantee between you and your users.
* **Security** Tags enable you to classify data by its security level, such as public or confidential.
* **Governance and regulatory compliance** Tags enable you to identify resources that align with governance or regulatory compliance requirements, such as ISO 27001. Tags can also be part of your standards enforcement efforts. For example, you might require that all resources be tagged with an owner or department name.
* **Workload optimization and automation** Tags can help you visualize all of the resources that participate in complex deployments. For example, you might tag a resource with its associated workload or application name and use software such as Azure DevOps to perform automated tasks on those resources.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Managing Resource Tags
</edukamu-collapse-hidden-title>

You can add, modify, or delete resource tags through Windows PowerShell, the Azure CLI, Azure Resource Manager templates, the REST API, or the Azure portal.

You can use Azure Policy to enforce tagging rules and conventions. For example, you can require that certain tags be added to new resources as they're provisioned. You can also define rules that reapply tags that have been removed. Tags aren’t inherited, meaning that you can apply tags one level and not have those tags automatically show up at a different level, allowing you to create custom tagging schemas that change depending on the level (resource, resource group, subscription, and so on).

</edukamu-collapse>

<edukamu-section class="slate-section slate-blue">
How does it seem? Azure has many tools to help you and your company save money – whether it be managing costs or effective planning, there’s a service available for you.

Next, you will get to plan a little. You will take on the role of a manager trying to get work done as productively as possible while remaining cost-effective. Afterwards, it's time for the third and final knowledge check of this course!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Projects and Costs
</edukamu-collapse-hidden-title>

In this practical exercise, you will assume the role of a beginning project manager. You’ve decided to move your project to Azure, but you will still have to sell your idea to your supervisor. 

Your company is creating applications for customers interested in healthy nutrition, and you oversee the development of a brand-new web abb that’s currently in development. You’re a team of 10 professionals, and you will need the following services to operate smoothly:

* storage
* analysis
* security.

Alternatively, you can also make a plan for your own personal/professional needs.

Use your newly gained knowledge and decide which Azure services you could use. You will find more information from the following sources:

* [Azure Cloud Computing Services](https://azure.microsoft.com/en-us)(target="_blank")
* [Azure Products and Pricing](https://azure.microsoft.com/en-us/pricing/#product-pricing)(target="_blank")

Find out as much as you can about the monthly/yearly costs of running the needed Azure services for your team. Write a summary of your cost management plan and submit it to the Edukamu platform.

The goal for this exercise is to gain practical knowledge on the costs of running Azure services. Try to make the plan as concrete as possible, as it may come in handy later.

<edukamu-return-box url="exercises/module3/cost-management-ReturnBox.yaml" id="yy392b6hegs495h1">
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Knowledge Check 3
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/cost-management-knowledge-check-3-question-scroll.yaml" id="mba9j9b1s334bb93"/>
<br>

</edukamu-collapse>
<br>


How did your plan turn out? Hopefully you learned something useful and got to familiarize yourself with Azure’s cost management tools.

Let’s move on to the summary – click on forward!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
