## Authentication and Authorization

Azure makes sure that only authorized people have access to the stored data. That’s not all, though, as Azure’s authorization and authentication practices in place go well beyond.

In this section, you will be introduced to the Azure identity, access, and security services and tools. You will learn about directory services in Azure, authentication methods, and access control. 

<edukamu-note class="edukamu-note-icon-info">
This is a great place to remind you about Zero Trust, a simplified approach to making security measures even more effective. This topic was covered in our course [Elements of Cloud and Cybersecurity](https://cs.edukamu.fi/elements-of-cloud-and-cybersecurity)(target="_blank"). This course is also part of the Microsoft Skills for Jobs.
<br>
<br>
<edukamu-image url="/graphics/module2/zero-trust.png" alt="Diagram comparing zero trust authenticating everyone compared to classic relying on network location." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
</edukamu-note>
<br>


### Secure Login with Azure AD

Azure Active Directory (Azure AD) is a cloud-based identity and access management service. In essence, it is a service that allows you and your employees to access external services, such as Microsof 365, safely and securely.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Who Can Use Azure AD?
</edukamu-collapse-hidden-title>

Azure AD is suitable for:

* **IT administrators**. Administrators can use Azure AD to control access to applications and resources based on their business requirements.
* **App developers**. Developers can use Azure AD to provide a standards-based approach for adding functionality to applications that they build, such as adding SSO functionality to an app or enabling an app to work with a user's existing credentials.
* **Users**. Users can manage their identities and take maintenance actions like self-service password reset.
* **Online service subscribers**. Microsoft 365, Microsoft Office 365, Azure, and Microsoft Dynamics CRM Online subscribers are already using Azure AD to authenticate into their account.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### What Services Does Azure AD Offer?
</edukamu-collapse-hidden-title>

Azure AD is meant to make logins and connections to external services more safe and secure. The package includes services such as:

* **Authentication**: This includes verifying identity to access applications and resources. It also includes providing functionality such as self-service password reset, multifactor authentication, a custom list of banned passwords, and smart lockout services.
* **Single sign-on**: Single sign-on (SSO) enables you to remember only one username and one password to access multiple applications. A single identity is tied to a user, which simplifies the security model. As users change roles or leave an organization, access modifications are tied to that identity, which greatly reduces the effort needed to change or disable accounts.
* **Application management**: You can manage your cloud and on-premises apps by using Azure AD. Features like Application Proxy, SaaS apps, the My Apps portal, and single sign-on provide a better user experience.
* **Device management**: Along with accounts for individual people, Azure AD supports the registration of devices. Registration enables devices to be managed through tools like Microsoft Intune. It also allows for device-based Conditional Access policies to restrict access attempts to only those coming from known devices, regardless of the requesting user account.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
### Azure Authentication Methods

Authentication is the process of establishing the identity of a person, service, or device. It requires the person, service, or device to provide some type of credential to prove who they are. Authentication is like presenting ID when you’re traveling. It doesn’t confirm that you’re ticketed, it just proves that you're who you say you are. Azure supports multiple authentication methods, including standard passwords, single sign-on (SSO), multifactor authentication (MFA), and passwordless.

For the longest time, security and convenience seemed to be at odds with each other. Thankfully, new authentication solutions provide both security and convenience.
The following diagram shows the security level compared to the convenience. Notice Passwordless authentication is high security and high convenience while passwords on their own are low security but high convenience.

<edukamu-image url="/graphics/module2/passwordless-convenience-security.png" alt="Four quadrant diagram showing security vs convenience, with Passwords + 2 Factor authentication being high security but low convenience." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<br>
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Passwordless Authentication
</edukamu-collapse-hidden-title>

Features like MFA (Multifactor Authentication – password protection enforced with a one-time keycode, for example) are a great way to secure your organization, but users often get frustrated with the additional security layer on top of having to remember their passwords. 

People are more likely to comply when it's easy and convenient to do so. Passwordless authentication methods are more convenient because the password is removed and replaced with something you have, plus something you are, or something you know.

Passwordless authentication needs to be set up on a device before it can work. For example, your computer is something you have. Once it’s been registered or enrolled, Azure now knows that it’s associated with you. Now that the computer is known, once you provide something you know or are (such as a PIN or fingerprint), you can be authenticated without using a password.

Each organization has different needs when it comes to authentication. Microsoft global Azure and Azure Government offer the following three passwordless authentication options that integrate with Azure Active Directory (Azure AD):

* Windows Hello for Business
* Microsoft Authenticator app
* FIDO2 security keys.

</edukamu-collapse>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Storage and Safety
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-quiz url="/exercises/module2/authentication-and-authorization-text-quiz.yaml" theme="text-quiz-no-answer-colors" id="3fj891h7947gt9u2"/>
<br>

<edukamu-text-quiz url="/exercises/module2/authentication-and-authorization-text-quiz-2.yaml" theme="text-quiz-no-answer-colors" id="275t034o1jo8x9i8"/>
<br>

<edukamu-text-quiz url="/exercises/module2/authentication-and-authorization-text-quiz-3.yaml" theme="text-quiz-no-answer-colors" id="yx98z53u94z5d721"/>
<br>

<edukamu-text-quiz url="/exercises/module2/authentication-and-authorization-text-quiz-4.yaml" theme="text-quiz-no-answer-colors" id="4pr799o1967g4y0r"/>
<br>

</edukamu-collapse>
<br>

These are just some of the means Azure takes to protect you and your data. Denying unauthorized access is perhaps the most crucial aspect of authentication and authorization, but there’s more to it than you may think. Azure keeps an eye on everyone’s identity on login, but external parties can also join in, if you want them to. Let’s move on. 

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/2024-02-21/1920px/da-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
