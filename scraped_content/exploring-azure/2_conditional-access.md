## Conditional Access

Conditional Access is a tool that Azure Active Directory uses to allow (or deny) access to resources based on identity signals. These signals include who the user is, where the user is, and what device the user is requesting access from.

Conditional Access helps IT administrators:

* empower users to be productive wherever and whenever
* protect the organization's assets.

Conditional Access also provides a more granular multifactor authentication experience for users. For example, a user might not be challenged for second authentication factor if they're at a known location. However, they might be challenged for a second authentication factor if their sign-in signals are unusual or they're at an unexpected location.

During sign-in, Conditional Access collects signals from the user, makes decisions based on those signals, and then enforces that decision by allowing or denying the access request or challenging for a multifactor authentication response.

The following diagram illustrates this flow:

<edukamu-image url="/graphics/module2/signal-decision-enforcement.png" alt="Diagram showing the conditional access flow of a signal leading to a decision, leading to enforcement." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

Here, the signal might be the user's location, the user's device, or the application that the user is trying to access.

Based on these signals, the decision might be to allow full access if the user is signing in from their usual location. If the user is signing in from an unusual location or a location that's marked as high risk, then access might be blocked entirely or possibly granted after the user provides a second form of authentication.

Enforcement is the action that carries out the decision. For example, the action is to allow access or require the user to provide a second form of authentication.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### When to Use Conditional Access?
</edukamu-collapse-hidden-title>

Azure Conditional Access may come in handy in many situations. It should be at least considered whenever you want to…

* require multifactor authentication (MFA) to access an application depending on the requester’s role, location, or network. For example, you could require MFA for administrators but not regular users or for people connecting from outside your corporate network.
* require access to services only through approved client applications. For example, you could limit which email applications are able to connect to your email service.
* require users to access your application only from managed devices. A managed device is a device that meets your standards for security and compliance.
* lock access from untrusted sources, such as access from unknown or unexpected locations.

</edukamu-collapse>

Even though Azure makes it easy to ensure that only people from your organization have access to your data and projects, external access can also be granted if necessary. This is when Azure External Access comes in handy.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure External Identities
</edukamu-collapse-hidden-title>

An external identity can be a person, device, or service that is outside your organization. Azure AD External Identities refers to all the ways you can securely interact with users outside of your organization. If you want to collaborate with partners, distributors, suppliers, or vendors, you can share your resources and define how your internal users can access external organizations. If you're a developer creating consumer-facing apps, you can manage your customers' identity experiences.

External identities may sound similar to single sign-on. With External Identities, external users can "bring their own identities." Whether they have a corporate or government-issued digital identity, or an unmanaged social identity like Google or Facebook, they can use their own credentials to sign in. The external user’s identity provider manages their identity, and you manage access to your apps with Azure AD or Azure AD B2C to keep your resources protected.

<edukamu-image url="/graphics/module2/azure-adei.png" alt="Diagram showing B2B collaborators accessing your tenant and B2C collaborators accessing the AD B2C tenant." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; max-width: 80%;">
<br>

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
### Role-based Access Control

When you have multiple IT and engineering teams, how can you control what access they have to the resources in your cloud environment? The principle of least privilege says you should only grant access up to the level needed to complete a task. If you only need read access to a storage blob, then you should only be granted read access to that storage blob. Write access to that blob shouldn’t be granted, nor should read access to other storage blobs. It’s a good security practice to follow.

However, managing that level of permissions for an entire team would become tedious. Instead of defining the detailed access requirements for each individual, and then updating access requirements when new resources are created or new people join the team, Azure enables you to control access through Azure role-based access control (Azure RBAC).

Azure provides built-in roles that describe common access rules for cloud resources. You can also define your own roles. Each role has an associated set of access permissions that relate to that role. When you assign individuals or groups to one or more roles, they receive all the associated access permissions.

So, if you hire a new engineer and add them to the Azure RBAC group for engineers, they automatically get the same access as the other engineers in the same Azure RBAC group. Similarly, if you add additional resources and point Azure RBAC at them, everyone in that Azure RBAC group will now have those permissions on the new resources as well as the existing resources.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### How is Role-based Access Control Applied to Resources?
</edukamu-collapse-hidden-title>

Role-based access control (RBAC) is applied to a scope, which is a resource or set of resources that this access applies to.

The following diagram shows the relationship between roles and scopes. A management group, subscription, or resource admin might be given the role of owner, so they have increased control and authority. An observer, who isn't expected to make any updates, might be given a role of Reader for the same scope, enabling them to review or observe the management group, subscription, or resource group.

<edukamu-image url="/graphics/module2/rbac.png" alt="A diagram showing scopes and roles. Role and scope combinations map to a specific kind of user or account, such as an observer or an admin." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

Scopes include:

* A management group (a collection of multiple subscriptions).
* A single subscription.
* A resource group.
* A single resource.

Observers, users managing resources, admins, and automated processes illustrate the kinds of users or accounts that would typically be assigned each of the various roles.

Azure RBAC is hierarchical, in that when you grant access at a parent scope, those permissions are inherited by all child scopes. For example:
* When you assign the Owner role to a user at the management group scope, that user can manage everything in all subscriptions within the management group.
* When you assign the Reader role to a group at the subscription scope, the members of that group can view every resource group and resource within the subscription.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### How is Azure RBAC Enforced?
</edukamu-collapse-hidden-title>

Azure RBAC is enforced on any action that's initiated against an Azure resource that passes through Azure Resource Manager. Resource Manager is a management service that provides a way to organize and secure your cloud resources.

You typically access Resource Manager from the Azure portal, Azure Cloud Shell, Azure PowerShell, and the Azure CLI. Azure RBAC doesn't enforce access permissions at the application or data level. Application security must be handled by your application.

Azure RBAC uses an allow model. When you're assigned a role, Azure RBAC allows you to perform actions within the scope of that role. If one role assignment grants you read permissions to a resource group and a different role assignment grants you write permissions to the same resource group, you have both read and write permissions on that resource group.

</edukamu-collapse>

How does it seem so far? Are you beginning to understand Azure a little bit better? You’ve now reached the end of the second unit, and now is a splendid time to take a few deep breaths. Review the course materials up to this point and complete the following exercises before moving on.

<br>
<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Azure Services
</edukamu-collapse-hidden-title>

Take a moment to get truly acquainted with a few Azure services. You’ve now familiarized yourself with many of them, and now is your chance to dig deeper.

Choose three of the services we’ve covered so far on the course – be it computing, storage, data migration, or something entirely different – and find out more about them. Answer the following questions as precisely as possible.

1. What are the main purposes of the service? When is it the most useful?
2. What do you need to run the service?
3. How much does the service cost monthly?
4. Is the service still being developed?
5. Are there alternative solutions available?

You can find a lot of information directly from the [Azure Service Directory](https://azure.microsoft.com/en-us/products/)(target="_blank"), and there are many third-party resources explaining Azure online as well. 

Turn in your answers to the Edukamu platform. Take your time to answer the questions carefully, as the information might come in handy later.

<edukamu-return-box url="exercises/module2/conditional-access-ReturnBox.yaml" id="ccsf48g08t9kx75z">
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Knowledge Check 2
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/conditional-access-knowledge-check-2-question-scroll.yaml" id="3yaj23yqun895280"/>
<br>

</edukamu-collapse>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### YRITYS: Taking it a Step Further
</edukamu-collapse-hidden-title>

Placeholder: Tähän teksti, jossa on tietoiskuja tai pohdintaa.

</edukamu-collapse> -->

Next up is the third and final unit of this course. We’ve now familiarized ourselves with Azure and its basic services without forgetting the safety and security measures it offers. The third unit focuses on management, costs, and tools. 

Take the time to congratulate you for the work you’ve done so far and click yourself forward when you feel ready.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1-2-3-4-5.png" alt="Edukamu-progress-in-a-module-image">
