## Enriched Data and Query Design

In today's digital era, data is more than just raw information – it's a strategic asset that, when properly harnessed, can drive innovation and transformation.

Enriched data, on the other hand, is something that transforms conventional datasets into knowledge repositories: It involves the augmentation of information with contextual details, making it more valuable, insightful, and conducive to intelligent decision-making.

In order to make use of this data, we need to be smart and think ahead. Query design serves as the key to unlock the treasure trove of enriched data. Crafting well-designed queries is an art that allows you to extract precisely what you need from your data, fostering efficiency and precision in your AI applications.

On this page, we’ll take our first look at these exciting technologies. It’s the second to last topic of this course, so keep on going strong until the end!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Enriched Data and Knowledge Store
</edukamu-collapse-hidden-title>

A knowledge store is persistent storage of enriched content. The purpose of a knowledge store is to store the data generated from AI enrichment in a container. For example, you may want to save the results of an AI skillset that generates captions from images.

<edukamu-image url="/graphics/module5/knowledge-store-diagram.png" alt="Visualization of knowledge store." style="max-width: 80%;"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Recall that skillsets move a document through a sequence of enrichments that invoke transformations, such as recognizing entities or translating text. The outcome can be a search index, or projections in a knowledge store. The two outputs, search index and knowledge store, are mutually exclusive products of the same pipeline; derived from the same inputs, but resulting in output that is structured, stored, and used in different applications.

While the focus of an Azure Cognitive Search solution is usually to create a searchable index, you can also take advantage of its data extraction and enrichment capabilities to persist the enriched data in a knowledge store for further analysis or processing.

A knowledge store can contain one or more of three types of projection of the extracted data:
* Table projections are used to structure the extracted data in a relational schema for querying and visualization
* Object projections are JSON documents that represent each data entity
* File projections are used to store extracted images in JPG format

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Creating Indexes in Azure
</edukamu-collapse-hidden-title>

Before using an indexer to create an index, you'll first need to make your data available in a supported data source. Supported data sources include:
* Cosmos DB (SQL API)
* Azure SQL (database, managed instance, and SQL Server on an Azure VM)
* Azure Storage (Blob Storage, Table Storage, ADLS Gen2)

Once your data is in an Azure data source, you can begin using Azure Cognitive Search. Contained within the Azure Cognitive Search service in Azure portal is the Import data wizard, which automates processes in the Azure portal to create various objects needed for the search engine. You can see it in action when creating any of the following objects using the Azure portal:

* **Data Source**: Persists connection information to source data, including credentials. A data source object is used exclusively with indexers.
* **Index**: Physical data structure used for full text search and other queries.
* **Indexer**: A configuration object specifying a data source, target index, an optional AI skillset, optional schedule, and optional configuration settings for error handling and base-64 encoding.
* **Skillset**: A complete set of instructions for manipulating, transforming, and shaping content, including analyzing and extracting information from image files. Except for very simple and limited structures, it includes a reference to an Azure AI services resource that provides enrichment.
* **Knowledge store**: Stores output from an AI enrichment pipeline in tables and blobs in Azure Storage for independent analysis or downstream processing.

To use Azure Cognitive Search, you'll need an Azure Cognitive Search resource. You can create a resource in the Azure portal. Once the resource is created, you can manage components of your service from the resource *Overview* page in the portal.

Here’s what the page looks like:

<edukamu-image url="/graphics/module5/azure-search-portal.png" alt="Screenshot of the overview page of an Azure AI Search resource." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br> 

You can build Azure search indexes using the Azure portal or programmatically with the REST API or software development kits (SDKs).

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Query Design
</edukamu-collapse-hidden-title>

Index and query design are closely linked. After we build the index, we can perform queries. A crucial component to understand is that the schema of the index determines what queries can be answered.

Azure Cognitive Search queries can be submitted as an HTTP or REST API request, with the response coming back as JSON. Queries can specify what fields are searched and returned, how search results are shaped, and how the results should be filtered or sorted. A query that doesn't specify the field to search will execute against all the searchable fields within the index.

Azure Cognitive Search supports two types of syntax: simple and full Lucene. Simple syntax covers all of the common query scenarios, while full Lucene is useful for advanced scenarios.

### Simple Query Requests

A query request is a list or words (search terms) and query operators (simple or full) of what you would like to see returned in a result set. Let's look what components make up a search query. Consider this simple search example:

*coffee (-"busy" + "wifi")*

This query is trying to find content about coffee, excluding busy and including wifi.

Breaking the query into components, it's made up of search terms, (*coffee*), plus two verbatim phrases, "*busy*" and "*wifi*", and operators (-, +, and ( )). The search terms can be matched in the search index in any order or location in the content. The two phrases will only match with exactly what is specified, so wi-fi would not be a match. Finally, a query can contain a number of operators. In this example, the - operator tells the search engine that these phrases should *NOT* be in the results. The parenthesis group terms together, and set their precedence.

By default, the search engine will match any of the terms in the query. Content containing just *coffee* would be a match. In this example, using -"*busy*" would lead to the search results including all content that doesn't have the exact string "busy" in it.

The simple query syntax in Azure Cognitive Search excludes some of the more complex features of the full Lucene query syntax, and it's the default search syntax for queries.


</edukamu-collapse>
<br>


Together, enriched data and query design form the backbone of AI-driven solutions in Azure, laying the foundation for applications ranging from advanced search functionalities to knowledge mining and beyond.

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Exploring Azure Cognitive Search Indexes
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked Practice are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

If you have an active Azure subscription, you can try out the capabilities we’ve learned in this unit on your own over at Microsoft’s Learn platform.

<edukamu-button url="https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/11-ai-search.html">Practice: Exploring Azure Cognitive Search Indexes (Microsoft Learn)</edukamu-button>
<br>

</edukamu-collapse>
<br> -->

<edukamu-section class="slate-section slate-blue">
As you continue exploring the world of Microsoft Azure and AI, you’ll surely come across enriched data and query design many times.

The topics we’ve just explored might be quite complicated, so make sure to recap a little before taking on the following exercise.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Enriched Data and Query Design
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module5/enriched-data-and-query-question-scroll.yaml" id="v5p1t8xr7b0gq3df">
<br>


</edukamu-collapse>
<br>


On this page, we've explored enriched data and query design from various perspectives. Take a while to think how you could also benefit from your new skills! Maybe not now, but in the future? Whenever you're ready, feel free to move on to the last topic of this course: Azure AI Search!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
