## GitHub Copilot and Python

Python is a programming language known for its simplicity and versatility: its elegant syntax makes it a favorite for beginners and seasoned developers alike. More specifically, Python excels in web development, data analysis, machine learning, and automation.

On this page we'll learn how GitHub Copilot can help anyone working with Python. We'll explore the possibilities like we did earlier with JavaScript.

Shall we get started?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Python
</edukamu-collapse-hidden-title>

JavaScript and Python are both programming languages that are used to develop applications and other types of software. They are high-level, interpreted languages used for a wide range of scenarios, including web development, software engineering, data science, and more. Programmers use these languages to write instructions that computers can understand and execute to perform various tasks and functions.

JavaScript is often associated with web development, while Python is known for its versatility across different domains. Let's explore the characteristics of Python a bit further.


### Python

#### 1. Data Science and Machine Learning:

**Example**: Developing a program that predicts if a given email is spam or not, helping filter unwanted emails from your inbox.

#### 2. Web Development (Django, Flask):

**Example**: Building a personal blog where you can easily create, edit, and organize your posts without needing extensive coding knowledge.

#### 3. Scripting and Automation:

**Example**: Writing a script that renames and organizes your photo collection based on the date they were taken, saving you manual effort.

#### 4. Scientific Computing:

**Example**: Creating a simple program to analyze data from a school science experiment, like tracking the growth of plants under different conditions.

In summary, Python can be the programming language of choice in diverse scenarios, from simplifying daily tasks to solving complex problems in areas like data analysis and machine learning.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Example: Python in Use
</edukamu-collapse-hidden-title>

Imagine a scenario in which you want to automate a repetitive task at your workplace, like managing and organizing files. Python can be a valuable tool in this context. Here's how:

### 1. File Organization Script:
* **Python Use Case**: You have a folder with hundreds of files from different projects. With Python, you can write a script that organizes these files into separate folders based on project names or file types. This automation saves time and ensures a tidy file structure.

### 2. Data Analysis for Business Insights:
* **Python Use Case**: Your company collects data on customer interactions. Python can be used to analyze this data, providing insights into customer behavior, preferences, and trends. This information can even be used to build business strategies and help decision-making.

### 3. Automated Email Responses:
* **Python Use Case**: If you receive a large volume of similar emails that require standard responses, Python scripts can be used to automate email replies. For instance, acknowledging receipt of inquiries or sending follow-up messages.

In summary, Python shines in scenarios in which automation, data analysis, and scripting are needed, making it a versatile choice for improving efficiency in various business processes.

</edukamu-collapse>
<br>


In summary, many programmers choose Python because of its versatility, readability, and suitability for a wide range of applications, including data science and backend web development.

As we did before, we'll next explore how GitHub Copilot can be used to make code written in Python even more advanced and skillful! First, we'll again need to set up GitHub Copilot to work with Visual Studio Code.

Along the road, we'll learn to:

* Configure a GitHub repository in Codespaces and install GitHub Copilot extension.
* Use crafted prompts to generate suggestions from GitHub Copilot.
* Apply GitHub Copilot to improve your projects in Python.

<edukamu-note class="edukamu-note-icon-info">
**Important**

The following setup process is quite similar to what we already did with JavaScript, but make sure to complete it. In order to use GitHub Copilot with Python, we'll need to install a special Web API (don't worry, it's quick and simple!). If you already set up an environment before, feel free to jump straight into the API section. Good luck!
</edukamu-note>
<br>


Let’s begin!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Setting up GitHub Copilot for JavaScript
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

Please notice that setting up GitHub Copilot for JavaScript requires a subscription. You can begin a free trial period (30 days) over at the GitHub website - that will give you plenty of time to complete the practical exercises on this course, if you feel like completing them.

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


### Python Web API

When complete, Codespaces loads with a terminal section at the bottom. Codespaces installs all the required extensions in your container. Once the package installs are completed, Codespaces will execute the uvicorn command to start your web application running within your Codespace.

When the web application has successfully started, a message in the terminal shows that the server is running on port 8000 within your Codespace.

### Testing the API

Try to interact with the API by sending a request using the self-documented page. Select the POST button and then on the Try it Out button. If everything works well, feel free to move forward! If not, please review the instructions above.

</edukamu-collapse>
<br>


After completing the steps described above, we're all set to begin enhancing Python with GitHub Copilot!

Before beginning, please review the tips and tricks we discussed in the last section when working with JavaScript. We've pasted them here for your convenience.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Getting the Most out of GitHub Copilot with Python
</edukamu-collapse-hidden-title>

Soon, we'll explore how GitHub Copilot can help you with Python in practice.

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

Keep your prompts simple then add more elaborate components as you keep going for example: `: create an HTML form with a text field and button`

Next, elaborate more on the prompt to get more specific suggestions:

`Add an event listen to the button to send a POST request to /generate endpoint and display response in a div with id "result"`

Cycle between suggestions, you can do this using `Ctrl+Enter` (or `Cmd+Enter` on a Mac). You get various suggestions from Copilot, and you can pick the best output.

If you're stuck or not getting the results you want, then you can reword the prompt or start writing code for Copilot to autocomplete.

**Note**: GitHub Copilot uses open files in your text editor as additional context. This is helpful because it provides useful information in addition to the prompt or code you may be writing. If you need GitHub Copilot to provide suggestions based on other files, remember to have those open for more accurate suggestions.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-green">
In the next practice exercise, we'll review updating a Python web API with GitHub Copilot.

If you've completed the previous courses of this micro degree, you should already be familiar with APIs, or Application Programming Interfaces. In summary, it is a set of rules and tools that allows different software applications to communicate with each other.

If you use a weather app on your phone, an API could be used to fetch real-time weather data from an external service. For instance, the app might use a weather API that allows it to send a request for the current weather conditions of a specific location. The API then responds with the relevant data, such as temperature, humidity, and weather conditions.

In the context of GitHub Copilot, APIs act as the intermediary that allows different applications to communicate to each other. For example, a weather website can either share historical data or provide forecast functionality through its API. Using the API, you can embed the data into your website or create an application sharing weather data with other features.

All right, let’s get busy with updating APIs.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Updating Python Web API with GitHub Copilot
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

Let's explore how you can modify a Python repository using code suggestions from GitHub Copilot to create an interactive HTML form and an Application Programming Interface (API) endpoint. By working with this repository, you'll quickly get hands-on with a Python web app that serves an HTTP API that generates a pseudo-random token, commonly used in for identification.

### Extending the Python Web API

The API already has a single endpoint to generate a token. Let's update the API by adding a new endpoint that accepts text and returns a list of tokens.

For this exercise, use the Codespace with the preconfigured environment in your browser. We've set up an environment earlier in this unit.

#### 1. Adding a Pydantic Model

Go to the `main.py` file, and add a comment so that GitHub Copilot can generate a `Pydantic` model for you. The generated model should look like this:

```
class Text(BaseModel):

text: str
```

#### 2. Generating a New Endpoint

Next, generate a new endpoint with GitHub Copilot by adding the comment:

`# Create a FastAPI endpoint that accepts a POST request with a JSON body containing a single field called "text" and returns a checksum of the text`

#### 3. Adding Necessary Imports

The generated code causes the application to crash. The crash happens because the base64 and os modules aren't imported. Add the following lines to the top of the file:

```
import base64
import os
```

Finally, verify the new endpoint is working by trying it out by going to the /docs endpoint and confirming that the endpoint shows up.

This is just a little example of what GitHub Copilot is capable of, and we highly recommend that you explore the service to your heart's content if you have the opportunity!

</edukamu-collapse>
<br>


Hopefully the materials we've reviewed on this page have helped you see the opportunities that GitHub Copilot provides for everyone working with Python! If you’ve used the programming language before, maybe you could show some of your work to GitHub Copilot and even improve it with the help of your brand new AI assistant?

Before wrapping up this section, there's one more aspect to consider.

Imagine having already written some code, say, for an application. GitHub Copilot is not only there to help you write new lines but to improve existing code as well! The process is fairly simple, as you'll soon see.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Improving Written Code with GitHub Copilot
</edukamu-collapse-hidden-title>

GitHub Copilot can be a valuable tool for checking, assessing, and improving existing code. When working with codebases, you can use Copilot to generate suggestions and improvements for specific sections or functions and even assess already-existing code for potential flaws and shortcomings!

GitHub Copilot can indeed help you improve your code in many ways. In the following example, we're trying to improve a function that calculates the are of a rectangle.

### Step 1: Inserting Existing Code

Let's imagine we've written the following function to calculate the area of a rectangle:

```
function calculateRectangleArea(length, width) {
    return length * width;
}
```

We can paste this function to GitHub Copilot's code editor and assess it in a few simple steps.

### Step 2: Generating Suggestions

Let's say we're interested in how well the code works. By highlighting the `calculateRectangleArea` in the code editor, we can receive suggestions from GitHub Copilot. It might offer improvements or variations of the existing code.

### Step 3: Reviewing Suggestions

After receiving the ideas of improvement, the logical next step is to assess and review them.

Let's say GitHub Copilot comes up with the following suggestion:

```
// Suggestion: Use ES6 arrow function syntax
const calculateRectangleArea = (length, width) => length * width;
```

At this stage, it would be our turn to review the suggestion and consider whether using a suggested arrow function syntax aligns with the project's style and standards.

### Step 4: Accepting or Customizing Suggestions

After reviewing the suggestion, it's time to either accept, reject, or customize it.

We would freely be able to customize the suggested syntax or just leave it as is.

### Step 5: Iterating for Improvement

We would then be able to use the improved syntax in our original code and improve it. Afterwards, we could for example assess and improve error handling in another function based on Copilot's suggestions. The possibilities are virtually limitless!

Remember, these examples are simplified, and in a real-world scenario, you'd carefully evaluate each suggestion to ensure it meets your project's requirements and doesn't introduce unintended consequences. Copilot serves as a helpful assistant, but the final decision rests with the developer.

</edukamu-collapse>
<br>


GitHub Copilot supports a wide range of programming languages. If you've ever written code yourself, changes are that your language of choice is already available within the service.

Core languages supported by GitHub services include C, C++, C#, Go, Java, JavaScript, PHP, Python, Ruby, Scala, and TypeScript, and new features for each supported language are constantly being added.

Now, in order to consolidate your new knowledge, take some time to review before completing the following exercise.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: GitHub Copilot with Python
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/github-copilot-and-python-question-scroll.yaml" id="t010041r3zvrsgcu">
<br>

</edukamu-collapse>
<br>


Can you already see yourself writing amazing code with GitHub Copilot on your side? You might not be there yet, but remember that, with your new AI-powered sidekick, you're never alone!

It's time for the last topic of this course: GitHub Actions. Let's go!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
