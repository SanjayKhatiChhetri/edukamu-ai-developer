## Advanced Capabilities

On this course, we've explained some of the most widely adapted capabilities Microsoft Azure offers for developers. While our goal has been building a strong foundational understanding of the overall process, many neat features are simply beyond the scope of this course, as they require advanced knowledge and experience working with Azure.

In this section, we'll briefly overview a few of these capabilities. Instead of delving into the technical details, we'll explore how they can be used to empower modern applications.

We'll start with 1) event-based solutions and 2) message-based solutions. We'll wrap up the course with an overview of 3) performance monitoring with Application Insights, a capable tool for troubleshooting solutions.

Let's begin, shall we?

### 1. Event-Based Solutions

Event-based solutions are an essential aspect of modern software architecture, particularly in distributed systems and cloud computing. These solutions revolve around the concept of events - significant changes or occurrences within a system - and how these events trigger specific actions or workflows.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Key Aspects of Event-Based Solutions
</edukamu-collapse-hidden-title>

Event-based solutions focus on responding to events, which are often lightweight notifications that signify a change in state or signals for an action to occur. Unlike message-based solutions, which typically involve direct communication between systems and can carry a significant payload of data, event-based solutions are more about signaling that something has occurred.

Key characteristics of event-based solutions include:

1. **Asynchronous Processing**: Event-based systems allow for asynchronous processing, which means that the system generating the event does not wait for a response from the receiver. This decoupling of components promotes flexibility and scalability.
2. **Event Publishers and Subscribers**: In an event-driven architecture, there are publishers (or producers) that generate events, and subscribers (or consumers) that listen and react to these events.
3. **Loose Coupling**: Event-based architectures promote loose coupling between services. The producer of the event does not need to know about the consumers, making the system more modular and easier to extend.
4. **Scalability and Resilience**: These systems can handle high volumes of events and are resilient to failures, as the event processing is often distributed among multiple consumers.

### Difference from Message-Based Solutions

While both event-based and message-based architectures involve communication between different parts of a system, they differ in their approach and use cases.

Message-Based Solutions focus on transmitting data from one point to another, often involving a queue or bus that holds the message until it's processed. The message typically carries a payload and is used for direct communication.

Event-based solutions, on the other hand, are focused on signaling that an event has occurred. They are often used for indirect communication in which the details of the event are not as crucial as the fact that it occurred.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Event-Based Solutions in Azure
</edukamu-collapse-hidden-title>

Microsoft Azure offers the following services for building, implementing, and managing event-based solutions:

1. **Azure Event Grid**: An event-routing service which helps build applications with event-based architectures. It supports system events from Azure services and custom events.
2. **Azure Event Hubs**: A big data streaming platform and event ingestion service, capable of receiving and processing millions of events per second.

In order to get a glimpse of event-based solutions at Azure, let's take a short look at Azure Event Grid.

### Introduction to Azure Event Grid

Azure Event Grid is a serverless event broker that you can use to integrate applications using events. Events are delivered by Event Grid to subscriber destinations such as applications, Azure services, or any endpoint to which Event Grid has network access. The source of those events can be other applications, SaaS services and Azure services. Publishers emit events, but have no expectation about how the events are handled. Subscribers decide on which events they want to handle.

Event Grid allows you to easily build applications with event-based architectures. Event Grid has built-in support for events coming from Azure services, like storage blobs and resource groups. Event Grid also has support for your own events, using custom topics.

You can use filters to route specific events to different endpoints, multicast to multiple endpoints, and make sure your events are reliably delivered.

The following image shows how Event Grid connects sources and handlers, and isn't a comprehensive list of supported integrations.

<edukamu-image url="/graphics/module3/functional-model.png" alt="Image showing the Event Grid model of sources and handlers.">
<br>

There are five concepts in Azure Event Grid you need to understand to help you get started:

- **Events** - What happened?
- **Event sources** - Where the event took place?
- **Topics** - The endpoint where publishers send events.
- **Event subscriptions** - The endpoint or built-in mechanism to route events, sometimes to more than one handler. Subscriptions are also used by handlers to intelligently filter incoming events.
- **Event handlers** - The app or service reacting to the event.

### Events

An event is the smallest amount of information that fully describes something that happened in the system. Every event has common information like: source of the event, time the event took place, and unique identifier. Every event also has specific information that is only relevant to the specific type of event. For example, an event about a new file being created in Azure Storage has details about the file, such as the `lastTimeModified` value. Or, an Event Hubs event has the URL of the Capture file.

An event of size up to 64 KB is covered by General Availability (GA) Service Level Agreement (SLA). The support for an event of size up to 1 MB is currently in preview. Events over 64 KB are charged in 64-KB increments.

### Event Sources

An event source is where the event happens. Each event source is related to one or more event types. For example, Azure Storage is the event source for blob created events. IoT Hub is the event source for device created events. Your application is the event source for custom events that you define. Event sources are responsible for sending events to Event Grid.

### Topics

The Event Grid topic provides an endpoint where the source sends events. The publisher creates the Event Grid topic, and decides whether an event source needs one topic or more than one topic. A topic is used for a collection of related events. To respond to certain types of events, subscribers decide which topics to subscribe to.

**System topics** are built-in topics provided by Azure services. You don't see system topics in your Azure subscription because the publisher owns the topics, but you can subscribe to them. To subscribe, you provide information about the resource you want to receive events from. As long as you have access to the resource, you can subscribe to its events.

**Custom topics** are application and third-party topics. When you create or are assigned access to a custom topic, you see that custom topic in your subscription.

### Event Subscriptions

A subscription tells Event Grid which events on a topic you're interested in receiving. When creating the subscription, you provide an endpoint for handling the event. You can filter the events that are sent to the endpoint. You can filter by event type, or subject pattern. Set an expiration for event subscriptions that are only needed for a limited time and you don't want to worry about cleaning up those subscriptions.

### Event Handlers

From an Event Grid perspective, an event handler is the place where the event is sent. The handler takes some further action to process the event. Event Grid supports several handler types. You can use a supported Azure service or your own webhook as the handler. Depending on the type of handler, Event Grid follows different mechanisms to guarantee the delivery of the event. For HTTP webhook event handlers, the event is retried until the handler returns a status code of 200 – OK. For Azure Storage Queue, the events are retried until the Queue service successfully processes the message push into the queue.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Scenario: Event-Based Solutions in Action
</edukamu-collapse-hidden-title>

Omise, our imaginary e-commerce business, can significantly benefit from implementing event-based solutions in several areas of its operations. Let's consider a scenario in e-commerce that demonstrates how Omise could utilize Azure's event-based solutions to enhance its business processes and customer experience.

### Scenario: Real-time Inventory Management and Customer Notifications

**Context**: Omise has a dynamic inventory that changes rapidly due to high sales volume and frequent restocking. Keeping track of inventory levels and promptly notifying customers about product availability is crucial for maintaining customer satisfaction and efficient operations.


### Event-Based Solution Implementation

1. **Product Sold Event**
- **Trigger**: Each time a product is sold on Omise's platform, an event is generated.
- **Process**: This event is sent to Azure Event Grid, which then routes the event to various subscribers.
- **Subscribers**: One subscriber could be the inventory management system, which updates the inventory count in real-time.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold;">Low Stock Alert</span>
</li>
</ol>
</edukamu-section>
- **Trigger**: When the inventory level for a product falls below a certain threshold, the inventory management system generates a 'Low Stock' event.
- **Process**: This event is published to Azure Event Grid.
- **Subscribers**: The relevant teams in Omise, such as procurement and marketing, subscribe to these events to initiate restocking processes and update marketing strategies.


### Benefits for Omise

- **Improved Inventory Management**: Real-time tracking helps maintain optimal inventory levels, reducing the chances of overstocking or stockouts.
- **Operational Efficiency**: Automated event handling reduces manual interventions, leading to more efficient operations.
- **Better Feedback Loop**: Quick responses to customer reviews enhance brand reputation and customer satisfaction.

Please notice that the scenario described above only lists a few capabilities offered by utilizing event-based solutions. In reality, services like Azure Event Grid can be suitable for countless different use cases!

</edukamu-collapse>
<br>

In summary, event-based solutions are designed to respond dynamically to specific occurrences or changes within a system. They enable real-time reactions to discrete events, facilitating efficient and responsive architectures, which makes them well suited for for scenarios in which immediate action is required upon the occurrence of a particular event.

Next, let's check out message-based solutions.

### 2. Message-Based Solutions

Just like their event-based counterparts, message-based solutions are a fundamental aspect of modern distributed systems, providing a robust and flexible way to communicate between different parts of an application. These solutions focus on transmitting messages – discrete packets of data – between services or components, often decoupling the sender and receiver for greater scalability and reliability.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Key Aspects of Message-Based Solutions
</edukamu-collapse-hidden-title>

Message-based solutions are integral in scenarios that require reliable communication between loosely coupled services, support for complex workflows, or the ability to handle high volumes of messages. Key benefits of such solutions include the following:

1. **Decoupling of Services**: Message-based architectures allow different parts of an application to operate independently. The sender and receiver of a message do not need to be online or active at the same time, reducing dependencies between system components.
2. **Scalability**: By decoupling services, message-based solutions enable easier scaling. As the volume of messages increases, additional resources can be allocated to handle the load without significantly reorganizing the system.
3. **Reliability and Fault Tolerance**: Messages are stored in queues until processed, ensuring that no data is lost even if a part of the system fails. This contributes to the overall reliability of the system.
4. **Asynchronous Communication**: Message-based systems allow for asynchronous processing, meaning that the sender of a message can continue its operation without waiting for the receiver to process the message.
5. **Load Balancing**: Message queues can help distribute workloads evenly across various processing services, aiding in efficient load balancing.
6. **Flexibility and Maintainability**: These solutions allow for easier updates and maintenance of individual components without disrupting the entire system.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Message-Based Solutions in Azure
</edukamu-collapse-hidden-title>

Message-based solutions are key in building resilient, scalable, and maintainable applications. This is especially true in cloud environments like Microsoft Azure, which offers services like Azure Service Bus to facilitate message-based communication.

Let's take a closer look at Azure Service Bus.

### Introduction to Azure Service Bus

Azure Service Bus is a highly reliable cloud messaging service that provides queued and publish-subscribe messaging patterns. It is used in a variety of scenarios, primarily focusing on decoupling applications and services from each other, allowing them to communicate reliably even in complex, distributed environments.

When using Service Bus, data is transferred between different applications and services using **messages**. A message is a container decorated with metadata, and contains data. The data can be any kind of information, including structured data encoded with the common formats such as the following ones: JSON, XML, Apache Avro, Plain Text.

Some common messaging scenarios are:

- *Messaging*. Transfer business data, such as sales or purchase orders, journals, or inventory movements.
- *Decouple applications*. Improve reliability and scalability of applications and services. Client and service don't have to be online at the same time.
- *Topics and subscriptions*. Enable 1:n relationships between publishers and subscribers.
- *Message sessions*. Implement workflows that require message ordering or message deferral.

### Service Bus Tiers

Service Bus offers a standard and premium tier. The *premium* tier of Service Bus Messaging addresses common customer requests around scale, performance, and availability for mission-critical applications. The premium tier is recommended for production scenarios. Although the feature sets are nearly identical, these two tiers of Service Bus Messaging are designed to serve different use cases.

Some high-level differences are highlighted in the following table.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Premium**
</edukamu-table-header>
<edukamu-table-header>
**Standard**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
High throughput
</edukamu-table-cell>
<edukamu-table-cell>
Variable throughput
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Predictable performance
</edukamu-table-cell>
<edukamu-table-cell>
Variable latency
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Fixed pricing
</edukamu-table-cell>
<edukamu-table-cell>
Pay as you go variable pricing
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Ability to scale workload up and down
</edukamu-table-cell>
<edukamu-table-cell>
N/A
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Message size up to 100 MB
</edukamu-table-cell>
<edukamu-table-cell>
Message size up to 256 KB
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

### Advanced Features

Service Bus includes advanced features that enable you to solve more complex messaging problems. The following table describes several of these features.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="30%">
**Feature**
</edukamu-table-header>
<edukamu-table-header width="70%">
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Message sessions
</edukamu-table-cell>
<edukamu-table-cell>
To create a first-in, first-out (FIFO) guarantee in Service Bus, use sessions. Message sessions enable exclusive, ordered handling of unbounded sequences of related messages.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Autoforwarding
</edukamu-table-cell>
<edukamu-table-cell>
The autoforwarding feature chains a queue or subscription to another queue or topic that is in the same namespace.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Dead-letter queue
</edukamu-table-cell>
<edukamu-table-cell>
Service Bus supports a dead-letter queue (DLQ). A DLQ holds messages that can't be delivered to any receiver. Service Bus lets you remove messages from the DLQ and inspect them.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Scheduled delivery
</edukamu-table-cell>
<edukamu-table-cell>
You can submit messages to a queue or topic for delayed processing. You can schedule a job to become available for processing by a system at a certain time.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Message deferral
</edukamu-table-cell>
<edukamu-table-cell>
A queue or subscription client can defer retrieval of a message until a later time. The message remains in the queue or subscription, but it's set aside.
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

In essence, Azure Service Bus is used when reliable, secure, and scalable communication is needed between different applications or services. It is particularly useful when real-time processing is not a strict requirement, and the system can benefit from asynchronous processing.

In addition to Service Bus, Azure offers another tool for message-based solutions: Storage Queues. Although the two are similar in many aspects, they do have some important differences.

As a solution architect/developer, you should consider using Storage Queues when:

- Your application must store over 80 gigabytes of messages in a queue.
- Your application wants to track progress for processing a message in the queue. It's useful if the worker processing a message crashes. Another worker can then use that information to continue from where the prior worker left off.
- You require server side logs of all of the transactions executed against your queues.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Message-Based Solutions in Action
</edukamu-collapse-hidden-title>

Let's explore how our imaginary e-commerce company, Omise, could integrate message-based solutions into their platform.

### Scenario: Order Processing and Inventory Management

1. **Customer Order Placement**: When a customer places an order on Omise’s e-commerce platform, the order details are sent as a message to a message queue in Azure Service Bus. This message includes customer details, product IDs, quantities, and payment information.
2. **Order Processing System**: A separate order processing service, which is continuously listening to the queue, receives the order message. This service is responsible for various tasks such as validating order details, processing payments, and updating order status.
3. **Inventory Management**: Upon successful payment processing, another message is sent to an inventory management system, possibly through a different queue or topic within Azure Service Bus. This message triggers the inventory system to update stock levels, ensuring accurate inventory tracking.
4. **Order Fulfillment and Shipping**: After inventory update, a notification is sent to the order fulfillment system. This could be through Azure Service Bus or Azure Queue Storage, instructing the system to package and ship the ordered items. The fulfillment system can then send a message back upon completion, which updates the order status to ‘Shipped’ and notifies the customer.

In this scenario, message-based solutions allow Omise to sustain a highly efficient, scalable, and reliable e-commerce platform that can handle complex workflows and high volumes of transactions smoothly.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
Consider the both Omise examples one more time. They may seem similar at first, but make sure to take notice of the following differences:

### Real-time vs. Asynchronous:

- **Event-Based**: Immediate, real-time reactions to events.
- **Message-Based**: Asynchronous processing of messages at a controlled pace.

### Nature of Data:

- **Event-Based**: Events usually carry less data, mainly about the occurrence of a specific action.
- **Message-Based**: Messages can carry more complex data and are part of a larger workflow process.

In summary, event-based solutions are more about responding immediately to user interactions, whereas message-based solutions are geared towards managing more complex, asynchronous workflows like order processing. As such, they can complement each other and empower developers to create even better experiences for their users.

How are you feeling about solution development with Microsoft Azure? On this course, we've been focusing mainly on broadening our horizons about the capabilities offered by the platform - and laying a strong foundation on which to start building practical expertise.

Even though we all strive towards perfection, even the best applications don't always function correctly. That's when troubleshooting becomes crucial for fixing issues and getting the app up and running again as quickly and smoothly as possible.
</edukamu-section>
<br>

### 3. Performance Monitoring in Azure

Microsoft Azure offers quite a few tools for monitoring and troubleshooting solutions. One of the most powerful services in this category is Application Insights.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Application Insights
</edukamu-collapse-hidden-title>

Application Insights is a tool built into Azure Monitor, a comprehensive monitoring solution for collecting, analyzing, and responding to monitoring data from cloud and on-premises environments.  It's a powerful tool for collecting, analyzing, and acting on telemetry data, including metrics, logs, and traces. This service helps developers understand the performance and usage of their applications, identify and diagnose errors and issues, and improve overall performance and reliability.

APM tools are useful to monitor applications from development, through test, and into production in the following ways:

- Proactively understand how an application is performing.
- Reactively review application execution data to determine the cause of an incident.

In addition to collecting metrics and application telemetry data, which describe application activities and health, Application Insights can also be used to collect and store application trace logging data.

The log trace is associated with other telemetry to give a detailed view of the activity. Adding trace logging to existing apps only requires providing a destination for the logs; the logging framework rarely needs to be changed.

### Application Insights Features

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Feature**
</edukamu-table-header>
<edukamu-table-header>
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Live Metrics
</edukamu-table-cell>
<edukamu-table-cell>
Observe activity from your deployed application in real time with no effect on the host environment.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Availability
</edukamu-table-cell>
<edukamu-table-cell>
Also known as “Synthetic Transaction Monitoring”, probe your applications external endpoint(s) to test the overall availability and responsiveness over time.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
GitHub or Azure DevOps integration
</edukamu-table-cell>
<edukamu-table-cell>
Create GitHub or Azure DevOps work items in context of Application Insights data.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Usage
</edukamu-table-cell>
<edukamu-table-cell>
Understand which features are popular with users and how users interact and use your application
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Smart Detection
</edukamu-table-cell>
<edukamu-table-cell>
Automatic failure and anomaly detection through proactive telemetry analysis.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Application Map
</edukamu-table-cell>
<edukamu-table-cell>
A high level top-down view of the application architecture and at-a-glance visual references to component health and responsiveness.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Distributed Tracing
</edukamu-table-cell>
<edukamu-table-cell>
Search and visualize an end-to-end flow of a given execution or transaction.
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

Application Insights collects Metrics and application Telemetry data, which describe application activities and health, as well as trace logging data.

- **Request rates, response times, and failure rates** - Find out which pages are most popular, at what times of day, and where your users are. See which pages perform best. If your response times and failure rates go high when there are more requests, then perhaps you have a resourcing problem.
- **Dependency rates, response times, and failure rates** - Find out whether external services are slowing you down.
- **Exceptions** - Analyze the aggregated statistics, or pick specific instances and drill into the stack trace and related requests. Both server and browser exceptions are reported.
- **Page views and load performance** - reported by your users' browsers.
- **AJAX calls** from web pages - rates, response times, and failure rates.
- **User and session counts.**
- **Performance counters** from your Windows or Linux server machines, such as CPU, memory, and network usage.
- **Host diagnostics** from Docker or Azure.
- **Diagnostic trace logs** from your app - so that you can correlate trace events with requests.
- **Custom events and metrics** that you write yourself in the client or server code, to track business events such as items sold or games won.

Using the data collected by Application Insights, developers can foresee possible issues before they arise, implementing effective mitigation strategies in time.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Scenario: Application Insights in Action
</edukamu-collapse-hidden-title>

Our imaginary e-commerce platform, Omise, aims to provide its customers with the best, smoothest shopping experiences. However, problems are bound to rise from time to time. In order to implement capable monitoring and troubleshooting policies, Omise could use Application Insights in the following ways:

1. **Performance Monitoring**: Omise can monitor the performance of their web platform in real-time. They could track page load times, server response times, and other critical metrics to ensure that customers have a smooth shopping experience.
2. **Error Identification and Diagnostics**: Application Insights can automatically detect and log errors and exceptions that occur on the platform. Omise can use this information to quickly identify and address issues, minimizing downtime and improving the reliability of their service.
3. **User Behavior Analysis**: By tracking user interactions, such as how customers navigate through their site, which products they view most, and where users typically drop off in the purchase process, Omise can gain valuable insights to optimize the user experience and increase sales.
4. **Custom Telemetry for Business Metrics**: Omise can extend the capabilities of Application Insights by tracking custom events and metrics, such as the number of completed transactions, average cart size, and popular payment methods.
5. **Alerts for Critical Issues**: They can set up alerts to notify their IT team if certain thresholds are exceeded, like an unexpected drop in web traffic or a spike in error rates, enabling quick response to potential issues.
6. **Integrated Feedback Loop**: Application Insights can help Omise to continuously improve their platform by providing data-driven insights into the most effective areas for optimization, whether it's enhancing performance or refining user interfaces.

In summary, Azure Application Insights would give Omise a comprehensive understanding of their platform's performance, user behavior, and system health, allowing them to proactively manage their e-commerce service for optimal efficiency and customer satisfaction.

</edukamu-collapse>
<br>

In summary, monitoring and troubleshooting on Azure are essential components for maintaining the health, performance, and reliability of cloud-based applications and services. By leveraging tools like Azure Application Insights, businesses can ensure optimal performance, enhance user experience, and maintain high standards of service delivery, all of which are crucial for success in the digital landscape.

Event-based and message-based solutions, as well as well-rounded monitoring and troubleshooting capabilities, are just examples of the advanced tools and services offered by Microsoft Azure. While it might not be possible to completely grasp and understand everything after a single course, or even a few, having basic knowledge of the wide range of possibilities available on the platform will certainly be helpful as you aim to learn more and more about the exciting role of an Azure developer.

It's time for the last exercise of the course - would you believe it? We've covered a lot during this last section, so make sure to recap a little before taking on the exercise!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Advanced Capabilities
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-text-poll-1.yaml" id="j3y3w59ydcymkzdv">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-text-poll-2.yaml" id="1jkwxgrrevwndfu2">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-text-poll-3.yaml" id="lri6yibzfihoe2a5">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-text-poll-4.yaml" id="k56qgedatpiig51i">

<edukamu-text-poll url="/exercises/module3/advanced-capabilities-text-poll-5.yaml" id="ldhkfvovdalyvjup">
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/3/advanced-capabilities?question=j3y3w59ydcymkzdv">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

You've now completed each and every section of this course. Well done!

All that's left is the traditional summary. Enjoy, you've earned it!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
