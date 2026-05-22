<edukamu-video content="/videos/devai-6-unit1-video.yaml"/>
<br>

## Introduction to Azure AI Development

Welcome to the world of Azure AI development!

On this course, we aim to develop a solid foundational knowledge of solution development on Microsoft Azure. We'll cover the whole development process, exploring topics like web apps, functions, design, deployment, and security - the whole package!

We'll spend the most time working with Microsoft Azure, although there are other options available as well. For beginning developers, such as yourself, the Azure environment is the perfect place to begin!

This first unit focuses on two fundamental aspects: Azure App Service (especially web apps) and Azure Functions. We'll start with an overview of the development process, though, which will make it easier to understand the individual steps and aspects that need to be completed when building AI-enhanced, global-scale solutions.

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="devisioona-logo">
### Business Perspective: Why is the Cloud so Important?
</edukamu-collapse-hidden-title>

Azure App Service and Azure Functions are typical examples of compute or hosting services: They provide computational capacity (i.e., servers) to run your code. They are also typical examples of Platform as a Service (PaaS) solutions: They provide a unified, ready-to-go platform on which to deploy your code without having to worry about IT infrastructure such as name servers, firewalls, networks, operating system security updates and so on.

This readiness is extremely important because the world is about to become even more software-intensive than it already is. According to some estimates, we are going to build more software in the next five years than we did in the last 40. That rate of change requires ready-made platforms and increasing abstraction, as we simply don’t have the money or talent to build and run all that. Cloud is essential, because it allows us to focus on the software – on the actual innovation – itself.

Businesses always look for ROI (Return on Investment). As we developers need to think about the cost of building and running the applications of the future, we come face to face with an undeniable truth: Simple is cheap, complexity drains your wallet. The cloud is a magnificent tool for building systems of all sizes, and we as developers are charged with having the most impact with the least responsible amount of resources. This is true in terms of money, CO2 emissions as well as developer time.

While Azure sports hundreds of distinct services, a typical Finnish cloud application runs on just a few. Azure App Service and Azure Functions are usual suspects when it comes to making your own code run. Whether you’re building an e-commerce website, a backend for a mobile game, an AI-powered business dashboard or even an IoT solution, these services are the key building blocks. They also qualify in terms of ROI: They are simple, cost-effective and fast to adopt.

Modularity is also part of the beauty of the cloud. While App Service will run your first Hello World application, it can equally run a real-time interconnected AI system at a blistering pace and epic scale. Sure, that bigger system will definitely have more pieces attached to it, but it will still benefit from the simplicity and elegance of these basic hosting solutions. Learn them well, and they’ll help you along the whole way.

</edukamu-collapse>
<br>

If you've never worked with programming languages, like C#, before, we recommend that you take the crash course presented below. That'll make it a lot easier to grasp the latter sections of this course! Notice that the same crash course was also included in the fifth course of this program.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### C# Crash Course
</edukamu-collapse-hidden-title>

The C# programming language allows you to build many types of applications, like:

- Business applications to capture, analyze, and process data 
- Dynamic web applications that can be accessed from a web browser
- Games, both 2D and 3D
- Financial and scientific applications
- Cloud-based applications
- Mobile applications

But how do you begin to write an application?

Applications are all made up of many lines of code that work together to achieve a task. By far, the best way to learn how to code is to *write* code. Writing code yourself in each exercise and solving small coding challenges will accelerate your learning.

You'll also begin learning small foundational concepts and build on them with continual practice and exploration.

In this crash course, you'll:

- Write your first lines of C# code.
- Use two different techniques to print a message as output.
- Diagnose errors when code is incorrect.
- Identify different C# syntax elements like operators, classes, and methods.

By the end of this crash course, you'll be able to write C# code to print a message to the standard output of a console, like the Windows Terminal. These lines of code will give you your first look at the C# syntax, and immediately provide invaluable insights.

There is a handy practical introduction to C# available on Microsoft's Learn platform. It requires no subscriptions or signing in, so you can get started immediately! Just follow the instructions on the left hand side of your screen and get acquainted with programming!

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/csharp-write-first/2-exercise-hello-world" target="_blank">Microsoft Learn: Writing Your First Code</edukamu-button>
<br>

To understand how your code works, you need to step back and think about what a programming language is. Consider how your code communicates commands to the computer.

### What is a Programming Language?

Programming languages like C# let you write instructions that you want the computer to carry out. Each programming language has its own syntax, but after learning your first programming language and attempting to learn another one, you'll quickly realize that they all share many similar concepts. A programming language's job is to allow a human to express their intent in a human-readable and understandable way. The instructions you write in a programming language are called "source code" or just "code". Software developers write code.

At this point, a developer can update and change the code, but the computer can't understand the code. The code first must be *compiled* into a format that the computer can understand.

### What is a Compilation?

A special program called a **compiler** converts your source code into a different format that the computer's central processing unit (CPU) can execute. When you used the green **Run** button in the previous unit, the code you wrote was first compiled, then executed.

Why does code need to be compiled? Although most programming languages seem cryptic at first, they can be more easily understood by humans than the computer's *preferred* language. The CPU understands instructions that are expressed by turning thousands or millions of tiny switches either on or off. Compilers bridge these two worlds by translating your human-readable instructions into a computer-understandable set of instructions.

### What is a Syntax?

The rules for writing C# code is called syntax. Just like human languages have rules regarding punctuation and sentence structure, computer programming languages also have rules. Those rules define the keywords and operators of C# and how they are put together to form programs.

When you wrote code into the .NET Editor, you may have noticed subtle changes to the color of different words and symbols. Syntax highlighting is a helpful feature that you'll begin to use to easily spot mistakes in your code that don't conform to the syntax rules of C#.

### How did Your Code Work?

Let's focus on the following line of code you wrote:

C#

```C#
Console.WriteLine("Hello World!");
```

When you ran your code, you saw that the message `Hello World!` was printed to the output console. When the phrase is surrounded by double-quotation marks in your C# code, it's called a **literal string**. In other words, you literally wanted the characters `H, e, l, l, o,` and so on, sent to the output.

The ```Console``` part is called a **class**. Classes "own" methods; or you could say that methods live inside of a class. To visit the method, you must know which class it's in. For now, think of a class as a way to represent an object. In this case, all of the methods that operate on your output console are defined inside of the ```Console``` class.

There's also a dot (or period) that separates the class name ```Console``` and the method name ```WriteLine()```. The period is the *member access operator*. In other words, the dot is how you "navigate" from the class to one of its methods.

The `WriteLine()` part is called a **method**. You can always spot a method because it has a set of parentheses after it. Each method has one job. The ```WriteLine()``` method's job is to write a line of data to the output console. The data that's printed is sent in between the opening and closing parenthesis as an input parameter. Some methods need input parameters, while others don't. But if you want to invoke a method, you must always use the parentheses after the method's name. The parentheses are known as the *method invocation operator*.

Finally, the semicolon is the *end of statement operator*. A **statement** is a complete instruction in C#. The semicolon tells the compiler that you've finished entering the command.

Don't worry if all of these ideas and terms don't make sense. For now, all you need to remember is that if you want to print a message to the output console:

- Use ```Console.WriteLine("Your message here");```
- Capitalize ```Console```, ```Write```, and ```Line```
- Use the correct *punctuation* because it has a special role in C#
- If you make a mistake, just spot it, fix it and re-run

**Tip**: Create a cheat sheet for yourself until you've memorized certain key commands.

It's important to understand the flow of execution. In other words, your code instructions were executed in order, one line at a time, until there were no more instructions to execute. Some instructions will require the CPU to wait before it can continue. Other instructions can be used to change the flow of execution.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Challenge: Problem Solving and Code 
</edukamu-collapse-hidden-title>

Using your newly gained knowledge, try to complete the following challenge using the emulator available over at Microsoft Learn.

Your job is to write code in the .NET Editor to display two messages. Follow the instructions below and try to come up with a solution.

1. Select all of the code in the .NET Editor, and press ```Delete``` or ```Backspace``` to delete it.
2. Write new code that produces the following output:

```code
This is the first line.
This is the second line.
```

Previously, you learned how to display a message in just one line of code, and you learned how to display a message using multiple lines of code. Use both techniques for this challenge. It doesn't matter which technique you apply to which line, and it doesn't matter how many ways you split one of the messages into multiple lines of code. That's your choice.

No matter how you do it, your code should produce the specified output - there are more solutions than one!

You'll find an example solution below.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Challenge: Example Solution
</edukamu-collapse-hidden-title>
The following code is one possible solution for the challenge from the previous unit.

C#

```C#
Console.WriteLine("This is the first line.");

Console.Write("This is ");
Console.Write("the second ");
Console.Write("line.");
```

Remember that this code is just *one possible solution*, among many possible ways to achieve the same result. However, you should have used both the Console.WriteLine() and Console.Write(String) methods to produce the desired output.

```code
This is the first line.
This is the second line.
```

If you were successful, congratulations! If not, review the solutions described here and try to come up with one of your own before moving on. Programming is as much about problem solving as it is about writing code!

We hope you enjoyed the crash course presented here!

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
The C# language examples are more complicated than the ones covered in the crash course, but this basic knowledge will certainly come in handy as you move forward on this course. Spend all the time you need with the examples presented and try to understand them - this way you'll not only learn about global database services but also reinforce your programming skills!

All right, it's time to dig into our core topics on this first unit: Azure App Service and Azure Functions. After a short overview, we'll look at an example scenario in which Microsoft Azure is used to build a modern, global-scale solution for an e-commerce platform. 

Without further ado, let's get acquainted with Azure App Service and Azure Functions.
</edukamu-section>
<br>

<edukamu-tabs theme="edukamu-tabs1">

<edukamu-tabs-tab title="Introduction to Azure App Service">
Azure App Service is a powerful platform for building web apps, mobile back ends, and RESTful APIs. In this section, we will explore the key functions of Azure App Service, focusing on aspects like authentication, authorization, app settings configuration, scaling applications, and using deployment slots.

### Terminology

**Web Apps**: Web applications are software applications that run on a web server and are accessed through a web browser. They offer interactive user experiences and can handle various tasks, from displaying content to processing data, but don't need to be installed like mobile apps, for example.

**Mobile Back Ends**: This refers to the server-side infrastructure for mobile apps. It handles the app's data processing, storage, security, and integrates business logic. Mobile back ends are essential for managing user authentication, data synchronization, push notifications, and other server-side functions. Front end, by the way, refers to user-facing elements, such as the user interfaxe and user experience (UI/UX).

**RESTful APIs**: Representational State Transfer (REST) APIs are a set of rules and standards used to build web services. They allow different software applications to communicate over the internet using standard HTTP methods. RESTful APIs are known for their simplicity, scalability, and statelessness, making them widely used for web services and applications.

Azure App Service simplifies the development process by supporting multiple programming languages and frameworks, such as .NET, Java, Node.js, and PHP. This service offers a range of features like auto-scaling, integrated security, and support for continuous integration and continuous deployment (CI/CD) workflows. It's particularly beneficial for businesses and developers looking to create robust web and mobile applications without the overhead of managing servers and infrastructure.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="Introduction to Azure Functions">
Azure Functions is a serverless computing service provided by Microsoft Azure, enabling developers to run small pieces of code, or "functions," in the cloud. This service allows the execution of code in response to a variety of events, such as HTTP requests, database changes, or message queue triggers, without the need for managing infrastructure.

### Terminology

**HTTP Requests**: An Azure Function can be triggered by an HTTP request, such as a user submitting a form on a website. This could initiate a function to process the form data, verify it, and store it in a database.

**Database Changes**: A function can be set to trigger on changes in a database, like a new entry being added. This can be used for real-time data processing, like sending a confirmation email to a user after a transaction is recorded.

**Message Queue Triggers**: Azure Functions can respond to messages added to Azure queues (a service for storing large numbers of messages). For instance, a function could be triggered when a message is added to a queue, indicating that a new order has been placed in an e-commerce system

Azure Functions supports numerous programming languages and integrates with other Azure services, making it ideal for building scalable, event-driven applications with reduced development and operational costs.
</edukamu-tabs-tab>

</edukamu-tabs>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure App Service
</edukamu-collapse-hidden-title>

Azure App Service is a powerful platform for building web apps, mobile back ends, and RESTful APIs. In this section, we will explore the key functions of Azure App Service, focusing on aspects like authentication, authorization, app settings configuration, scaling applications, and using deployment slots.

### Terminology

**Web Apps**: Web applications are software applications that run on a web server and are accessed through a web browser. They offer interactive user experiences and can handle various tasks, from displaying content to processing data, but don't need to be installed like mobile apps, for example.

**Mobile Back Ends**: This refers to the server-side infrastructure for mobile apps. It handles the app's data processing, storage, security, and integrates business logic. Mobile back ends are essential for managing user authentication, data synchronization, push notifications, and other server-side functions. Front end, by the way, refers to user-facing elements, such as the user interfaxe and user experience (UI/UX).

**RESTful APIs**: Representational State Transfer (REST) APIs are a set of rules and standards used to build web services. They allow different software applications to communicate over the internet using standard HTTP methods. RESTful APIs are known for their simplicity, scalability, and statelessness, making them widely used for web services and applications.

Azure App Service simplifies the development process by supporting multiple programming languages and frameworks, such as .NET, Java, Node.js, and PHP. This service offers a range of features like auto-scaling, integrated security, and support for continuous integration and continuous deployment (CI/CD) workflows. It's particularly beneficial for businesses and developers looking to create robust web and mobile applications without the overhead of managing servers and infrastructure.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Functions
</edukamu-collapse-hidden-title>

Azure Functions is a serverless computing service provided by Microsoft Azure, enabling developers to run small pieces of code, or "functions," in the cloud. This service allows the execution of code in response to a variety of events, such as HTTP requests, database changes, or message queue triggers, without the need for managing infrastructure.

### Terminology

**HTTP Requests**: An Azure Function can be triggered by an HTTP request, such as a user submitting a form on a website. This could initiate a function to process the form data, verify it, and store it in a database.

**Database Changes**: A function can be set to trigger on changes in a database, like a new entry being added. This can be used for real-time data processing, like sending a confirmation email to a user after a transaction is recorded.

**Message Queue Triggers**: Azure Functions can respond to messages added to Azure queues (a service for storing large numbers of messages). For instance, a function could be triggered when a message is added to a queue, indicating that a new order has been placed in an e-commerce system

Azure Functions supports numerous programming languages and integrates with other Azure services, making it ideal for building scalable, event-driven applications with reduced development and operational costs.

</edukamu-collapse>
<br> -->

Just getting to know these two services will get you a lot closer to building independent Azure solutions using the latest cutting-edge technology provided by Microsoft. We'll spend the rest of this unit exploring the duo, but before we begin, as promised, let's find out about Azure development in a bit more detail.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Example: Microsoft Azure Development for Global E-Commerce
</edukamu-collapse-hidden-title>

In this example scenario, we'll meet GlobalTech Innovations, an inspiring and agile company looking to expand into e-commerce. After using Microsoft Azure services for years, they decide to trust the same platform one more time, this time while building their very own e-commerce application.

Let's check out the development process, step by step.

### Project Overview

GlobalTech Innovations aims to create an e-commerce platform that offers a wide range of products, personalized shopping experiences, and seamless global transactions. The platform will support high user traffic, offer real-time inventory updates, and process transactions securely.

The following is an overview of how they would take into account some crucial aspects within the development cycle.

#### 1. Using Azure App Service Web Apps

Azure App Service Web Apps is utilized to host the e-commerce platform's front-end. This ensures an engaging and responsive interface, crucial for retaining customers and facilitating easy navigation. The service's scalability is vital for handling varying levels of user traffic, especially during peak shopping seasons, sales, or product launches.

#### 2. Implementing Azure Functions

Azure Functions plays a critical role in the back-end, handling order processing, payment gateway integration, and customer notification systems. By using serverless architecture, GlobalTech efficiently manages these operations without worrying about the underlying infrastructure. This approach is particularly beneficial during high-demand periods, as Azure Functions can automatically scale to meet increased workload demands.

#### 3. Leveraging Azure Cosmos DB

Do you still remember Azure Cosmos DB from the previous course? To manage the vast amount of product data, customer information, and transaction records, GlobalTech uses the very service. Its global distribution capabilities ensure that users worldwide experience low latency, essential for a smooth shopping experience. Cosmos DB's scalability and multi-model support make it ideal for handling the platform's diverse data needs, from product catalogs to customer preferences.

#### 4. Authentication and Security

For authentication, Azure Active Directory is integrated to provide secure login and user management. This is crucial for protecting customer data and transaction details. The platform also implements multi-factor authentication and secure payment processing to ensure transaction security.

#### 5. Development Process

The e-commerce platform's development includes continuous integration and deployment for regular updates, deployment slots for testing new features without affecting the live environment, and a focus on responsive design to accommodate various devices.

#### 6. Monitoring and Optimization

Post-launch, the platform is continuously monitored using Azure Monitor and Application Insights. This enables GlobalTech to optimize performance, manage inventory efficiently, and improve customer experience based on real-time data and user feedback.

### Conclusion

This e-commerce platform makes online shopping a breeze by providing a global reach, personalized shopping experiences, and robust performance. The Azure-powered infrastructure ensures that the platform can handle high traffic volumes, maintain product data integrity, and offer secure transactions. GlobalTech's e-commerce platform sets a new standard in the online retail space, demonstrating the power and flexibility of Microsoft Azure in developing scalable, secure, and user-centric applications.

</edukamu-collapse>
<br>

Even though we will visit each aspect of the above example during this course, remember that developing modern applications is a time-consuming and demanding process. The short overview we've just covered contains only the most principal elements that need to be addressed in unique ways, according to the specific scenario at hand.

There are no one-size-fits-all solutions available when developing solutions with Azure - which makes it all the more exciting! By mastering the platform, you too could be one of the game-changers building the intelligent solutions that shape our future!

Let's take the first exercise of this course before getting started with Azure App Service.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Warming Up
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module1/introduction-to-azure-ai-development-text-poll-1.yaml" id="pxfy80799epa0gxb">

<edukamu-text-poll url="/exercises/module1/introduction-to-azure-ai-development-text-poll-2.yaml" id="rkjeywskjybzxtx4">

<edukamu-text-poll url="/exercises/module1/introduction-to-azure-ai-development-text-poll-3.yaml" id="pojkb458tswd3w5s">
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/1/introduction-to-azure-ai-development?question=pxfy80799epa0gxb">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

How are you feeling? Anxious to get going? In that case, feel free to click yourself forward - Azure App Service is waiting!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
