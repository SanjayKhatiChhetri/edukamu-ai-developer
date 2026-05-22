---
title: "Course 2: Exploring Artificial Intelligence"
layout: default
nav_order: 4
parent: Courses
---

# Course 2: Exploring Artificial Intelligence

**URL:** [https://cs.edukamu.fi/exploring-ai](https://cs.edukamu.fi/exploring-ai)  
**Sections:** 21  

---

## Table of Contents

- **Unit 1:** Azure And Ai | Fundamental Concepts Of Ai | Introduction To Machine Learning ...
- **Unit 2:** Ai And Facial Recognition | Fundamental Concepts Of Computer Vision | Recognizing Characters With Ai
- **Unit 3:** Azure And Ai Speech | Conversational Language Understanding | Fundamental Concepts Of Nlp ...
- **Unit 4:** Ai And Copilots | Azure Openai Services | Fundamentals Of Generative Ai ...
- **Unit 5:** Azure Ai Search | Azure And Cognitive Search | Enriched Data And Query Design ...

---

## Unit 1

### Azure And Ai

**TL;DR:** By this stage, you should already have quite a comprehensive understanding of both Azure and AI. On their own, they're already amazing services, but imagine them combined...

**Topics covered:**
- Azure AI Services
- Prebuilt and Ready to Go
- Example: APIs and Weather Apps
- Activating Azure AI Services
- Azure AI Terminology
- Exercise: Azure and AI

**Key Terms:**

| Term | Definition |
|------|-----------|
| Request | When you open the weather app, it sends a request to a Weather API, asking for the current weather data for your current location or another desired place. |
| API Response | The Weather API receives the request, fetches the latest weather information from its database, and sends back a response to your app. |
| Data Display | Your weather app takes the data received from the API and displays it beautifully on your screen – and that’s it! You know if you need an umbrella or sunglasses or even a pair of... |
| Multi-service resource | a resource created in the Azure portal that provides access to multiple Azure AI services with a single key and endpoint. Use the resource **Azure AI services** when you need... |
| Single-service resources | a resource created in the Azure portal that provides access to a single Azure AI service, such as Speech, Vision, Language, etc. Each Azure AI service has a unique key and... |
| API | application programming interfaces (APIs) enable software components to communicate, so one side can be updated without stopping the other from working. |
| Artificial Intelligence (AI) | computer programs that respond in ways that are normally associated with human reasoning, learning, and thought. |
| Azure AI services | a portfolio of AI services that can be incorporated into applications quickly and easily without specialist knowledge. Azure AI services is also the name for the multi-service... |
| Endpoint | the location of a resource, such as an Azure AI service. |
| Key | a private string that is used to authenticate a request. |

**Key Points:**
- Multi-service resource: a resource created in the Azure portal that provides access to multiple Azure AI services with a single key and endpoint. Use the resource Azure AI services when you need...
- Single-service resources: a resource created in the Azure portal that provides access to a single Azure AI service, such as Speech, Vision, Language, etc. Each Azure AI service has a unique key and...
- API – application programming interfaces (APIs) enable software components to communicate, so one side can be updated without stopping the other from working.
- Artificial Intelligence (AI) – computer programs that respond in ways that are normally associated with human reasoning, learning, and thought.
- Azure AI services – a portfolio of AI services that can be incorporated into applications quickly and easily without specialist knowledge. Azure AI services is also the name for the multi-service...
- Endpoint – the location of a resource, such as an Azure AI service.
- Key – a private string that is used to authenticate a request.
- Machine learning – the ability for computer programs to learn from large amounts of data, in a process known as "training".

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Fundamental Concepts Of Ai

**TL;DR:** <edukamu-video content="/videos/devai-2-unit1-video.yaml"/>
<br>

**Topics covered:**
- What is AI?
- 1. Machine Learning
- Machine Learning in Microsoft Azure
- 2. Computer Vision
- What Can Computer Vision Do?
- 3. Natural Language Processing
- NLP in Microsoft Azure
- 4. Generative AI
- Generative AI in Microsoft Azure
- 5. Document Intelligence

**Key Terms:**

| Term | Definition |
|------|-----------|
| Machine Learning | This is often the foundation for an AI system, and is the way we "teach" a computer model to make predictions and draw conclusions from data. |
| Computer Vision | Capabilities within AI to interpret the world visually through cameras, video, and images. |
| Natural Language Processing | Capabilities within AI for a computer to interpret written or spoken language, and respond in kind. |
| Document Intelligence | Capabilities within AI that deal with managing, processing, and using high volumes of data found in forms and documents. |
| Knowledge Mining | Capabilities within AI to extract information from large volumes of often unstructured data to create a searchable knowledge store. |
| Generative AI | Capabilities within AI that create original content in a variety of formats including natural language, image, code, and more. |
| Automated machine learning | this feature enables non-experts to quickly create an effective machine learning model from data. |
| Azure Machine Learning designer | a graphical interface enabling no-code development of machine learning solutions. |
| Data metric visualization | analyze and optimize your experiments with visualization. |
| Notebooks | write and run your own code in managed Jupyter Notebook servers that are directly integrated in the studio. |

**Key Points:**
- Machine Learning: This is often the foundation for an AI system, and is the way we "teach" a computer model to make predictions and draw conclusions from data.
- Computer Vision: Capabilities within AI to interpret the world visually through cameras, video, and images.
- Natural Language Processing: Capabilities within AI for a computer to interpret written or spoken language, and respond in kind.
- Document Intelligence: Capabilities within AI that deal with managing, processing, and using high volumes of data found in forms and documents.
- Knowledge Mining: Capabilities within AI to extract information from large volumes of often unstructured data to create a searchable knowledge store.
- Generative AI: Capabilities within AI that create original content in a variety of formats including natural language, image, code, and more.
- Automated machine learning: this feature enables non-experts to quickly create an effective machine learning model from data.
- Azure Machine Learning designer: a graphical interface enabling no-code development of machine learning solutions.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Introduction To Machine Learning

**TL;DR:** As you learned before, machine learning is all about, you know it, machines learning. In practice, the process is a lot more interesting and multi-faceted than that.

**Topics covered:**
- Origins of Machine Learning
- Interfencing in Action
- Supervised Machine Learning
- Regression
- Classification
- Unsupervised Machine Learning
- Clustering
- Exercise: Machine Learning Basics
- YRITYKSEN NIMI: Career in the World of AI

**Key Terms:**

| Term | Definition |
|------|-----------|
| y = f(x) | 4.	Now that the *training* phase is complete, the trained model can be used for *inferencing*. The model is essentially a software program that encapsulates the function produced... |

**Key Points:**
- The proprietor of an ice cream store might use an app that combines historical sales and weather records to predict how many ice creams they're likely to sell on a given day, based on the weather...
- A doctor might use clinical data from past patients to run automated tests that predict whether a new patient is at risk from diabetes based on factors like weight, blood glucose level, and other...
- A researcher in the Antarctic might use past observations automate the identification of different penguin species (such as Adelie, Gentoo, or Chinstrap) based on measurements of a bird's flippers,...
- In the ice cream sales scenario, our goal is to train a model that can predict the number of ice cream sales based on the weather. The weather measurements for the day (temperature, rainfall,...
- In the medical scenario, the goal is to predict whether or not a patient is at risk of diabetes based on their clinical measurements. The patient's measurements (weight, blood glucose level, and so...
- In the Antarctic research scenario, we want to predict the species of a penguin based on its physical attributes. The key measurements of the penguin (length of its flippers, width of its bill, and...
- In predicting ice cream sales based on weather, the weather measurements (temperature, rainfall, etc.) are features (x), and the number of ice creams sold is the label (y).
- In a medical scenario, patient measurements (weight, blood glucose) are features (x), and the likelihood of diabetes (1 for at risk, 0 for not at risk) is the label (y).

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Supervised Learning

**TL;DR:** Let's pause for a while and picture a world inhabited by algorithms. In fact, it's not that different from our own world, but the algorithms are visible and tangible – not just series of written code. The algorithms are moving around seemingly randomly, but once you follow them for a while, you begin to notice something...

**Topics covered:**
- 1. Regression
- Example: Regression
- 2. Binary Classification
- Example: Binary Classification
- 3. Multiclass Classification
- Example: Multiclass Classification
- Evaluating a Multiclass Classification Model
- Exercise: Supervised Learning
- Feedback to the task:

**Key Terms:**

| Term | Definition |
|------|-----------|
| f(x) = x-50 | You can use this function to predict the number of ice creams sold on a day with any given temperature. For example, suppose the weather forecast tells us that tomorrow it will be... |
| Mean Absolute Error (MAE) | Imagine predicting ice cream sales; MAE measures the average of absolute errors, revealing how much each prediction deviates from reality. In our example, the mean of errors (2,... |
| Mean Squared Error (MSE) | MAE treats all errors equally, but MSE magnifies larger errors by squaring them. The mean of squared errors (4, 9, 9, 1, 4, and 9) in our scenario is 6. |
| Root Mean Squared Error (RMSE) | To interpret errors in the original quantity (ice creams), we take the square root of MSE. Here, √6 equals 2.45 (ice creams). |
| Coefficient of determination (R2) | R2 goes beyond error comparison. It gauges how much of the variance in results can be ascribed to the model rather than random fluctuations. In our ice cream model, an R2 of 0.95... |
| true | or **false**. In most real scenarios, the data observations used to train and validate the model consist of multiple feature (**x**) values and a **y** value that is either **1**... |
| f(x) = P(y=1 | x) | For three of the six observations in the training data, we know that **y** is definitely *true*, so the probability for those observations that y=1 is **1.0** and for the other... |
| f<sup>0</sup>(x) = P(y=0 | x) | * **f<sup>1</sup>(x) = P(y=1 \| x)** |
| f<sup>2</sup>(x) = P(y=2 | x) | Each algorithm produces a sigmoid function that calculates a probability value between 0.0 and 1.0. A model trained using this kind of algorithm predicts the class for the... |
| f(x) =[P(y=0|x), P(y=1|x), P(y=2|x)] | An example of this kind of function is a *softmax* function, which could produce an output like the following example: |

**Key Points:**
- f<sup>0</sup>(x) = P(y=0 | x)
- f<sup>1</sup>(x) = P(y=1 | x)
- f<sup>2</sup>(x) = P(y=2 | x)
- Overall accuracy = (13+6)÷(13+6+1+1) = 0.90
- Overall recall = 6÷(6+1) = 0.86
- Overall precision = 6÷(6+1) = 0.86
- Overall F1-score = (2x0.86x0.86)÷(0.86+0.86) = 0.86

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Unsupervised Learning

**TL;DR:** Once again, close your eyes for a while and return to the world in which tangible, three-dimensional algorithms roam free... It kind of feels like you've just been here, doesn't it?

**Topics covered:**
- 1. Clustering
- Example: Clustering
- Evaluating a Clustering Model
- 2. Deep Learning
- Deep Learning and Classification
- Neural Networks and Learning
- Exercise: Unsupervised Learning
- Azure and Machine Learning
- Features and Capabilities

**Key Terms:**

| Term | Definition |
|------|-----------|
| Average distance to cluster center | How close, on average, each point in the cluster is to the centroid of the cluster. |
| Average distance to other center | How close, on average, each point in the cluster is to the centroid of all other clusters. |
| Maximum distance to cluster center | The furthest distance between a point in the cluster and its centroid. |
| Silhouette | A value between -1 and 1 that summarizes the ratio of distance between points in the same cluster and points in different clusters (The closer to 1, the better the cluster... |
| [37.3, 16.8, 19.2, 30.0] | 2.	The functions for the first layer of neurons each calculate a weighted sum by combining the **x** value and **w** weight, and pass it to an activation function that determines... |
| [0.2, 0.7, 0.1] | 5.	The elements of the vector represent the probabilities for classes 0, 1, and 2. The second value is the highest, so the model predicts that the species of the penguin is **1**... |

**Key Points:**
- Average distance to cluster center: How close, on average, each point in the cluster is to the centroid of the cluster.
- Average distance to other center: How close, on average, each point in the cluster is to the centroid of all other clusters.
- Maximum distance to cluster center: The furthest distance between a point in the cluster and its centroid.
- Silhouette: A value between -1 and 1 that summarizes the ratio of distance between points in the same cluster and points in different clusters (The closer to 1, the better the cluster separation).
- The length of the penguin's bill.
- The depth of the penguin's bill.
- The length of the penguin's flippers.
- Exploring data and preparing it for modeling.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 2

### Ai And Facial Recognition

**TL;DR:** Facial recognition is something the most of us might already have witnessed on our phones, tablets, or when crossing international borders. We’re talking about a sphere of AI in which machines not only see but recognize – a world where your face becomes a key.

**Topics covered:**
- Introduction to Facial Recognition
- Combining the Two: Facial Recognition
- Azure Face Service
- Tips for Accuracy
- Issue
- Microsoft's Approach
- Issue
- Microsoft's Approach
- Issue
- Microsoft's Approach

**Key Terms:**

| Term | Definition |
|------|-----------|
| face detection | and **face analysis**. |
| Accessories | indicates whether the given face has accessories. This attribute returns possible accessories including headwear, glasses, and mask, with confidence score between zero and one for... |
| Blur | how blurred the face is, which can be an indication of how likely the face is to be the main focus of the image. |
| Exposure | such as whether the image is underexposed or over exposed. This applies to the face in the image and not the overall image exposure. |
| Glasses | whether or not the person is wearing glasses. |
| Head pose | the face's orientation in a 3D space. |
| Mask | indicates whether the face is wearing a mask. |
| Noise | refers to visual noise in the image. If you have taken a photo with a high ISO setting for darker settings, you would notice this noise in the image. The image looks grainy or... |
| Occlusion | determines if there might be objects blocking the face in the image. |
| Please notice | that, in order to use the Face service, you must create one of the following types of resource in your Azure subscription: |

**Key Points:**
- Security - facial recognition can be used in building security applications, and increasingly it is used in smart phones operating systems for unlocking devices.
- Social media - facial recognition can be used to automatically tag known friends in photographs.
- Intelligent monitoring - for example, an automobile might include a system that monitors the driver's face to determine if the driver is looking at the road, looking at a mobile device, or shows...
- Advertising - analyzing faces in an image can help direct advertisements to an appropriate demographic audience.
- Missing persons - using public cameras systems, facial recognition can be used to identify if a missing person is in the image frame.
- Identity validation - useful at ports of entry kiosks where a person holds a special entry permit.
- Azure AI Vision, which offers face detection and some basic face analysis, such as returning the bounding box coordinates around an image.
- Azure AI Video Indexer, which you can use to detect and identify faces in a video.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Fundamental Concepts Of Computer Vision

**TL;DR:** <edukamu-video content="/videos/devai-2-unit2-video.yaml"/>
<br>

**Topics covered:**
- Computer Vision and Groceries
- Machine Learning and Computer Vision
- Convolutional Neural Networks (CNNs)
- Multi-modal Models (Microsoft Florence)
- Azure AI Vision
- Azure AI Vision and Image Analysis
- 1. Optical Character Recognition
- 2. Describing Images
- 3. Detecting Common Objects
- 4. Tagging Visual Features

**Key Terms:**

| Term | Definition |
|------|-----------|
| Automated Item Recognition | * As you pick items from the shelf, overhead cameras equipped with Computer Vision identify each product through visual recognition. |
| Seamless Shopping Experience | * Toss your selected items into your bag, and the smart cart updates your digital tab. |
| Intelligent Payment Processing | * Ready to leave? No queues, no scanning. The store's payment system, powered by Computer Vision, effortlessly tallies your selections. |
| Automated Receipt Generation | * Your purchase is complete. A digital receipt is instantly generated, detailing your items and the total cost. |
| Benefits | * **Efficiency**: Say goodbye to long queues. The streamlined process enhances the shopping experience, saving time for both customers and retailers. |
| Accuracy | Computer Vision reduces the risk of errors in item identification and pricing, providing a highly accurate transaction process. |
| Personalized Offers | The system, aware of your preferences, can offer personalized discounts and recommendations based on your shopping history. Similar technologies are, of course, largely used... |
| Azure AI Vision | A specific resource for the Azure AI Vision service. Use this resource type if you don't intend to use any other Azure AI services, or if you want to track utilization and costs... |
| Azure AI services | A general resource that includes Azure AI Vision along with many other Azure AI services; such as Azure AI Language, Azure AI Custom Vision, Azure AI Translator, and others. Use... |

**Key Points:**
- Toss your selected items into your bag, and the smart cart updates your digital tab.
- Computer Vision algorithms continuously analyze the contents of your cart in real-time.
- Ready to leave? No queues, no scanning. The store's payment system, powered by Computer Vision, effortlessly tallies your selections.
- The system ensures accuracy, even distinguishing between similar-looking products.
- Your purchase is complete. A digital receipt is instantly generated, detailing your items and the total cost.
- No more fumbling with paper receipts – everything is stored digitally.
- Efficiency: Say goodbye to long queues. The streamlined process enhances the shopping experience, saving time for both customers and retailers.
- Accuracy: Computer Vision reduces the risk of errors in item identification and pricing, providing a highly accurate transaction process.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Recognizing Characters With Ai

**TL;DR:** Artificial intelligence can be trained to do pretty much everything imaginable, and recognizing different shapes, forms, and even people is no exception. AI also excels in recognizing characters, with which we humans might struggle every once in a while.

**Topics covered:**
- Use Cases of Character Recognition
- 1. Document Digitization
- 2. Accessibility for Visually Impaired
- 3. Translation Services
- 4. Data Entry Automation
- 5. Historical Document Preservation
- Introduction to Azure Vision Studio
- Exercise: Character Recognition and AI
- YRITYS: Scenarios from Real Life

**Key Terms:**

| Term | Definition |
|------|-----------|
| Pages | One for each page of text, including information about the page size and orientation. |
| Lines | The lines of text on a page. |
| Words | The words in a line of text, including the bounding box coordinates and text itself. |
| Reminder | Here and there within these courses, you’ll find exercises marked *Practice*. They are not a mandatory requirement for completing this course since they may require technical... |
| Azure AI Vision | A specific resource for vision services. Use this resource type if you don't intend to use any other AI services, or if you want to track utilization and costs for your AI Vision... |
| Azure AI services | A general resource that includes Azure AI Vision along with many other Azure AI services such as Azure AI Language, Azure AI Speech, and others. Use this resource type if you plan... |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. |

**Key Points:**
- Pages - One for each page of text, including information about the page size and orientation.
- Lines - The lines of text on a page.
- Words - The words in a line of text, including the bounding box coordinates and text itself.
- Azure AI Vision: A specific resource for vision services. Use this resource type if you don't intend to use any other AI services, or if you want to track utilization and costs for your AI Vision...
- Azure AI services: A general resource that includes Azure AI Vision along with many other Azure AI services such as Azure AI Language, Azure AI Speech, and others. Use this resource type if you plan...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 3

### Azure And Ai Speech

**TL;DR:** In not-so-distant future, your morning routine might be significantly different from what you’re used to. Actually, it might not be that much different, but it will certainly be more personalized for your taste. Let’s use our imagination once again…

**Topics covered:**
- Introduction to AI Speech
- Speech Recognition and Synthesis
- Speech to Text API
- Speech to Text (API)
- Real-time Transcription
- Batch Transcription
- Text to Speech (API)
- Speech Synthesis Voices
- Supported Languages
- Exercise: Azure AI Speech

**Key Terms:**

| Term | Definition |
|------|-----------|
| Speech recognition | the ability to detect and interpret spoken input |
| Speech synthesis | the ability to generate spoken output |
| Azure AI Speech | provides speech to text and text to speech capabilities through speech recognition and synthesis. You can use prebuilt and custom Speech service models for a variety of tasks,... |
| Speech recognition | takes the spoken word and converts it into data that can be processed - often by transcribing it into text. The spoken words can be in the form of a recorded voice in an audio... |
| Speech synthesis | is concerned with vocalizing data, usually by converting text to speech. A speech synthesis solution typically requires the following information: |
| Speech | resource - choose this resource type if you only plan to use Azure AI Speech, or if you want to manage access and billing for the resource separately from other services. |
| Azure AI services | resource - choose this resource type if you plan to use Azure AI Speech in combination with other Azure AI services, and you want to manage access and billing for these services... |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. |

**Key Points:**
- Speech recognition - the ability to detect and interpret spoken input
- Speech synthesis - the ability to generate spoken output
- An *acoustic* model that converts the audio signal into phonemes (representations of specific sounds).
- A *language* model that maps phonemes to words, usually using a statistical algorithm that predicts the most probable sequence of words based on the phonemes.
- Providing closed captions for recorded or live videos
- Creating a transcript of a phone call or meeting
- Determining intended user input for further processing
- The voice to be used to vocalize the speech

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Conversational Language Understanding

**TL;DR:** Understanding words and questions is a challenge for every machine or AI, which in turn means that keeping a conversation going is even more demanding.

**Topics covered:**
- Introduction to Conversational Language Understanding
- Utterances, Entities, and Intents
- Utterances
- Entities
- Intents
- Azure and Conversational Language Understanding
- Authoring
- Training
- Predicting
- Exercise: Conversational Language Understanding

**Key Terms:**

| Term | Definition |
|------|-----------|
| Azure AI Language | service. One example using conversational language understanding is an application that's able to turn devices on and off based on speech. Many types of tasks involving command... |
| fan | and **light** entities as being specific instances of a general **device** entity. |
| TurnOn | intent that is related to these utterances. |
| None | intent. You should consider always using the *None* intent to help handle utterances that do not map any of the utterances you have entered. The *None* intent is considered a... |
| Azure AI Language | A resource that enables you to build apps with industry-leading natural language understanding capabilities without machine learning expertise. You can use a language resource for... |
| Azure AI services | A general resource that includes conversational language understanding along with many other Azure AI services. You can only use this type of resource for *prediction*. |

**Key Points:**
- Azure AI Language: A resource that enables you to build apps with industry-leading natural language understanding capabilities without machine learning expertise. You can use a language resource for...
- Azure AI services: A general resource that includes conversational language understanding along with many other Azure AI services. You can only use this type of resource for *prediction*.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Fundamental Concepts Of Nlp

**TL;DR:** <edukamu-video content="/videos/devai-2-unit3-video.yaml"/>
<br>

**Topics covered:**
- Introduction to NLP
- Use Cases of NLP
- NLP and Text Analysis
- Principle 1: Tokenization
- Principle 2: Frequency Analysis
- Tip
- Principle 3: Machine Learning in Text Classification
- Principle 4: Semantic Language Models
- 1. Entry Recognition
- 2. Language Detection

**Key Terms:**

| Term | Definition |
|------|-----------|
| Text Understanding | NLP enables machines to understand and extract information from written texts, making it valuable for tasks like sentiment analysis, named entity recognition, and information... |
| Language Translation | NLP is instrumental in machine translation, facilitating the conversion of text from one language to another, breaking down language barriers. |
| Chatbots and Virtual Assistants | NLP powers chatbots and virtual assistants, enabling them to understand and respond to user queries in a conversational manner. Microsoft’s Copilot, released in late 2023, is an... |
| Summarization | NLP algorithms can summarize large volumes of text, condensing information while retaining essential details. |
| Speech Recognition | NLP is used in speech recognition systems, converting spoken language into text, improving voice-activated technologies. |
| Search Engines | NLP enhances search engines by understanding user queries and providing more accurate and relevant results. |
| natural language processing | (NLP), an area within AI that deals with understanding written or spoken language and responding in kind. *Text analysis* describes NLP processes that extract information from... |
| Azure AI Language | is a cloud-based service that includes features for understanding and analyzing text. Azure AI Language includes various features that support sentiment analysis, key phrase... |
| Named entity recognition | identifies people, places, events, and more. This feature can also be customized to extract custom categories. |
| Entity linking | identifies known entities together with a link to Wikipedia. |

**Key Points:**
- A social media feed analyzer that detects sentiment for a product marketing campaign.
- A document search application that summarizes documents in a catalog.
- An application that extracts brands and company names from text.
- *The food and service were both great: 1*
- *A really terrible experience: 0*
- *Mmm! tasty food and a fun vibe: 1*
- *Slow service and substandard food: 0*
- Text analysis, such as extracting key terms or identifying named entities in text.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Question Answering

**TL;DR:** In the modern society, we’re used to being able to communicate at any time of the day or night, anywhere in the world, putting organizations under pressure to react fast enough to their customers.

**Topics covered:**
- Introduction to Question Answering
- Use Cases of Question Answering
- 1. Chatbots for Customer Support
- 2. Virtual Assistants
- 3. Educational Chatbots
- 4. Information Retrieval Bots
- 5. Search Engine Conversational Interfaces
- 1. Azure AI Language
- Define Questions and Answers
- 2. Azure AI Bot

**Key Terms:**

| Term | Definition |
|------|-----------|
| Question answering | supports natural language AI workloads that require an automated conversational element. Typically, question answering is used to build bot applications that respond to customer... |
| Example | A customer asks a chatbot, "How can I return a product?" The chatbot interprets the question, understands the context, and provides step-by-step instructions on the return process. |
| Example | A user asks a virtual assistant, "What's the weather forecast for tomorrow in Taivalkoski, Finland?" The virtual assistant uses question answering to extract the relevant... |
| Example | A student on an educational chatbot platform asks, "Explain the concept of photosynthesis." The chatbot processes the query, retrieves information from educational resources, and... |
| Example | A user queries a news bot, "What are the latest developments in renewable energy?" The bot uses question answering techniques to fetch recent news articles and presents a summary... |
| Example | A user interacts with a search engine chat interface, asking, "Who is the president of Finland?" The chatbot retrieves real-time data from the web and responds with the current... |
| Language | resource in your Azure subscription.) |

**Key Points:**
- Generated from an existing FAQ document or web page.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 4

### Ai And Copilots

**TL;DR:** The availability of LLMs has led to the emergence of a new software application, often referred to as a copilot. Copilots are often integrated into other applications and provide a way for users to get help with common tasks from a generative AI model. Copilots are based on a common architecture, so developers can build custom copilots for various ...

**Topics covered:**
- Introduction to Copilots
- Examples of Copilots
- Prompt Engineering
- System Messages
- Writing Good Prompts
- Providing Examples
- Grounding Data
- Practice: Exploring Generative AI
- Phase 1: Working with Text
- Phase 2: Image Generation

**Key Terms:**

| Term | Definition |
|------|-----------|
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |
| Note | While you can sign in with your work or school account, you will see a slightly different user experience compared to signing in with your personal account. Using your work or... |
| Note | If you do not see a *Generating… message or a bullet list response, you have not gotten to see Bing Copilot in action yet. You need to return to the sign-in menu and connect the... |
| Note | Notice that while Bing Copilot is able to give a related response, it can drop earlier “memories” of the conversation thread as it continues. As a result, the responses you get... |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. |

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Azure Openai Services

**TL;DR:** As mentioned previously, OpenAI is the research company behind the popular ChatGPT service as well as the GPT-4 large language model also used and endorsed by Microsoft.

**Topics covered:**
- Introduction to Azure OpenAI Service
- Azure AI Studio

**Key Terms:**

| Term | Definition |
|------|-----------|
| GPT-4 models | are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code completions based on natural language prompts. |
| GPT 3.5 models | can generate natural language and code completions based on natural language prompts. In particular, **GPT-35-turbo** models are optimized for chat-based interactions and work... |
| Embeddings models | convert text into numeric vectors, and are useful in language analytics scenarios such as comparing text sources for similarities. |
| DALL-E models | are used to generate images based on natural language prompts. Currently, DALL-E models are in preview. DALL-E models aren't listed in the Azure OpenAI Studio interface and don't... |

**Key Points:**
- GPT-4 models are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code completions based on natural language prompts.
- GPT 3.5 models can generate natural language and code completions based on natural language prompts. In particular, GPT-35-turbo models are optimized for chat-based interactions and work well in most...
- Embeddings models convert text into numeric vectors, and are useful in language analytics scenarios such as comparing text sources for similarities.
- DALL-E models are used to generate images based on natural language prompts. Currently, DALL-E models are in preview. DALL-E models aren't listed in the Azure OpenAI Studio interface and don't need...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Fundamentals Of Generative Ai

**TL;DR:** <edukamu-video content="/videos/devai-2-unit4-video.yaml"/>
<br>

**Topics covered:**
- Tip: Fascinated by AI?
- YRITYKSEN NIMI: Career in the Cloud
- 1. Introduction to Generative AI
- Natural Language Generation
- Image Generation
- Code Generation
- 2. Introduction to Large Language Models
- Transformer Models
- Tokenization in Transformer Models
- Embeddings in Transformer Models

**Key Terms:**

| Term | Definition |
|------|-----------|
| Note | The previous example shows a simple example model in which each embedding has only three dimensions. Real language models have many more dimensions. |
| I heard a dog [bark] | Remember that the attention layer is working with numeric vector representations of the tokens, not the actual text. In a decoder, the process starts with a sequence of token... |

**Key Points:**
- Determining *sentiment* or otherwise classifying natural language text.
- Comparing multiple text sources for semantic similarity.
- Generating new natural language.
- An *encoder* block that creates semantic representations of the training vocabulary.
- A *decoder* block that generates new language sequences.
- (*"a" is already tokenized as 3*)

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Responsibility And Ethics

**TL;DR:** Artificial intelligence is broadening the horizons of what we can achieve with technology. While these amazing tools are already capable of deeds considered impossible just a few years ago, it’s important to keep our cool.

**Topics covered:**
- Stages of Responsibility
- Stage 1: Identify Potential Harms
- 1. Identify
- 2. Prioritize
- 3. Test and Verify
- 4. Document and Share
- Stage 2: Measure the Situation
- Manual and Automatic Testing
- Stage 3: Mitigate Risks
- 1. Model Layer

**Key Terms:**

| Term | Definition |
|------|-----------|
| Note | Red teaming is a strategy that is often used to find security vulnerabilities or other weaknesses that can compromise the integrity of a software solution. By extending this... |

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

## Unit 5

### Azure Ai Search

**TL;DR:** In this unit, we've explored document intelligence and cognitive search from a variety of perspectives. It's time to add one last ingredient into the mix: Azure AI Search.

**Topics covered:**
- What is Azure AI Search?
- Identifying Search Solution Elements
- Setting Up Indexes
- Querying Azure AI Search Indexes
- Exercise: Azure AI Search

**Key Terms:**

| Term | Definition |
|------|-----------|
| Data from any source | accepts data from any source provided in JSON format, with auto crawling support for selected data sources in Azure. |
| Multiple options for search and analysis | including vector search, full text, and hybrid search. |
| AI enrichment | has Azure AI capabilities built in for image and text analysis from raw content. |
| Linguistic analysis | offers analysis for 56 languages to intelligently handle phonetic matching or language-specific linguistics. Natural language processors available in Azure AI Search are also used... |
| Configurable user experience | has options for query syntax including vector queries, text search, hybrid queries, fuzzy search, autocomplete, geo-search filtering based on proximity to a physical location, and... |
| Azure scale, security, and integration | at the data layer, machine learning layer, and with Azure AI services and Azure OpenAI. |
| Indexer | automates the movement data from the data *source* through *document cracking* and *enrichment* to *indexing*. An indexer automates a portion of data ingestion and exports the... |
| Document cracking | the indexer opens files and extracts content. |
| Enrichment | the indexer moves data through AI enrichment, which implements Azure AI on your original data to extract more information. AI enrichment is achieved by adding and combining skills... |
| Push to index | the serialized JSON data populates the search *index*. |

**Key Points:**
- Data from any source: accepts data from any source provided in JSON format, with auto crawling support for selected data sources in Azure.
- Multiple options for search and analysis: including vector search, full text, and hybrid search.
- AI enrichment: has Azure AI capabilities built in for image and text analysis from raw content.
- Linguistic analysis: offers analysis for 56 languages to intelligently handle phonetic matching or language-specific linguistics. Natural language processors available in Azure AI Search are also...
- Configurable user experience: has options for query syntax including vector queries, text search, hybrid queries, fuzzy search, autocomplete, geo-search filtering based on proximity to a physical...
- Azure scale, security, and integration: at the data layer, machine learning layer, and with Azure AI services and Azure OpenAI.
- Azure portal's Import data wizard
- with a software development kit (SDK)

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Azure And Cognitive Search

**TL;DR:** We all have used different search engines countless times in our lives, but have we ever stopped to wonder how they all work? One of the most basic principles is keyword matching: an engine provides results based on a search query, showing the user every instance where a matching word or phrase is found.

**Topics covered:**
- Introduction to Cognitive Search
- What is Azure Cognitive Search?
- Features
- 1. Elements of Search Solutions
- 2. Skillsets and Enrichment Pipelines
- Built-in Skills
- 3. Understanding Indexes
- Index Schema
- Index Attributes
- 4. Building Indexes with Indexers

**Key Terms:**

| Term | Definition |
|------|-----------|
| Data from any source | Azure Cognitive Search accepts data from any source provided in JSON format, with auto crawling support for selected data sources in Azure. |
| Full text search and analysis | Azure Cognitive Search offers full text search capabilities supporting both simple query and full Lucene query syntax. |
| AI powered search | Azure Cognitive Search has Azure AI capabilities built in for image and text analysis from raw content. |
| Multi-lingual | Azure Cognitive Search offers linguistic analysis for 56 languages to intelligently handle phonetic matching or language-specific linguistics. Natural language processors... |
| Geo-enabled | Azure Cognitive Search supports geo-search filtering based on proximity to a physical location. |
| Configurable user experience | Azure Cognitive Search has several features to improve the user experience including autocomplete, autosuggest, pagination, and hit highlighting. |
| Natural language processing skills | with these skills, unstructured text is mapped as searchable and filterable fields in an index. |
| Image processing skills | creates text representations of image content, making it searchable using the query capabilities of Azure Cognitive Search. |
| Push method | JSON data is pushed into a search index via either the REST API or the .NET SDK. Pushing data has the most flexibility as it has no restrictions on the data source type, location,... |
| Pull method | Search service indexers can pull data from popular Azure data sources, and if necessary, export that data into JSON if it isn't already in that format. |

**Key Points:**
- Data from any source: Azure Cognitive Search accepts data from any source provided in JSON format, with auto crawling support for selected data sources in Azure.
- Full text search and analysis: Azure Cognitive Search offers full text search capabilities supporting both simple query and full Lucene query syntax.
- AI powered search: Azure Cognitive Search has Azure AI capabilities built in for image and text analysis from raw content.
- Multi-lingual: Azure Cognitive Search offers linguistic analysis for 56 languages to intelligently handle phonetic matching or language-specific linguistics. Natural language processors available in...
- Geo-enabled: Azure Cognitive Search supports geo-search filtering based on proximity to a physical location.
- Configurable user experience: Azure Cognitive Search has several features to improve the user experience including autocomplete, autosuggest, pagination, and hit highlighting.
- Key Phrase Extraction: uses a pre-trained model to detect important phrases based on term placement, linguistic rules, proximity to other terms, and how unusual the term is within the source data.
- Text Translation Skill: uses a pre-trained model to translate the input text into various languages for normalization or localization use cases.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Enriched Data And Query Design

**TL;DR:** In today's digital era, data is more than just raw information – it's a strategic asset that, when properly harnessed, can drive innovation and transformation.

**Topics covered:**
- Enriched Data and Knowledge Store
- Creating Indexes in Azure
- Query Design
- Simple Query Requests
- Practice: Exploring Azure Cognitive Search Indexes
- Exercise: Enriched Data and Query Design

**Key Terms:**

| Term | Definition |
|------|-----------|
| Data Source | Persists connection information to source data, including credentials. A data source object is used exclusively with indexers. |
| Index | Physical data structure used for full text search and other queries. |
| Indexer | A configuration object specifying a data source, target index, an optional AI skillset, optional schedule, and optional configuration settings for error handling and base-64... |
| Skillset | A complete set of instructions for manipulating, transforming, and shaping content, including analyzing and extracting information from image files. Except for very simple and... |
| Knowledge store | Stores output from an AI enrichment pipeline in tables and blobs in Azure Storage for independent analysis or downstream processing. |
| Reminder | The exercises marked Practice are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |

**Key Points:**
- Table projections are used to structure the extracted data in a relational schema for querying and visualization
- Object projections are JSON documents that represent each data entity
- File projections are used to store extracted images in JPG format
- Azure SQL (database, managed instance, and SQL Server on an Azure VM)
- Azure Storage (Blob Storage, Table Storage, ADLS Gen2)
- Data Source: Persists connection information to source data, including credentials. A data source object is used exclusively with indexers.
- Index: Physical data structure used for full text search and other queries.
- Indexer: A configuration object specifying a data source, target index, an optional AI skillset, optional schedule, and optional configuration settings for error handling and base-64 encoding.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Fundamental Concepts Of Di

**TL;DR:** <edukamu-video content="/videos/devai-2-unit5-video.yaml"/>
<br>

**Topics covered:**
- Introduction to Document Intelligence
- Document Intelligence Capabilities
- Document Intelligence and AI
- Why is Document Intelligence Important for Beginning AI Developers?
- DI and Azure: Receipt Analysis
- Prebuilt Models
- Practice: Document Intelligence
- Exercise: Basics of Document Intelligence
- Scenario Exercise
- YRITYS: Taking it a Step Further

**Key Terms:**

| Term | Definition |
|------|-----------|
| Azure AI Document Intelligence | supports features that can analyze documents and forms with prebuilt and custom models. During the course of this unit, we’ll explore the main features within the service. |
| Natural Language Processing (NLP) | NLP enables machines to understand and interpret human language, making it possible to extract information, identify entities, and comprehend the context of textual content in... |
| Computer Vision | Computer vision is utilized to analyze and interpret visual information within documents, such as images or scanned pages. It enables the extraction of data from images and the... |
| Machine Learning | Machine learning algorithms are employed for tasks like document classification, sentiment analysis, and entity recognition. These algorithms can be trained on large datasets to... |
| Data Extraction Techniques | Document intelligence involves techniques for extracting structured data from unstructured documents, enabling the conversion of information into a format that can be easily... |
| Real-World Applications | Document intelligence has a wide range of real-world applications across various industries. From automating data entry and processing invoices to extracting insights from... |
| Versatility | Document intelligence techniques can be applied to different types of documents, including text-based files, images, PDFs, and more. This versatility makes it applicable to a... |
| Problem-Solving Skills | Working with document intelligence challenges developers to think critically about how to extract meaningful information from unstructured data. It enhances problem-solving skills... |
| Integration with Business Processes | Many businesses rely on handling vast amounts of document-based information. Document intelligence allows developers to create AI solutions that seamlessly integrate with existing... |
| Foundation for Advanced AI Projects | Document intelligence serves as a foundational knowledge area for more advanced AI projects. As developers progress in their AI journey, the skills learned in document... |

**Key Points:**
- Prebuilt models - pretrained models that have been built to process common document types such as invoices, business cards, ID documents, and more. These models are designed to recognize and extract...
- Custom models - can be trained to identify specific fields that are not included in the existing pretrained models.
- Document analysis - general document analysis that returns structured data representations, including regions of interest and their inter-relationships.
- customer and vendor details from invoices
- sales and transaction details from receipts
- identification and verification details from identity documents
- agreement and party details from contracts
- taxable compensation, mortgage interest, student loan details and more

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Summary

**TL;DR:** Congratulations on reaching the summary of the Exploring Artificial Intelligence course!

**Topics covered:**
- Conversation: Representing the World with Azure
- Unit 1: Getting Started with Azure AI
- Unit 2: Azure and Computer Vision
- Unit 3: Azure and Natural Language Processing
- Unit 4: Azure and Generative AI
- Unit 5: Azure and Document Intelligence
- Course Feedback

**Key Points:**
- How would you describe artificial intelligence?
- What is the difference between supervised and unsupervised learning?
- How would you describe computer vision?
- What are the main principles of facial recognition?
- How does character recognition differ from recognizing faces?
- What are the main principles of natural language processing?
- What do AI applications need in order to recognize conversations?
- What are the main AI Speech features offered in Microsoft Azure?

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Quick-Reference Glossary

| Term | Definition | Section |
|------|-----------|---------|
| Request | When you open the weather app, it sends a request to a Weather API, asking for the current weather data for your current location or another desired place. | Azure And Ai |
| API Response | The Weather API receives the request, fetches the latest weather information from its database, and sends back a response to your app. | Azure And Ai |
| Data Display | Your weather app takes the data received from the API and displays it beautifully on your screen – and that’s it! You know if you need an umbrella or sunglasses or even a pair of... | Azure And Ai |
| Multi-service resource | a resource created in the Azure portal that provides access to multiple Azure AI services with a single key and endpoint. Use the resource **Azure AI services** when you need... | Azure And Ai |
| Single-service resources | a resource created in the Azure portal that provides access to a single Azure AI service, such as Speech, Vision, Language, etc. Each Azure AI service has a unique key and... | Azure And Ai |
| API | application programming interfaces (APIs) enable software components to communicate, so one side can be updated without stopping the other from working. | Azure And Ai |
| Artificial Intelligence (AI) | computer programs that respond in ways that are normally associated with human reasoning, learning, and thought. | Azure And Ai |
| Azure AI services | a portfolio of AI services that can be incorporated into applications quickly and easily without specialist knowledge. Azure AI services is also the name for the multi-service... | Azure And Ai |
| Endpoint | the location of a resource, such as an Azure AI service. | Azure And Ai |
| Key | a private string that is used to authenticate a request. | Azure And Ai |
| Machine Learning | This is often the foundation for an AI system, and is the way we "teach" a computer model to make predictions and draw conclusions from data. | Fundamental Concepts Of Ai |
| Computer Vision | Capabilities within AI to interpret the world visually through cameras, video, and images. | Fundamental Concepts Of Ai |
| Natural Language Processing | Capabilities within AI for a computer to interpret written or spoken language, and respond in kind. | Fundamental Concepts Of Ai |
| Document Intelligence | Capabilities within AI that deal with managing, processing, and using high volumes of data found in forms and documents. | Fundamental Concepts Of Ai |
| Knowledge Mining | Capabilities within AI to extract information from large volumes of often unstructured data to create a searchable knowledge store. | Fundamental Concepts Of Ai |
| Generative AI | Capabilities within AI that create original content in a variety of formats including natural language, image, code, and more. | Fundamental Concepts Of Ai |
| Automated machine learning | this feature enables non-experts to quickly create an effective machine learning model from data. | Fundamental Concepts Of Ai |
| Azure Machine Learning designer | a graphical interface enabling no-code development of machine learning solutions. | Fundamental Concepts Of Ai |
| Data metric visualization | analyze and optimize your experiments with visualization. | Fundamental Concepts Of Ai |
| Notebooks | write and run your own code in managed Jupyter Notebook servers that are directly integrated in the studio. | Fundamental Concepts Of Ai |
| y = f(x) | 4.	Now that the *training* phase is complete, the trained model can be used for *inferencing*. The model is essentially a software program that encapsulates the function produced... | Introduction To Machine Learning |
| f(x) = x-50 | You can use this function to predict the number of ice creams sold on a day with any given temperature. For example, suppose the weather forecast tells us that tomorrow it will be... | Supervised Learning |
| Mean Absolute Error (MAE) | Imagine predicting ice cream sales; MAE measures the average of absolute errors, revealing how much each prediction deviates from reality. In our example, the mean of errors (2,... | Supervised Learning |
| Mean Squared Error (MSE) | MAE treats all errors equally, but MSE magnifies larger errors by squaring them. The mean of squared errors (4, 9, 9, 1, 4, and 9) in our scenario is 6. | Supervised Learning |
| Root Mean Squared Error (RMSE) | To interpret errors in the original quantity (ice creams), we take the square root of MSE. Here, √6 equals 2.45 (ice creams). | Supervised Learning |
| Coefficient of determination (R2) | R2 goes beyond error comparison. It gauges how much of the variance in results can be ascribed to the model rather than random fluctuations. In our ice cream model, an R2 of 0.95... | Supervised Learning |
| true | or **false**. In most real scenarios, the data observations used to train and validate the model consist of multiple feature (**x**) values and a **y** value that is either **1**... | Supervised Learning |
| f(x) = P(y=1 | x) | For three of the six observations in the training data, we know that **y** is definitely *true*, so the probability for those observations that y=1 is **1.0** and for the other... | Supervised Learning |
| f<sup>0</sup>(x) = P(y=0 | x) | * **f<sup>1</sup>(x) = P(y=1 \| x)** | Supervised Learning |
| f<sup>2</sup>(x) = P(y=2 | x) | Each algorithm produces a sigmoid function that calculates a probability value between 0.0 and 1.0. A model trained using this kind of algorithm predicts the class for the... | Supervised Learning |
| f(x) =[P(y=0|x), P(y=1|x), P(y=2|x)] | An example of this kind of function is a *softmax* function, which could produce an output like the following example: | Supervised Learning |
| Average distance to cluster center | How close, on average, each point in the cluster is to the centroid of the cluster. | Unsupervised Learning |
| Average distance to other center | How close, on average, each point in the cluster is to the centroid of all other clusters. | Unsupervised Learning |
| Maximum distance to cluster center | The furthest distance between a point in the cluster and its centroid. | Unsupervised Learning |
| Silhouette | A value between -1 and 1 that summarizes the ratio of distance between points in the same cluster and points in different clusters (The closer to 1, the better the cluster... | Unsupervised Learning |
| [37.3, 16.8, 19.2, 30.0] | 2.	The functions for the first layer of neurons each calculate a weighted sum by combining the **x** value and **w** weight, and pass it to an activation function that determines... | Unsupervised Learning |
| [0.2, 0.7, 0.1] | 5.	The elements of the vector represent the probabilities for classes 0, 1, and 2. The second value is the highest, so the model predicts that the species of the penguin is **1**... | Unsupervised Learning |
| face detection | and **face analysis**. | Ai And Facial Recognition |
| Accessories | indicates whether the given face has accessories. This attribute returns possible accessories including headwear, glasses, and mask, with confidence score between zero and one for... | Ai And Facial Recognition |
| Blur | how blurred the face is, which can be an indication of how likely the face is to be the main focus of the image. | Ai And Facial Recognition |
| Exposure | such as whether the image is underexposed or over exposed. This applies to the face in the image and not the overall image exposure. | Ai And Facial Recognition |
| Glasses | whether or not the person is wearing glasses. | Ai And Facial Recognition |
| Head pose | the face's orientation in a 3D space. | Ai And Facial Recognition |
| Mask | indicates whether the face is wearing a mask. | Ai And Facial Recognition |
| Noise | refers to visual noise in the image. If you have taken a photo with a high ISO setting for darker settings, you would notice this noise in the image. The image looks grainy or... | Ai And Facial Recognition |
| Occlusion | determines if there might be objects blocking the face in the image. | Ai And Facial Recognition |
| Please notice | that, in order to use the Face service, you must create one of the following types of resource in your Azure subscription: | Ai And Facial Recognition |
| Automated Item Recognition | * As you pick items from the shelf, overhead cameras equipped with Computer Vision identify each product through visual recognition. | Fundamental Concepts Of Computer Vision |
| Seamless Shopping Experience | * Toss your selected items into your bag, and the smart cart updates your digital tab. | Fundamental Concepts Of Computer Vision |
| Intelligent Payment Processing | * Ready to leave? No queues, no scanning. The store's payment system, powered by Computer Vision, effortlessly tallies your selections. | Fundamental Concepts Of Computer Vision |
| Automated Receipt Generation | * Your purchase is complete. A digital receipt is instantly generated, detailing your items and the total cost. | Fundamental Concepts Of Computer Vision |
| Benefits | * **Efficiency**: Say goodbye to long queues. The streamlined process enhances the shopping experience, saving time for both customers and retailers. | Fundamental Concepts Of Computer Vision |
| Accuracy | Computer Vision reduces the risk of errors in item identification and pricing, providing a highly accurate transaction process. | Fundamental Concepts Of Computer Vision |
| Personalized Offers | The system, aware of your preferences, can offer personalized discounts and recommendations based on your shopping history. Similar technologies are, of course, largely used... | Fundamental Concepts Of Computer Vision |
| Azure AI Vision | A specific resource for the Azure AI Vision service. Use this resource type if you don't intend to use any other Azure AI services, or if you want to track utilization and costs... | Fundamental Concepts Of Computer Vision |
| Pages | One for each page of text, including information about the page size and orientation. | Recognizing Characters With Ai |
| Lines | The lines of text on a page. | Recognizing Characters With Ai |
| Words | The words in a line of text, including the bounding box coordinates and text itself. | Recognizing Characters With Ai |
| Reminder | Here and there within these courses, you’ll find exercises marked *Practice*. They are not a mandatory requirement for completing this course since they may require technical... | Recognizing Characters With Ai |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. | Recognizing Characters With Ai |
| Speech recognition | the ability to detect and interpret spoken input | Azure And Ai Speech |
| Speech synthesis | the ability to generate spoken output | Azure And Ai Speech |
| Azure AI Speech | provides speech to text and text to speech capabilities through speech recognition and synthesis. You can use prebuilt and custom Speech service models for a variety of tasks,... | Azure And Ai Speech |
| Speech | resource - choose this resource type if you only plan to use Azure AI Speech, or if you want to manage access and billing for the resource separately from other services. | Azure And Ai Speech |
| Azure AI Language | service. One example using conversational language understanding is an application that's able to turn devices on and off based on speech. Many types of tasks involving command... | Conversational Language Understanding |
| fan | and **light** entities as being specific instances of a general **device** entity. | Conversational Language Understanding |
| TurnOn | intent that is related to these utterances. | Conversational Language Understanding |
| None | intent. You should consider always using the *None* intent to help handle utterances that do not map any of the utterances you have entered. The *None* intent is considered a... | Conversational Language Understanding |
| Text Understanding | NLP enables machines to understand and extract information from written texts, making it valuable for tasks like sentiment analysis, named entity recognition, and information... | Fundamental Concepts Of Nlp |
| Language Translation | NLP is instrumental in machine translation, facilitating the conversion of text from one language to another, breaking down language barriers. | Fundamental Concepts Of Nlp |
| Chatbots and Virtual Assistants | NLP powers chatbots and virtual assistants, enabling them to understand and respond to user queries in a conversational manner. Microsoft’s Copilot, released in late 2023, is an... | Fundamental Concepts Of Nlp |
| Summarization | NLP algorithms can summarize large volumes of text, condensing information while retaining essential details. | Fundamental Concepts Of Nlp |
| Search Engines | NLP enhances search engines by understanding user queries and providing more accurate and relevant results. | Fundamental Concepts Of Nlp |
| Named entity recognition | identifies people, places, events, and more. This feature can also be customized to extract custom categories. | Fundamental Concepts Of Nlp |
| Entity linking | identifies known entities together with a link to Wikipedia. | Fundamental Concepts Of Nlp |
| Question answering | supports natural language AI workloads that require an automated conversational element. Typically, question answering is used to build bot applications that respond to customer... | Question Answering |
| Example | A customer asks a chatbot, "How can I return a product?" The chatbot interprets the question, understands the context, and provides step-by-step instructions on the return process. | Question Answering |
| Language | resource in your Azure subscription.) | Question Answering |
| Note | While you can sign in with your work or school account, you will see a slightly different user experience compared to signing in with your personal account. Using your work or... | Ai And Copilots |
| GPT-4 models | are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code completions based on natural language prompts. | Azure Openai Services |
| GPT 3.5 models | can generate natural language and code completions based on natural language prompts. In particular, **GPT-35-turbo** models are optimized for chat-based interactions and work... | Azure Openai Services |
| Embeddings models | convert text into numeric vectors, and are useful in language analytics scenarios such as comparing text sources for similarities. | Azure Openai Services |
| DALL-E models | are used to generate images based on natural language prompts. Currently, DALL-E models are in preview. DALL-E models aren't listed in the Azure OpenAI Studio interface and don't... | Azure Openai Services |
| I heard a dog [bark] | Remember that the attention layer is working with numeric vector representations of the tokens, not the actual text. In a decoder, the process starts with a sequence of token... | Fundamentals Of Generative Ai |
| Data from any source | accepts data from any source provided in JSON format, with auto crawling support for selected data sources in Azure. | Azure Ai Search |
| Multiple options for search and analysis | including vector search, full text, and hybrid search. | Azure Ai Search |
| AI enrichment | has Azure AI capabilities built in for image and text analysis from raw content. | Azure Ai Search |
| Linguistic analysis | offers analysis for 56 languages to intelligently handle phonetic matching or language-specific linguistics. Natural language processors available in Azure AI Search are also used... | Azure Ai Search |
| Configurable user experience | has options for query syntax including vector queries, text search, hybrid queries, fuzzy search, autocomplete, geo-search filtering based on proximity to a physical location, and... | Azure Ai Search |
| Azure scale, security, and integration | at the data layer, machine learning layer, and with Azure AI services and Azure OpenAI. | Azure Ai Search |
| Indexer | automates the movement data from the data *source* through *document cracking* and *enrichment* to *indexing*. An indexer automates a portion of data ingestion and exports the... | Azure Ai Search |
| Document cracking | the indexer opens files and extracts content. | Azure Ai Search |
| Enrichment | the indexer moves data through AI enrichment, which implements Azure AI on your original data to extract more information. AI enrichment is achieved by adding and combining skills... | Azure Ai Search |
| Push to index | the serialized JSON data populates the search *index*. | Azure Ai Search |
| Full text search and analysis | Azure Cognitive Search offers full text search capabilities supporting both simple query and full Lucene query syntax. | Azure And Cognitive Search |
| AI powered search | Azure Cognitive Search has Azure AI capabilities built in for image and text analysis from raw content. | Azure And Cognitive Search |
| Multi-lingual | Azure Cognitive Search offers linguistic analysis for 56 languages to intelligently handle phonetic matching or language-specific linguistics. Natural language processors... | Azure And Cognitive Search |
| Geo-enabled | Azure Cognitive Search supports geo-search filtering based on proximity to a physical location. | Azure And Cognitive Search |
| Natural language processing skills | with these skills, unstructured text is mapped as searchable and filterable fields in an index. | Azure And Cognitive Search |
| Image processing skills | creates text representations of image content, making it searchable using the query capabilities of Azure Cognitive Search. | Azure And Cognitive Search |
| Push method | JSON data is pushed into a search index via either the REST API or the .NET SDK. Pushing data has the most flexibility as it has no restrictions on the data source type, location,... | Azure And Cognitive Search |
| Pull method | Search service indexers can pull data from popular Azure data sources, and if necessary, export that data into JSON if it isn't already in that format. | Azure And Cognitive Search |
| Data Source | Persists connection information to source data, including credentials. A data source object is used exclusively with indexers. | Enriched Data And Query Design |
| Index | Physical data structure used for full text search and other queries. | Enriched Data And Query Design |
| Skillset | A complete set of instructions for manipulating, transforming, and shaping content, including analyzing and extracting information from image files. Except for very simple and... | Enriched Data And Query Design |
| Knowledge store | Stores output from an AI enrichment pipeline in tables and blobs in Azure Storage for independent analysis or downstream processing. | Enriched Data And Query Design |
| Azure AI Document Intelligence | supports features that can analyze documents and forms with prebuilt and custom models. During the course of this unit, we’ll explore the main features within the service. | Fundamental Concepts Of Di |
| Natural Language Processing (NLP) | NLP enables machines to understand and interpret human language, making it possible to extract information, identify entities, and comprehend the context of textual content in... | Fundamental Concepts Of Di |
| Data Extraction Techniques | Document intelligence involves techniques for extracting structured data from unstructured documents, enabling the conversion of information into a format that can be easily... | Fundamental Concepts Of Di |
| Real-World Applications | Document intelligence has a wide range of real-world applications across various industries. From automating data entry and processing invoices to extracting insights from... | Fundamental Concepts Of Di |
| Versatility | Document intelligence techniques can be applied to different types of documents, including text-based files, images, PDFs, and more. This versatility makes it applicable to a... | Fundamental Concepts Of Di |
| Problem-Solving Skills | Working with document intelligence challenges developers to think critically about how to extract meaningful information from unstructured data. It enhances problem-solving skills... | Fundamental Concepts Of Di |
| Integration with Business Processes | Many businesses rely on handling vast amounts of document-based information. Document intelligence allows developers to create AI solutions that seamlessly integrate with existing... | Fundamental Concepts Of Di |
| Foundation for Advanced AI Projects | Document intelligence serves as a foundational knowledge area for more advanced AI projects. As developers progress in their AI journey, the skills learned in document... | Fundamental Concepts Of Di |

---

*Auto-generated by `generate_diary.py` — re-run to refresh after re-scraping.*
