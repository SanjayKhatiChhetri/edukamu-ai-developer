## RAG Capabilities in Microsoft Azure

In summary, Retrieval Augmentation Generation (RAG) is an architecture that augments the capabilities of a Large Language Model (LLM) like ChatGPT by adding an information retrieval system that provides grounding data. Adding an information retrieval system gives you control over grounding data used by an LLM when it formulates a response. For an enterprise solution, RAG architecture means that you can constrain generative AI to your enterprise content sourced from vectorized documents, images, audio, and video.

The decision about which information retrieval system to use is critical because it determines the inputs to the LLM. The information retrieval system should provide:

- Indexing strategies that load and refresh at scale, for all of your content, at the frequency you require.
- Query capabilities and relevance tuning. The system should return relevant results, in the short-form formats necessary for meeting the token length requirements of LLM inputs.
- Security, global reach, and reliability for both data and operations.
- Integration with LLMs.

Azure AI Search is a proven solution for information retrieval in a RAG architecture. It provides indexing and query capabilities, with the infrastructure and security of the Azure cloud. Through code and other components, you can design a comprehensive RAG solution that includes all of the elements for generative AI over your proprietary content.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Approaches for RAG with Azure AI Search
</edukamu-collapse-hidden-title>

Microsoft has several built-in implementations for using Azure AI Search in a RAG solution.

- Azure AI Studio, use a vector index and retrieval augmentation.
- Azure OpenAI Studio, use a search index with or without vectors.
- Azure Machine Learning, use a search index as a vector store in a prompt flow.

Curated approaches make it simple to get started, but for more control over the architecture, you need a custom solution. These templates create end-to-end solutions in:

- Python.
- .NET.
- JavaScript.
- Java.

</edukamu-collapse>
<br>

The architecture behind an effective RAG solution is built around information retrieval and language generation with an aim to provide informative and contextually relevant responses to users. The process involves an integration layer that manages the flow and a web application that presents the user interface. This combined approach ensures that users receive accurate and meaningful responses to their queries.

Next, let’s explore this approach.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### RAG Architecture
</edukamu-collapse-hidden-title>

A high-level summary of the pattern looks like this:

- Start with a user question or request (prompt).
- Send it to Azure AI Search to find relevant information.
- Send the top ranked search results to the LLM.
- Use the natural language understanding and reasoning capabilities of the LLM to generate a response to the initial prompt.

Azure AI Search provides inputs to the LLM prompt, but doesn't train the model. In RAG architecture, there's no extra training. The LLM is pretrained using public data, but it generates responses that are augmented by information from the retriever.

RAG patterns that include Azure AI Search have the elements indicated in the following illustration.

<edukamu-image url="/graphics/module3/architecture-diagram.png" alt="Architecture diagram of information retrieval with search and ChatGPT." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

- App UX (web app) for the user experience
- App server or orchestrator (integration and coordination layer)
- Azure AI Search (information retrieval system)
- Azure OpenAI (LLM for generative AI)

The web app provides the user experience, providing the presentation, context, and user interaction. Questions or prompts from a user start here. Inputs pass through the integration layer, going first to information retrieval to get the search results, but also go to the LLM to set the context and intent.

The app server or orchestrator is the integration code that coordinates the handoffs between information retrieval and the LLM. One option is to use LangChain to coordinate the workflow. LangChain integrates with Azure AI Search, making it easier to include Azure AI Search as a retriever in your workflow.

The information retrieval system provides the searchable index, query logic, and the payload (query response). The search index can contain vectors or non-vector content. Although most samples and demos include vector fields, it's not a requirement. The query is executed using the existing search engine in Azure AI Search, which can handle keyword (or term) and vector queries. The index is created in advance, based on a schema you define, and loaded with your content that's sourced from files, databases, or storage.

The LLM receives the original prompt, plus the results from Azure AI Search. The LLM analyzes the results and formulates a response. If the LLM is ChatGPT, the user interaction might be a back and forth conversation. If you're using Davinci, the prompt might be a fully composed answer. An Azure solution most likely uses Azure OpenAI, but there's no hard dependency on this specific service.

Azure AI Search doesn't provide native LLM integration, web frontends, or vector encoding (embeddings) out of the box, so you need to write code that handles those parts of the solution. You can review demo source (Azure-Samples/azure-search-openai-demo) for a blueprint of what a full solution entails.

</edukamu-collapse>
<br>

Do notice that the above is just an example of RAG architecture, or pattern, and that other models also exist.

Next, we’ll review what content can be searched with Azure AI Search and how it is retrieved by using query capabilities.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Searchable Content in Azure AI Search
</edukamu-collapse-hidden-title>

In Azure AI Search, all searchable content is stored in a search index that's hosted on your search service. A search index is designed for fast queries with millisecond response times, so its internal data structures exist to support that objective. To that end, a search index stores *indexed content*, and not whole content files like entire PDFs or images.

Internally, the data structures include inverted indexes of tokenized text, vector indexes for embeddings, and unaltered text for cases where verbatim matching is required (for example, in filters, fuzzy search, regular expression queries).

When you set up the data for your RAG solution, you use the features that create and load an index in Azure AI Search. An index includes fields that duplicate or represent your source content. An index field might be simple transference (a title or description in a source document becomes a title or description in a search index), or a field might contain the output of an external process, such as vectorization or skill processing that generates a representation or text description of an image.

Since you probably know what kind of content you want to search over, consider the indexing features that are applicable to each content type:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Content type**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Indexed as**
</edukamu-table-header>
<edukamu-table-header width="60%">
**Features**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
text
</edukamu-table-cell>
<edukamu-table-cell>
tokens, unaltered text
</edukamu-table-cell>
<edukamu-table-cell>
Indexers can pull plain text from other Azure resources like Azure Storage and Cosmos DB. You can also push any JSON content to an index. To modify text in flight, use analyzers and normalizers to add lexical processing during indexing. Synonym maps are useful if source documents are missing terminology that might be used in a query.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
text
</edukamu-table-cell>
<edukamu-table-cell>
vectors¹
</edukamu-table-cell>
<edukamu-table-cell>
Text can be chunked and vectorized externally and then indexed as vector fields in your index.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
image
</edukamu-table-cell>
<edukamu-table-cell>
tokens, unaltered text 2
</edukamu-table-cell>
<edukamu-table-cell>
Skills for OCR and Image Analysis can process images for text recognition or image characteristics. Image information is converted to searchable text and added to the index. Skills have an indexer requirement.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
image
</edukamu-table-cell>
<edukamu-table-cell>
vectors¹
</edukamu-table-cell>
<edukamu-table-cell>
Images can be vectorized externally for a mathematical representation of image content and then indexed as vector fields in your index.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
video
</edukamu-table-cell>
<edukamu-table-cell>
vectors¹
</edukamu-table-cell>
<edukamu-table-cell>
Video files can be vectorized externally for a mathematical representation of video content and then indexed as vector fields in your index.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
audio
</edukamu-table-cell>
<edukamu-table-cell>
vectors¹
</edukamu-table-cell>
<edukamu-table-cell>
Audio files can be vectorized externally for a mathematical representation of audio content and then indexed as vector fields in your index.
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

1. The generally available functionality of vector support requires that you call other libraries or models for data chunking and vectorization. However, integrated vectorization (preview) embeds these steps.
2. Skills are built-in support for AI enrichment. For OCR and Image Analysis, the indexing pipeline makes an internal call to the Azure AI Vision APIs. These skills pass an extracted image to Azure AI for processing, and receive the output as text that's indexed by Azure AI Search.

Vectors provide the best accommodation for dissimilar content (multiple file formats and languages) because content is expressed universally in mathematic representations. Vectors also support similarity search: matching on the coordinates that are most similar to the vector query. Compared to keyword search (or term search) that matches on tokenized terms, similarity search is more nuanced. It's a better choice if there's ambiguity or interpretation requirements in the content or in queries.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Content Retrieval in Azure AI Search
</edukamu-collapse-hidden-title>

Once your data is in a search index, you use the query capabilities of Azure AI Search to retrieve content.

In a non-RAG pattern, queries make a round trip from a search client. The query is submitted, it executes on a search engine, and the response returned to the client application. The response, or search results, consist exclusively of the verbatim content found in your index.

In a RAG pattern, queries and responses are coordinated between the search engine and the LLM. A user's question or query is forwarded to both the search engine and to the LLM as a prompt. The search results come back from the search engine and are redirected to an LLM. The response that makes it back to the user is generative AI, either a summation or answer from the LLM.

There's no query type in Azure AI Search - not even semantic or vector search - that composes new answers. Only the LLM provides generative AI. Here are the capabilities in Azure AI Search that are used to formulate queries:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="25%">
**Query feature**
</edukamu-table-header>
<edukamu-table-header>
**Purpose**
</edukamu-table-header>
<edukamu-table-header>
**Why use it**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Simple or full Lucene syntax
</edukamu-table-cell>
<edukamu-table-cell>
Query execution over text and non-vector numeric content.
</edukamu-table-cell>
<edukamu-table-cell>
Full text search is best for exact matches, rather than similar matches. Full text search queries are ranked using the BM25 algorithm and support relevance tuning through scoring profiles. It also supports filters and facets.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Filters and facets
</edukamu-table-cell>
<edukamu-table-cell>
Applies to text or numeric (non-vector) fields only. Reduces the search surface area based on inclusion or exclusion criteria.
</edukamu-table-cell>
<edukamu-table-cell>
Adds precision to your queries.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Semantic ranking
</edukamu-table-cell>
<edukamu-table-cell>
Re-ranks a BM25 result set using semantic models. Produces short-form captions and answers that are useful as LLM inputs.
</edukamu-table-cell>
<edukamu-table-cell>
Easier than scoring profiles, and depending on your content, a more reliable technique for relevance tuning.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Vector search
</edukamu-table-cell>
<edukamu-table-cell>
Query execution over vector fields for similarity search, where the query string is one or more vectors.
</edukamu-table-cell>
<edukamu-table-cell>
Vectors can represent all types of content, in any language.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Hybrid search
</edukamu-table-cell>
<edukamu-table-cell>
Combines any or all of the above query techniques. Vector and non-vector queries execute in parallel and are returned in a unified result set.
</edukamu-table-cell>
<edukamu-table-cell>
The most significant gains in precision and recall are through hybrid queries.
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


### Structuring the Query Response

A query's response provides the input to the LLM, so the quality of your search results is critical to success. Results are a tabular row set. The composition or structure of the results depends on:

- Fields that determine which parts of the index are included in the response. 
- Rows that represent a match from index.

Fields appear in search results when the attribute is "retrievable". A field definition in the index schema has attributes, and those determine whether a field is used in a response. Only "retrievable" fields are returned in full text or vector query results. By default all "retrievable" fields are returned, but you can use "select" to specify a subset. Besides "retrievable", there are no restrictions on the field. Fields can be of any length or type. Regarding length, there's no maximum field length limit in Azure AI Search, but there are limits on the size of an API request.

Rows are matches to the query, ranked by relevance, similarity, or both. By default, results are capped at the top 50 matches for full text search or k-nearest-neighbor matches for vector search. You can change the defaults to increase or decrease the limit up to the maximum of 1,000 documents. You can also use top and skip paging parameters to retrieve results as a series of paged results.


### Ranking by Relevance

When you're working with complex processes, a large amount of data, and expectations for millisecond responses, it's critical that each step adds value and improves the quality of the end result. On the information retrieval side, relevance tuning is an activity that improves the quality of the results sent to the LLM. Only the most relevant or the most similar matching documents should be included in results.

Relevance applies to keyword (non-vector) search and to hybrid queries (over the non-vector fields). In Azure AI Search, there's no relevance tuning for similarity search and vector queries. BM25 ranking is the ranking algorithm for full text search.

Relevance tuning is supported through features that enhance BM25 ranking. These approaches include:

- Scoring profiles that boost the search score if matches are found in a specific search field or on other criteria.
- Semantic ranking that re-ranks a BM25 results set, using semantic models from Bing to reorder results for a better semantic fit to the original query.

In comparison and benchmark testing, hybrid queries with text and vector fields, supplemented with semantic ranking over the BM25-ranked results, produce the most relevant results.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Advanced Example: Code of an Azure AI Search Query for RAG Scenarios
</edukamu-collapse-hidden-title>

The following code is copied from the retrievethenread.py file from a demo site. It produces content for the LLM from hybrid query search results. You can write a simpler query, but this example is inclusive of vector search and keyword search with semantic reranking and spell check. In the demo, this query is used to get initial content.

Python

```python
# Use semantic ranker if requested and if retrieval mode is text or hybrid (vectors + text)
if overrides.get("semantic_ranker") and has_text:
    r = await self.search_client.search(query_text,
                                  filter=filter,
                                  query_type=QueryType.SEMANTIC,
                                  query_language="en-us",
                                  query_speller="lexicon",
                                  semantic_configuration_name="default",
                                  top=top,
                                  query_caption="extractive|highlight-false" if use_semantic_captions else None,
                                  vector=query_vector,
                                  top_k=50 if query_vector else None,
                                  vector_fields="embedding" if query_vector else None)
else:
    r = await self.search_client.search(query_text,
                                  filter=filter,
                                  top=top,
                                  vector=query_vector,
                                  top_k=50 if query_vector else None,
                                  vector_fields="embedding" if query_vector else None)
if use_semantic_captions:
    results = [doc[self.sourcepage_field] + ": " + nonewlines(" . ".join([c.text for c in doc['@search.captions']])) async for doc in r]
else:
    results = [doc[self.sourcepage_field] + ": " + nonewlines(doc[self.content_field]) async for doc in r]
content = "\n".join(results)

```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Advanced Example: Integration Code and LLMs
</edukamu-collapse-hidden-title>

A RAG solution that includes Azure AI Search requires other components and code to create a complete solution. Whereas the previous sections covered information retrieval through Azure AI Search and which features are used to create and query searchable content, this section introduces LLM integration and interaction.

Notebooks in the demo repositories are a great starting point because they show patterns for passing search results to an LLM. Most of the code in a RAG solution consists of calls to the LLM so you need to develop an understanding of how those APIs work, which is outside the scope of this article.

The following cell block in the chat-read-retrieve-read.ipynb notebook shows search calls in the context of a chat session:

Python

```python
# Execute this cell multiple times updating user_input to accumulate chat history
user_input = "Does my plan cover annual eye exams?"

# Exclude category, to simulate scenarios where there's a set of docs you can't see
exclude_category = None

if len(history) > 0:
    completion = openai.Completion.create(
        engine=AZURE_OPENAI_GPT_DEPLOYMENT,
        prompt=summary_prompt_template.format(summary="\n".join(history), question=user_input),
        temperature=0.7,
        max_tokens=32,
        stop=["\n"])
    search = completion.choices[0].text
else:
    search = user_input

# Alternatively simply use search_client.search(q, top=3) if not using semantic ranking
print("Searching:", search)
print("-------------------")
filter = "category ne '{}'".format(exclude_category.replace("'", "''")) if exclude_category else None
r = search_client.search(search, 
                         filter=filter,
                         query_type=QueryType.SEMANTIC, 
                         query_language="en-us", 
                         query_speller="lexicon", 
                         semantic_configuration_name="default", 
                         top=3)
results = [doc[KB_FIELDS_SOURCEPAGE] + ": " + doc[KB_FIELDS_CONTENT].replace("\n", "").replace("\r", "") for doc in r]
content = "\n".join(results)

prompt = prompt_prefix.format(sources=content) + prompt_history + user_input + turn_suffix

completion = openai.Completion.create(
    engine=AZURE_OPENAI_CHATGPT_DEPLOYMENT, 
    prompt=prompt, 
    temperature=0.7, 
    max_tokens=1024,
    stop=["<|im_end|>", "<|im_start|>"])

prompt_history += user_input + turn_suffix + completion.choices[0].text + "\n<|im_end|>" + turn_prefix
history.append("user: " + user_input)
history.append("assistant: " + completion.choices[0].text)

print("\n-------------------\n".join(history))
print("\n-------------------\nPrompt:\n" + prompt)
```

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-orange">
Don’t worry if the last two examples seemed too difficult for you to understand at this stage. Working with such code usually requires previous knowledge and expertise, and you’ll have plenty of time to develop those skills in the future!

Next, let’s review how retrieval augmented generation can be used to complement already-existing AP applications. We’ll get reacquainted with Omise, our imaginary e-commerce platform, and see how they could implement RAG into their applications in order to improve customer experience and, thus, overall business.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Scenario: Enhancing E-Commerce with Retrieval Augmented Generation
</edukamu-collapse-hidden-title>

Retrieval-Augmented Generation (RAG) can significantly enhance the performance of an e-commerce platform, like the one maintained by our imaginary company Omise, by improving customer interaction, personalization, and decision-making processes. In this context, let's consider how RAG, combined with Conversational Language Understanding (CLU), can create a more dynamic and efficient e-commerce environment.

### Enhanced Customer Service and Product Recommendation

Omise is an e-commerce platform specializing in a wide range of products, from electronics to clothing. They aim to improve customer engagement and streamline their shopping experience.


### Implementing RAG and CLU

#### 1. Enhanced Customer Interaction
**Scenario**: A customer, Sarah, is looking for a new smartphone but is overwhelmed by the choices.

**RAG and CLU Integration**: When Sarah asks for recommendations, the system uses CLU to understand her query's context and preferences. Then, RAG retrieves relevant information from a vast database, including product specifications, reviews, and previous customer queries.

**Outcome**: Sarah receives a personalized list of smartphones that fit her preferences, along with summarized reviews and ratings, making her decision process easier.


#### 2. Dynamic Product Recommendations

**Scenario**: John, another customer, is browsing for winter jackets but leaves the site without making a purchase.

**RAG and CLU Integration**: RAG analyzes John's browsing history and past purchases. Simultaneously, CLU interprets any written feedback or queries John has made in the past regarding winter wear.

**Outcome**: The next time John visits Omise, he receives customized recommendations for winter jackets, along with a guide on how to choose the right one, enhancing his shopping experience.


#### 3. Improved Query Resolution

**Scenario**: A customer asks about the return policy for a specific product category.

**RAG and CLU Integration**: CLU understands the query's intent, and RAG retrieves the most up-to-date return policies related to that product category from Omise's knowledge base.

**Outcome**: The customer receives an immediate and accurate response, improving trust and satisfaction.


#### 4. Market Trend Analysis

**Scenario**: Omise wants to understand the latest trends in electronics.

**RAG and CLU Integration**: RAG retrieves and analyzes current market trends, customer feedback, and query patterns. CLU helps interpret the context of customer interactions and reviews.

**Outcome**: Omise gains insights into popular products and customer preferences, aiding in stock management and marketing strategies.


### Key Takeaways

#### 1. Synergy of RAG and CLU

This scenario illustrates how RAG and CLU can complement each other. In this example, RAG provides a powerful tool for data retrieval and generation, while CLU takes care of understanding language and customer intent.

#### 2. Customer Experience Enhancement

By integrating RAG and CLU, businesses like Omise can offer more personalized and efficient customer service, leading to higher satisfaction and retention rates.

#### 3. Informed Decision-Making

RAG helps businesses in making data-driven decisions by providing comprehensive market and customer insights, essential for staying competitive.

</edukamu-collapse>
<br>

In summary, CLU and RAG, when used together, can transform an e-commerce platform like Omise by personalizing the customer experience, improving service efficiency, and aiding in strategic decision-making. This integration is a prime example of leveraging AI to enhance business processes and customer engagement in the digital age – and everything needed to implement such capabilities is available in Microsoft Azure.

Now, it’s time for another exercise! Afterwards, we’ll move on to a topic that’s a bit less about theory and a bit more about practice.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Retrieval Augmented Generation
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/rag-capabilities-in-microsoft-azure-question-scroll-1.yaml" id="3j23a7bjvbra14qe">
<br>

</edukamu-collapse>
<br>

On the next page, we’ll take our first steps towards building natural language solutions. It’s also the last topic of the unit, so keep on going strong!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
