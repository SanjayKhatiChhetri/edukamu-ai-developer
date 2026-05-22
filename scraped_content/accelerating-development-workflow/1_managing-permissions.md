## Managing Permissions

Close your eyes again and return to the bustling and modern (yet still surprisingly well-structured and accessible) mega city of GitHub. In this place, collaboration is the key, code flows like traffic, and permissions act as the city's governing laws. In this city, like in each of its real-life counterparts, understanding the laws is vital for making it – and the same applies to GitHub.

In a way, GitHub repositories are like office buildings in a city and user roles like professions. In this analogy, permissions would serve as keys that allow entrance to one of the offices – your own – while keeping unwanted visitors out.

In GitHub, permissions and user roles go hand in hand, as you'll soon see. Permissions can be managed on different levels as well, which is a great place to begin.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Permissions on a Repository Level
</edukamu-collapse-hidden-title>

You can customize access to a given repository by assigning permissions. There are five repository-level permissions:
* **Read** - Recommended for non-code contributors who want to view or discuss your project. This level is good for anyone that needs to view the content within the repository but doesn't need to actually make contributions or changes.
* **Triage** - Recommended for contributors who need to proactively manage issues and pull requests without write access. This level could be good for some project managers who manage tracking issues but don't make any changes.
* **Write** - Recommended for contributors who actively push to your project. Write is the standard permission for most developers.
* **Maintain** - Recommended for project managers who need to manage the repository without access to sensitive or destructive actions.
* **Admin** - Recommended for people who need full access to the project, including sensitive and destructive actions like managing security or deleting a repository. These people are repository owners and administrators.

You can give organization members, outside collaborators, and teams different levels of access to repositories owned by an organization. Each permission level progressively increases access to a repository's content and settings. Choose the level that best fits each person or team's role in your project without giving more access to the project than necessary.

After you create a repository with the correct permissions, you can make it a template so that anyone who has access to the repository can generate a new repository that has the same directory structure and files as your default branch. To make a template:
1. On GitHub.com, go to the main page of the repository.
2. Under the repository name, select **Settings**. If you can't see the **Settings** tab, open the dropdown menu and then select **Settings**.

<edukamu-image url="/graphics/module1/repository-actions-settings.png" alt="Screenshot showing where to locate the settings button in your GitHub repository." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold">Template repository</span>.
</li>
</ol>
</edukamu-section>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Permissions on a Team Level
</edukamu-collapse-hidden-title>

Teams provide an easy way to assign repository permissions to several related users at once. Members of a child team also inherit the permission settings of the parent team, providing an easy way to cascade permissions based on the natural structure of a company.

There are two levels of permissions at the team level:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="40%">
Permission level
</edukamu-table-header>
<edukamu-table-header width="60%">
Description
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Member
</edukamu-table-cell>
<edukamu-table-cell >
Team members have the same set of abilities as organization members
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Maintainer
</edukamu-table-cell>
<edukamu-table-cell >
Team maintainers can do everything team members can, plus: 
- Change the team's name, description, and visibility 
- Request that the team change parent and child teams 
- Set the team profile picture 
- Edit and delete team discussions 
- Add and remove organization members from the team 
- Promote team members to also have the team maintainer permission 
- Remove the team's access to repositories 
- Manage code review assignment for the team 
- Manage scheduled reminders for pull requests
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

An organization owner can also promote any member of the organization to be a maintainer for a team.

To audit access to a repository that you administer, you can view a combined list of teams and users with access to your repository in your settings:

<edukamu-image url="/graphics/module1/manage-access-overview.png" alt="Screenshot of the manage access screen." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. Permissions on an Organization Level
</edukamu-collapse-hidden-title>

There are multiple levels of permissions at the organizational level:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="40%">
Permission level
</edukamu-table-header>
<edukamu-table-header width="60%">
Description
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Owner
</edukamu-table-cell>
<edukamu-table-cell >
Organization owners can do everything that organization members can do, and they can add or remove other users to and from the organization. This role should be limited to no less than two people in your organization.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Member
</edukamu-table-cell>
<edukamu-table-cell >
Organization members can create and manage organization repositories and teams.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Moderator
</edukamu-table-cell>
<edukamu-table-cell >
Organization moderators can block and unblock nonmember contributors, set interaction limits, and hide comments in public repositories that the organization owns.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Billing manager
</edukamu-table-cell>
<edukamu-table-cell >
Organization billing managers can view and edit billing information.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Security managers
</edukamu-table-cell>
<edukamu-table-cell >
Organization security managers can manage security alerts and settings across your organization. They can also read permissions for all repositories in the organization.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Outside collaborator
</edukamu-table-cell>
<edukamu-table-cell >
Outside collaborators, such as a consultant or temporary employee, can access one or more organization repositories. They aren't explicit members of the organization.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

In addition to these levels, you can also set default permissions for all members of your organization:

<edukamu-image url="/graphics/module1/org-base-permissions.png" alt="Screenshot of the member privileges screen with the base permissions dropdown displayed." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

For improved management and security, you might also consider giving default read permissions to all members of your organization and adjusting their access to repositories on a case-by-case basis. If you have a relatively small organization with a low number of users, a low number of repositories, or a combination of the two, this level of restriction might be unnecessary. If you trust everyone with pushing changes to any repository, you might prefer to give all members write permissions by default.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 4. Permissions on an Enterprise Level
</edukamu-collapse-hidden-title>

Recall from earlier that enterprise accounts are collections of organizations. By extension, each individual user account that is a member of an organization is also a member of the enterprise, and you can control various settings related to authentication from this higher level.

There are three levels of permission at the enterprise level:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="40%">
Permission level
</edukamu-table-header>
<edukamu-table-header width="60%">
Description
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Owner
</edukamu-table-cell>
<edukamu-table-cell >
Enterprise owners have complete control over the enterprise and can take every action, including: 
- Managing administrators 
- Adding and removing organizations to and from the enterprise 
- Managing enterprise settings 
- Enforcing policies across organizations 
- Managing billing settings
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Member
</edukamu-table-cell>
<edukamu-table-cell >
Enterprise members have the same set of abilities as organization members
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Billing manager
</edukamu-table-cell>
<edukamu-table-cell >
Enterprise billing managers can only view and edit your enterprise's billing information and add or remove other billing managers
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

In addition to these three levels, you can also set a policy of default repository permissions across all your organizations:

<edukamu-image url="/graphics/module1/enterprise-base-permissions.png" alt="Screenshot of the policies screen with the default permissions dropdown displayed." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"> 
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

For improved management and security, you can give default read permissions to all members of your enterprise and adjust their access to repositories on a case-by-case basis. In a smaller enterprise, such as one with a single, relatively small organization, you might prefer to trust all members with write permissions by default.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-green">
If you're ever in charge of GitHub administration, paying attention to different organizational levels and job duties is a great place to begin when handling permissions.

Just managing user permissions and authentication methods might not be enough to secure projects, however. This is especially true when your team's repositories are filled with fundamental, invaluable data. That's when you should also think about security and management on a repository level.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Repository Security and Management
</edukamu-collapse-hidden-title>

You can oversee the security and management of your repositories in several ways.

### 1. Creating Protection Rules

To manage changes to content within your repository, you can create branch protection rules to enforce certain workflows for one or more branches. Protection rules that can be applied to a branch include:
* Require a pull request before merging.
* Require status checks to pass before merging.
* Require conversation resolution before merging.
* Require signed commits.
* Require linear history.
* Require merge queue.
* Require deployments to succeed before merging.
* Lock the branch by making it read-only.
* Restrict who can push to matching branches.

Additionally, you can set branch rules that apply to everyone, including administrators. For example, you can allow force pushes to matching branches and allow deletions from users who have push access.

### 2. Adding CODEOWNERS Files

By adding a CODEOWNERS file to your repository, you can assign team members or entire teams as code owners who are responsible for code in the repository. When someone opens a pull request that modifies code that belongs to a code owner, the code owner is automatically requested as a reviewer.

You can create the CODEOWNERS file in either the root of the repository or in the `docs` or `.github` folder.

### 3. Using Traffic Insights

Anyone who has push access to a repository can view its traffic. In the traffic graph, they can view full clones (not fetches), visitors from the past 14 days, referring sites, and popular content.

To access the traffic graph:
1. On GitHub.com, go to the main page of the repository.
2. Under your repository name, select **Insights**.

<edukamu-image url="/graphics/module1/repository-navigation-insights-tab.png" alt="Screenshot showing where to locate the Insights button in GitHub." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
On the left, select <span style="font-weight: bold">Traffic</span>.
</li>
</ol>
</edukamu-section>

<edukamu-image url="/graphics/module1/traffic-tab.png" alt="Screenshot showing the Traffic tab highlighted in GitHub." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br>

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Optionally, you can select <span style="font-weight: bold">Clones</span> or <span style="font-weight: bold">Views</span> to see the traffic graph for clones or views.
</li>
</ol>
</edukamu-section>

</edukamu-collapse>
<br>


The above examples are something to keep in mind when designing security strategies for you and your team. The best policy is often to treat all data as if it was invaluable for your organization: it's better to be safe than sorry!

All right, it's time for the last exercise of this unit!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Permissions in GitHub
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/managing-permissions-question-scroll.yaml" id="o73w31o05o323b6c">
<br>

</edukamu-collapse>
<br>


That's the first unit in the bag, well done!

We've now explored the basic functionalities of GitHub from various perspectives. In the second unit, we'll get acquainted with GitHub Copilot.

If you thought that GitHub alone is impressive, wait until you see the capabilities of GitHub Copilot!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
