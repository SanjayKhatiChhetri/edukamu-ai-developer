<edukamu-video content="/videos/devai-4-unit3-video.yaml"/>
<br>

## GitHub Copilot and JavaScript

GitHub Copilot, armed with seemingly endless computational power and information, makes writing code simpler and more efficient across all imaginable use cases. As we learned in the second unit, the service can be fine-tuned to the detail, which enables tailored user experiences for individuals and businesses alike.

On this third and final unit of this course, we'll explore how GitHub Copilot can be used when working with JavaScript or Python – two of the best-known programming languages. We'll move from theory to practice, and you'll also get to try out the service yourself in a few practical exercises (which, as you remember, are optional!).

In case you're not familiar with JavaScript and/or Python, we'll start with a little introduction. On this page, we'll focus on JavaScript. On the next, it's time for Python.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to JavaScript
</edukamu-collapse-hidden-title>

JavaScript and Python are both programming languages that are used to develop applications and other types of software. They are high-level, interpreted languages used for a wide range of scenarios, including web development, software engineering, data science, and more. Programmers use these languages to write instructions that computers can understand and execute to perform various tasks and functions.

JavaScript is often associated with web development, while Python is known for its versatility across different domains. Let's explore the characteristics of JavaScript a bit further.

### JavaScript

JavaScript stands as the cornerstone of web development, empowering websites with dynamic and interactive features. As a client-side scripting language, it runs directly in web browsers, enabling developers to create responsive user interfaces. JavaScript is instrumental in building modern web applications, handling events, manipulating the DOM (Document Object Model), and facilitating seamless communication with servers.

Consider the following use cases:

#### 1. Front-End Web Development:

**Example**: Adding a live search feature to a website, where the search results update dynamically as you type. This enhances user experience by providing instant feedback.

#### 2. Back-End Development:

**Example**: Creating a server that handles real-time notifications in a chat application. This ensures messages are delivered instantly to users.

#### 3. User Interface Development:

**Example**: Building a responsive and interactive form on a social media site, allowing users to post comments, like posts, and see updates without refreshing the page.

JavaScript is by no means the only option for the scenarios described above, but it's among the most flexible! When there is a need to enhance user interfaces and interactions on websites, JavaScript excels.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Example: JavaScript in Use
</edukamu-collapse-hidden-title>

Imagine you're building an online shopping website. In this scenario, JavaScript would play a crucial role in creating a seamless and interactive shopping experience for users. Here's how:

### Shopping Cart Interaction:

* **JavaScript Use Case**: When a user adds an item to their cart, JavaScript can dynamically update the cart icon, showing the current number of items. It can also enable a smooth dropdown or slide-in animation to display the added item details without refreshing the entire page.

### Real-Time Price Calculation:
 
* **JavaScript Use Case**: As users select different quantities or variations of products, JavaScript can instantly calculate and display the updated total price. This ensures customers have a clear understanding of their expenses as they shop.

### User Feedback on Form Submission:

* **JavaScript Use Case**: When a user completes an order form, JavaScript can provide immediate feedback, such as a confirmation message or highlighting any missing information. This real-time response enhances user satisfaction and reduces confusion.

In summary, JavaScript excels in creating dynamic and engaging user interfaces, making it ideal for scenarios in which interactivity and responsiveness are key, such as in e-commerce websites.

</edukamu-collapse>
<br>


JavaScript can make a huge impact when creating smooth user experiences, and GitHub Copilot is there to make sure that even beginners can learn to use JavaScript in no time! 

The following sections contain code snippets that can be difficult to understand if you’re not familiar with JavaScript. If something feels confusing, don’t worry – you can still understand the basic principles!

Without further ado, let' dive right in and start by setting up GitHub Copilot to work with Visual Studio Code!

Soon, we'll learn to:
* Configure a GitHub repository in Codespaces and install GitHub Copilot extension.
* Use crafted prompts to generate suggestions from GitHub Copilot.
* Apply GitHub Copilot to improve your projects in JavaScript.

Let’s get started!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Setting up GitHub Copilot for JavaScript
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

Also notice that setting up GitHub Copilot for JavaScript requires a subscription. You can begin a free trial period (30 days) over at the GitHub website. That will give you plenty of time to complete the practical exercises on this course.

<edukamu-button url="https://github.com/github-copilot/signup">GitHub Copilot: Free Trial</edukamu-button>
<br>

**Note**: Educators, Students and select open-source maintainers can sign up for Copilot for free. More information is available in [Microsoft website](https://techcommunity.microsoft.com/t5/educator-developer-blog/step-by-step-setting-up-github-student-and-github-copilot-as-an/ba-p/3736279?WT.mc_id=academic-91025-alfredodez)(target="_blank"). 


### Setting Up an Environment

First you need to launch the Codespaces environment, which comes preconfigured with the GitHub Copilot extension.
1. Open the Codespace with the preconfigured environment in your browser.

<edukamu-button url="https://codespaces.new/MicrosoftDocs/mslearn-copilot-codespaces-javascript?quickstart=1">Open Codespace</edukamu-button>
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
On the <span style="font-weight: bold">Create codespace</span> page, review the codespace configuration settings and then select <span style="font-weight: bold">Create new codespace</span>.
</li>
</ol>
</edukamu-section>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Wait for the codespace to start. This startup process can take a few minutes.
</li>
</ol>
</edukamu-section>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
The remaining exercises in this project take place in the context of this development container.
</li>
</ol>
</edukamu-section>

**Important**: All GitHub accounts can use Codespaces for up to 60 hours free each month with two core instances. For more information, see GitHub Codespaces monthly included storage and core hours.


### JavaScript Portfolio

When complete, Codespaces loads with a terminal section at the bottom. Codespaces installs all the required extensions and dependencies in your container. Once complete, Codespaces uses npm start to start the web application within your Codespace.

When the web application has successfully started, a message in the terminal shows that the server is running on port 1234 within your Codespace.

After completing the steps described above, you're all set to continue!

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Getting the Most out of GitHub Copilot with JavaScript
</edukamu-collapse-hidden-title>

Soon, we'll explore how GitHub Copilot can help you with JavaScript in practice.

Often when we build out projects, we need to continuously ensure our code is fresh and updated. Additionally, we might need to fix any bugs that come up or add new features to improve its functionality and usability. Let's explore some ways to make updates with GitHub Copilot.

### Tip: Prompt Engineering

As this stage, you should already be familiar with prompt engineering. Although GitHub Copilot can suggest code as you type, you can also build prompts to create useful suggestions. A prompt, which is our input, is a collection of instructions or guidelines that help generate code. A prompt is useful to generate specific responses from Copilot. The prompt might be a comment that steers Copilot to generate code on your behalf or writing code that Copilot autocompletes.

The quality of output from Copilot is dependent on how well you craft your prompt. Designing an effective prompt is, therefore, crucial in ensuring we achieve our desired outcomes. For example, if you have the following prompt:

`// Create an API endpoint`

Since the prompt is ambiguous and vague, the result from GitHub Copilot might not be what you need. For example, it could use a framework that you don't know, or an endpoint that requires data that you don't recognize. However, if you have the following prompt:

`// Create an API endpoint using the React framework that accepts a JSON payload in a POST request`

This last prompt is specific, clear and allows GitHub Copilot to understand the goal and scope of the task. You can also provide context and examples to Copilot using both comments and code. Having a good prompt ensures that the model generates a high-quality output.

### Best Practices

Copilot supercharges your productivity but requires some good practices to ensure quality. Some best practices when using Copilot are:

Keep your prompts simple then add more elaborate components as you keep going for example:

`: create an HTML form with a text field and button`

Next, elaborate more on the prompt to get more specific suggestions:

`Add an event listen to the button to send a POST request to /generate endpoint and display response in a div with id "result"`

Cycle between suggestions, you can do this using `Ctrl+Enter` (or `Cmd+Enter` on a Mac). You get various suggestions from Copilot, and you can pick the best output.

If you're stuck or not getting the results you want, then you can reword the prompt or start writing code for Copilot to autocomplete.

**Note**: GitHub Copilot uses open files in your text editor as additional context. This is helpful because it provides useful information in addition to the prompt or code you may be writing. If you need GitHub Copilot to provide suggestions based on other files, remember to have those open for more accurate suggestions.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Updating a JavaScript Portfolio with GitHub Copilot
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

Let's explore how you can use code suggestions from GitHub Copilot. In this exercise, you add animations with live suggestions and use a prompt to customize scroll behavior from an already existing JavaScript template repository. With GitHub Copilot, you can quickly work with a real-life JavaScript situation.


### JavaScript Portfolio

Whether you're a student, recent graduate, or an experienced professional, your portfolio is your personal space to showcase your skills and experience.

Having a portfolio provides credibility and notoriety to the experience you're mentioning in your resume when applying for jobs. Whether you're a Data Scientist, UX Designer, or a Front-end developer. A strong online presence can help you get a job and be discovered!

**Note**: For this exercise, use the Codespace with the preconfigured environment in your browser. We set this environment up a while back on this page.


### Customizing Your JavaScript Portfolio

In this template portfolio, we have a React based web application ready for you to easily customize and deploy using only your web browser.

Before starting, you can customize the portfolio with your own links. Go to `src/App.jsx` and update the `siteProps` with your information. The `siteProps` variable is a JavaScript object that holds key value pairs used to customize the site, it should look like this:

```
const siteProps = {
  name: "Alexandrie Grenier",
  title: "Web Designer & Content Creator",
  email: "alex@example.com",
  gitHub: "microsoft",
  instagram: "microsoft",
  linkedIn: "satyanadella",
  medium: "",
  twitter: "microsoft",
  youTube: "Code",
};
```

### Animating Social Media Icons with Prompts

An animation can make the social media section more eye-catching. Ask Copilot’s help to animate the icons. Write the following prompt in the `src/styles.css` file:

`/* add an amazing animation to the social icons */`

The suggestion from Copilot should look similar to the following:

```
img.socialIcon:hover {
  animation: bounce 0.5s;
  animation-iteration-count: infinite;
}

@keyframes bounce {
  0% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.2);
  }
  100% {
    transform: scale(1);
  }
}
```

Accept the suggestion by pressing the tab key. If you don't receive the exact same suggestion, then you can either experiment with the suggestion provided or keep typing the CSS code until it matches.

Your site should already be running in your Codespace, and the change will reload onto the page automatically. To see them, hover over one of your social media icons in the footer to see the magic!

Please try out the code snippets and prompts for yourself. Take advantage of that GitHub Copilot trial you activated earlier!

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-green">
How was it? Did you manage to see GitHub Copilot in action? Hopefully you did, since practicing the things we learn always makes them easier to remember and understand.

If you're familiar with JavaScript, you might already be able to imagine the endless opportunities such a service provides! However, even if you're new to the programming world, you should already have an idea of just how handy GitHub Copilot can be. The best thing is that it can even help beginning programmers learn new skills quicker than ever before!

Please notice that we only cover a handful of quite simple use cases on this course. If the examples presented here seem too simple for you, feel free to explore GitHub Copilot for yourself! Maybe you can even take the last project you created with JavaScript and see what your new AI-powered assistant would suggest...

All right, it's time to review what we've learned on this page. Take a moment to recap before completing the following exercise!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: GitHub Copilot in Action
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/github-copilot-and-js-question-scroll.yaml" id="h7o8po76710z86x8">
<br>

</edukamu-collapse>
<br>


If you are not familiar with programming, understanding the nuances of GitHub Copilot might seem difficult, but don't worry! Being familiar with how the service operates will still come in handy if and when you do start to use GitHub in a professional context.

It's time to move on to the next topic! As promised, we'll explore how GitHub Copilot can be of assistance when using a programming language called Python. Can you still remember its main characteristics?

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
