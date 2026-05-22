<edukamu-video content="/videos/devai-7-unit4-video.yaml"/>
<br>

## Getting Started with Azure OpenAI

Welcome to the fourth and final unit of this course – and of the entire study program, for that matter! You’ve already come a long way, and now it’s time to use everything you’ve learned so far about AI and put it into good use.

We’ll spend the entire unit focusing on Azure OpenAI Service. We’ve already touched upon it a few times and even spent a while working with it in the previous unit. So far, we haven’t had a change to get properly acquainted with it, however, so we’ll start from the very basics to kick off this unit.

Without further ado, let’s find out more about Azure OpenAI Service!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure OpenAI Service
</edukamu-collapse-hidden-title>

Suppose you want to build a support application that summarizes text and suggest code. To build this app, you want to utilize the capabilities you see in ChatGPT, a chatbot built by the OpenAI research company that takes in natural language input from a user and returns a machine-created, human-like response.

Generative AI models power ChatGPT's ability to produce new content, such as text, code, and images, based on a natural language prompts. Many generative AI models are a subset of deep learning algorithms. These algorithms support various workloads across vision, speech, language, decision, search, and more.

Azure OpenAI Service brings these generative AI models to the Azure platform, enabling you to develop powerful AI solutions that benefit from the security, scalability, and integration of other services provided by the Azure cloud platform. These models are available for building applications through a REST API, various SDKs, and a Studio interface. This section guides you through the Azure OpenAI Studio experience, giving you the foundation to further develop solutions with generative AI.

The first step in building a generative AI solution with Azure OpenAI is to provision an Azure OpenAI resource in your Azure subscription. As of February 2024, Azure OpenAI Service is currently in limited access.

Once you have access to Azure OpenAI Service, you can get started by creating a resource in the Azure portal or with the Azure command line interface (CLI).


### Setting Up Resources with Azure Portal

When you create an Azure OpenAI Service resource, you need to provide a subscription name, resource group name, region, unique instance name, and select a pricing tier.

<edukamu-image url="/graphics/module4/create-azure-openai-portal.png" alt="Screenshot of the Azure portal's page to create an Azure OpenAI Service resource." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>


### Setting Up Resources with Azure CLI

To create an Azure OpenAI Service resource from the CLI, refer to this example and replace the following variables with your own:

- MyOpenAIResource: *replace with a unique name for your resource*
- OAIResourceGroup: *replace with your resource group name*
- eastus: *replace with the region to deploy your resource*
- subscriptionID: *replace with your subscription ID*

.NET CLI

``az cognitiveservices account create \``<br>
``-n MyOpenAIResource \``<br>
``-g OAIResourceGroup \``<br>
``-l eastus \``<br>
``--kind OpenAI \``<br>
``--sku s0 \``<br>
``--subscription subscriptionID``


**Note**: You can find the regions available for a service through the CLI command az account list-locations.

Azure OpenAI Service provides access to many types of models. You should keep in mind that certain models are only available in select regions. Consult the <edukamu-link url="https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/models#model-summary-table-and-region-availability/?azure-portal=true" target="_blank">Azure OpenAI model availability guide</edukamu-link> for region availability. You can create two Azure OpenAI resources per region.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Using Azure OpenAI Studio
</edukamu-collapse-hidden-title>

Azure OpenAI Studio provides access to model management, deployment, experimentation, customization, and learning resources.

You can access the Azure OpenAI Studio through the Azure portal after creating a resource, or at *https://oai.azure.com* by logging in with your Azure OpenAI resource instance. During the sign-in workflow, select the appropriate directory, Azure subscription, and Azure OpenAI resource.

<edukamu-image url="/graphics/module4/studio-portal.png" alt="Screenshot of the Azure OpenAI Studio portal which can be used to access several features." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

When you first open Azure OpenAI Studio, you'll see a call-to-action button at the top of the screen to deploy your first model. Selecting the option to create a new deployment opens the **Deployments** page, from where you can deploy a base model and start experimenting with it.

<edukamu-image url="/graphics/module4/openai-portal-navigation.png" alt="Screenshot of the Azure OpenAI Studio portal menu of pages." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

</edukamu-collapse>
<br>

As you’ve learned during these courses, Microsoft Azure contains multiple services for developing fast, modern, and reliable applications that use artificial intelligence. Azure OpenAI Service has an ace up its sleeve, though, and that’s generative AI.

Generative AI is capable of creating, or generating, brand-new contents using the data that was used in its training. Let’s see what kind of generative AI models the service offers!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Generative AI in Azure OpenAI Service
</edukamu-collapse-hidden-title>

To begin building with Azure OpenAI, you need to choose a base model and deploy it. Microsoft provides base models and the option to create customized base models. This section covers the currently available base models.

Azure OpenAI includes several types of model:

- **GPT-4 models** are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code completions based on natural language prompts.
- **GPT 3.5 models** can generate natural language and code completions based on natural language prompts. In particular, **GPT-35-turbo** models are optimized for chat-based interactions and work well in most generative AI scenarios.
- **Embeddings models** convert text into numeric vectors, and are useful in language analytics scenarios such as comparing text sources for similarities.
- **DALL-E models** are used to generate images based on natural language prompts. Currently, DALL-E models are in preview. DALL-E models aren't listed in the Azure OpenAI Studio interface and don't need to be explicitly deployed.

In the Azure OpenAI Studio, the **Models** page lists the available base models (other than DALL-E models) and provides an option to create additional customized models by fine-tuning the base models. The models that have a *Succeeded* status mean they're successfully trained and can be selected for deployment.

<edukamu-image url="/graphics/module4/studio-models.png" alt="Screenshot of the Azure OpenAI Studio portal's out-of-the-box generative AI models." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Deploying Generative AI Models
</edukamu-collapse-hidden-title>

You first need to deploy a model to make API calls to receive completions to prompts. When you create a new deployment, you need to indicate which base model to deploy. You can deploy any number of deployments in one or multiple Azure OpenAI resources as long as their TPM adds up to less than 240K total in that region. There are several ways you can deploy your base model.


### 1. Deployment with Azure OpenAI Studio

In Azure OpenAI Studio's **Deployments** page, you can create a new deployment by selecting a model name from the menu. The available base models come from the list in the models page.

<edukamu-image url="/graphics/module4/studio-deployment.png" alt="Screenshot of the Azure OpenAI Studio portal's model deployment wizard." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

From the *Deployments* page in the Studio, you can also view information about all your deployments including deployment name, model name, model version, status, date created, and more.


### 2. Deployment with Azure CLI

You can also deploy a model using the console. Using this example, replace the following variables with your own resource values:

- myResourceGroupName: *replace with your resource group name*
- myResourceName: *replace with your resource name*
- MyModel: *replace with a unique name for your model*
- gpt-35-turbo: *replace with the base model you wish to deploy*

.NET CLI

``az cognitiveservices account deployment create \``<br>
   ``-g myResourceGroupName \``<br>
   ``-n myResourceName \``<br>
   ``--deployment-name MyModel \``<br>
   ``--model-name gpt-35-turbo \``<br>
   ``--model-version "0301"  \``<br>
   ``--model-format OpenAI \``<br>
   ``--scale-settings-scale-type "Standard"``



### 3. Deployment with the REST API

You can deploy a model using the REST API. In the request body, you specify the base model you wish to deploy. While we won’t cover this method during this course, it’s good to be aware of its availability.

</edukamu-collapse>
<br>

Generative AI is used by writing prompts, which we’ve visited on a few occasions during this program. On the next page, we’ll delve deeper into this so-called prompt engineering, but we’ll already take a little head start right now.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Using Prompts
</edukamu-collapse-hidden-title>

Once the model is deployed, you can test how it completes prompts. A prompt is the text portion of a request that is sent to the deployed model's completions endpoint. Responses are referred to as completions, which can come in form of text, code, or other formats.


### Prompt Types

Prompts can be grouped into types of requests based on task.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Task type**
</edukamu-table-header>
<edukamu-table-header>
**Prompt example**
</edukamu-table-header>
<edukamu-table-header>
**Completion example**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
**Classifying content**
</edukamu-table-cell>
<edukamu-table-cell>
Tweet: I enjoyed the trip.
Sentiment:
</edukamu-table-cell>
<edukamu-table-cell>
Positive
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Generating new content**
</edukamu-table-cell>
<edukamu-table-cell>
List ways of traveling
</edukamu-table-cell>
<edukamu-table-cell>
1. Bike
2. Car ...
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Holding a conversation**
</edukamu-table-cell>
<edukamu-table-cell>
A friendly AI assistant
</edukamu-table-cell>
<edukamu-table-cell>
I’m here to help, what would you like to do?
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Transformation** (translation and symbol conversion)
</edukamu-table-cell>
<edukamu-table-cell>
English: Hello<br>
French:
</edukamu-table-cell>
<edukamu-table-cell>
bonjour
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Summarizing content**
</edukamu-table-cell>
<edukamu-table-cell>
Provide a summary of the content
{text}
</edukamu-table-cell>
<edukamu-table-cell>
The content shares methods of machine learning.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Picking up where you left off**
</edukamu-table-cell>
<edukamu-table-cell>
One way to grow tomatoes
</edukamu-table-cell>
<edukamu-table-cell>
is to plant seeds.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
**Giving factual responses**
</edukamu-table-cell>
<edukamu-table-cell>
How many moons does Earth have?
</edukamu-table-cell>
<edukamu-table-cell>
One
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

Several factors affect the quality of completions you'll get from a generative AI solution.

- The way a prompt is engineered. Learn more about prompt engineering here.
- The model parameters (covered next).
- The data the model is trained on, which can be adapted through model fine-tuning with customization.

You have more control over the completions returned by training a custom model than through prompt engineering and parameter adjustment.

There are three basic guidelines for creating useful prompts:

- **Show and tell**. Make it clear what you want either through instructions, examples, or a combination of the two. If you want the model to rank a list of items in alphabetical order or to classify a paragraph by sentiment, include these details in your prompt to show the model.
- **Provide quality data**. If you're trying to build a classifier or get the model to follow a pattern, make sure there are enough examples. Be sure to proofread your examples. The model is smart enough to resolve basic spelling mistakes and give you a meaningful response. Conversely, the model might assume the mistakes are intentional, which can affect the response.
- **Check your settings**. Probability settings, such as Temperature and Top P, control how deterministic the model is in generating a response. If you're asking for a response where there's only one right answer, you should specify lower values for these settings. If you're looking for a response that's not obvious, you might want to use higher values. The most common mistake users make with these settings is assuming they control "cleverness" or "creativity" in the model response.

We’ll find out more about creating prompts on the next page.


### Making Calls

You can start making calls to a deployed model via the REST API, Python, C#, or from the Studio. If your deployed model has a GPT-3.5 or GPT-4 model base, you need to use the Chat completions documentation, which has different request endpoints and variables required than for other base models.

</edukamu-collapse>
<br>

Azure OpenAI Service includes AI models that have already been crafted, created, and optimized for you. You can also try out the models before using them in order to find out what works for you and your application. You can enjoy trying out everything you like –as if you were having fun on a playground.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure OpenAI Studio Playgrounds
</edukamu-collapse-hidden-title>

Playgrounds are useful interfaces in Azure OpenAI Studio that you can use to experiment with your deployed models without needing to develop your own client application. Azure OpenAI Studio offers multiple playgrounds with different parameter tuning options.


### Completions Playground

The Completions playground allows you to make calls to your deployed models through a text-in, text-out interface and to adjust parameters. You need to select the deployment name of your model under Deployments. Optionally, you can use the provided examples to get you started, and then you can enter your own prompts.

<edukamu-image url="/graphics/module4/azure-openai-completions-playground.png" alt="Screenshot of the Azure OpenAI Studio portal's completions playground." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>


### Completions Playground Parameters

There are many parameters that you can adjust to change the performance of your model:

- **Temperature**: Controls randomness. Lowering the temperature means that the model produces more repetitive and deterministic responses. Increasing the temperature results in more unexpected or creative responses. Try adjusting temperature or Top P but not both.
- **Max length (tokens)**: Set a limit on the number of tokens per model response. The API supports a maximum of 4000 tokens shared between the prompt (including system message, examples, message history, and user query) and the model's response. One token is roughly four characters for typical English text.
- **Stop sequences**: Make responses stop at a desired point, such as the end of a sentence or list. Specify up to four sequences where the model will stop generating further tokens in a response. The returned text won't contain the stop sequence.
- **Top probabilities (Top P)**: Similar to temperature, this controls randomness but uses a different method. Lowering Top P narrows the model’s token selection to likelier tokens. Increasing Top P lets the model choose from tokens with both high and low likelihood. Try adjusting temperature or Top P but not both.
- **Frequency penalty**: Reduce the chance of repeating a token proportionally based on how often it has appeared in the text so far. This decreases the likelihood of repeating the exact same text in a response.
- **Presence penalty**: Reduce the chance of repeating any token that has appeared in the text at all so far. This increases the likelihood of introducing new topics in a response.
- **Pre-response text**: Insert text after the user’s input and before the model’s response. This can help prepare the model for a response.
- **Post-response text**: Insert text after the model’s generated response to encourage further user input, as when modeling a conversation.


### Chat Playground

The Chat playground is based on a conversation-in, message-out interface. You can initialize the session with a system message to set up the chat context.

In the Chat playground, you're able to add *few-shot examples*. The term few-shot refers to providing a few of examples to help the model learn what it needs to do. You can think of it in contrast to zero-shot, which refers to providing no examples.

In the *Assistant setup*, you can provide few-shot examples of what the user input may be, and what the assistant response should be. The assistant tries to mimic the responses you include here in tone, rules, and format you've defined in your system message.

<edukamu-image url="/graphics/module4/azure-openai-chat-playground.png" alt="Screenshot of the Azure OpenAI Studio portal's Chat playground." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>


### Chat Playground Parameters

The Chat playground, like the Completions playground, also includes the Temperature parameter. The Chat playground also supports other parameters not available in the Completions playground. These include:

- **Max response**: Set a limit on the number of tokens per model response. The API supports a maximum of 4000 tokens shared between the prompt (including system message, examples, message history, and user query) and the model's response. One token is roughly four characters for typical English text.
- **Top P**: Similar to temperature, this controls randomness but uses a different method. Lowering Top P narrows the model’s token selection to likelier tokens. Increasing Top P lets the model choose from tokens with both high and low likelihood. Try adjusting temperature or Top P but not both.
- **Past messages included**: Select the number of past messages to include in each new API request. Including past messages helps give the model context for new user queries. Setting this number to 10 will include five user queries and five system responses.

The **Current token count** is viewable from the Chat playground. Since the API calls are priced by token and it's possible to set a max response token limit, you'll want to keep an eye out for the current token count to make sure the conversation-in doesn't exceed the max response token count.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-orange">
AzureOpenAI Service is the go-to solution for employing generative AI and integrating it with your applications. On this page, we’ve explored its basic functions and use cases, and during this unit, we’ll keep on digging deeper.

Before continuing, let’s consolidate our knowledge with an exercise.
</edukamu-section>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Setting Up Azure OpenAI Service
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practice exercise, we’ll start using Azure OpenAI Service in a lab environment. We’ll build on the knowledge gained here on the following pages, so make sure to take your time here if you have access to Microsoft Azure!

We’ll deploy Azure OpenAI base models and test them in the Completions and Chat playgrounds. You'll get a chance to explore the effects of prompts and parameters on text and code completions.

(Microsoft provides this lab experience and related content for educational purposes. All presented information is owned by Microsoft and intended solely for learning about the covered products and services.)

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/get-started-openai/8-exercise" target="_blank">Microsoft Learn: Lab Environment</edukamu-button>
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

</edukamu-collapse> -->

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Azure OpenAI Service Basics
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module4/getting-started-with-azure-openai-question-scroll-1.yaml" id="uaa3b70w72dzbzb8">
<br>

</edukamu-collapse>
<br>

How are you feeling at this stage? Are you already excited about the possibilities offered by Microsoft and OpenAI? In that case, feel free to explore forward!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1.png" alt="Edukamu-progress-in-a-module-image">
