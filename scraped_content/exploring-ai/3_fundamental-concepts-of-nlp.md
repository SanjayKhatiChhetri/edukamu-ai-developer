<edukamu-video content="/videos/devai-2-unit3-video.yaml"/>
<br>

## Fundamental Concepts of NLP

Welcome to the third unit, which is all about the exciting world of Natural Language Processing (NLP)! In this unit, we’ll explore the capabilities of artificial intelligence (AI) to comprehend, interpret, and even generate human-like text.

NLP is the key that unlocks the potential for machines to understand the subtleties of language, enabling them to communicate with us in a way that feels both intuitive and intelligent. From understanding sentiments in text to translating languages seamlessly, NLP is at the forefront of revolutionizing how we interact with technology and maybe even with each other.

You might have used generative AI services that let you chat with a bot as if it was a human. Do you remember how you felt the first time you encountered such a service? NLP is one of the fundamental concepts in making those tools a reality.

On this unit, we’ll uncover the fundamental concepts of NLP, exploring its use cases across diverse domains – without forgetting Microsoft Azure, the platform of choice for everyone interested in leveraging NLP.

Let’s start with a short introduction.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to NLP
</edukamu-collapse-hidden-title>

Natural language processing supports applications that can see, hear, speak with, and understand users. Using text analytics, translation, and language understanding services, Microsoft Azure makes it easy to build applications that support natural language.

Natural Language Processing (NLP) is a field of artificial intelligence (AI) that focuses on the interaction between computers and humans through natural language. It involves the development of algorithms and models that enable machines to understand, interpret, and generate human-like text. NLP aims to bridge the gap between human communication and computer understanding, allowing computers to comprehend, analyze, and respond to human language in a way that is meaningful.

### Use Cases of NLP

1. **Text Understanding**: NLP enables machines to understand and extract information from written texts, making it valuable for tasks like sentiment analysis, named entity recognition, and information extraction.
2. **Language Translation**: NLP is instrumental in machine translation, facilitating the conversion of text from one language to another, breaking down language barriers.
3. **Chatbots and Virtual Assistants**: NLP powers chatbots and virtual assistants, enabling them to understand and respond to user queries in a conversational manner. Microsoft’s Copilot, released in late 2023, is an example of such service.
4. **Summarization**: NLP algorithms can summarize large volumes of text, condensing information while retaining essential details.
5. **Speech Recognition**: NLP is used in speech recognition systems, converting spoken language into text, improving voice-activated technologies.
6. **Search Engines**: NLP enhances search engines by understanding user queries and providing more accurate and relevant results.

Keep in mind that, as always, these are just examples. We’re constantly pushing the boundaries of NLP and finding new ways of leveraging this exciting technology.

</edukamu-collapse>
<br>


Microsoft Azure integrates NLP capabilities through various services, providing developers with powerful tools to incorporate natural language understanding into applications.

By leveraging Azure's NLP capabilities, developers can enhance the functionality of their applications, making them more intuitive, user-friendly, and able to understand and respond to natural language input.

In this unit, we’ll dig deeper into natural language processing and get familiar with three different aspects of NLP. We’ll start by exploring 1) text analysis and 2) question answering before moving on to 3) fundamentals of conversational language understanding.

The capabilities mentioned above are made possible by Azure’s cutting edge Language Service. We’ll wrap this unit up by getting to know another capable tool, Azure AI Speech.

Let’s get started with text analysis.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### NLP and Text Analysis
</edukamu-collapse-hidden-title>

In order for computer systems to interpret the subject of a text in a similar way humans do, they use **natural language processing** (NLP), an area within AI that deals with understanding written or spoken language and responding in kind. *Text analysis* describes NLP processes that extract information from unstructured text.

Natural language processing might be used to create:
* A social media feed analyzer that detects sentiment for a product marketing campaign.
* A document search application that summarizes documents in a catalog.
* An application that extracts brands and company names from text.

**Azure AI Language** is a cloud-based service that includes features for understanding and analyzing text. Azure AI Language includes various features that support sentiment analysis, key phrase identification, text summarization, and conversational language understanding.

</edukamu-collapse>
<br>


Before exploring the text analytics capabilities of the Azure AI Language service, let's examine some general principles and common techniques used to perform text analysis and other natural language processing (NLP) tasks.

Some of the earliest techniques used to analyze text with computers involve statistical analysis of a body of text (a corpus) to infer some kind of semantic meaning. Put simply, if you can determine the most commonly used words in a given document, you can often get a good idea of what the document is about.

Let’s take a look at a few core principles.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Principle 1: Tokenization
</edukamu-collapse-hidden-title>

The first step in analyzing a corpus is to break it down into *tokens*. For the sake of simplicity, you can think of each distinct word in the training text as a token, though in reality, tokens can be generated for partial words, or combinations of words and punctuation.

For example, consider this phrase from a famous US presidential speech: "*we choose to go to the moon*". The phrase can be broken down into the following tokens, with numeric identifiers:
1. we
2. choose
3. to
4. go
5. the
6. moon

Notice that "to" (token number 3) is used twice in the corpus. The phrase "*we choose to go to the moon*" can be represented by the tokens *[1,2,3,4,3,5,6]*.

We've used a simple example in which tokens are identified for each distinct word in the text. In real-life scenarios, however, it might be more complicated than that.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Principle 2: Frequency Analysis
</edukamu-collapse-hidden-title>

After tokenizing the words, you can perform some analysis to count the number of occurrences of each token. The most used words (other than *stop words* such as "*a*", "*the*", and so on) can often provide a clue as to the main subject of a text corpus.

For example, the most common words in the entire text of the "go to the moon" speech we considered previously include "*new*", "*go*", "*space*", and "*moon*". If we were to tokenize the text as bi-grams (word pairs), the most common bi-gram in the speech is "*the moon*". From this information, we can easily surmise that the text is primarily concerned with space travel and going to the moon.

### Tip

Simple frequency analysis in which you simply count the number of occurrences of each token can be an effective way to analyze a single document, but when you need to differentiate across multiple documents within the same corpus, you need a way to determine which tokens are most relevant in each document.

*Term frequency - inverse document frequency* (TF-IDF) is a common technique in which a score is calculated based on how often a word or term appears in one document compared to its more general frequency across the entire collection of documents. Using this technique, a high degree of relevance is assumed for words that appear frequently in a particular document, but relatively infrequently across a wide range of other documents.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Principle 3: Machine Learning in Text Classification
</edukamu-collapse-hidden-title>

Another useful text analysis technique is to use a classification algorithm, such as *logistic regression*, to train a machine learning model that classifies text based on a known set of categorizations. A common application of this technique is to train a model that classifies text as *positive* or *negative* in order to perform *sentiment analysis* or *opinion mining*.

For example, consider the following restaurant reviews, which are already labeled as **0** (*negative*) or **1** (*positive*):
* *The food and service were both great: 1*
* *A really terrible experience: 0*
* *Mmm! tasty food and a fun vibe: 1*
* *Slow service and substandard food: 0*

With enough labeled reviews, you can train a classification model using the tokenized text as *features* and the sentiment (0 or 1) a *label*. The model will encapsulate a relationship between tokens and sentiment - for example, reviews with tokens for words like "*great*", "*tasty*", or "*fun*" are more likely to return a sentiment of **1** (*positive*), while reviews with words like "*terrible*", "*slow*", and "*substandard*" are more likely to return **0** (*negative*).

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Principle 4: Semantic Language Models
</edukamu-collapse-hidden-title>

As the state of the art for NLP has advanced, the ability to train models that encapsulate the semantic relationship between tokens has led to the emergence of powerful language models. At the heart of these models is the encoding of language tokens as vectors (multi-valued arrays of numbers) known as *embeddings*.

It can be useful to think of the elements in a token embedding vector as coordinates in multidimensional space, so that each token occupies a specific "location." The closer tokens are to one another along a particular dimension, the more semantically related they are. In other words, related words are grouped closer together. As a simple example, suppose the embeddings for our tokens consist of vectors with three elements, for example:
* 4 ("dog"): [10,3,2]
* 5 ("bark"): [10,2,2]
* 8 ("cat"): [10,3,1]
* 9 ("meow"): [10,2,1]
* 10 ("skateboard"): [3,3,1]

We can plot the location of tokens based on these vectors in three-dimensional space, like this:

<edukamu-image url="/graphics/module3/example-embeddings-graph.png" alt="A diagram of tokens plotted on a three-dimensional space."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The locations of the tokens in the embeddings space include some information about how closely the tokens are related to one another. For example, the token for "dog" is close to "cat" and also to "bark." The tokens for "cat" and "bark" are close to "meow." The token for "skateboard" is further away from the other tokens.

The language models we use in industry are based on these principles but have greater complexity. For example, the vectors used generally have many more dimensions. There are also multiple ways you can calculate appropriate embeddings for a given set of tokens. Different methods result in different predictions from natural language processing models.

A generalized view of most modern natural language processing solutions is shown in the following diagram. A large corpus of raw text is tokenized and used to train language models, which can support many different types of natural language processing task.

<edukamu-image url="/graphics/module3/language-model.png" alt="A diagram of the process to tokenize text and train a language model that supports natural language processing tasks."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Common NLP tasks supported by language models include:
* Text analysis, such as extracting key terms or identifying named entities in text.
* Sentiment analysis and opinion mining to categorize text as *positive* or *negative*.
* Machine translation, in which text is automatically translated from one language to another.
* Summarization, in which the main points of a large body of text are summarized.
* Conversational AI solutions such as *bots* or *digital assistants* in which the language model can interpret natural language input and return an appropriate response.

These capabilities and more are supported by the models in the Azure AI Language service, which we'll explore next.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Azure handles text analysis with a service called Azure AI Language. It is a part of the Azure AI services offerings that can perform advanced natural language processing over unstructured text.

Azure AI Language's text analysis features include:
* **Named entity recognition** identifies people, places, events, and more. This feature can also be customized to extract custom categories.
* **Entity linking** identifies known entities together with a link to Wikipedia.
* **Personal identifying information (PII) detection** identifies personally sensitive information, including personal health information (PHI).
* **Language detection** identifies the language of the text and returns a language code such as "en" for English.
* **Sentiment analysis and opinion mining** identifies whether text is positive or negative.
* **Summarization** summarizes text by identifying the most important information.
* **Key phrase extraction** lists the main concepts from unstructured text.

Let’s briefly check out three examples of Azure AI Language in action: 1) entry recognition, 2) language detection, and 3) sentiment analysis.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Entry Recognition
</edukamu-collapse-hidden-title>

You can provide Azure AI Language with unstructured text, and it will return a list of entities in the text that it recognizes. An entity is an item of a particular type or a category; and in some cases, subtype, such as those as shown in the following table.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="33,33%">
Type
</edukamu-table-header>
<edukamu-table-header width="33,33%">
SubType
</edukamu-table-header>
<edukamu-table-header width="33,33%">
Example
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Person
</edukamu-table-cell>
<edukamu-table-cell >

</edukamu-table-cell>
<edukamu-table-cell >
"Bill Gates", "John"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Location
</edukamu-table-cell>
<edukamu-table-cell >

</edukamu-table-cell>
<edukamu-table-cell >
"Paris", "New York"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Organization
</edukamu-table-cell>
<edukamu-table-cell >

</edukamu-table-cell>
<edukamu-table-cell >
"Microsoft"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Quantity
</edukamu-table-cell>
<edukamu-table-cell >
Number
</edukamu-table-cell>
<edukamu-table-cell >
"6" or "six"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Quantity
</edukamu-table-cell>
<edukamu-table-cell >
Percentage
</edukamu-table-cell>
<edukamu-table-cell >
"25%" or "fifty percent"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Quantity
</edukamu-table-cell>
<edukamu-table-cell >
Ordinal
</edukamu-table-cell>
<edukamu-table-cell >
"1st" or "first"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Quantity
</edukamu-table-cell>
<edukamu-table-cell >
Age
</edukamu-table-cell>
<edukamu-table-cell >
"90 day old" or "30 years old"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Quantity
</edukamu-table-cell>
<edukamu-table-cell >
Currency
</edukamu-table-cell>
<edukamu-table-cell >
"10.99"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Quantity
</edukamu-table-cell>
<edukamu-table-cell >
Dimension
</edukamu-table-cell>
<edukamu-table-cell >
"10 miles", "40 cm"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Quantity
</edukamu-table-cell>
<edukamu-table-cell >
Temperature
</edukamu-table-cell>
<edukamu-table-cell >
"45 degrees"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DateTime
</edukamu-table-cell>
<edukamu-table-cell >

</edukamu-table-cell>
<edukamu-table-cell >
"6:30PM February 4, 2012"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DateTime
</edukamu-table-cell>
<edukamu-table-cell >
Date
</edukamu-table-cell>
<edukamu-table-cell >
"May 2nd, 2017" or "05/02/2017"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DateTime
</edukamu-table-cell>
<edukamu-table-cell >
Time
</edukamu-table-cell>
<edukamu-table-cell >
"8am" or "8:00"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DateTime
</edukamu-table-cell>
<edukamu-table-cell >
DateRange
</edukamu-table-cell>
<edukamu-table-cell >
"May 2nd to May 5th"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DateTime
</edukamu-table-cell>
<edukamu-table-cell >
TimeRange
</edukamu-table-cell>
<edukamu-table-cell >
"6pm to 7pm"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DateTime
</edukamu-table-cell>
<edukamu-table-cell >
Duration
</edukamu-table-cell>
<edukamu-table-cell >
"1 minute and 45 seconds"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DateTime
</edukamu-table-cell>
<edukamu-table-cell >
Set
</edukamu-table-cell>
<edukamu-table-cell >
"every Tuesday"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
URL
</edukamu-table-cell>
<edukamu-table-cell >

</edukamu-table-cell>
<edukamu-table-cell >
"https://www.bing.com"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Email
</edukamu-table-cell>
<edukamu-table-cell >

</edukamu-table-cell>
<edukamu-table-cell >
"support@microsoft.com"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
US-based Phone Number
</edukamu-table-cell>
<edukamu-table-cell >

</edukamu-table-cell>
<edukamu-table-cell >
"(312) 555-0176"
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
IP Address
</edukamu-table-cell>
<edukamu-table-cell >

</edukamu-table-cell>
<edukamu-table-cell >
"10.0.1.125"
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

Azure AI Language also supports *entity linking* to help disambiguate entities by linking to a specific reference. For recognized entities, the service returns a URL for a relevant *Wikipedia* article.

For example, suppose you use Azure AI Language to detect entities in the following restaurant review extract:

>"I ate at the restaurant in Seattle last week."


<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="25%">
Entity
</edukamu-table-header>
<edukamu-table-header width="25%">
Type
</edukamu-table-header>
<edukamu-table-header width="25%">
SubType
</edukamu-table-header>
<edukamu-table-header width="25%">
Wikipedia URL
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Seattle
</edukamu-table-cell>
<edukamu-table-cell >
Location
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell >
https://en.wikipedia.org/wiki/Seattle
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
last week
</edukamu-table-cell>
<edukamu-table-cell >
DateTime
</edukamu-table-cell>
<edukamu-table-cell>
DateRange
</edukamu-table-cell>
<edukamu-table-cell >

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
### 2. Language Detection
</edukamu-collapse-hidden-title>

Use the language detection capability of Azure AI Language to identify the language in which text is written. You can submit multiple documents at a time for analysis. For each document submitted the service will detect:
* The language name (for example "English").
* The ISO 639-1 language code (for example, "en").
* A score indicating a level of confidence in the language detection.

For example, consider a scenario where you own and operate a restaurant where customers can complete surveys and provide feedback on the food, the service, staff, and so on. Suppose you have received the following reviews from customers:

**Review 1**: "*A fantastic place for lunch. The soup was delicious.*"

**Review 2**: "*Comida maravillosa y gran servicio.*"

**Review 3**: "*The croque monsieur avec frites was terrific. Bon appetit!*"

You can use the text analytics capabilities in Azure AI Language to detect the language foreach of these reviews; and it might respond with the following results:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="20%">
Document
</edukamu-table-header>
<edukamu-table-header width="20%">
Language 
</edukamu-table-header>
<edukamu-table-header width="20%">
Name
</edukamu-table-header>
<edukamu-table-header width="20%">
ISO 6391 Code
</edukamu-table-header>
<edukamu-table-header width="20%">
Score
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Review 1
</edukamu-table-cell>
<edukamu-table-cell >
English
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell >
en
</edukamu-table-cell>
<edukamu-table-cell >
1.0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Review 2
</edukamu-table-cell>
<edukamu-table-cell >
Spanish
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell >
es
</edukamu-table-cell>
<edukamu-table-cell >
1.0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Review 3
</edukamu-table-cell>
<edukamu-table-cell >
English
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell >
en
</edukamu-table-cell>
<edukamu-table-cell >
0.9
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

Notice that the language detected for review 3 is English, despite the text containing a mix of English and French. The language detection service will focus on the **predominant** language in the text. The service uses an algorithm to determine the predominant language, such as length of phrases or total amount of text for the language compared to other languages in the text. The predominant language will be the value returned, along with the language code. The confidence score might be less than 1 as a result of the mixed language text.

There might be text that is ambiguous in nature, or that has mixed language content. These situations can present a challenge. An ambiguous content example would be a case where the document contains limited text, or only punctuation. For example, using Azure AI Language to analyze the text ":-)", results in a value of **unknown** for the language name and the language identifier, and a score of **NaN** (which is used to indicate *not a number*).

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. Sentiment Analysis
</edukamu-collapse-hidden-title>

The text analytics capabilities in Azure AI Language can evaluate text and return sentiment scores and labels for each sentence. This capability is useful for detecting positive and negative sentiment in social media, customer reviews, discussion forums and more.

Azure AI Language uses a prebuilt machine learning classification model to evaluate the text. The service returns sentiment scores in three categories: positive, neutral, and negative. In each of the categories, a score between 0 and 1 is provided. Scores indicate how likely the provided text is a particular sentiment. One document sentiment is also provided.

For example, the following two restaurant reviews could be analyzed for sentiment:

> Review 1: "We had dinner at this restaurant last night and the first thing I noticed was how courteous the staff was. We were greeted in a friendly manner and taken to our table right away. The table was clean, the chairs were comfortable, and the food was amazing."

and

> Review 2: "Our dining experience at this restaurant was one of the worst I've ever had. The service was slow, and the food was awful. I'll never eat at this establishment again."

The sentiment score for the first review might be: Document sentiment: positive Positive score: .90 Neutral score: .10 Negative score: .00

The second review might return a response: Document sentiment: negative Positive score: .00 Neutral score: .00 Negative score: .99

</edukamu-collapse>
<br>


In addition to the examples covered above, Azure AI Language is capable of other tasks as well, such as key phrase detection (whenever a certain phrase or a word is detected, a certain action occurs).

These features can be used in various scenarios. Imagine a shopkeeper, for example, who’s interested in improving their business. By using Azure AI Language, they would be able to extract all positive or negative reviews from a database and thus analyze them to make improvements.

We’ve already covered a lot, but these are just some of the features made possible by NLP.
<br>

Review your new knowledge and skills with the exercises below.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Introduction to NLP
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module3/fundamental-concepts-text-poll.yaml" id="6ls6z4xsgum5fr4x"/>
<br>
<edukamu-text-poll url="/exercises/module3/fundamental-concepts-text-poll-2.yaml" id="smu1jqr8zr0d8xi1"/>
<br>
<edukamu-text-poll url="/exercises/module3/fundamental-concepts-text-poll-3.yaml" id="wiuj2vn1f9v651ti"/>
<br>
<edukamu-text-poll url="/exercises/module3/fundamental-concepts-text-poll-4.yaml" id="1o5p24u6i9qlvu31"/>
<br>
<edukamu-text-poll url="/exercises/module3/fundamental-concepts-text-poll-5.yaml" id="65km29g83kb9r6pn"/>
<br>
<edukamu-text-poll url="/exercises/module3/fundamental-concepts-text-poll-6.yaml" id="b93c7f2av2tbbz4i"/>
<br>
<edukamu-text-poll url="/exercises/module3/fundamental-concepts-text-poll-7.yaml" id="o9s44ym37dko659h"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/3/fundamental-concepts-of-nlp?question=6ls6z4xsgum5fr4x">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="digital-workforce-logo">
### Scenario Exercise: NLP Analysis
</edukamu-collapse-hidden-title>

Yardability is an imaginary company that focuses on garden planning and related services. Their business was struggling some time ago, but in the past year they have automated many of their business processes and now business is booming! This has generated a new problem though – their back office is drowning in paperwork and various customer service tasks. 

They do have partial automation – they have a system capable of opening the company email inbox and reading email text contents and metadata. Currently any email from a given list of subcontractor email addresses is automatically forwarded to the billing department for invoice processing. But this is no longer enough. They have identified a few main challenges that they cannot automate with basic scripts or automation tools. You have been hired as a consultant to advise them which AI-tools might be most suitable for the tasks at hand.

Get familiar with the scenarios presented below and come up with your solutions! You can also check out our model answers afterwards.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="digital-workforce-logo">
### Exercise: Problem 1
</edukamu-collapse-hidden-title>

Their customer service representatives receive a lot of feedback from customers through their feedback portal. Most of the feedback is happy and consists of mostly thanks for the good service. Yardability takes pride in their customer interactions, and they want to always respond to these thanks with a personalized note, but this is not urgent and can be done with a week’s delay when there is some downtime. A small amount, about 5%, of the feedback is negative and  more urgent. It consists mostly of generic complaints or inquiries of failed deadlines. It is important for Yardability that they can respond to these concerns as swiftly as possible, but currently they have to read through a lot of happy emails that they flag for later processing before they find the problematic cases.

<edukamu-text-poll url="/exercises/module3/fundamental-concepts-digital-workforce-text-poll.yaml" id="5w4d51sqc14d159o"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/3/fundamental-concepts-of-nlp?question=5w4d51sqc14d159o">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="digital-workforce-logo">
### Exercise: Problem 2 - Classification
</edukamu-collapse-hidden-title>

The billing department has heard of the success of the automatic classification of customer feedback through the portal. Their daily work consists of going through emails to check for new invoices that they need to validate and log into their payment system. They are now wondering if their current system that forwards emails that are coming from a given list of subcontractor emails could be improved – the current system is otherwise great but does not catch all incoming invoices. In particular, they would be interested if there is a way to detect from all the various incoming emails those that are invoices to be paid.

<edukamu-text-poll url="/exercises/module3/fundamental-concepts-digital-workforce-text-poll-2.yaml" id="wfr0lk063wgl98rc"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/3/fundamental-concepts-of-nlp?question=wfr0lk063wgl98rc">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


How was it? Are you starting to get the hang of neural language processing, at least on a surface level?

As promised earlier, we’ll look at natural language processing from various angles and perspectives. One of the most exciting ones is question answering, our next topic.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
