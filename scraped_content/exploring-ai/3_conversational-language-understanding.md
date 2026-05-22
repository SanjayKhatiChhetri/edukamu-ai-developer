## Conversational Language Understanding

Understanding words and questions is a challenge for every machine or AI, which in turn means that keeping a conversation going is even more demanding.

Conversational Language Understanding, in the context of Microsoft Azure and AI, refers to the ability of machines to comprehend and respond to natural language in a way that mimics human conversation. This involves the application of advanced natural language processing (NLP) and machine learning techniques to interpret user queries, extract meaningful information, and generate contextually relevant responses.

Real-life examples of conversational language understanding include interactive search engines or assistants, like Microsoft’s Copilot. Services like it leverage conversational language understanding to process and react to commands given by you, the end user.

Let’s find out about the core principles behind conversational language understanding, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Conversational Language Understanding
</edukamu-collapse-hidden-title>

In 1950, the British mathematician Alan Turing devised the *Imitation Game*, which has become known as the *Turing Test* and hypothesizes that if a dialog is natural enough, you might not know whether you're conversing with a human or a computer.

As artificial intelligence (AI) grows ever more sophisticated, this kind of conversational interaction with applications and digital assistants is becoming more and more common, and in specific scenarios can result in human-like interactions with AI agents. Common scenarios for this kind of solution include customer support applications, reservation systems, and home automation among others.

To realize the aspiration of the imitation game, computers need not only to be able to accept language as input (either in text or audio format), but also to be able to interpret the semantic meaning of the input - in other words, *understand* what is being said.

Microsoft Azure supports conversational language understanding through **Azure AI Language** service. One example using conversational language understanding is an application that's able to turn devices on and off based on speech. Many types of tasks involving command and control, end-to-end conversation, and enterprise support can be completed with Azure AI Language's conversational language understanding feature.

</edukamu-collapse>
<br>


Microsoft Azure supports conversational language understanding through Azure AI Language service with which we’re already familiar.

In order to really start working with conversational language understanding, an Azure developer needs to consider three key aspects: utterances, entities, and intents. Let’s find out more.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Utterances, Entities, and Intents
</edukamu-collapse-hidden-title>

### Utterances

An utterance is an example of something a user might say, and which your application must interpret. For example, when using a home automation system, a user might use the following utterances:

>"Switch the fan on."<br>
>"Turn on the light."


### Entities

An entity is an item to which an utterance refers. For example, fan and light in the following utterances:

>"Switch the **fan** on."<br>
>"Turn on the **light**."

You can think of the **fan** and **light** entities as being specific instances of a general **device** entity.


### Intents

An intent represents the purpose, or goal, expressed in a user's utterance. For example, for both of the previously considered utterances, the intent is to turn a device on; so in your conversational language understanding application, you might define a **TurnOn** intent that is related to these utterances.

A conversational language understanding application defines a model consisting of intents and entities. Utterances are used to train the model to identify the most likely intent and the entities to which it should be applied based on a given input. The home assistant application we've been considering might include multiple intents, like the following examples:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="33,33%">
Intent
</edukamu-table-header>
<edukamu-table-header width="33,33%">
Related Utterances 
</edukamu-table-header>
<edukamu-table-header width="33,33%">
Entities
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Greeting
</edukamu-table-cell>
<edukamu-table-cell >
"Hello"<br>
"Hi"<br>
"Hey"<br>
"Good morning"
</edukamu-table-cell>
<edukamu-table-cell>
<!-- - -->
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
TurnOn
</edukamu-table-cell>
<edukamu-table-cell >
"Switch the fan on"<br>
"Turn the light on"<br>
"Turn on the light"<br>
</edukamu-table-cell>
<edukamu-table-cell>
fan (device)<br>
light (device)<br>
light (device)<br>
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
TurnOff
</edukamu-table-cell>
<edukamu-table-cell >
"Switch the fan off"<br>
"Turn the light off"<br>
"Turn off the light"<br>
</edukamu-table-cell>
<edukamu-table-cell>
fan (device)<br>
light (device)<br>
light (device)<br>
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
CheckWeather
</edukamu-table-cell>
<edukamu-table-cell >
"What is the weather for today?"
"Give me the weather forecast"
"What is the forecast for Paris?"
"What will the weather be like in Seattle tomorrow?"
</edukamu-table-cell>
<edukamu-table-cell>
today (datetime)<br>
<br>
Paris (location)<br>
Seattle (location), tomorrow (datetime)
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
None
</edukamu-table-cell>
<edukamu-table-cell >
"What is the meaning of life?"<br>
"Is this thing on?"
</edukamu-table-cell>
<edukamu-table-cell>
<!-- - -->
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

In the table there are numerous utterances used for each of the intents. The intent should be a concise way of grouping the utterance tasks. Of special interest is the **None** intent. You should consider always using the *None* intent to help handle utterances that do not map any of the utterances you have entered. The *None* intent is considered a fallback, and is typically used to provide a generic response to users when their requests don't match any other intent.

After defining the entities and intents with sample utterances in your conversational language understanding application, you can train a language model to predict intents and entities from user input - even if it doesn't match the sample utterances exactly. You can then use the model from a client application to retrieve predictions and respond appropriately.

</edukamu-collapse>
<br>

Imagine yourself talking with another person. To keep a conversation going, you’ll need to understand each other (which is not necessarily tied to linguistic abilities, but this is an entirely different question) in order to turn words and phrases into logical concepts, right?

The same principles largely apply to language models. To put it shortly, each NLP model aimed at conversational language understanding needs to be able to

1. understand what the end user says (utterances).
2. form a bridge between the utterance and the thing that us being referred (entities).
3. recognize the intent of the user (intents).

Microsoft Azure includes a host of tools and services aimed at improving conversational language understanding.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure and Conversational Language Understanding
</edukamu-collapse-hidden-title>

Azure AI Language's conversational language understanding feature enables you to author a language model and use it for predictions. Authoring a model involves defining entities, intents, and utterances. Generating predictions involves publishing a model so that client applications can take user input and return responses.

To use conversational language capabilities in Azure, you need a resource in your Azure subscription. This is also common to you.

You can use the following types of resource:
* **Azure AI Language**: A resource that enables you to build apps with industry-leading natural language understanding capabilities without machine learning expertise. You can use a language resource for *authoring* and *prediction*.
* **Azure AI services**: A general resource that includes conversational language understanding along with many other Azure AI services. You can only use this type of resource for *prediction*.

The separation of resources is useful when you want to track resource utilization for Azure AI Language use separately from client applications using all Azure AI services applications.

### Authoring

After you've created an authoring resource, you can use it to train a conversational language understanding model. To train a model, start by defining the entities and intents that your application will predict as well as utterances for each intent that can be used to train the predictive model.

Conversational language understanding provides a comprehensive collection of prebuilt domains that include pre-defined intents and entities for common scenarios; which you can use as a starting point for your model. You can also create your own entities and intents.

When you create entities and intents, you can do so in any order. You can create an intent, and select words in the sample utterances you define for it to create entities for them; or you can create the entities ahead of time and then map them to words in utterances as you're creating the intents.

You can write code to define the elements of your model, but in most cases it's easiest to author your model using the Language studio - a web-based interface for creating and managing Conversational Language Understanding applications.

### Training

After you have defined the intents and entities in your model, and included a suitable set of sample utterances; the next step is to train the model. Training is the process of using your sample utterances to teach your model to match natural language expressions that a user might say to probable intents and entities.

After training the model, you can test it by submitting text and reviewing the predicted intents. Training and testing is an iterative process. After you train your model, you test it with sample utterances to see if the intents and entities are recognized correctly. If they're not, make updates, retrain, and test again.

### Predicting

When you are satisfied with the results from the training and testing, you can publish your Conversational Language Understanding application to a prediction resource for consumption.

Client applications can use the model by connecting to the endpoint for the prediction resource, specifying the appropriate authentication key; and submit user input to get predicted intents and entities. The predictions are returned to the client application, which can then take appropriate action based on the predicted intent.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
By exploring conversational language understanding in Microsoft Azure, developers gain the tools to build intelligent applications that can comprehend, interpret, and respond to user queries in a manner that mirrors human conversation.

After this initial look, you’ll be more prepared to face the challenges awaiting you within this micro degree.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Conversational Language Understanding
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/conversational-language-question-scroll.yaml" id="b2d5t13kt7ro7lh2">
<br>

</edukamu-collapse>
<br>


We’ve now explored natural language processing, or NLP for short, from various perspectives ranging from simple words to keeping up conversations. We’ll wrap up this unit with a special Azure service that you’ll undoubtedly find useful: Azure AI Speech.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
