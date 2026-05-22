<edukamu-video content="/videos/devai-7-unit1-video.yaml"/>
<br>

## Getting Started with Azure AI Services

Welcome to the seventh and final course of this study program! This course is all about artificial intelligence and, more specifically, about empowering modern solutions with cutting-edge technologies like natural language processing and generative AI.

If you’ve already completed all the previous courses within this degree, as recommended, you should already have a solid foundation on which to keep building your understanding. As such, we’ll skip the more elemental explanations and jump right into topics that are a tad more challenging.

Don’t worry, though, you don’t have to be an Azure veteran to keep up with this course! 

In this first unit, we’ll focus on Azure AI Services. It’s a suite of cloud-based services and tools provided by Microsoft Azure, designed to enable developers and businesses to build, deploy, and manage AI-infused applications without requiring deep expertise in AI or data science.

Before we begin, let’s find out why Azure AI Services are so crucial for all Azure developers.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Why Study Azure AI Services?
</edukamu-collapse-hidden-title>

Azure AI Services include easily approachable solutions for implementing artificial intelligence and allow advanced developers to build models of their own. They’re, however, extremely useful for newcomers as well. Consider the following:

**1. Ease of Use:** Azure AI Services offers pre-built AI models and tools, making it easier for developers with basic knowledge of Azure and AI to integrate advanced AI capabilities into their applications. This accessibility accelerates the development process and lowers the barrier to entry for incorporating AI features.

**2. Wide Range of Services:** Azure AI Services encompasses various domains, including:

- Azure AI Services, which provides APIs for vision, speech, language, decision, and search, enabling features like speech recognition, language understanding, and computer vision in applications.

- Azure Machine Learning, a platform for building, training, and deploying machine learning models at scale, catering to both seasoned data scientists and developers just getting to know to machine learning.

- Azure Bot Services, which enables the creation of intelligent, conversational AI bots, useful in customer service, e-commerce, and internal company processes.

**3. Scalability and Integration:** As a cloud service, Azure AI is highly scalable, allowing applications to handle increased loads without the need for extensive infrastructure changes. It integrates seamlessly with other Azure services and tools, providing a comprehensive ecosystem for application development.

**4. Business Benefits:** Azure AI Services help businesses increase efficiency, reduce costs, and make data-driven decisions. AI-driven insights can lead to more informed business strategies, improved customer experiences, and competitive advantages in various industries.

**5. Innovation and Futureproofing:** As AI continues to evolve, Azure AI Services provide a platform for experimenting with and deploying the latest AI innovations, ensuring that applications remain relevant and cutting-edge.

### Practical Use Scenarios:

- **Healthcare:** Azure AI can be used to develop applications for patient data analysis, predicting patient risks, and providing personalized healthcare recommendations.
- **Retail:** Retailers can leverage AI for personalized customer recommendations, inventory management, and customer sentiment analysis.
- **Banking:** AI applications in banking include fraud detection, risk management, and customer service chatbots.

In summary, Azure AI Services is crucial for newcomers to Azure development as it offers a simplified yet powerful gateway to integrating AI capabilities into applications.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-orange">
As you can see, Azure AI Services includes a host of tools and techniques for creating all kinds of intelligent solutions for all kinds of business scenarios. Understanding these services will go a long way towards making you an Azure development professional!

We’re just getting started, but we’ve already encountered concepts like API and SDK. Please make sure that you understand the two before continuing – we’ve explored them in depth during this program, and they’ll be used a lot on this course as well.

Without further ado, let’s jump right in and get acquainted with Azure AI Services!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Preparing to Develop AI Solutions
</edukamu-collapse-hidden-title>

Artificial Intelligence (AI) is increasingly prevalent in the software applications we use every day; including digital assistants in our homes and cellphones, automotive technology in the vehicles that take us to work, and smart productivity applications that help us do our jobs when we get there.

So, what actually is artificial intelligence? We’ve explored this in great detail during this study program, but let’s take a quick recap, shall we?

There are many definitions; some technical, some philosophical; but in general terms, we tend to think of AI as software that exhibits one or more human-like capabilities. Consider the following:

**Visual perception** - The ability to use *computer* vision capabilities to accept, interpret, and process input from images, video streams, and live cameras.

**Text analysis and conversation** - The ability to use *natural language processing (NLP)* to not only "read", but also generate realistic responses and extract semantic meaning from text.

**Speech** - The ability to recognize speech as input and synthesize spoken output. The combination of speech capabilities together with the ability to apply NLP analysis of text enables a form of human-compute interaction that's become known as conversational AI, in which users can interact with AI agents (usually referred to as bots) in much the same way they would with another human.

**Decision making** - The ability to use past experience and learned correlations to assess situations and take appropriate actions. For example, recognizing anomalies in sensor readings and taking automated action to prevent failure or system damage.

These kinds of capabilities are increasingly within the reach of everyday software applications, helping make them more intuitive and useful in a wide variety of scenarios that previously existed only in the realms of science fiction.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### AI Terminology
</edukamu-collapse-hidden-title>

There are several related terms that people use when talking about artificial intelligence, so it's useful to have clear definitions for each.

<edukamu-image url="/graphics/module1/terminology.png" alt="Data science underpins machine learning, which underpins artificial intelligence.">
<br>

### Data Science

Data science is a discipline that focuses on the processing and analysis of data; applying statistical techniques to uncover and visualize relationships and patterns in the data, and defining experimental models that help explore those patterns.

For example, a data scientist might gather samples of data about the population of an endangered species in a geographical area and combine it with data about levels of industrialization and economic demographics in the same area. The data can then be analyzed, using statistical techniques to extrapolate from the samples to understand trends and relationships between human activities and wildlife, and test hypotheses using models that show the likely impact of human activity on the wildlife population. By doing so, the data scientists may help determine optimal policies that balance the need for economic wellbeing for the human population with the need for conservation of the endangered wildlife.

### Machine Learning

Machine learning is a subset of data science that deals with the training and validation of predictive models. Typically, a data scientist prepares the data and then uses it to train a model based on an algorithm that exploits the relationships between the features in the data to predict values for unknown labels.

For example, a data scientist might use the data they have collected to train a model that predicts the annual growth or decline in population of a species based on factors such as the number of nesting sites observed, the area of land designated as protected, the human population in the local area, the daily volume of traffic on local roads, and so on. This predictive model can then be used as a tool to evaluate plans for housing, infrastructure, and industrial development in the local area and assess their likely impact on the local wildlife.

### Artificial Intelligence

Artificial intelligence usually (but not always) builds on machine learning to create software that emulates one or more characteristics of human intelligence.

For example, balancing the need for wildlife conservation against economic development requires accurate monitoring of the population of the endangered species being protected. It may not be feasible to rely on human experts who can positively identify the animal in question, or to monitor a large area over a sufficient period of time to get an accurate count. Indeed, the presence of human observers may deter animals and prevent their detection.

In this case, a predictive model could be trained to analyze image data taken by motion-activated cameras in remote locations and predict whether a photograph contains a sighting of the animal. The model could then be used in a software application that responds to automated identification of animals to track animal sightings across a large geographical area, identifying areas with dense animal populations that may be candidates for protected status.

</edukamu-collapse>
<br>

Artificial intelligence is becoming more and more prominent in our modern societies, and by choosing to take on this course, you’ve also chosen to become one of the forerunners in this exciting field.

Before getting started, however, there are a few important factors that should be considered. Namely, we’re talking about responsibility.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Considering AI Integration and Responsibility
</edukamu-collapse-hidden-title>

Responsibility and ethics must be carefully considered when developing AI solutions. Consider the following topics.

### Fairness

AI systems should treat all people fairly. For example, suppose you create a machine learning model to support a loan approval application for a bank. The model should make predictions of whether or not the loan should be approved without incorporating any bias based on gender, ethnicity, or other factors that might result in an unfair advantage or disadvantage to specific groups of applicants.

Fairness of machine learned systems is a highly active area of ongoing research, and some software solutions exist for evaluating, quantifying, and mitigating unfairness in machine learned models. However, tooling alone isn't sufficient to ensure fairness. Consider fairness from the beginning of the application development process; carefully reviewing training data to ensure it's representative of all potentially affected subjects, and evaluating predictive performance for subsections of your user population throughout the development lifecycle.

### Reliability and Safety

AI systems should perform reliably and safely. For example, consider an AI-based software system for an autonomous vehicle; or a machine learning model that diagnoses patient symptoms and recommends prescriptions. Unreliability in these kinds of system can result in substantial risk to human life.

As with any software, AI-based software application development must be subjected to rigorous testing and deployment management processes to ensure that they work as expected before release. Additionally, software engineers need to take into account the probabilistic nature of machine learning models, and apply appropriate thresholds when evaluating confidence scores for predictions.

### Privacy and Security

AI systems should be secure and respect privacy. The machine learning models on which AI systems are based rely on large volumes of data, which may contain personal details that must be kept private. Even after models are trained and the system is in production, they use new data to make predictions or take action that may be subject to privacy or security concerns; so appropriate safeguards to protect data and customer content must be implemented.

### Inclusiveness

AI systems should empower everyone and engage people. AI should bring benefits to all parts of society, regardless of physical ability, gender, sexual orientation, ethnicity, or other factors.

One way to optimize for inclusiveness is to ensure that the design, development, and testing of your application includes input from as diverse a group of people as possible.

### Transparency

AI systems should be understandable. Users should be made fully aware of the purpose of the system, how it works, and what limitations may be expected.

For example, when an AI system is based on a machine learning model, you should generally make users aware of factors that may affect the accuracy of its predictions, such as the number of cases used to train the model, or the specific features that have the most influence over its predictions. You should also share information about the confidence score for predictions.

When an AI application relies on personal data, such as a facial recognition system that takes images of people to recognize them; you should make it clear to the user how their data is used and retained, and who has access to it.

### Accountability

People should be accountable for AI systems. Although many AI systems seem to operate autonomously, ultimately it's the responsibility of the developers who trained and validated the models they use, and defined the logic that bases decisions on model predictions to ensure that the overall system meets responsibility requirements. To help meet this goal, designers and developers of AI-based solution should work within a framework of governance and organizational principles that ensure the solution meets ethical and legal standards that are clearly defined.

</edukamu-collapse>
<br>

We’ll review ethics and responsible AI practices in depth later, but these aspects should be kept in mind throughout this course. As AI developers, we possess great power, but it does come with certain responsibilities.

Next, let’s continue our tour of Azure AI Services by reviewing a few main capabilities.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Machine Learning
</edukamu-collapse-hidden-title>

Microsoft Azure provides the Azure Machine Learning service - a cloud-based platform for running experiments at scale to train predictive models from data and publish the trained models as services.

<edukamu-image url="/graphics/module1/azure-machine-learning.png" alt="A conceptual diagram of Azure Machine Learning with data being used in an experiment to train a predictive model.">
<br>

Azure Machine Learning provides the following features and capabilities:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
**Feature**
</edukamu-table-header>
<edukamu-table-header width="70%">
**Capability**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Automated machine learning
</edukamu-table-cell>
<edukamu-table-cell>
This feature enables non-experts to quickly create an effective machine learning model from data.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Azure Machine Learning designer
</edukamu-table-cell>
<edukamu-table-cell>
A graphical interface enabling no-code development of machine learning solutions.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Data and compute management
</edukamu-table-cell>
<edukamu-table-cell>
Cloud-based data storage and compute resources that professional data scientists can use to run data experiment code at scale.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Pipelines
</edukamu-table-cell>
<edukamu-table-cell>
Data scientists, software engineers, and IT operations professionals can define pipelines to orchestrate model training, deployment, and management tasks.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section>
<br>

Data scientists can use Azure Machine Learning throughout the entire machine learning lifecycle to:

- Ingest and prepare data.
- Run experiments to explore data and train predictive models.
- Deploy and manage trained models as web services.

Software engineers may interact with Azure Machine Learning in the following ways:

- Using Automated Machine Learning or Azure Machine Learning designer to train machine learning models and deploy them as services that can be integrated into AI-enabled applications.
- Collaborating with data scientists to deploy models based on common frameworks such as Scikit-Learn, PyTorch, and TensorFlow as web services, and consume them in applications.
- Using Azure Machine Learning SDKs or command-line interface (CLI) scripts to orchestrate DevOps processes that manage versioning, deployment, and testing of machine learning models as part of an overall application delivery solution.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure AI Services
</edukamu-collapse-hidden-title>

Azure AI Services are cloud-based services that encapsulate AI capabilities. Rather than a single product, you should think of Azure AI Services as a set of individual services that you can use as building blocks to compose sophisticated, intelligent applications.

Azure AI services offer a wide range of prebuilt AI capabilities across multiple categories, with examples shown in the following table.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Natural language processing**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Knowledge mining and document intelligence**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Computer vision**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Decision support**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Generative AI**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Text analysis
</edukamu-table-cell>
<edukamu-table-cell>
AI Search
</edukamu-table-cell>
<edukamu-table-cell>
Image analysis
</edukamu-table-cell>
<edukamu-table-cell>
Content safety
</edukamu-table-cell>
<edukamu-table-cell>
Azure OpenAI Service
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Question answering
</edukamu-table-cell>
<edukamu-table-cell>
Document Intelligence
</edukamu-table-cell>
<edukamu-table-cell>
Video analysis
</edukamu-table-cell>
<edukamu-table-cell>
Content moderation
</edukamu-table-cell>
<edukamu-table-cell>
DALL-E image generation
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Language understanding
</edukamu-table-cell>
<edukamu-table-cell>
Custom Document Intelligence
</edukamu-table-cell>
<edukamu-table-cell>
Image classification
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Translation
</edukamu-table-cell>
<edukamu-table-cell>
Custom skills
</edukamu-table-cell>
<edukamu-table-cell>
Object detection
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Named entity recognition
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
Facial analysis
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Custom text classification
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
Optical character recognition
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Speech
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>
Azure AI Video Indexer
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Speech Translation
</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
<edukamu-table-cell>

</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section
<edukamu-section class="edukamu-included-only-in-mobile">
<edukamu-section class="edukamu-kuvateksti">
The Table above is horizontally scrollable.
</edukamu-section>
</edukamu-section>
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Bot Service
</edukamu-collapse-hidden-title>

Generative AI is a relatively new and quickly progressing field of AI focused on AI models that generate content. Content that these models generate can be in the form of text, images, code or more, and in a way that almost feels like interacting with a real person in a real conversation. Generative AI models depend on large language models (LLMs) based on the transformer architecture that evolved from years of machine learning progress. Generative AI models are often queried with natural language prompts, and return an impressively accurate response when prompted correctly.

Azure OpenAI Service is an Azure AI service for deploying, utilizing, and fine-tuning models developed by OpenAI. OpenAI, the company who built ChatGPT, is one of the most popular applications most people have seen, and the models behind that ChatGPT uses are available through the Azure OpenAI Service. You can develop applications that use the powerful generative AI models in Azure OpenAI to further utilize this technology.

AI engineers can develop applications that use the powerful generative AI models in Azure OpenAI to further utilize this technology. Both REST and language specific SDKs are available when developing applications.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure AI Search
</edukamu-collapse-hidden-title>

Searching for information is a common requirement in many applications, from dedicated search engine web sites to mobile apps that can find context-appropriate information based on where you are and what you want to accomplish.

<edukamu-image url="graphics/module1/cognitive-search.png" alt="Diagram of a search solution using AI services to extract insights from data and create an index for search.">
<br>

Azure AI Search is an Applied AI Service that enables you to ingest and index data from various sources, and search the index to find, filter, and sort information extracted from the source data.

In addition to basic text-based indexing, Azure AI Search enables you to define an enrichment pipeline that uses AI skills to enhance the index with insights derived from the source data - for example, by using computer vision and natural language processing capabilities to generate descriptions of images, extract text from scanned documents, and determine key phrases in large documents that encapsulate their key points.

Not only does this AI enrichment produce a more useful search experience, the insights extracted by your enrichment pipeline can be persisted in a knowledge store for further analysis or integration into a data pipeline for a business intelligence solution.

</edukamu-collapse>
<br>


We won’t cover all the above services on this course, but it’s good to know about their existence. As you know, all Azure services are tied together in one way or another, and the same principle also applies for its AI capabilities.

We have a lot to cover on this course, so let’s take a moment to gather our thoughts at this stage. And what better way to do it than with a handy little exercise!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Introduction to Azure AI Services
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/getting-started-with-azure-ai-services-question-scroll-1.yaml" id="r4wux5jkczv7ckq0">
<br>

</edukamu-collapse>

Now that we’ve reviewed the basics of Azure AI Services, let’s move right along and start using them, shall we? First, we’ll need to learn how such services are enabled.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
