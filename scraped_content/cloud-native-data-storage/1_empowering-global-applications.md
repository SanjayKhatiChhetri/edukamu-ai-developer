## Empowering Global Applications

In our modern, increasingly digital societies, endless amounts of data are being processed each day. As we've learned during the earlier courses of this micro degree, data is the backbone of all modern applications: be it your favorite weather app, a local event-sharing hub, or an international e-commerce platform, they all run on data.

In a world run by data, handling is has become critical. In an ideal situation, a single database would comfortably hold all the information necessary for running such services. In real life settings, though, this is not possible because the needs of every service, feature, and – especially – user, are wildly different.

Applications are no longer confined to local domains; they span the globe, serving users with diverse needs and expectations. One thing they all have in common is that they expect seamless, hassle-free user experiences around the clock on any device which, in turn, presents a huge challenge for the developing teams and especially their databases.

Do you still remember *relational* and *non-relational* databases from the third course? In essence, relational data is docile and organized, information that's a lot easier to manage than non-relational data. And, unfortunately, non-relational data is crucial for running global services, such as large e-commerce platforms.

The varying needs and expectations of a worldwide customer base present a challenge that's too difficult for a traditional database solution to handle. That's why we need something special, something *global*, *diverse*, and *scalable*.

In a bit more technical terms, we need globally distributed, multi-model database services. In practice we're talking about database services that enable us to run global applications and services smoothly and reliably.

That's the kind of service we'll be dealing with throughout this entire course. More specifically, we'll be focusing on Azure Cosmos DB, which, as the name implies, is the go-to solution for global application developers on Microsoft Azure.

Before leaping into the world of Azure Cosmos DB, we'll review a few more basic concepts. Or, to put it more concretely, why do we need services like Azure Cosmos DB? Let's explore four key capabilities, shall we?

<edukamu-tabs theme="edukamu-tabs1">

<edukamu-tabs-tab title="1. Global Accessibility">
**Scenario:** Consider a social media platform with users spanning continents. Users all around Asia, Europe, Africa, Oceania, and the Americas demand real-time updates and interactions. Traditional databases struggle with providing low-latency access to users worldwide.

**Solution:** Globally distributed databases, like Azure Cosmos DB, ensure that data is stored and served from multiple regions, reducing latency and enhancing user experience on a global scale. For developers, understanding how to implement such global accessibility is essential to cater to the diverse user base of modern applications.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="2. Diverse Data Models">
**Scenario:** Imagine a content management system handling articles, images, and user profiles. Each type of data requires a unique structure and handling method. A rigid, one-size-fits-all data model falls short. Most social media platforms, for example, rely on services like this.

**Solution:** Multi-model databases, such as Azure Cosmos DB, support various data models like document, key-value, graph, and column-family. This flexibility empowers developers to choose the most suitable data model for each aspect of their application, fostering efficiency and adaptability in the face of diverse data requirements.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="3. On-demand Scalability">
**Scenario:** Picture an e-commerce platform launching a flash sale, resulting in an overwhelming surge of user traffic. Traditional databases may struggle to scale rapidly, leading to performance issues and potential downtime due to lack of *scalability*.

Scalability, in the context of application development, refers to the ability of a system to handle increasing amounts of work, such as data processing or user requests, by efficiently and seamlessly expanding its resources.

**Solution:** Elastic scalability is a hallmark of services like Azure Cosmos DB. It allows developers to seamlessly scale resources, both in terms of throughput and storage, ensuring applications can handle varying workloads without compromising performance. Aspiring developers need to grasp this concept to build applications that can grow and adapt to unpredictable demands.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="4. Consistency Tailored to Needs">
**Scenario:** In a banking application processing money transaction, maintaining data integrity is paramount. On the other hand, a movie streaming service optimizing for low-latency access might prioritize speed over absolute consistency. Traditional database services might struggle trying to tick all the boxes.

**Solution:** Globally distributed databases offer different consistency models, allowing developers to align database behavior with specific application requirements. Aspiring developers must understand these models to strike the right balance between consistency, availability, and partition tolerance based on the needs of their applications.
</edukamu-tabs-tab>

</edukamu-tabs>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Global Accessibility
</edukamu-collapse-hidden-title>

**Scenario:** Consider a social media platform with users spanning continents. Users all around Asia, Europe, Africa, Oceania, and the Americas demand real-time updates and interactions. Traditional databases struggle with providing low-latency access to users worldwide.

**Solution:** Globally distributed databases, like Azure Cosmos DB, ensure that data is stored and served from multiple regions, reducing latency and enhancing user experience on a global scale. For developers, understanding how to implement such global accessibility is essential to cater to the diverse user base of modern applications.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Diverse Data Models
</edukamu-collapse-hidden-title>

**Scenario:** Imagine a content management system handling articles, images, and user profiles. Each type of data requires a unique structure and handling method. A rigid, one-size-fits-all data model falls short. Most social media platforms, for example, rely on services like this.

**Solution:** Multi-model databases, such as Azure Cosmos DB, support various data models like document, key-value, graph, and column-family. This flexibility empowers developers to choose the most suitable data model for each aspect of their application, fostering efficiency and adaptability in the face of diverse data requirements.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. On-demand Scalability
</edukamu-collapse-hidden-title>

**Scenario:** Picture an e-commerce platform launching a flash sale, resulting in an overwhelming surge of user traffic. Traditional databases may struggle to scale rapidly, leading to performance issues and potential downtime due to lack of *scalability*.

Scalability, in the context of application development, refers to the ability of a system to handle increasing amounts of work, such as data processing or user requests, by efficiently and seamlessly expanding its resources.

**Solution:** Elastic scalability is a hallmark of services like Azure Cosmos DB. It allows developers to seamlessly scale resources, both in terms of throughput and storage, ensuring applications can handle varying workloads without compromising performance. Aspiring developers need to grasp this concept to build applications that can grow and adapt to unpredictable demands.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 4. Consistency Tailored to Needs
</edukamu-collapse-hidden-title>

**Scenario:** In a banking application processing money transaction, maintaining data integrity is paramount. On the other hand, a movie streaming service optimizing for low-latency access might prioritize speed over absolute consistency. Traditional database services might struggle trying to tick all the boxes.

**Solution:** Globally distributed databases offer different consistency models, allowing developers to align database behavior with specific application requirements. Aspiring developers must understand these models to strike the right balance between consistency, availability, and partition tolerance based on the needs of their applications.

</edukamu-collapse>
<br> -->


This course contains a few quite technical topics, so understanding the basics is essential. With this in mind, please take enough time to focus on the fundamentals covered on this first page!

Next, we'll take a more concrete look at globally distributed, multi-model database services from the perspective of an imaginary online e-commerce platform, Omise, that operates worldwide.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Use Case: Data and Global E-commerce
</edukamu-collapse-hidden-title>

Omise is an international marketplace focusing on the art of tea. They have an active client base distributed all around the world. While Omise, with plans to grow, only has physical stores in India as of now, but they already cater to customers all over the world. This has led to significant problems, which has led Omise to, encouraged by dozens of success stories, turn to Azure Cosmos DB for help.

### Case 1: Latency in Global Sales

Customers in Canada, Ireland, and Jamaica are having trouble when accessing Omise's e-commerce platform hosted in India. They are experiencing delays in loading product pages and completing transactions, especially during peak hours.

Omise finds out that traditional databases, centralized in one location, struggle to provide swift responses to users accessing the platform from distant regions. The problem is technical, geographical, and logistical: the data is just too far away to be accessible quickly. Along the way, centralized databases might also lead to trouble with different rules and regulations of each area.

**Answer:** Omise employs Azure Cosmos DB's **Multi-region Write** feature. For example, the product details, frequently accessed from the US, are replicated in an Azure region closer to the US. This minimizes the latency for users in that region, ensuring quicker access to product information.

### Case 2: Data Availability

Customers in Europe attempting to view product pricing and availability may face inconsistencies due to delays in updating data across various servers. In essence, maintaining synchronized and up-to-date information for users worldwide is a challenge with a single, centralized database, pretty much like in the first case example.

**Answer:** Omise leverages Azure Cosmos DB's **Multi-region Read** capability. For instance, pricing information is replicated in European Azure regions, allowing customers in Europe to access localized and updated pricing data without relying solely on a central database.

### Case 3: Traffic Spikes

Omise announces a limited-time promotion, resulting in a surge of users trying to access the platform simultaneously, leading to slow response times and potential system failures.
Scenarios like this are common, since traditional databases struggle to scale rapidly, hindering the ability to handle sudden spikes in user activity effectively.

Omise has gained a reputation with their attractive flash sale campaigns, so the company turns to Azure Cosmos DB for a solution.

**Answer:** Omise takes advantage of Azure Cosmos DB's **Autoscale** feature. During a promotional event, the database dynamically scales resources, ensuring sufficient throughput to accommodate the increased demand and maintain a responsive e-commerce experience.

### Case 4: Problems Modernizing

As Omise expands its product offerings, introducing new data types like 3D models for augmented reality shopping experiences, the existing database schema becomes limiting. The company also has plans of implementing augmented reality (AR), which turns out to be completely impossible for the same data-related reasons.

Traditional databases with fixed schemas make it difficult to adapt to evolving data requirements without significant restructuring. This, in turn, would require massive investments.

**Answer:** Omise utilizes Azure Cosmos DB's **Schema-agnostic Indexing**. For instance, when integrating 3D models, the flexible schema allows for seamless inclusion without disrupting existing data structures, ensuring adaptability to evolving data needs.

In addressing these challenges, Azure Cosmos DB provides Omise with specific features designed for scenarios such as reducing latency through Multi-region Writes, ensuring data consistency with Multi-region Reads, handling scalability challenges with Autoscale, and maintaining data model flexibility through Schema-agnostic Indexing. These features collectively empower Omise to deliver a truly global and adaptable e-commerce experience.

Please remember, however, that the services and tools described above are just a fraction of Azure Cosmos DB's offerings.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
In conclusion, the need for globally distributed, multi-model database services is underlined by the dynamic nature of modern applications. Their role in achieving global accessibility, handling diverse data, scaling on demand, and tailoring consistency to application needs is crucial for all modern applications catering to customers all over the globe.

Every aspiring developer should grasp these concepts, as they form the foundation for building applications that meet the expectations of a connected, global audience. On this course, we'll get familiar with all the basic principles of these incredibly powerful services.

Before getting into the technical details, however, let’s spend a moment reviewing what we've just learned with the very first exercise of this course.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Global Applications, Global Solutions
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module1/empowering-global-applications-text-poll-1.yaml" id="z9huo99cs4tso9zc">

<edukamu-text-poll url="/exercises/module1/empowering-global-applications-text-poll-2.yaml" id="zfdye0uszlpdpreg">

<edukamu-text-poll url="/exercises/module1/empowering-global-applications-text-poll-3.yaml" id="fw0t3julk7ceo8pq">

<edukamu-text-poll url="/exercises/module1/empowering-global-applications-text-poll-4.yaml" id="glb5m0hbda7tn1jy">

<edukamu-text-poll url="/exercises/module1/empowering-global-applications-text-poll-5.yaml" id="br6kumtwaa18w93w">

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/1/empowering-global-applications?question=z9huo99cs4tso9zc">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

In our digital age, applications are no longer confined to a single location. Users span the globe, and the expectations for seamless, low-latency experiences have never been higher. This is where services like Azure Cosmos DB come into play.

On the next page, we'll start exploring Azure Cosmos DB in detail. We'll start from the very basics, so don't worry!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
