## Capabilities of CLU

Conversational language understanding can greatly enhance user experience and empower our chatbots in ways that seemed unimaginable just a few years ago.

Without further ado, let’s keep on exploring this interesting technology – without forgetting Microsoft Azure’s capabilities for leveraging it!

We’ll begin with intents, utterances, and entities. Do you still remember the trio?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Defining Intents, Utterances, and Entities
</edukamu-collapse-hidden-title>

*Utterances* are the phrases that a user might enter when interacting with an application that uses your language model. An *intent* represents a task or action the user wants to perform, or more simply the *meaning* of an utterance. You create a model by defining intents and associating them with one or more utterances.

For example, consider the following list of intents and associated utterances:

- **GetTime**:
    - "What time is it?"
    - "What is the time?"
    - "Tell me the time."
- **GetWeather**:
    - "What is the weather forecast?"
    - "Do I need an umbrella?"
    - "Will it snow?"
- **TurnOnDevice**
    - "Turn the light on."
    - "Switch on the light."
    - "Turn on the fan."
- **None**:
    - "Hello"
    - "Goodbye"

In your model, you must define the intents that you want your model to understand, so spend some time considering the *domain* your model must support and the kinds of actions or information that users might request. In addition to the intents that you define, every model includes a **None** intent that you should use to explicitly identify utterances that a user might submit, but for which there is no specific action required (for example, conversational greetings like "hello") or that fall outside of the scope of the domain for this model.

After you've identified the intents your model must support, it's important to capture various different example utterances for each intent. Collect utterances that you think users will enter; including utterances meaning the same thing but that are constructed in different ways. Keep these guidelines in mind:

- Capture multiple different examples, or alternative ways of saying the same thing
- Vary the length of the utterances from short, to medium, to long
- Vary the location of the *noun* or *subject* of the utterance. Place it at the beginning, the end, or somewhere in between
- Use correct grammar and incorrect grammar in different utterances to offer good training data examples
- The precision, consistency and completeness of your labeled data are key factors to determining model performance.
  - Label **precisely**: Label each entity to its right type always. Only include what you want extracted, avoid unnecessary data in your labels.
  - Label **consistently**: The same entity should have the same label across all the utterances.
  - Label **completely**: Label all the instances of the entity in all your utterances.

*Entities* are used to add specific context to intents. For example, you might define a **TurnOnDevice** intent that can be applied to multiple devices, and use entities to define the different devices.

Consider the following utterances, intents, and entities:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Utterance**
</edukamu-table-header>
<edukamu-table-header>
**Intent**
</edukamu-table-header>
<edukamu-table-header>
**Entities**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
What is the time?
</edukamu-table-cell>
<edukamu-table-cell>
GetTime
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
What time is it in London?
</edukamu-table-cell>
<edukamu-table-cell>
GetTime
</edukamu-table-cell>
<edukamu-table-cell>
Location (London)
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
What's the weather forecast for Paris?
</edukamu-table-cell>
<edukamu-table-cell>
GetWeather
</edukamu-table-cell>
<edukamu-table-cell>
Location (Paris)
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Will I need an umbrella tonight?
</edukamu-table-cell>
<edukamu-table-cell>
GetWeather
</edukamu-table-cell>
<edukamu-table-cell>
Time (tonight)
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
What's the forecast for Seattle tomorrow?
</edukamu-table-cell>
<edukamu-table-cell>
GetWeather
</edukamu-table-cell>
<edukamu-table-cell>
Location (Seattle), Time (tomorrow)
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Turn the light on.
</edukamu-table-cell>
<edukamu-table-cell>
TurnOnDevice
</edukamu-table-cell>
<edukamu-table-cell>
Device (light)
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Switch on the fan.
</edukamu-table-cell>
<edukamu-table-cell>
TurnOnDevice
</edukamu-table-cell>
<edukamu-table-cell>
Device (fan)
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

You can split entities into a few different component types:

- **Learned** entities are the most flexible kind of entity, and should be used in most cases. You define a learned component with a suitable name, and then associate words or phrases with it in training utterances. When you train your model, it learns to match the appropriate elements in the utterances with the entity.
- **List** entities are useful when you need an entity with a specific set of possible values - for example, days of the week. You can include synonyms in a list entity definition, so you could define a **DayOfWeek** entity that includes the values "Sunday", "Monday", "Tuesday", and so on; each with synonyms like "Sun", "Mon", "Tue", and so on.
- **Prebuilt** entities are useful for common types such as numbers, datetimes, and names. For example, when prebuilt components are added, you will automatically detect values such as "6" or organizations such as "Microsoft".

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Differentiating Utterances with Patterns
</edukamu-collapse-hidden-title>

In some cases, a model might contain multiple intents for which utterances are likely to be similar. You can use the pattern of utterances to disambiguate the intents while minimizing the number of sample utterances.

For example, consider the following utterances:

- "Turn on the kitchen light"
- "Is the kitchen light on?"
- "Turn off the kitchen light"

These utterances are syntactically similar, with only a few differences in words or punctuation. However, they represent three different intents (which could be named **TurnOnDevice**, **GetDeviceStatus**, and **TurnOffDevice**). Additionally, the intents could apply to a wide range of entity values. In addition to "kitchen light", the intent could apply to "living room light", television", or any other device that the model might need to support.

To correctly train your model, provide a handful of examples of each intent that specify the different formats of utterances.

- **TurnOnDevice**:
    - "Turn on the {DeviceName}"
    - "Switch on the {DeviceName}"
    - "Turn the {DeviceName} on"
- **GetDeviceStatus**:
    - "Is the {DeviceName} on[?]"
- **TurnOffDevice**:
    - "Turn the {DeviceName} off"
    - "Switch off the {DeviceName}"
    - "Turn off the {DeviceName}"

When you teach your model with each different type of utterance, the Azure AI Language service can learn how to categorize intents correctly based off format and punctuation.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Using Prebuilt Entity Components
</edukamu-collapse-hidden-title>

You can create your own language models by defining all the intents and utterances it requires, but often you can use prebuilt components to detect common entities such as numbers, emails, URLs, or choices.

Using prebuilt components allows you to let the Azure AI Language service automatically detect the specified type of entity, and not have to train your model with examples of that entity.

To add a prebuilt component, you can create an entity in your project, then select **Add new prebuilt** to that entity to detect certain entities.

<edukamu-image url="/graphics/module2/add-prebuilt-entity.png" alt="Screenshot of adding a prebuilt entity component." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;" modal="true">
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br>

You can have up to five prebuilt components per entity. Using prebuilt model elements can significantly reduce the time it takes to develop a conversational language understanding solution.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-orange">
Intents, utterances, and entities are among the most basic aspects of conversational language understanding, so you’ll certainly get familiar with them when you start working with Microsoft Azure.

Next, we’ll briefly review the process of training, testing, deploying, and reviewing a CLU model. It’s largely a theoretical summary of the process we already reviewed in practice before.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Process: Setting Up a CLU Model 
</edukamu-collapse-hidden-title>

Creating a model is an iterative process with the following activities:

<edukamu-image url="/graphics/module2/train-test-publish-review.png" alt="Diagram that shows the train, test, publish, review cycle.">
<br>

1. Train a model to learn intents and entities from sample utterances.
2. Test the model interactively or using a testing dataset with known labels.
3. Deploy a trained model to a public endpoint so client apps can use it.
4. Review predictions and iterate on utterances to train your model.

By following this iterative approach, you can improve the language model over time based on user input, helping you develop solutions that reflect the way users indicate their intents using natural language.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Building a CLU Model with Azure AI Services
</edukamu-collapse-hidden-title>

**Reminder**: Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere. We highly recommend that you try out Microsoft Azure for yourself if you have the opportunity, but it is not mandatory.

In this practice exercise, we’ll build a conversational language understanding model with the Azure AI Language Services. Follow the instructions below carefully.

This exercise uses a virtual machine, provided by Microsoft, on Microsoft’s Learn platform. In order to set up the lab environment, please navigate to the Microsoft Learn platform.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/build-language-understanding-model/7-exercise?launch-lab=true" target="_blank">Microsoft Learn: Lab Environment</edukamu-button>
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


That’s conversational language understanding in a nutshell! Let’s review everything we’ve covered so far with an exercise.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Capabilities of CLU
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/capabilities-of-clu-question-scroll-1.yaml" id="dsqnsjn6vfbbu0fr">
<br>

</edukamu-collapse>
<br>

You’ve now completed two units – that’s half of the course! Well done!

In the next unit, we’ll shift our focus to an entirely new topic: retrieval augmented generation, or RAG for short. In order to understand it, we’ll need to use everything we’ve learned so far, so make sure to rest for a while before moving forward!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
