## Prompt Engineering

Generative AI services aimed at general public is oftentimes used by writing detailed instructions often referred to as prompts. Prompts are like commands that make the service do what you need it to: think of them as instructions you'd give to an assistant.

The more detailed your instructions are, the easier it becomes for your assistant to fulfill your requests comprehensively. This is also the main reason why so-called prompt engineering is so important when using generative AI.

On this page, we'll get familiar with prompt engineering. In order to really make the most of generative AI and GitHub Copilot, you should take the time to really hone your prompts!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Prompt Engineering
</edukamu-collapse-hidden-title>

Prompt engineering is the process of crafting clear instructions to guide AI systems, like GitHub Copilot, to generate context-appropriate code tailored to your project's specific needs. This ensures the code is syntactically, functionally, and contextually correct. Think of it like giving precise directions to a driver. Without them, the journey might be inefficient. But with clear guidance, the route becomes direct and efficient, saving time and energy. In this scenario, you're the one providing directions, and GitHub Copilot is your skilled driver, ready to drive you smoothly through your coding journey with the right guidance.

Now that you know what prompt engineering is, let's learn about some of its principles.

### Principles of Prompt Engineering

Before we explore specific strategies, let's first understand the basic principles of prompt engineering, summed up in the **4 S's** below. These core rules are the basis for creating effective prompts.
* **Single**: Always focus your prompt on a single, well-defined task or question. This clarity is crucial for eliciting accurate and useful responses from Copilot.
* **Specific**: Ensure that your instructions are explicit and detailed. Specificity leads to more applicable and precise code suggestions.
* **Short**: While being specific, keep prompts concise and to the point. This balance ensures clarity without overloading Copilot or complicating the interaction.
* **Surround**: Utilize descriptive filenames and keep related files open. This provides Copilot with rich context, leading to more tailored code suggestions.

These core principles lay the foundation for crafting efficient and effective prompts. Keeping the 4 S's in mind, let's dive deeper into advanced best practices that ensure each interaction with GitHub Copilot is optimized.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Best Practices of Prompt Engineering
</edukamu-collapse-hidden-title>

The following advanced practices, based on the 4 S's described before, refine and enhance your engagement with Copilot, ensuring that the generated code isn't only accurate but perfectly aligned with your project's specific needs and contexts.

### 1. Clarity

Building on the 'Single' and 'Specific' principles, always aim for explicitness in your prompts. For instance, a prompt like "Write a Python function to filter and return even numbers from a given list" is both single-focused and specific.

<edukamu-image url="/graphics/module2/2-python-prompt.png" alt="Screenshot of a Copilot chat with a Python prompt."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

### 2. Details and Context

Enrich Copilot's understanding with context, following the 'Surround' principle. The more contextual information provided, the more fitting the generated code suggestions are. For example, by adding some comments at the top of your code to give more details to what you want, you can give more context to Copilot to understand your prompt, and provide better code suggestions.

<edukamu-image url="/graphics/module2/2-add-comments-example.gif" alt="Animation. Comments added to code for better Copilot suggestions."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

In the example above, we used steps to give more detail while keeping it short. This practice follows the 'Short' principle, balancing detail with conciseness to ensure clarity and precision in communication.

**Note**: Copilot also uses parallel open tabs in your code editor to get more context on the requirements of your code.

### 3. Examples for Learning

Using examples can clarify your requirements and expectations, illustrating abstract concepts and making the prompts more tangible for Copilot.

<edukamu-image url="/graphics/module2/2-clarify-prompts-example.gif" alt="Animation of an example used to clarify prompts for Copilot."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

### 4. Assert and Iterate

One of the keys to unlocking GitHub Copilot's full potential is the practice of iteration. Your first prompt might not always yield the perfect code, and that's perfectly okay. If the first output isn't quite what you're looking for, treat it as a step in a dialogue. Erase the suggested code, enrich your initial comment with added details and examples, and prompt Copilot again.

</edukamu-collapse>
<br>


Just as traditional assistants depend on detailed instructions, the effectiveness of an AI model relies on the prompts given to it. These prompts are the questions, commands, or inputs that guide the model to generate responses. This process of tailoring prompts for optimal outcomes is what we call prompt engineering.

In our city analogy, think of the prompts as the requests you make to city departments. If you ask for information about traffic in your neighborhood at 10am on a typical Tuesday, you'd not only message the transportation department but also provide details on the information which you’re after. Similarly, crafting effective prompts involves understanding how to articulate your queries to get the most accurate and valuable responses from your AI model.

Now that we've started improving our prompting skills, let's take a closer look at how we can provide examples from which the GitHub Copilot can learn.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Prompts and Learning
</edukamu-collapse-hidden-title>

GitHub Copilot operates based on AI models trained on vast amounts of data. To enhance its understanding of specific code contexts, engineers often provide it with examples. This practice, commonly found in machine learning, led to different training approaches such as:

### 1. Zero-shot Learning

Here, GitHub Copilot generates code without any specific examples, relying solely on its foundational training. For instance, suppose you want to create a function to convert temperatures between Celsius and Fahrenheit. You can start by only writing a comment describing what you want, and Copilot might be able to generate the code for you, based on its previous training, without any other examples.

<edukamu-image url="/graphics/module2/2-create-temp-conversion-from-comment.png" alt="Screenshot of Copilot creating a temperature conversion code from a comment." style="max-width: 70%;"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

### 2. One-shot Learning

With this approach, a single example is given, aiding the model in generating a more context-aware response. Building upon the previous zero-shot example, you might provide an example of a temperature conversion function and then ask Copilot to create another similar function. Here's how it could look:

<edukamu-image url="/graphics/module2/2-create-temp-conversion-from-example.png" alt="Screenshot of Copilot using an example to create similar temperature conversion code." style="max-width: 70%;"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

### 3. Few-shot Learning

In this method, Copilot is presented with several examples, which strike a balance between zero-shot unpredictability and the precision of fine-tuning. Let's say you want to generate code that sends you a greeting depending on the time of the day. Here's a few-shot version of that prompt:

<edukamu-image url="/graphics/module2/2-generate-greeting-code-from-examples.png" alt="Screenshot of Copilot generating greeting code based on multiple examples."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-green">
As you see, GitHub Copilot not only provides you with personally tailored code solutions, but it also keeps on learning. As you continue working with it, it will keep getting more and more effective – as will your prompts!

Next, let's take an in-depth look at how GitHub Copilot actually uses your prompt to suggest code for you.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Step-by-Step: From Prompts to Code
</edukamu-collapse-hidden-title>

Let's briefly walk through all the steps Copilot takes to process a user's prompt into a code suggestion.

<edukamu-image url="/graphics/module2/3-prompt-processing-flow-diagram.png" alt="Diagram of the GitHub Copilot prompt processing flow." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

### 1. Securing Prompt Transmission and Context Gathering

he process begins with the secure transmission of the user prompt over HTTPS. This ensures that your natural language comment is sent to GitHub Copilot's servers securely and confidentially, protecting sensitive information.

GitHub Copilot securely receives the user prompt, which could be a Copilot chat or a natural language comment provided by you within your code.

Simultaneously, Copilot collects context details:
* Code before and after the cursor position, which helps it understand the immediate context of the prompt.
* Filename and type of the file being edited, allowing it to tailor code suggestions to the specific file type.
* Information about adjacent open tabs, ensuring that the generated code aligns with other code segments in the same project.

### 2. Filtering Content

Copilot incorporates content filtering mechanisms before proceeding with intent extraction and code generation, to ensure that the generated code and responses don't include or promote:
* **Personal data**: Copilot actively filters out any personal data, such as names, addresses, or identification numbers, to protect user privacy and data security.
* **Hate speech and inappropriate content**: Copilot employs algorithms to detect and prevent the generation of hate speech, offensive language, or inappropriate content that could be harmful or offensive.

### 3. Analyzing Context

After content filtering, Copilot uses the gathered context information, including code snippets and file type, to contextualize the user's prompt. This comprehensive context helps Copilot understand the prompt's relevance and the coding task it's meant to address. Copilot understands the context and carries out the following:
* **Extract intent**: Copilot proceeds to extract your intent from the natural language comment. It identifies keywords, phrases, and context cues within the prompt.
* **Intent mapping**: Copilot maps the extracted intent to specific coding actions or functionalities, considering both the prompt's content and the contextual information. This step translates the user's high-level request into a concrete coding task.

### 4. Generating Code

Copilot, informed by mapped intent, completes the following actions:
* Delivers code suggestions tailored to your code preferences.
* Proposes apt function and variable names.
* Crafts complete code blocks ensuring syntax and context accuracy.
* Aligns with the project's specific language, framework, and standards.
* Respects customized settings like coding styles and constraints.

### 5. User Interaction

You're presented with the generated code for review and interaction, and have the options to:
* Accept the code as-is.
* Make modifications to the suggested code.
* Reject the code suggestions.

### 6. Feedback

Copilot initiates a feedback loop based on your actions to achieve the following:
* Grow its knowledge from accepted suggestions.
* Learn and improve through modifications and rejections of its suggestions.

### 7. Prompt History Retention

Throughout the coding session, Copilot retains a history of prompts, context details, and interactions. This history serves as a contextual reference, allowing Copilot to provide consistent and coherent suggestions.

### 8. Repetition

The process is repeated as you provide more prompts, with Copilot continuously handling user requests, understanding their intent, and generating code in response. Over time, Copilot applies the cumulative feedback and interaction data, including context details, to improve its understanding of user intent and refine its code generation capabilities.

</edukamu-collapse>
<br>


In a nutshell, that's how GitHub Copilot turns your ideas into code in no time, making your work significantly smoother and more effortless. By learning to design and write effective prompts, the entire software development can reach a whole new level.

We've now taken an extensive tour of the capabilities of GitHub Copilot. With this being the case, it's time for another exercise!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: GitHub Copilot
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/prompt-engineering-question-scroll.yaml" id="ajbc84zi7falz6gb">
<br>

</edukamu-collapse>
<br>


How was it? Are you starting to get the hang of GitHub Copilot?

On the next page, we'll learn how GitHub Copilot can help boost your business!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
