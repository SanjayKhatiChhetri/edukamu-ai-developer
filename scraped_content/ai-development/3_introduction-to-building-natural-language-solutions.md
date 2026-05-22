## Introduction to Building Natural Language Solutions

Now that we've explored Retrieval Augmented Generation (RAG) and Conversational Language Understanding (CLU), it's time to take our knowledge to the next level. These concepts have given us a glimpse into the powerful capabilities of natural language processing and AI-driven language models. However, learning about them is just the beginning of our journey.

In the world of technology and AI, turning theoretical capabilities into practical solutions is key. The true value lies in how we can harness the exciting concepts to build practical and innovative natural language solutions. On this page, we’ll take a look at the process.

<edukamu-note class="edukamu-note-icon-info">

**Azure OpenAI Service**

In the following sections, we’ll explore the process of creating natural language solutions with a toolbox called Azure OpenAI Service. We’ll explore it in detail in the fourth unit, but here’s a quick overview:

Azure OpenAI Service is a cloud-based offering that provides access to OpenAI's powerful language models, such as GPT-3, within the Azure cloud ecosystem. This service allows developers and organizations to integrate OpenAI's state-of-the-art natural language processing capabilities into their own applications, products, and services hosted on Microsoft Azure. Users can leverage these language models for various tasks, including text generation, language translation, content summarization, chatbots, and more.

Azure OpenAI Service provides a convenient and scalable way to incorporate advanced language understanding and generation capabilities into a wide range of applications, making it easier to build intelligent and conversational systems.

</edukamu-note>
<br>

Azure OpenAI Service is advanced, yet still simple to use, as you’ll soon see. In the following sections we’ll review 1) integrating the service into an application, 2) using Azure OpenAI REST API, and 3) using Azure OpenAI SDK.

Before beginning, let’s review the roles of REST API and SDK in this context.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### REST API, SDK, and Azure OpenAI Service
</edukamu-collapse-hidden-title>

In the context of Azure OpenAI Service, REST API and SDK play crucial roles:

1. **REST API (Representational State Transfer Application Programming Interface):**
  - **Overview**: REST API is a set of rules and conventions for building and interacting with web services. It allows developers to access and utilize the functionality of Azure OpenAI Service over the Internet.
  - **Significance**: With the REST API, developers can make HTTP requests to access the capabilities of Azure OpenAI Service from any programming language or platform. This is particularly useful for integrating AI language models into web applications, mobile apps, or any software that can communicate over the web.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">SDK (Software Development Kit):</span>
</li>
</ol>
</edukamu-section>
  - **Overview**: SDK is a set of pre-built libraries, tools, and code samples that simplifies the process of working with Azure OpenAI Service. It provides a higher-level abstraction and streamlined methods for interacting with the service compared to using raw HTTP requests.
  - **Significance**: The Azure OpenAI SDK makes it easier and more efficient for developers to integrate OpenAI's language models into their applications. It offers ready-made functions and components, reducing the complexity of implementation and allowing developers to focus on the specific AI capabilities they want to leverage.

In summary, while the REST API provides the fundamental means of communication with Azure OpenAI Service using HTTP requests while the SDK offers a more developer-friendly and efficient way to integrate the service into applications by providing pre-built tools and libraries. Developers can choose between these two options based on their project requirements and familiarity with programming interfaces.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-orange">
(If you feel confused about REST APIs and SDKs, please refer back to the earlier courses within this study program.)

Azure OpenAI provides a platform for developers to add artificial intelligence functionalities to their applications with the help of both Python and C# SDKs and REST APIs. The platform has various AI models available, each specializing in different tasks, which can be deployed through the Azure OpenAI Service.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Integrating Azure OpenAI Service
</edukamu-collapse-hidden-title>

Azure OpenAI (AOAI) offers both C# and Python SDKs and a REST API that developers can use to add AI functionality to their applications. Generative AI capabilities in Azure OpenAI are provided through models. The models available in the Azure OpenAI service belong to different families, each with their own focus. To use one of these models, you need to deploy through the Azure OpenAI Service.

**Important**: Azure OpenAI has been released with limited access to support the responsible use of the service. Users need to apply for access and be approved before they can create an AOAI resource.

### Creating Azure OpenAI Resources

An AOAI resource can be deployed through both the Azure command line interface (CLI) and the Azure portal. Creating the AOAI resource through the Azure portal is similar to deploying individual Azure AI Services resources and is part of the Azure AI Services services.

1. Navigate to the Azure Portal.
2. Search for **Azure OpenAI**, select it, and click **Create**.
3. Enter the appropriate values for the empty fields, and create the resource.

The possible regions for an AOAI are currently limited. Choose the region closest to your physical location.

Once the resource has been created, you'll have keys and an endpoint that you can use in your app.


### Choosing and Deploying a Model

Each model family excels at different tasks, and there are different capabilities of the models within each family. Model families break down into three main families:

- **Text** or **Generative Pre-trained Transformer (GPT)** - Models that understand and generate natural language and some code. These models are best at general tasks, conversations, and chat formats.
- **Code** - Code models are built on top of GPT models, and trained on millions of lines of code. These models can understand and generate code, including interpreting comments or natural language to generate code.
- **Embeddings** - These models can understand and use embeddings, which are a special format of data that can be used by machine learning models and algorithms.

This section focuses on general GPT models.

The model family and capability is indicated in the name of the base model, such as text-davinci-003, which specifies that it's a text model, with davinci level capability, and identifier 3. Details on models, capability levels, and naming conventions can be found on the AOAI Models documentation page.

To deploy a model for you to use, navigate to the Azure OpenAI Studio and go to the **Deployments** page. The lab later in this section covers exactly how to do that.


### Authentication and Specification of Deployed Models

When you deploy a model in AOAI, you choose a deployment name to give it. When configuring your app, you need to specify your resource endpoint, key, and deployment name to specify which deploy model to send your request to. This enables you to deploy various models within the same resource, and make requests to the appropriate model depending on the task.


### Prompt Engineering

How the input prompt is written plays a large part in how the AI model will respond. For example, if prompted with a simple request such as "What is Azure OpenAI", you often get a generic answer similar to using a search engine.

However, if you give it more details about what you want in your response, you get a more specific answer. For example, given this prompt:

```
Classify the following news headline into 1 of the following categories: Business, Tech, Politics, Sport, Entertainment

Headline 1: Donna Steffensen Is Cooking Up a New Kind of Perfection. The Internet’s most beloved cooking guru has a buzzy new book and a fresh new perspective
Category: Entertainment

Headline 2: Major Retailer Announces Plans to Close Over 100 Stores
Category:
```

You'll likely get the "Category:" under headline filled out with "Business".

Several examples similar to this one can be found in the Azure OpenAI Studio Playground, under the Examples dropdown. Try to be as specific as possible about what you want in response from the model, and you may be surprised at how insightful it can be!

**Note**: It is never safe to assume that answers from an AI model are factual or correct. Teams or individuals tasked with developing and deploying AI systems should work to identify, measure, and mitigate harm. It is your responsibility to verify any responses from an AI model, and to use AI responsibly. In the fourth unit, we’ll review a few key aspects of responsibly and ethically using artificial intelligence.


### Available Endpoints

AOAI can be accessed via a REST API or an SDK currently available for Python and C#. The endpoints available for interacting with a deployed model are used differently, and certain endpoints can only use certain models. The available endpoints are:

- **Completion** - model takes an input prompt, and generates one or more predicted completions
- **ChatCompletion** - model takes input in the form of a chat conversation (where roles are specified with the message they send), and the next chat completion is generated
- **Embeddings** - model takes input and returns a vector representation of that input

For example, the input for Completion might be a prompt like "What is Azure OpenAI", or it might include some role tags or other prompt engineering elements.

```
<|im_start|>user
What is Azure OpenAI?
<|im_end|>
```

In contrast, the input for ChatCompletion is a conversation with clearly defined roles for each message:

JSON

```JSON
{"role": "system", "content": "You are a helpful assistant, teaching people about AI."},
{"role": "user", "content": "Does Azure OpenAI support multiple languages?"},
{"role": "assistant", "content": "Yes, Azure OpenAI supports several languages, and can translate between them."},
{"role": "user", "content": "Do other Azure AI Services support translation too?"}
```

When you give the AI model a real conversation, it can generate a better response with more accurate tone, phrasing, and context. The ChatCompletion endpoint enables the ChatGPT model to have a more realistic conversation by sending the history of the chat with the next user message.

ChatCompletion also allows for non-chat scenarios, such as summarization or entity extraction that you can do with the Completion endpoint. This can be accomplished by providing a short conversation, specifying the system information and what you want, along with the user input. For example, if you want to generate a job description, provide ChatCompletion with something like the following conversation input.

JSON

```JSON
{"role": "system", "content": "You are an assistant designed to write intriguing job descriptions. "},
{"role": "user", "content": "Write a job description for the following job title: 'Business Intelligence Analyst'. It should include responsibilities, required qualifications, and highlight benefits like time off and flexible hours."}
```

**Note**: Completion is available for all gpt-3 generation models, while ChatCompletion is the only supported option for gpt-4 models and is the preferred endpoint when using the gpt-35-turbo model. The lab in this section uses gpt-35-turbo with the ChatCompletion endpoint.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Using Azure OpenAI Service REST API
</edukamu-collapse-hidden-title>

AOAI offers a REST API for interacting and generating responses that developers can use to add AI functionality to their applications. This unit covers example usage, input and output from the API.

**Note**: Before interacting with the API, you must create an Azure OpenAI resource in the Azure portal, deploy a model in that resource, and retrieve your endpoint and keys.

For each call to the REST API, you need the endpoint and a key from your Azure OpenAI resource, and the name you gave for your deployed model. In the following examples, the following placeholders are used:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
**Placeholder name**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
YOUR_ENDPOINT_NAME
</edukamu-table-cell>
<edukamu-table-cell>
This base endpoint is found in the **Keys & Endpoint** section in the Azure portal. It's the base endpoint of your resource, such as https://sample.openai.azure.com/.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
YOUR_API_KEY
</edukamu-table-cell>
<edukamu-table-cell>
Keys are found in the **Keys & Endpoint** section in the Azure portal. You can use either key for your resource.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
YOUR_DEPLOYMENT_NAME
</edukamu-table-cell>
<edukamu-table-cell>
This deployment name is the name provided when you deployed your model in the Azure OpenAI Studio.
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


### Completions

Once you've deployed a model in your AOAI resource, you can send a prompt to the service using a POST request. One endpoint is completions, which generates the completion of your prompt.

HTTP

```HTTP
curl https://YOUR_ENDPOINT_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/completions?api-version=2022-12-01\
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d "{
  \"prompt\": \"Your favorite Shakespeare is\",
  \"max_tokens\": 5
}"
```

The response from the API will be similar to the following JSON:

JSON

```JSON
{
    "id": "<id>",
    "object": "text_completion",
    "created": 1679001781,
    "model": "text-davinci-003",
    "choices": [
        {
            "text": "Macbeth",
            "index": 0,
            "logprobs": null,
            "finish_reason": "stop"
        }
    ]
}
```

The completion response to look for is within choices[].text. Notice that also included in the response is finish_reason, which in this example is stop. Other possibilities for finish_reason include length, which means it used up the max_tokens specified in the request, or content_filter, which means the system detected harmful content was generated from the prompt. If harmful content is included in the prompt, the API request returns an error.


### Chat Completions

Similar to completions, chat/completions generates a completion to your prompt, but works best when that prompt is a chat exchange.

HTTP

```HTTP
curl https://YOUR_ENDPOINT_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/chat/completions?api-version=2023-03-15-preview \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d '{"messages":[{"role": "system", "content": "You are a helpful assistant, teaching people about AI."},
{"role": "user", "content": "Does Azure OpenAI support multiple languages?"},
{"role": "assistant", "content": "Yes, Azure OpenAI supports several languages, and can translate between them."},
{"role": "user", "content": "Do other Azure AI Services support translation too?"}]}'
```

The response from the API will be similar to the following JSON:

JSON

```JSON
{
    "id": "chatcmpl-6v7mkQj980V1yBec6ETrKPRqFjNw9",
    "object": "chat.completion",
    "created": 1679001781,
    "model": "gpt-35-turbo",
    "usage": {
        "prompt_tokens": 95,
        "completion_tokens": 84,
        "total_tokens": 179
    },
    "choices": [
        {
            "message":
                {
                    "role": "assistant",
                    "content": "Yes, other Azure AI Services also support translation. Azure AI Services offer translation between multiple languages for text, documents, or custom translation through Azure AI Services Translator."
                },
            "finish_reason": "stop",
            "index": 0
        }
    ]
}
```

Both completion endpoints allow for specifying other optional input parameters, such as *temperature*, *max_tokens* and more. If you'd like to include any of those parameters in your request, add them to the input data with the request.


### Embeddings

Embeddings are helpful for specific formats that are easily consumed by machine learning models. To generate embeddings from the input text, POST a request to the embeddings endpoint.

HTTP

```HTTP
curl https://YOUR_ENDPOINT_NAME.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT_NAME/embeddings?api-version=2022-12-01 \
  -H "Content-Type: application/json" \
  -H "api-key: YOUR_API_KEY" \
  -d "{\"input\": \"The food was delicious and the waiter...\"}"
```

When generating embeddings, be sure to use a model in AOAI meant for embeddings. Those models start with text-embedding or text-similarity, depending on what functionality you're looking for.

The response from the API will be similar to the following JSON:

JSON

```JSON
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [
        0.0172990688066482523,
        -0.0291879814639389515,
        ....
        0.0134544348834753042,
      ],
      "index": 0
    }
  ],
  "model": "text-embedding-ada:002"
}
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. Using Azure OpenAI Service SDK
</edukamu-collapse-hidden-title>

In the following examples, we’ll be using the C# programming language.

In addition to REST APIs covered in the previous unit, users can also access Azure OpenAI models through C# and Python SDKs. The same functionality is available through both REST and these SDKs.

**Note**: Before interacting with the API using either SDK, you must create an Azure OpenAI resource in the Azure portal, deploy a model in that resource, and retrieve your endpoint and keys. Check out the Getting started with Azure OpenAI Service to learn how to do that.

For both SDKs covered in this unit, you need the endpoint and a key from your Azure OpenAI resource, and the name you gave for your deployed model. In the following code snippets, the following placeholders are used:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
**Placeholder name**
</edukamu-table-header>
<edukamu-table-header>
**Value**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
YOUR_ENDPOINT_NAME
</edukamu-table-cell>
<edukamu-table-cell>
This base endpoint is found in the **Keys & Endpoint** section in the Azure portal. It's the base endpoint of your resource, such as https://sample.openai.azure.com/.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
YOUR_API_KEY
</edukamu-table-cell>
<edukamu-table-cell>
Keys are found in the **Keys & Endpoint** section in the Azure portal. You can use either key for your resource.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
YOUR_DEPLOYMENT_NAME
</edukamu-table-cell>
<edukamu-table-cell>
This deployment name is the name provided when you deployed your model in the Azure OpenAI Studio
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


### Installing Libraries

First, install the client library for your preferred language. The C# SDK is a .NET adaptation of the REST APIs and built specifically for Azure OpenAI, however it can be used to connect to Azure OpenAI resources or non-Azure OpenAI endpoints. The Python SDK is built and maintained by OpenAI.

Console

```Console
dotnet add package Azure.AI.OpenAI --prerelease
```


### Configuring Apps to Access Azure OpenAI Service

Configuration for each language varies slightly, but both require the same parameters to be set. The necessary parameters are endpoint, key, and the name of your deployment, which is called the engine when sending your prompt to the model.

Add the library to your app, and set the required parameters for your client

C#

```C#
// Add OpenAI library
using Azure.AI.OpenAI;

// Define parameters and initialize the client
string endpoint = "<YOUR_ENDPOINT_NAME>";
string key = "<YOUR_API_KEY>";
string deploymentName = "<YOUR_DEPLOYMENT_NAME>"; //SDK calls this "engine", but naming
                                                  // it "deploymentName" for clarity

OpenAIClient client = new OpenAIClient(new Uri(endpoint), new AzureKeyCredential(key));
```


### Calling Azure OpenAI Resource

Once you've configured your connection to Azure OpenAI, send your prompt to one of the available endpoints of Completion, ChatCompletion, or Embedding.

C#

```C#
string prompt = "What is Azure OpenAI?";

Response<Completions> completionsResponse = client.GetCompletions(deploymentName, prompt);
string completion = completionsResponse.Value.Choices[0].Text;
Console.WriteLine($"Chatbot: {completion}");
```

If using ChatCompletion, sending the prompt is formed differently.

C#

```C#
// Build completion options object
ChatCompletionsOptions chatCompletionsOptions = new ChatCompletionsOptions()
{
    Messages = 
    {
        new ChatMessage(ChatRole.System, "You are a helpful AI bot."), 
        new ChatMessage(ChatRole.User, "What is Azure OpenAI?")
    }
};

// Send request to Azure OpenAI model
ChatCompletions chatCompletionsResponse = client.GetChatCompletions(
    deploymentName, 
    chatCompletionsOptions);

ChatMessage completion = chatCompletionsResponse.Choices[0].Message;
Console.WriteLine($"Chatbot: {completion.Content}");
```

The response object contains several values, such as total_tokens and finish_reason. The completion from the response object will be similar to the following completion:

Console

```Console
"Azure OpenAI is a cloud-based artificial intelligence (AI) service that offers a range of tools and services for developing and deploying AI applications. Azure OpenAI provides a variety of services for training and deploying machine learning models, including a managed service for training and deploying deep learning models, a managed service for deploying machine learning models, and a managed service for managing and deploying machine learning models."
```

In both C# and Python, your create call can include optional parameters including temperature and max_tokens.

</edukamu-collapse>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Integrating Azure OpenAI into Your App
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practice exercise, we’ll integrate Azure OpenAI Service into an application. This practical exercise will also serve as a great introduction to the fourth unit, which you’ll find out quite soon.

This exercise uses a virtual machine, provided by Microsoft, on Microsoft’s Learn platform. In order to set up the lab environment, please navigate to the Microsoft Learn platform.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/build-language-solution-azure-openai/5-exercise?launch-lab=true" target="_blank">Microsoft Learn: Lab Environment</edukamu-button>
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

Good luck!

</edukamu-collapse>
<br> -->

Azure OpenAI Service, along with its impressive AI capabilities, can be integrated into any application with tools already familiar to you, namely REST APIs and SDKs. This being the case, you already have foundational knowledge on using the service – and soon, you’ll learn a lot more!

Before moving on to the fourth unit, complete the following exercise.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Integrating AOAI
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module3/introduction-to-building-natural-language-solutions-text-poll-1.yaml" id="0zm00u7ixbdkuuwi">

<edukamu-text-poll url="/exercises/module3/introduction-to-building-natural-language-solutions-text-poll-2.yaml" id="0fsprtbmsv2j5r91">

<edukamu-text-poll url="/exercises/module3/introduction-to-building-natural-language-solutions-text-poll-3.yaml" id="l32e73fn6mrkl1km">

<edukamu-text-poll url="/exercises/module3/introduction-to-building-natural-language-solutions-text-poll-4.yaml" id="kygbrqhxlf78rsli">

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/3/introduction-to-building-natural-language-solutions?question=0zm00u7ixbdkuuwi">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

Congratulations for completing the third unit – there’s just one left to go now! Take a while to relax in order to give your brain some room to breathe before moving on. The last unit of this course is all about Azure OpenAI.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
