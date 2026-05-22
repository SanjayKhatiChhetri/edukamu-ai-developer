<edukamu-video content="/videos/devai-3-unit3-video.yaml"/>
<br>

## Large-scale Analytics

Welcome to the third and final unit of this course!

In the digital age, in which information is abundant and diverse, the ability to extract meaningful insights from data has become paramount. Data analytics, at its core, is the systematic process of examining, cleaning, transforming, and modeling data to uncover valuable information, draw conclusions, and support decision-making.

In our data-driven world, organizations leverage data analytics to gain a competitive edge, enhance operational efficiency, and make informed strategic choices. Whether it's understanding customer behavior, optimizing business processes, or predicting future trends, data analytics serves as the compass guiding modern enterprises.

We'll start our journey into the world of data analytics by getting to know large-scale analytics. Afterwards, we'll explore real-time analytics before wrapping up the course with data visualization.

Without further ado, let's get familiar with large-scale analytics.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Large-scale Analytics
</edukamu-collapse-hidden-title>

Large-scale data analytics solutions combine conventional data warehousing used to support business intelligence (BI) with data lakehouse techniques that are used to integrate data from files and external sources. A conventional data warehousing solution typically involves copying data from transactional data stores into a relational database with a schema that's optimized for querying and building multidimensional models.

Data lakehouse solutions on the other hand are used with large volumes of data in multiple formats, which is batch loaded or captured in real-time streams and stored in a data lake from which distributed processing engines like Apache Spark are used to process it.

<!-- <iframe width="640" height="360" src="https://www.microsoft.com/en-us/videoplayer/embed/RE57fRS?postJsllMsg=true" frameborder="0" allowfullscreen></iframe>
 <!--https://learn.microsoft.com/en-us/training/paths/azure-data-fundamentals-explore-data-warehouse-analytics/
<br> -->

</edukamu-collapse>
<br>

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="elisa-logo">
### Scenario: Data and AI
</edukamu-collapse-hidden-title>

One of the goals of GreenThrive Networks was to make more data-based decisions and help their customers with their own business to success. When talking about understanding the data stored in the system, they built data visualization reports and dashboards for customers using Power BI. Customers can read and understand their gardening related system better and achieve even better results on growing new plants, flowers etc. 

GreenThrive Networks’ next bigger features in the roadmap are based on artificial intelligence. 

One of those is a forecasting system based on machine learning that uses collected data to train a customized machine learning model to predict the customer's growing needs. After the model is trained, the customer can receive tailored suggestions and growing projections based on weather forecasts and other factors.

Another one of those is a bot that answers natural language questions about the data. Bot uses Azure OpenAI Service and large language models to understand question, process it by grounding the answer to question from backend, and response in natural language. It supports many languages across the globe, so everyone can use their own native language to ask questions and get answers.

</edukamu-collapse>
<br>


Organizations use analytics platforms to build large-scale data analytics solutions that generate insights and drive success. Microsoft provides multiple technologies for such purposes.

Let's go through the most important of them.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Data Warehousing Architecture
</edukamu-collapse-hidden-title>

Large-scale data analytics architecture can vary, as can the specific technologies used to implement it; but in general, the following elements are included:

<edukamu-image url="/graphics/module3/modern-data-warehousing.png" alt="Diagram showing data ingestion and processing, an analytical data store, an analytical data model, and data visualization."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

1. **Data ingestion and processing** – data from one or more transactional data stores, files, real-time streams, or other sources is loaded into a data lake or a relational data warehouse. The load operation usually involves an *extract, transform, and load* (ETL) or *extract, load, and transform* (ELT) process in which the data is cleaned, filtered, and restructured for analysis. In ETL processes, the data is transformed before being loaded into an analytical store, while in an ELT process the data is copied to the store and then transformed. Either way, the resulting data structure is optimized for analytical queries. The data processing is often performed by distributed systems that can process high volumes of data in parallel using multi-node clusters. Data ingestion includes both batch processing of static data and real-time processing of streaming data.
2. **Analytical data store** – data stores for large scale analytics include relational *data warehouses*, filesystem based *data lakes*, and hybrid architectures that combine features of data warehouses and data lakes (sometimes called *data lakehouses* or *lake databases*). We'll discuss these in more depth later.
3. **Analytical data model** – while data analysts and data scientists can work with the data directly in the analytical data store, it’s common to create one or more data models that pre-aggregate the data to make it easier to produce reports, dashboards, and interactive visualizations. Often these data models are described as *cubes*, in which numeric data values are aggregated across one or more dimensions (for example, to determine total sales by product and region). The model encapsulates the relationships between data values and dimensional entities to support "drill-up/drill-down" analysis.
4. **Data visualization** – data analysts consume data from analytical models, and directly from analytical stores to create reports, dashboards, and other visualizations. Additionally, users in an organization who may not be technology professionals might perform self-service data analysis and reporting. The visualizations from the data show trends, comparisons, and key performance indicators (KPIs) for a business or other organization, and can take the form of printed reports, graphs and charts in documents or PowerPoint presentations, web-based dashboards, and interactive environments in which users can explore data visually.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Data Ingestion Pipelines
</edukamu-collapse-hidden-title>

Now that you understand a little about the architecture of a large-scale data warehousing solution and some of the distributed processing technologies that can be used to handle large volumes of data, it's time to explore how data is ingested into an analytical data store from one or more sources.

<edukamu-image url="/graphics/module3/pipeline.png" alt="Diagram showing a pipeline."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

On Azure, large-scale data ingestion is best implemented by creating pipelines that orchestrate ETL processes. You can create and run pipelines using Azure Data Factory, or you can use a similar pipeline engine in Azure Synapse Analytics or Microsoft Fabric if you want to manage all of the components of your data analytics solution in a unified workspace.

In either case, pipelines consist of one or more activities that operate on data. An input dataset provides the source data, and activities can be defined as a data flow that incrementally manipulates the data until an output dataset is produced. Pipelines can connect to external data sources to integrate with a wide variety of data services.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Analytical Data Stores
</edukamu-collapse-hidden-title>

There are two common types of analytical data store: 1) data warehouses and 2) data lakehouses. Let's review both of them.

### Data Warehouses

<edukamu-image url="/graphics/module3/data-warehouse.png" alt="Diagram showing a data warehouse with a star schema."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

A *data warehouse* is a relational database in which the data is stored in a schema that is optimized for data analytics rather than transactional workloads. Commonly, the data from a transactional store is transformed into a schema in which numeric values are stored in central *fact* tables, which are related to one or more *dimension* tables that represent entities by which the data can be aggregated. For example a fact table might contain sales order data, which can be aggregated by customer, product, store, and time dimensions (enabling you, for example, to easily find monthly total sales revenue by product for each store).

This kind of fact and dimension table schema is called a *star schema*; though it's often extended into a *snowflake schema* by adding additional tables related to the dimension tables to represent dimensional hierarchies (for example, product might be related to product categories). A data warehouse is a great choice when you have transactional data that can be organized into a structured schema of tables, and you want to use SQL to query them.

### Data Lakehouses

<edukamu-image url="/graphics/module3/data-lake.png" alt="Diagram showing a data lake in which files are abstracted by tables."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

A *data lake* is a file store, usually on a distributed file system for high performance data access. Technologies like Spark or Hadoop are often used to process queries on the stored files and return data for reporting and analytics. These systems often apply a *schema-on-read* approach to define tabular schemas on semi-structured data files at the point where the data is read for analysis, without applying constraints when it's stored. Data lakes are great for supporting a mix of structured, semi-structured, and even unstructured data that you want to analyze without the need for schema enforcement when the data is written to the store.

You can use a hybrid approach that combines features of data lakes and data warehouses in a *lake database* or *data lakehouse*. The raw data is stored as files in a data lake, and a relational storage layer abstracts the underlying files and expose them as tables, which can be queried using SQL. SQL pools in Azure Synapse Analytics include *PolyBase*, which enables you to define external tables based on files in a datalake (and other sources) and query them using SQL.

Synapse Analytics also supports a Lake Database approach in which you can use database templates to define the relational schema of your data warehouse, while storing the underlying data in data lake storage – separating the storage and compute for your data warehousing solution. Data lakehouses are a relatively new approach in Spark-based systems, and are enabled through technologies like *Delta Lake*; which adds relational storage capabilities to Spark, so you can define tables that enforce schemas and transactional consistency, support batch-loaded and streaming data sources, and provide a SQL API for querying.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Platform-as-a-service Solutions (PaaS)
</edukamu-collapse-hidden-title>

On Azure, there are three main platform-as-a-service (PaaS) services that you can use to implement a large-scale analytical store. They all have their own characteristics and strengths.

### 1. Azure Synapse Analytics

<edukamu-image url="/graphics/module3/azure-synapse.png" alt="Screenshot of Azure Synapse Analytics logo."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

Azure Synapse Analytics is a unified, end-to-end solution for large scale data analytics. It brings together multiple technologies and capabilities, enabling you to combine the data integrity and reliability of a scalable, high-performance SQL Server based relational data warehouse with the flexibility of a data lake and open-source Apache Spark. It also includes native support for log and telemetry analytics with Azure Synapse Data Explorer pools, as well as built in data pipelines for data ingestion and transformation.

All Azure Synapse Analytics services can be managed through a single, interactive user interface called Azure Synapse Studio, which includes the ability to create interactive notebooks in which Spark code and markdown content can be combined. Synapse Analytics is a great choice when you want to create a single, unified analytics solution on Azure.

### 2. Azure Databricks

<edukamu-image url="/graphics/module3/azure-databricks.png" alt="Screenshot of Azure Databricks logo."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

Azure Databricks is an Azure implementation of the popular Databricks platform. Databricks is a comprehensive data analytics solution built on Apache Spark, and offers native SQL capabilities as well as workload-optimized Spark clusters for data analytics and data science. Databricks provides an interactive user interface through which the system can be managed and data can be explored in interactive notebooks.

Due to its common use on multiple cloud platforms, you might want to consider using Azure Databricks as your analytical store if you want to use existing expertise with the platform or if you need to operate in a multi-cloud environment or support a cloud-portable solution.

### 3. Azure HDInsight

<edukamu-image url="/graphics/module3/hdinsight.png" alt="Screenshot of Azure HDInsight logo."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

Azure HDInsight is an Azure service that supports multiple open-source data analytics cluster types. Although not as user-friendly as Azure Synapse Analytics and Azure Databricks, it can be a suitable option if your analytics solution relies on multiple open-source frameworks or if you need to migrate an existing on-premises Hadoop-based solution to the cloud.

**Note**: Each of these services can be thought of as an analytical data store, in the sense that they provide a schema and interface through which the data can be queried. In many cases however, the data is actually stored in a data lake and the service is used to process the data and run queries. Some solutions might even combine the use of these services. An extract, load, and transform (ELT) ingestion process might copy data into the data lake, and then use one of these services to transform the data, and another to query it. For example, a pipeline might use a MapReduce job running in HDInsight or a notebook running in Azure Databricks to process a large volume of data in the data lake, and then load it into tables in a SQL pool in Azure Synapse Analytics.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Did you notice something familiar when exploring the three PaaS solutions? They're the same tools we covered earlier during the non-relational data section. Even though the services are used for different purposes, they do overlap at times!

As we delve deeper into data analytics, it's crucial to acknowledge challenges such as data quality, privacy concerns, and the ethical use of information. Striking a balance between extracting value from data and respecting individual privacy is an ongoing conversation in the field. Luckily, Microsoft Azure contains tools for addressing these concerns.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Explore Azure Synapse Analytics
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

If you have an active Azure subscription, you can explore the services we just covered over at Microsoft’s Learn platform.

The exercise is designed to familiarize you with some key elements of a large-scale data warehousing solution, not as a comprehensive guide to performing advanced data analysis with Azure Synapse Analytics. The exercise should take around 30 minutes to complete.

<edukamu-button url="https://microsoftlearning.github.io/DP-900T00A-Azure-Data-Fundamentals/Instructions/Labs/dp900-04-synapse-lab.html">Practice: Explore Azure Synapse Analytics (Microsoft Learn)</edukamu-button>
<br>

If you aren't able to access Azure, don't worry. These practice exercises are not a requirement for completing this course.

</edukamu-collapse>
<br>


There are many services for aimed at scalable analytics within Microsoft Azure, and there's something for every imaginable use case. Sometimes, however, tools as advanced as the ones we've covered on this page might be a little complex or even expensive.

Whenever you're looking for simple, all-in-one kind of solutions, you should definitely check out Microsoft Fabric. It is an all-in-one analytics solution for enterprises that covers everything from data movement to data science, real-time analytics, and business intelligence


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Microsoft Fabric
</edukamu-collapse-hidden-title>

<edukamu-image url="/graphics/module3/fabric-icon.png" alt="Screenshot of Microsoft Fabric logo."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

Scalable analytics with PaaS services can be complex, fragmented, and expensive. With Microsoft Fabric, you don't have to spend all of your time combining various services and implementing interfaces through which business users can access them. Instead, you can use a single product that is easy to understand, set up, create, and manage. Fabric is a unified software-as-a-service (SaaS) offering, with all your data stored in a single open format in OneLake.

OneLake is Fabric's lake-centric architecture that provides a single, integrated environment for data professionals and the business to collaborate on data projects. Think of it like OneDrive for data; OneLake combines storage locations across different regions and clouds into a single logical lake, without moving or duplicating data.  Data can be stored in any file format in OneLake and can be structured or unstructured. For tabular data, the analytical engines in Fabric will write data in delta format when writing to OneLake. All engines will know how to read this format and treat delta files as tables no matter which engine writes it.

With Fabric, you don't need to piece together different services from multiple vendors. Instead, you can enjoy a highly integrated, end-to-end, and easy-to-use product that is designed to simplify your analytics needs.

The platform is built on a foundation of Software as a Service (SaaS), which takes simplicity and integration to a whole new level.


### SaaS Foundation

Microsoft Fabric brings together new and existing components from Power BI, Azure Synapse, and Azure Data Factory into a single integrated environment. These components are then presented in various customized user experiences.

<edukamu-image url="/graphics/module3/saas-foundation.png" alt="Diagram of the software as a service foundation beneath the different experiences of Fabric."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

Fabric brings together experiences such as Data Engineering, Data Factory, Data Science, Data Warehouse, Real-Time Analytics, and Power BI onto a shared SaaS foundation. This integration provides the following advantages:
* An extensive range of deeply integrated analytics in the industry.
* Shared experiences across experiences that are familiar and easy to learn.
* Developers can easily access and reuse all assets.
* A unified data lake that allows you to retain the data where it is while using your preferred analytics tools.
* Centralized administration and governance across all experiences.

With the Microsoft Fabric SaaS experience, all the data and the services are seamlessly integrated. IT teams can centrally configure core enterprise capabilities and permissions are automatically applied across all the underlying services. Additionally, data sensitivity labels are inherited automatically across the items in the suite.

Fabric allows creators to concentrate on producing their best work, freeing them from the need to integrate, manage, or understand the underlying infrastructure that supports the experience.

</edukamu-collapse>


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Exploring Microsoft Fabric
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

If you have an active Azure subscription, you can explore Microsoft Fabric over at Microsoft’s Learn platform.

The exercise is designed to familiarize you with some key elements of a large-scale data analytics solution, not as a comprehensive guide to performing advanced data analysis with Microsoft Fabric. The exercise should take around 25 minutes to complete.

<edukamu-button url="https://microsoftlearning.github.io/DP-900T00A-Azure-Data-Fundamentals/Instructions/Labs/dp900-04b-fabric-lake-lab.html">Practice: Exploring Microsoft Fabric (Microsoft Learn)</edukamu-button>
<br>

If you aren't able to access Azure, don't worry. These practice exercises are not a requirement for completing this course.

</edukamu-collapse>
<br>


Large-scale data analytics is extremely useful for most modern companies, and developers with deep understanding of data and its behavior are valued greatly. You've now taken your first steps towards expertise of the field!

You know what's coming next, don't you? It's time for another exercise!

We've covered a lot on this page, so make sure to recap and review before tackling the exercise.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Large-scale Analytics
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module3/large-scale-analytics-text-poll.yaml" id="ig1i7ufubj2j58l6"/>
<br>
<edukamu-text-poll url="/exercises/module3/large-scale-analytics-text-poll-2.yaml" id="i0z0wbg3uts944eb"/>
<br>
<edukamu-text-poll url="/exercises/module3/large-scale-analytics-text-poll-3.yaml" id="136461y5f159g1pa"/>
<br>
<edukamu-text-poll url="/exercises/module3/large-scale-analytics-text-poll-4.yaml" id="ebcn27yx02806p6j"/>
<br>
<edukamu-text-poll url="/exercises/module3/large-scale-analytics-text-poll-5.yaml" id="0w20pv2kohmdoep1"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/3/large-scale-analytics?question=ig1i7ufubj2j58l6">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


Data analytics is an extensive field, and large-scale analytics is just one of its dimensions. In summary, it is a complex workload that can involve many different technologies, but there's a lot more still left to learn and discover in the world of Microsoft Azure.

Next, we'll focus on real-time analytics. It's still analytics, but with a whole different approach!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
