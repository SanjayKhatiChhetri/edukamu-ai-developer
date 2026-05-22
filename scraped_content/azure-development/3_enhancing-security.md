<edukamu-video content="/videos/devai-6-unit3-video.yaml"/>
<br>

## Enhancing Security

Welcome to the third and final unit of this course!

So far, we've explored Azure development from multiple perspectives. Building on the foundation laid during the earlier courses of this program, we've explored tools and services like web apps, Azure Functions, and containerized solutions while consolidating our knowledge.

In the third unit, we have three main targets: 1) deepen our understanding about solution security, 2) exploring API management capabilities, and 3) reviewing a few advanced capabilities available in Microsoft Azure.

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="devisioona-logo">
### Real-World View: Non-functional Requirements May Seem Boring, but They are Still Critical.
</edukamu-collapse-hidden-title>

When you ask somebody to describe a piece of software, they start by describing its *functional* component: what does the software do, who uses it and what benefits it brings. Business value is key: software would be useless if there were no compelling answers to the previous questions.

So that’s how we describe software, but when building it, we often have to spend almost equal effort for the *non-functional requirements*. They include operational characteristics such as:

- Security: The system must be safe from external misuse and/or attacks
- Performance: The system must be fast enough to fill its purpose, whether that’s for a background batch system or for an interactive user interface
- Usability: The system must be easy enough to use
- Resilience and reliability: The system must be able to automatically recover from normal errors (e.g., invalid input) and be easily-enough recoverable from catastrophic failures (e.g., erroneous deletion of the database)
- Observability: There must be a way to know what the system is doing, which errors occur and how the system is performing
- Cost-effectiveness: The system should run at the minimal reasonable cost without impacting performance or reliability
- Configurability: The most frequently changed configuration settings must be settable in a way that is least disturbing to the continuous operation of the system
- Integrability: It must be possible to incorporate data into the system as well as out of it

While compute and data services are often sufficient to fulfill the functional requirements, Azure has many supporting services to help build these non-functional capabilities. This chapter will look into some of the key pieces, but there’s a lot more to learn.

The cloud is also continuously expanding: some of the services go way beyond just being a technology platform, rather providing quite good functionalities out of the box. For example, Azure AI Content Safety acts as a moderator for user content, while services such as Azure Digital Twins can reach out quite far to specific fields like real estate digitalization. These services are not covered by this course, but when building a real-world project, you should always be boldly looking into the Azure service catalog to understand what you could be getting pre-built for you.

</edukamu-collapse>
<br>

First, we'll tackle security, which has always been high on Microsoft's list of priorities. More specifically, we'll explore two services, Azure Key Vault and Azure App Configuration, while briefly covering managed identities as well.

Let's get started, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Key Vault
</edukamu-collapse-hidden-title>

Azure Key Vault is a cloud service for securely storing and accessing secrets. As we learned before, secrets can be anything that you want to tightly control access to, such as API keys, passwords, certificates, or cryptographic keys.

The Azure Key Vault service supports two types of containers: vaults and managed hardware security module(HSM) pools. Vaults support storing software and HSM-backed keys, secrets, and certificates. Managed HSM pools only support HSM-backed keys.

Azure Key Vault helps solve the following problems:

- **Secrets Management**: Azure Key Vault can be used to Securely store and tightly control access to tokens, passwords, certificates, API keys, and other secrets.
- **Key Management**: Azure Key Vault can also be used as a Key Management solution. Azure Key Vault makes it easy to create and control the encryption keys used to encrypt your data.
- **Certificate Management**: Azure Key Vault is also a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with Azure and your internal connected resources.

Azure Key Vault has two service tiers: Standard, which encrypts with a software key, and a Premium tier, which includes hardware security module(HSM)-protected keys.


### Key Benefits of Azure Key Vault

**Centralized application secrets**: Centralizing storage of application secrets in Azure Key Vault allows you to control their distribution. For example, instead of storing the connection string in the app's code you can store it securely in Key Vault. Your applications can securely access the information they need by using URIs. These URIs allow the applications to retrieve specific versions of a secret.

**Securely store secrets and keys**: Access to a key vault requires proper authentication and authorization before a caller (user or application) can get access. Authentication is done via Microsoft Entra ID. Authorization may be done via Azure role-based access control (Azure RBAC) or Key Vault access policy. Azure RBAC is used when dealing with the management of the vaults and key vault access policy is used when attempting to access data stored in a vault. Azure Key Vaults may be either software-protected or, with the Azure Key Vault Premium tier, hardware-protected by hardware security modules (HSMs).

**Monitor access and use**: You can monitor activity by enabling logging for your vaults. You have control over your logs and you may secure them by restricting access and you may also delete logs that you no longer need. Azure Key Vault can be configured to:
- Archive to a storage account.
- Stream to an event hub.
- Send the logs to Azure Monitor logs.

**Simplified administration of application secrets**: Security information must be secured, it must follow a life cycle, and it must be highly available. Azure Key Vault simplifies the process of meeting these requirements by:
- Removing the need for in-house knowledge of Hardware Security Modules
- Scaling up on short notice to meet your organization’s usage spikes.
- Replicating the contents of your Key Vault within a region and to a secondary region. Data replication ensures high availability and takes away the need of any action from the administrator to trigger the failover.
- Providing standard Azure administration options via the portal, Azure CLI and PowerShell.
- Automating certain tasks on certificates that you purchase from Public CAs, such as enrollment and renewal.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure App Configuration
</edukamu-collapse-hidden-title>

Azure App Configuration provides a service to centrally manage application settings and feature flags. Modern programs, especially programs running in a cloud, generally have many components that are distributed in nature. Spreading configuration settings across these components can lead to hard-to-troubleshoot errors during an application deployment. Use App Configuration to store all the settings for your application and secure their accesses in one place.

App Configuration offers the following benefits:

- A fully managed service that can be set up in minutes
- Flexible key representations and mappings
- Tagging with labels
- Point-in-time replay of settings
- Dedicated UI for feature flag management
- Comparison of two sets of configurations on custom-defined dimensions
- Enhanced security through Azure-managed identities
- Encryption of sensitive information at rest and in transit
- Native integration with popular frameworks

App Configuration complements Azure Key Vault, which is used to store application secrets. App Configuration makes it easier to implement the following scenarios:

- Centralize management and distribution of hierarchical configuration data for different environments and geographies
- Dynamically change application settings without the need to redeploy or restart an application
- Control feature availability in real-time

### Using App Configuration

The easiest way to add an App Configuration store to your application is through a client library that Microsoft provides. Based on the programming language and framework, the following best methods are available to you.

**Supported programming languages and framework:**

- .NET Core and ASP.NET Core
- .NET Framework and ASP.NET
- Java Spring
- JavaScript/Node.js
- Python
- REST API

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Managed Identities
</edukamu-collapse-hidden-title>

Managed Identities come into play as a key component of the services introduced above. In Azure, managed identities are used to securely authenticate services and applications within the Azure ecosystem without needing to manage credentials. They provide an identity for applications to use when connecting to resources like Key Vault and App Configuration, eliminating the need for developers to manage secrets in their code. This not only simplifies the security model but also enhances it by reducing the risks associated with handling credentials.

There are two types of managed identities:

- A **system-assigned managed identity** is enabled directly on an Azure service instance. When the identity is enabled, Azure creates an identity for the instance in the Microsoft Entra tenant that's trusted by the subscription of the instance. After the identity is created, the credentials are provisioned onto the instance. The lifecycle of a system-assigned identity is directly tied to the Azure service instance that it's enabled on. If the instance is deleted, Azure automatically cleans up the credentials and the identity in Microsoft Entra ID.
- A **user-assigned managed identity** is created as a standalone Azure resource. Through a create process, Azure creates an identity in the Microsoft Entra tenant that's trusted by the subscription in use. After the identity is created, the identity can be assigned to one or more Azure service instances. The lifecycle of a user-assigned identity is managed separately from the lifecycle of the Azure service instances to which it's assigned.

Internally, managed identities are service principals of a special type, which are locked to only be used with Azure resources. When the managed identity is deleted, the corresponding service principal is automatically removed.

The following table highlights some of the key differences between the two types of managed identities.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Characteristic**
</edukamu-table-header>
<edukamu-table-header width="50%">
**System-assigned managed identity**
</edukamu-table-header>
<edukamu-table-header width="30%">
**User-assigned managed identity**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Creation
</edukamu-table-cell>
<edukamu-table-cell>
Created as part of an Azure resource (for example, an Azure virtual machine or Azure App Service).
</edukamu-table-cell>
<edukamu-table-cell>
Created as a stand-alone Azure resource.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Lifecycle
</edukamu-table-cell>
<edukamu-table-cell>
Shared lifecycle with the Azure resource that the managed identity is created with. When the parent resource is deleted, the managed identity is deleted as well.
</edukamu-table-cell>
<edukamu-table-cell>
Independent life-cycle. Must be explicitly deleted.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Sharing across Azure resources
</edukamu-table-cell>
<edukamu-table-cell>
Can't be shared, it can only be associated with a single Azure resource.
</edukamu-table-cell>
<edukamu-table-cell>
Can be shared, the same user-assigned managed identity can be associated with more than one Azure resource.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<edukamu-section class="edukamu-included-only-in-mobile">
<edukamu-section class="edukamu-kuvateksti">
The Table above is horizontally scrollable.
</edukamu-section>
</edukamu-section>
<br>

### When to Use Managed Identities?

The following image gives an overview of the scenarios that support using managed identities. For example, you can use managed identities if you want to build an app using Azure App Services that accesses Azure Storage without having to manage any credentials.

<edukamu-image url="/graphics/module3/managed-identities-use-case.png" alt="Image showing a list of sources that gain access to targets through Microsoft Entra ID." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;">
<br>

Managed identities for Azure resources can be used to authenticate to all services that support Microsoft Entra authentication.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
Together, Azure Key Vault and Azure App Configuration, backed by managed identities, form a powerful trio that ensures your cloud solutions are not only efficient and flexible but also secure. Understanding and implementing these services is essential for building robust and reliable cloud-based applications.

The key differences between Key Vault and App Configuration lie in their use cases:

- **Azure Key Vault** is best used for handling sensitive data that must be kept secure and accessed under strict controls. This includes scenarios like encryption key storage, secrets management for authenticating to other services, and storing certificates for secure communications.
- **Azure App Configuration** is ideal for general configuration management and controlling application features. It's more about operational efficiency and ensuring consistency across various deployments than focusing on security aspects of sensitive data.

In this unit, we'll spend some time exploring both of these services, starting with Azure Key Vault and managed identities. Let's begin with some best practices.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Key Vault Best Practices
</edukamu-collapse-hidden-title>

Azure Key Vault is a tool for securely storing and accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, or certificates. A vault is logical group of secrets.

### Authentication

To do any operations with Key Vault, you first need to authenticate to it. There are three ways to authenticate to Key Vault:

- **Managed identities for Azure resources**: When you deploy an app on a virtual machine in Azure, you can assign an identity to your virtual machine that has access to Key Vault. You can also assign identities to other Azure resources. The benefit of this approach is that the app or service isn't managing the rotation of the first secret. Azure automatically rotates the service principal client secret associated with the identity. We recommend this approach as a best practice.
- **Service principal and certificate**: You can use a service principal and an associated certificate that has access to Key Vault. We don't recommend this approach because the application owner or developer must rotate the certificate.
- **Service principal and secret**: Although you can use a service principal and a secret to authenticate to Key Vault, we don't recommend it. It's hard to automatically rotate the bootstrap secret that's used to authenticate to Key Vault.

### Encryption of Data in Transit

Azure Key Vault enforces Transport Layer Security (TLS) protocol to protect data when it’s traveling between Azure Key Vault and clients. Clients negotiate a TLS connection with Azure Key Vault. TLS provides strong authentication, message privacy, and integrity (enabling detection of message tampering, interception, and forgery), interoperability, algorithm flexibility, and ease of deployment and use.

Perfect Forward Secrecy (PFS) protects connections between customers’ client systems and Microsoft cloud services by unique keys. Connections also use RSA-based 2,048-bit encryption key lengths. This combination makes it difficult for someone to intercept and access data that is in transit.

When using Azure Key Vault, it is recommended to follow the best practices listed below:

- **Use separate key vaults**: Recommended using a vault per application per environment (Development, Pre-Production and Production). This pattern helps you not share secrets across environments and also reduces the threat if there is a breach.
- **Control access to your vault**: Key Vault data is sensitive and business critical, you need to secure access to your key vaults by allowing only authorized applications and users.
- **Backup**: Create regular back ups of your vault on update/delete/create of objects within a Vault.
- **Logging**: Be sure to turn on logging and alerts.
- **Recovery options**: Turn on soft-delete and purge protection if you want to guard against force deletion of the secret.

</edukamu-collapse>
<br>

Both Azure Key Vault and App Configuration use Microsoft Entra to enhance their security. If you've been studying at Microsoft Skills for Jobs before, you've most probably heard of Azure Active Directory (Azure AD). The same service was re-branded as Microsoft Entra in July 2023. In order to avoid confusion, here's a little overview.

<edukamu-note class="edukamu-note-icon-info">
### Microsoft Entra, Azure Active Directory, and Similar Services

Microsoft Entra is an identity and access management solution offered by Microsoft. It plays a pivotal role in securing and managing access to resources in the cloud. The best-known part of the solution is Microsoft Entra ID, a directory of user and application accounts. Until 2023, Entra ID was known as “Azure Active Directory” or just “AAD”. Some learning material will still refer to the old product names, so you should just remember that “Azure Active Directory = Microsoft Entra ID”.

For Azure Key Vault, Microsoft Entra ID  is commonly used for authentication, ensuring that only authenticated and authorized users and applications can access the secrets, keys, or certificates stored in the vault.

Azure App Configuration, on the other hand, also integrates with Entra for authentication and authorization, but its usage is more focused on the secure management of application settings and feature flags. It leverages Azure AD's capabilities to ensure that only authorized users and applications can access and modify the configuration data.
</edukamu-note>
<br>

In summary, while both Azure Key Vault and Azure App Configuration use Microsoft Entra ID for secure authentication and authorization, their primary purposes are different – Key Vault for managing sensitive data and App Configuration for managing application settings and features. Entra ID underpins these services with robust identity management and security features.

In order to find out more about Azure Key Vault, let's explore it with a practical exercise! If you have an active Azure subscription (or a free trial), we recommend that you take on the challenge.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Working Secrets with Azure Key Vault
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

In this exercise you learn how to perform the following actions by using the Azure CLI:

- Create a Key Vault
- Add and retrieve a secret

Follow the instructions below.

### Step 1. Start the Cloud Shell

This step should already be familiar from the previous exercises.

1. Sign in to the Azure Portal and open the **Cloud Shell**.
2. When the shell opens, select the **Bash** environment.


### Step 2. Create a Key Vault

1. Let's set some variables for the CLI commands to use to reduce the amount of retyping. Replace the `< myLocation >` variable string with a region that makes sense for you. The Key Vault name needs to be a globally unique name, and the following script generates a random string.

Bash

```Bash
myKeyVault=az204vault-$RANDOM
myLocation=<myLocation>
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Create a resource group.
</li>
</ol>
</edukamu-section>

Azure CLI

```
az group create --name az204-vault-rg --location $myLocation
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Create a Key Vault by using the <code>az keyvault create</code> command.
</li>
</ol>
</edukamu-section>

Azure CLI

```bash
az keyvault create --name $myKeyVault --resource-group az204-vault-rg --location $myLocation
```

**Note**: The above command can take a few minutes to run, so wait patiently.


### Step 3. Add and Retrieve a Secret

To add a secret to the vault, you just need to take a couple of extra steps.

1. Create a secret. Let's add a password that could be used by an app. The password is called **ExamplePassword** and will store the value of **hVFkk965BuUv** in it.

Azure CLI

```
az keyvault secret set --vault-name $myKeyVault --name "ExamplePassword" --value "hVFkk965BuUv"
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Use the <code>az keyvault secret show</code> command to retrieve the secret.
</li>
</ol>
</edukamu-section>

Azure CLI

```bash
az keyvault secret show --name "ExamplePassword" --vault-name $myKeyVault
```

This command returns some JSON. The last line contains the password in plain text.

JSON

```JSON
"value": "hVFkk965BuUv"
```

You've created a Key Vault, stored a secret, and retrieved it. Well done!


### Step 4. Clean Up Resources (Optional)

If you no longer need the resources in this exercise use the following command to delete the resource group and associated Key Vault.

Azure CLI

```
az group delete --name az204-vault-rg --no-wait
```

</edukamu-collapse>
<br>

As you remember from before, managed identities are a great way of providing an additional layer of security without the need for complex configurations. But how does it actually work? Let's find out by reviewing authentication flows.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Managed Identities: Authentication Flow
</edukamu-collapse-hidden-title>

Managed identities in Azure offer a secure and streamlined authentication flow for applications needing to access Azure services. This authentication flow eliminates the need for developers to manage credentials manually, enhancing security and simplifying the development process.

In this section, we'll look at how managed identities work with Azure virtual machines. Below are the flows detailing how the two types of managed identities work with an Azure virtual machine.

### Flow 1: System-Assigned Identities with Azure Virtual Machines

1. Azure Resource Manager receives a request to enable the system-assigned managed identity on a virtual machine.
2. Azure Resource Manager creates a service principal in Microsoft Entra ID for the identity of the virtual machine. The service principal is created in the Microsoft Entra tenant that's trusted by the subscription.
3. Azure Resource Manager configures the identity on the virtual machine by updating the Azure Instance Metadata Service identity endpoint with the service principal client ID and certificate.
4. After the virtual machine has an identity, use the service principal information to grant the virtual machine access to Azure resources. To call Azure Resource Manager, use role-based access control in Microsoft Entra ID to assign the appropriate role to the virtual machine service principal. To call Key Vault, grant your code access to the specific secret or key in Key Vault.
5. Your code that's running on the virtual machine can request a token from the Azure Instance Metadata service endpoint, accessible only from within the virtual machine: `http://169.254.169.254/metadata/identity/oauth2/token`.
6. A call is made to Microsoft Entra ID to request an access token (as specified in step 5) by using the client ID and certificate configured in step 3. Microsoft Entra ID returns a JSON Web Token (JWT) access token.
7. Your code sends the access token on a call to a service that supports Microsoft Entra authentication.

### Flow 2: User-Assigned Identities with Azure Virtual Machines

1. Azure Resource Manager receives a request to create a user-assigned managed identity.
2. Azure Resource Manager creates a service principal in Microsoft Entra ID for the user-assigned managed identity. The service principal is created in the Microsoft Entra tenant that's trusted by the subscription.
3. Azure Resource Manager receives a request to configure the user-assigned managed identity on a virtual machine and updates the Azure Instance Metadata Service identity endpoint with the user-assigned managed identity service principal client ID and certificate.
4. After the user-assigned managed identity is created, use the service principal information to grant the identity access to Azure resources. To call Azure Resource Manager, use role-based access control in Microsoft Entra ID to assign the appropriate role to the service principal of the user-assigned identity. To call Key Vault, grant your code access to the specific secret or key in Key Vault.
5. Your code that's running on the virtual machine can request a token from the Azure Instance Metadata Service identity endpoint, accessible only from within the virtual machine: `http://169.254.169.254/metadata/identity/oauth2/token`.
6. A call is made to Microsoft Entra ID to request an access token (as specified in step 5) by using the client ID and certificate configured in step 3. Microsoft Entra ID returns a JSON Web Token (JWT) access token.
7. Your code sends the access token on a call to a service that supports Microsoft Entra authentication.

</edukamu-collapse>
<br>

Managed identities simplify and secure the authentication flow to Azure services, making it an essential feature for building secure cloud solutions in Azure.

Complete the following exercise in order to consolidate your knowledge!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Key Vault and Managed Identities
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module3/enhancing-security-question-scroll-1.yaml" id="wxgwpm55czz56abj">
<br>

</edukamu-collapse>
<br>

We've now explored two out of three security features that make securing your Azure products simple and straightforward. After Azure Key Vault and managed identities, it's time to dig into Azure App Configuration!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1.png" alt="Edukamu-progress-in-a-module-image">
