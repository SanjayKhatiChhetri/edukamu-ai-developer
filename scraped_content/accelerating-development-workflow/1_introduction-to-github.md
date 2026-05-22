<edukamu-video content="/videos/devai-4-unit1-video.yaml"/>
<br>

## Introduction to GitHub

When was the last time you updated an application? Maybe you just installed the latest version of your favorite messaging app on your phone or the video-editing software you enjoy using on your computer. Either way, installing updates is simple for the end user, but dealing with all the code associated with keeping applications up do date can be a real hassle from the developer's perspective.

Luckily, services like GitHub are there to make project management, code sharing, and collaboration much more convenient.

In a way, GitHub is not just another piece of software. Instead, it's a multi-faceted approach to building and managing software with simple, yet versatile and secure tools that are available on the Internet with no additional downloads – all you need is a browser, and you're good to go!

On this course, we'll explore GitHub from a variety of perspectives, but it's always best to start from the beginning, isn't it? Once more, welcome to the exciting, orderly, and surprisingly manageable world of GitHub!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Getting to Know GitHub
</edukamu-collapse-hidden-title>

<edukamu-image url="/graphics/module1/github-enterprise-platform.png" alt="A conceptual image of the GitHub Platform with layers from top to bottom: AI, Collaboration, Productivity, Security, and Scale."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

GitHub is a web-based platform that serves as a repository hosting service. It is widely used for version control, collaborative software development, and project management. GitHub provides a platform for developers to work on projects together, whether they are open source or private repositories.

Here are key features and aspects of GitHub:
* **Version Control**: GitHub uses Git, a distributed version control system, to track changes in source code during software development. This allows multiple contributors to work on the same project simultaneously without conflicts.
* **Repositories**: Projects on GitHub are organized into repositories, which can contain code, images, text, or any other resource related to the project. Repositories can be public (visible to anyone) or private (accessible only to specified collaborators).
* **Collaboration**: GitHub facilitates collaboration through features such as pull requests, issues, and discussions. Developers can propose changes to a project through pull requests, and collaborators can review and discuss the proposed changes before merging them into the main codebase.
* **Community and Social Coding**: GitHub fosters a strong community around open source development. Developers can discover projects, contribute to others' work, and build a portfolio of their own contributions.
* **Wikis and Documentation**: Repositories can include wikis and documentation to provide information about the project, its structure, and ways to contribute. This helps maintain a well-documented and accessible codebase.

GitHub has become a central hub for software development, enabling teams and individuals to collaborate efficiently and contribute to a wide range of projects across different domains. On this course, we’ll cover all its main functions.

</edukamu-collapse>
<br>

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="arrow-logo">
### What is Version Control?
</edukamu-collapse-hidden-title>

Before the Internet, there were very few comprehensive tools to manage the end-to-end process that begins with writing code and concludes with deploying the application into production.

The early version control tools were limited to keeping backups of changed files and preventing unwanted parallel changes. By checking out a file, similar to borrowing a book from a library, a developer could lock a file for editing while other developers waited for the file to be committed or checked in again.

Even though the old tools made tracking changes and merging files possible, they did not focus on teamwork or collaboration. The tools also did not track requirements or issues, which had to be managed through other means available at the time, including project management and issue tracking systems, along with those infamous yellow sticky notes.

As the public internet grew and free open-source software gained ground, better solutions were needed. New tools and platforms like GitHub were developed to provide repositories for sharing source code online. Today, GitHub enables millions of developers worldwide to share their code, contribute to a wide range of projects, and work at their own pace in parallel without locking each other out.

</edukamu-collapse>
<br>


GitHub is also used by the world's leading AI developers who use it to keep track of code, updates, and versions, among other things. Everything in GitHub is stored in repositories that make collaborating a straightforward affair.

But what are repositories? That's a great question, let's find out!

Before we do, may we suggest you to create a GitHub account and sign in? That way, you can try out all the neat actions we cover on this course – and ensure that the new information really sticks.

You can create an account at the GitHub website.

<edukamu-button url="https://github.com/signup?user_email=&source=form-home-signup">GitHub: Sign up</edukamu-button>
<br>

Registering and exploring GitHub is entirely free of charge, although many paid features exist as well. An active email address is all you need, since GitHub requires no additional downloads and is available on computers, tablets, and smartphones.

After signing up, it's time to get down to business! In the following sections, we’ll explore GitHub’s basic functions and capabilities, starting with repositories, branches, and commits.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Understanding and Using Repositories
</edukamu-collapse-hidden-title>

A repository contains all your project's files and each file's revision history. It is one of the essential parts that helps you collaborate with people. You can use repositories to manage your work, track changes, store revision history and work with others. Before we dive too deep, let’s first start with how to create a repository.

### Setting Up a Repository

1. In the upper-right corner of any page, use the drop-down menu, and select New repository.

<edukamu-image url="/graphics/module1/2-new-repo-option.png" alt="A screenshot of the drop-down menu of the plus sign in the top right corner of GitHub.com, with the first option being New repository." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Use the Owner dropdown menu to select the account you want to own the repository.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/2-selecting-repo-owner.png" alt="A screenshot of the drop-down menu of who should be the owner of the new repository." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Type a name for your repository, and an optional description.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/2-repo-name-text-box.png" alt="An image of the text box of the repository name highlighted." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Choose a repository visibility.
</li>
</ol>
</edukamu-section>
* **Public repositories** are accessible to everyone on the internet.
* **Private repositories** are only accessible to you, people you explicitly share access with, and, for organization repositories, certain organization members.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click Create repository and congratulations! You just created a repository!
</li>
</ol>
</edukamu-section>

Next up, let’s review how to add files to your repository.


### Adding Files

Files in GitHub can do a handful of things, but the main purpose of files is to store data and information about your project.

Let’s review how to add a file to your repository.

But before we begin, it is worth knowing in order to add a file to a repository you must first have minimum **Write** access within the repository you want to add a file.
1. On GitHub.com, navigate to the main page of the repository.
2. In your repository, browse to the folder where you want to create a file.
3. Above the list of files, select the Add file ᐁ dropdown menu, then click ᐩ Create new file. Alternatively, you can click ᐩ in the file tree view on the left.

<edukamu-image url="/graphics/module1/add-file-options.png" alt="A screenshot of the two options of adding a file to your new repository highlighted in red. One option is the plus sign in the left hand navigation bar, the second option is the add file button towards the right of the screen." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the file name field, type the name and extension for the file. To create subdirectories, type the / directory separator.
</li>
</ol>
</edukamu-section>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 5;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the file contents text box, type content for the file.
</li>
</ol>
</edukamu-section>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 6;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
To review the new content, above the file contents, click Preview.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/2-preview-option-in-a-file.png" alt="Screenshot showing a yml file with the preview button highlighted in the top left." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 7;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click Commit changes.
</li>
</ol>
</edukamu-section>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 8;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
In the "Commit message" field, type a short, meaningful commit message that describes the change you made to the file. You can attribute the commit to more than one author in the commit message.
</li>
</ol>
</edukamu-section>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 9;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
If you have more than one email address associated with your account on GitHub.com, click the email address drop-down menu and select the email address to use as the Git author email address. Only verified email addresses appear in this drop-down menu. If you enabled email address privacy, then [username]@users.noreply.github.com is the default commit author email address.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/2-commit-description-box.png" alt="Screenshot showing a commit change with a description box and the drop-down menu of the email to select as the author of the commit." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; max-width: 70%;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 10;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Below the commit message fields, decide whether to add your commit to the current branch or to a new branch. If your current branch is the default branch, you should choose to create a new branch for your commit and then create a pull request.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/2-create-a-new-branch.png" alt="Screenshot showing creating a new branch from a commit option select with the textbox of the new branch below it." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 11;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Click Commit changes or Propose changes.
</li>
</ol>
</edukamu-section>

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-green">
In short, repositories are like little databases that contains files, images, and other resources related to a project. 

If you followed the instructions above, you've already created a new repository and started populating it with files – and not only that, you've also created a new branch and made a commit!

If, for one reason or another, you’re unable to use GitHub, don’t worry. Even though this course contains many practical exercises and instructions, completing them is not a requirement for passing the course. We strongly recommend that you explore GitHub on your own as well, but it’s not mandatory.

All right, then! Before reviewing branches and commits, let’s quickly check out gists and wikis since they are actually similar to repositories.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Gists and Wikis
</edukamu-collapse-hidden-title>

### Gists

Now that we have a good understanding of repositories, we can review gists. Similarly to repositories, gists are a simplified way to share code snippets with others.

Every gist is a Git repository, which you can fork and clone and can be either public or secret.

Public gists are displayed publicly where people can browse new ones as they’re created. Public gists are also searchable.

Conversely, secret gists are not searchable, but they aren’t entirely private. If you send the URL of a secret gist to a friend, they'll be able to see it.


### Wikis

Every repository on GitHub.com comes equipped with a section for hosting documentation, called a wiki.

You can use your repository's wiki to share long-form content about your project, such as how to use it, how you designed it, or its core principles.

While a README file quickly tells what your project can do, you can use a wiki to provide additional documentation.

It’s worth a reminder that if your repository is private, only people who have at least read access to your repository have access to your wiki.

</edukamu-collapse>
<br>


As you see, there are many ways to keep track of your data and other resources on GitHub. 

Sometimes during product development, you'll want to try our something different before affecting the main version – often regarded to as the master – of your code. That's when you'll need branches, while commits are like little snapshots of your code at a specific point in time.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Branches and Commits
</edukamu-collapse-hidden-title>

### Branches

Just a moment ago, we created a new file in the last section, along the way to you also created a new branch in your repositories.

Branches are an essential part to the GitHub experience because they're where we can make changes without affecting the entire project we're working on.

Your branch is a safe place to experiment with new features or fixes. If you make a mistake, you can revert your changes or push more changes to fix the mistake. Your changes won't update on the default branch until you *merge* your branch.

**Note**: Instead of merging, you can create a new branch and check it out by simply using git in a terminal the command would be: `git checkout -b newBranchName`

### Commits

As you might have noticed in the previous unit, adding in a new file into the repository, you needed to push a commit.

Let’s briefly review what commits are.

A commit is a change to one or more files on a branch. Every time a commit is created, it's assigned a unique ID and tracked, along with the time and contributor. Commits provide a clear audit trail for anyone reviewing the history of a file or linked item, such as an issue or pull request.

<edukamu-image url="/graphics/module1/2-commits.png" alt="A screenshot of a list of GitHub commits to a main branch." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Within a git repository, a file can exist in several valid states as it goes through the version control process:

The primary states for a file in a Git repository are:
* Untracked: An initial state of a file when it isn't yet part of the Git repository. Git is unaware of its existence.
* Tracked: A tracked file is one that Git is actively monitoring. It can be in one of the following substates:
    * Unmodified: The file is tracked, but it hasn't been modified since the last commit.
    * Modified: The file has been changed since the last commit, but these changes aren't yet staged for the next commit.
    * Staged: The file has been modified, and the changes have been added to the staging area (also known as the index). These changes are ready to be committed.
    * Committed: The file is in the repository's database. It represents the latest committed version of the file.

These states and substates are important to collaborating with your team to know where each and every commit is in the process of your project.

</edukamu-collapse>
<br>


Imagine you've been assigned to create a login page for a website. First, you'd create a branch called "feature-login" to work on it. Once done, you'd merge it back into the main branch and create a commit with a message like "Added login page layout." 

Commits serve as milestones in your project's development, working hand-in-hand with branches to make product development more accessible and easier to follow even for newcomers just joining your team!

When a new feature is ready, it needs to be added to the main branch. Thanks to GitHub, such a technically challenging task is made simple with pull requests.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Pull Requests
</edukamu-collapse-hidden-title>

Now that we know what a commit is, let’s review pull requests.

A pull request is the mechanism used to signal that the commits from one branch are ready to be merged into another branch.

The team member submitting the pull request requests one or more reviewers to verify the code and approve the merge. These reviewers have the opportunity to comment on changes, add their own, or use the pull request itself for further discussion.

Once the changes have been approved (if approval is required), the pull request's source branch (the compare branch) is merged into the base branch.

<edukamu-image url="/graphics/module1/2-pull-request.png" alt="A screenshot of a pull request and a comment within the pull request."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

</edukamu-collapse>
<br>


In essence, pull requests act as a bridge between branches, allowing for collaborative code review and integration. They enhance the development process by providing a systematic and controlled way to introduce changes to the main codebase.

Circling back to the login page example, after completing the login feature on the "feature-login" branch, you'd create a pull request titled "Add Login Feature." Once the team approves and the checks pass, the changes are merged into the main branch, incorporating your new login feature into the project.

Just like that, we've reviewed all the basic components of a *GitHub flow*. Let's see what we get when we combine the ingredients!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### GitHub Flows
</edukamu-collapse-hidden-title>

<edukamu-image url="/graphics/module1/2-branching.png" alt="Screenshot showing a visual representation of the GitHub Flow in a linear format that includes a new branch, commits, pull request, and merging the changes back to main in that order."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The GitHub flow can be defined as a lightweight workflow that allows for safe experimentation. You can test new ideas and collaboration with your team by using branching, pull requests, and merging.

Now that we know the basics of GitHub we can walk through the GitHub flow and its components.
1. The first step of the GitHub flow is creating a branch so that the changes, features, and fixes you create don't affect the main branch.
2. The second step is to make your changes. We recommend deploying changes to your feature branch before merging into the main branch. Doing so ensures the changes are valid in a production environment.
3. The third step is to create a pull request to ask collaborators for feedback. Pull request review is so valuable that some repositories require an approving review before pull requests can be merged.
4. Next is the fourth step of reviewing and implementing your feedback from your collaborators.
5. The fifth step, once you’re feeling great about your changes now it's time to get your pull request approved and merge it into the main branch.
6. The sixth and final step is to delete your branch. Deleting your branch signals your work on the branch is completed and prevents you or others from accidentally using old branches.

And that’s it, you're now familiar with a whole GitHub flow cycle!

</edukamu-collapse>
<br>


Project management and product development might sound like a challenging combination but, with services like GitHub, they can be made much more straightforward and enjoyable for all the participants regardless of their role.

<edukamu-note class="edukamu-note-icon-info">
### Why GitHub? 

As we are about to embark on an adventure to master the fundamental features of GitHub, an important question might arise. Namely: Why are we studying GitHub, if this micro degree should be all about Microsoft Azure? Isn't GitHub a separate service?

Well, yes and no. In business terms, GitHub is a subsidiary of Microsoft, which means it's also highly compatible with Microsoft's services, like Azure. And for each Azure developer, GitHub can be an invaluable companion as they continue building applications and services that continue to astonish us.

That being said, GitHub is not the only collaborative service available, but it’s certainly among the most versatile options – especially when used in tandem with services provided by Microsoft.
</edukamu-note>
<br>


Let's find out a little bit more about how Microsoft Azure and GitHub work together to empower aspiring Azure developers such as yourself.

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="arrow-logo">
### GitHub and DevOps
</edukamu-collapse-hidden-title>

You may have heard about DevOps, a collaborative approach that integrates development and operations teams to streamline and automate processes for faster and more reliable delivery. How does GitHub support DevOps?

One integral part of DevOps practices is continuous integration and delivery, also referred to as CI/CD. CI/CD means building, testing, and deploying applications directly and automatically from the version control system, which reduces the time it takes to deploy patches and new releases from weeks to hours, or even faster.

GitHub Actions is an integrated CI/CD and automation service. It allows you to define workflows directly within your repository that can be triggered by events such as pushes, pull requests, or manual triggers. You can configure workflows to pull code from GitHub repositories, build the application, run tests, and deploy it automatically.

An important scenario for CI/CD is automated testing of changes as soon as they are committed. This allows identifying bugs, issues and security vulnerabilities early in the development process, reducing the time and effort required for debugging later.

Faster development processes also lead to a reduced time to market. This can be a significant business advantage in today's competitive software market, where new features and updates must be rolled out continuously.

If you’re collaborating with organizations with other solutions for DevOps pipelines, GitHub also integrates seamlessly with other popular CI/CD tools like Jenkins, CircleCI, and Travis CI.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Improving Microsoft Azure Development with GitHub
</edukamu-collapse-hidden-title>

GitHub makes developing cutting-edge AI applications in Microsoft Azure smoother and more exciting. Let's check out how, shall we?

Picture this: crafting AI models together, managing your work with ease, and making your way through Azure's powerful tools. GitHub, your friend in coding, opens up a world of opportunities.

(If you run across unknown terminology or concepts that make you scratch your head, worry not! We'll explore each and every one of them during this course!)

### Benefit 1: Working Together on Code

See how GitHub helps you and your team keep track of your work. It's like having a neat and organized canvas for your AI projects, ensuring they're always ready and up-to-date for the next big idea.

### Benefit 2: Working Together on AI Models

Break away from solo work as GitHub's features, like pull requests and discussions, make teamwork a breeze. Your AI models, kept safe and sound on GitHub, become collaborative masterpieces.

### Benefit 3: Making Things Easier with Azure Pipelines

Explore Azure pipelines, essentially project workflows, that connect seamlessly with GitHub. Learn how to automate different steps when working on your AI projects. It's like setting up a series of helpful assistants that take care of routine tasks and let you and your colleagues and friends focus on stuff that's actually important.

### Benefit 4: Automating Tasks with GitHub Actions

Discover GitHub Actions, a tool that helps you automate your work. It's like having a robot friend that follows your instructions, making sure your AI tasks are done quickly and without any mistakes.

### Benefit 5: Making Azure Resources Work with GitHub

See how GitHub and Azure work together smoothly. Imagine your AI projects working hand in hand with the resources on Azure... It's as if you has a translator that makes sure everyone understands each other at all times, regardless of the (programming) language!

### Benefit 6: Keeping Track of Your Work

Explore the collaboration between Azure Boards and GitHub Issues. In essence, it's like a shared calendar, which lets everyone can see what's happening. This, in turn makes your AI projects organized and easy to follow.

Now, imagine your part in this adventure. Envision yourself becoming a GitHub expert, guiding your AI projects through new possibilities. Your journey with Azure is about to become even more exciting with GitHub as your trusty sidekick.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-green">
Along this course, we'll explore GitHub from many perspectives. At all times, remember this fundamental question: *How could I use GitHub to improve my workflows and code over at Microsoft Azure?* You'll soon come up with quite a few answers!

Since we've now covered all the main features of GitHub, it's the perfect time for an exercise, don't you think? It's the first one of this course, so take your time!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: The ABC of GitHub
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module1/introduction-to-github-text-poll.yaml" id="dzir0yav206d5x68"/>
<br>
<edukamu-text-poll url="/exercises/module1/introduction-to-github-text-poll-2.yaml" id="2814s6uam12zd5bf"/>
<br>
<edukamu-text-poll url="/exercises/module1/introduction-to-github-text-poll-3.yaml" id="w15j715377k27p50"/>
<br>
<edukamu-text-poll url="/exercises/module1/introduction-to-github-text-poll-4.yaml" id="7p2j38h0yfo63an0"/>
<br>
<edukamu-text-poll url="/exercises/module1/introduction-to-github-text-poll-5.yaml" id="4b43zx3211ti909u"/>
<br>
<edukamu-text-poll url="/exercises/module1/introduction-to-github-text-poll-6.yaml" id="aq293cq65q0pn341"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/1/introduction-to-github?question=dzir0yav206d5x68">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


At any time, if an exercise seems challenging, please take time to recap and review the current topic. On Edukamu courses you can advance at your own pace, so there's no need to hurry!

Let's dive right into our second topic!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
