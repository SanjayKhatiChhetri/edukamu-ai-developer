## Automating Workflows with GitHub Actions

Imagine getting so skilled at writing code that some tasks start to feel boring and repetitive. According to your current position and skill level, this might seem like a distant dream, but it could also be your future reality. Either way, GitHub Actions is there to take care of those dull tasks!

GitHub Actions is a powerful automation service that allows you to define workflows to build, test, and deploy your code directly from your GitHub repository. It's designed to streamline your software development process by automating repetitive tasks, reducing manual intervention, and ensuring consistent workflows.

On this page, we'll explore the main capabilities and opportunities offered by GitHub actions. While we won't dig deep into the details, we'll learn how GitHub Actions can significantly empower all Azure developers regardless their current skill level.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Automating Development Tasks
</edukamu-collapse-hidden-title>

GitHub Actions optimize code-delivery time, from idea to deployment, on a community-powered platform.

Suppose you manage a team that's developing a web site that will improve your customers' experience when they contact product support. This project is important to upper management. They want a high-quality site, and they want to publish it soon. You need to make sure your team is producing code that tests, builds, and deploys quickly once a feature is implemented. On top of that, your IT department wants to automate creating and tearing down the project's infrastructure. You decide to use continuous integration (CI) and continuous delivery (CD) to automate all the build, test, and deployment tasks. You're also going to adopt infrastructure as code (IaC) to automate the IT tasks.

There are several tools available to help you achieve these goals. However, because you're already using GitHub for your code repository, you decide to investigate GitHub Actions to see if it provides the automation you need.

On this page, we'll get acquainted with GitHub Actions and workflows. More specifically, we'll learn what GitHub Actions are, the types of actions, and where to find them. We'll also explore how to identify the required components within a GitHub Actions workflow file and look at how we all can plan the automation processes in advance.

GitHub is designed to help teams of developers and DevOps engineers build and deploy applications quickly. There are many features in GitHub that enable this, but they generally fall into one of two categories:
* **Communication**: Consider all of the ways that GitHub makes it easy for a team of developers to communicate about the software development project: code reviews in pull requests, GitHub issues, project boards, wikis, notifications, and so on.
* **Automation**: GitHub Actions lets your team automate workflows at every step in the software-development process, from integration to delivery to deployment. It even lets you automate adding labels to pull requests and checking for stale issues and pull requests.

When combined, these features have allowed thousands of development teams to effectively decrease the amount of time it takes from their initial idea to deployment.


### Workflow Automation

Consider all of the tasks that must happen *after* the code is written, but before you can reliably use the code for its intended purpose. Depending on your organization's goals, you'll likely need to perform one or more of the following tasks:
* Ensure the code passes all unit tests
* Perform code quality and compliance checks to make sure the source code meets the organization's standards
* Check the code and its dependencies for known security issues
* Build the code integrating new source from (potentially) multiple contributors
* Ensure the software passes integration tests
* Version the new build
* Deliver the new binaries to the appropriate filesystem location
* Deploy the new binaries to one or more servers
* If any of these tasks don't pass, report the issue to the proper individual or team for resolution

The challenge is to do these tasks reliably, consistently, and in a sustainable manner. This is an ideal job for workflow automation. If you're already relying on GitHub, you'll likely want to set up your workflow automation using GitHub Actions.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Getting Started with GitHub Actions
</edukamu-collapse-hidden-title>

*GitHub Actions* are packaged scripts to automate tasks in a software-development workflow in GitHub. You can configure GitHub Actions to trigger complex workflows that meet your organization's needs; each time developers check new source code into a specific branch, at timed intervals, or manually. The result is a reliable and sustainable automated workflow, which leads to a significant decrease in development time.

GitHub Actions are scripts that adhere to a yml data format. Each repository has an **Actions** tab that provides a quick and easy way to get started with setting up your first script. If you see a workflow that you think might be a great starting point, just select the **Configure** button to add the script and begin editing the source yml.

<edukamu-image url="/graphics/module3/github-actions-automate-development-tasks-01.png" alt="Screenshot of the Actions tab in GitHub Actions displaying a simple workflow and a button to set up this workflow."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

However, beyond those GitHub Actions featured on the Actions tab, you can:
* Search for GitHub Actions in the GitHub Marketplace. The GitHub Marketplace allows you to discover and purchase tools that extend your workflow.
* Search for open-source projects. For example, the GitHub Actions organization features many popular open-source repos containing GitHub Actions you can use.
* Write your own GitHub Actions from scratch. Furthermore, if you want, you could make them open source, or even publish them to the GitHub Marketplace.


### Using Open-source GitHub Actions

Many GitHub Actions are open source and available for anyone who wants to use them. However, just like with any open-source software, you need to carefully check them before using them in your project. Similar to recommended community standards with open-source software—such as including a README, code of conduct, contributing file, and issue templates, just to name a few—you can follow these recommendations when using GitHub Actions:
* Review the action's `action.yml` file for inputs, outputs, and to make sure the code does what it says it does.
* Check if the action is in the GitHub Marketplace. This is a good check, even if an action does not have to be on the GitHub Marketplace to be valid.
* Check if the action is verified in the GitHub Marketplace. This means that GitHub has approved the use of this action. However, you should still review it before using it.
* Include the version of the action you're using by specifying a Git ref, SHA, or tag.

</edukamu-collapse>
<br>


GitHub Actions are very handy when you and your development team need to find ways to save time. While they can’t take care of the whole development process, they can significantly reduce the time spent on repetitive, fairly simple tasks.

There are three types of GitHub actions: container actions, JavaScript actions, and composite actions.

With **container actions**, the environment is part of the action's code. These actions can only be run in a Linux environment that GitHub hosts. Container actions support many different languages.

**JavaScript actions** don't include the environment in the code. You'll have to specify the environment to execute these actions. You can run these actions in a VM in the cloud or on-premises. JavaScript actions support Linux, macOS, and Windows environments.

**Composite actions** allow you to combine multiple workflow steps within one action. For example, you can use this feature to bundle together multiple run commands into an action, and then have a workflow that executes the bundled commands as a single step using that action.

There are many ways to implement GitHub Actions to your projects. Next, we’ll review the components of GitHub Actions to deepen our understanding.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Basic Components of GitHub Actions
</edukamu-collapse-hidden-title>

There are several components that work together to run tasks or jobs within a GitHub Actions workflow. In short, an event triggers the *workflow*, which contains a *job*. This job then uses *steps* to dictate which *actions* will run within the workflow. To better see how these components work together, let's take a quick look at each one.

<edukamu-image url="/graphics/module3/github-actions-workflow-components.png" alt="Screenshot of a GitHub Actions workflow file showing the job, step, and action components." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>


### Workflows

A workflow is an automated process that you add to your repository. A workflow needs to have at least one job, and different events can trigger it. You can use it to build, test, package, release, or deploy your repository's project on GitHub.

### Jobs

The job is the first major component within the workflow. A job is a section of the workflow that will be associated with a runner. A runner can be GitHub-hosted or self-hosted, and the job can run on a machine or in a container. You'll specify the runner with the `runs-on:` attribute. Here, you're telling the workflow to run this job on `ubuntu-latest`. We'll talk more about runners in the next unit.

### Steps

A step is an individual task that can run commands in a job. In our preceding example, the step uses the action `actions/checkout@v2` to check out the repository. What's interesting is the `uses: ./action-a` value. This is the path to the container action that you'll build in an `action.yml` file.

### Actions

The actions inside your workflow are the standalone commands that are executed. These standalone commands can reference GitHub actions such as using your own custom actions, or community actions like the one we use in the preceding example, `actions/checkout@v2`. You can also run commands such as `run: npm install -g bats` to execute a command on the runner.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Example: Git Checkout Action
</edukamu-collapse-hidden-title>

Here's an example of an action that performs a git checkout of a repository. This action, `actions/checkout@v1`, is part of a step in a workflow.

Here's how the GitHub action looks like:

```
steps:
  - uses: actions/checkout@v1
  - name: npm install and build webpack
    run: |
      npm install
      npm run build
```

Then, suppose you want to use a container action to run containerized code. Your action might look like this:

```
name: "Hello Actions"
description: "Greet someone"
author: "octocat@github.com"

inputs:
    MY_NAME:
      description: "Who to greet"
      required: true
      default: "World"

runs:
    uses: "docker"
    image: "Dockerfile"

branding:
    icon: "mic"
    color: "purple"

```

Notice the `inputs` section. Here, you're getting the value of a variable called `MY_NAME`. This variable will be set in the workflow that runs this action.

In the `runs` section, notice you specify *docker* in the `uses` attribute. When you do this, you'll need to provide the path to the Docker image file. Here, it's called *Dockerfile*. You don't need to worry about the technical specifications during this course.

The last section, *branding*, personalizes your action in the GitHub Marketplace if you decide to publish it there.


### Workflows

A *GitHub Actions workflow* is a process that you set up in your repository to automate software-development lifecycle tasks, including GitHub Actions. With a workflow, you can build, test, package, release, and deploy any project on GitHub.

To create a workflow, you add actions to a .yml file in the `.github/workflows` directory in your GitHub repository.

In the exercise coming up, your workflow file, *main.yml*, will look like this:

```
name: A workflow for my Hello World file
on: push
jobs:
  build:
    name: Hello world action
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v1
    - uses: ./action-a
      with:
        MY_NAME: "Mona"
```

Notice the `on:` attribute. This is a *trigger* to specify when this workflow will run. Here, it triggers a run when there's a push event to your repository. You can specify single events like `on: push`, an array of events like `on: [push, pull_request]`, or an event-configuration map that schedules a workflow or restricts the execution of a workflow to specific files, tags, or branch changes. The map might look something like this:

```
on:
  # Trigger the workflow on push or pull request,
  # but only for the main branch
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  # Also trigger on page_build, as well as release created events
  page_build:
  release:
    types: # This configuration does not affect the page_build event above
      - created
```

An event will trigger on all activity types for the event unless you specify the type or types. For a comprehensive list of events and their activity types, see: [Events that trigger workflows](https://docs.github.com/actions/using-workflows/events-that-trigger-workflows)(target="_blank") in the GitHub documentation.

A workflow must have at least one *job*. A job is a section of the workflow associated with a *runner*. A runner can be GitHub-hosted or self-hosted, and the job can run on a machine or in a container. You'll specify the runner with the `runs-on:` attrib  ute. Here, you're telling the workflow to run this job on `ubuntu-latest`.

Each job will have steps to complete. In our example, the step uses the action `actions/checkout@v1` to check out the repository. What's interesting is the `uses: ./action-a` value, which is the path to the container action that you build in an *action.yml* file. We looked at the contents of an *action.yml* file in the **What is GitHub Actions?** section.

The last part of this workflow file sets the `MY_NAME` variable value for this workflow. Recall the container action took an input called `MY_NAME`.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-green">
Do notice that the above example is a fairly simple one. GitHub Actions can be used for many different tasks, including some much more complicated than the one we just witnessed!

At this stage, it's good to remind you that the things we explore in this section might feel confusing if you're not familiar with programming or writing code. However, do your best to explore the examples in detail, as just reading the code snippets and trying to see the logic behind them will help you along the way!

Now, it's time to set up a GitHub Actions workflow on our own! In other words, it's time for another practice exercise. Shall we begin?
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Using GitHub Actions
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

In this practical exercise, you'll get to try setting up a GitHub Action and using it in a workflow. As this particular practice might be quite challenging, you have the option to try and complete it completely of just focus on the basic details. It's up to you!

Before beginning, we recommend that you review the contents of the first unit and especially using push and pull requests in repositories once more, since you'll need it during this exercise!

Feel free to click on the button below and jump right in. After the exercise, make sure to return here - don't get lost in the intriguing world of GitHub just yet!

Good luck!

<edukamu-button url="https://github.com/new?template_owner=skills&template_name=hello-github-actions&owner=%40me&name=skills-hello-github-actions&description=My+clone+repository&visibility=public">Begin Exercise</edukamu-button>
<br>    

### Instructions

* **Who is this for**: Developers, DevOps engineers, students, managers, teams, GitHub users.
* **What you'll learn**: How to create workflow files, trigger workflows, and find workflow logs.
* **What you'll build**: An Actions workflow that will check emoji shortcode references in Markdown files.
* **Prerequisites**: In this exercise you will work with issues and pull requests, as well as edit files.
* **How long**: This exercise can be finished in less than two hours.

In more detail, we will:
1. Create a workflow.
2. Add a job.
3. Add actions.
4. Merge your pull request.
5. See the action run.

### Additional Tips

1. Click on the **Begin Exercise** button below and open the link in a new tab.
2. In the new tab, most of the prompts will automatically fill in for you.
   * For owner, choose your personal account or an organization to host the repository.
   * We recommend creating a public repository, as private repositories will use Actions minutes.
   * Scroll down and click the **Create repository** button at the bottom of the form.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
After your new repository is created, wait about 20 seconds, then refresh the page. Follow the step-by-step instructions in the new repository's README.
</li>
</ol>
</edukamu-section>

</edukamu-collapse>
<br>


Can you see yourself automatizing repetitive tasks with actions like the ones described before? If you ever collaborate with other developers using GitHub, make sure to take advantage of the capabilities offered by GitHub Actions.

Guess what? It's time for the last exercise of this course! Take a while to recap the materials we've just covered before completing it. Enjoy, it's the last one!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Introduction to GitHub Actions
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module3/automating-workflows-text-poll.yaml" id="2m4a3adqdhh59zsp"/>
<br>
<edukamu-text-poll url="/exercises/module3/automating-workflows-text-poll-2.yaml" id="65kt40vcf0550k07"/>
<br>
<edukamu-text-poll url="/exercises/module3/automating-workflows-text-poll-3.yaml" id="peo1xmbu3tn9yc3m"/>
<br>
<edukamu-text-poll url="/exercises/module3/automating-workflows-text-poll-4.yaml" id="2gpymj3s5mynydb5"/>
<br>
<edukamu-text-poll url="/exercises/module3/automating-workflows-text-poll-5.yaml" id="5t73m43w7sul5r36"/>
<br>
<edukamu-text-poll url="/exercises/module3/automating-workflows-text-poll-6.yaml" id="y8l8a281irze856y"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/3/automating-workflows-with-github-actions?question=2m4a3adqdhh59zsp">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


You've now reached the end of this course! Well done!

All that's left is the summary, in which we'll look back at what we've learned.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
