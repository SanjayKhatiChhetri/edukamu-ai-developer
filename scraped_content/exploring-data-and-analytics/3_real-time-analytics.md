## Real-time Analytics

When developing effective business models in the digital age, data analytics is the key to success and improvement. In the fast-paced landscape of data-driven decision-making, however, traditional large-scale analytics faces challenges in keeping up with the need for instant insights. At times, we need something different, something dynamic and responsive. We need real-time analytics.

Large-scale analytics often involves processing vast volumes of data in batches, typically from data warehouses or data lakes. This approach is well-suited for complex analytical queries and in-depth business intelligence, but the time lag between data generation and analysis can be a limitation, especially in scenarios requiring immediate insights for agile decision-making.

Real-time analytics is geared towards processing data as it is generated, allowing organizations to derive insights in near real-time. This means that the moment data enters the system, it is analyzed and interpreted, providing instantaneous feedback. This shift from a batch-oriented to a streaming model revolutionizes how businesses respond to events, enabling them to make decisions on the fly.

Real-time analytics might sound like the ultimate solution to all data analyzing needs, but both styles have their advantages. Before delving deeper into real-time analytics, have a look at the following.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Large-scale vs. Real-time
</edukamu-collapse-hidden-title>

Large-scale analytics and real-time analytics both have their advantages and disadvantages. If you ever work with data, you'll most probably get to use them both, so it's good to be aware of their key differences from the get-go.

### Key Differences

1. **Time Sensitivity**
   * Large-Scale Analytics: Primarily concerned with processing historical data in batches
   * Real-Time Analytics: Focuses on analyzing data as it arrives, minimizing processing delays

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Processing Paradigm</span>
</li>
</ol>
</edukamu-section>
* Large-Scale Analytics: Relies on batch processing, suitable for complex queries and comprehensive reports
* Real-Time Analytics: Embraces streaming processing, allowing for immediate insights and rapid decision-making

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Use Cases</span>
</li>
</ol>
</edukamu-section>
* Large-Scale Analytics: Ideal for in-depth trend analysis, historical reporting, and business intelligence
* Real-Time Analytics: Suitable for scenarios demanding instant response, such as fraud detection, IoT applications, and dynamic pricing

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Data Freshness</span>
</li>
</ol>
</edukamu-section>
* Large-Scale Analytics: Provides insights based on historical snapshots
* Real-Time Analytics: Offers a real-time view of the current state, enabling proactive decision-making

<!-- 2. **Processing Paradigm**
   * Large-Scale Analytics: Relies on batch processing, suitable for complex queries and comprehensive reports
   * Real-Time Analytics: Embraces streaming processing, allowing for immediate insights and rapid decision-making
3. **Use Cases**
   * Large-Scale Analytics: Ideal for in-depth trend analysis, historical reporting, and business intelligence
   * Real-Time Analytics: Suitable for scenarios demanding instant response, such as fraud detection, IoT applications, and dynamic pricing
4. **Data Freshness**
   * Large-Scale Analytics: Provides insights based on historical snapshots
   * Real-Time Analytics: Offers a real-time view of the current state, enabling proactive decision-making -->

</edukamu-collapse>
<br>


In summary, real-time analytics brings a transformative shift from history-focused analysis to proactive decision-making. It's time to get to know the techniques behind this rapid and dynamic method!

First, we'll need to get familiar with batch and stream processing.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Batch and Stream Processing
</edukamu-collapse-hidden-title>

Data processing is simply the conversion of raw data to meaningful information through a process. There are two general ways to process data:
* *Batch processing*, in which multiple data records are collected and stored before being processed together in a single operation.
* *Stream processing*, in which a source of data is constantly monitored and processed in real time as new data events occur.

Next, let's explore them both.

### Batch Processing

In batch processing, newly arriving data elements are collected and stored, and the whole group is processed together as a batch. Exactly when each group is processed can be determined in a number of ways. For example, you can process data based on a scheduled time interval (for example, every hour), or it could be triggered when a certain amount of data has arrived, or as the result of some other event.

For example, suppose you want to analyze road traffic by counting the number of cars on a stretch of road. A batch processing approach to this would require that you collect the cars in a parking lot, and then count them in a single operation while they're at rest.

<edukamu-image url="/graphics/module3/batch.png" alt="Cars being counted in a parking lot."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

If the road is busy, with a large number of cars driving along at frequent intervals, this approach may be impractical; and note that you don't get any results until you have parked a batch of cars and counted them.

A real-world example of batch processing is the way that credit card companies handle billing. The customer doesn't receive a bill for each separate credit card purchase but one monthly bill for all of that month's purchases.

Advantages of batch processing include:
* Large volumes of data can be processed at a convenient time.
* It can be scheduled to run at a time when computers or systems might otherwise be idle, such as overnight, or during off-peak hours.

Disadvantages of batch processing include:
* The time delay between ingesting the data and getting the results.
* All of a batch job's input data must be ready before a batch can be processed. This means data must be carefully checked. Problems with data, errors, and program crashes that occur during batch jobs bring the whole process to a halt. The input data must be carefully checked before the job can be run again. Even minor data errors can prevent a batch job from running.

### Stream Processing

In stream processing, each new piece of data is processed when it arrives. Unlike batch processing, there's no waiting until the next batch processing interval - data is processed as individual units in real-time rather than being processed a batch at a time. Stream data processing is beneficial in scenarios where new, dynamic data is generated on a continual basis.

For example, a better approach to our hypothetical car counting problem might be to apply a streaming approach, by counting the cars in real-time as they pass:

<edukamu-image url="/graphics/module3/stream.gif" alt="Animation. Cars being counted as they pass."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

In this approach, you don't need to wait until all of the cars have parked to start processing them, and you can aggregate the data over time intervals; for example, by counting the number of cars that pass each minute.

Real world examples of streaming data include:
* A financial institution tracks changes in the stock market in real time, computes value-at-risk, and automatically rebalances portfolios based on stock price movements.
* An online gaming company collects real-time data about player-game interactions, and feeds the data into its gaming platform. It then analyzes the data in real time, offers incentives and dynamic experiences to engage its players.
* A real-estate website that tracks a subset of data from mobile devices, and makes real-time property recommendations of properties to visit based on their geo-location.

Stream processing is ideal for time-critical operations that require an instant real-time response. For example, a system that monitors a building for smoke and heat needs to trigger alarms and unlock doors to allow residents to escape immediately in the event of a fire.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Understanding the Difference
</edukamu-collapse-hidden-title>

Apart from the way in which batch processing and streaming processing handle data, there are other differences:
* *Data scope*: Batch processing can process all the data in the dataset. Stream processing typically only has access to the most recent data received, or within a rolling time window (the last 30 seconds, for example).
* *Data size*: Batch processing is suitable for handling large datasets efficiently. Stream processing is intended for individual records or *micro batches* consisting of few records.
* *Performance*: Latency is the time taken for the data to be received and processed. The latency for batch processing is typically a few hours. Stream processing typically occurs immediately, with latency in the order of seconds or milliseconds.
* *Analysis*: You typically use batch processing to perform complex analytics. Stream processing is used for simple response functions, aggregates, or calculations such as rolling averages.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Combining Batch and Stream Processing
</edukamu-collapse-hidden-title>

Many large-scale analytics solutions include a mix of batch and stream processing, enabling both historical and real-time data analysis. It's common for stream processing solutions to capture real-time data, process it by filtering or aggregating it, and present it through real-time dashboards and visualizations (for example, showing the running total of cars that have passed along a road within the current hour), while also persisting the processed results in a data store for historical analysis alongside batch processed data (for example, to enable analysis of traffic volumes over the past year).

Even when real-time analysis or visualization of data is not required, streaming technologies are often used to capture real-time data and store it in a data store for subsequent batch processing (this is the equivalent of redirecting all of the cars that travel along a road into a parking lot before counting them).

The following diagram shows some ways in which batch and stream processing can be combined in a large-scale data analytics architecture.

<edukamu-image url="/graphics/module3/lambda-architecture.png" alt="A data analytics architecture that includes batch and stream processing."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

1. Data events from a streaming data source are captured in real-time.
2. Data from other sources is ingested into a data store (often a data lake) for batch processing.
3. If real-time analytics is not required, the captured streaming data is written to the data store for subsequent batch processing.
4. When real-time analytics is required, a stream processing technology is used to prepare the streaming data for real-time analysis or visualization; often by filtering or aggregating the data over temporal windows.
5. The non-streaming data is periodically batch processed to prepare it for analysis, and the results are persisted in an analytical data store (often referred to as a data warehouse) for historical analysis.
6. The results of stream processing may also be persisted in the analytical data store to support historical analysis.
7. Analytical and visualization tools are used to present and explore the real-time and historical data.

Commonly used solution architectures for combined batch and stream data processing include *lambda* and *delta* architectures. Details of these architectures are beyond the scope of this course, but they incorporate technologies for both large-scale batch data processing and real-time stream processing to create an end-to-end analytical solution.

</edukamu-collapse>
<br>


In essence, batch processing is designed for in-depth historical analysis, while stream processing is tailored for real-time insights and dynamic decision-making. In a way, it's analogous to the difference between large-scale and real-time analytics.

Next, we'll take a closer look at stream processing, the rapid and dynamic method.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Understanding Stream Processing Architecture
</edukamu-collapse-hidden-title>

There are many technologies that you can use to implement a stream processing solution, but while specific implementation details may vary, there are common elements to most streaming architectures.

At its simplest, a high-level architecture for stream processing looks like this:

<edukamu-image url="/graphics/module3/stream-architecture.png" alt="An event generates data, which is captured in a queue before being processed, and the results are written to a data store or visualization."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

1. An event generates some data. This might be a signal being emitted by a sensor, a social media message being posted, a log file entry being written, or any other occurrence that results in some digital data.
2. The generated data is captured in a streaming *source* for processing. In simple cases, the source may be a folder in a cloud data store or a table in a database. In more robust streaming solutions, the source may be a "queue" that encapsulates logic to ensure that event data is processed in order and that each event is processed only once.
3. The event data is processed, often by a perpetual query that operates on the event data to select data for specific types of events, project data values, or aggregate data values over temporal (time-based) periods (or *windows*) - for example, by counting the number of sensor emissions per minute.
4. The results of the stream processing operation are written to an output (or *sink*), which may be a file, a database table, a real-time visual dashboard, or another queue for further processing by a subsequent downstream query.

### Real-time analytics in Azure

Microsoft Azure supports multiple technologies that you can use to implement real-time analytics of streaming data, including:
* **Azure Stream Analytics**: A platform-as-a-service (PaaS) solution that you can use to define *streaming jobs* that ingest data from a streaming source, apply a perpetual query, and write the results to an output.
* **Spark Structured Streaming**: An open-source library that enables you to develop complex streaming solutions on Apache Spark based services, including **Azure Synapse Analytics**, **Azure Databricks**, and **Azure HDInsight**.
* **Azure Data Explorer**: A high-performance database and analytics service that is optimized for ingesting and querying batch or streaming data with a time-series element, and which can be used as a standalone Azure service or as an **Azure Synapse Data Explorer** runtime in an Azure Synapse Analytics workspace.

### Sources for Stream Processing

The following services are commonly used to ingest data for stream processing on Azure:
* **Azure Event Hubs**: A data ingestion service that you can use to manage queues of event data, ensuring that each event is processed in order, exactly once.
* **Azure IoT Hub**: A data ingestion service that is similar to Azure Event Hubs, but which is optimized for managing event data from *Internet-of-things* (IoT) devices.
* **Azure Data Lake Store Gen 2**: A highly scalable storage service that is often used in *batch processing* scenarios, but which can also be used as a source of streaming data.
* **Apache Kafka**: An open-source data ingestion solution that is commonly used together with Apache Spark. You can use Azure HDInsight to create a Kafka cluster.

### Sinks for Stream Processing

The output from stream processing is often sent to the following services:
* **Azure Event Hubs**: Used to queue the processed data for further downstream processing.
* **Azure Data Lake Store Gen 2 or Azure blob storage**: Used to persist the processed results as a file.
* **Azure SQL Database or Azure Synapse Analytics, or Azure Databricks**: Used to persist the processed results in a database table for querying and analysis.
* **Microsoft Power BI**: Used to generate real time data visualizations in reports and dashboards.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Naturally, Microsoft Azure also includes services for stream analytics. Tools like Azure Stream Analytics can be extremely helpful when rapid, dynamic insights are needed.

Once again, you can explore Azure Stream Analytics with a practical exercise after the introduction if you have an active Azure subscription.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Stream Analytics
</edukamu-collapse-hidden-title>

Azure Stream Analytics is a service for complex event processing and analysis of streaming data. Stream Analytics is used to:
* Ingest data from an *input*, such as an Azure event hub, Azure IoT Hub, or Azure Storage blob container.
* Process the data by using a *query* to select, project, and aggregate data values.
* Write the results to an *output*, such as Azure Data Lake Gen 2, Azure SQL Database, Azure Synapse Analytics, Azure Functions, Azure event hub, Microsoft Power BI, or others.

<edukamu-image url="/graphics/module3/stream-analytics.png" alt="A Stream Analytics job with inputs, a query, and outputs."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

Once started, a Stream Analytics query will run perpetually, processing new data as it arrives in the input and storing results in the output.

Azure Stream Analytics is a great technology choice when you need to continually capture data from a streaming source, filter or aggregate it, and send the results to a data store or downstream process for analysis and reporting.

### Jobs and Clusters

The easiest way to use Azure Stream Analytics is to create a Stream Analytics *job* in an Azure subscription, configure its input(s) and output(s), and define the query that the job will use to process the data. The query is expressed using structured query language (SQL) syntax, and can incorporate static reference data from multiple data sources to supply lookup values that can be combined with the streaming data ingested from an input.

If your stream process requirements are complex or resource-intensive, you can create a Stream Analysis *cluster*, which uses the same underlying processing engine as a Stream Analytics job, but in a dedicated tenant (so your processing is not affected by other customers) and with configurable scalability that enables you to define the right balance of throughput and cost for your specific scenario.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Exploring Azure Stream Analytics
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

If you have an active Azure subscription, you can explore the services we just covered over at Microsoft’s Learn platform.

The sample solution covered in the practice aggregates streaming data from a simulated IoT device.

<edukamu-button url="https://microsoftlearning.github.io/DP-900T00A-Azure-Data-Fundamentals/Instructions/Labs/dp900-05-stream-lab.html">Practice: Exploring Azure Stream Analytics (Microsoft Learn)</edukamu-button>
<br>

</edukamu-collapse>
<br>


Do you still remember Azure Synapse Analytics and Microsoft Fabric, the services we briefly covered earlier?

Azure Synapse Analytics is a unified analytics service that seamlessly combines big data and data warehousing for comprehensive insights, while Microsoft Fabric is an all-in-one analytics solution offering simplified, end-to-end analytics by integrating services like Power BI.

Both of them are also useful when it comes to real-time analytics.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Spark Streaming with Azure Synapse Analytics
</edukamu-collapse-hidden-title>

Apache Spark is a distributed processing framework for large scale data analytics. You can use Spark on Microsoft Azure in the following services:
* Azure Synapse Analytics
* Azure Databricks
* Azure HDInsight

Spark can be used to run code (usually written in Python, Scala, or Java) in parallel across multiple cluster nodes, enabling it to process very large volumes of data efficiently. Spark can be used for both batch processing and stream processing.

### Spark Structured Streaming

To process streaming data on Spark, you can use the Spark Structured Streaming library, which provides an application programming interface (API) for ingesting, processing, and outputting results from perpetual streams of data.

Spark Structured Streaming is built on a ubiquitous structure in Spark called a dataframe, which encapsulates a table of data. You use the Spark Structured Streaming API to read data from a real-time data source, such as a Kafka hub, a file store, or a network port, into a "boundless" dataframe that is continually populated with new data from the stream. You then define a query on the dataframe that selects, projects, or aggregates the data - often in temporal windows. The results of the query generate another dataframe, which can be persisted for analysis or further processing.

<edukamu-image url="/graphics/module3/spark-streaming.png" alt="Streaming data is written to a dataframe, which is queried to create another dataframe for analysis."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

Spark Structured Streaming is a great choice for real-time analytics when you need to incorporate streaming data into a Spark based data lake or analytical data store.

### Delta Lake

Delta Lake is an open-source storage layer that adds support for transactional consistency, schema enforcement, and other common data warehousing features to data lake storage. It also unifies storage for streaming and batch data, and can be used in Spark to define relational tables for both batch and stream processing. When used for stream processing, a Delta Lake table can be used as a streaming source for queries against real-time data, or as a sink to which a stream of data is written.

The Spark runtimes in Azure Synapse Analytics and Azure Databricks include support for Delta Lake.

Delta Lake combined with Spark Structured Streaming is a good solution when you need to abstract batch and stream processed data in a data lake behind a relational schema for SQL-based querying and analysis.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Real-time Analytics with Microsoft Fabric
</edukamu-collapse-hidden-title>

Microsoft Fabric includes native support for real-time data analytics, including real-time data ingestion from multiple streaming sources.

<edukamu-image url="/graphics/module3/fabric-realtime-analytics.png" alt="Diagram of real-time analytics in Microsoft Fabric."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

In Microsoft Fabric, you can use an eventstream to capture real-time event data from a streaming source and persist it in a destination such as a table in a Lakehouse or a KQL database.

When writing eventstream data to a Lakehouse table, you can apply aggregations and filters to summarize the captured data. A KQL database supports tables based on the Data Explorer engine, enabling you to perform real-time analytics on the data in tables by running KQL queries. After capturing real-time data in a table, you can use Power BI in Microsoft Fabric to create real-time data visualizations.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Explore Spark Streaming
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

If you have an active Azure subscription, you can explore the services we just covered over at Microsoft’s Learn platform.

In this practical exercise, you'll use Spark Structured Streaming and delta tables in Azure Synapse Analytics to process streaming data.

<edukamu-button url="https://microsoftlearning.github.io/DP-900T00A-Azure-Data-Fundamentals/Instructions/Labs/dp900-05a-stream-with-spark.html">Practice: Explore Spark Streaming (Microsoft Learn)</edukamu-button>
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Data Insights with Microsoft Fabric
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

If you have an active Azure subscription, you can explore the services we just covered over at Microsoft’s Learn platform.

In this practical exercise, you'll use real-time analytics in Microsoft Fabric in Azure Synapse Analytics to process streaming data.

<edukamu-button url="https://microsoftlearning.github.io/DP-900T00A-Azure-Data-Fundamentals/Instructions/Labs/dp900-05c-fabric-realtime-lab.html">Practice: Data Insights with Microsoft Fabric (Microsoft Learn)</edukamu-button>
<br>

</edukamu-collapse>
<br>


In conclusion, real-time analytics represents a paradigm shift from traditional large-scale analytics by enabling instantaneous processing of data streams and providing immediate insights and responses. This dynamic approach, in contrast to batch processing, empowers organizations to make informed decisions with minimal latency, crucial for scenarios requiring timely actions and adaptability.

Use the following exercise to consolidate your new knowledge.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Real-time Analytics
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/real-time-analytics-question-scroll.yaml" id="4lyj7nys1xm06n7j">
<br>

</edukamu-collapse>
<br>


So far in this unit, we've spent a lot of time covering data analysis, but what can we do after analyzing the data? In order to make the most out of our analyses, we need a way to represent the data in a way that's easy to understand. It's time to learn about data visualization, which is also the last topic of this course.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
