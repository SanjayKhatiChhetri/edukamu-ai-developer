<edukamu-video content="/videos/devai-7-unit2-video.yaml"/>
<br>

## Building Natural Language Solutions

Welcome to the second unit! In this unit, we'll learn a lot about natural language processing.

Take a moment to recall the contents of the second course of this study program. In that one, we spent a while working with natural language processing, or NLPs for short. Browse your notes or even revisit the course – does the term NLP ring any bells?

We'll start this unit with a little recap of NLP before focusing on the Azure AI Language service with which we got acquainted earlier. After reviewing, we'll get busy with question answering before reviewing conversational language understanding, retrieval augmented generation, and even natural language solutions.

First, though, let's recap natural language processing and see how it is connected to Azure AI Language. 

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Recap: Natural Language Processing (NLP)
</edukamu-collapse-hidden-title>

Arguably one of the most interesting aspects of artificial intelligence is Natural Language Processing, often referred to as NLP. NLP is a branch of AI that focuses on the interaction between computers and human language, allowing machines to understand, interpret, and generate human language in a way that is both meaningful and contextually relevant.

At its core, NLP is based on the idea that human language is rich in nuances, context, and structure. Unlike structured data, which is highly organized and machine-readable, natural language is complex, unstructured, and varies widely in its expression. NLP seeks to bridge this gap by providing machines with the ability to work with unstructured text data, just as humans do. Some of these services even mimic the human brain in the way they take actions and reason.

The applications of NLP are as diverse as the languages spoken around the world. From chatbots that hold conversations with customers to sentiment analysis tools that gauge public opinion, NLP is a versatile technology that finds utility in numerous domains. It's used in healthcare for analyzing patient records, in finance for sentiment analysis of market data, in e-commerce for customer feedback analysis, and in content generation for creating human-like text.

### NLP and Azure AI Language

Azure AI Language Service, offered by Microsoft Azure, is a powerful platform that leverages the capabilities of NLP to help developers and businesses extract valuable insights from text data. Whether you want to identify the language of a document, extract key phrases to summarize content, analyze sentiment, or recognize named entities, Azure AI Language Service provides a comprehensive set of tools and APIs that leverage NLP.

By integrating Azure AI Language Service into your applications and workflows, you can harness the power of NLP without the need for building complex language models from scratch. Microsoft has already done the heavy lifting by training state-of-the-art language models, which you can leverage to enhance your own projects.

</edukamu-collapse>
<br>

Whether you're a developer, data scientist, or business professional, NLP and Azure AI Language Service are your keys to unlocking the potential of language in the digital age, which you'll soon find out!

It's time to get started with question answering. In essence, we're talking about a technology that that enables machines to understand and respond to questions posed in natural language, much like how humans ask and answer questions in everyday conversation. Let's find out more, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Question Answering
</edukamu-collapse-hidden-title>

A common pattern for "intelligent" applications is to enable users to ask questions using natural language and receive appropriate answers. In effect, this kind of solution brings conversational intelligence to a traditional frequently asked questions (FAQ) publication. In this section, you will learn how to use Azure AI Language to create a knowledge base of question-and-answer pairs that can support an application or bot.

**Azure AI Language** includes a *question answering* capability, which enables you to define a *knowledge base* of question-and-answer pairs that can be queried using natural language input. The knowledge base can be published to a REST endpoint and consumed by client applications, commonly *bots*.

<edukamu-image url="/graphics/module2/diagram.png" alt="A diagram showing how a conversational app uses a knowledge base of questions and answers.">
<br>

The knowledge base can be created from existing sources, including:

- Web sites containing frequently asked question (FAQ) documentation.
- Files containing structured text, such as brochures or user guides.
- Built-in *chit chat* question and answer pairs that encapsulate common conversational exchanges.

**Note:** The question answering capability of Azure AI Language is a newer version of the QnA Service, which still exists as a standalone service. Please don't let this re-branding confuse you.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Question Answering or Language Understanding?
</edukamu-collapse-hidden-title>

A question answering knowledge base is a form of language model, which raises the question of when to use question answering, and when to use the conversational language understanding capabilities of Azure AI Language.

The two features are similar in that they both enable you to define a language model that can be queried using natural language expressions. However, there are some differences in the use cases that they are designed to address, as shown in the following table:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">

</edukamu-table-header>
<edukamu-table-header width="40%">
Question answering
</edukamu-table-header>
<edukamu-table-header width="40%">
Language understanding
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Usage pattern
</edukamu-table-cell>
<edukamu-table-cell>
User submits a question, expecting an answer
</edukamu-table-cell>
<edukamu-table-cell>
User submits an utterance, expecting an appropriate response or action
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Query processing
</edukamu-table-cell>
<edukamu-table-cell>
Service uses natural language understanding to match the question to an answer in the knowledge base
</edukamu-table-cell>
<edukamu-table-cell>
Service uses natural language understanding to interpret the utterance, match it to an intent, and identify entities
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Response
</edukamu-table-cell>
<edukamu-table-cell>
Response is a static answer to a known question
</edukamu-table-cell>
<edukamu-table-cell>
Response indicates the most likely intent and referenced entities
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Client logic
</edukamu-table-cell>
<edukamu-table-cell>
Client application typically presents the answer to the user
</edukamu-table-cell>
<edukamu-table-cell>
Client application is responsible for performing appropriate action based on the detected intent
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

The two services are in fact complementary. You can build comprehensive natural language solutions that combine language understanding models and question answering knowledge bases.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-orange">
Question answering systems can vary in complexity, from simple rule-based systems that rely on predefined patterns to more advanced machine learning models that learn to understand language and context. They are used in a wide range of applications, including chatbots, virtual assistants, customer support, and information retrieval systems.

Microsoft Azure provides pre-trained models for question answering as well, which means that you can set up, say, an intelligent virtual assistant in no time. Next, we'll explore how.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step 1. Creating a Knowledge Base
</edukamu-collapse-hidden-title>

To create a question answering solution, you can use the REST API or SDK to write code that defines, trains, and publishes the knowledge base. However, it's more common to use the Language Studio web interface to define and manage a knowledge base.

To create a knowledge base, you:

1. Sign in to Azure portal.
2. Search for **Azure AI services** using the search field at the top of the portal.
3. Select **Create** under the **Language Service** resource.
4. Create a resource in your Azure subscription:
  - Enable the *question answering* feature.
  - Create or select an **Azure AI Search** resource to host the knowledge base index.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In Language Studio, select your Azure AI Language resource and create a <span style="font-weight: bold">Custom question answering</span> project.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Add one or more data sources to populate the knowledge base:
</li>
</ol>
</edukamu-section>
  - URLs for web pages containing FAQs.
  - Files containing structured text from which questions and answers can be derived.
  - Predefined *chit-chat* datasets that include common conversational questions and responses in a specified style.
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 7;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Edit question and answer pairs in the portal.
</li>
</ol>
</edukamu-section>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step 2. Implementing Multi-Turn Conversation
</edukamu-collapse-hidden-title>

Although you can often create an effective knowledge base that consists of individual question and answer pairs, sometimes you might need to ask follow-up questions to elicit more information from a user before presenting a definitive answer. This kind of interaction is referred to as a *multi-turn* conversation.

<edukamu-image url="/graphics/module2/multi-turn-conversation.png" alt="A diagram showing a multi-turn conversation.">
<br>

You can enable multi-turn responses when importing questions and answers from an existing web page or document based on its structure, or you can explicitly define follow-up prompts and responses for existing question and answer pairs.

For example, suppose an initial question for a travel booking knowledge base is "How can I cancel a reservation?". A reservation might refer to a hotel or a flight, so a follow-up prompt is required to clarify this detail. The answer might consist of text such as "Cancellation policies depend on the type of reservation" and include follow-up prompts with links to answers about canceling flights and canceling hotels.

When you define a follow-up prompt for multi-turn conversation, you can link to an existing answer in the knowledge base or define a new answer specifically for the follow-up. You can also restrict the linked answer so that it is only ever displayed in the context of the multi-turn conversation initiated by the original question.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step 3. Testing and Publishing a Knowledge Phase
</edukamu-collapse-hidden-title>

After you have defined a knowledge base, you can train its natural language model, and test it before publishing it for use in an application or bot.

### Testing a Knowledge Base

You can test your knowledge base interactively in Language Studio, submitting questions and reviewing the answers that are returned. You can inspect the results to view their confidence scores as well as other potential answers.

<edukamu-image url="/graphics/module2/test-new.png" alt="Screenshot of the test pane of the custom question answering project in the Language studio." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

### Deploying a Knowledge Base

When you are happy with the performance of your knowledge base, you can deploy it to a REST endpoint that client applications can use to submit questions and receive answers. You can deploy it directly from Language Studio.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step 4. Using a Knowledge Base
</edukamu-collapse-hidden-title>

To consume the published knowledge base, you can use the REST interface.

The minimal request body for the function contains a question, like this:

JSON

```JSON
{
  "question": "What do I need to do to cancel a reservation?",
  "top": 2,
  "scoreThreshold": 20,
  "strictFilters": [
    {
      "name": "category",
      "value": "api"
    }
  ]
}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Property**
</edukamu-table-header>
<edukamu-table-header>
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
question
</edukamu-table-cell>
<edukamu-table-cell>
Question to send to the knowledge base.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
top
</edukamu-table-cell>
<edukamu-table-cell>
Maximum number of answers to be returned.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
scoreThreshold
</edukamu-table-cell>
<edukamu-table-cell>
Score threshold for answers returned.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
strictFilters
</edukamu-table-cell>
<edukamu-table-cell>
Limit to only answers that contain the specified metadata.
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

The response includes the closest question match that was found in the knowledge base, along with the associated answer, the confidence score, and other metadata about the question and answer pair:

JSON

```JSON
{
  "answers": [
    {
      "score": 27.74823341616769,
      "id": 20,
      "answer": "Call us on 555 123 4567 to cancel a reservation.",
      "questions": [
        "How can I cancel a reservation?"
      ],
      "metadata": [
        {
          "name": "category",
          "value": "api"
        }
      ]
    }
  ]
}
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step 5. Improving the Performance
</edukamu-collapse-hidden-title>

After creating and testing a knowledge base, you can improve its performance with active learning and by defining synonyms.

### Using Active Learning

Active learning can help you make continuous improvements to get better at answering user questions correctly over time. People often ask questions that are phrased differently, but ultimately have the same meaning. Active learning can help in situations like this because it enables you to consider alternate questions to each question and answer pair. Active learning is enabled by default.

To use active learning, you can do the following:

#### a. Creating Question and Answer Pairs

You create pairs of questions and answers in Language Studio for your project. You can also import a file that contains question and answer pairs to upload in bulk.

<edukamu-image url="/graphics/module2/import-file.png" alt="A screenshot showing how to import a file with question and answer pairs." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

#### b. Reviewing Suggestions

Active learning then begins to offer alternate questions for each question in your question-and-answer pairs. You access this from the Review suggestions pane:

<edukamu-image url="/graphics/module2/review-suggestions.png" alt="A screenshot of the Review suggestions pane." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

You review, and then accept or reject these alternate phrases suggested for each question by selecting the checkmark or delete symbol next to the alternate phrase. You can bulk accept or reject suggestions using the **Accept all suggestions** or **Reject all suggestions** option at the top.

You can also manually add alternate questions when you select Add alternate question for a pair in the Edit knowledge base pane:

<edukamu-image url="/graphics/module2/add-alternate-questions-manual.png" alt="A screenshot showing the Add alternate question option on the Edit knowledge base pane." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>


### Defining Synonyms

Synonyms are useful when questions submitted by users might include multiple different words to mean the same thing. For example, a travel agency customer might refer to a "reservation" or a "booking". By defining these as synonyms, the question answering service can find an appropriate answer regardless of which term an individual customer uses.

To define synonyms, you use the REST API to submit synonyms in the following JSON format:

JSON

```JSON
{
    "synonyms": [
        {
            "alterations": [
                "reservation",
                "booking"
                ]
        }
    ]
}
```

</edukamu-collapse>
<br>

That is question answering in a nutshell – an advanced AI capability that empowers developers to set up models that can answer all kinds of questions in no time, catering to the various needs of customers in a way that is both natural and accurate.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Use Cases of Question Answering
</edukamu-collapse-hidden-title>

### 1. Customer Support Chatbots

Companies can deploy QA-based chatbots on their websites or messaging platforms to answer customer inquiries. Customers can ask questions about product specifications, troubleshooting, account information, or policies, and the chatbot provides instant and accurate responses.


### 2. Educational Assistants

QA models can be integrated into e-learning platforms and educational apps to help students find answers to questions in textbooks, lecture notes, or online resources. Students can ask questions related to their coursework, and the AI assistant provides explanations and relevant content.


### 3. Medical Diagnosis

In healthcare, QA models can assist doctors and medical professionals by answering questions about patient symptoms, treatment options, drug interactions, and research findings. This can aid in quicker and more informed decision-making.


### 4. Legal Research

Legal professionals can use QA systems to search through vast legal documents and databases to find specific case law, statutes, or legal precedents. They can ask questions about legal matters, and the AI system retrieves relevant legal references.


### 5. Content Recommendations

Streaming platforms and news websites can employ QA models to enhance user engagement. Users can ask questions like, "What are the top-rated movies this week?" or "Tell me the latest tech news," and the system provides personalized recommendations or news summaries.


### 6. Technical Support

QA-based systems can assist IT support teams by answering questions related to software troubleshooting, hardware specifications, network configurations, and cybersecurity best practices

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Creating a Question Answering Solution
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practical exercise, you’ll get to set up a question answering solution. 

This exercise uses a virtual machine, provided by Microsoft, on Microsoft’s Learn platform. In order to set up the lab environment, please navigate to the Microsoft Learn platform.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/create-question-answer-solution-ai-language/10-exercise-create" target="_blank">Microsoft Learn: Lab Environment</edukamu-button>
<br>

Please notice that you need to sign into your Microsoft account (personal or professional) in order to use the Lab environment.

After signing in, you can launch the Lab environment by clicking on the button illustrated in the image below.

<edukamu-image url="/graphics/module2/lab-ohje.png" alt="Picture illustrating the lab button on Microsoft Learn." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

The lab environment (Virtual Machine) will launch in a separate window. You’ll find detailed instructions on signing in, getting started, and completing the practice exercise on the right.

<edukamu-image url="/graphics/module2/lab-ohje-2.png" alt="Picture illustrating the lab environment." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

Good luck!

</edukamu-collapse>
<br>


It is important to notice that QA-based bots are not meant to replace human workers and assistants. Instead, they can take care of highly demanding tasks quicker than people, which in turn leaves human employees more time to focus on other duties.

Now, recap a little before consolidating your knowledge with the following exercises.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Question Answering
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/building-natural-language-solutions-question-scroll-1.yaml" id="x6nkk4t8bd0y7zeo">

</edukamu-collapse>


<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="reaktor-logo">
### Scenario Exercise: Extraction Solutions
</edukamu-collapse-hidden-title>

Company Captain’s Delight Subsystems provides subsystems for shipbuilding. They have 20 sales experts that receive hundreds of RFQs (Request for quotation) documents per year. The documents come in .pdf, email, and Excel formats. A typical RFQ text in a .pdf file has 50 pages. In the first stage, the sales experts need to gather the information on ten key aspects of the project to make an informed go / no go decision for the project. The documents are long. Therefore quick, well-founded “no”-answers are highly desirable.

### 1. Suggest an extraction solution based on Azure components.

  a. What if the document layouts are widely variable?

### 2. How to assess if the solution is viable?

  a. How much extra development is needed?
  
  b. How much do the analyses cost?

  c. How to estimate the benefit from your solution? What indicators to measure pre- and post deployment?

<edukamu-text-poll url="/exercises/module2/building-natural-language-solutions-text-poll-1.yaml" id="mid4pa8s33ar6jcw">
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/2/building-natural-language-solutions?question=mid4pa8s33ar6jcw">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


Now that we've explored the power of Question Answering (QA) models in providing precise answers to specific queries, let's shift our focus to a broader and more dynamic realm of natural language processing: Conversational Language Understanding.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
