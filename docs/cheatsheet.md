---
title: "Cheat Sheet"
layout: default
nav_order: 2
description: "Cross-course quick reference"
---

# Cheat Sheet

One-page quick reference across all 7 courses. `Ctrl+F` is your friend.

---

## Course 1: Exploring Microsoft Azure

**Key Terms:**
- **Be ready for the future:** Continuous innovation from Microsoft supports your development today and your product visions for tomorrow.
- **Build on your terms:** You have choices. With a commitment to open source, and support for all languages and frameworks, you can build how you...
- **Operate hybrid seamlessly:** On-premises, in the cloud, and at the edge, we'll meet you where you are. Integrate and manage your environments with...
- **When extending your datacenter to the cloud:** An organization can extend the capabilities of its own on-premises network by creating a virtual network in Azure and...
- **During disaster recovery:** As with running certain types of applications in the cloud and extending an on-premises network to the cloud, you can...
- **Note:** Some services or virtual machine (VM) features are only available in certain regions, such as specific VM sizes or...
- **Important to notice:** To ensure resiliency, a minimum of three separate availability zones are present in all availability zone-enabled...
- **Zonal services:** You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
- **Important:** You can't use Azure DNS to buy a domain name. For an annual fee, you can buy a domain name by using App Service domains...
- **Authentication:** This includes verifying identity to access applications and resources. It also includes providing functionality such as...
- **Single sign-on:** Single sign-on (SSO) enables you to remember only one username and one password to access multiple applications. A...
- **Application management:** You can manage your cloud and on-premises apps by using Azure AD. Features like Application Proxy, SaaS apps, the My...
- **Unified migration platform:** A single portal to start, run, and track your migration to Azure.
- **Range of tools:** A range of tools for assessment and migration. Azure Migrate tools include Azure Migrate: Discovery and assessment and...
- **Assessment and migration:** In the Azure Migrate hub, you can assess and migrate your on-premises infrastructure to Azure.
- **Shared access:** Azure file shares support the industry standard SMB and NFS protocols, meaning you can seamlessly replace your...
- **Fully managed:** Azure file shares can be created without the need to manage hardware or an OS. This means you don't have to deal with...
- **Scripting and tooling:** PowerShell cmdlets and Azure CLI can be used to create, mount, and manage Azure file shares as part of the...
- **Budget alerts:** Budget alerts notify you when spending, based on usage or cost, reaches or exceeds the amount defined in the alert...
- **Credit alerts:** Credit alerts notify you when your Azure credit monetary commitments are consumed.
- **Department spending quota alerts:** Department spending quota alerts notify you when department spending reaches a fixed threshold of the quota.
- **Reliability:** is used to ensure and improve the continuity of your business-critical applications.
- **Security:** is used to detect threats and vulnerabilities that might lead to security breaches.
- **Performance:** is used to improve the speed of your applications.

**Key Facts:**
- Lift-and-shift migration: You’re setting up cloud resources similar to your on-prem datacenter, and then simply moving the things running on-prem to r
- Testing and development: You have established configurations for development and test environments that you need to rapidly replicate. You can start u
- Total control over the operating system (OS).
- The ability to run custom software.
- Create a hierarchy that applies a policy. You could limit VM locations to the US West Region in a group called Production. This policy will inherit on
- Provide user access to multiple subscriptions. By moving multiple subscriptions under a management group, you can create one Azure role-based access c
- Zonal services: You pin the resource to a specific zone (for example, VMs, managed disks, IP addresses).
- Zone-redundant services: The platform replicates automatically across zones (for example, zone-redundant storage, SQL Database).
- communicating between Azure resources
- communicating with on-premises resources
- IT administrators. Administrators can use Azure AD to control access to applications and resources based on their business requirements.
- App developers. Developers can use Azure AD to provide a standards-based approach for adding functionality to applications that they build, such as ad
- How your data is replicated in the primary region.
- Whether your data is replicated to a second region that is geographically distant to the primary region, to protect against regional disasters.
- empower users to be productive wherever and whenever
- protect the organization's assets.
- Unified migration platform: A single portal to start, run, and track your migration to Azure.
- Range of tools: A range of tools for assessment and migration. Azure Migrate tools include Azure Migrate: Discovery and assessment and Azure Migrate: 
- Durability and availability. Redundancy ensures that your data is safe if transient hardware failures occur. You can also opt to replicate data across
- Security. All data written to an Azure storage account is encrypted by the service. Azure Storage provides you with fine-grained control over who has 
- Budget alerts: Budget alerts notify you when spending, based on usage or cost, reaches or exceeds the amount defined in the alert condition of the bud
- Credit alerts: Credit alerts notify you when your Azure credit monetary commitments are consumed.
- Delete means authorized users can still read and modify a resource, but they can't delete the resource.
- ReadOnly means authorized users can read a resource, but they can't delete or update the resource. Applying this lock is similar to restricting all au
- Manage your infrastructure through declarative templates rather than scripts. A Resource Manager template is a JSON file that defines what you want to
- Deploy, manage, and monitor all the resources for your solution as a group, rather than handling these resources individually.
- build, manage, and monitor everything from simple web apps to complex cloud deployments
- create custom dashboards for an organized view of resources
- How would you describe Azure in a few sentences?
- Can you describe the infrastructure of Azure?

---

## Course 2: Exploring Artificial Intelligence

**Key Terms:**
- **Request:** When you open the weather app, it sends a request to a Weather API, asking for the current weather data for your...
- **API Response:** The Weather API receives the request, fetches the latest weather information from its database, and sends back a...
- **Data Display:** Your weather app takes the data received from the API and displays it beautifully on your screen – and that’s it! You...
- **Machine Learning:** This is often the foundation for an AI system, and is the way we "teach" a computer model to make predictions and draw...
- **Computer Vision:** Capabilities within AI to interpret the world visually through cameras, video, and images.
- **Natural Language Processing:** Capabilities within AI for a computer to interpret written or spoken language, and respond in kind.
- **y = f(x):** 4.	Now that the *training* phase is complete, the trained model can be used for *inferencing*. The model is essentially...
- **f(x) = x-50:** You can use this function to predict the number of ice creams sold on a day with any given temperature. For example,...
- **Mean Absolute Error (MAE):** Imagine predicting ice cream sales; MAE measures the average of absolute errors, revealing how much each prediction...
- **Mean Squared Error (MSE):** MAE treats all errors equally, but MSE magnifies larger errors by squaring them. The mean of squared errors (4, 9, 9,...
- **Average distance to cluster center:** How close, on average, each point in the cluster is to the centroid of the cluster.
- **Average distance to other center:** How close, on average, each point in the cluster is to the centroid of all other clusters.
- **Maximum distance to cluster center:** The furthest distance between a point in the cluster and its centroid.
- **face detection:** and **face analysis**.
- **Accessories:** indicates whether the given face has accessories. This attribute returns possible accessories including headwear,...
- **Blur:** how blurred the face is, which can be an indication of how likely the face is to be the main focus of the image.
- **Automated Item Recognition:** * As you pick items from the shelf, overhead cameras equipped with Computer Vision identify each product through visual...
- **Seamless Shopping Experience:** * Toss your selected items into your bag, and the smart cart updates your digital tab.
- **Intelligent Payment Processing:** * Ready to leave? No queues, no scanning. The store's payment system, powered by Computer Vision, effortlessly tallies...
- **Pages:** One for each page of text, including information about the page size and orientation.
- **Lines:** The lines of text on a page.
- **Words:** The words in a line of text, including the bounding box coordinates and text itself.
- **Speech recognition:** the ability to detect and interpret spoken input
- **Speech synthesis:** the ability to generate spoken output
- **Azure AI Speech:** provides speech to text and text to speech capabilities through speech recognition and synthesis. You can use prebuilt...
- **Azure AI Language:** service. One example using conversational language understanding is an application that's able to turn devices on and...
- **fan:** and **light** entities as being specific instances of a general **device** entity.
- **TurnOn:** intent that is related to these utterances.
- **Text Understanding:** NLP enables machines to understand and extract information from written texts, making it valuable for tasks like...
- **Language Translation:** NLP is instrumental in machine translation, facilitating the conversion of text from one language to another, breaking...
- **Chatbots and Virtual Assistants:** NLP powers chatbots and virtual assistants, enabling them to understand and respond to user queries in a conversational...
- **Question answering:** supports natural language AI workloads that require an automated conversational element. Typically, question answering...
- **Example:** A customer asks a chatbot, "How can I return a product?" The chatbot interprets the question, understands the context,...
- **Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require...
- **Note:** While you can sign in with your work or school account, you will see a slightly different user experience compared to...
- **GPT-4 models:** are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code...
- **GPT 3.5 models:** can generate natural language and code completions based on natural language prompts. In particular, **GPT-35-turbo**...
- **Embeddings models:** convert text into numeric vectors, and are useful in language analytics scenarios such as comparing text sources for...
- **I heard a dog [bark]:** Remember that the attention layer is working with numeric vector representations of the tokens, not the actual text. In...
- **Data from any source:** accepts data from any source provided in JSON format, with auto crawling support for selected data sources in Azure.
- **Multiple options for search and analysis:** including vector search, full text, and hybrid search.
- **AI enrichment:** has Azure AI capabilities built in for image and text analysis from raw content.
- **Full text search and analysis:** Azure Cognitive Search offers full text search capabilities supporting both simple query and full Lucene query syntax.
- **AI powered search:** Azure Cognitive Search has Azure AI capabilities built in for image and text analysis from raw content.
- **Data Source:** Persists connection information to source data, including credentials. A data source object is used exclusively with...
- **Index:** Physical data structure used for full text search and other queries.
- **Indexer:** A configuration object specifying a data source, target index, an optional AI skillset, optional schedule, and optional...
- **Azure AI Document Intelligence:** supports features that can analyze documents and forms with prebuilt and custom models. During the course of this unit,...
- **Natural Language Processing (NLP):** NLP enables machines to understand and interpret human language, making it possible to extract information, identify...

**Key Facts:**
- Multi-service resource: a resource created in the Azure portal that provides access to multiple Azure AI services with a single key and endpoint. Use 
- Single-service resources: a resource created in the Azure portal that provides access to a single Azure AI service, such as Speech, Vision, Language, 
- Machine Learning: This is often the foundation for an AI system, and is the way we "teach" a computer model to make predictions and draw conclusions f
- Computer Vision: Capabilities within AI to interpret the world visually through cameras, video, and images.
- The proprietor of an ice cream store might use an app that combines historical sales and weather records to predict how many ice creams they're likely
- A doctor might use clinical data from past patients to run automated tests that predict whether a new patient is at risk from diabetes based on factor
- f<sup>0</sup>(x) = P(y=0 | x)
- f<sup>1</sup>(x) = P(y=1 | x)
- Average distance to cluster center: How close, on average, each point in the cluster is to the centroid of the cluster.
- Average distance to other center: How close, on average, each point in the cluster is to the centroid of all other clusters.
- Security - facial recognition can be used in building security applications, and increasingly it is used in smart phones operating systems for unlocki
- Social media - facial recognition can be used to automatically tag known friends in photographs.
- Toss your selected items into your bag, and the smart cart updates your digital tab.
- Computer Vision algorithms continuously analyze the contents of your cart in real-time.
- Pages - One for each page of text, including information about the page size and orientation.
- Lines - The lines of text on a page.
- Speech recognition - the ability to detect and interpret spoken input
- Speech synthesis - the ability to generate spoken output
- Azure AI Language: A resource that enables you to build apps with industry-leading natural language understanding capabilities without machine learnin
- Azure AI services: A general resource that includes conversational language understanding along with many other Azure AI services. You can only use th
- A social media feed analyzer that detects sentiment for a product marketing campaign.
- A document search application that summarizes documents in a catalog.
- Generated from an existing FAQ document or web page.
- GPT-4 models are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code completions based on natura
- GPT 3.5 models can generate natural language and code completions based on natural language prompts. In particular, GPT-35-turbo models are optimized 
- Determining *sentiment* or otherwise classifying natural language text.
- Comparing multiple text sources for semantic similarity.
- Generating content that is offensive, pejorative, or discriminatory.
- Generating content that contains factual inaccuracies.
- Data from any source: accepts data from any source provided in JSON format, with auto crawling support for selected data sources in Azure.
- Multiple options for search and analysis: including vector search, full text, and hybrid search.
- Data from any source: Azure Cognitive Search accepts data from any source provided in JSON format, with auto crawling support for selected data source
- Full text search and analysis: Azure Cognitive Search offers full text search capabilities supporting both simple query and full Lucene query syntax.
- Table projections are used to structure the extracted data in a relational schema for querying and visualization
- Object projections are JSON documents that represent each data entity
- Prebuilt models - pretrained models that have been built to process common document types such as invoices, business cards, ID documents, and more. Th
- Custom models - can be trained to identify specific fields that are not included in the existing pretrained models.
- How would you describe artificial intelligence?
- What is the difference between supervised and unsupervised learning?

---

## Course 3: Exploring Data and Analytics

**Key Terms:**
- **Database administrators:** manage databases, assigning permissions to users, storing backup copies of data and restore data in the event of a...
- **Data engineers:** manage infrastructure and processes for data integration across the organization, applying data cleaning routines,...
- **Data analysts:** explore and analyze data to create visualizations and charts that enable organizations to make informed decisions.
- **1. Key-value databases:** in which each record consists of a unique key and an associated value, which can be in any format.
- **Atomicity:** each transaction is treated as a single unit, which succeeds completely or fails completely. For example, a transaction...
- **Consistency:** transactions can only take the data in the database from one valid state to another. To continue the debit and credit...
- **Note:** JSON is just one of many ways in which semi-structured data can be represented. The point here is not to provide a...
- **Hierarchical Namespace:** option of an Azure Storage account. You can do this when initially creating the storage account, or you can upgrade an...
- **Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require...
- **Relational Data:** * **Structure**: Organized into tables with predefined schema.
- **Schema:** Strict and fixed structure, enforced by the database.
- **Relationships:** Emphasizes relationships between tables using primary and foreign keys.
- **find:** method to query the **products** collection in the **db** object:
- **Employees:** table like this:
- **DROP:** to accomplish almost everything that you need to do with a database. Although these SQL statements are part of the SQL...
- **Warning:** The DROP statement is very powerful. When you drop a table, all the rows in that table are lost. Unless you have a...
- **Clarity and Simplicity:** * **Principle**: Keep it simple. Avoid unnecessary complexity that can confuse the audience.
- **Why it matters:** Simplicity enhances understanding, ensuring that the audience quickly grasps the intended message without being...
- **Principle:** Tailor visualizations to your audience's expertise and interests.
- **Data ingestion and processing:** data from one or more transactional data stores, files, real-time streams, or other sources is loaded into a data lake...
- **Analytical data store:** data stores for large scale analytics include relational *data warehouses*, filesystem based *data lakes*, and hybrid...
- **Analytical data model:** while data analysts and data scientists can work with the data directly in the analytical data store, it’s common to...
- **Time Sensitivity:** * Large-Scale Analytics: Primarily concerned with processing historical data in batches
- **Processing Paradigm:** * Large-Scale Analytics: Relies on batch processing, suitable for complex queries and comprehensive reports
- **Use Cases:** * Large-Scale Analytics: Ideal for in-depth trend analysis, historical reporting, and business intelligence

**Key Facts:**
- Database administrators manage databases, assigning permissions to users, storing backup copies of data and restore data in the event of a failure.
- Data engineers manage infrastructure and processes for data integration across the organization, applying data cleaning routines, identifying data gov
- Atomicity – each transaction is treated as a single unit, which succeeds completely or fails completely. For example, a transaction that involved debi
- Consistency – transactions can only take the data in the database from one valid state to another. To continue the debit and credit example above, the
- The type of data being stored (structured, semi-structured, or unstructured).
- The applications and services that will need to read, write, and process the data.
- Modern cloud applications that need to use the latest stable SQL Server features.
- Applications that require high availability.
- Block blobs. A block blob is handled as a set of blocks. Each block can vary in size, up to 4000 MiB. A block blob can contain up to 190.7 TiB (4000 M
- Page blobs. A page blob is organized as a collection of fixed size 512-byte pages. A page blob is optimized to support random read and write operation
- Structure: Organized into tables with predefined schema.
- Schema: Strict and fixed structure, enforced by the database.
- *IoT and telematics*. These systems typically ingest large amounts of data in frequent bursts of activity. Cosmos DB can accept and store this informa
- *Retail and marketing*. Microsoft uses Cosmos DB for its own e-commerce platforms that run as part of Windows Store and Xbox Live. It's also used in t
- *Transact-SQL (T-SQL)*. This version of SQL is used by Microsoft SQL Server and Azure SQL services.
- *pgSQL*. This is the dialect, with extensions implemented in PostgreSQL.
- Principle: Tailor visualizations to your audience's expertise and interests.
- Why it matters: Different people and customers have varying levels of technical proficiency, so aligning visualizations with their needs ensures maxim
- An extensive range of deeply integrated analytics in the industry.
- Shared experiences across experiences that are familiar and easy to learn.
- Large-Scale Analytics: Relies on batch processing, suitable for complex queries and comprehensive reports
- Real-Time Analytics: Embraces streaming processing, allowing for immediate insights and rapid decision-making
- What is data and why is it important?
- What are the main purposes of databases?

---

## Course 4: Accelerating Development Workflow

**Key Terms:**
- **Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require...
- **Who is this for:** New developers, new GitHub users, and students.
- **What you'll learn:** We'll introduce repositories, branches, commits, and pull requests.
- **Version Control:** GitHub uses Git, a distributed version control system, to track changes in source code during software development....
- **Repositories:** Projects on GitHub are organized into repositories, which can contain code, images, text, or any other resource related...
- **Collaboration:** GitHub facilitates collaboration through features such as pull requests, issues, and discussions. Developers can...
- **Read:** Recommended for non-code contributors who want to view or discuss your project. This level is good for anyone that...
- **Triage:** Recommended for contributors who need to proactively manage issues and pull requests without write access. This level...
- **Write:** Recommended for contributors who actively push to your project. Write is the standard permission for most developers.
- **A more powerful AI model:** New modeling algorithms improve the quality of code suggestions.
- **AI-based security vulnerability filtering:** GitHub Copilot for Business automatically blocks common insecure code suggestions by targeting issues such as...
- **VPN proxy support:** GitHub Copilot works with VPNs including self-signed certificates, allowing developers to use it in any working...
- **4 S's:** below. These core rules are the basis for creating effective prompts.
- **Single:** Always focus your prompt on a single, well-defined task or question. This clarity is crucial for eliciting accurate and...
- **Specific:** Ensure that your instructions are explicit and detailed. Specificity leads to more applicable and precise code...
- **Communication:** Consider all of the ways that GitHub makes it easy for a team of developers to communicate about the software...
- **Automation:** GitHub Actions lets your team automate workflows at every step in the software-development process, from integration to...
- **Actions:** tab that provides a quick and easy way to get started with setting up your first script. If you see a workflow that you...
- **Example:** Adding a live search feature to a website, where the search results update dynamically as you type. This enhances user...

**Key Facts:**
- Create a new team, and select or change the parent team.
- Add or remove organization members from a team, or synchronize a GitHub team's membership with an IdP group.
- a comment in an issue or pull request
- Enabling a discussion in your repository
- Version Control: GitHub uses Git, a distributed version control system, to track changes in source code during software development. This allows multi
- Repositories: Projects on GitHub are organized into repositories, which can contain code, images, text, or any other resource related to the project. 
- Read - Recommended for non-code contributors who want to view or discuss your project. This level is good for anyone that needs to view the content wi
- Triage - Recommended for contributors who need to proactively manage issues and pull requests without write access. This level could be good for some 
- Instead of changing everything, LoRA adds smaller trainable parts to each layer of the pretrained model.
- The original model remains the same, which saves time and resources.
- 46% of new code is now written by AI
- 55% faster overall developer productivity
- Single: Always focus your prompt on a single, well-defined task or question. This clarity is crucial for eliciting accurate and useful responses from 
- Specific: Ensure that your instructions are explicit and detailed. Specificity leads to more applicable and precise code suggestions.
- Communication: Consider all of the ways that GitHub makes it easy for a team of developers to communicate about the software development project: code
- Automation: GitHub Actions lets your team automate workflows at every step in the software-development process, from integration to delivery to deploy
- JavaScript Use Case: When a user adds an item to their cart, JavaScript can dynamically update the cart icon, showing the current number of items. It 
- JavaScript Use Case: As users select different quantities or variations of products, JavaScript can instantly calculate and display the updated total 
- Python Use Case: You have a folder with hundreds of files from different projects. With Python, you can write a script that organizes these files into
- Python Use Case: Your company collects data on customer interactions. Python can be used to analyze this data, providing insights into customer behavi
- How would you describe GitHub in a few sentences?
- How does GitHub boost collaboration?

---

## Course 5: Getting Started with Cloud Native Data Storage

**Key Terms:**
- **path:** of /department/name, then the partition key **value** of this document would be information-technology. Behind the...
- **Reminder::** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require...
- **Note::** Only the options in the Basics tab are required to create an Azure Cosmos DB account.
- **Scenario::** Consider a social media platform with users spanning continents. Users all around Asia, Europe, Africa, Oceania, and...
- **Solution::** Globally distributed databases, like Azure Cosmos DB, ensure that data is stored and served from multiple regions,...
- **Structured Data:** SQL databases handle structured data with predefined schemas, ensuring data consistency and integrity.
- **ACID Properties:** Transactions in SQL databases follow ACID properties, providing a high level of data reliability.
- **Normalization:** Emphasizes normalization to eliminate redundancy in data storage.
- **Dedicated provisioned throughput mode::** The throughput provisioned on a container is exclusively reserved for that container and it's backed by the SLAs.
- **Shared provisioned throughput mode::** These containers share the provisioned throughput with the other containers in the same database (excluding containers...
- **Data Access::** APIs provide a standardized way for applications to access data stored in the database. Developers use APIs to...
- **Definition::** Client-side programming in Azure Cosmos DB involves writing code or logic that runs on the *client side*, typically...
- **Responsibility::** The client-side is responsible for tasks such as handling user inputs, executing application-specific business logic,...
- **Operations::** Client-side programming includes operations like creating queries, processing query results, and managing the data...
- **Model::** Traditional model in which you pre-allocate a fixed amount of throughput measured in Request Units per Second (RU/s)...
- **Billing::** You are billed based on the provisioned RU/s, regardless of actual usage. This means you pay for the provisioned...
- **Predictability::** Offers predictable performance because you have a dedicated amount of throughput reserved for your use.
- **Azure Data Factory:** is a native service to extract data, transform it, and load it across sinks and stores in an entirely serverless...
- **linked service:** within Azure Data Factory. This type of linked service is supported both as a source of data ingest and as a target...
- **source:** activity has a configuration JSON object that we can use to set properties such as the query:
- **Note:** While there are others available, this is the most commonly used method of manual throughput provisioning.
- **Write Single Document:** </edukamu-table-cell>
- **Top Query #1:** </edukamu-table-cell>
- **NoSQL vs. Traditional Relational Databases::** Unlike traditional relational databases that use tables, rows, and columns, NoSQL databases can store and manage...
- **Schema-less Nature::** NoSQL databases are often schema-less, meaning you don't have to define the structure of your data before you store it....
- **Focus on Application Needs::** In NoSQL, data modeling is more focused on how the data will be used by the application. You design your data model...
- **Docker:** container image.
- **Microsoft Docs:** website and supports various APIs depending on the platform. The NoSQL API is universally supported across all...
- **pull:** the image from mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator.
- **Example::** Imagine entering your Wi-Fi password on your phone so that it securely connects to the Internet.

**Key Facts:**
- The globally unique name of your account.
- The location (Azure region) for the account.
- Data with many different sources and forms.
- Dynamic data schemas that store different types of data.
- Identify the key benefits provided by Azure Cosmos DB.
- Describe the elements in an Azure Cosmos DB account and how they're organized.
- API Interaction: The SDK enables .NET applications to perform operations such as querying, inserting, updating, and deleting data in Azure Cosmos DB.
- Resource Management: It provides tools for managing databases, collections, users, and permissions within Azure Cosmos DB.
- A new application with hard to forecast users loads
- A new prototype application within your organization
- Number of read operations per second
- Number of write operations per second
- Scalability: As your database grows, partitioning helps manage large amounts of data efficiently by distributing it across multiple servers or locatio
- Performance: It improves performance by allowing parallel processing and reducing the load on any single server.
- 500: Unexpected service error
- A constructor that takes a single string value representing the connection string for the account.
- A constructor that takes two string values representing the endpoint and a key for the account.
- What are SQL and NoSQL databases? What differentiates them?
- What are examples of possible challenges surrounding global-scale data solutions?

---

## Course 6: Getting Started with Azure Development

**Key Terms:**
- **Edit:** button on the right side.
- **Save:** back in the **Configuration** page.
- **Tip:** There is one case in which you may want to use connection strings instead of app settings for non-.NET languages:...
- **Functions:** is a serverless solution that allows you to write less code, maintain less infrastructure, and save on costs. Instead...
- **Azure Functions:** </edukamu-table-header>
- **Logic Apps:** </edukamu-table-header>
- **Rapid Development:** You need to develop and deploy applications quickly.
- **Scalability:** You require automatic scaling to handle fluctuating traffic.
- **Multi-language Support:** Your project involves using various programming languages.
- **compiler:** converts your source code into a different format that the computer's central processing unit (CPU) can execute. When...
- **statement:** is a complete instruction in C#. The semicolon tells the compiler that you've finished entering the command.
- **Development of the Application:** The first step is developing the application. This involves writing code in the preferred programming language and...
- **Fast startup:** ACI can start containers in Azure in seconds, without the need to provision and manage VMs
- **Container access:** ACI enables exposing your container groups directly to the internet with an IP address and a fully qualified domain...
- **Consistency Across Environments:** Containers encapsulate an application and its dependencies, ensuring that it works uniformly across different computing...
- **Rapid Deployment and Scaling:** Containers can be started, stopped, and replicated quickly and easily, which is ideal for scaling applications in...
- **Isolation:** Each container operates in isolation, preventing one application's issues or changes from affecting others. This...
- **Hot:** Optimized for storing data that is accessed frequently.
- **Cool:** Optimized for storing data that is infrequently accessed and stored for a minimum of 30 days.
- **Cold tier:** Optimized for storing data that is infrequently accessed and stored for a minimum of 90 days. The cold tier has lower...
- **Azure Blob Storage:** (the first major topic of this unit) shines, offering a highly scalable, secure, and cost-effective platform for...
- **containerized solutions:** an approach in which applications are packaged with all their dependencies into containers.
- **Azure Container Instances:** and **Azure Container Apps** are prime examples, providing a serverless platform for running containers, thus reducing...
- **Note:** Running multiple containers in a single container app is an advanced use case. In most situations where you want to run...
- **Privileged containers:** Azure Container Apps can't run privileged containers. If your program attempts to run a process that requires root...
- **Operating system:** Linux-based (`linux/amd64`) container images are required.
- **Asynchronous Processing:** Event-based systems allow for asynchronous processing, which means that the system generating the event does not wait...
- **Event Publishers and Subscribers:** In an event-driven architecture, there are publishers (or producers) that generate events, and subscribers (or...
- **Loose Coupling:** Event-based architectures promote loose coupling between services. The producer of the event does not need to know...
- **Secrets Management:** Azure Key Vault can be used to Securely store and tightly control access to tokens, passwords, certificates, API keys,...
- **Key Management:** Azure Key Vault can also be used as a Key Management solution. Azure Key Vault makes it easy to create and control the...
- **Certificate Management:** Azure Key Vault is also a service that lets you easily provision, manage, and deploy public and private Secure Sockets...
- **API gateway:** is the endpoint that:
- **management plane:** is the administrative interface where you set up your API program. Use it to:
- **Developer portal:** is an automatically generated, fully customizable website with the documentation of your APIs. Using the developer...
- **Feature flag:** A feature flag is a variable with a binary state of on or off. The feature flag also has an associated code block. The...
- **Feature manager:** A feature manager is an application package that handles the lifecycle of all the feature flags in an application. The...
- **Filter:** A filter is a rule for evaluating the state of a feature flag. A user group, a device or browser type, a geographic...

**Key Facts:**
- Stack settings: The software stack to run the app, including the language and SDK versions. For Linux apps and custom container apps, you can also set
- Platform settings: Lets you configure settings for the hosting platform, including:
- How your function app is scaled.
- The resources available to each function app instance.
- The Azure portal shows only features that currently work for Linux apps. As features are enabled, they're activated on the portal.
- When deployed to built-in images, your code and content are allocated a storage volume for web content, backed by Azure Storage. The disk latency of t
- Business applications to capture, analyze, and process data
- Dynamic web applications that can be accessed from a web browser
- The first step is developing the application. This involves writing code in the preferred programming language and creating a suitable environment for
- Creating a Container Image: The application and its dependencies are packaged into a container image. This is done using a tool like Docker. A Dockerf
- Container Image: A container image is a lightweight, standalone, executable software package that includes everything needed to run a piece of softwar
- Managed Service: ACR is a managed service, meaning that Azure handles the infrastructure, scalability, and maintenance of the registry. Users don't ne
- Hot - Optimized for storing data that is accessed frequently.
- Cool - Optimized for storing data that is infrequently accessed and stored for a minimum of 30 days.
- Serving images or documents directly to a browser.
- Storing files for distributed access.
- An agent that reads logs from the primary app container on a shared volume and forwards them to a logging service.
- A background process that refreshes a cache used by the primary app container in a shared volume.
- Event sources - Where the event took place?
- Topics - The endpoint where publishers send events.
- Security: The system must be safe from external misuse and/or attacks
- Performance: The system must be fast enough to fill its purpose, whether that’s for a background batch system or for an interactive user interface
- The API gateway is the endpoint that:
- The management plane is the administrative interface where you set up your API program. Use it to:
- Easier to read. Instead of one long sequence of characters, delimiters in a hierarchical key name function as spaces in a sentence.
- Easier to manage. A key name hierarchy represents logical groups of configuration data.
- What are so-called web apps? How do they differ from other types of applications?
- What are Azure Functions? Give a few examples.

---

## Course 7: Getting Started with AI Development

**Key Terms:**
- **Recap: Containers:** Containerized development, unlike traditional methods, separates applications from specific hardware and software...
- **Feature:** </edukamu-table-header>
- **Image:** </edukamu-table-header>
- **Language:** </edukamu-table-header>
- **Speech:** </edukamu-table-header>
- **Vision:** </edukamu-table-header>
- **Language detection:** determining the language in which text is written.
- **Key phrase extraction:** identifying important words and phrases in the text that indicate the main points.
- **Sentiment analysis:** quantifying how positive or negative the text is.
- **1. Ease of Use::** Azure AI Services offers pre-built AI models and tools, making it easier for developers with basic knowledge of Azure...
- **2. Wide Range of Services::** Azure AI Services encompasses various domains, including:
- **3. Scalability and Integration::** As a cloud service, Azure AI is highly scalable, allowing applications to handle increased loads without the need for...
- **Azure AI Language:** includes a *question answering* capability, which enables you to define a *knowledge base* of question-and-answer pairs...
- **Note::** The question answering capability of Azure AI Language is a newer version of the QnA Service, which still exists as a...
- **Azure AI services:** using the search field at the top of the portal.
- **GetTime:** "What time is it?"
- **GetWeather:** "What is the weather forecast?"
- **TurnOnDevice:** "Turn the light on."
- **Create:** under the **Language Service**.
- **Azure OpenAI Service:** In the following sections, we’ll explore the process of creating natural language solutions with a toolbox called Azure...
- **Overview:** REST API is a set of rules and conventions for building and interacting with web services. It allows developers to...
- **Significance:** With the REST API, developers can make HTTP requests to access the capabilities of Azure OpenAI Service from any...
- **Content type:** </edukamu-table-header>
- **Indexed as:** </edukamu-table-header>
- **Features:** </edukamu-table-header>
- **Enhanced Responses:** RAG focuses on improving the quality of responses generated by AI systems. It achieves this by retrieving relevant...
- **Azure AI Search:** resource in your Azure subscription. Depending on the specific solution you intend to build, you may also need Azure...
- **Basic (B):** Use this tier for small-scale search solutions that include a maximum of 15 indexes and 2 GB of index data.
- **Important:** No matter how good of a prompt you can design, responses from AI models should never be taken as fact or completely...
- **Prompt:** Write a product description for a new water bottle
- **Response:** *Introducing the latest addition to our product line - the innovative and eco-friendly water bottle. Made from...
- **Reminder:** Exploring Microsoft Azure is not a mandatory requirement for completing this course since it may require technical...
- **Note:** You can find the regions available for a service through the CLI command az account list-locations.
- **Deployments:** page, from where you can deploy a base model and start experimenting with it.
- **GPT-4 models:** are the latest generation of *generative pretrained* (GPT) models that can generate natural language and code...
- **Context Establishment:** This stage involves understanding the environment in which the AI system will operate, including its purpose, the...
- **Governance:** This aspect focuses on establishing oversight and accountability mechanisms. It includes developing policies,...
- **Risk Assessment:** This step involves identifying, analyzing, and evaluating risks. This includes understanding the potential for harm,...

**Key Facts:**
- Containers are portable across hosts, which may be running different operating systems or use different hardware - making it easier to move an applica
- A single container host can support multiple isolated containers, each with its own specific runtime configuration - making it easier to consolidate m
- Azure AI Document Intelligence - An optical character recognition (OCR) solution that can extract semantic meaning from forms, such as invoices, recei
- Azure AI Immersive Reader - A reading solution that supports people of all ages and abilities.
- Language detection - determining the language in which text is written.
- Key phrase extraction - identifying important words and phrases in the text that indicate the main points.
- Azure AI Services, which provides APIs for vision, speech, language, decision, and search, enabling features like speech recognition, language underst
- Azure Machine Learning, a platform for building, training, and deploying machine learning models at scale, catering to both seasoned data scientists a
- Web sites containing frequently asked question (FAQ) documentation.
- Files containing structured text, such as brochures or user guides.
- Capture multiple different examples, or alternative ways of saying the same thing
- Vary the length of the utterances from short, to medium, to long
- The intents and entities include a confidence score between 0.0 to 1.0 associated with how confident the model is about predicting a certain element i
- The top scoring intent is contained within its own parameter.
- Text or Generative Pre-trained Transformer (GPT) - Models that understand and generate natural language and some code. These models are best at genera
- Code - Code models are built on top of GPT models, and trained on millions of lines of code. These models can understand and generate code, including 
- Indexing strategies that load and refresh at scale, for all of your content, at the frequency you require.
- Query capabilities and relevance tuning. The system should return relevant results, in the short-form formats necessary for meeting the token length r
- Index documents and data from a range of sources.
- Use cognitive skills to enrich index data.
- "I want you to act like a command line terminal. Respond to commands exactly as cmd.exe would, in one unique code block, and nothing else."
- "I want you to be a translator, from English to Spanish. Don't respond to anything I say or ask, only translate between those two languages and reply 
- If n is equal to 0, the function returns m + 1.
- If m is equal to 0, the function calls itself recursively with n - 1 and 1 as arguments.
- MyOpenAIResource: *replace with a unique name for your resource*
- OAIResourceGroup: *replace with your resource group name*
- Generating content that is offensive, pejorative, or discriminatory.
- Generating content that contains factual inaccuracies.
- What tools are included in Azure AI Services?
- How can using containers make Azure AI Services more powerful?

---
