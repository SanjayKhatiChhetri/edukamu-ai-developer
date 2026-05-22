## GitHub Copilot for Business

In the bustling city of software development, GitHub Copilot stands as a visionary assisting architect, reshaping how businesses construct their digital landscapes. This AI-driven coding companion understands the city's unique architecture, providing architects with tailor-made blueprints for efficient code structures.

In GitHub, Copilot’s capabilities can also be of great value for businesses or different sizes and fields of expertise. From implementing secure login systems to scaling applications' databases, GitHub Copilot for Business has the solutions of significantly improving business, making it more productive.

On this page, we'll explore how GitHub Copilot can help businesses. First, however, let's review Large Language Models (LLM), the backbone of GitHub Copilot. If you've already completed the previous courses of this micro degree, this might already be familiar, but a little repetition never hurts!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### LLM and GitHub Copilot
</edukamu-collapse-hidden-title>

GitHub Copilot is powered by Large Language Models (LLMs) to assist you in writing code seamlessly. Before digging deeper into GitHub Copilot's business capabilities, we'll review the following:
1. What are LLMs?
2. Fine-tuning LLMs
3. LoRA fine-tuning

### What are LLMs?

Large Language Models (LLMs) are artificial intelligence models designed and trained to understand, generate, and manipulate human language. These models are ingrained with the capability to handle a broad range of tasks involving text, thanks to the extensive amount of text data they're trained on. Here are some core aspects to understand about LLMs:

#### 1. Training Data

LLMs are exposed to vast amounts of text from diverse sources. This exposure equips them with a broad understanding of language, context, and intricacies involved in various forms of communication.

#### 2. Contextual Understanding

LLMs excel in generating contextually relevant and coherent text. Their ability to understand context allows them to provide meaningful contributions, be it completing sentences, paragraphs, or even generating whole documents that are contextually apt.

#### 3. Machine Learning and AI Integration

LLMs are grounded in machine learning and artificial intelligence principles. They're neural networks with millions, or even billions, of parameters that are fine-tuned during the training process to understand and predict text effectively.

#### 4. Versatility

These models aren't limited to a specific type of text or language. They can be tailored and fine-tuned to perform specialized tasks, making them highly versatile and applicable across various domains and languages.

### Fine-tuning LLMs

Fine-tuning is a critical process that allows us to tailor pretrained large language models (LLMs) for specific tasks or domains. It involves training the model on a smaller, task-specific dataset, known as the target dataset, while using the knowledge and parameters gained from a large pretrained dataset, referred to as the source model.

<edukamu-image url="/graphics/module2/4-fine-tune-in-large-language-models-diagram.png" alt="Diagram that shows how fine-tuning is used in Large Language Models." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"> 
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

Fine-tuning is essential to adapt LLMs for specific tasks, enhancing their performance. However, GitHub took it a step further by using the LoRA fine tuning method, which we'll discuss next.

### LoRA Fine-tuning

Traditional full fine-tuning means to train all parts of a neural network, which can be slow and heavily reliant on resources. But LoRA (Learning to Rank) fine-tuning is a clever alternative. It's used to make large pretrained language models (LLMs) work better for specific tasks without redoing all the training.

Here's how LoRA works:
* Instead of changing everything, LoRA adds smaller trainable parts to each layer of the pretrained model.
* The original model remains the same, which saves time and resources.

What's great about LoRA:
* It beats other adaptation methods like adapters and prefix-tuning.
* It's like getting great results with fewer moving parts.

In simple terms, LoRA fine-tuning is about working smarter, not harder, to make LLMs better for your specific coding requirements when using Copilot.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-green">
GitHub Copilot utilizes LLMs to provide context-aware code suggestions. The LLM considers not just the current file but also other open files and tabs to generate accurate and relevant code completions. This dynamic approach ensures tailored suggestions, improving your productivity.

Understanding the nature of Large Language Models makes grasping the capabilities and opportunities provided by GitHub Copilot a lot simpler. Now that we've reviewed LLMs, let's dive straight into the world of business.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Improving Operations with GitHub Copilot for Business
</edukamu-collapse-hidden-title>

GitHub Copilot for Business builds the power of generative AI into an editor extension that suggests code in real time. It works with code and natural-language prompts to offer multiple suggestions that you can quickly accept or reject. GitHub Copilot learns alongside developers to adapt to individual coding styles and conventions. With GitHub Copilot, developers can use the editor of their choice, including Visual Studio, Neovim, VS Code, or JetBrains integrated development environments (IDEs).

GitHub Copilot for Business focuses on making your organization more productive, secure, and fulfilled by enabling your developers to code faster and focus on more satisfying work.

New features in Copilot for Business include:
* **A more powerful AI model**: New modeling algorithms improve the quality of code suggestions.
* **AI-based security vulnerability filtering**: GitHub Copilot for Business automatically blocks common insecure code suggestions by targeting issues such as hard-coded credentials, SQL injections, and path injections.
* **VPN proxy support**: GitHub Copilot works with VPNs including self-signed certificates, allowing developers to use it in any working environment.
* **Simple sign-up**: Any company can quickly purchase Copilot for Business licenses online and easily assign seats, even if they don't use the GitHub platform for their source code.

Now, let's review the differences between GitHub Copilot for Business and GitHub Copilot for Individuals.

### GitHub Copilot for Business vs. GitHub Copilot for Individuals

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="40%">
<!-- - -->
</edukamu-table-header>
<edukamu-table-header width="30%">
GitHub Copilot for Business
</edukamu-table-header>
<edukamu-table-header width="30%">
GitHub Copilot for Individuals
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Zero data retention for code snippets and usage telemetry
</edukamu-table-cell>
<edukamu-table-cell >
✓
</edukamu-table-cell>
<edukamu-table-cell >
✕
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Blocks suggestions matching public code
</edukamu-table-cell>
<edukamu-table-cell >
✓
</edukamu-table-cell>
<edukamu-table-cell >
✓
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Plugs right into your editor
</edukamu-table-cell>
<edukamu-table-cell >
✓
</edukamu-table-cell>
<edukamu-table-cell >
✓
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Offers multiline function suggestions
</edukamu-table-cell>
<edukamu-table-cell >
✓
</edukamu-table-cell>
<edukamu-table-cell >
✓
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Organization-wide policy management
</edukamu-table-cell>
<edukamu-table-cell >
✓
</edukamu-table-cell>
<edukamu-table-cell >
✕
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
VPN proxy support via self-signed certificates
</edukamu-table-cell>
<edukamu-table-cell >
✓
</edukamu-table-cell>
<edukamu-table-cell >
✕
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### GitHub for Business Use Cases
</edukamu-collapse-hidden-title>

GitHub Copilot improves developer productivity and happiness, reduces disruptions, improves flow, and increases the amount of time a developer spends doing satisfying work.

<edukamu-image url="/graphics/module2/3-coyote-logistics-app.png" alt="Screenshot of a view of Coyote Logistics's tracking system on a laptop and phone app."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

**Developers code faster**: In a survey conducted by Microsoft, almost 90% of developers said they completed tasks faster with GitHub Copilot.

Coyote Logistics, a third-party logistics provider, utilized GitHub Copilot for Business to save developers time and effort, enabling them to focus on more high-value work and less on nitpicky details. "It used to take me 20 or 30 minutes to write a Terraform configuration," Cloud Delivery Engineer Gavin Borgeson says. "Now it saves me 10 minutes." Once Borgeson writes the base configuration, GitHub Copilot for Business is able to fill in the rest of the details.

**Developers stay in the flow longer**: 73% of developers that were surveyed said GitHub Copilot helps them stay in the flow longer and more easily, and 87% said it helped them preserve mental energy when working through repetitive tasks. Previous research has underscored how disruptive context switching and navigating interruptions can be for developers, and how draining repetitive work can be.

Duolingo, the language-learning app, has a team of more than 300 developers that has accelerated their workflow with their recent adoption of GitHub Copilot. The tool offers two ways for developers to receive suggestions: by starting to write the code they want to use, or by writing natural-language comments that describe what they want the code to do.

Jonathan Burket, a senior engineering manager at Duolingo, explains that GitHub Copilot has increased developer productivity by:
* Limiting context switching.
* Reducing the need to manually produce boilerplate code.
* Helping developers stay focused on solving complex business challenges.

"Boilerplate code is where Copilot is very, very effective. You can practically tab complete the basic class or function using Copilot," says Burket.

For developers who are new to working with a specific repository or framework, for example, Burket estimates at least a 25% increase in developer speed, and a 10% increase for those already familiar with that same codebase, who can more quickly and easily create boilerplate code.

</edukamu-collapse>
<br>


For future AI developers, such as yourself, understanding all the capabilities of GitHub Copilot can be invaluable, especially from a business perspective.

Even though all this might sound quite abstract as of now, using GitHub Copilot can be an effective option from a variety of reasons. As an aspiring Azure developer, consider the following.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Improving Business with GitHub Copilot
</edukamu-collapse-hidden-title>

GitHub Copilot can help businesses across fields and areas of expertise significantly improve their performance. The following are just a few examples.

1. **Enhanced Productivity**: GitHub Copilot streamlines the coding process by providing AI-generated code suggestions. This can significantly reduce the time developers spend on routine and repetitive tasks, allowing them to focus on more complex and critical aspects of Azure development.

*Example*: When developing a cloud-based application on Azure, Copilot can assist in generating code snippets for common tasks such as setting up virtual machines, configuring cloud services, or implementing security measures. This accelerates the development workflow, leading to faster delivery.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Code Consistency and Best Practices</span>: Copilot for Business ensures that the generated code aligns with the organization's coding standards and best practices. This is crucial for maintaining consistency across Azure projects and adhering to industry standards.
</li>
</ol>
</edukamu-section>   

*Example*: If a team follows specific guidelines for deploying resources on Azure, Copilot can be utilized to ensure that the generated deployment scripts, infrastructure-as-code templates, or configuration files consistently adhere to these standards.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Optimized Collaboration</span>: With Copilot, teams working on Azure projects can use consistent and well-structured code, fostering collaboration among developers. Shared understanding of code generated by Copilot can enhance communication and simplify collaborative efforts.
</li>
</ol>
</edukamu-section>  

*Example*: In a scenario where multiple developers are contributing to an Azure solution, Copilot can help maintain coherence in coding styles and patterns, minimizing conflicts and making the collaboration more seamless.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Learning and Skill Enhancement</span>: GitHub Copilot continuously learns from user interactions. For Azure developers, this means that as they work on various Azure-related projects, Copilot adapts and becomes more proficient in suggesting context-aware and Azure-specific code.
</li>
</ol>
</edukamu-section>  

*Example*: For developers new to Azure, Copilot can provide valuable guidance by suggesting code snippets related to common Azure services, functions, and integrations. Over time, it becomes a personalized assistant, tailored to the developer's Azure expertise.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Efficient Troubleshooting</span>: Copilot's ability to understand the context of code can be beneficial for Azure developers when troubleshooting issues. By generating relevant snippets based on error messages or specific scenarios, Copilot aids in quickly identifying and resolving problems.
</li>
</ol>
</edukamu-section>

*Example*: When encountering an error in an Azure Function, Copilot can assist by suggesting potential solutions, helping developers troubleshoot and fix issues efficiently.

In summary, GitHub Copilot for Business can empower Microsoft Azure developers by boosting productivity, ensuring code quality, facilitating collaboration, accelerating learning curves, and providing efficient troubleshooting support in the dynamic and evolving landscape of cloud development.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Setting Up GitHub Copilot for Business
</edukamu-collapse-hidden-title>

If you're willing to use GitHub Copilot in a business setting, you must first establish a few policies. Once GitHub Copilot for Business is enabled at the enterprise level, you can configure GitHub Copilot settings for each organization in your enterprise.

Let's take a brief look at the process.

Follow these steps to enforce a policy to manage the use of GitHub Copilot for Business:
1. In the enterprise sidebar, select **Policies**.
2. Under **Policies**, select Copilot.
3. Under **Manage organization access to GitHub Copilot**, configure the access for your GitHub Copilot subscription.

### Enabling User Access for Organizations

Select your profile photo, then select **Your organizations**.

1. Next to the organization, select **Settings**.
2. In the **Code planning and automation** section of the sidebar, select **Copilot**, then select **Access**.
3. To enable GitHub Copilot for all users in your organization, select **Allow for all members** under **User permissions**.
4. In the **Confirm seat assignment** dialog, confirm that you want to enable GitHub Copilot for all current and future users in your organization, then select **Confirm**.
5. To save your changes, select **Save**.

### Enabling User Access for Selected Users

Start at step 3 from the preceding enabling steps.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
To enable GitHub Copilot for select users in your organization, select <span style="font-weight: bold">Selected teams/users</span> under <span style="font-weight: bold">User permissions</span>.
</li>
</ol>
</edukamu-section>  
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the <span style="font-weight: bold">Confirm seat assignment</span> dialog, confirm that you want to enable GitHub Copilot for selected teams/users in your organization, then select <span style="font-weight: bold">Confirm</span>.
</li>
</ol>
</edukamu-section>  
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
To save your changes, select <span style="font-weight: bold">Save</span>.
</li>
</ol>
</edukamu-section>

### Disabling Access at an Organizational Level

Start at step 3 from the preceding enabling steps.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
To disable GitHub Copilot for all users in your organization, select <span style="font-weight: bold">Disabled</span> under the <span style="font-weight: bold">User permissions</span> section.
</li>
</ol>
</edukamu-section>  
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the <span style="font-weight: bold">Confirm seat assignment</span> dialog, confirm that you want to disable GitHub Copilot for selected teams/users in your organization, then select <span style="font-weight: bold">Confirm</span>.
</li>
</ol>
</edukamu-section>  
<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
To save your changes, select <span style="font-weight: bold">Save</span>.
</li>
</ol>
</edukamu-section>

Even though enabling GitHub Copilot for Business might not be the most current thing on your task list, it never hurts to be aware of how the process goes! It's quite simple, as you've just witnessed.

</edukamu-collapse>
<br>


GitHub is aimed at development teams of all shapes and sizes. When used professionally, it can also offer significant advantages for business.

Let's finish up the second unit with a little exercise, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Improving Business with GitHub Copilot
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module2/github-copilot-for-business-text-poll.yaml" id="v51p4289778db4su"/>
<br>
<edukamu-text-poll url="/exercises/module2/github-copilot-for-business-text-poll-2.yaml" id="60d8oq38zidihib7"/>
<br>
<edukamu-text-poll url="/exercises/module2/github-copilot-for-business-text-poll-3.yaml" id="2563qx7177wxwrk6"/>
<br>
<edukamu-text-poll url="/exercises/module2/github-copilot-for-business-text-poll-4.yaml" id="l921r7896m04xwg5"/>
<br>
<edukamu-text-poll url="/exercises/module2/github-copilot-for-business-text-poll-5.yaml" id="hg54e56054f1va66"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/2/github-copilot-for-business?question=v51p4289778db4su">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


Over the course of the first two units, we've explored GitHub Copilot from quite a few angles and learned about its capabilities. In the third unite, we'll start moving from theory to practice and learn to improve our code with GitHub Copilot.

Take a moment to rest and review before moving on. See you in the third and final unit!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
