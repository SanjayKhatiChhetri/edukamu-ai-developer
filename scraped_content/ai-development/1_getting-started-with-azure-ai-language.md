## Getting Started with Azure AI Language

Do you still remember the term natural language processing, or NLP for short? This revolutionary technology essentially combines language understanding with the seemingly endless computing power offered by cloud services, and by now, you should already be familiar with the fundamentals after completing the first courses of this study program.

In today's digital age, understanding and harnessing the power of human language is fundamental to creating intelligent and responsive applications, and Azure AI Language Service is your gateway to doing just that.

The second unit is all about natural language processing, and right now we’re going to get started by exploring Azure AI Language.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure AI Language
</edukamu-collapse-hidden-title>

Every day, the world generates a vast quantity of data; much of it text-based in the form of emails, social media posts, online reviews, business documents, and more. Artificial intelligence techniques that apply statistical and semantic models enable you to create applications that extract meaning and insights from this text-based data.

The Azure AI Language provides an API for common text analysis techniques that you can easily integrate into your own application code. Let’s find out more, shall we?

### Provisioning Azure AI Language Resources

Azure AI Language is designed to help you extract information from text. It provides functionality that you can use for:

- **Language detection** - determining the language in which text is written.
- **Key phrase extraction** - identifying important words and phrases in the text that indicate the main points.
- **Sentiment analysis** - quantifying how positive or negative the text is.
- **Named entity recognition** - detecting references to entities, including people, locations, time periods, organizations, and more.
- **Entity linking** - identifying specific entities by providing reference links to Wikipedia articles.

<edukamu-image url="/graphics/module1/text-analytics-resource.png" alt="Diagram showing an Azure AI Language resource performing language detection, key phrase extraction, sentiment analysis, named entity recognition, and entity linking." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

### Azure Resources for Text Analysis

To use Azure AI Language to analyze text, you must provision a resource for it in your Azure subscription.

After you have provisioned a suitable resource in your Azure subscription, you can use its endpoint and one of its keys to call the Azure AI Language APIs from your code. You can call the Azure AI Language APIs by submitting requests in JSON format to the REST interface, or by using any of the available programming language-specific SDKs.

**Note:** The code examples in the subsequent sections show the JSON requests and responses exchanged with the REST interface. When using an SDK, the JSON requests are abstracted by appropriate objects and methods that encapsulate the same data values. You'll get a chance to try the SDK for C# or Python for yourself in the exercise later.

</edukamu-collapse>
<br>

Whether you aim to create chatbots, sentiment analysis engines, language translation tools, or any other language-driven application, Azure AI Language Service provides you with the building blocks to bring your ideas to life.

We have a lot to cover, so let’s keep moving! Next, we’ll briefly visit 1) language detection, 2) key-phrase extraction, and 3) sentiment analysis.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1) Language Detection with Azure AI Language
</edukamu-collapse-hidden-title>

The Azure AI Language detection API evaluates text input and, for each document submitted, returns language identifiers with a score indicating the strength of the analysis.

This capability is useful for content stores that collect arbitrary text, where language is unknown. Another scenario could involve a chat bot. If a user starts a session with the chat bot, language detection can be used to determine which language they are using and allow you to configure your bot responses in the appropriate language.

You can parse the results of this analysis to determine which language is used in the input document. The response also returns a score, which reflects the confidence of the model (a value between 0 and 1).

Language detection can work with documents or single phrases. It's important to note that the document size must be under 5,120 characters. The size limit is per document and each collection is restricted to 1,000 items (IDs). A sample of a properly formatted JSON payload that you might submit to the service in the request body is shown here, including a collection of **documents**, each containing a unique **id** and the **text** to be analyzed. Optionally, you can provide a **countryHint** to improve prediction performance.

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
                "id": "1",
                "text": "Hello world",
                "countryHint": "US"
              },
              {
                "id": "2",
                "text": "Bonjour tout le monde"
              }
        ]
    }
}
```

The service will return a JSON response that contains a result for each document in the request body, including the predicted language and a value indicating the confidence level of the prediction. The confidence level is a value ranging from 0 to 1 with values closer to 1 being a higher confidence level. Here's an example of a standard JSON response that maps to the above request JSON.

JSON

```JSON
{   "kind": "LanguageDetectionResults",
    "results": {
        "documents": [
          {
            "detectedLanguage": {
              "confidenceScore": 1,
              "iso6391Name": "en",
              "name": "English"
            },
            "id": "1",
            "warnings": []
          },
          {
            "detectedLanguage": {
              "confidenceScore": 1,
              "iso6391Name": "fr",
              "name": "French"
            },
            "id": "2",
            "warnings": []
          }
        ],
        "errors": [],
        "modelVersion": "2022-10-01"
    }
}
```

In our sample, all of the languages show a confidence of 1, mostly because the text is relatively simple and easy to identify the language for.

If you pass in a document that has multilingual content, the service will behave a bit differently. Mixed language content within the same document returns the language with the largest representation in the content, but with a lower positive rating, reflecting the marginal strength of that assessment. In the following example, the input is a blend of English, Spanish, and French. The analyzer uses statistical analysis of the text to determine the *predominant* language.

JSON

```JSON
{
  "documents": [
    {
      "id": "1",
      "text": "Hello, I would like to take a class at your University. ¿Se ofrecen clases en español? Es mi primera lengua y más fácil para escribir. Que diriez-vous des cours en français?"
    }
  ]
}

```

The following sample shows a response for this multi-language example.

JSON

```JSON
{
    "documents": [
        {
            "id": "1",
            "detectedLanguage": {
                "name": "Spanish",
                "iso6391Name": "es",
                "confidenceScore": 0.9375
            },
            "warnings": []
        }
    ],
    "errors": [],
    "modelVersion": "2022-10-01"
}
```


The last condition to consider is when there is ambiguity as to the language content. The scenario might happen if you submit textual content that the analyzer is not able to parse, for example because of character encoding issues when converting the text to a string variable. As a result, the response for the language name and ISO code will indicate (unknown) and the score value will be returned as 0. The following example shows how the response would look.

JSON

```JSON
{
    "documents": [
        {
            "id": "1",
            "detectedLanguage": {
                "name": "(Unknown)",
                "iso6391Name": "(Unknown)",
                "confidenceScore": 0.0
            },
            "warnings": []
        }
    ],
    "errors": [],
    "modelVersion": "2022-10-01"
}
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2) Key-Phrase Extraction with Azure AI Language
</edukamu-collapse-hidden-title>

Key phrase extraction is the process of evaluating the text of a document, or documents, and then identifying the main points around the context of the document(s).

Key phrase extraction works best for larger documents (the maximum size that can be analyzed is 5,120 characters).

As with language detection, the REST interface enables you to submit one or more documents for analysis.

JSON

```JSON
{
    "kind": "KeyPhraseExtraction",
    "parameters": {
        "modelVersion": "latest"
    },
    "analysisInput":{
        "documents":[
            {
              "id": "1",
              "language": "en",
              "text": "You must be the change you wish 
                       to see in the world."
            },
            {
              "id": "2",
              "language": "en",
              "text": "The journey of a thousand miles 
                       begins with a single step."
            }
        ]
    }
}
```

The response contains a list of key phrases detected in each document:

JSON

```JSON
{
    "kind": "KeyPhraseExtractionResults",
    "results": {
    "documents": [   
        {
         "id": "1",
         "keyPhrases": [
           "change",
           "world"
         ],
         "warnings": []
       },
       {
         "id": "2",
         "keyPhrases": [
           "miles",
           "single step",
           "journey"
         ],
         "warnings": []
       }
],
    "errors": [],
    "modelVersion": "2021-06-01"
    }
}
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3) Sentiment Analysis with Azure AI Language
</edukamu-collapse-hidden-title>

Sentiment analysis is used to evaluate how positive or negative a text document is, which can be useful in various workloads, such as:

- Evaluating a movie, book, or product by quantifying sentiment based on reviews. 
- Prioritizing customer service responses to correspondence received through email or social media messaging.

When using Azure AI Language to evaluate sentiment, the response includes overall document sentiment and individual sentence sentiment for each document submitted to the service.

For example, you could submit a single document for sentiment analysis like this:

JSON

```JSON
{
  "kind": "SentimentAnalysis",
  "parameters": {
    "modelVersion": "latest"
  },
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "en",
        "text": "Good morning!"
      }
    ]
  }
}
```

The response from the service might look like this:

JSON

```JSON
{
  "kind": "SentimentAnalysisResults",
  "results": {
    "documents": [
      {
        "id": "1",
        "sentiment": "positive",
        "confidenceScores": {
          "positive": 0.89,
          "neutral": 0.1,
          "negative": 0.01
        },
        "sentences": [
          {
            "sentiment": "positive",
            "confidenceScores": {
              "positive": 0.89,
              "neutral": 0.1,
              "negative": 0.01
            },
            "offset": 0,
            "length": 13,
            "text": "Good morning!"
          }
        ],
        "warnings": []
      }
    ],
    "errors": [],
    "modelVersion": "2022-11-01"
  }
}
```

Sentence sentiment is based on confidence scores for **positive**, **negative**, and **neutral** classification values between 0 and 1.

Overall document sentiment is based on sentences:

- If all sentences are neutral, the overall sentiment is neutral.
- If sentence classifications include only positive and neutral, the overall sentiment is positive.
- If the sentence classifications include only negative and neutral, the overall sentiment is negative.
- If the sentence classifications include positive and negative, the overall sentiment is mixed.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-orange">
All the capabilities described above are so advanced that just imagining them a decade ago would have seemed like science fiction. With the power of Microsoft Azure, however, such capabilities are at your fingertips!

When developing with Azure, there’s no need to understand all technical aspects of every solution you encounter. Instead, you can rest assured that the services are constantly being developed and maintained for you, by Microsoft, while you focus on what matters the most – your solutions.

All right, let’s get back on track. Azure AI Language also provides advanced capabilities for recognizing information and patterns from natural language. In essence, we’re talking about extracting entities.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Extracting Entities
</edukamu-collapse-hidden-title>

Named Entity Recognition identifies entities that are mentioned in the text. Entities are grouped into categories and subcategories, for example:

- Person
- Location
- DateTime
- Organization
- Address
- Email
- URL

Input for entity recognition is similar to input for other Azure AI Language API functions:

JSON

```JSON
{
  "kind": "EntityRecognition",
  "parameters": {
    "modelVersion": "latest"
  },
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "en",
        "text": "Joe went to London on Saturday"
      }
    ]
  }
}
```

The response includes a list of categorized entities found in each document:

JSON

```JSON
{
    "kind": "EntityRecognitionResults",
     "results": {
          "documents":[
              {
                  "entities":[
                  {
                    "text":"Joe",
                    "category":"Person",
                    "offset":0,
                    "length":3,
                    "confidenceScore":0.62
                  },
                  {
                    "text":"London",
                    "category":"Location",
                    "subcategory":"GPE",
                    "offset":12,
                    "length":6,
                    "confidenceScore":0.88
                  },
                  {
                    "text":"Saturday",
                    "category":"DateTime",
                    "subcategory":"Date",
                    "offset":22,
                    "length":8,
                    "confidenceScore":0.8
                  }
                ],
                "id":"1",
                "warnings":[]
              }
          ],
          "errors":[],
          "modelVersion":"2021-01-15"
    }
}
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Extracting Linked Entities
</edukamu-collapse-hidden-title>

In some cases, the same name might be applicable to more than one entity. For example, does an instance of the word "Venus" refer to the planet or the goddess from mythology?

Entity linking can be used to disambiguate entities of the same name by referencing an article in a knowledge base. Wikipedia provides the knowledge base for the Text Analytics service. Specific article links are determined based on entity context within the text.

For example, "I saw Venus shining in the sky" is associated with the link https://en.wikipedia.org/wiki/Venus; while "Venus, the goddess of beauty" is associated with https://en.wikipedia.org/wiki/Venus_(mythology).

As with all Azure AI Language service functions, you can submit one or more documents for analysis:

JSON
```JSON
{
  "kind": "EntityLinking",
  "parameters": {
    "modelVersion": "latest"
  },
  "analysisInput": {
    "documents": [
      {
        "id": "1",
        "language": "en",
        "text": "I saw Venus shining in the sky"
      }
    ]
  }
}
```

The response includes the entities identified in the text along with links to associated articles:

JSON
```JSON
{
  "kind": "EntityLinkingResults",
  "results": {
    "documents": [
      {
        "id": "1",
        "entities": [
          {
            "bingId": "89253af3-5b63-e620-9227-f839138139f6",
            "name": "Venus",
            "matches": [
              {
                "text": "Venus",
                "offset": 6,
                "length": 5,
                "confidenceScore": 0.01
              }
            ],
            "language": "en",
            "id": "Venus",
            "url": "https://en.wikipedia.org/wiki/Venus",
            "dataSource": "Wikipedia"
          }
        ],
        "warnings": []
      }
    ],
    "errors": [],
    "modelVersion": "2021-06-01"
  }
}
```

</edukamu-collapse>
<br>

When it comes to natural language processing, Azure AI Language is among the most capable services. After this brief but comprehensive introduction, we’re all set to start delving in deeper!

<edukamu-section class="slate-section slate-orange">
If you’ve completed the previous courses of this program, you should already be familiar with the practice exercises. These exercises give you the opportunity to explore Microsoft Azure on your own and learn a thing or two about the tools and capabilities we’ve explored – and this course also includes such exercises.

As you also might remember, the practice exercises are not a mandatory requirement for completing this course since they may require software or services not available everywhere. We do recommend that you complete them if you have the change, though! 

It’s time for the first practical exercise of this course. In order to access Microsoft Azure, you’ll need an active subscription. Below, you’ll also find detailed instructions on how to activate a free trial.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step-by-Step Guide for Activating a Free Azure Trial
</edukamu-collapse-hidden-title>

If you're having trouble activating your free Azure trial needed for accessing Microsoft Azure, follow the step-by-step instructions below.

**1.** Navigate to <edukamu-link url="https://azure.microsoft.com/en-us/" target="_blank">Microsoft Azure</edukamu-link>.

**2.** Click "Sign in".

<edukamu-image url="/graphics/module1/step-2.jpeg" alt="Screenshot from Microsoft Azure homepage with highlighted Sign in -button at the top of the page." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**3.** Sign in to your account.

Notice that you need a Microsoft account in order to use activate a free Azure trial. You can either use your organizational account (such as school or work) or create a new one free of charge.

<edukamu-image url="/graphics/module1/step-3.jpeg" alt="Screenshot from Sign in -view with the highlighted Next -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**4.** Enter your password.

<edukamu-image url="/graphics/module1/step-4.jpeg" alt="Screenshot from Enter Password -view with the highlighted Sign in -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**5.** Click the "Subscriptions" icon.

<edukamu-image url="/graphics/module1/step-5.jpeg" alt="Screenshot from Azure services menu with highlighted Subscriptions -icon." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**6.** Click this "+ Add" icon to add a new Subscription.

<edukamu-image url="/graphics/module1/step-6.jpeg" alt="Screenshot from Subscription -view with highlighted + Add -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**7.** Click "Try Azure for free"; We will add a trial subscription in this example.

<edukamu-image url="/graphics/module1/step-7.jpeg" alt="Screenshot from Free trial -view with highlighted Try Azure for free -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**8.** Fill in your details including your phone number for identity verification.

<edukamu-image url="/graphics/module1/step-8.jpeg" alt="Screenshot from personal information fields with highlighted Phone -field." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**9.** Click "Text me".

<edukamu-image url="/graphics/module1/step-9.jpeg" alt="Screenshot from personal information fields with highlighted Text me -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**10.** Type in the code and then click "Verify code".

<edukamu-image url="/graphics/module1/step-10.jpeg" alt="Screenshot from personal information fields with written verification code and highlighted Verify code -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**11.** Fill in the rest of the form.

<edukamu-image url="/graphics/module1/step-11.jpeg" alt="Screenshot from personal information fields with highlighted Address line 1 -field." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**12.** Accept Agreements.

<edukamu-image url="/graphics/module1/step-12.jpeg" alt="creenshot from personal information fields with accepted agreements." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**13.** Click "Next".

<edukamu-image url="/graphics/module1/step-13.jpeg" alt="Screenshot from personal information fields with highlighted Next -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

**14.** Fill in your credit card information for Identity Verification (you will not be charged) and click "Sign up".

<edukamu-image url="/graphics/module1/step-14.jpeg" alt="Screenshot from personal information fields with highlighted Sign up -button." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

You can find additional information about Microsoft Azure's free trial (also needed for accessing Power Platform) over at <edukamu-link url="https://azure.microsoft.com/en-us/free" target="_blank">Microsoft's website</edukamu-link>.


If setting up a free Azure trial isn't possible for one reason or another, don't worry. You can still follow the practical exercises carefully and complete the courses without exploring Microsoft Azure yourself.

</edukamu-collapse>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Using Azure AI Services
</edukamu-collapse-hidden-title>

**Reminder:** Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practice exercise, we’ll have a go at using Azure AI Services provided by Microsoft. The exercise uses a lab environment, and you’ll find detailed instructions below.

(Microsoft provides this lab experience and related content for educational purposes. All presented information is owned by Microsoft and intended solely for learning about the covered products and services.)

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/create-manage-ai-services/5a-exercise-ai-services?launch-lab=true">Microsoft Learn: Lab Environment</edukamu-button>
<br>

Please notice that you need to sign into your Microsoft account (personal or professional) in order to use the Lab environment.

After signing in, you can launch the Lab environment by clicking on the button illustrated in the image below.

<edukamu-image url="/graphics/module1/lab-ohje.png" alt="Picture illustrating the lab button on Microsoft Learn." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

The lab environment (Virtual Machine) will launch in a separate window. You’ll find detailed instructions on signing in, getting started, and completing the practice exercise on the right.

<edukamu-image url="/graphics/module1/lab-ohje-2.png" alt="Picture illustrating the lab environment." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

We highly recommend that you try your hands with the practical exercises! Good luck!

</edukamu-collapse>
<br> -->

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Analyze Text with Azure AI Language
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practical exercise, you’ll get to analyze text with the Azure AI Language service.

This exercise uses a virtual machine, provided by Microsoft, on Microsoft’s Learn platform. In order to set up the lab environment, please navigate to the Microsoft Learn platform.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/analyze-text-ai-language/8-exercise-analyze-text" target="_blank">Microsoft Learn: Lab Environment</edukamu-button>
<br>

Please notice that you need to sign into your Microsoft account (personal or professional) in order to use the Lab environment. 

After signing in, you can launch the Lab environment by clicking on the button illustrated in the image below.

<edukamu-image url="/graphics/module1/lab-ohje.png" alt="Picture illustrating the lab button on Microsoft Learn." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>
<!-- Lab-ohje.png
Vaihtoehtoinen teksti: Picture illustrating the lab button on Microsoft Learn. -->

The lab environment (Virtual Machine) will launch in a separate window. You’ll find detailed instructions on signing in, getting started, and completing the practice exercise on the right.

<edukamu-image url="/graphics/module1/lab-ohje-2.png" alt="Picture illustrating the lab environment." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

Good luck!

</edukamu-collapse>
<br>

There’s one exercise left before finishing this unit. Take some time to recap before completing it. 

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Introduction to Azure AI Language
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/getting-started-with-azure-ai-language-question-scroll-1.yaml" id="hfoil567l33t2mj6">
<br>

</edukamu-collapse>
<br>


That’s the first unit in the bag – awesome work! After exploring Azure AI Services, it’s time to shift our focus to natural language processing, which is arguably one of the most interesting technologies right now.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
