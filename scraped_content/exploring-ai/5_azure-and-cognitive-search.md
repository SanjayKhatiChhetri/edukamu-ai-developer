## Azure and Cognitive Search

We all have used different search engines countless times in our lives, but have we ever stopped to wonder how they all work? One of the most basic principles is keyword matching: an engine provides results based on a search query, showing the user every instance where a matching word or phrase is found.

This is how you’d typically find certain information within a text document, for example. Interested in the use of eggs within a recipe? Just hit search and type *eggs*. Cognitive search, powered by AI, goes well beyond that.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Cognitive Search
</edukamu-collapse-hidden-title>

Searching for information online has never been easier. However, it's still a challenge to find information from documents that aren't in a search index. For example, every day, people deal with unstructured, typed, image-based, or hand-written documents. Often, people must manually read through these documents to extract and record their insights in order to persist the found data. Now we have solutions that can automate information extraction.

Knowledge mining is the term used to describe solutions that involve extracting information from large volumes of often unstructured data. One of these knowledge mining solutions is Azure Cognitive Search, a cloud search service that has tools for building user-managed indexes. The indexes can be used for internal only use, or to enable searchable content on public-facing internet assets.

Importantly, Azure Cognitive Search can utilize the built-in capabilities of Azure AI services such as image processing, content extraction, and natural language processing to perform knowledge mining of documents. The product's AI capabilities makes it possible to index previously unsearchable documents and to extract and surface insights from large amounts of data quickly.

</edukamu-collapse>
<br>


Microsoft Azure is equipped with everything needed in order to make cognitive search not only a reality, but also a lot stronger than it is today.

Let’s explore the various ways in which Azure Cognitive Search uses skills that are, well, cognitive.

(By the way, the term *cognitive* refers to the mental processes, like thinking and reasoning, that are needed in knowing, learning, and understanding things. In other words, a cognitive machine is capable of much more than just providing hit or miss results for keyword searched.)


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### What is Azure Cognitive Search?
</edukamu-collapse-hidden-title>

Azure Cognitive Search provides the infrastructure and tools to create search solutions that extract data from various structured, semi-structured, and non-structured documents.

<edukamu-image url="/graphics/module5/2-what-is-azure-search.png" alt="Visualization of Azure Search." style="max-width: 80%;"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Azure Cognitive Search results contain only your data, which can include text inferred or extracted from images, or new entities and key phrases detection through text analytics. It's a Platform as a Service (PaaS) solution. Microsoft manages the infrastructure and availability, allowing your organization to benefit without the need to purchase or manage dedicated hardware resources.

### Features

Azure Cognitive Search exists to complement existing technologies and provides a programmable search engine built on Apache Lucene, an open-source software library. It's a highly available platform offering a 99.9% uptime SLA available for cloud and on-premises assets.

Azure Cognitive Search comes with the following features:
* **Data from any source**: Azure Cognitive Search accepts data from any source provided in JSON format, with auto crawling support for selected data sources in Azure.
* **Full text search and analysis**: Azure Cognitive Search offers full text search capabilities supporting both simple query and full Lucene query syntax.
* **AI powered search**: Azure Cognitive Search has Azure AI capabilities built in for image and text analysis from raw content.
* **Multi-lingual**: Azure Cognitive Search offers linguistic analysis for 56 languages to intelligently handle phonetic matching or language-specific linguistics. Natural language processors available in Azure Cognitive Search are also used by Bing and Office.
* **Geo-enabled**: Azure Cognitive Search supports geo-search filtering based on proximity to a physical location.
* **Configurable user experience**: Azure Cognitive Search has several features to improve the user experience including autocomplete, autosuggest, pagination, and hit highlighting.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
When using Azure services to build tools that leverage cognitive search, we’re talking about search solutions. In a way, it’s as simple as defining *what* to find and *how* to find it.

As mentioned earlier, the most typical solution is based on your own data, which is the basis for developing efficient search solutions. Let’s dig deeper.

Please pay close attention to the upcoming sections, as they contain some important terminology and concepts that will be used a lot during these courses!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Elements of Search Solutions
</edukamu-collapse-hidden-title>

<edukamu-image url="/graphics/module5/data-indexing-process.png" alt="Visualization of indexing process." style="max-width: 80%;"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

A typical Azure Cognitive Search solution starts with a data source that contains the data artifacts you want to search. This could be a hierarchy of folders and files in Azure Storage, or text in a database such as Azure SQL Database or Azure Cosmos DB. The data format that Cognitive Search supports is JSON. Regardless of where your data originates, if you can provide it as a JSON document, the search engine can index it.

If your data resides in supported data source, you can use an indexer to automate data ingestion, including JSON serialization of source data in native formats. An indexer connects to a data source, serializes the data, and passes to the search engine for indexing. Most indexers support change detection, which makes data refresh a simpler exercise.

Besides automating data ingestion, indexers also support AI enrichment. You can attach a skillset that applies a sequence of AI skills to enrich the data, making it more searchable. A comprehensive set of built-in skills, based on Azure AI services APIs, can help you derive new fields – for example by recognizing entities in text, translating text, evaluating sentiment, or predicting appropriate captions for images.

Optionally, enriched content can be sent to a knowledge store, which stores output from an AI enrichment pipeline in tables and blobs in Azure Storage for independent analysis or downstream processing.

Whether you write application code that pushes data to an index - or use an indexer that automates data ingestion and adds AI enrichment - the fields containing your content are persisted in an index, which can be searched by client applications. The fields are used for searching, filtering, and sorting to generate a set of results that can be displayed or otherwise used by the client application.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Skillsets and Enrichment Pipelines
</edukamu-collapse-hidden-title>

AI enrichment refers to embedded image and natural language processing in a pipeline that extracts text and information from content that can't otherwise be indexed for full text search.

AI processing is achieved by adding and combining skills in a skillset. A skillset defines the operations that extract and enrich data to make it searchable. These AI skills can be either built-in skills, such as text translation or Optical Character Recognition (OCR), or custom skills that you provide.

### Built-in Skills

Built-in skills are based on pretrained models from Microsoft, which means you can't train the model using your own training data. Skills that call the Azure AI services APIs have a dependency on those services and are billed at the Azure AI services pay-as-you-go price when you attach a resource. Other skills are metered by Azure Cognitive Search, or are utility skills that are available at no charge.

Built-in skills fall into these categories:

**Natural language processing skills**: with these skills, unstructured text is mapped as searchable and filterable fields in an index.

Some examples include:
* Key Phrase Extraction: uses a pre-trained model to detect important phrases based on term placement, linguistic rules, proximity to other terms, and how unusual the term is within the source data.
* Text Translation Skill: uses a pre-trained model to translate the input text into various languages for normalization or localization use cases.

**Image processing skills**: creates text representations of image content, making it searchable using the query capabilities of Azure Cognitive Search.

Some examples include:
* Image Analysis Skill: uses an image detection algorithm to identify the content of an image and generate a text description.
* Optical Character Recognition Skill: allows you to extract printed or handwritten text from images, such as photos of street signs and products, as well as from documents—invoices, bills, financial reports, articles, and more.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. Understanding Indexes
</edukamu-collapse-hidden-title>

An Azure Cognitive Search index can be thought of as a container of searchable documents. Conceptually you can think of an index as a table and each row in the table represents a document. Tables have columns, and the columns can be thought of as equivalent to the fields in a document. Columns have data types, just as the fields do on the documents.

### Index Schema

In Azure Cognitive Search, an index is a persistent collection of JSON documents and other content used to enable search functionality. The documents within an index can be thought of as rows in a table, each document is a single unit of searchable data in the index.

The index includes a definition of the structure of the data in these documents, called its schema. An example of an index schema with AI-extracted fields keyphrases and imageTags is below:

<edukamu-image url="/graphics/module5/json-index-example.png" alt="A screenshot of the structure of an index schema in json including key phrases and image tags."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

### Index Attributes

Azure Cognitive Search needs to know how you would like to search and display the fields in the documents. You specify that by assigning attributes, or behaviors, to these fields. For each field in the document, the index stores its name, the data type, and supported behaviors for the field such as, is the field searchable, can the field be sorted?

The most efficient indexes use only the behaviors that are needed. If you forget to set a required behavior on a field when designing, the only way to get that feature is to rebuild the index.

The following image depicts the fields when designing an index in Azure:

<edukamu-image url="/graphics/module5/2-index-workflows.png" alt="Screenshot showing an example index with different fields." modal="true"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br> 

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 4. Building Indexes with Indexers
</edukamu-collapse-hidden-title>

In order to index the documents in Azure Storage, they need to be exported from their original file type to JSON. Similarly, to export data in any format to JSON and load it into an index, we use an indexer.

To create search documents, you can either generate JSON documents with application code or you can use Azure's indexer to export incoming documents into JSON.

Azure Cognitive Search lets you create and load JSON documents into an index with two approaches:
* **Push method**: JSON data is pushed into a search index via either the REST API or the .NET SDK. Pushing data has the most flexibility as it has no restrictions on the data source type, location, or frequency of execution.
* **Pull method**: Search service indexers can pull data from popular Azure data sources, and if necessary, export that data into JSON if it isn't already in that format.

### Pull Method and Loading Data

Azure Cognitive Search's indexer is a crawler that extracts searchable text and metadata from an external Azure data source and populates a search index using field-to-field mappings between source data and your index. Using the indexer is sometimes referred to as a 'pull model' approach because the service pulls data in without you having to write any code that adds data to an index. An indexer maps source fields to their matching fields in the index.

### Data Import Monitoring and Verification

The search services overview page has a dashboard that lets you quickly see the health of the search service. On the dashboard, you can see how many documents are in the search service, how many indexes have been used, and how much storage is in use.

When loading new documents into an index, the progress can be monitored by clicking on the index's associated indexer. The document count will grow as documents are loaded into the index. In some instances, the portal page can take a few minutes to display up-to-date document counts. Once the index is ready for querying, you can then use Search explorer to verify the results. An index is ready when the first document is successfully loaded.

Indexers only import new or updated documents, so it is normal to see zero documents indexed.

The Search explorer can perform quick searches to check the contents of an index, and ensure that you are getting expected search results. Having this tool available in the portal enables you to easily check the index by reviewing the results that are returned as JSON documents.

### Making Changes to Indexes

You have to drop and recreate indexes if you need to make changes to field definitions. Adding new fields is supported, with all existing documents having null values. You'll find it faster using a code-based approach to iterate your designs, as working in the portal requires the index to be deleted, recreated, and the schema details to be manually filled out.

An approach to updating an index without affecting your users is to create a new index under a different name. You can use the same indexer and data source. After importing data, you can switch your app to use the new index.

</edukamu-collapse>
<br>


In summary, indexes in Azure Cognitive Search serve as the backbone for efficient and intelligent information retrieval. They streamline the process of searching, filtering, and analyzing data, empowering users to derive valuable knowledge from their datasets.

Take the next exercise to consolidate your new knowledge and recap what we’ve just learned.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Cognitive Search
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module5/azure-and-cognitive-search-text-poll.yaml" id="28vc211f86l06h6h"/>
<br>
<edukamu-text-poll url="/exercises/module5/azure-and-cognitive-search-text-poll-2.yaml" id="9gm249y5fzu3z1k0"/>
<br>
<edukamu-text-poll url="/exercises/module5/azure-and-cognitive-search-text-poll-3.yaml" id="737skqv7x3p575fw"/>
<br>
<edukamu-text-poll url="/exercises/module5/azure-and-cognitive-search-text-poll-4.yaml" id="1w660n72e58n7tca"/>
<br>
<edukamu-text-poll url="/exercises/module5/azure-and-cognitive-search-text-poll-5.yaml" id="98a0i01tbc8f7qp5"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/5/azure-and-cognitive-search?question=28vc211f86l06h6h">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


As you may have understood during this course, data is the backbone of all AI applications and services, and cognitive search is no exception. There are more than one kind of data, though. Have you heard of enriched data, for example?

After checking out enriched data on the next page, we’ll circle back to indexes and learn how they behave within Microsoft Azure. That’s also our last topic on this course!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
