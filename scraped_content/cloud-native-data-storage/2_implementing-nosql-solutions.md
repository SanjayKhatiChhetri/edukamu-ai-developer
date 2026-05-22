## Implementing NoSQL Solutions

Each NoSQL database is unique, and so is the use scenario. That's why developers using platforms like Azure Cosmos DB should pay extra close attention to not only the planning, but also the implementation of such services.

On the previous page, we reviewed important aspects to consider when planning to implement NoSQL databases. Now it's time to explore the implementation itself.

Applications come in many different patterns, they may have predictable usage, or they could be spiked with sudden traffic surges. Azure Cosmos DB has multiple ways to host workloads that map directly to how applications run in the real world, whether the applications are predictable or not.

Let's get familiar with the various service and throughput offerings Cosmos DB has to offer. We'll start by comparing so-called *serverless* and *provisional* throughput methods.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Understanding Serverless Throughput
</edukamu-collapse-hidden-title>

As you remember, the term throughput refers to the measure of the resources allocated to a database, container, or operation within the Cosmos DB service. In essence, it's a question of balancing between sufficient resources and cost management.

Serverless options might be suitable when you're looking for strictly consumption-based models whereas provisioned throughput is ideal for predictable traffic patterns to which resources can be allocated beforehand.

Azure Cosmos DB serverless is a consumption-based model where each request consumes request units. The consumption model eliminates the need to pre-provision throughput request units ahead of time.

Remember, when using Azure Cosmos DB, you typically express database options as a cost described in Request Units per second.

### Use Cases for Azure Cosmos DB Serverless

<edukamu-image url="/graphics/module2/2-serverless.png" alt="Diagram of individual requests consuming RU/s.">
<br>

Serverless is great for applications with unpredictable or bursty traffic. You can use serverless with an application such as:

- A new application with hard to forecast users loads
- A new prototype application within your organization
- Serverless compute integration with a service like Azure Functions
- Just getting started with Azure Cosmos DB as a new developer
- Low traffic application that doesn’t send or receive numerous data

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Comparing Serverless and Provisioned Throughput
</edukamu-collapse-hidden-title>

In Azure Cosmos DB, the primary difference between serverless and provisioned throughput lies in how resources are allocated and billed:

### 1. Provisioned Throughput:

- **Model:** Traditional model in which you pre-allocate a fixed amount of throughput measured in Request Units per Second (RU/s) for a container or a database.
- **Billing:** You are billed based on the provisioned RU/s, regardless of actual usage. This means you pay for the provisioned capacity, whether or not you fully utilize it.
- **Predictability:** Offers predictable performance because you have a dedicated amount of throughput reserved for your use.


### 2. Serverless:

- **Model:** A consumption-based model in which you don't need to pre-allocate or provision a specific amount of throughput. Instead, you pay for the actual resources consumed by your operations.
- **Billing:** You are billed based on the actual number of RU/s consumed by your requests. This model is suitable for scenarios with unpredictable or intermittent workloads.
- **Cost-Efficiency:** Cost-efficient for workloads with varying demand as you only pay for what you use, making it suitable for scenarios where usage patterns are sporadic.
- **Automatic Scaling:** Scales automatically based on demand without the need for manual provisioning.

In summary, provisioned throughput provides a fixed and predictable amount of resources that you pay for upfront, while serverless allows for more flexible and cost-effective resource usage based on actual demand, ideal for scenarios with variable workloads.

</edukamu-collapse>
<br>


At first, the serverless model seems ideal, doesn't it? Why pay for something *just in case* when you can just pay as you go without spending a dime extra? Well, serverless accounts have some limitations. They can, for example, only run in a single Azure region at a time and are limited to storing 50 gigabytes of data per container.

In other words, while the serverless model might require less planning and worrying about payments, it might not work well for large-scale applications – especially those trying to gain popularity worldwide!

Next, let's get to know two throughput methods, namely *autoscale* and *standard* (or manual).


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Understanding Autoscale and Standard Throughput
</edukamu-collapse-hidden-title>

### Autoscale Throughput

We can often make an educated guess about where our workload will be as far as throughput, but we won’t know exactly where it lands until it’s in production. We also may know our operational tolerances. We know:

- The maximum amount of money we are willing to spend
- The minimum amount of performance we are ready to tolerate.

With all of this information in mind, we could define a range. This range would represent our application running at a comfortable performance level without overspending without our knowledge.

<edukamu-image url="/graphics/module2/4-autoscale-1.png" alt="Application with usage oscillating between maximum potential spend and minimum performance." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

With Azure Cosmos DB autoscale, we can define a range of request units per second (RU/s) to scale our database or container automatically and instantly. The throughput RU/s is scaled based on real-time usage instantly.

<edukamu-image url="/graphics/module2/4-autoscale-2.png" alt="Autoscale between max and min RU/s." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Autoscale is great for workloads with variable or unpredictable traffic patterns and can minimize unused capacity that would typically be pre-provisioned.

### Standard Throughput

Standard throughput, also referred to as manual throughput provisioning, allows you to manually specify the provisioned throughput (measured in Request Units per second, RU/s) for your Azure Cosmos DB containers or databases. You need to determine and set the amount of throughput based on your expected workload and performance requirements.

This method offers the following characteristics:

- **Fixed Capacity:** The provisioned throughput remains fixed unless manually adjusted.
- **Predictable Performance:** Offers predictable and consistent performance because you're guaranteed the provisioned number of resources.
- **Cost Implications:** You pay for the provisioned throughput, regardless of whether the actual usage is lower than the provisioned amount.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Comparing Autoscale and Standard Throughput
</edukamu-collapse-hidden-title>

Let's consider a few factors that are helpful when choosing between autoscale and standard throughput.

### 1. Comparing Workloads

Standard throughput is again suited for workloads with steady traffic.

Autoscale throughput is better suited for unpredictable traffic. Autoscale can ensure that your actual Azure Cosmos DB provisioned throughput oscillates between your minimal acceptable performance and maximum allowed spend.

### 2. Comparing Request Units

Standard throughput requires a static number of request units to be assigned ahead of time.

With autoscale, you only set the maximum, and the minimum billed will be 10% of the maximum when there are zero requests.

### 3. Comparing Scenarios

You want to use standard throughput provisioning in scenarios when your team can accurately predict the amount of throughput your application needs, and your team suspects these needs will not change over time. Also, throughput provisioning is ideal for scenarios where the full RU/s provisioned is consumed for > 66% of hours per month.

Autoscale throughput is helpful if your team cannot predict your throughput needs accurately or otherwise use the max throughput amount for < 66% of hours per month.

### 4. Comparing Rare-Limiting

The standard throughput will always remain static at the set RU/s that is provisioned. Requests beyond this will be rate-limited, with a response indicating that a wait should be attempted before retrying.

Autoscale will scale up to the max RU/s before similarly rate-limiting responses

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
In summary, standard (manual) throughput provides fixed and predictable resources, while autoscale throughput offers dynamic and cost-efficient scalability based on actual workload demand. The choice between them depends on factors such as workload predictability and, as you know, should always be taken consciously.

You should also notice that throughput can always be modified at a later stage. Existing containers can be migrated to and from autoscale using the Azure portal, Azure CLI, or Azure PowerShell. During the migration process, the system will automatically apply a request unit per second (RU/s) value to the container, so your development team can keep on working with confidence!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Configuring Throughput for Azure Cosmos DB
</edukamu-collapse-hidden-title>

**Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

This practice exercise also requires a lab environment to be completed. You'll once again get to use a Windows-based virtual machine provided by Microsoft. You'll also be provided step-by-step instructions on configuring throughput on Azure Cosmos DB.

You can access the lab environment by navigating to Microsoft Learn and using the button to activate the lab.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/configure-azure-cosmos-db-sql-api/7-exercise-configure-throughput-for-azure-portal">Lab: Configuring Throughput for Azure Cosmos DB</edukamu-button>
<br>

Should you run any issues, please refer to the more detailed instructions on the page *Components of Cosmos DB for NoSQL*.

If you decide to take on the practice exercise, good luck! Enjoy the process!

</edukamu-collapse>
<br>


Throughput is arguably the most important aspect to consider when configuring NoSQL solutions for global databases – whether it be with Azure Cosmos DB or some other similar service.

Let's review what we've just learned with an exercise.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Configuring Throughput
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/implementing-nosql-solutions-question-scroll-1.yaml" id="vgymh3s1epbg5ixd">
<br>

</edukamu-collapse>
<br>


In the second unit, we’ve so far focused on planning and implementing NoSQL database solutions, and we'll continue exploring the same topic on the next page. More precisely, we'll look at importing and exporting data to Azure Cosmos DB using various methods.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
