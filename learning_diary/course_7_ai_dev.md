# Course 7: Getting Started with AI Development

**URL:** [https://cs.edukamu.fi/ai-development](https://cs.edukamu.fi/ai-development)  
**Sections:** 15  

---

## Table of Contents

- **Unit 1:** Deploying Azure Ai Containers | Enabling Azure Ai Services | Getting Started With Azure Ai Language ...
- **Unit 2:** Building Natural Language Solutions | Capabilities Of Clu | Conversational Language Understanding
- **Unit 3:** Introduction To Building Natural Language Solutions | Rag Capabilities In Microsoft Azure | Retrieving Information With Azure Ai Search
- **Unit 4:** Fine Tuning Effective Prompts | Generating Code With Ai | Getting Started With Azure Openai ...

---

## Unit 1

### Deploying Azure Ai Containers

**TL;DR:** Microsoft Azure’s AI Services can be seamlessly integrated into all kinds of intelligent solutions and systems, but sometimes even that is not enough. Sometimes, we need even greater flexibility and control over our AI workloads, which is when we must take an entirely different approach – in other words, we need containers.

**Topics covered:**
- Getting Started with Azure AI Services Containers
- What are Containers?
- Container Deployment
- Using Azure AI Containers
- Azure AI Services Container Images
- Configuring Azure AI Services Containers
- Practice: Using Azure AI Services Containers
- Scenario: Shopping Assistant and Containers
- Objective: Create a Generative AI Shopping Assistant
- Model Answer: Advantages of Containerization

**Key Terms:**

| Term | Definition |
|------|-----------|
| Recap: Containers | Containerized development, unlike traditional methods, separates applications from specific hardware and software configurations. Containers encapsulate applications and... |
| Feature | </edukamu-table-header> |
| Image | </edukamu-table-header> |
| Feature | </edukamu-table-header> |
| Image | </edukamu-table-header> |
| Feature | </edukamu-table-header> |
| Image | </edukamu-table-header> |
| Feature | </edukamu-table-header> |
| Image | </edukamu-table-header> |
| Setting | </edukamu-table-header> |

**Key Points:**
- Containers are portable across hosts, which may be running different operating systems or use different hardware - making it easier to move an application and all its dependencies.
- A single container host can support multiple isolated containers, each with its own specific runtime configuration - making it easier to consolidate multiple applications that have different...
- An Azure Container Instance (ACI).
- An Azure Kubernetes Service (AKS) cluster.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Enabling Azure Ai Services

**TL;DR:** Azure AI Services are cloud-based services that are available whenever and wherever you need them. In order to use them, they need to be enabled.

**Topics covered:**
- Resources in Azure AI Services
- Provisioning Service Resources
- Options for Azure Resources
- Training and Prediction Resources
- Defining Endpoints and Keys
- APIs or SDKs?
- REST API
- SDK
- Using REST APIs
- Using SDKs

**Key Terms:**

| Term | Definition |
|------|-----------|
| Language | </edukamu-table-header> |
| Speech | </edukamu-table-header> |
| Vision | </edukamu-table-header> |
| Decision | </edukamu-table-header> |
| Azure AI Document Intelligence | An optical character recognition (OCR) solution that can extract semantic meaning from forms, such as invoices, receipts, and others. |
| Azure AI Immersive Reader | A reading solution that supports people of all ages and abilities. |
| Azure AI Search | A cloud-scale search solution that uses AI services to extract insights from data and documents. |
| Azure OpenAI | An Azure AI Service that provides access to the capabilities of OpenAI GPT-4. |
| AI services | resource that supports multiple different AI services. For example, you could create a single resource that enables you to use the **Azure AI Language**, **Azure AI Vision**,... |
| AI Language | and **AI Vision** resources in your Azure subscription. |

**Key Points:**
- Azure AI Document Intelligence - An optical character recognition (OCR) solution that can extract semantic meaning from forms, such as invoices, receipts, and others.
- Azure AI Immersive Reader - A reading solution that supports people of all ages and abilities.
- Azure AI Search - A cloud-scale search solution that uses AI services to extract insights from data and documents.
- Azure OpenAI - An Azure AI Service that provides access to the capabilities of OpenAI GPT-4.
- Create Azure AI services resources in an Azure subscription.
- Identify endpoints, keys, and locations required to consume an AI services resource.
- Use a REST API to consume an AI service.
- Use an SDK to consume an AI service.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Getting Started With Azure Ai Language

**TL;DR:** Do you still remember the term natural language processing, or NLP for short? This revolutionary technology essentially combines language understanding with the seemingly endless computing power offered by cloud services, and by now, you should already be familiar with the fundamentals after completing the first courses of this study program.

**Topics covered:**
- Introduction to Azure AI Language
- Provisioning Azure AI Language Resources
- Azure Resources for Text Analysis
- 1) Language Detection with Azure AI Language
- 2) Key-Phrase Extraction with Azure AI Language
- 3) Sentiment Analysis with Azure AI Language
- Extracting Entities
- Extracting Linked Entities
- Step-by-Step Guide for Activating a Free Azure Trial
- Practice: Using Azure AI Services

**Key Terms:**

| Term | Definition |
|------|-----------|
| Language detection | determining the language in which text is written. |
| Key phrase extraction | identifying important words and phrases in the text that indicate the main points. |
| Sentiment analysis | quantifying how positive or negative the text is. |
| Named entity recognition | detecting references to entities, including people, locations, time periods, organizations, and more. |
| Entity linking | identifying specific entities by providing reference links to Wikipedia articles. |
| Note: | The code examples in the subsequent sections show the JSON requests and responses exchanged with the REST interface. When using an SDK, the JSON requests are abstracted by... |
| text | to be analyzed. Optionally, you can provide a **countryHint** to improve prediction performance. |
| neutral | classification values between 0 and 1. |
| 10. | Type in the code and then click "Verify code". |
| 11. | Fill in the rest of the form. |

**Key Points:**
- Language detection - determining the language in which text is written.
- Key phrase extraction - identifying important words and phrases in the text that indicate the main points.
- Sentiment analysis - quantifying how positive or negative the text is.
- Named entity recognition - detecting references to entities, including people, locations, time periods, organizations, and more.
- Entity linking - identifying specific entities by providing reference links to Wikipedia articles.
- Evaluating a movie, book, or product by quantifying sentiment based on reviews.
- Prioritizing customer service responses to correspondence received through email or social media messaging.
- If all sentences are neutral, the overall sentiment is neutral.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Getting Started With Azure Ai Services

**TL;DR:** <edukamu-video content="/videos/devai-7-unit1-video.yaml"/>
<br>

**Topics covered:**
- Why Study Azure AI Services?
- Practical Use Scenarios:
- Preparing to Develop AI Solutions
- AI Terminology
- Data Science
- Machine Learning
- Artificial Intelligence
- Considering AI Integration and Responsibility
- Fairness
- Reliability and Safety

**Key Terms:**

| Term | Definition |
|------|-----------|
| 1. Ease of Use: | Azure AI Services offers pre-built AI models and tools, making it easier for developers with basic knowledge of Azure and AI to integrate advanced AI capabilities into their... |
| 2. Wide Range of Services: | Azure AI Services encompasses various domains, including: |
| 3. Scalability and Integration: | As a cloud service, Azure AI is highly scalable, allowing applications to handle increased loads without the need for extensive infrastructure changes. It integrates seamlessly... |
| 4. Business Benefits: | Azure AI Services help businesses increase efficiency, reduce costs, and make data-driven decisions. AI-driven insights can lead to more informed business strategies, improved... |
| 5. Innovation and Futureproofing: | As AI continues to evolve, Azure AI Services provide a platform for experimenting with and deploying the latest AI innovations, ensuring that applications remain relevant and... |
| Healthcare: | Azure AI can be used to develop applications for patient data analysis, predicting patient risks, and providing personalized healthcare recommendations. |
| Retail: | Retailers can leverage AI for personalized customer recommendations, inventory management, and customer sentiment analysis. |
| Banking: | AI applications in banking include fraud detection, risk management, and customer service chatbots. |
| Visual perception | The ability to use *computer* vision capabilities to accept, interpret, and process input from images, video streams, and live cameras. |
| Text analysis and conversation | The ability to use *natural language processing (NLP)* to not only "read", but also generate realistic responses and extract semantic meaning from text. |

**Key Points:**
- Azure AI Services, which provides APIs for vision, speech, language, decision, and search, enabling features like speech recognition, language understanding, and computer vision in applications.
- Azure Machine Learning, a platform for building, training, and deploying machine learning models at scale, catering to both seasoned data scientists and developers just getting to know to machine...
- Azure Bot Services, which enables the creation of intelligent, conversational AI bots, useful in customer service, e-commerce, and internal company processes.
- Healthcare: Azure AI can be used to develop applications for patient data analysis, predicting patient risks, and providing personalized healthcare recommendations.
- Retail: Retailers can leverage AI for personalized customer recommendations, inventory management, and customer sentiment analysis.
- Banking: AI applications in banking include fraud detection, risk management, and customer service chatbots.
- Run experiments to explore data and train predictive models.
- Deploy and manage trained models as web services.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 2

### Building Natural Language Solutions

**TL;DR:** <edukamu-video content="/videos/devai-7-unit2-video.yaml"/>
<br>

**Topics covered:**
- Recap: Natural Language Processing (NLP)
- NLP and Azure AI Language
- Introduction to Question Answering
- Question Answering or Language Understanding?
- Step 1. Creating a Knowledge Base
- Step 2. Implementing Multi-Turn Conversation
- Step 3. Testing and Publishing a Knowledge Phase
- Testing a Knowledge Base
- Deploying a Knowledge Base
- Step 4. Using a Knowledge Base

**Key Terms:**

| Term | Definition |
|------|-----------|
| Azure AI Language | includes a *question answering* capability, which enables you to define a *knowledge base* of question-and-answer pairs that can be queried using natural language input. The... |
| Note: | The question answering capability of Azure AI Language is a newer version of the QnA Service, which still exists as a standalone service. Please don't let this re-branding confuse... |
| Azure AI services | using the search field at the top of the portal. |
| Create | under the **Language Service** resource. |
| Azure AI Search | resource to host the knowledge base index. |
| Property | </edukamu-table-header> |
| Description | </edukamu-table-header> |
| Accept all suggestions | or **Reject all suggestions** option at the top. |
| Reminder | Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere.... |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. |

**Key Points:**
- Web sites containing frequently asked question (FAQ) documentation.
- Files containing structured text, such as brochures or user guides.
- Built-in *chit chat* question and answer pairs that encapsulate common conversational exchanges.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Capabilities Of Clu

**TL;DR:** Conversational language understanding can greatly enhance user experience and empower our chatbots in ways that seemed unimaginable just a few years ago.

**Topics covered:**
- Defining Intents, Utterances, and Entities
- Differentiating Utterances with Patterns
- Using Prebuilt Entity Components
- Process: Setting Up a CLU Model
- Practice: Building a CLU Model with Azure AI Services
- Exercise: Capabilities of CLU

**Key Terms:**

| Term | Definition |
|------|-----------|
| GetTime | "What time is it?" |
| GetWeather | "What is the weather forecast?" |
| TurnOnDevice | "Turn the light on." |
| None | intent that you should use to explicitly identify utterances that a user might submit, but for which there is no specific action required (for example, conversational greetings... |
| precisely | Label each entity to its right type always. Only include what you want extracted, avoid unnecessary data in your labels. |
| consistently | The same entity should have the same label across all the utterances. |
| completely | Label all the instances of the entity in all your utterances. |
| TurnOnDevice | intent that can be applied to multiple devices, and use entities to define the different devices. |
| Utterance | </edukamu-table-header> |
| Intent | </edukamu-table-header> |

**Key Points:**
- Capture multiple different examples, or alternative ways of saying the same thing
- Vary the length of the utterances from short, to medium, to long
- Vary the location of the *noun* or *subject* of the utterance. Place it at the beginning, the end, or somewhere in between
- Use correct grammar and incorrect grammar in different utterances to offer good training data examples
- The precision, consistency and completeness of your labeled data are key factors to determining model performance.
- Learned entities are the most flexible kind of entity, and should be used in most cases. You define a learned component with a suitable name, and then associate words or phrases with it in training...
- List entities are useful when you need an entity with a specific set of possible values - for example, days of the week. You can include synonyms in a list entity definition, so you could define a...
- Prebuilt entities are useful for common types such as numbers, datetimes, and names. For example, when prebuilt components are added, you will automatically detect values such as "6" or organizations...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Conversational Language Understanding

**TL;DR:** Question answering models have proven incredibly useful for retrieving information by responding to direct questions. However, in real-life interactions, language is often more nuanced and interactive. Conversational Language Understanding takes us beyond simple Q&A scenarios and focuses on the complexities of understanding and generating human-lik...

**Topics covered:**
- Getting Started with Conversational Language Understanding
- Key Benefits of Conversational Language Understanding
- Conversational Language Understanding in Microsoft Azure
- Prebuilt Capabilities in Azure AI Language
- 1. Pre-configured Features
- 2. Learned Features
- Resources and Conversational Language Understanding
- 1. Build Your Model
- 2. Use Language Studio
- 3. Use REST API

**Key Terms:**

| Term | Definition |
|------|-----------|
| Azure AI Language | enables developers to build apps based on language models that can be trained with a relatively small number of samples to discern a user's intended meaning. |
| Note: | Quality of data greatly impacts the model's accuracy. Be intentional about what data is used, how well it is tagged or labeled, and how varied the training data is. |
| Create | under the **Language Service**. |
| Keys and Endpoint | of the resource overview page. |
| POST | request to the following endpoint. |
| Placeholder | </edukamu-table-header> |
| Value | </edukamu-table-header> |
| Example | </edukamu-table-header> |
| GET | request to the URL from the response header above. The values will already be filled out based on the initial deployment request. |
| Placeholder | </edukamu-table-header> |

**Key Points:**
- The intents and entities include a confidence score between 0.0 to 1.0 associated with how confident the model is about predicting a certain element in your project.
- The top scoring intent is contained within its own parameter.
- Only predicted entities will show up in your response.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 3

### Introduction To Building Natural Language Solutions

**TL;DR:** Now that we've explored Retrieval Augmented Generation (RAG) and Conversational Language Understanding (CLU), it's time to take our knowledge to the next level. These concepts have given us a glimpse into the powerful capabilities of natural language processing and AI-driven language models. However, learning about them is just the beginning of our...

**Topics covered:**
- REST API, SDK, and Azure OpenAI Service
- 1. Integrating Azure OpenAI Service
- Creating Azure OpenAI Resources
- Choosing and Deploying a Model
- Authentication and Specification of Deployed Models
- Prompt Engineering
- Available Endpoints
- 2. Using Azure OpenAI Service REST API
- Completions
- Chat Completions

**Key Terms:**

| Term | Definition |
|------|-----------|
| Azure OpenAI Service | In the following sections, we’ll explore the process of creating natural language solutions with a toolbox called Azure OpenAI Service. We’ll explore it in detail in the fourth... |
| Overview | REST API is a set of rules and conventions for building and interacting with web services. It allows developers to access and utilize the functionality of Azure OpenAI Service... |
| Significance | With the REST API, developers can make HTTP requests to access the capabilities of Azure OpenAI Service from any programming language or platform. This is particularly useful for... |
| Overview | SDK is a set of pre-built libraries, tools, and code samples that simplifies the process of working with Azure OpenAI Service. It provides a higher-level abstraction and... |
| Significance | The Azure OpenAI SDK makes it easier and more efficient for developers to integrate OpenAI's language models into their applications. It offers ready-made functions and... |
| Important | Azure OpenAI has been released with limited access to support the responsible use of the service. Users need to apply for access and be approved before they can create an AOAI... |
| Text | or **Generative Pre-trained Transformer (GPT)** - Models that understand and generate natural language and some code. These models are best at general tasks, conversations, and... |
| Code | Code models are built on top of GPT models, and trained on millions of lines of code. These models can understand and generate code, including interpreting comments or natural... |
| Embeddings | These models can understand and use embeddings, which are a special format of data that can be used by machine learning models and algorithms. |
| Deployments | page. The lab later in this section covers exactly how to do that. |

**Key Points:**
- Text or Generative Pre-trained Transformer (GPT) - Models that understand and generate natural language and some code. These models are best at general tasks, conversations, and chat formats.
- Code - Code models are built on top of GPT models, and trained on millions of lines of code. These models can understand and generate code, including interpreting comments or natural language to...
- Embeddings - These models can understand and use embeddings, which are a special format of data that can be used by machine learning models and algorithms.
- Completion - model takes an input prompt, and generates one or more predicted completions
- ChatCompletion - model takes input in the form of a chat conversation (where roles are specified with the message they send), and the next chat completion is generated
- Embeddings - model takes input and returns a vector representation of that input

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Rag Capabilities In Microsoft Azure

**TL;DR:** In summary, Retrieval Augmentation Generation (RAG) is an architecture that augments the capabilities of a Large Language Model (LLM) like ChatGPT by adding an information retrieval system that provides grounding data. Adding an information retrieval system gives you control over grounding data used by an LLM when it formulates a response. For an e...

**Topics covered:**
- Approaches for RAG with Azure AI Search
- RAG Architecture
- Searchable Content in Azure AI Search
- Content Retrieval in Azure AI Search
- Structuring the Query Response
- Ranking by Relevance
- Advanced Example: Code of an Azure AI Search Query for RAG Scenarios
- Use semantic ranker if requested and if retrieval mode is text or hybrid (vectors + text)
- Advanced Example: Integration Code and LLMs
- Execute this cell multiple times updating user_input to accumulate chat history

**Key Terms:**

| Term | Definition |
|------|-----------|
| Content type | </edukamu-table-header> |
| Indexed as | </edukamu-table-header> |
| Features | </edukamu-table-header> |
| Query feature | </edukamu-table-header> |
| Purpose | </edukamu-table-header> |
| Why use it | </edukamu-table-header> |
| Scenario | A customer, Sarah, is looking for a new smartphone but is overwhelmed by the choices. |
| RAG and CLU Integration | When Sarah asks for recommendations, the system uses CLU to understand her query's context and preferences. Then, RAG retrieves relevant information from a vast database,... |
| Outcome | Sarah receives a personalized list of smartphones that fit her preferences, along with summarized reviews and ratings, making her decision process easier. |
| Scenario | John, another customer, is browsing for winter jackets but leaves the site without making a purchase. |

**Key Points:**
- Indexing strategies that load and refresh at scale, for all of your content, at the frequency you require.
- Query capabilities and relevance tuning. The system should return relevant results, in the short-form formats necessary for meeting the token length requirements of LLM inputs.
- Security, global reach, and reliability for both data and operations.
- Azure AI Studio, use a vector index and retrieval augmentation.
- Azure OpenAI Studio, use a search index with or without vectors.
- Azure Machine Learning, use a search index as a vector store in a prompt flow.
- Start with a user question or request (prompt).
- Send it to Azure AI Search to find relevant information.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Retrieving Information With Azure Ai Search

**TL;DR:** <edukamu-video content="/videos/devai-7-unit3-video.yaml"/>
<br>

**Topics covered:**
- Getting Started with RAG
- Key Benefits of RAG
- RAG and Azure AI Search
- 1. Managing Capacity
- Service Tiers and Capacity Management
- Replicas and Partitions
- 2. Understanding Search Components
- Data Source
- Skillset
- Indexer

**Key Terms:**

| Term | Definition |
|------|-----------|
| Enhanced Responses | RAG focuses on improving the quality of responses generated by AI systems. It achieves this by retrieving relevant information from large corpora of text or knowledge bases and... |
| Azure AI Search | resource in your Azure subscription. Depending on the specific solution you intend to build, you may also need Azure resources for data storage and other application services. |
| Basic (B) | Use this tier for small-scale search solutions that include a maximum of 15 indexes and 2 GB of index data. |
| Standard (S) | Use this tier for enterprise-scale solutions. There are multiple variants of this tier, including **S**, **S2**, and **S3**; which offer increasing capacity in terms of indexes... |
| Storage Optimized (L) | Use a storage optimized tier (**L1** or **L2**) when you need to create large indexes, at the cost of higher query latency. |
| Note | It's important to select the most suitable pricing tier for your solution, because you can't change it later. If you find that the pricing tier you have chosen is no longer... |
| key | Fields that define a unique key for index records. |
| searchable | Fields that can be queried using full-text search. |
| filterable | Fields that can be included in filter expressions to return only documents that match specified constraints. |
| sortable | Fields that can be used to order the results. |

**Key Points:**
- Index documents and data from a range of sources.
- Use cognitive skills to enrich index data.
- Store extracted insights in a knowledge store for analysis and integration.
- Free (F). Use this tier to explore the service or try the tutorials in the product documentation.
- Basic (B): Use this tier for small-scale search solutions that include a maximum of 15 indexes and 2 GB of index data.
- Standard (S): Use this tier for enterprise-scale solutions. There are multiple variants of this tier, including S, S2, and S3; which offer increasing capacity in terms of indexes and storage, and...
- Storage Optimized (L): Use a storage optimized tier (L1 or L2) when you need to create large indexes, at the cost of higher query latency.
- *Replicas* are instances of the search service - you can think of them as nodes in a cluster. Increasing the number of replicas can help ensure there is sufficient capacity to service multiple...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 4

### Fine Tuning Effective Prompts

**TL;DR:** Generative artificial intelligence is capable of amazing feats, ranging from generating human-like speech and text to creating brand-new music and images. But we can’t take advantage of all its capabilities if we can’t provide it with detailed, easy to follow instructions. We’re, naturally, talking about prompts.

**Topics covered:**
- Understanding Prompt Engineering
- What is Prompt Engineering?
- Considerations for API Endpoints
- Adjusting Model Parameters
- 1. Providing Clear Instructions
- 2. Formatting Instructions
- Using Section Markers
- 3. Primary, Supporting, and Grounding Content
- 4. Cues
- 1. Requesting Output Composition

**Key Terms:**

| Term | Definition |
|------|-----------|
| Important | No matter how good of a prompt you can design, responses from AI models should never be taken as fact or completely free from bias. Always use AI responsibly. We’ll visit this... |
| Prompt | Write a product description for a new water bottle |
| Response | *Introducing the latest addition to our product line - the innovative and eco-friendly water bottle. Made from high-quality, BPA-free materials, this bottle is designed to keep... |
| Prompt | Write a product description for a new water bottle that is 100% recycled. Be sure to include that it comes in natural colors with no dyes, and each purchase removes 10 pounds of... |
| Response | *Introducing our newest water bottle, the eco-friendly choice for the conscious consumer. Made from 100% recycled materials and available in natural colors with no dyes, this... |
| Note | Best practices for section markers may change over time as the AI models are developed further. |
| Note | More conversation history included in the prompt means a larger number of input tokens are used. You will have to determine what the correct balance is for your use case,... |
| Reminder | Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere.... |

**Key Points:**
- "I want you to act like a command line terminal. Respond to commands exactly as cmd.exe would, in one unique code block, and nothing else."
- "I want you to be a translator, from English to Spanish. Don't respond to anything I say or ask, only translate between those two languages and reply with the translated text."
- "Act as a motivational speaker, freely giving out encouraging advice about goals and challenges. You should include lots of positive affirmations and suggested activities for reaching the user's end...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Generating Code With Ai

**TL;DR:** Prompt engineering has provided us with a solid foundation, teaching us to communicate effectively with AI models, guiding them to produce accurate and context-aware responses. Just answering questions is only the beginning, though, as these models can assist you in generating code, simplifying complex programming tasks, and even offering creative ...

**Topics covered:**
- Generating Code with Natural Language
- AI Models for Code Generation
- Writing Functions
- Completing Code
- 1. Completing Partial Code
- 2. Writing Unit Tests
- 3. Adding Comments and Generating Documentation
- Fixing Bugs and Improving the Code
- 1. Fixing Bugs in Code
- 2. Improving Code Performance

**Key Terms:**

| Term | Definition |
|------|-----------|
| Reminder | Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere.... |

**Key Points:**
- If n is equal to 0, the function returns m + 1.
- If m is equal to 0, the function calls itself recursively with n - 1 and 1 as arguments.
- Otherwise, the function calls itself recursively with n - 1 and the result of calling itself with n

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Getting Started With Azure Openai

**TL;DR:** <edukamu-video content="/videos/devai-7-unit4-video.yaml"/>
<br>

**Topics covered:**
- Introduction to Azure OpenAI Service
- Setting Up Resources with Azure Portal
- Setting Up Resources with Azure CLI
- Using Azure OpenAI Studio
- Generative AI in Azure OpenAI Service
- Deploying Generative AI Models
- 1. Deployment with Azure OpenAI Studio
- 2. Deployment with Azure CLI
- 3. Deployment with the REST API
- Using Prompts

**Key Terms:**

| Term | Definition |
|------|-----------|
| Note | You can find the regions available for a service through the CLI command az account list-locations. |
| Deployments | page, from where you can deploy a base model and start experimenting with it. |
| GPT-4 models | are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code completions based on natural language prompts. |
| GPT 3.5 models | can generate natural language and code completions based on natural language prompts. In particular, **GPT-35-turbo** models are optimized for chat-based interactions and work... |
| Embeddings models | convert text into numeric vectors, and are useful in language analytics scenarios such as comparing text sources for similarities. |
| DALL-E models | are used to generate images based on natural language prompts. Currently, DALL-E models are in preview. DALL-E models aren't listed in the Azure OpenAI Studio interface and don't... |
| Models | page lists the available base models (other than DALL-E models) and provides an option to create additional customized models by fine-tuning the base models. The models that have... |
| Deployments | page, you can create a new deployment by selecting a model name from the menu. The available base models come from the list in the models page. |
| Task type | </edukamu-table-header> |
| Prompt example | </edukamu-table-header> |

**Key Points:**
- MyOpenAIResource: *replace with a unique name for your resource*
- OAIResourceGroup: *replace with your resource group name*
- eastus: *replace with the region to deploy your resource*
- subscriptionID: *replace with your subscription ID*
- GPT-4 models are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code completions based on natural language prompts.
- GPT 3.5 models can generate natural language and code completions based on natural language prompts. In particular, GPT-35-turbo models are optimized for chat-based interactions and work well in most...
- Embeddings models convert text into numeric vectors, and are useful in language analytics scenarios such as comparing text sources for similarities.
- DALL-E models are used to generate images based on natural language prompts. Currently, DALL-E models are in preview. DALL-E models aren't listed in the Azure OpenAI Studio interface and don't need...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Responsible Generative Ai

**TL;DR:** So far during this study program, we’ve noticed how artificial intelligence can boost productivity, enhance creativity, and simplify complex coding tasks. The collaboration between human developers and AI-powered algorithms has broadened our horizons in the world of programming. However, with great power comes great responsibility.

**Topics covered:**
- 1. Planning Responsible Generative AI Solutions
- 2. Identifying Potential Harms
- 1. Identify Potential Harms
- 2. Prioritize the Harms
- 3. Test and Verify the Prioritized Harms
- 4. Document and Share the Verified Harms
- 3. Measuring Potential Harms
- Manual and Automatic Testing
- 4. Mitigating Potential Harms
- 1. The Model Layer

**Key Terms:**

| Term | Definition |
|------|-----------|
| Context Establishment | This stage involves understanding the environment in which the AI system will operate, including its purpose, the stakeholders involved, and the legal, regulatory, and ethical... |
| Governance | This aspect focuses on establishing oversight and accountability mechanisms. It includes developing policies, procedures, and standards to guide AI development and deployment. |
| Risk Assessment | This step involves identifying, analyzing, and evaluating risks. This includes understanding the potential for harm, bias, and other unintended consequences of AI systems. |
| Risk Response | After assessing risks, organizations must decide on how to address them. This could involve mitigating, accepting, transferring, or avoiding risks. |
| Monitoring and Review | Continuous monitoring of the AI system is essential to assess its performance and to identify any new or evolving risks. This stage also includes periodic reviews to ensure that... |
| Communication and Reporting | Transparent communication and reporting mechanisms are crucial for conveying information about AI risks and management strategies to stakeholders. |
| Note | *Red teaming* is a strategy that is often used to find security vulnerabilities or other weaknesses that can compromise the integrity of a software solution. By extending this... |
| Screening Outputs | Content filters quickly review AI-generated content for any red flags, such as hate speech, explicit material, or misinformation. |
| Customization | Content filters can often be tailored to specific use cases, allowing businesses to set their own thresholds for what is considered acceptable. |
| Maintain Ethical Standards | Content filters help in maintaining a high ethical standard in AI interactions. |

**Key Points:**
- Generating content that is offensive, pejorative, or discriminatory.
- Generating content that contains factual inaccuracies.
- Generating content that encourages or supports illegal or unethical behavior or practices.
- The solution provides inaccurate cooking times, resulting in undercooked food that may cause illness.
- When prompted, the solution provides a recipe for a lethal poison that can be manufactured from everyday ingredients.
- Selecting a model that is appropriate for the intended solution use. For example, while GPT-4 may be a powerful and versatile model, in a solution that is required only to classify small, specific...
- *Fine-tuning* a foundational model with your own training data so that the responses it generates are more likely to be relevant and scoped to your solution scenario.
- Specifying *metaprompts* or system inputs that define behavioral parameters for the model.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Summary

**TL;DR:** Congratulations on reaching the summary of the Getting Started with AI Development course! As stated at the beginning, you must complete every assignment in order to pass this course. Therefore please go to Course progress page by pressing the button below (*or the progress icon in the top right corner*), and check that you have indeed completed al...

**Topics covered:**
- Unit 1: Foundations of Azure AI Services
- Unit 2: Natural Language Processing
- Unit 3: Retrieval Augmented Generation
- Unit 4: Implementing Generative AI
- Course Feedback

**Key Points:**
- What tools are included in Azure AI Services?
- How can using containers make Azure AI Services more powerful?
- How would you describe the main functions of Azure AI Language?
- What are the main capabilities and benefits of natural language processing?
- What are question answering and conversational language understanding? How do they differ?
- How do question answering and conversational language understanding complement each other?
- What is retrieval augmented generation?
- How is RAG implemented in Azure AI Search?

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Quick-Reference Glossary

| Term | Definition | Section |
|------|-----------|---------|
| Recap: Containers | Containerized development, unlike traditional methods, separates applications from specific hardware and software configurations. Containers encapsulate applications and... | Deploying Azure Ai Containers |
| Feature | </edukamu-table-header> | Deploying Azure Ai Containers |
| Image | </edukamu-table-header> | Deploying Azure Ai Containers |
| Setting | </edukamu-table-header> | Deploying Azure Ai Containers |
| Language | </edukamu-table-header> | Enabling Azure Ai Services |
| Speech | </edukamu-table-header> | Enabling Azure Ai Services |
| Vision | </edukamu-table-header> | Enabling Azure Ai Services |
| Decision | </edukamu-table-header> | Enabling Azure Ai Services |
| Azure AI Document Intelligence | An optical character recognition (OCR) solution that can extract semantic meaning from forms, such as invoices, receipts, and others. | Enabling Azure Ai Services |
| Azure AI Immersive Reader | A reading solution that supports people of all ages and abilities. | Enabling Azure Ai Services |
| Azure AI Search | A cloud-scale search solution that uses AI services to extract insights from data and documents. | Enabling Azure Ai Services |
| Azure OpenAI | An Azure AI Service that provides access to the capabilities of OpenAI GPT-4. | Enabling Azure Ai Services |
| AI services | resource that supports multiple different AI services. For example, you could create a single resource that enables you to use the **Azure AI Language**, **Azure AI Vision**,... | Enabling Azure Ai Services |
| AI Language | and **AI Vision** resources in your Azure subscription. | Enabling Azure Ai Services |
| Language detection | determining the language in which text is written. | Getting Started With Azure Ai Language |
| Key phrase extraction | identifying important words and phrases in the text that indicate the main points. | Getting Started With Azure Ai Language |
| Sentiment analysis | quantifying how positive or negative the text is. | Getting Started With Azure Ai Language |
| Named entity recognition | detecting references to entities, including people, locations, time periods, organizations, and more. | Getting Started With Azure Ai Language |
| Entity linking | identifying specific entities by providing reference links to Wikipedia articles. | Getting Started With Azure Ai Language |
| Note: | The code examples in the subsequent sections show the JSON requests and responses exchanged with the REST interface. When using an SDK, the JSON requests are abstracted by... | Getting Started With Azure Ai Language |
| text | to be analyzed. Optionally, you can provide a **countryHint** to improve prediction performance. | Getting Started With Azure Ai Language |
| neutral | classification values between 0 and 1. | Getting Started With Azure Ai Language |
| 10. | Type in the code and then click "Verify code". | Getting Started With Azure Ai Language |
| 11. | Fill in the rest of the form. | Getting Started With Azure Ai Language |
| 1. Ease of Use: | Azure AI Services offers pre-built AI models and tools, making it easier for developers with basic knowledge of Azure and AI to integrate advanced AI capabilities into their... | Getting Started With Azure Ai Services |
| 2. Wide Range of Services: | Azure AI Services encompasses various domains, including: | Getting Started With Azure Ai Services |
| 3. Scalability and Integration: | As a cloud service, Azure AI is highly scalable, allowing applications to handle increased loads without the need for extensive infrastructure changes. It integrates seamlessly... | Getting Started With Azure Ai Services |
| 4. Business Benefits: | Azure AI Services help businesses increase efficiency, reduce costs, and make data-driven decisions. AI-driven insights can lead to more informed business strategies, improved... | Getting Started With Azure Ai Services |
| 5. Innovation and Futureproofing: | As AI continues to evolve, Azure AI Services provide a platform for experimenting with and deploying the latest AI innovations, ensuring that applications remain relevant and... | Getting Started With Azure Ai Services |
| Healthcare: | Azure AI can be used to develop applications for patient data analysis, predicting patient risks, and providing personalized healthcare recommendations. | Getting Started With Azure Ai Services |
| Retail: | Retailers can leverage AI for personalized customer recommendations, inventory management, and customer sentiment analysis. | Getting Started With Azure Ai Services |
| Banking: | AI applications in banking include fraud detection, risk management, and customer service chatbots. | Getting Started With Azure Ai Services |
| Visual perception | The ability to use *computer* vision capabilities to accept, interpret, and process input from images, video streams, and live cameras. | Getting Started With Azure Ai Services |
| Text analysis and conversation | The ability to use *natural language processing (NLP)* to not only "read", but also generate realistic responses and extract semantic meaning from text. | Getting Started With Azure Ai Services |
| Azure AI Language | includes a *question answering* capability, which enables you to define a *knowledge base* of question-and-answer pairs that can be queried using natural language input. The... | Building Natural Language Solutions |
| Azure AI services | using the search field at the top of the portal. | Building Natural Language Solutions |
| Create | under the **Language Service** resource. | Building Natural Language Solutions |
| Property | </edukamu-table-header> | Building Natural Language Solutions |
| Description | </edukamu-table-header> | Building Natural Language Solutions |
| Accept all suggestions | or **Reject all suggestions** option at the top. | Building Natural Language Solutions |
| Reminder | Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical hardware or software not available for everyone or everywhere.... | Building Natural Language Solutions |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. | Building Natural Language Solutions |
| GetTime | "What time is it?" | Capabilities Of Clu |
| GetWeather | "What is the weather forecast?" | Capabilities Of Clu |
| TurnOnDevice | "Turn the light on." | Capabilities Of Clu |
| None | intent that you should use to explicitly identify utterances that a user might submit, but for which there is no specific action required (for example, conversational greetings... | Capabilities Of Clu |
| precisely | Label each entity to its right type always. Only include what you want extracted, avoid unnecessary data in your labels. | Capabilities Of Clu |
| consistently | The same entity should have the same label across all the utterances. | Capabilities Of Clu |
| completely | Label all the instances of the entity in all your utterances. | Capabilities Of Clu |
| Utterance | </edukamu-table-header> | Capabilities Of Clu |
| Intent | </edukamu-table-header> | Capabilities Of Clu |
| Keys and Endpoint | of the resource overview page. | Conversational Language Understanding |
| POST | request to the following endpoint. | Conversational Language Understanding |
| Placeholder | </edukamu-table-header> | Conversational Language Understanding |
| Value | </edukamu-table-header> | Conversational Language Understanding |
| Example | </edukamu-table-header> | Conversational Language Understanding |
| GET | request to the URL from the response header above. The values will already be filled out based on the initial deployment request. | Conversational Language Understanding |
| Azure OpenAI Service | In the following sections, we’ll explore the process of creating natural language solutions with a toolbox called Azure OpenAI Service. We’ll explore it in detail in the fourth... | Introduction To Building Natural Language Solutions |
| Overview | REST API is a set of rules and conventions for building and interacting with web services. It allows developers to access and utilize the functionality of Azure OpenAI Service... | Introduction To Building Natural Language Solutions |
| Significance | With the REST API, developers can make HTTP requests to access the capabilities of Azure OpenAI Service from any programming language or platform. This is particularly useful for... | Introduction To Building Natural Language Solutions |
| Important | Azure OpenAI has been released with limited access to support the responsible use of the service. Users need to apply for access and be approved before they can create an AOAI... | Introduction To Building Natural Language Solutions |
| Code | Code models are built on top of GPT models, and trained on millions of lines of code. These models can understand and generate code, including interpreting comments or natural... | Introduction To Building Natural Language Solutions |
| Embeddings | These models can understand and use embeddings, which are a special format of data that can be used by machine learning models and algorithms. | Introduction To Building Natural Language Solutions |
| Deployments | page. The lab later in this section covers exactly how to do that. | Introduction To Building Natural Language Solutions |
| Content type | </edukamu-table-header> | Rag Capabilities In Microsoft Azure |
| Indexed as | </edukamu-table-header> | Rag Capabilities In Microsoft Azure |
| Features | </edukamu-table-header> | Rag Capabilities In Microsoft Azure |
| Query feature | </edukamu-table-header> | Rag Capabilities In Microsoft Azure |
| Purpose | </edukamu-table-header> | Rag Capabilities In Microsoft Azure |
| Why use it | </edukamu-table-header> | Rag Capabilities In Microsoft Azure |
| Scenario | A customer, Sarah, is looking for a new smartphone but is overwhelmed by the choices. | Rag Capabilities In Microsoft Azure |
| RAG and CLU Integration | When Sarah asks for recommendations, the system uses CLU to understand her query's context and preferences. Then, RAG retrieves relevant information from a vast database,... | Rag Capabilities In Microsoft Azure |
| Outcome | Sarah receives a personalized list of smartphones that fit her preferences, along with summarized reviews and ratings, making her decision process easier. | Rag Capabilities In Microsoft Azure |
| Enhanced Responses | RAG focuses on improving the quality of responses generated by AI systems. It achieves this by retrieving relevant information from large corpora of text or knowledge bases and... | Retrieving Information With Azure Ai Search |
| Basic (B) | Use this tier for small-scale search solutions that include a maximum of 15 indexes and 2 GB of index data. | Retrieving Information With Azure Ai Search |
| Standard (S) | Use this tier for enterprise-scale solutions. There are multiple variants of this tier, including **S**, **S2**, and **S3**; which offer increasing capacity in terms of indexes... | Retrieving Information With Azure Ai Search |
| Storage Optimized (L) | Use a storage optimized tier (**L1** or **L2**) when you need to create large indexes, at the cost of higher query latency. | Retrieving Information With Azure Ai Search |
| Note | It's important to select the most suitable pricing tier for your solution, because you can't change it later. If you find that the pricing tier you have chosen is no longer... | Retrieving Information With Azure Ai Search |
| key | Fields that define a unique key for index records. | Retrieving Information With Azure Ai Search |
| searchable | Fields that can be queried using full-text search. | Retrieving Information With Azure Ai Search |
| filterable | Fields that can be included in filter expressions to return only documents that match specified constraints. | Retrieving Information With Azure Ai Search |
| sortable | Fields that can be used to order the results. | Retrieving Information With Azure Ai Search |
| Prompt | Write a product description for a new water bottle | Fine Tuning Effective Prompts |
| Response | *Introducing the latest addition to our product line - the innovative and eco-friendly water bottle. Made from high-quality, BPA-free materials, this bottle is designed to keep... | Fine Tuning Effective Prompts |
| GPT-4 models | are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code completions based on natural language prompts. | Getting Started With Azure Openai |
| GPT 3.5 models | can generate natural language and code completions based on natural language prompts. In particular, **GPT-35-turbo** models are optimized for chat-based interactions and work... | Getting Started With Azure Openai |
| Embeddings models | convert text into numeric vectors, and are useful in language analytics scenarios such as comparing text sources for similarities. | Getting Started With Azure Openai |
| DALL-E models | are used to generate images based on natural language prompts. Currently, DALL-E models are in preview. DALL-E models aren't listed in the Azure OpenAI Studio interface and don't... | Getting Started With Azure Openai |
| Models | page lists the available base models (other than DALL-E models) and provides an option to create additional customized models by fine-tuning the base models. The models that have... | Getting Started With Azure Openai |
| Task type | </edukamu-table-header> | Getting Started With Azure Openai |
| Prompt example | </edukamu-table-header> | Getting Started With Azure Openai |
| Context Establishment | This stage involves understanding the environment in which the AI system will operate, including its purpose, the stakeholders involved, and the legal, regulatory, and ethical... | Responsible Generative Ai |
| Governance | This aspect focuses on establishing oversight and accountability mechanisms. It includes developing policies, procedures, and standards to guide AI development and deployment. | Responsible Generative Ai |
| Risk Assessment | This step involves identifying, analyzing, and evaluating risks. This includes understanding the potential for harm, bias, and other unintended consequences of AI systems. | Responsible Generative Ai |
| Risk Response | After assessing risks, organizations must decide on how to address them. This could involve mitigating, accepting, transferring, or avoiding risks. | Responsible Generative Ai |
| Monitoring and Review | Continuous monitoring of the AI system is essential to assess its performance and to identify any new or evolving risks. This stage also includes periodic reviews to ensure that... | Responsible Generative Ai |
| Communication and Reporting | Transparent communication and reporting mechanisms are crucial for conveying information about AI risks and management strategies to stakeholders. | Responsible Generative Ai |
| Screening Outputs | Content filters quickly review AI-generated content for any red flags, such as hate speech, explicit material, or misinformation. | Responsible Generative Ai |
| Customization | Content filters can often be tailored to specific use cases, allowing businesses to set their own thresholds for what is considered acceptable. | Responsible Generative Ai |
| Maintain Ethical Standards | Content filters help in maintaining a high ethical standard in AI interactions. | Responsible Generative Ai |

---

*Auto-generated by `generate_diary.py` — re-run to refresh after re-scraping.*
