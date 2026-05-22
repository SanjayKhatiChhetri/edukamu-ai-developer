## Azure AI Search

In this unit, we've explored document intelligence and cognitive search from a variety of perspectives. It's time to add one last ingredient into the mix: Azure AI Search.

Think of Azure AI Search as the glue that brings together all the concepts we've covered. It's a cloud-based search service that allows you to not only index and search over your data, but also enrich it with AI to extract deeper meaning and insights. Imagine being able to instantly search through thousands of documents, not just by keywords, but by concepts, entities, and relationships hidden within the text. That's the power of Azure AI Search.

Azure AI Search makes it possible to ingest data from various sources and explore it in-depth with AI. Data professionals and developers can even design custom search experiences, tailoring the system to their specific needs.

In this final section, we’ll spend a while exploring Azure AI Search. Let’s begin!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### What is Azure AI Search?
</edukamu-collapse-hidden-title>

Azure AI Search provides the infrastructure and tools to create search solutions that extract data from various structured, semi-structured, and non-structured documents.

<edukamu-image url="/graphics/module5/5-what-is-azure-search.png" alt="Infographic of Azure Search.">
<br>

Azure AI Search results contain only your data, which can include text inferred or extracted from images, or new entities and key phrases detection through text analytics. It's a Platform as a Service (PaaS) solution. Microsoft manages the infrastructure and availability, allowing your organization to benefit without the need to purchase or manage dedicated hardware resources.

#### Azure AI Search Features

Azure AI Search exists to complement existing technologies and provides a programmable search engine built on Apache Lucene, an open-source software library. It's a highly available platform offering a 99.9% uptime Service Level Agreement (SLA) available for cloud and on-premises assets.

Azure AI Search comes with the following features:

- **Data from any source**: accepts data from any source provided in JSON format, with auto crawling support for selected data sources in Azure.

- **Multiple options for search and analysis**: including vector search, full text, and hybrid search.

- **AI enrichment**: has Azure AI capabilities built in for image and text analysis from raw content.

- **Linguistic analysis**: offers analysis for 56 languages to intelligently handle phonetic matching or language-specific linguistics. Natural language processors available in Azure AI Search are also used by Bing and Office.

- **Configurable user experience**: has options for query syntax including vector queries, text search, hybrid queries, fuzzy search, autocomplete, geo-search filtering based on proximity to a physical location, and more.

- **Azure scale, security, and integration**: at the data layer, machine learning layer, and with Azure AI services and Azure OpenAI.

</edukamu-collapse>
<br>


When it comes to implementing Azure AI Search, it is crucial to consider and understand the targets and goals set for the project. In other words, we’re talking about search indexes and data queries - topics we’ve already explored on this course!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Identifying Search Solution Elements
</edukamu-collapse-hidden-title>

<edukamu-image url="/graphics/module5/5-data-indexing-process-1.png" alt="A screenshot showing the process of data moving from a data source to a search index. The process is automated by an indexer.">
<br>

A *search index* contains your searchable content. In an Azure AI Search solution, you create a search index by moving data through the following indexing pipeline:

1. ***Start* with a data source**: the storage location of your original data artifacts, such as PDFs, video files, and images. For Azure AI Search, your data source could be files in Azure Storage, or text in a database such as Azure SQL Database or Azure Cosmos DB.
2. **Indexer**: automates the movement data from the data *source* through *document cracking* and *enrichment* to *indexing*. An indexer automates a portion of data ingestion and exports the original file type to JSON (in an action called JSON serialization).
3. **Document cracking**: the indexer opens files and extracts content.
4. **Enrichment**: the indexer moves data through AI enrichment, which implements Azure AI on your original data to extract more information. AI enrichment is achieved by adding and combining skills in a *skillset*. A skillset defines the operations that extract and enrich data to make it searchable. These AI skills can be either built-in skills, such as text translation or Optical Character Recognition (OCR), or custom skills that you provide. Examples of AI enrichment include adding captions to a photo and evaluating text sentiment. AI enriched content can be sent to a knowledge store, which persists output from an AI enrichment pipeline in tables and blobs in Azure Storage for independent analysis or downstream processing.
5. **Push to index**: the serialized JSON data populates the search *index*.
6. *The result* is a populated search index which can be explored through queries. When users make a search query such as "coffee", the search engine looks for that information in the search index. A search index has a structure similar to a table, known as the index *schema*. A typical search index schema contains *fields*, the field's data type (such as string), and field attributes. The fields store searchable text, and the *field attributes* allow for actions such as filtering and sorting. Below is an example of a search index schema:

<edukamu-image url="/graphics/module5/json-index-example.png" alt="A screenshot of the structure of an index schema in json including key phrases and image tags.">
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Setting Up Indexes
</edukamu-collapse-hidden-title>

The first step to creating an Azure AI Search solution is to provision an Azure AI Search resource. Once the Azure AI Search resource is created, you can manage components of your service from the resource *Overview* page in the portal.

<edukamu-image url="/graphics/module5/5-azure-search-portal.png" alt="Image of the overview page of an Azure AI Search resource." modal="true">
<edukamu-section class="edukamu-kuvateksti">
Click the image if you want to view it more closely.
</edukamu-section>
<br>

Before you begin, identify your data source. You may also create an Azure Storage object to contain your original data.

You can use one of several methods to create your search solution:

- Azure portal's Import data wizard
- with the REST API
- with a software development kit (SDK)

We will focus on the method using the portal below.


#### Azure Portal's Import Data Wizard

Contained within the Azure AI Search service in the Azure portal is the Import data wizard, which automates processes in the Azure portal to create various objects needed for the search engine.

A unique aspect of working with the Azure portal's Import data wizard is that it defines the search index and runs the indexer. You can see it in action when creating any of the following objects using the Azure portal:

- **Data Source**: Persists connection information to source data, including credentials. A data source object is used exclusively with indexers.
- **Index**: Physical data structure used for full text search and other queries.
- **Indexer**: A configuration object specifying a data source, target index, an optional AI skillset, optional schedule, and optional configuration settings for error handling and base-64 encoding.
- **Skillset**: A complete set of instructions for manipulating, transforming, and shaping content, including analyzing and extracting information from image files. Except for very simple and limited structures, it includes a reference to an Azure AI services resource that provides enrichment.
- **Knowledge store**: Stores output from an AI enrichment pipeline in tables and blobs in Azure Storage for independent analysis or downstream processing.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Querying Azure AI Search Indexes
</edukamu-collapse-hidden-title>

Index and query design are closely linked. After we build the index, we can perform queries. A crucial component to understand is that the schema of the index determines what queries can be answered.

Azure AI Search queries can be submitted as an HTTP or REST API request, with the response coming back as JSON. Queries can specify what fields are searched and returned, how search results are shaped, and how the results should be filtered or sorted. A query that doesn't specify the field to search will execute against all the searchable fields within the index.

Azure AI Search supports two types of syntax: simple and full Lucene. Simple syntax covers all of the common query scenarios, while full Lucene is useful for advanced scenarios.

#### Simple Query Requests (Behind the Scenes)

A query request is a list of words (search terms) and query operators (simple or full) of what you would like to see returned in a result set. Let's look what components make up a search query. Consider this simple search example:

`coffee (-"busy" + "wifi")`

This query is trying to find content about coffee, excluding busy and including wifi.

Breaking the query into components, it's made up of search terms (coffee), plus two verbatim phrases, `"busy"` and `"wifi"`, and operators (-, +, and ( )). The search terms can be matched in the search index in any order or location in the content. The two phrases will only match with exactly what is specified, so `wi-fi` would not be a match. Finally, a query can contain a number of operators. In this example, the - operator tells the search engine that these phrases should NOT be in the results. The parenthesis group terms together, and set their precedence.

By default, the search engine will match any of the terms in the query. Content containing just `coffee` would be a match. In this example, using `-"busy"` would lead to the search results including all content that doesn't have the exact string "busy" in it.

The simple query syntax in Azure AI Search excludes some of the more complex features of the full Lucene query syntax, and it's the default search syntax for queries.

</edukamu-collapse>
<br>

As you’ve noticed during this course, many topics regarding Azure AI are interconnected. Even if we aren’t looking to implement AI Search into our solution, we might still benefit from a solid understanding of queries and indexes - and vice versa!

<!-- Let’s make sure you’ve thoroughly grasped the concepts of this final section. It’s time for the last exercise of this course!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Exercise: Azure AI Search
</edukamu-collapse-hidden-title>

PLACEHOLDER ehkä tehtävä ehkä ei 🤷‍♂️

</edukamu-collapse> -->

You have now explored every topic of this course! Amazing work!

On the next page, you’ll find a little summary. We’ll briefly review everything we’ve covered on this course. It will also help you refresh your memory before continuing your studies on this micro degree!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
