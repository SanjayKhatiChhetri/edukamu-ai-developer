## Azure and AI

By this stage, you should already have quite a comprehensive understanding of both Azure and AI. On their own, they're already amazing services, but imagine them combined...

With Azure at your fingertips, you can unleash the power of artificial intelligence and create your own tech marvels. Want to build a smart app that recognizes your voice? Azure's got you covered. Dreaming of a world-changing AI that helps doctors diagnose diseases? Azure's got the power.

Whether you're interested in coding, data science, or just cool things, Azure and AI are your tools to turn dreams into reality. Let's start exploring them, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure AI Services
</edukamu-collapse-hidden-title>

Azure AI services are AI capabilities that can be built into web or mobile applications, in a way that's straightforward to implement. These AI services include image recognition, natural language processing, speech, AI-powered search, and more. There are over a dozen different services that can be used separately or together to add AI power to applications.

Let's take a look at some examples of what can be done with Azure AI services. The Azure AI Content Safety service can be used to detect harmful content within text or images, including violent or hateful content, and report on its severity. The Azure AI Language service can be used to summarize text, classify information, or extract key phrases. The Azure AI Speech service provides powerful speech to text and text to speech capabilities, allowing speech to be accurately transcribed into text, or text to natural sounding voice audio.

Azure AI services are based on three principles that dramatically improve speed-to-market:
* Prebuilt and ready to use
* Accessed through APIs
* Available on Azure


### Prebuilt and Ready to Go

AI has been prohibitive for all but the largest technology companies because of several factors, including the large amounts of data required to train models, the massive amount of computing power needed, and the budget to hire specialist programmers. Azure AI services make AI accessible to businesses of all sizes by using pre-trained machine learning models to deliver AI as a service. Azure AI services use high-performance Azure computing to deploy advanced AI models as resources, making decades of research available to developers of all skill levels.

Azure AI services are a portfolio of services, with capabilities suitable for use cases across sectors and industries.

For example, in education, Immersive Reader is being used to support students by adapting to their requirements. Learners can have varying needs, such as wanting to read more slowly, get words or text translated into another language, or see pictures to aid their understanding. Immersive Reader helps students with different needs learn at their own pace, and in their own way.

While Azure AI services can be used without any modification, some AI services can be customized to better fit specific requirements. Customization capabilities in Azure AI Vision, Azure AI Speech, and Azure OpenAI all allow you to add data to existing models.

For example, in sport, athletes, and coaches are customizing Azure AI Vision to improve performance and reduce injury. One application allows surfers to upload a video and receive AI-generated insights and analysis. These insights can then be used by coaches, medics, judges, and event broadcasters.

</edukamu-collapse>
<br>


Azure AI Services are accessible through APIs, or Application Programming Interfaces, with the goal of making them available with minimal coding.

Application Programming Interfaces, are like digital bridges that enable different software systems to communicate and share information. They define a set of rules and protocols that allow one piece of software to interact with another, providing a standardized way for developers to access the functionalities of a system, service, or application.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Example: APIs and Weather Apps
</edukamu-collapse-hidden-title>

If you've just heard about APIs for the first time, the following example might help you understand their importance a bit better.

Imagine you have a weather app on your phone. When you check the weather for your location, the app doesn't have a tiny meteorologist inside predicting the forecast; it relies on a Weather API instead.

Here's how it works:
1. **Request**: When you open the weather app, it sends a request to a Weather API, asking for the current weather data for your current location or another desired place.
2. **API Response**: The Weather API receives the request, fetches the latest weather information from its database, and sends back a response to your app.
3. **Data Display**: Your weather app takes the data received from the API and displays it beautifully on your screen – and that’s it! You know if you need an umbrella or sunglasses or even a pair of skis.

In this scenario, the Weather API acts as the bridge, allowing your weather app to access and use up-to-date information without having to store all that data itself. APIs facilitate this seamless communication, making our digital experiences richer and more connected.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
To put it shortly, APIs make it possible for applications to talk to each other, allowing them to request and exchange data seamlessly.

Azure AI services, much like most other Azure tools and services, are used as resources. In practice this means that you'll need to create a resource to take advantage of each of them. In practice, it’s a simple ordeal.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Activating Azure AI Services
</edukamu-collapse-hidden-title>

Azure AI services are cloud-based, and like all Azure services you need to create a resource to use them. There are two types of AI service resources: multi-service or single-service. Your development requirements and how you want costs to be billed determine the types of resources you need.

* **Multi-service resource**: a resource created in the Azure portal that provides access to multiple Azure AI services with a single key and endpoint. Use the resource **Azure AI services** when you need several AI services or are exploring AI capabilities. When you use an Azure AI services resource, all your AI services are billed together.
* **Single-service resources**: a resource created in the Azure portal that provides access to a single Azure AI service, such as Speech, Vision, Language, etc. Each Azure AI service has a unique key and endpoint. These resources might be used when you only require one AI service or want to see cost information separately.

You can create a resource several ways, such as in the Azure portal. Most AI services have a free price tier to allow you to explore their capabilities.

After creating an Azure AI service resource, you can build applications using the REST API, software development kits (SDKs), or visual studio interfaces.

<edukamu-image url="/graphics/module1/azure-studio-examples.png" alt="Screenshot of several examples of Azure studios including Azure Language Studio, Azure OpenAI Studio, and Azure Vision Studio." modal="true"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<edukamu-section class="edukamu-kuvateksti">
You can click the image to view a bigger version.
</edukamu-section>
<br> 

Studio interfaces provide a friendly user interface to explore Azure AI services. There are different studios for different Azure AI services, such as Vision Studio, Language Studio, Speech Studio, and the Content Safety Studio. You can test out Azure AI services using the samples provided, or experiment with your own content. A studio-based approach allows you to explore, demo, and evaluate Azure AI services regardless of your experience with AI or coding.

When you use a studio interface with Azure AI services, your credentials are authenticated when you sign in, and a similar process is happening in the background. This is just one example of how Azure ensures the security of each piece of data it processes so that you can use it without a care.

</edukamu-collapse>
<br>


Azure is full of different tools and services leveraging artificial intelligence. They are available as resources on the Azure platform and include tools like Language, Speech, Vision, Decision, Cognitive Search, and Azure OpenAI.

To summarize this topic, let's review a few important concepts. They'll come in handy later!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure AI Terminology
</edukamu-collapse-hidden-title>

* **API** – application programming interfaces (APIs) enable software components to communicate, so one side can be updated without stopping the other from working.
* **Artificial Intelligence (AI)** – computer programs that respond in ways that are normally associated with human reasoning, learning, and thought.
* **Azure AI services** – a portfolio of AI services that can be incorporated into applications quickly and easily without specialist knowledge. Azure AI services is also the name for the multi-service resource created in the Azure portal that provides access to several different Azure AI services with a single key and endpoint.
* **Endpoint** – the location of a resource, such as an Azure AI service.
* **Key** – a private string that is used to authenticate a request.
* **Machine learning** – the ability for computer programs to learn from large amounts of data, in a process known as "training".
* **Multi-service resource** – the AI service resource created in the Azure portal that provides access to a bundle of AI services.
* **Single-service resource** – a resource created in the Azure portal that provides access to a single Azure AI service, such as Speech, Vision, Language, etc. Each Azure AI service has a unique key and endpoint.
* **RESTful API** – a scalable web application programming interface used to access Azure AI services.

</edukamu-collapse>
<br>


If you ever run across a term you don’t recognize, make sure to circle back here. You just might find some help!

Are you ready for the last exercise of the first unit? Feel free to recap a little before tackling it!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Azure and AI
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/azure-and-ai-question-scroll.yaml" id="d9t2729o479lz0yo">
<br>

</edukamu-collapse>
<br>


You've now completed the first unit of this course – good job!

Take a little break before moving on to the second unit. It's all about an Azure technology called Computer Vision, which is an exciting one!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3-4-5.png" alt="Edukamu-progress-in-a-module-image">
