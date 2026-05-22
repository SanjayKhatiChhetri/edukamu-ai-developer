## Planning NoSQL Solutions

So far on this course, we've explored NoSQL services, such as Azure Cosmos DB for NoSQL, from various perspectives, and also tried setting up a brand-new database. Now, it's time to delve deeper into NoSQL database implementation.

Creating a new Azure Cosmos DB account often requires making many configuration choices that can, at first, be daunting. While the defaults fit numerous scenarios, it makes the most sense to familiarize yourself with the configuration options to ensure that your account and resources are optimally configured for your solution. Careful planning will pay off in the long run.

We'll start by evaluating resource requirements. It is important to recognize the needs of your project and evaluate thoroughly before starting the actual setup process.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step 1. Understanding Throughput
</edukamu-collapse-hidden-title>

Referring to our basic hierarchy of resources, an Azure Cosmos DB for NoSQL database is a unit of management for a set of schema-agnostic containers. Each container is a unit of scalability for both throughput and storage.

Containers are partitioned horizontally across compute within an Azure region and distributed across all Azure Regions you configure in your Azure Cosmos DB for NoSQL account.

When configuring Azure Cosmos DB, you can provision throughput at either or both the database and container levels.

### Container-Level Throughput Provisioning

<edukamu-image url="/graphics/module2/2-container.png" alt="Throughput provisioned at container level." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Any throughput provisioned exclusively at the container level is reserved only for this container. This throughput is available only for this container all the time. This throughput is also financially backed by SLAs.

**Note**: While there are others available, this is the most commonly used method of manual throughput provisioning.


### Database-Level Throughput Provisioning

<edukamu-image url="/graphics/module2/2-database.png" alt="Throughput provisioned at database level." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Throughput provisioned on a database is shared across all containers in the database. Because all containers share the throughput resources, you may not get predictable performance in a specific container within the database.


### Mixed-Throughput Provisioning

<edukamu-image url="/graphics/module2/2-mixed.png" alt="Throughput provisioned at both container and database level." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

There may be situations where you may want to combine provisioning throughput at the database and container level. A container with provisioned throughput cannot be converted to a shared database container. Conversely, a shared database container cannot be converted to have dedicated throughput.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Evaluating Throughput Requirements
</edukamu-collapse-hidden-title>

Request units are a rate-based currency. They are used to make it simple to talk about physical resources like memory, CPU, and IO when performing requests in Azure Cosmos DB. For example, it’s easier to think of 10 request units as roughly twice as much as five request units in a relative sense without worrying about the physical resources that are abstracted away. Request units are used to measure both foreground and background activities.

Every request consumes a fixed number of request units, including but not limited to:

- Reads
- Writes
- Queries
- Stored procedures

### Configuring Output

When you create a database or container in Azure Cosmos DB, you can provision request units in an increment of request units per second (or RU/s for short). You cannot provision less than 400 RU/s, and they are provisioned in increments of 100.

### Estimating ad-hoc RU/s Consumption

Some RU/s are normalized across various access methods, making many common operations predictable. Using this knowledge, you can perform some basic estimations for simple workloads. For example, you can estimate the RU/s required for common database operations such as one RU for a read and six RU/s for a write operation of a 1-KB document in optimal conditions.

<edukamu-image url="/graphics/module2/3-request-units.png" alt="Request units diagram with estimates." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; max-width: 60%;">
<br>

Using this strategy, you should identify your solution's query and access patterns to make an educated guess as to how many request units will be needed in Azure Cosmos DB. To accomplish this, you will want information such as:

- Top five queries
- Number of read operations per second
- Number of write operations per second

You can use a spreadsheet application to build a quick table to figure out a rough estimate of your needed request unit capacity. Here's a quick example:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
Operation type
</edukamu-table-header>
<edukamu-table-header>
Number of requests per second
</edukamu-table-header>
<edukamu-table-header>
Number of RU per request
</edukamu-table-header>
<edukamu-table-header>
RU/s needed
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**Write Single Document**
</edukamu-table-cell>
<edukamu-table-cell>
10,000
</edukamu-table-cell>
<edukamu-table-cell>
10
</edukamu-table-cell>
<edukamu-table-cell>
100,000
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Top Query #1**
</edukamu-table-cell>
<edukamu-table-cell>
700
</edukamu-table-cell>
<edukamu-table-cell>
100
</edukamu-table-cell>
<edukamu-table-cell>
70,000
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Top Query #2**
</edukamu-table-cell>
<edukamu-table-cell>
200
</edukamu-table-cell>
<edukamu-table-cell>
100
</edukamu-table-cell>
<edukamu-table-cell>
20,000
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Top Query #3**
</edukamu-table-cell>
<edukamu-table-cell>
100
</edukamu-table-cell>
<edukamu-table-cell>
100
</edukamu-table-cell>
<edukamu-table-cell>
10,000
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Total RU/s**
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
200,000 RU/s
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<edukamu-section class="edukamu-included-only-in-mobile">
<edukamu-section class="edukamu-kuvateksti">
The Table above is horizontally scrollable.
</edukamu-section>
</edukamu-section>
<br>

**Tip:** You can also run a proof of concept application, and use the request charge property of the SDK to measure the real-world RU charge of running the operations that you intend to make against Azure Cosmos DB.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
The goal of throughput evaluation is to strike a balance between providing sufficient resources to meet the performance requirements of your application and avoiding over-provisioning, which can lead to unnecessary costs.

While important, throughput evaluation is not the only step when it comes to setting up NoSQL services. Let's learn more.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step 2. Planning Data Storage
</edukamu-collapse-hidden-title>

Planning for a new Azure Cosmos DB account is composed of two components: throughput and storage. While we have already discussed throughput, data in Azure Cosmos DB will also consume SSD storage billed per GB per month.

### Migrating Existing Workloads

The Azure Cosmos DB Capacity Calculator is a calculator surfaced as an online form to plug in details about your existing data workload to help estimate your application's storage and throughput requirements and translate it to a cost estimate in terms of Azure Cosmos DB.

<edukamu-image url="/graphics/module2/4-calculator.png" alt="Screenshot of the Azure Cosmos DB Capacity Calculator." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

The calculator will inquire about details such as:

- Total data stored
- Whether you expect to perform near real-time analytics
- The anticipated size of documents
- Point reads per second
- Queries per second

After your rough estimate and proof of concept, use the capacity calculator to refine your estimate further to a much more accurate cost to run your solution in Azure Cosmos DB.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step 3. Configuring Time-to-live (TTL)
</edukamu-collapse-hidden-title>

Azure Cosmos DB allows you to set the length of time documents live in the database before being automatically purged. A document's "time-to-live" (TTL) is measured in seconds from the last modification and can be set at the container level with the ability to override on a per-item basis.

Once set at the container level, Azure Cosmos DB will automatically purge documents at the specified time since they were last modified. The TTL value is defined as an integer in seconds.

**Tip:** The maximum TTL value is 2147483647.

TTL expiration is a background task performed in the background using request units and is scheduled when quiescent.

### Configuring TTL on a Container

The TTL value for a container is configured using the DefaultTimeToLive property of the container's JSON object.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
DefaultTimeToLive
</edukamu-table-header>
<edukamu-table-header>
Expiration
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
*Does not exist*
</edukamu-table-cell>
<edukamu-table-cell>
Items are not automatically expired.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
-1
</edukamu-table-cell>
<edukamu-table-cell>
Items will not expire by default.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
*n*
</edukamu-table-cell>
<edukamu-table-cell>
*n* seconds after last modified time.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section>
<br>

### Examples

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
Container.DefaultTimeToLive
</edukamu-table-header>
<edukamu-table-header>
Item.ttl
</edukamu-table-header>
<edukamu-table-header>
Expiration in seconds
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
1000
</edukamu-table-cell>
<edukamu-table-cell>
*null*
</edukamu-table-cell>
<edukamu-table-cell>
1000
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
1000
</edukamu-table-cell>
<edukamu-table-cell>
-1
</edukamu-table-cell>
<edukamu-table-cell>
*This item will never expire*.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
1000
</edukamu-table-cell>
<edukamu-table-cell>
2000
</edukamu-table-cell>
<edukamu-table-cell>
2000
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
Container.DefaultTimeToLive
</edukamu-table-header>
<edukamu-table-header>
Item.ttl
</edukamu-table-header>
<edukamu-table-header>
Expiration in seconds
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
*null*
</edukamu-table-cell>
<edukamu-table-cell>
*null*
</edukamu-table-cell>
<edukamu-table-cell>
*This item will never expire*.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
*null*
</edukamu-table-cell>
<edukamu-table-cell>
-1
</edukamu-table-cell>
<edukamu-table-cell>
*This item will never expire*.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
*null*
</edukamu-table-cell>
<edukamu-table-cell>
2000
</edukamu-table-cell>
<edukamu-table-cell>
*TTL is disabled at the container level. This item will never expire.*
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section>
<edukamu-section class="edukamu-included-only-in-mobile">
<edukamu-section class="edukamu-kuvateksti">
The Table above is horizontally scrollable.
</edukamu-section>
</edukamu-section>
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step 4. Considering Data Retention with TTL
</edukamu-collapse-hidden-title>

Azure Cosmos DB only charges for storage you directly consume in real time, and you don't have to pre-reserve storage in advance. In high-write scenarios, TTL values can be used to save on data storage costs in Azure Cosmos DB. Data that has already been shipped out to data warehouses or aggregated and stored in other forms or elsewhere can be immediately purged to ensure that you only keep fresh and relevant data in local SSD storage.

Consider solutions such to aggregate and migrate data such as:

- Change feed
- Azure Data Warehouse
- Azure Blob Storage

When designing your solution, game plan how long your data will need to be retained in Azure Cosmos DB before being migrated across your entire Azure solution space to minimize storage costs.

</edukamu-collapse>
<br>


When planning to implement NoSQL database solutions with services like Azure Cosmos DB, a multitude of factors need to be considered. While the steps covered on this page are a good place to begin, each scenario and use case should be assessed separately.

As such, remember to always plan according to the project at hand. That way, you'll help secure success for you, your team, and your application!

It's time for another exercise. Good luck!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Planning NoSQL
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/planning-nosql-solutions-question-scroll-1.yaml" id="any0d77zf9wbe3ag">
<br>

</edukamu-collapse>
<br>


After planning, the next logical step is to start implementing a NoSQL solution. That's also the center of our attention on the following page!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
