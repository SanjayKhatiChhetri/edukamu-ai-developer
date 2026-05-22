## Question Answering

In the modern society, we’re used to being able to communicate at any time of the day or night, anywhere in the world, putting organizations under pressure to react fast enough to their customers.

We want personal responses to our queries, without having to read in-depth documentation to find answers. This often means that support staff get overloaded with requests for help through multiple channels – and that people are still left waiting for a response.

*Conversational AI* describes solutions that enable dialogues between AI agents and people. Generically, conversational AI agents are known as *bots*. People can engage with bots through channels such as web chat interfaces, email, social media platforms, and more.

Azure AI Language's question answering feature provides you with the ability to create conversational AI solutions.

On this page, we’ll focus on question answering.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Question Answering
</edukamu-collapse-hidden-title>

**Question answering** supports natural language AI workloads that require an automated conversational element. Typically, question answering is used to build bot applications that respond to customer queries.

Question answering capabilities can respond immediately, answer concerns accurately, and interact with users in a natural multi-turned way. Bots can be implemented on a range of platforms, such as a web site or a social media platform.

Question answering applications provide a friendly way for people to get answers to their questions and allows people to deal with queries at a time that suits them, rather than during office hours.

In the following example, a chat bot uses natural language and provides options to a customer to best handle their query. The user gets an answer to their question quickly, and only gets passed to a person if their query is more complicated.

<edukamu-image url="/graphics/module3/bot.png" alt="Screenshot of a chat interface showing user input and responses from a bot."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

</edukamu-collapse>
<br>


That’s question answering in a nutshell – a basic capability of every modern AI bot. By leveraging these concepts, Azure developers can design bots that help customers get the help they need when they need it.

Before checking out Azure’s question answering services in a bit more detail, let’s review a few prominent use cases.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Use Cases of Question Answering
</edukamu-collapse-hidden-title>

### 1. Chatbots for Customer Support

**Example**: A customer asks a chatbot, "How can I return a product?" The chatbot interprets the question, understands the context, and provides step-by-step instructions on the return process.

### 2. Virtual Assistants

**Example**: A user asks a virtual assistant, "What's the weather forecast for tomorrow in Taivalkoski, Finland?" The virtual assistant uses question answering to extract the relevant information from a weather database and responds with the forecast.

### 3. Educational Chatbots

**Example**: A student on an educational chatbot platform asks, "Explain the concept of photosynthesis." The chatbot processes the query, retrieves information from educational resources, and provides a concise explanation.

### 4. Information Retrieval Bots

**Example**: A user queries a news bot, "What are the latest developments in renewable energy?" The bot uses question answering techniques to fetch recent news articles and presents a summary of the relevant information.

### 5. Search Engine Conversational Interfaces

**Example**: A user interacts with a search engine chat interface, asking, "Who is the president of Finland?" The chatbot retrieves real-time data from the web and responds with the current president of Finland.

In short, question answering enhances user interactions by allowing users to seek information or perform tasks through natural language queries, making the interaction more intuitive and user-friendly.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
The previous examples are just fraction of all the possibilities made possible by question answering bots and other related technologies. The coolest thing about the list might be that all the examples are reality right now – there’s no need to wait!

All right, let’s review the Azure services related to question answering: 1) Azure AI Language and 2) Azure AI Bot Service.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Azure AI Language
</edukamu-collapse-hidden-title>

As you already know, Azure AI Language includes a custom question answering feature that enables you to create a knowledge base of question-and-answer pairs that can be queried using natural language input.

You can use Azure AI Language Studio to create, train, publish, and manage question answering projects.

(To create a project, you must first provision a **Language** resource in your Azure subscription.)

### Define Questions and Answers

After provisioning a language resource, you can use the Language Studio's custom question answering feature to create a project that consists of question-and-answer pairs. These questions and answers can be:
* Generated from an existing FAQ document or web page.
* Entered and edited manually.

In many cases, a project is created using a combination of all of these techniques; starting with a base dataset of questions and answers from an existing FAQ document and extending the knowledge base with additional manual entries.

Questions in the project can be assigned *alternative phrasing* to help consolidate questions with the same meaning. For example, you might include a question like:

> What is your head office location?

You can anticipate different ways this question could be asked by adding an alternative phrasing such as:

> Where is your head office located?

After creating a set of question-and-answer pairs, you must save it. This process analyzes your literal questions and answers and applies a built-in natural language processing model to match appropriate answers to questions, even when they are not phrased exactly as specified in your question definitions. Then you can use the built-in test interface in the Language Studio to test your knowledge base by submitting questions and reviewing the answers that are returned.

Azure AI Language is fitted with a user-interface that’s logical and simple to comprehend. This means that the service sounds a lot more complicated to use than it actually is.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Azure AI Bot
</edukamu-collapse-hidden-title>

After you've created and deployed a knowledge base, you can deliver it to users through a bot. You can create a custom bot by using the Microsoft Bot Framework SDK to write code that controls conversation flow and integrates with your knowledge base. However, an easier approach is to use the automatic bot creation functionality, which enables you to create a bot for your deployed knowledge base and publish it as an Azure AI Bot Service application with just a few clicks

### Connecting Channels

When your bot is ready to be delivered to users, you can connect it to multiple channels; making it possible for users to interact with it through web chat, email, Microsoft Teams, and other common communication media.

<edukamu-image url="/graphics/module3/bot-solution.png" alt="Diagram visualize the connections of the conversation."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

Users can submit questions to the bot through any of its channels, and receive an appropriate answer from the knowledge base on which the bot is based.

</edukamu-collapse>
<br>


If you have an active Azure subscription, make sure to check out Azure AI Language and Azure AI Bot whenever you have the time! Trying out the things covered on these courses will really boost the learning process.

Speaking of learning, recap for a while and move on to the next exercise.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Question Answering
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/question-answering-question-scroll.yaml" id="85n3ulq09rs9977m">
<br>

</edukamu-collapse>
<br>


Azure AI Language's custom question answering feature enables you to define and publish a knowledge base of questions and answers with support for natural language querying. When combined with Azure AI Bot Service, you can use such a base to deliver a bot that responds intelligently to user questions over multiple communication channels.

The ability to create conversational AI solutions with these services makes it possible for AI agents to reduce the support workload for human personnel; enabling organizations to provide user support at global scale.

We’ve now reviewed how NLP models can be used to recognize words and languages or even answer questions. The next logical step is to strike up a conversation.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
