## Management Infrastructure

While physical infrastructure is quite concrete and therefore simple on the surface, the management infrastructure is a little bit more abstract. It includes Azure resources and resource groups, subscriptions, and accounts. Understanding the hierarchical organization will help you plan your projects and products within Azure.

### Azure Resources and Resource Groups

A resource is the basic building block of Azure. Anything you create, provision, or deploy is a resource. Virtual Machines (VMs), virtual networks, databases, AI Services are also considered resources within Azure.

<edukamu-image url="/graphics/module1/resource-group.png" alt="Diagram showing a resource group box with a function, VM, database, and app included." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

<edukamu-section class="slate-section slate-blue">
Resource groups are simply groupings of resources. When you create a resource, you’re required to place it into a resource group. While a resource group can contain many resources, a single resource can only be in one resource group at a time. 

Some resources may be moved between resource groups, but when you move a resource to a new group, it will no longer be associated with the former group. Additionally, resource groups can't be nested, meaning you can’t put resource group B inside of resource group A.

Resource groups provide a convenient way to group resources together. When you apply an action to a resource group, that action will apply to all the resources within the resource group. If you delete a resource group, all the resources will be deleted. If you grant or deny access to a resource group, you’ve granted or denied access to all the resources within the resource group.

When you’re provisioning resources, it’s good to think about the resource group structure that best suits your needs. Furthermore, there aren’t hard rules about how you use resource groups, so consider how to set up your resource groups to maximize their usefulness for you.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Management Groups
</edukamu-collapse-hidden-title>

The final piece is the management group. Resources are gathered into resource groups, and resource groups are gathered into subscriptions. If you’re just starting in Azure that might seem like enough hierarchy to keep things organized. But imagine if you’re dealing with multiple applications, multiple development teams, in multiple geographies.

If you have many subscriptions, you might need a way to efficiently manage access, policies, and compliance for those subscriptions. Azure management groups provide a level of scope above subscriptions. You organize subscriptions into containers called management groups and apply governance conditions to the management groups. 

All Azure subscriptions within a management group automatically inherit the conditions applied to the management group, the same way that resource groups inherit settings from subscriptions and resources inherit from resource groups. Management groups give you enterprise-grade management at a large scale, no matter what type of subscriptions you might have. Management groups can be nested.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Management Group and Subscription Hierarchy
</edukamu-collapse-hidden-title>

You can build a flexible structure of management groups and subscriptions to organize your resources into a hierarchy for unified policy and access management. The following diagram shows an example of creating a hierarchy for governance by using management groups.

<edukamu-image url="/graphics/module1/management-groups-subscriptions.png" alt="Diagram showing an example of a management group hierarchy tree." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

Some examples of how you could use management groups might be:

* **Create a hierarchy that applies a policy**. You could limit VM locations to the US West Region in a group called Production. This policy will inherit onto all the subscriptions that are descendants of that management group and will apply to all VMs under those subscriptions. This security policy can't be altered by the resource or subscription owner, which allows for improved governance.
* **Provide user access to multiple subscriptions**. By moving multiple subscriptions under a management group, you can create one Azure role-based access control (Azure RBAC) assignment on the management group. Assigning Azure RBAC at the management group level means that all sub-management groups, subscriptions, resource groups, and resources underneath that management group would also inherit those permissions. One assignment on the management group can enable users to have access to everything they need instead of scripting Azure RBAC over different subscriptions.

Important facts about management groups:

* 10,000 management groups can be supported in a single directory.
* A management group tree can support up to six levels of depth. This limit doesn't include the root level or the subscription level.
* Each management group and subscription can support only one parent.

</edukamu-collapse>
<br>

You should now have a basic understanding of the management infrastructure of Azure. This may have been a lot to take in, so feel free to relax for a moment and gather your thoughts. When you’re ready, let’s move on to computing services.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
