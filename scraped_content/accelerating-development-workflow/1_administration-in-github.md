## Administration in GitHub

Imagine GitHub as a bustling city, in which people live and work in harmony with each other completing daily tasks and achieving great feats by solving issues through discussions. In a city like this, infrastructure is vital, since without it, the city as a whole just wouldn't work.

Now imagine that GitHub is such a city, with developers as its creative inhabitants, constantly building and expanding. Now, who manages the city's infrastructure, ensures smooth traffic flow, and keeps everything organized? That's the work of administrators, serving as the city planners, architects, and organizers of this GitHub metropolis. 

GitHub Administration is not just about rule-setting; it's about empowering teams to build exceptional projects. It's about fostering a culture of collaboration, innovation, and secure development. A well-administered GitHub environment ensures that the city of code thrives, attracting developers and contributors from all corners of the programming world.

On this page, we'll spend a while focusing on administration in GitHub. In order to better understand the main principles, it's best to look at administration from different perspectives or, in this case, levels: team, organization, and enterprise.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Administration at Team Level
</edukamu-collapse-hidden-title>

In GitHub, each user is an organization member that you can add to a team. You can create teams in your organization with cascading access permissions and mentions to reflect your company or group's structure. Teams are useful for refining repository permissions on a more granular level and enabling communication and notification between team members.

<edukamu-image url="/graphics/module1/teams.png" alt="Screenshot of the organization screen with the Teams tab highlighted." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Additionally, GitHub allows you to sync your teams with identity provider (IdP) groups such as Microsoft Entra ID. When you synchronize a GitHub team with Microsoft Entra ID, you can replicate changes to GitHub automatically, which reduces the need for manual updates and custom scripts. You can use Microsoft Entra ID with team synchronization to manage administrative tasks such as onboarding new members, granting new permissions, and removing member access to the organization.

Members of a team with *team maintainer* or repository *admin* permissions can:
* Create a new team, and select or change the parent team.
* Delete or rename a team.
* Add or remove organization members from a team, or synchronize a GitHub team's membership with an IdP group.
* Add or remove outside collaborators (people who aren't explicitly members of your organization, such as consultants or temporary employees) from team repositories.
* Enable or disable team discussions on the team's page.
* Change the visibility of the team within the organization.
* Manage automatic code review assignment for pull requests, utilizing GitHub's review assignment routing algorithm.
* Schedule reminders.
* Set the team profile picture.


### Best Practices

Creating teams in your organization enables greater flexibility for collaboration and can make it easier to separate repositories and permissions. The following are some best practices for setting up teams on GitHub:
* Create nested teams to reflect your group or company's hierarchy within your GitHub organization.
* Create teams based on interests or specific technology (JavaScript, data science, etc.) to help streamline PR review processes. Individuals can choose to join these teams according to their interests or skills.
* Enable team synchronization between your identity provider (IdP) and GitHub to allow organization owners and team maintainers to connect teams in your organization with IdP groups. When you synchronize a GitHub team with an IdP group, you can replicate changes to GitHub automatically, reducing the need for manual updates and custom scripts. You can use an IdP with team synchronization to manage administrative tasks such as onboarding new members, granting new permissions, and removing member access to the organization.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Administration at Organization Level
</edukamu-collapse-hidden-title>

In GitHub, organizations are shared spaces enabling users to collaborate across many projects at once. Owners and administrators can manage member access to the organization's data and repositories with sophisticated security and administrative features.

Members of an organization with the *owner* permission can perform a wide range of activities at the organization level including:
* Invite users to join the organization and remove members from the organization.
* Organize users into a team, and grant "team maintainer" permissions to organization members.
* Add or remove outside collaborators (people who aren't explicitly members of your organization, such as consultants or temporary employees) to organizational repositories.
* Grant repository permission levels to members, and set the base (default) permission level for a given repository.
* Set up organization security.
* Set up billing or assign a billing manager for the organization.
* Extract various types of information about repositories via the use of custom scripts.
* Apply organization-wide changes such as migrations via the use of custom scripts.

We recommend setting up only one organization for your users and repositories. If specific constraints in your company require you to create multiple organizations, be aware that:
* It isn't possible to duplicate an organization or share configurations between two organizations. This means that you must set up everything from scratch every time you create an organization, which increases the risk of errors in your settings.
* Depending on your software providers' policies, you might incur extra costs if you need to install some applications in multiple organizations.
* Managing multiple organizations is generally more difficult!

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. Administration at Enterprise Level
</edukamu-collapse-hidden-title>

Enterprise accounts include GitHub Enterprise Cloud and Enterprise Server instances and enable owners to centrally manage policy and billing for multiple organizations.

At the enterprise level, members of an enterprise with the *owner* permissions can:
* Enable SAML single sign-on for their enterprise account, allowing each enterprise member to link their external identity on your identity provider (IdP) to their existing GitHub account.
* Add or remove organizations from the enterprise.
* Set up billing or assign a billing manager for all organizations in the enterprise.
* Set up repository management policies, project board policies, team policies, and other security settings that apply to all the organizations, repositories, and members in the enterprise.
* Extract various types of information about organizations via the use of custom scripts.
* Apply enterprise-wide changes such as migrations via the use of custom scripts.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-green">
Even though the actual duties may vary a little, the goal of every GitHub administrator is to keep everything working smoothly for all users, regardless of the level.

One of the most important duties of GitHub administrators is user authentication since, in essence, we're talking about the core security of a GitHub environment. There are several authentication options available in GitHub, as you'll soon see.

In this context, authentication refers to the process of logging in and accessing GitHub, for example. Next, we'll review a few common authentication methods.
</edukamu-section>
<br>

<edukamu-tabs theme="edukamu-tabs1">

<edukamu-tabs-tab title="Personal Access Tokens">
<edukamu-image url="/graphics/module1/personal-access-token.png" alt="Screenshot of the personal access token screen." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br> 

Personal access tokens (PATs) are an alternative to using passwords for authentication to GitHub when using the GitHub API or the command line. Users generate a token via the GitHub's settings option, and tie the token permissions to a repository or organization. When users interact with GitHub by using the git command-line tool, they can enter the token information when they're asked for their username and password.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="SSH Keys">
As an alternative to using personal access tokens, users can connect and authenticate to remote servers and services via SSH with the help of SSH keys. SSH keys eliminate the need for users to supply their username and personal access token for every interaction.

When setting up SSH, users generate an SSH key, add it to the ssh-agent and then add the key to their GitHub account. Adding the SSH key to the ssh-agent ensures that the SSH key has a passphrase as an extra layer of security. Users can configure their local copy of git to automatically supply the passphrase, or they can supply it manually each time they use the git command-line tool to interact with GitHub.

You can even use SSH keys with a repository owned by an organization that uses SAML single sign-on. If the organization provides SSH certificates, users can also use it to access the organization's repositories without adding the certificate to their GitHub account.

### Deploy Keys

Deploy keys are another type of SSH key in GitHub that grants a user access to a single repository. GitHub attaches the public part of the key directly to the repository instead of a personal user account, and the private part of the key remains on the user's server. Deploy keys are read-only by default, but you can give them write access when adding them to a repository.
</edukamu-tabs-tab>

</edukamu-tabs>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Personal Access Tokens
</edukamu-collapse-hidden-title>

<edukamu-image url="/graphics/module1/personal-access-token.png" alt="Screenshot of the personal access token screen." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br> 

Personal access tokens (PATs) are an alternative to using passwords for authentication to GitHub when using the GitHub API or the command line. Users generate a token via the GitHub's settings option, and tie the token permissions to a repository or organization. When users interact with GitHub by using the git command-line tool, they can enter the token information when they're asked for their username and password.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### SSH Keys
</edukamu-collapse-hidden-title>

As an alternative to using personal access tokens, users can connect and authenticate to remote servers and services via SSH with the help of SSH keys. SSH keys eliminate the need for users to supply their username and personal access token for every interaction.

When setting up SSH, users generate an SSH key, add it to the ssh-agent and then add the key to their GitHub account. Adding the SSH key to the ssh-agent ensures that the SSH key has a passphrase as an extra layer of security. Users can configure their local copy of git to automatically supply the passphrase, or they can supply it manually each time they use the git command-line tool to interact with GitHub.

You can even use SSH keys with a repository owned by an organization that uses SAML single sign-on. If the organization provides SSH certificates, users can also use it to access the organization's repositories without adding the certificate to their GitHub account.

### Deploy Keys

Deploy keys are another type of SSH key in GitHub that grants a user access to a single repository. GitHub attaches the public part of the key directly to the repository instead of a personal user account, and the private part of the key remains on the user's server. Deploy keys are read-only by default, but you can give them write access when adding them to a repository.

</edukamu-collapse> -->

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Enhanced Security Options
</edukamu-collapse-hidden-title>

GitHub also offers the following extra security options. Using them might feel bothersome at first, but in the long run, paying attention to authentication will surely pay off.

### 1. Two-factor Authentication

<edukamu-image url="/graphics/module1/2-factor-authentication.png" alt="Screenshot of the two-factor authentication screen." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Two-factor authentication (2FA), sometimes known as multifactor authentication (MFA), is an extra layer of security used when logging into websites or apps. With 2FA, users have to sign in with their username and password and provide another form of authentication that only they have access to.

For GitHub, the second form of authentication is a code generated by an application on a user's mobile device or sent as a text message (SMS). After a user enables 2FA, GitHub generates an authentication code anytime someone attempts to sign into their GitHub account. Users can only sign into their account if they know their password and have access to the authentication code on their phone.

Organization owners can require organization members, outside collaborators, and billing managers to enable two-factor authentication for their personal accounts, making it harder for malicious actors to access an organization's repositories and settings.

Enterprise owners can also enforce certain security policies for all organizations owned by an enterprise account.

### 2. SAML SSO

If you centrally manage your users' identities and applications with an identity provider (IdP), you can configure Security Assertion Markup Language (SAML) single sign-on (SSO) to protect your organization's resources on GitHub.

This type of authentication gives organization and enterprise owners on GitHub a way to control and secure access to organization resources like repositories, issues, and pull requests. Organization owners can invite GitHub users to join the organization that uses SAML SSO, which allows those users to contribute to the organization and retain their existing identity and contributions on GitHub.

When users access resources within an organization that uses SAML SSO, GitHub will redirect them to the organization's SAML IdP for authentication. After they successfully authenticate with their account on the IdP, the IdP redirects to GitHub to access the organization's resources.

GitHub offers limited support for all identity providers that implement the SAML 2.0 standard with official support for several popular identity providers including:
* Active Directory Federation Services (AD FS)
* Microsoft Entra ID
* Okta
* OneLogin
* PingOne

... among others.

### 3. LDAP

Lightweight directory access protocol (LDAP) is a popular application protocol for accessing and maintaining directory information services. LDAP lets you authenticate GitHub Enterprise Server against your existing accounts and centrally manage repository access. It's one of the most common protocols used to integrate third-party software with large company user directories.

GitHub Enterprise Server integrates with popular LDAP services like:
* Active Directory
* Oracle Directory Server Enterprise Edition
* OpenLDAP
* Open Directory

... among others.

</edukamu-collapse>
<br>


Administrators can allow users to continue using the default username and password authentication method, sometimes known as the "basic" HTTP authentication scheme. In recent years, however basic authentication has proven to be too risky when dealing with highly sensitive information, so we strongly recommend using one (or several) of the other options we just covered.

All right, it's time to review the contents of this page with an exercise. Take your time and recap a little before tackling it!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Administration in GitHub
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/administration-in-github-question-scroll.yaml" id="6q69580n5evo316u">
<br>

</edukamu-collapse>
<br>


GitHub administrators do important work securing smooth and productive workflows for everyone involved in a project. When developing solutions on Microsoft Azure, for example, GitHub can be an invaluable tool.

On this page, we explored authentication options available in GitHub. Next, we'll focus on another important aspect of security: permissions.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
