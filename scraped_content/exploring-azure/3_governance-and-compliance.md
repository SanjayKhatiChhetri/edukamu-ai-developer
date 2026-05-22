## Governance and Compliance

Let’s imagine you’re running a project on Azure. It all goes well – you have your resources in place, data secured, and a few motivated employees working with you towards the same goals. Actually, it’s going so well that you will soon find yourself in a situation in which you have to expand the project.

Azure Blueprints is there to guide and support you through the process.

<edukamu-section class="slate-section slate-blue">
### Azure Blueprints

Azure Blueprints lets you standardize cloud subscription or environment deployments. Instead of having to configure features like Azure Policy for each new subscription, with Azure Blueprints you can define repeatable settings and policies that are applied as new subscriptions are created. 

Need a new test/dev environment? Azure Blueprints lets you deploy one with security and compliance settings already configured. In this way, development teams can rapidly build and deploy new environments with the knowledge that they're building within organizational requirements.

Each component in the blueprint definition is known as an artifact.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Blueprints and Deployments
</edukamu-collapse-hidden-title>

Azure Blueprints are version-able, allowing you to create an initial configuration and then make updates later on and assign a new version to the update. With versioning, you can make small updates and keep track of which deployments used which configuration set.

With Azure Blueprints, the relationship between the blueprint definition (what should be deployed) and the blueprint assignment (what was deployed) is preserved. In other words, Azure creates a record that associates a resource with the blueprint that defines it. This connection helps you track and audit your deployments.

</edukamu-collapse>
<br>

As you expand your project, you might run into worries about compliance. How do you ensure that your resources stay compliant? Can you be alerted if a resource's configuration has changed?

Azure Policy is a service in Azure that enables you to create, assign, and manage policies that control or audit your resources. These policies enforce different rules across your resource configurations so that those configurations stay compliant with corporate standards.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Policy and Initiatives
</edukamu-collapse-hidden-title>

Azure Policy enables you to define both individual policies and groups of related policies, known as initiatives. Azure Policy evaluates your resources and highlights resources that aren't compliant with the policies you've created. Azure Policy can also prevent noncompliant resources from being created.

Azure Policies can be set at each level, enabling you to set policies on a specific resource, resource group, subscription, and so on. Additionally, Azure Policies are inherited, so if you set a policy at a high level, it will automatically be applied to all of the groupings that fall within the parent. For example, if you set an Azure Policy on a resource group, all resources created within that resource group will automatically receive the same policy.

Azure Policy comes with built-in policy and initiative definitions for Storage, Networking, Compute, Security Center, and Monitoring. For example, if you define a policy that allows only a certain size for the virtual machines (VMs) to be used in your environment, that policy is invoked when you create a new VM and whenever you resize existing VMs. Azure Policy also evaluates and monitors all current VMs in your environment, including VMs that were created before the policy was created.

In some cases, Azure Policy can automatically remediate noncompliant resources and configurations to ensure the integrity of the state of the resources. For example, if all resources in a certain resource group should be tagged with AppName tag and a value of "SpecialOrders," Azure Policy will automatically apply that tag if it is missing. However, you still retain full control of your environment. If you have a specific resource that you don’t want Azure Policy to automatically fix, you can flag that resource as an exception – and the policy won’t automatically fix that resource.

Azure Policy also integrates with Azure DevOps by applying any continuous integration and delivery pipeline policies that pertain to the pre-deployment and post-deployment phases of your applications.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Policy Initiatives
</edukamu-collapse-hidden-title>

An Azure Policy initiative is a way of grouping related policies together. The initiative definition contains all of the policy definitions to help track your compliance state for a larger goal.

For example, Azure Policy includes an initiative named Enable Monitoring in Azure Security Center. Its goal is to monitor all available security recommendations for all Azure resource types in Azure Security Center.

</edukamu-collapse>

</edukamu-collapse>
<br>

After expanding your project from a simple subscription using Azure Blueprints and ensuring co-operation compliance with Azure Policy, it’s time to make sure everything will keep on working as intended. A resource lock is a great way to do just that, to keep resources from being accidentally deleted or changed.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Resource Lock
</edukamu-collapse-hidden-title>

Even with Azure role-based access control (Azure RBAC) policies in place, there's still a risk that people with the right level of access could delete critical cloud resources. Resource locks prevent resources from being deleted or updated, depending on the type of lock. 

Resource locks can be applied to individual resources, resource groups, or even an entire subscription. Resource locks are inherited, meaning that if you place a resource lock on a resource group, all of the resources within the resource group will also have the resource lock applied.

There are two types of resource locks, one that prevents users from deleting and one that prevents users from changing or deleting a resource.

* Delete means authorized users can still read and modify a resource, but they can't delete the resource.
* ReadOnly means authorized users can read a resource, but they can't delete or update the resource. Applying this lock is similar to restricting all authorized users to the permissions granted by the Reader role.

### Managing Resource Locks

You can manage resource locks from the Azure portal, PowerShell, the Azure CLI, or from an Azure Resource Manager template.

To view, add, or delete locks in the Azure portal, go to the Settings section of any resource's Settings pane in the Azure portal.

<edukamu-image url="/graphics/module3/resource-lock.png" alt="A screenshot showing the resource lock control, under settings, for a storage account." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

### Modifying Resources

Although locking helps prevent accidental changes, you can still make changes by following a two-step process.

To modify a locked resource, you must first remove the lock. After you remove the lock, you can apply any action you have permissions to perform. Resource locks apply regardless of RBAC permissions. Even if you're an owner of the resource, you must still remove the lock before you can perform the blocked activity.

</edukamu-collapse>

<edukamu-section class="slate-section slate-blue">
Don't worry if using all these tools seems challenging or even their names difficult to remember. During this course, you’re given a guided tour through the basics – and a bit beyond – of Azure, and the goal is to provide you with tools to continue on your path to becoming an effective Azure manager. 

When you get the chance to use Azure on a daily basis, your hard work will surely pay off, and all the terminology will become clearer and clearer as you go.  

Before we move on to our final topic, let’s get to know the Service Trust Portal. It’s the place to go for all your security, privacy, and compliance worries relating to Microsoft services like Azure. 
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Service Trust Portal
</edukamu-collapse-hidden-title>

The Microsoft Service Trust Portal is a portal that provides access to various content, tools, and other resources about Microsoft security, privacy, and compliance practices.

The Service Trust Portal contains details about Microsoft's implementation of controls and processes that protect our cloud services and the customer data therein. To access some of the resources on the Service Trust Portal, you must sign in as an authenticated user with your Microsoft cloud services account (Azure Active Directory organization account). You will need to review and accept the Microsoft non-disclosure agreement for compliance materials.

You can access the Service Trust Portal right away!

<edukamu-button url="https://servicetrust.microsoft.com/">Service Trust Portal</edukamu-button>
<br>

<edukamu-image url="/graphics/module3/service-trust-portal.png" alt="Screenshot of the service trust portal with the main menu items visible." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

</edukamu-collapse>  
<br>

We’ve already covered Azure quite extensively, but the platform still has a lot left up its cloud-based sleeve, like the following. They are meant for quite advanced project managers, but you can still take a glance at them if you want to. We won’t cover them to a deep extent on this course, so it’s entirely up to you.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Advisor
</edukamu-collapse-hidden-title>

Azure Advisor evaluates your Azure resources and makes recommendations to help improve reliability, security, and performance, achieve operational excellence, and reduce costs. Azure Advisor is designed to help you save time on cloud optimization. The recommendation service includes suggested actions you can take right away, postpone, or dismiss.

The recommendations are available via the Azure portal and the API, and you can set up notifications to alert you to new recommendations.

When you're in the Azure portal, the Advisor dashboard displays personalized recommendations for all your subscriptions. You can use filters to select recommendations for specific subscriptions, resource groups, or services. The recommendations are divided into five categories:

* **Reliability** is used to ensure and improve the continuity of your business-critical applications.
* **Security** is used to detect threats and vulnerabilities that might lead to security breaches.
* **Performance** is used to improve the speed of your applications.
* **Operational Excellence** is used to help you achieve process and workflow efficiency, resource manageability, and deployment best practices.
* **Cost** is used to optimize and reduce your overall Azure spending.

The following image shows the Azure Advisor dashboard.

<edukamu-image url="/graphics/module3/azure-advisor-dashboard.png" alt="Screenshot of the Azure Advisor dashboard with boxes for the main areas of recommendations." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Service Health
</edukamu-collapse-hidden-title>

Microsoft Azure provides a global cloud solution to help you manage your infrastructure needs, reach your customers, innovate, and adapt rapidly. Knowing the status of the global Azure infrastructure and your individual resources could seem like a daunting task. Azure Service Health helps you keep track of Azure resource, both your specifically deployed resources and the overall status of Azure. Azure service health does this by combining three different Azure services:

* **Azure Status** is a broad picture of the status of Azure globally. Azure status informs you of service outages in Azure on the Azure Status page. The page is a global view of the health of all Azure services across all Azure regions. It’s a good reference for incidents with widespread impact.
* **Service Health** provides a narrower view of Azure services and regions. It focuses on the Azure services and regions you're using. This is the best place to look for service impacting communications about outages, planned maintenance activities, and other health advisories because the authenticated Service Health experience knows which services and resources you currently use. You can even set up Service Health alerts to notify you when service issues, planned maintenance, or other changes may affect the Azure services and regions you use.
* **Resource Health** is a tailored view of your actual Azure resources. It provides information about the health of your individual cloud resources, such as a specific virtual machine instance. Using Azure Monitor, you can also configure alerts to notify you of availability changes to your cloud resources.

By using Azure status, Service health, and Resource health, Azure Service Health gives you a complete view of your Azure environment-all the way from the global status of Azure services and regions down to specific resources. Additionally, historical alerts are stored and accessible for later review. Something you initially thought was a simple anomaly that turned into a trend, can readily be reviewed and investigated thanks to the historical alerts.

Finally, in the event that a workload you’re running is impacted by an event, Azure Service Health provides links to support.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Monitor
</edukamu-collapse-hidden-title>

Azure Monitor is a platform for collecting data on your resources, analyzing that data, visualizing the information, and even acting on the results. Azure Monitor can monitor Azure resources, your on-premises resources, and even multi-cloud resources like virtual machines hosted with a different cloud provider.

The following diagram illustrates just how comprehensive Azure Monitor is:

<edukamu-image url="/graphics/module3/azure-monitor-overview_2.svg" alt="An illustration showing the flow of information that Azure Monitor uses to provide monitoring and data visualization." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<edukamu-section class="edukamu-kuvateksti">
On the left is a list of the sources of logging and metric data that can be collected at every layer in your application architecture, from application to operating system and network.

In the center, the logging and metric data are stored in central repositories.

On the right, the data is used in several ways. You can view real-time and historical performance across each layer of your architecture or aggregated and detailed information. The data is displayed at different levels for different audiences. You can view high-level reports on the Azure Monitor Dashboard or create custom views by using Power BI and Kusto queries.
</edukamu-section>
<br>

Additionally, you can use the data to help you react to critical events in real time, through alerts delivered to teams via SMS, email, and so on. Or you can use thresholds to trigger autoscaling functionality to scale to meet the demand.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Log Analytics
</edukamu-collapse-hidden-title>

Azure Log Analytics is the tool in the Azure portal where you will write and run log queries on the data gathered by Azure Monitor. Log Analytics is a robust tool that supports both simple, complex queries, and data analysis. You can write a simple query that returns a set of records and then use features of Log Analytics to sort, filter, and analyze the records. You can write an advanced query to perform statistical analysis and visualize the results in a chart to identify a particular trend. Whether you work with the results of your queries interactively or use them with other Azure Monitor features such as log query alerts or workbooks, Log Analytics is the tool that you're going to use to write and test those queries.

### 1. Azure Monitor Alerts

Azure Monitor Alerts are an automated way to stay informed when Azure Monitor detects a threshold being crossed. You set the alert conditions, the notification actions, and then Azure Monitor Alerts notifies when an alert is triggered. Depending on your configuration, Azure Monitor Alerts can also attempt corrective action.

<edukamu-image url="/graphics/module3/azure-monitor-alerts.png" alt="Screenshot of Azure Monitor Alerts showing total alerts, and then the alerts grouped by severity." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>

Alerts can be set up to monitor the logs and trigger on certain log events, or they can be set to monitor metrics and trigger when certain metrics are crossed. For example, you could set a metric-based alert up to notify you when the CPU usage on a virtual machine exceeded 80%. Alert rules based on metrics provide near real time alerts based on numeric values. Rules based on logs allow for complex logic across data from multiple sources.

Azure Monitor Alerts use action groups to configure who to notify and what action to take. An action group is simply a collection of notification and action preferences that you associate with one or multiple alerts. Azure Monitor, Service Health, and Azure Advisor all use actions groups to notify you when an alert has been triggered.

### 2. Application Insights

Application Insights, an Azure Monitor feature, monitors your web applications. Application Insights is capable of monitoring applications that are running in Azure, on-premises, or in a different cloud environment.

There are two ways to configure Application Insights to help monitor your application. You can either install an SDK in your application, or you can use the Application Insights agent. The Application Insights agent is supported in C#.NET, VB.NET, Java, JavaScript, Node.js, and Python.

Once Application Insights is up and running, you can use it to monitor a broad array of information, such as:

* Request rates, response times, and failure rates
* Dependency rates, response times, and failure rates, to show whether external services are slowing down performance
* Page views and load performance reported by users' browsers
* AJAX calls from web pages, including rates, response times, and failure rates
* User and session counts
* Performance counters from Windows or Linux server machines, such as CPU, memory, and network usage

Not only does Application Insights help you monitor the performance of your application, but you can also configure it to periodically send synthetic requests to your application, allowing you to check the status and monitor your application even during periods of low activity.

</edukamu-collapse>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Managing Projects on Azure
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-quiz url="/exercises/module3/governance-and-compliance-text-quiz.yaml" theme="text-quiz-no-answer-colors" id="3n98hq6qnbn04o94"/>
<br>

<edukamu-text-quiz url="/exercises/module3/governance-and-compliance-text-quiz-2.yaml" theme="text-quiz-no-answer-colors" id="0k6g1o142jtcha47"/>
<br>

<edukamu-text-quiz url="/exercises/module3/governance-and-compliance-text-quiz-3.yaml" theme="text-quiz-no-answer-colors" id="38ef6c1hv5l4xhf4"/>
<br>

<edukamu-text-quiz url="/exercises/module3/governance-and-compliance-text-quiz-4.yaml" theme="text-quiz-no-answer-colors" id="c8016bcvsi4it012"/>
<br>

<edukamu-text-quiz url="/exercises/module3/governance-and-compliance-text-quiz-5.yaml" theme="text-quiz-no-answer-colors" id="fy1goydlv2l21u0d"/>
<br>

</edukamu-collapse>
<br>


We still have one topic to go – costs. While being an extensive, all-encompassing cloud solution, Azure can also help you save money. How exactly? Click on to the final section of this course to find out.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
