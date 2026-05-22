## Conversational Language Understanding

Question answering models have proven incredibly useful for retrieving information by responding to direct questions. However, in real-life interactions, language is often more nuanced and interactive. Conversational Language Understanding takes us beyond simple Q&A scenarios and focuses on the complexities of understanding and generating human-like responses in dynamic conversations.

Conversational Language Understanding thus opens a world of possibilities, from building sophisticated chatbots and virtual assistants to improving customer support experiences and facilitating more natural human-computer interactions.

During the following sections, we’ll discover how this fascinating technology enables AI systems to engage in meaningful, context-aware conversations, bridging the gap between machines and humans in a way that was once only possible in our wildest dreams. As always, we’ll start with a little introduction.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Getting Started with Conversational Language Understanding
</edukamu-collapse-hidden-title>

Conversational Language Understanding refers to the ability of computer systems or AI applications to comprehend and interpret natural language input during human-computer interactions, especially in the context of conversations. It is a crucial aspect of natural language processing (NLP) and artificial intelligence (AI) that focuses on enabling machines to understand and respond to user queries, commands, or statements as if they were engaging in a conversation with a human.


### Key Benefits of Conversational Language Understanding

#### 1. Enhanced User Experience

Conversational language understanding enhances the user experience by allowing people to interact with technology in a more natural and intuitive manner. Users can communicate with chatbots, virtual assistants, or applications using everyday language, making technology more accessible.

#### 2. Efficient Customer Support

It is used in customer support chatbots and virtual assistants to handle user inquiries and issues efficiently. Users can describe their problems, and the system can provide relevant solutions or escalate the issue if necessary.

#### 3. Personalization

Conversational understanding enables personalized recommendations and responses. For example, in e-commerce, users can ask for product recommendations, and the system can provide tailored suggestions based on their preferences and past behavior.

#### 4. Data Collection

It helps in collecting valuable data from user interactions, which can be used for analytics, understanding user behavior, and improving services. For example, sentiment analysis can gauge user satisfaction and therefore help further develop the software.

</edukamu-collapse>
<br>

Microsoft Azure has all the tools you need for planning and developing effective, intelligent conversational language understanding features for all your applications.

Let’s find out more, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Conversational Language Understanding in Microsoft Azure
</edukamu-collapse-hidden-title>

*Natural language processing* (NLP) is a common AI problem in which software must be able to work with text or speech in the natural language form that a human user would write or speak. Within the broader area of NLP, *natural language understanding (NLU)* deals with the problem of determining semantic meaning from natural language - usually by using a trained language model.

A common design pattern for a natural language understanding solution looks like this:

<edukamu-image url="/graphics/module2/language-understanding-app.png" alt="Diagram showing an app accepts natural language input, and uses a model to determine semantic meaning before taking the appropriate action.">
<br>

In this design pattern:

1. An app accepts natural language input from a user.
2. A language model is used to determine semantic meaning (the user's *intent*).
3. The app performs an appropriate action.

**Azure AI Language** enables developers to build apps based on language models that can be trained with a relatively small number of samples to discern a user's intended meaning.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Prebuilt Capabilities in Azure AI Language
</edukamu-collapse-hidden-title>

The Azure AI Language service provides various features for understanding human language. You can use each feature to better communicate with users, better understand incoming communication, or use them together to provide more insight into what the user is saying, intending, and asking about.

Azure AI Language service features fall into two categories: 1) Pre-configured features and 2) Learned features.

Using these features in your app requires sending your query to the appropriate endpoint. The endpoint used to query a specific feature varies, but all of them are prefixed with the Azure AI Language resource you created in your Azure account, either when building your REST request or defining your client using an SDK.

### 1. Pre-configured Features

The Azure AI Language service provides certain features without any model labeling or training. Once you create your resource, you can send your data and use the returned results within your app.

The following features are all pre-configured.


#### Summarization

Summarization is available for both documents and conversations, and will summarize the text into key sentences that are predicted to encapsulate the input's meaning.

#### Named Entity Recognition

Named entity recognition can extract and identify entities, such as people, places, or companies, allowing your app to recognize different types of entities for improved natural language responses. For example, given the text "The waterfront pier is my favorite Seattle attraction", Seattle would be identified and categorized as a location.

#### Personally Identifiable Information (PI) Detection

PII detection allows you to identify, categorize, and redact information that could be considered sensitive, such as email addresses, home addresses, IP addresses, names, and protected health information. For example, if the text "email@contoso.com" was included in the query, the entire email address can be identified and redacted.

#### Key Phrase Extraction

Key phrase extraction is a feature that quickly pulls the main concepts out of the provided text. For example, given the text "Text Analytics is one of the features in Azure AI Services.", the service would extract "*Azure AI Services*" and "*Text Analytics*".

#### Sentiment Analysis

Sentiment analysis identifies how positive or negative a string or document is. For example, given the text "Great hotel. Close to plenty of food and attractions we could walk to", the service would identify that as *positive* with a relatively high confidence score.

#### Language Detection

Language detection takes one or more documents, and identifies the language for each. For example, if the text of one of the documents was "Bonjour", the service would identify that as *French*.


### 2. Learned Features

Learned features require you to label data, train, and deploy your model to make it available to use in your application. These features allow you to customize what information is predicted or extracted.

**Note:** Quality of data greatly impacts the model's accuracy. Be intentional about what data is used, how well it is tagged or labeled, and how varied the training data is.

#### Conversational Language Understanding (CLU)

CLU is one of the core custom features offered by Azure AI Language. CLU helps users to build custom natural language understanding models to predict overall intent and extract important information from incoming utterances. CLU does require data to be tagged by the user to teach it how to predict intents and entities accurately.

Later, there will be a practical exercise about building a CLU model and using it in your app.

#### Custom Named Entity Recognition

Custom entity recognition takes custom labeled data and extracts specified entities from unstructured text. For example, if you have various contract documents that you want to extract involved parties from, you can train a model to recognize how to predict them.

#### Custom Text Classification

Custom text classification enables users to classify text or documents as custom defined groups. For example, you can train a model to look at news articles and identify the category they should fall into, such as News or Entertainment.

#### Question Answering

Question answering is a mostly pre-configured feature that provides answers to questions provided as input. The data to answer these questions comes from documents like FAQs or manuals.

For example, say you want to make a virtual chat assistant on your company website to answer common questions. You could use a company FAQ as the input document to create the question and answer pairs. Once deployed, your chat assistant can pass input questions to the service, and get the answers as a result.

</edukamu-collapse>
<br>

If the capabilities described above seem familiar, good for you! It means that you still remember these aspects from the second course, during which we briefly touched upon some of them. On this course, we’ll take it up a notch!

Let’s move right along and find out which resources are needed in order to build a conversational language understanding model. Please remember to explore these capabilities on your own as well if you have access to Microsoft Azure!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Resources and Conversational Language Understanding
</edukamu-collapse-hidden-title>

To use the Language Understanding service to develop a NLP solution, you'll need to create a Language resource in Azure. That resource will be used for both authoring your model and processing prediction requests from client applications.


### 1. Build Your Model

For features that require a model for prediction, you'll need to build, train and deploy that model before using it to make a prediction. This building and training will teach the Azure AI Language service what to look for.

First, you'll need to create your Azure AI Language resource in the Azure portal. Then:

1. Search for **Azure AI services**.
2. Find and select **Language Service**.
3. Select **Create** under the **Language Service**.
4. Fill out the necessary details, choosing the region closest to you geographically (for best performance) and giving it a unique name.

Once that resource has been created, you'll need a key and the endpoint. You can find that on the left side under **Keys and Endpoint** of the resource overview page.


### 2. Use Language Studio

For a more visual method of building, training, and deploying your model, you can use Language Studio to achieve each of these steps. On the main page, you can choose to create a Conversational language understanding project. Once the project is created, then go through the same process as above to build, train, and deploy your model.

<edukamu-image url="/graphics/module2/language-studio-conversational-small.png" alt="Screenshot of the Language Studio home page." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>


### 3. Use REST API

One way to build your model is through the REST API. The pattern would be to create your project, import data, train, deploy, then use your model.

These tasks are done asynchronously; you'll need to submit a request to the appropriate URI for each step, and then send another request to get the status of that job.

For example, if you want to deploy a model for a conversational language understanding project, you'd submit the deployment job, and then check on the deployment job status.

#### Authentication

For each call to your Azure AI Language resource, you authenticate the request by providing the following header.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
Key
</edukamu-table-header>
<edukamu-table-header>
Value
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Ocp-Apim-Subscription-Key
</edukamu-table-cell>
<edukamu-table-cell>
The key to your resource
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

#### Requesting Deployment

Submit a **POST** request to the following endpoint.

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Placeholder**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
<edukamu-table-header>
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell width="20%">
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint of your Azure AI Language resource.
</edukamu-table-cell>
<edukamu-table-cell>
https://<your-subdomain>.cognitiveservices.azure.com
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your project. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
myProject
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{DEPLOYMENT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your deployment. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
staging
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you're calling.
</edukamu-table-cell>
<edukamu-table-cell>
2022-05-01
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

Include the following body with your request.

JSON

```JSON
{
  "trainedModelLabel": "{MODEL-NAME}",
}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
Placeholder
</edukamu-table-header>
<edukamu-table-header width="70%">
Value
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{MODEL-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The model name that will be assigned to your deployment. This value is case-sensitive.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

Successfully submitting your request will receive a 202 response, with a response header of operation-location. This header will have a URL with which to request the status, formatted like this:

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
```

#### Getting Deployment Status

Submit a **GET** request to the URL from the response header above. The values will already be filled out based on the initial deployment request.

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
**Placeholder**
</edukamu-table-header>
<edukamu-table-header width="70%">
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint for authenticating your API request.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your project (case-sensitive).
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{DEPLOYMENT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your deployment (case-sensitive).
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{JOB-ID}
</edukamu-table-cell>
<edukamu-table-cell>
The ID for locating your model's training status, found in the header value detailed above in the deployment request.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you're calling.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

The response body will give the deployment status details. The status field will have the value of *succeeded* when the deployment is complete.

JSON

```JSON
{
    "jobId":"{JOB-ID}",
    "createdDateTime":"String",
    "lastUpdatedDateTime":"String",
    "expirationDateTime":"String",
    "status":"running"
}
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Querying Models
</edukamu-collapse-hidden-title>

To query your model for a prediction, you can use SDKs in C# or Python, or use the REST API.

### a. Querying with SDKs

To query your model using an SDK, you first need to create your client. Once you have your client, you then use it to call the appropriate endpoint.

C#
```C#
var languageClient = new TextAnalyticsClient(endpoint, credentials);
var response = languageClient.ExtractKeyPhrases(document);
```

Python

```Python
language_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=credentials)
response = language_client.extract_key_phrases(documents = documents)[0]
```

Other language features, such as the conversational language understanding, require the request be built and sent differently.

C#

```C#
var data = new
{
    analysisInput = new
    {
        conversationItem = new
        {
            text = userText,
            id = "1",
            participantId = "1",
        }
    },
    parameters = new
    {
        projectName,
        deploymentName,
        // Use Utf16CodeUnit for strings in .NET.
        stringIndexType = "Utf16CodeUnit",
    },
    kind = "Conversation",
};
Response response = await client.AnalyzeConversationAsync(RequestContent.Create(data));
```

Python

```Python
result = client.analyze_conversation(
    task={
        "kind": "Conversation",
        "analysisInput": {
            "conversationItem": {
                "participantId": "1",
                "id": "1",
                "modality": "text",
                "language": "en",
                "text": query
            },
            "isLoggingEnabled": False
        },
        "parameters": {
            "projectName": cls_project,
            "deploymentName": deployment_slot,
            "verbose": True
        }
    }
)
```

### b. Querying with the REST API

To query your model using REST, create a POST request to the appropriate URL with the appropriate body specified. For built in features such as language detection or sentiment analysis, you'll query the analyze-text endpoint.

**Tip**: Remember each request needs to be authenticated with your Azure AI Language resource key in the Ocp-Apim-Subscription-Key header.

HTTP

```HTTP
{ENDPOINT}/language/:analyze-text?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
**Placeholder**
</edukamu-table-header>
<edukamu-table-header width="70%">
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint for authenticating your API request.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you're calling.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

Within the body of that request, you must specify the kind parameter, which tells the service what type of language understanding you're requesting.

If you want to detect the language, for example, the JSON body would look something like the following.

JSON

```JSON
{
    "kind": "LanguageDetection",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput":{
        "documents":[
            {
                "id":"1",
                "text": "This is a document written in English."
            }
        ]
    }
}
```

Other language features, such as the conversational language understanding, require the request be routed to a different endpoint. For example, the conversational language understanding request would be sent to the following.

HTTP

```HTTP
{ENDPOINT}/language/:analyze-conversations?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
**Placeholder**
</edukamu-table-header>
<edukamu-table-header width="70%">
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint for authenticating your API request.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you're calling.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

That request would include a JSON body similar to the following.

JSON

```JSON
{
  "kind": "Conversation",
  "analysisInput": {
    "conversationItem": {
      "id": "1",
      "participantId": "1",
      "text": "Sample text"
    }
  },
  "parameters": {
    "projectName": "{PROJECT-NAME}",
    "deploymentName": "{DEPLOYMENT-NAME}",
    "stringIndexType": "TextElement_V8"
  }
}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Placeholder**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name of the project where you built your model.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{DEPLOYMENT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name of your deployment.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

### Sample Response

The query response from an SDK will in the object returned, which varies depending on the feature (such as in response.key_phrases or response.Value). The REST API will return JSON that would be similar to the following.

JSON

```JSON
{
    "kind": "KeyPhraseExtractionResults",
    "results": {
        "documents": [{
            "id": "1",
            "keyPhrases": ["modern medical office", "Dr. Smith", "great staff"],
            "warnings": []
        }],
        "errors": [],
        "modelVersion": "{VERSION}"
    }
}
```

For other models like conversational language understanding, a sample response to your query would be similar to the following.

JSON

```JSON
{
  "kind": "ConversationResult",
  "result": {
    "query": "String",
    "prediction": {
      "topIntent": "intent1",
      "projectKind": "Conversation",
      "intents": [
        {
          "category": "intent1",
          "confidenceScore": 1
        },
        {
          "category": "intent2",
          "confidenceScore": 0
        }
      ],
      "entities": [
        {
          "category": "entity1",
          "text": "text",
          "offset": 7,
          "length": 4,
          "confidenceScore": 1
        }
      ]
    }
  }
}
```

The SDKs for both Python and C# return JSON that is very similar to the REST response.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-orange">
The above examples contain some quite advanced details, so understanding them might seem difficult at first. As such, you should always remember to recap and review as long as it takes.

Before continuing any further, let’s try setting up a CLU model on our own using the Azure Portal. Have a go at completing the following practical exercise! If you can’t access Microsoft Azure for one reason or another, read through the instructions carefully.

Please reserve some uninterrupted time for the following practice exercises, as they might be quite time-consuming.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Setting Up a CLU Model
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practice exercise, we’ll have a go at setting up a conversational language understanding model. We’ll be using Azure Portal, so start by signing in and firing up the Azure platform!

### 1. Creating Resources

1. Sign in to the <edukamu-link url="https://portal.azure.com/#create/Microsoft.CognitiveServicesTextAnalytics" target="_blank">Azure Portal</edukamu-link> to create a new Azure AI Language resource.
2. Select **Create a new resource**.
3. In the window that appears, search for **Language service**.
4. Select **Create**.
5. Create a Language resource with following details.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
Instance detail
</edukamu-table-header>
<edukamu-table-header width="70%">
Required value
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Region
</edukamu-table-cell>
<edukamu-table-cell>
One of the supported regions for your Language resource.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Name
</edukamu-table-cell>
<edukamu-table-cell>
Required name for your Language resource.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Pricing tier
</edukamu-table-cell>
<edukamu-table-cell>
One of the supported pricing tiers for your Language resource.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


### 2. Resource Keys and Endpoints

1. Go to your resource overview page in the Azure portal.
2. From the menu on the left side, select **Keys and Endpoint**. You will use the endpoint and key for the API requests.

<edukamu-image url="/graphics/module2/azure-portal-resource-credentials.png" alt="A screenshot showing the key and endpoint page in the Azure portal." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>


### 3. Importing a Sample Project

Once you have a Language resource created, create a conversational language understanding project. A project is a work area for building your custom ML models based on your data. Your project can only be accessed by you and others who have access to the Language resource being used.

For this practice exercise, you can download a sample project and import it. This project can predict the intended commands from user input, such as: reading emails, deleting emails, and attaching a document to an email.

<edukamu-button url="https://go.microsoft.com/fwlink/?linkid=2196152" target="_blank">Download Sample Project</edukamu-button>
<br>

Submit a POST request using the following URL, headers, and JSON body to import your project.

#### a. URL

Use the following URL when creating your API request. Replace the placeholder values with your own values.

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/:import?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Placeholder**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
<edukamu-table-header>
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell width="15%">
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint for authenticating your API request.
</edukamu-table-cell>
<edukamu-table-cell>
https://<your-custom-subdomain>.cognitiveservices.azure.com
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
ceThe name for your project. This value is case-sensitive, and must match the project name in the JSON file you're importing.ll2
</edukamu-table-cell>
<edukamu-table-cell>
EmailAppDemo
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you're calling.
</edukamu-table-cell>
<edukamu-table-cell>
2023-04-01
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

#### b. Headers

Use the following header to authenticate your request.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Ocp-Apim-Subscription-Key
</edukamu-table-cell>
<edukamu-table-cell>
The key to your resource. Used for authenticating your API requests.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


#### c. JSON Body

The JSON body you send is similar to the following example.

JSON

```JSON
{
  "projectFileVersion": "{API-VERSION}",
  "stringIndexType": "Utf16CodeUnit",
  "metadata": {
    "projectKind": "Conversation",
    "settings": {
      "confidenceThreshold": 0.7
    },
    "projectName": "{PROJECT-NAME}",
    "multilingual": true,
    "description": "Trying out CLU",
    "language": "{LANGUAGE-CODE}"
  },
  "assets": {
    "projectKind": "Conversation",
    "intents": [
      {
        "category": "intent1"
      },
      {
        "category": "intent2"
      }
    ],
    "entities": [
      {
        "category": "entity1"
      }
    ],
    "utterances": [
      {
        "text": "text1",
        "dataset": "{DATASET}",
        "intent": "intent1",
        "entities": [
          {
            "category": "entity1",
            "offset": 5,
            "length": 5
          }
        ]
      },
      {
        "text": "text2",
        "language": "{LANGUAGE-CODE}",
        "dataset": "{DATASET}",
        "intent": "intent2",
        "entities": []
      }
    ]
  }
}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Placeholder**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
<edukamu-table-header>
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell width="15%">
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you're calling.
</edukamu-table-cell>
<edukamu-table-cell>
2023-04-01
</edukamu-table-cell>
<edukamu-table-cell width="16%">

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
projectName
</edukamu-table-cell>
<edukamu-table-cell width="15%">
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name of your project. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
EmailAppDemo
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
language
</edukamu-table-cell>
<edukamu-table-cell>
{LANGUAGE-CODE}
</edukamu-table-cell>
<edukamu-table-cell>
A string specifying the language code for the utterances used in your project. If your project is a multilingual project, choose the language code of the majority of the utterances.
</edukamu-table-cell>
<edukamu-table-cell>
en-us
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
multilingual
</edukamu-table-cell>
<edukamu-table-cell>
true
</edukamu-table-cell>
<edukamu-table-cell>
A boolean value that enables you to have documents in multiple languages in your dataset. When your model is deployed, you can query the model in any supported language including languages that aren't included in your training documents.
</edukamu-table-cell>
<edukamu-table-cell>
true
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
dataset
</edukamu-table-cell>
<edukamu-table-cell>
{DATASET}
</edukamu-table-cell>
<edukamu-table-cell>
See how to train a model for information on splitting your data between a testing and training set. Possible values for this field are Train and Test.
</edukamu-table-cell>
<edukamu-table-cell>
Train
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

Upon a successful request, the API response will contain an operation-location header with a URL you can use to check the status of the import job. It is formatted like this:

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/import/jobs/{JOB-ID}?api-version={API-VERSION}
```


### 4. Getting the Import Job Status

When you send a successful project import request, the full request URL for checking the import job's status (including your endpoint, project name, and job ID) is contained in the response's operation-location header.

Use the following **GET** request to query the status of your import job. You can use the URL you received from the previous step, or replace the placeholder values with your own values

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/import/jobs/{JOB-ID}?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Placeholder**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
<edukamu-table-header>
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint for authenticating your API request.
</edukamu-table-cell>
<edukamu-table-cell>
https://<your-custom-subdomain>.cognitiveservices.azure.com
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your project. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
myProject
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{JOB-ID}
</edukamu-table-cell>
<edukamu-table-cell>
The ID for locating your import job status.
</edukamu-table-cell>
<edukamu-table-cell>
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you are calling.
</edukamu-table-cell>
<edukamu-table-cell>
2023-04-01
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


#### a. Headers

Use the following header to authenticate your request.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Description**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Ocp-Apim-Subscription-Key
</edukamu-table-cell>
<edukamu-table-cell>
The key to your resource. Used for authenticating your API requests.
</edukamu-table-cell>
<edukamu-table-cell>
{YOUR-PRIMARY-RESOURCE-KEY}
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


#### b. Response Body

Once you send the request, you'll get the following response. Keep polling this endpoint until the status parameter changes to "succeeded".

JSON

```JSON
{
  "jobId": "xxxxx-xxxxx-xxxx-xxxxx",
  "createdDateTime": "2022-04-18T15:17:20Z",
  "lastUpdatedDateTime": "2022-04-18T15:17:22Z",
  "expirationDateTime": "2022-04-25T15:17:20Z",
  "status": "succeeded"
}
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Training the CLU Model
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practice exercise, we’ll build on the previous exercise and start training the model we just set up.

Typically, after you create a project, you should build schema and tag utterances. For this quickstart, we already imported a ready project with built schema and tagged utterances.

### 1. Create a POST request

Create a POST request using the following URL, headers, and JSON body to submit a training job.

#### a. URL

Use the following URL when creating your API request. Replace the placeholder values with your own values.

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/:train?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Placeholder**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Value**
</edukamu-table-header>
<edukamu-table-header width="60%">
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint for authenticating your API request.
</edukamu-table-cell>
<edukamu-table-cell>

`https://<your-custom-subdomain>.cognitiveservices.azure.com`

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your project. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
EmailApp
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you are calling.
</edukamu-table-cell>
<edukamu-table-cell>
2023-04-01
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


#### b. Headers

Use the following header to authenticate your request.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Ocp-Apim-Subscription-Key
</edukamu-table-cell>
<edukamu-table-cell>
The key to your resource. Used for authenticating your API requests.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


#### c. JSON Body

Use the following object in your request. The model will be named after the value you use for the modelLabel parameter once training is complete.

JSON

```JSON
{
  "modelLabel": "{MODEL-NAME}",
  "trainingMode": "{TRAINING-MODE}",
  "trainingConfigVersion": "{CONFIG-VERSION}",
  "evaluationOptions": {
    "kind": "percentage",
    "testingSplitPercentage": 20,
    "trainingSplitPercentage": 80
  }
}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Placeholder**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
<edukamu-table-header>
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell width="25%">
modelLabel
</edukamu-table-cell>
<edukamu-table-cell width="21%">
{MODEL-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
Your Model name.
</edukamu-table-cell>
<edukamu-table-cell width="15%">
Model1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
trainingConfigVersion
</edukamu-table-cell>
<edukamu-table-cell>
{CONFIG-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The training configuration model version. By default, the latest model version is used.
</edukamu-table-cell>
<edukamu-table-cell>
2022-05-01
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
trainingMode
</edukamu-table-cell>
<edukamu-table-cell>
{TRAINING-MODE}
</edukamu-table-cell>
<edukamu-table-cell>
The training mode to be used for training. Supported modes are **Standard training**, faster training, but only available for English and **Advanced training** supported for other languages and multilingual projects, but involves longer training times. Learn more about training modes.
</edukamu-table-cell>
<edukamu-table-cell>
standard
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
kind
</edukamu-table-cell>
<edukamu-table-cell>
percentage
</edukamu-table-cell>
<edukamu-table-cell>
Split methods. Possible Values are percentage or manual. See how to train a model for more information.
</edukamu-table-cell>
<edukamu-table-cell>
percentage
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
trainingSplitPercentage
</edukamu-table-cell>
<edukamu-table-cell>
80
</edukamu-table-cell>
<edukamu-table-cell>
Percentage of your tagged data to be included in the training set. Recommended value is 80.
</edukamu-table-cell>
<edukamu-table-cell>
80
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
testingSplitPercentage
</edukamu-table-cell>
<edukamu-table-cell>
20
</edukamu-table-cell>
<edukamu-table-cell>
Percentage of your tagged data to be included in the testing set. Recommended value is 20.
</edukamu-table-cell>
<edukamu-table-cell>
20
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

**Note**: The trainingSplitPercentage and testingSplitPercentage are only required if Kind is set to percentage and the sum of both percentages should be equal to 100.

Once you send your API request, you will receive a 202 response indicating success. In the response headers, extract the operation-location value. It will be formatted like this:

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/train/jobs/{JOB-ID}?api-version={API-VERSION}
```

You can then use the following URL to get the training job status.


### 2. Getting Training Job Status

Training may take time to complete - sometimes between 10 and 30 minutes. You can use the following request to keep polling the status of the training job until it is successfully completed.

When you send a successful training request, the full request URL for checking the job's status (including your endpoint, project name, and job ID) is contained in the response's operation-location header.

Use the following **GET** request to get the status of your model's training progress. Replace the placeholder values below with your own values.

#### a. Request URL

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/train/jobs/{JOB-ID}?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Placeholder**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Value**
</edukamu-table-header>
<edukamu-table-header width="60%">
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{YOUR-ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint for authenticating your API request.
</edukamu-table-cell>
<edukamu-table-cell>

`https://<your-custom-subdomain>.cognitiveservices.azure.com`

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your project. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
EmailApp
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{JOB-ID}
</edukamu-table-cell>
<edukamu-table-cell>
The ID for locating your model's training status.
</edukamu-table-cell>
<edukamu-table-cell>
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you are calling.
</edukamu-table-cell>
<edukamu-table-cell>
2023-04-01
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


#### b. Headers

Use the following header to authenticate your request.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Ocp-Apim-Subscription-Key
</edukamu-table-cell>
<edukamu-table-cell>
The key to your resource. Used for authenticating your API requests.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


#### c. Response Body

Once you send the request, you will get the following response. Keep polling this endpoint until the **status** parameter changes to "succeeded".

JSON

```JSON
{
  "result": {
    "modelLabel": "{MODEL-LABEL}",
    "trainingConfigVersion": "{TRAINING-CONFIG-VERSION}",
    "trainingMode": "{TRAINING-MODE}",
    "estimatedEndDateTime": "2022-04-18T15:47:58.8190649Z",
    "trainingStatus": {
      "percentComplete": 3,
      "startDateTime": "2022-04-18T15:45:06.8190649Z",
      "status": "running"
    },
    "evaluationStatus": {
      "percentComplete": 0,
      "status": "notStarted"
    }
  },
  "jobId": "xxxxx-xxxxx-xxxx-xxxxx-xxxx",
  "createdDateTime": "2022-04-18T15:44:44Z",
  "lastUpdatedDateTime": "2022-04-18T15:45:48Z",
  "expirationDateTime": "2022-04-25T15:44:44Z",
  "status": "running"
}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
<edukamu-table-header>
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell width="25%">
modelLabel
</edukamu-table-cell>
<edukamu-table-cell>
The model name.
</edukamu-table-cell>
<edukamu-table-cell>
Model1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
trainingConfigVersion
</edukamu-table-cell>
<edukamu-table-cell>
The training configuration version. By default, the latest version is used.
</edukamu-table-cell>
<edukamu-table-cell>
2022-05-01
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
trainingMode
</edukamu-table-cell>
<edukamu-table-cell>
Your selected training mode.
</edukamu-table-cell>
<edukamu-table-cell>
standard
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
startDateTime
</edukamu-table-cell>
<edukamu-table-cell>
The time training started.
</edukamu-table-cell>
<edukamu-table-cell>
2022-04-14T10:23:04.2598544Z
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
status
</edukamu-table-cell>
<edukamu-table-cell>
The status of the training job.
</edukamu-table-cell>
<edukamu-table-cell>
running
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
estimatedEndDateTime
</edukamu-table-cell>
<edukamu-table-cell>
Estimated time for the training job to finish.
</edukamu-table-cell>
<edukamu-table-cell>
2022-04-14T10:29:38.2598544Z
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
jobId
</edukamu-table-cell>
<edukamu-table-cell>
Your training job ID.
</edukamu-table-cell>
<edukamu-table-cell>
xxxxx-xxxx-xxxx-xxxx-xxxxxxxxx
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
createdDateTime
</edukamu-table-cell>
<edukamu-table-cell>
Training job creation date and time.
</edukamu-table-cell>
<edukamu-table-cell>
2022-04-14T10:22:42Z
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
lastUpdatedDateTime
</edukamu-table-cell>
<edukamu-table-cell>
Training job last updated date and time.
</edukamu-table-cell>
<edukamu-table-cell>
2022-04-14T10:23:45Z
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
expirationDateTime
</edukamu-table-cell>
<edukamu-table-cell>
Training job expiration date and time.
</edukamu-table-cell>
<edukamu-table-cell>
2022-04-14T10:22:42Z
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
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Deploying Your Model
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practical exercise, we’ll deploy the model we set up and trained before.

Generally after training a model you would review its evaluation details. In this quickstart, you will just deploy your model, and call the prediction API to query the results.

### 1. Submit Deployment Job

Create a PUT request using the following URL, headers, and JSON body to start deploying a conversational language understanding model.

#### a. URL

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Placeholder**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
<edukamu-table-header>
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell width="25%">
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell width="25%">
The endpoint for authenticating your API request.
</edukamu-table-cell>
<edukamu-table-cell>

`https://<your-custom-subdomain>.cognitiveservices.azure.com`

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your project. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
myProject
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{DEPLOYMENT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your deployment. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
staging
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you are calling.
</edukamu-table-cell>
<edukamu-table-cell>
2023-04-01
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


#### b. Headers

Use the following header to authenticate your request.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Ocp-Apim-Subscription-Key
</edukamu-table-cell>
<edukamu-table-cell>
The key to your resource. Used for authenticating your API requests.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


#### c. Request Body

JSON

```JSON
{
  "trainedModelLabel": "{MODEL-NAME}",
}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Key**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Placeholder**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
<edukamu-table-header width="15%">
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
trainedModelLabel
</edukamu-table-cell>
<edukamu-table-cell>
{MODEL-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The model name that will be assigned to your deployment. You can only assign successfully trained models. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
myModel
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

Once you send your API request, you will receive a 202 response indicating success. In the response headers, extract the operation-location value. It will be formatted like this:

HTTP
```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
```

You can use this URL to get the deployment job status.

### 2. Getting Deployment Status

When you send a successful deployment request, the full request URL for checking the job's status (including your endpoint, project name, and job ID) is contained in the response's operation-location header.

Use the following **GET** request to get the status of your deployment job. Replace the placeholder values with your own values.

#### a. URL

HTTP

```HTTP
{ENDPOINT}/language/authoring/analyze-conversations/projects/{PROJECT-NAME}/deployments/{DEPLOYMENT-NAME}/jobs/{JOB-ID}?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="15%">
**Placeholder**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Value**
</edukamu-table-header>
<edukamu-table-header>
**Example**
</edukamu-table-header >
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint for authenticating your API request.
</edukamu-table-cell>
<edukamu-table-cell>

`https://<your-custom-subdomain>.cognitiveservices.azure.com`

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your project. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
myProject
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{DEPLOYMENT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name for your deployment. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
staging
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{JOB-ID}
</edukamu-table-cell>
<edukamu-table-cell>
The ID for locating your model's training status.
</edukamu-table-cell>
<edukamu-table-cell>
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you are calling.
</edukamu-table-cell>
<edukamu-table-cell>
2023-04-01
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


#### b. Headers

Use the following header to authenticate your request.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Ocp-Apim-Subscription-Key
</edukamu-table-cell>
<edukamu-table-cell>
The key
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


#### c. Request Body

Once you send the request, you'll get the following response. Keep polling this endpoint until the status parameter changes to "succeeded".

JSON

```JSON
{
    "jobId":"{JOB-ID}",
    "createdDateTime":"{CREATED-TIME}",
    "lastUpdatedDateTime":"{UPDATED-TIME}",
    "expirationDateTime":"{EXPIRATION-TIME}",
    "status":"running"
}
```

### 3. Query Model

After your model is deployed, you can start using it to make predictions through the prediction API.

Once deployment succeeds, you can begin querying your deployed model for predictions.

Create a POST request using the following URL, headers, and JSON body to start testing a conversational language understanding model.

#### a. Request URL

HTTP

```HTTP
{ENDPOINT}/language/:analyze-conversations?api-version={API-VERSION}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Placeholder**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
<edukamu-table-header>
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
{ENDPOINT}
</edukamu-table-cell>
<edukamu-table-cell>
The endpoint for authenticating your API request.
</edukamu-table-cell>
<edukamu-table-cell>

`https://<your-custom-subdomain>.cognitiveservices.azure.com`

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
{API-VERSION}
</edukamu-table-cell>
<edukamu-table-cell>
The version of the API you are calling.
</edukamu-table-cell>
<edukamu-table-cell>
2023-04-01
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


#### b. Headers

Use the following header to authenticate your request.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Ocp-Apim-Subscription-Key
</edukamu-table-cell>
<edukamu-table-cell>
The key to your resource. Used for authenticating your API requests.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


#### c. Request Body

JSON

```JSON
{
  "kind": "Conversation",
  "analysisInput": {
    "conversationItem": {
      "id": "1",
      "participantId": "1",
      "text": "Text 1"
    }
  },
  "parameters": {
    "projectName": "{PROJECT-NAME}",
    "deploymentName": "{DEPLOYMENT-NAME}",
    "stringIndexType": "TextElement_V8"
  }
}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Key**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Placeholder**
</edukamu-table-header>
<edukamu-table-header width="40%">
**Value**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
participantId
</edukamu-table-cell>
<edukamu-table-cell>
{JOB-NAME}
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
"MyJobName
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
id
</edukamu-table-cell>
<edukamu-table-cell>
{JOB-NAME}
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
"MyJobName
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
text
</edukamu-table-cell>
<edukamu-table-cell>
{TEST-UTTERANCE}
</edukamu-table-cell>
<edukamu-table-cell>
The utterance that you want to predict its intent and extract entities from.
</edukamu-table-cell>
<edukamu-table-cell>
"Read Matt's email
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
projectName
</edukamu-table-cell>
<edukamu-table-cell>
{PROJECT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name of your project. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
myProject
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
deploymentName
</edukamu-table-cell>
<edukamu-table-cell>
{DEPLOYMENT-NAME}
</edukamu-table-cell>
<edukamu-table-cell>
The name of your deployment. This value is case-sensitive.
</edukamu-table-cell>
<edukamu-table-cell>
staging
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

Once you send the request, you will get the following response for the prediction.

#### d. Response Body

JSON

```JSON
{
  "kind": "ConversationResult",
  "result": {
    "query": "Text1",
    "prediction": {
      "topIntent": "inten1",
      "projectKind": "Conversation",
      "intents": [
        {
          "category": "intent1",
          "confidenceScore": 1
        },
        {
          "category": "intent2",
          "confidenceScore": 0
        },
        {
          "category": "intent3",
          "confidenceScore": 0
        }
      ],
      "entities": [
        {
          "category": "entity1",
          "text": "text1",
          "offset": 29,
          "length": 12,
          "confidenceScore": 1
        }
      ]
    }
  }
}
```

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Key**
</edukamu-table-header>
<edukamu-table-header>
**Sample Value**
</edukamu-table-header>
<edukamu-table-header>
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
query
</edukamu-table-cell>
<edukamu-table-cell>
"Read Matt's email"
</edukamu-table-cell>
<edukamu-table-cell>
The text you submitted for query.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
topIntent
</edukamu-table-cell>
<edukamu-table-cell>
"Read"
</edukamu-table-cell>
<edukamu-table-cell>
The predicted intent with highest confidence score.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
intents
</edukamu-table-cell>
<edukamu-table-cell>
[]
</edukamu-table-cell>
<edukamu-table-cell>
A list of all the intents that were predicted for the query text each of them with a confidence score.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
entities
</edukamu-table-cell>
<edukamu-table-cell>
[]
</edukamu-table-cell>
<edukamu-table-cell>
Array containing list of extracted entities from the query text.
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


### API Response for a Conversations Project

In a conversations project, you'll get predictions for both your intents and entities that are present within your project.

- The intents and entities include a confidence score between 0.0 to 1.0 associated with how confident the model is about predicting a certain element in your project.
- The top scoring intent is contained within its own parameter.
- Only predicted entities will show up in your response.
- Entities indicate: 
    - The text of the entity that was extracted
    - Its start location denoted by an offset value
    - The length of the entity text denoted by a length value.

</edukamu-collapse>
<br>


Did you manage to follow the instructions and complete and/or understand the process described above? In that case, congratulations are in order! You’re already well underway towards grasping conversational language understanding on a technical level!

We’ll continue with this topic for a little longer, but please recap a while and complete the following exercise before continuing.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Basics of CLU
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module2/conversational-language-understanding-text-poll-1.yaml" id="wleuhv0zyybu08bu">

<edukamu-text-poll url="/exercises/module2/conversational-language-understanding-text-poll-2.yaml" id="4qezyrmhmdan6phq">

<edukamu-text-poll url="/exercises/module2/conversational-language-understanding-text-poll-3.yaml" id="v7sl3pfmugjftiel"> 

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/2/conversational-language-understanding?question=wleuhv0zyybu08bu">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

We’ve covered a lot in the second unit already, haven’t we? On the next page, we’ll explore conversational language understanding a little further. Let’s keep going!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
