## AI and Copilots

The availability of LLMs has led to the emergence of a new software application, often referred to as a copilot. Copilots are often integrated into other applications and provide a way for users to get help with common tasks from a generative AI model. Copilots are based on a common architecture, so developers can build custom copilots for various business-specific applications and services.

In short, copilots are like your personal assistants – except that they never get tired and are available around the clock.

Microsoft sees copilots as a fundamental part of the future working life, and they’re already used throughout its services.

Let’s take a look at what copilots are and why they’re a game changer. Afterwards, we’ll focus a while on some practical tips and tricks for using generative AI.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Copilots
</edukamu-collapse-hidden-title>

You may see copilots appear within the products that you already use, for example, as a chat screen feature that opens up next to your file. These copilots use the content that is created or searched for in the product as specific information for its results.

It's helpful to think of how the creation of a large language model is related to the process of creating a copilot application:
1. A large amount of data is used to train a large language model.
2. Services such as Azure OpenAI Service make pretrained models available. Developers can use these pretrained models as they are, or fine-tune them with custom data.
3. Deploying a model makes it available for use in applications.
4. Developers can build copilots that submit prompts to models and generate content for use in applications.
5. Business users can use copilots to boost their productivity and creativity with AI-generated content.

### Examples of Copilots

Microsoft has already added copilots to commonly used applications.

In the Microsoft Edge browser, a copilot enables you to summarize the page you’re currently browsing or to generate new content.

<edukamu-image url="/graphics/module4/edge-copilot.png" alt="Screenshot of Microsoft Artificial Intelligence Solutions page."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The Microsoft Bing search engine provides a copilot to help when browsing or searching the Internet by generating natural language answers to questions based on context rather than just search results of indexed pages.

<edukamu-image url="/graphics/module4/bing-copilot.png" alt="Screenshot of chat with AI and prompt “Create a cover letter for a job application for a candidate with a masters degree in political science.”"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Both these services are built into Microsoft 365 Copilot, which works alongside you in productivity and communication apps such as PowerPoint and Outlook, assisting you in creating effective documents, spreadsheets, presentations, emails, and other ways.

<edukamu-image url="/graphics/module4/microsoft-365-dall-e.gif" alt="Animation introduces the basic functions of Microsoft 365 Copilot." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Microsoft 365 Copilot is available within the Windows 11 operating system. There’s also a separate website for accessing the service.

Another tool, the GitHub copilot provides support to software developers, helping them write, document, and test code.

<edukamu-image url="/graphics/module4/github-copilot.gif" alt="Animation of GitHub copilot."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

All these copilots help you complete daily tasks and become more effective at whatever it is you’re doing on your computer – and Microsoft Azure.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Copilots have the potential to revolutionize the way we work. These handy assistants use generative AI to help with first drafts, information synthesis, strategic planning, and much more.

Generative AI models are used by writing *prompts*. Prompts are like commands and instructions combined: when writing one, it’s important to meticulously detail what you want the model to do. These models are incredibly capable, but they still need detailed instructions.

Have a look at the following tips on improving your prompts and, consequently, get better results when using generative AI.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Prompt Engineering
</edukamu-collapse-hidden-title>

The quality of responses that a generative AI application returns not only depends on the model itself, but on the types of prompts it's given. The term prompt engineering describes the process of prompt improvement. Both developers who design applications and consumers who use those applications can improve the quality of responses from generative AI by considering prompt engineering.

Prompts are ways we tell an application what we want it to do. An engineer can add instructions for the program with prompts. For example, developers may build a generative AI application for teachers to create multiple-choice questions related to text students read. During the development of the application, developers can add other rules for what the program should do with the prompts it receives.

### System Messages

Prompt engineering techniques include defining a system message. The message sets the context for the model by describing expectations and constraints, for example, "You're a helpful assistant that responds in a cheerful, friendly manner". These system messages determine constraints and styles for the model's responses.

### Writing Good Prompts

You can get the most useful completions by being explicit about the kind of response you want, for example, “Create a list of 10 things to do in Edinburgh during August”. You can achieve better results when you submit clear, specific prompts.

### Providing Examples

LLMs generally support *zero-shot learning* in which responses can be generated without prior examples. However, you can also provide *one-shot* learning prompts that include one, or a few, examples of the output you require such as, “Visit the castle in the morning before the crowds arrive”. The model can then generate further responses in the same style as the examples provided in the prompt.

### Grounding Data

Prompts can include grounding data to provide context. You can use grounding data as a prompt engineering technique to gain many of the benefits of fine-tuning without having to train a custom model.

To apply this technique, include contextual data in the prompt so that the model can use it to generate an appropriate output. For example, suppose you want to use an LLM to generate a summary of an email. You can include the email text in the prompt with an instruction to summarize it.

</edukamu-collapse>
<br>


Remember that services like Microsoft 365 Copilot are free to use for everyone. This means that you can start practicing your prompting skills right away!

Keep the prompt engineering tips in mind as you try and complete the following practice exercise.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Exploring Generative AI
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

In this practice exercise, you’ll get to try prompting with generative AI built into Microsoft’s Bing search engine.

Follow the instructions below.

1. Open [Bing.com](https://www.bing.com/)(target="_blank") and sign in with your personal Microsoft account.

**Note**: While you can sign in with your work or school account, you will see a slightly different user experience compared to signing in with your personal account. Using your work or school account, you will see Bing Enterprise chat.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold">Chat</span> from the menu at the top of the screen. Chat brings you to Bing Copilot, which uses generative AI to power search results. What this means is that unlike search alone, which returns existing content, Bing Copilot can put together new responses based on natural language modeling and the web’s information.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Towards the bottom of the screen, you will see a window <span style="font-weight: bold">Ask me anything</span>. As you enter prompts into the window, Bing Copilot uses the entire conversation thread to return responses. For example, let’s try asking a series of questions about traveling.
</li>
</ol>
</edukamu-section>

### Phase 1: Working with Text

1. Type in a prompt: *What are 3 pros and cons of traveling in the winter?*.

You will see a *Searching for:…* and *Generating…* appear before the response. The model uses the searched for responses as grounding information to generate original responses. Notice that the end of the response contains links to its sources.

<edukamu-image url="/graphics/module4/bing-copilot-response-traveling.png" alt="A screenshot of Copilot's response to a traveling prompt with three bullets for pros and three bullets for cons." style="max-width: 80%;"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

**Note**: If you do not see a *Generating… message or a bullet list response, you have not gotten to see Bing Copilot in action yet. You need to return to the sign-in menu and connect the current account you are using with a personal account.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Type in a prompt: <span style="font-style: italic">Find me 3 more pros</span>.
</li>
</ol>
</edukamu-section>

What you mean with this prompt is that you would like to see 3 more positive reasons for traveling in the winter that have not already been listed. Notice that with this prompt, you are asking Bing Copilot to do two things that search alone does not do: use the previous chat response to exclude what’s returned in the new response, and use the previous chat’s topic without explicitly stating it.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Type in a prompt: <span style="font-style: italic">Where are 3 places I can go to find fewer crowds?</span>
</li>
</ol>
</edukamu-section>

**Note**: Notice that while Bing Copilot is able to give a related response, it can drop earlier “memories” of the conversation thread as it continues. As a result, the responses you get may not be directly related to traveling in the winter. This is largely to do with token input limitations. When chat “remembers” earlier parts of a conversation, it is because it has saved a certain amount of tokens from the conversation. As new tokens are introduced via your new prompts and responses, chat will let go of older tokens.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
The <span style="font-weight: bold">New Topic</span> button next to the chat window is useful Bing Copilot to clear the previous conversation thread so your new topic responses are not based on the previous topic. Use the <span style="font-weight: bold">New Topic</span> icon next to the chat window to clear your message history.
</li>
</ol>
</edukamu-section>

### Phase 2: Image Generation

1. Now let’s see an example of image generation. Type in a prompt: *Create an image of an elephant eating a hamburger.*

Notice that a message *I’ll try to create that…* appears before Bing Copilot returns a response.

<edukamu-image url="/graphics/module4/dall-e-elephant.png" alt="A screenshot of elephants eating hamburgers." style="max-width: 80%;"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Importantly, notice that the response may look similar but not the same. This is because responses are varied. Generative AI will always come up with something different, even when using the exact same prompt more than once.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the response, there is text at the bottom that reads “Powered by DALL-E”. Consider how DALL-E is based on large language models as your natural language input generates images.
</li>
</ol>
</edukamu-section>
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Return to Bing Copilot’s chat by clicking on the Microsoft Bing icon on the top right corner of the screen.
</li>
</ol>
</edukamu-section>


### Phase 3: Code Generation

Now’s let’s see an example of code generation and translation. Type in a prompt: *Use Python to create a list.*

1. Type in the prompt: *Translate that into C#.* Notice how you did not need to specify what “that” is as Bing Copilot knows to refer to the conversation history.


### Phase 4: Bonus Task
1.	Type in a prompt: What are 3 examples of generative AI helping people?. You can use this as a way to brainstorm your own copilot ideas!

</edukamu-collapse>
<br>


How was it? Generative AI is quite powerful, and it’s becoming more and more capable as we speak.

Here’s another exercise for you to complete before moving on. Take a while to recap before completing it.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Azure and Generative AI
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module4/ai-and-copilots-text-poll.yaml" id="ev6b06g1ta2v4ly5"/>
<br>
<edukamu-text-poll url="/exercises/module4/ai-and-copilots-text-poll-2.yaml" id="17vhfb48dxv7097q"/>
<br>
<edukamu-text-poll url="/exercises/module4/ai-and-copilots-text-poll-3.yaml" id="236j7vaz5x40mxk9"/>
<br>
<edukamu-text-poll url="/exercises/module4/ai-and-copilots-text-poll-4.yaml" id="38cc72wn19xz1dfh"/>
<br>
<edukamu-text-poll url="/exercises/module4/ai-and-copilots-text-poll-5.yaml" id="sd02dul6440g893j"/>
<br>
<edukamu-text-poll url="/exercises/module4/ai-and-copilots-text-poll-6.yaml" id="199411202190803q"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/4/ai-and-copilots?question=ev6b06g1ta2v4ly5">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


Generative AI has the potential to revolutionize the way we live and work. Microsoft Azure is the most comprehensive platform for developing brand new AI experiences for all kinds of purposes – but that’s not enough.

When working with generative AI, we’re in many ways dealing with something unknown. That’s why responsibility and ethics are always a key element. They’re also our next topic.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
