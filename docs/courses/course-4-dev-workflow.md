---
title: "Course 4: Accelerating Development Workflow"
layout: default
nav_order: 6
parent: Courses
---

# Course 4: Accelerating Development Workflow

**URL:** [https://cs.edukamu.fi/accelerating-development-workflow](https://cs.edukamu.fi/accelerating-development-workflow)  
**Sections:** 11  

---

## Table of Contents

- **Unit 1:** Administration In Github | Collaboration In Github | Introduction To Github ...
- **Unit 2:** Github Copilot For Business | Introduction To Github Copilot | Prompt Engineering
- **Unit 3:** Automating Workflows With Github Actions | Github Copilot And Javascript | Github Copilot And Python ...

---

## Unit 1

### Administration In Github

**TL;DR:** Imagine GitHub as a bustling city, in which people live and work in harmony with each other completing daily tasks and achieving great feats by solving issues through discussions. In a city like this, infrastructure is vital, since without it, the city as a whole just wouldn't work.

**Topics covered:**
- 1. Administration at Team Level
- Best Practices
- 2. Administration at Organization Level
- 3. Administration at Enterprise Level
- Deploy Keys
- Personal Access Tokens
- SSH Keys
- Deploy Keys
- Enhanced Security Options
- 1. Two-factor Authentication

**Key Points:**
- Create a new team, and select or change the parent team.
- Add or remove organization members from a team, or synchronize a GitHub team's membership with an IdP group.
- Add or remove outside collaborators (people who aren't explicitly members of your organization, such as consultants or temporary employees) from team repositories.
- Enable or disable team discussions on the team's page.
- Change the visibility of the team within the organization.
- Manage automatic code review assignment for pull requests, utilizing GitHub's review assignment routing algorithm.
- Create nested teams to reflect your group or company's hierarchy within your GitHub organization.
- Create teams based on interests or specific technology (JavaScript, data science, etc.) to help streamline PR review processes. Individuals can choose to join these teams according to their interests...

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Collaboration In Github

**TL;DR:** While GitHub can be used alone as well, it's a collaborative platform at its core. On this page, we'll review the main tools it offers for effective and productive teamwork.

**Topics covered:**
- Introduction to Issues
- Creating Issues
- Introduction to Discussions
- Enabling Discussions
- Creating Discussions
- Platform Management
- Subscriptions and Notifications
- GitHub Pages
- Practice: Exploring GitHub
- Additional Instructions:

**Key Terms:**

| Term | Definition |
|------|-----------|
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |
| Who is this for | New developers, new GitHub users, and students. |
| What you'll learn | We'll introduce repositories, branches, commits, and pull requests. |
| What you'll build | We'll make a short Markdown file you can use as your [profile... |
| Prerequisites | None. This practice exercise is a great introduction for your first day on GitHub. |
| How long | It will take around an hour to complete this exercise. |
| Create repository | button at the bottom of the form. |

**Key Points:**
- a comment in an issue or pull request
- Enabling a discussion in your repository
- Creating a new discussion and various discussion categories
- Managing notifications and subscriptions.
- Subscribing to threads and finding threads you're mentioned in.
- Publicizing your or your organization on GitHub pages.
- A conversation in a specific issue, pull request, or gist.
- CI activity, such as the status of workflows in repositories set up with GitHub Actions.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Introduction To Github

**TL;DR:** <edukamu-video content="/videos/devai-4-unit1-video.yaml"/>
<br>

**Topics covered:**
- Getting to Know GitHub
- What is Version Control?
- Understanding and Using Repositories
- Setting Up a Repository
- Adding Files
- Gists and Wikis
- Gists
- Wikis
- Branches and Commits
- Branches

**Key Terms:**

| Term | Definition |
|------|-----------|
| Version Control | GitHub uses Git, a distributed version control system, to track changes in source code during software development. This allows multiple contributors to work on the same project... |
| Repositories | Projects on GitHub are organized into repositories, which can contain code, images, text, or any other resource related to the project. Repositories can be public (visible to... |
| Collaboration | GitHub facilitates collaboration through features such as pull requests, issues, and discussions. Developers can propose changes to a project through pull requests, and... |
| Community and Social Coding | GitHub fosters a strong community around open source development. Developers can discover projects, contribute to others' work, and build a portfolio of their own contributions. |
| Wikis and Documentation | Repositories can include wikis and documentation to provide information about the project, its structure, and ways to contribute. This helps maintain a well-documented and... |
| Public repositories | are accessible to everyone on the internet. |
| Private repositories | are only accessible to you, people you explicitly share access with, and, for organization repositories, certain organization members. |
| Write | access within the repository you want to add a file. |
| Note | Instead of merging, you can create a new branch and check it out by simply using git in a terminal the command would be: `git checkout -b newBranchName` |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. |

**Key Points:**
- Version Control: GitHub uses Git, a distributed version control system, to track changes in source code during software development. This allows multiple contributors to work on the same project...
- Repositories: Projects on GitHub are organized into repositories, which can contain code, images, text, or any other resource related to the project. Repositories can be public (visible to anyone) or...
- Collaboration: GitHub facilitates collaboration through features such as pull requests, issues, and discussions. Developers can propose changes to a project through pull requests, and collaborators...
- Community and Social Coding: GitHub fosters a strong community around open source development. Developers can discover projects, contribute to others' work, and build a portfolio of their own...
- Wikis and Documentation: Repositories can include wikis and documentation to provide information about the project, its structure, and ways to contribute. This helps maintain a well-documented and...
- Public repositories are accessible to everyone on the internet.
- Private repositories are only accessible to you, people you explicitly share access with, and, for organization repositories, certain organization members.
- Untracked: An initial state of a file when it isn't yet part of the Git repository. Git is unaware of its existence.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Managing Permissions

**TL;DR:** Close your eyes again and return to the bustling and modern (yet still surprisingly well-structured and accessible) mega city of GitHub. In this place, collaboration is the key, code flows like traffic, and permissions act as the city's governing laws. In this city, like in each of its real-life counterparts, understanding the laws is vital for mak...

**Topics covered:**
- 1. Permissions on a Repository Level
- 2. Permissions on a Team Level
- 3. Permissions on an Organization Level
- 4. Permissions on an Enterprise Level
- Repository Security and Management
- 1. Creating Protection Rules
- 2. Adding CODEOWNERS Files
- 3. Using Traffic Insights
- Exercise: Permissions in GitHub

**Key Terms:**

| Term | Definition |
|------|-----------|
| Read | Recommended for non-code contributors who want to view or discuss your project. This level is good for anyone that needs to view the content within the repository but doesn't need... |
| Triage | Recommended for contributors who need to proactively manage issues and pull requests without write access. This level could be good for some project managers who manage tracking... |
| Write | Recommended for contributors who actively push to your project. Write is the standard permission for most developers. |
| Maintain | Recommended for project managers who need to manage the repository without access to sensitive or destructive actions. |
| Admin | Recommended for people who need full access to the project, including sensitive and destructive actions like managing security or deleting a repository. These people are... |
| Settings | tab, open the dropdown menu and then select **Settings**. |

**Key Points:**
- Read - Recommended for non-code contributors who want to view or discuss your project. This level is good for anyone that needs to view the content within the repository but doesn't need to actually...
- Triage - Recommended for contributors who need to proactively manage issues and pull requests without write access. This level could be good for some project managers who manage tracking issues but...
- Write - Recommended for contributors who actively push to your project. Write is the standard permission for most developers.
- Maintain - Recommended for project managers who need to manage the repository without access to sensitive or destructive actions.
- Admin - Recommended for people who need full access to the project, including sensitive and destructive actions like managing security or deleting a repository. These people are repository owners and...
- Change the team's name, description, and visibility
- Request that the team change parent and child teams
- Edit and delete team discussions

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 2

### Github Copilot For Business

**TL;DR:** In the bustling city of software development, GitHub Copilot stands as a visionary assisting architect, reshaping how businesses construct their digital landscapes. This AI-driven coding companion understands the city's unique architecture, providing architects with tailor-made blueprints for efficient code structures.

**Topics covered:**
- LLM and GitHub Copilot
- What are LLMs?
- Fine-tuning LLMs
- LoRA Fine-tuning
- Improving Operations with GitHub Copilot for Business
- GitHub Copilot for Business vs. GitHub Copilot for Individuals
- GitHub for Business Use Cases
- Improving Business with GitHub Copilot
- Setting Up GitHub Copilot for Business
- Enabling User Access for Organizations

**Key Terms:**

| Term | Definition |
|------|-----------|
| A more powerful AI model | New modeling algorithms improve the quality of code suggestions. |
| AI-based security vulnerability filtering | GitHub Copilot for Business automatically blocks common insecure code suggestions by targeting issues such as hard-coded credentials, SQL injections, and path injections. |
| VPN proxy support | GitHub Copilot works with VPNs including self-signed certificates, allowing developers to use it in any working environment. |
| Simple sign-up | Any company can quickly purchase Copilot for Business licenses online and easily assign seats, even if they don't use the GitHub platform for their source code. |
| Developers code faster | In a survey conducted by Microsoft, almost 90% of developers said they completed tasks faster with GitHub Copilot. |
| Developers stay in the flow longer | 73% of developers that were surveyed said GitHub Copilot helps them stay in the flow longer and more easily, and 87% said it helped them preserve mental energy when working... |
| Enhanced Productivity | GitHub Copilot streamlines the coding process by providing AI-generated code suggestions. This can significantly reduce the time developers spend on routine and repetitive tasks,... |
| Code planning and automation | section of the sidebar, select **Copilot**, then select **Access**. |
| Allow for all members | under **User permissions**. |
| Confirm seat assignment | dialog, confirm that you want to enable GitHub Copilot for all current and future users in your organization, then select **Confirm**. |

**Key Points:**
- Instead of changing everything, LoRA adds smaller trainable parts to each layer of the pretrained model.
- The original model remains the same, which saves time and resources.
- It beats other adaptation methods like adapters and prefix-tuning.
- It's like getting great results with fewer moving parts.
- A more powerful AI model: New modeling algorithms improve the quality of code suggestions.
- AI-based security vulnerability filtering: GitHub Copilot for Business automatically blocks common insecure code suggestions by targeting issues such as hard-coded credentials, SQL injections, and...
- VPN proxy support: GitHub Copilot works with VPNs including self-signed certificates, allowing developers to use it in any working environment.
- Simple sign-up: Any company can quickly purchase Copilot for Business licenses online and easily assign seats, even if they don't use the GitHub platform for their source code.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Introduction To Github Copilot

**TL;DR:** <edukamu-video content="/videos/devai-4-unit2-video.yaml"/>
<br>

**Topics covered:**
- Getting Started with GitHub Copilot
- Why Use GitHub Copilot?
- Coming Soon: GitHub Copilot X
- 1. Simple Code Creation with GitHub Copilot Chat
- 2. Copilot for Pull Requests
- 3. Copilot for Documentation
- 4. Copilot for CLI
- GitHub Copilot for Business
- Practice: Setting Up GitHub Copilot
- 1. Signing Up

**Key Terms:**

| Term | Definition |
|------|-----------|
| A more powerful AI model | New modeling algorithms improve the quality of code suggestions. |
| AI-based security vulnerability filtering | GitHub Copilot automatically blocks common insecure code suggestions by targeting issues such as hardcoded credentials, SQL injections, and path injections. |
| VPN proxy support | GitHub Copilot works with VPNs, including with self-signed certificates, so developers can use it in any working environment. |
| Simple sign-up | Any company can quickly purchase Copilot for Business licenses online, and easily assign seats even if they don’t use the GitHub platform for their source code. |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |
| Extension: GitHub Copilot | tab in Visual Studio Code, select **Install**.<br> |
| Preferences | and select **Settings**. |
| Help > Toggle Developer Tools | within Visual Studio Code. |
| Shift+Command+P | * For Windows or Linux, use **Ctrl+Shift+P** |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |

**Key Points:**
- 46% of new code is now written by AI
- 55% faster overall developer productivity
- 74% of developers feel more focused on satisfying work
- A more powerful AI model: New modeling algorithms improve the quality of code suggestions.
- AI-based security vulnerability filtering: GitHub Copilot automatically blocks common insecure code suggestions by targeting issues such as hardcoded credentials, SQL injections, and path injections.
- VPN proxy support: GitHub Copilot works with VPNs, including with self-signed certificates, so developers can use it in any working environment.
- Simple sign-up: Any company can quickly purchase Copilot for Business licenses online, and easily assign seats even if they don’t use the GitHub platform for their source code.
- To disable suggestions from GitHub Copilot globally, select Disable Globally.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Prompt Engineering

**TL;DR:** Generative AI services aimed at general public is oftentimes used by writing detailed instructions often referred to as prompts. Prompts are like commands that make the service do what you need it to: think of them as instructions you'd give to an assistant.

**Topics covered:**
- Introduction to Prompt Engineering
- Principles of Prompt Engineering
- Best Practices of Prompt Engineering
- 1. Clarity
- 2. Details and Context
- 3. Examples for Learning
- 4. Assert and Iterate
- Prompts and Learning
- 1. Zero-shot Learning
- 2. One-shot Learning

**Key Terms:**

| Term | Definition |
|------|-----------|
| 4 S's | below. These core rules are the basis for creating effective prompts. |
| Single | Always focus your prompt on a single, well-defined task or question. This clarity is crucial for eliciting accurate and useful responses from Copilot. |
| Specific | Ensure that your instructions are explicit and detailed. Specificity leads to more applicable and precise code suggestions. |
| Short | While being specific, keep prompts concise and to the point. This balance ensures clarity without overloading Copilot or complicating the interaction. |
| Surround | Utilize descriptive filenames and keep related files open. This provides Copilot with rich context, leading to more tailored code suggestions. |
| Note | Copilot also uses parallel open tabs in your code editor to get more context on the requirements of your code. |
| Personal data | Copilot actively filters out any personal data, such as names, addresses, or identification numbers, to protect user privacy and data security. |
| Hate speech and inappropriate content | Copilot employs algorithms to detect and prevent the generation of hate speech, offensive language, or inappropriate content that could be harmful or offensive. |
| Extract intent | Copilot proceeds to extract your intent from the natural language comment. It identifies keywords, phrases, and context cues within the prompt. |
| Intent mapping | Copilot maps the extracted intent to specific coding actions or functionalities, considering both the prompt's content and the contextual information. This step translates the... |

**Key Points:**
- Single: Always focus your prompt on a single, well-defined task or question. This clarity is crucial for eliciting accurate and useful responses from Copilot.
- Specific: Ensure that your instructions are explicit and detailed. Specificity leads to more applicable and precise code suggestions.
- Short: While being specific, keep prompts concise and to the point. This balance ensures clarity without overloading Copilot or complicating the interaction.
- Surround: Utilize descriptive filenames and keep related files open. This provides Copilot with rich context, leading to more tailored code suggestions.
- Code before and after the cursor position, which helps it understand the immediate context of the prompt.
- Filename and type of the file being edited, allowing it to tailor code suggestions to the specific file type.
- Information about adjacent open tabs, ensuring that the generated code aligns with other code segments in the same project.
- Personal data: Copilot actively filters out any personal data, such as names, addresses, or identification numbers, to protect user privacy and data security.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Unit 3

### Automating Workflows With Github Actions

**TL;DR:** Imagine getting so skilled at writing code that some tasks start to feel boring and repetitive. According to your current position and skill level, this might seem like a distant dream, but it could also be your future reality. Either way, GitHub Actions is there to take care of those dull tasks!

**Topics covered:**
- Automating Development Tasks
- Workflow Automation
- Getting Started with GitHub Actions
- Using Open-source GitHub Actions
- Basic Components of GitHub Actions
- Workflows
- Jobs
- Steps
- Actions
- Example: Git Checkout Action

**Key Terms:**

| Term | Definition |
|------|-----------|
| Communication | Consider all of the ways that GitHub makes it easy for a team of developers to communicate about the software development project: code reviews in pull requests, GitHub issues,... |
| Automation | GitHub Actions lets your team automate workflows at every step in the software-development process, from integration to delivery to deployment. It even lets you automate adding... |
| Actions | tab that provides a quick and easy way to get started with setting up your first script. If you see a workflow that you think might be a great starting point, just select the... |
| JavaScript actions | don't include the environment in the code. You'll have to specify the environment to execute these actions. You can run these actions in a VM in the cloud or on-premises.... |
| Composite actions | allow you to combine multiple workflow steps within one action. For example, you can use this feature to bundle together multiple run commands into an action, and then have a... |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |
| Who is this for | Developers, DevOps engineers, students, managers, teams, GitHub users. |
| What you'll learn | How to create workflow files, trigger workflows, and find workflow logs. |
| What you'll build | An Actions workflow that will check emoji shortcode references in Markdown files. |
| Prerequisites | In this exercise you will work with issues and pull requests, as well as edit files. |

**Key Points:**
- Communication: Consider all of the ways that GitHub makes it easy for a team of developers to communicate about the software development project: code reviews in pull requests, GitHub issues, project...
- Automation: GitHub Actions lets your team automate workflows at every step in the software-development process, from integration to delivery to deployment. It even lets you automate adding labels to...
- Ensure the code passes all unit tests
- Perform code quality and compliance checks to make sure the source code meets the organization's standards
- Check the code and its dependencies for known security issues
- Build the code integrating new source from (potentially) multiple contributors
- Ensure the software passes integration tests
- Deliver the new binaries to the appropriate filesystem location

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Github Copilot And Javascript

**TL;DR:** <edukamu-video content="/videos/devai-4-unit3-video.yaml"/>
<br>

**Topics covered:**
- Introduction to JavaScript
- JavaScript
- Example: JavaScript in Use
- Shopping Cart Interaction:
- Real-Time Price Calculation:
- User Feedback on Form Submission:
- Practice: Setting up GitHub Copilot for JavaScript
- Setting Up an Environment
- JavaScript Portfolio
- Getting the Most out of GitHub Copilot with JavaScript

**Key Terms:**

| Term | Definition |
|------|-----------|
| Example | Adding a live search feature to a website, where the search results update dynamically as you type. This enhances user experience by providing instant feedback. |
| Example | Creating a server that handles real-time notifications in a chat application. This ensures messages are delivered instantly to users. |
| Example | Building a responsive and interactive form on a social media site, allowing users to post comments, like posts, and see updates without refreshing the page. |
| JavaScript Use Case | When a user adds an item to their cart, JavaScript can dynamically update the cart icon, showing the current number of items. It can also enable a smooth dropdown or slide-in... |
| JavaScript Use Case | As users select different quantities or variations of products, JavaScript can instantly calculate and display the updated total price. This ensures customers have a clear... |
| JavaScript Use Case | When a user completes an order form, JavaScript can provide immediate feedback, such as a confirmation message or highlighting any missing information. This real-time response... |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |
| Note | Educators, Students and select open-source maintainers can sign up for Copilot for free. More information is available in [Microsoft... |
| Important | All GitHub accounts can use Codespaces for up to 60 hours free each month with two core instances. For more information, see GitHub Codespaces monthly included storage and core... |
| Note | GitHub Copilot uses open files in your text editor as additional context. This is helpful because it provides useful information in addition to the prompt or code you may be... |

**Key Points:**
- JavaScript Use Case: When a user adds an item to their cart, JavaScript can dynamically update the cart icon, showing the current number of items. It can also enable a smooth dropdown or slide-in...
- JavaScript Use Case: As users select different quantities or variations of products, JavaScript can instantly calculate and display the updated total price. This ensures customers have a clear...
- JavaScript Use Case: When a user completes an order form, JavaScript can provide immediate feedback, such as a confirmation message or highlighting any missing information. This real-time response...
- Configure a GitHub repository in Codespaces and install GitHub Copilot extension.
- Use crafted prompts to generate suggestions from GitHub Copilot.
- Apply GitHub Copilot to improve your projects in JavaScript.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Github Copilot And Python

**TL;DR:** Python is a programming language known for its simplicity and versatility: its elegant syntax makes it a favorite for beginners and seasoned developers alike. More specifically, Python excels in web development, data analysis, machine learning, and automation.

**Topics covered:**
- Introduction to Python
- Python
- Example: Python in Use
- 1. File Organization Script:
- 2. Data Analysis for Business Insights:
- 3. Automated Email Responses:
- Practice: Setting up GitHub Copilot for JavaScript
- Setting Up an Environment
- Python Web API
- Testing the API

**Key Terms:**

| Term | Definition |
|------|-----------|
| Example | Developing a program that predicts if a given email is spam or not, helping filter unwanted emails from your inbox. |
| Example | Building a personal blog where you can easily create, edit, and organize your posts without needing extensive coding knowledge. |
| Example | Writing a script that renames and organizes your photo collection based on the date they were taken, saving you manual effort. |
| Example | Creating a simple program to analyze data from a school science experiment, like tracking the growth of plants under different conditions. |
| Python Use Case | You have a folder with hundreds of files from different projects. With Python, you can write a script that organizes these files into separate folders based on project names or... |
| Python Use Case | Your company collects data on customer interactions. Python can be used to analyze this data, providing insights into customer behavior, preferences, and trends. This information... |
| Python Use Case | If you receive a large volume of similar emails that require standard responses, Python scripts can be used to automate email replies. For instance, acknowledging receipt of... |
| Important | The following setup process is quite similar to what we already did with JavaScript, but make sure to complete it. In order to use GitHub Copilot with Python, we'll need to... |
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... |
| Note | Educators, Students and select open-source maintainers can sign up for Copilot for free. More information is available in [Microsoft... |

**Key Points:**
- Python Use Case: You have a folder with hundreds of files from different projects. With Python, you can write a script that organizes these files into separate folders based on project names or file...
- Python Use Case: Your company collects data on customer interactions. Python can be used to analyze this data, providing insights into customer behavior, preferences, and trends. This information can...
- Python Use Case: If you receive a large volume of similar emails that require standard responses, Python scripts can be used to automate email replies. For instance, acknowledging receipt of...
- Configure a GitHub repository in Codespaces and install GitHub Copilot extension.
- Use crafted prompts to generate suggestions from GitHub Copilot.
- Apply GitHub Copilot to improve your projects in Python.

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

### Summary

**TL;DR:** Congratulations on reaching the summary of the Accelerating Development Workflow course! As stated at the beginning, you must complete every assignment in order to pass this course. Therefore please go to Course progress page by pressing the button below (*or the progress icon in the top right corner*), and check that you have indeed completed all ...

**Topics covered:**
- Empowering Microsoft Azure with GitHub
- 1. Unified Version Control
- 2. Orchestrating AI Pipelines
- 3. GitHub Actions for AI Workflows
- 4. Collaborative AI Model Development
- 5. Seamless Azure Resource Management
- 6. Azure Boards and GitHub Issues Integration
- Unit 1: Getting Started with GitHub
- Unit 2: Increasing Productivity with GitHub Copilot
- Unit 3: GitHub Copilot and Programming

**Key Points:**
- How would you describe GitHub in a few sentences?
- How does GitHub boost collaboration?
- What tools are available for improving project security on GitHub?
- What are the main capabilities of GitHub Copilot?
- What are prompts? Also, can you explain the main principles of prompt engineering?
- How can GitHub Copilot help businesses operate more effectively?
- In what ways can GitHub Copilot improve written code?
- How does GitHub Copilot help developers when writing code?

<details><summary>📝 My Notes</summary>

_Write your own observations, questions, or mnemonics here._

</details>

---

## Quick-Reference Glossary

| Term | Definition | Section |
|------|-----------|---------|
| Reminder | The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or... | Collaboration In Github |
| Who is this for | New developers, new GitHub users, and students. | Collaboration In Github |
| What you'll learn | We'll introduce repositories, branches, commits, and pull requests. | Collaboration In Github |
| What you'll build | We'll make a short Markdown file you can use as your [profile... | Collaboration In Github |
| Prerequisites | None. This practice exercise is a great introduction for your first day on GitHub. | Collaboration In Github |
| How long | It will take around an hour to complete this exercise. | Collaboration In Github |
| Create repository | button at the bottom of the form. | Collaboration In Github |
| Version Control | GitHub uses Git, a distributed version control system, to track changes in source code during software development. This allows multiple contributors to work on the same project... | Introduction To Github |
| Repositories | Projects on GitHub are organized into repositories, which can contain code, images, text, or any other resource related to the project. Repositories can be public (visible to... | Introduction To Github |
| Collaboration | GitHub facilitates collaboration through features such as pull requests, issues, and discussions. Developers can propose changes to a project through pull requests, and... | Introduction To Github |
| Community and Social Coding | GitHub fosters a strong community around open source development. Developers can discover projects, contribute to others' work, and build a portfolio of their own contributions. | Introduction To Github |
| Wikis and Documentation | Repositories can include wikis and documentation to provide information about the project, its structure, and ways to contribute. This helps maintain a well-documented and... | Introduction To Github |
| Public repositories | are accessible to everyone on the internet. | Introduction To Github |
| Private repositories | are only accessible to you, people you explicitly share access with, and, for organization repositories, certain organization members. | Introduction To Github |
| Write | access within the repository you want to add a file. | Introduction To Github |
| Note | Instead of merging, you can create a new branch and check it out by simply using git in a terminal the command would be: `git checkout -b newBranchName` | Introduction To Github |
| review your answers | and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you. | Introduction To Github |
| Read | Recommended for non-code contributors who want to view or discuss your project. This level is good for anyone that needs to view the content within the repository but doesn't need... | Managing Permissions |
| Triage | Recommended for contributors who need to proactively manage issues and pull requests without write access. This level could be good for some project managers who manage tracking... | Managing Permissions |
| Maintain | Recommended for project managers who need to manage the repository without access to sensitive or destructive actions. | Managing Permissions |
| Admin | Recommended for people who need full access to the project, including sensitive and destructive actions like managing security or deleting a repository. These people are... | Managing Permissions |
| Settings | tab, open the dropdown menu and then select **Settings**. | Managing Permissions |
| A more powerful AI model | New modeling algorithms improve the quality of code suggestions. | Github Copilot For Business |
| AI-based security vulnerability filtering | GitHub Copilot for Business automatically blocks common insecure code suggestions by targeting issues such as hard-coded credentials, SQL injections, and path injections. | Github Copilot For Business |
| VPN proxy support | GitHub Copilot works with VPNs including self-signed certificates, allowing developers to use it in any working environment. | Github Copilot For Business |
| Simple sign-up | Any company can quickly purchase Copilot for Business licenses online and easily assign seats, even if they don't use the GitHub platform for their source code. | Github Copilot For Business |
| Developers code faster | In a survey conducted by Microsoft, almost 90% of developers said they completed tasks faster with GitHub Copilot. | Github Copilot For Business |
| Developers stay in the flow longer | 73% of developers that were surveyed said GitHub Copilot helps them stay in the flow longer and more easily, and 87% said it helped them preserve mental energy when working... | Github Copilot For Business |
| Enhanced Productivity | GitHub Copilot streamlines the coding process by providing AI-generated code suggestions. This can significantly reduce the time developers spend on routine and repetitive tasks,... | Github Copilot For Business |
| Code planning and automation | section of the sidebar, select **Copilot**, then select **Access**. | Github Copilot For Business |
| Allow for all members | under **User permissions**. | Github Copilot For Business |
| Confirm seat assignment | dialog, confirm that you want to enable GitHub Copilot for all current and future users in your organization, then select **Confirm**. | Github Copilot For Business |
| Extension: GitHub Copilot | tab in Visual Studio Code, select **Install**.<br> | Introduction To Github Copilot |
| Preferences | and select **Settings**. | Introduction To Github Copilot |
| Help > Toggle Developer Tools | within Visual Studio Code. | Introduction To Github Copilot |
| Shift+Command+P | * For Windows or Linux, use **Ctrl+Shift+P** | Introduction To Github Copilot |
| 4 S's | below. These core rules are the basis for creating effective prompts. | Prompt Engineering |
| Single | Always focus your prompt on a single, well-defined task or question. This clarity is crucial for eliciting accurate and useful responses from Copilot. | Prompt Engineering |
| Specific | Ensure that your instructions are explicit and detailed. Specificity leads to more applicable and precise code suggestions. | Prompt Engineering |
| Short | While being specific, keep prompts concise and to the point. This balance ensures clarity without overloading Copilot or complicating the interaction. | Prompt Engineering |
| Surround | Utilize descriptive filenames and keep related files open. This provides Copilot with rich context, leading to more tailored code suggestions. | Prompt Engineering |
| Personal data | Copilot actively filters out any personal data, such as names, addresses, or identification numbers, to protect user privacy and data security. | Prompt Engineering |
| Hate speech and inappropriate content | Copilot employs algorithms to detect and prevent the generation of hate speech, offensive language, or inappropriate content that could be harmful or offensive. | Prompt Engineering |
| Extract intent | Copilot proceeds to extract your intent from the natural language comment. It identifies keywords, phrases, and context cues within the prompt. | Prompt Engineering |
| Intent mapping | Copilot maps the extracted intent to specific coding actions or functionalities, considering both the prompt's content and the contextual information. This step translates the... | Prompt Engineering |
| Communication | Consider all of the ways that GitHub makes it easy for a team of developers to communicate about the software development project: code reviews in pull requests, GitHub issues,... | Automating Workflows With Github Actions |
| Automation | GitHub Actions lets your team automate workflows at every step in the software-development process, from integration to delivery to deployment. It even lets you automate adding... | Automating Workflows With Github Actions |
| Actions | tab that provides a quick and easy way to get started with setting up your first script. If you see a workflow that you think might be a great starting point, just select the... | Automating Workflows With Github Actions |
| JavaScript actions | don't include the environment in the code. You'll have to specify the environment to execute these actions. You can run these actions in a VM in the cloud or on-premises.... | Automating Workflows With Github Actions |
| Composite actions | allow you to combine multiple workflow steps within one action. For example, you can use this feature to bundle together multiple run commands into an action, and then have a... | Automating Workflows With Github Actions |
| Example | Adding a live search feature to a website, where the search results update dynamically as you type. This enhances user experience by providing instant feedback. | Github Copilot And Javascript |
| JavaScript Use Case | When a user adds an item to their cart, JavaScript can dynamically update the cart icon, showing the current number of items. It can also enable a smooth dropdown or slide-in... | Github Copilot And Javascript |
| Important | All GitHub accounts can use Codespaces for up to 60 hours free each month with two core instances. For more information, see GitHub Codespaces monthly included storage and core... | Github Copilot And Javascript |
| Python Use Case | You have a folder with hundreds of files from different projects. With Python, you can write a script that organizes these files into separate folders based on project names or... | Github Copilot And Python |

---

*Auto-generated by `generate_diary.py` — re-run to refresh after re-scraping.*
