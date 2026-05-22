## Adopting Cloud Services

Microsoft Azure is full of cutting-edge services that facilitate smooth, efficient operations for companies of all sizes and specializations. But what about those who are not used to working online – let alone relying on cloud services?

Microsoft encourages everyone to embrace the possibilities of the latest AI and cloud services, and as such it offers relational database solutions for those seeking to transition from on-premises environments to the cloud.

Azure SQL Database Managed Instance is a tool aimed at exactly such purposes. After checking it out, we'll shortly review Azure SQL Database as well.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure SQL Database Managed Instance
</edukamu-collapse-hidden-title>

Azure SQL Managed instance effectively runs a fully controllable instance of SQL Server in the cloud. You can install multiple databases on the same instance. You have complete control over this instance, much as you would for an on-premises server. SQL Managed Instance automates backups, software patching, database monitoring, and other general tasks, but you have full control over security and resource allocation for your databases.

Managed instances depend on other Azure services such as Azure Storage for backups, Azure Event Hubs for telemetry, Microsoft Entra ID for authentication, Azure Key Vault for Transparent Data Encryption (TDE) and a couple of Azure platform services that provide security and supportability features. The managed instances make connections to these services.

All communications are encrypted and signed using certificates. To check the trustworthiness of communicating parties, managed instances constantly verify these certificates through certificate revocation lists. If the certificates are revoked, the managed instance closes the connections to protect the data.

### Use Cases

Consider Azure SQL Managed Instance if you want to lift-and-shift an on-premises SQL Server instance and all its databases to the cloud, without incurring the management overhead of running SQL Server on a virtual machine.

Azure SQL Managed Instance provides features not available in Azure SQL Database (discussed below). If your system uses features such as linked servers, Service Broker (a message processing system that can be used to distribute work across servers), or Database Mail (which enables your database to send email messages to users), then you should use managed instance.

To check compatibility with an existing on-premises system, you can install <br>[Data Migration Assistant (DMA)](https://www.microsoft.com/download/details.aspx?id=53595)(target="_blank"). This tool analyzes your databases on SQL Server and reports any issues that could block migration to a managed instance.

### Business Benefits

Azure SQL Managed Instance enables a system administrator to spend less time on administrative tasks because the service either performs them for you or greatly simplifies those tasks. Automated tasks include operating system and database management system software installation and patching, dynamic instance resizing and configuration, backups, database replication (including system databases), high availability configuration, and configuration of health and performance monitoring data streams.

Azure SQL Managed Instance has near 100% compatibility with SQL Server Enterprise Edition, running on-premises.

Azure SQL Managed Instance supports SQL Server Database engine logins and logins integrated with Microsoft Entra ID. SQL Server Database engine logins include a username and a password. You must enter your credentials each time you connect to the server. Microsoft Entra logins use the credentials associated with your current computer sign-in, and you don't need to provide them each time you connect to the server.

</edukamu-collapse>
<br>


Azure SQL Database Managed Instance has its perks and benefits in numerous situations, but it's not the only option out there. Actually, Microsoft Azure has tools for creating and operating entire database servers on the cloud.

Azure SQL Database is the most prominent option whenever databases need to be managed via independent servers hosted via Microsoft's cloud services.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure SQL Database
</edukamu-collapse-hidden-title>

Azure SQL Database is a PaaS offering from Microsoft. You create a managed database server in the cloud, and then deploy your databases on this server.

**Note**: A SQL Database server is a logical construct that acts as a central administrative point for multiple single or pooled databases, logins, firewall rules, auditing rules, threat detection policies, and failover groups.

Azure SQL Database is available as a Single Database or an Elastic Pool.

### 1. Single Database

This option enables you to quickly set up and run a single SQL Server database. You create and run a database server in the cloud, and you access your database through this server. Microsoft manages the server, so all you have to do is configure the database, create your tables, and populate them with your data.

You can scale the database if you need more storage space, memory, or processing power. By default, resources are pre-allocated, and you're charged per hour for the resources you've requested. You can also specify a serverless configuration. In this configuration, Microsoft creates its own server, which might be shared by databases belonging to other Azure subscribers. Microsoft ensures the privacy of your database. Your database automatically scales and resources are allocated or deallocated as required.

### 2. Elastic Pool

This option is similar to Single Database, except that by default multiple databases can share the same resources, such as memory, data storage space, and processing power through multiple-tenancy. The resources are referred to as a pool. You create the pool, and only your databases can use the pool. This model is useful if you have databases with resource requirements that vary over time, and can help you to reduce costs.

For example, your payroll database might require plenty of CPU power at the end of each month as you handle payroll processing, but at other times the database might become much less active. You might have another database that is used for running reports. This database might become active for several days in the middle of the month as management reports are generated, but with a lighter load at other times. Elastic Pool enables you to use the resources available in the pool, and then release the resources once processing has completed.

### Use Cases

Azure SQL Database gives you the best option for low cost with minimal administration. It isn't fully compatible with on-premises SQL Server installations. It's often used in new cloud projects where the application design can accommodate any required changes to your applications.

Azure SQL Database is often used for:
* Modern cloud applications that need to use the latest stable SQL Server features.
* Applications that require high availability.
* Systems with a variable load that need the database server to scale up and down quickly.

**Note**: You can use the Data Migration Assistant to detect compatibility issues with your databases that can impact database functionality in Azure SQL Database.


### Business Benefits

Azure SQL Database automatically updates and patches the SQL Server software to ensure that you're always running the latest and most secure version of the service.

The scalability features of Azure SQL Database ensure that you can increase the resources available to store and process data without having to perform a costly manual upgrade.

The service provides high availability guarantees, to ensure that your databases are available at least 99.995% of the time. Azure SQL Database supports point-in-time restore, enabling you to recover a database to the state it was in at any point in the past. Databases can be replicated to different regions to provide more resiliency and disaster recovery.

Advanced threat protection provides advanced security capabilities, such as vulnerability assessments, to help detect and remediate potential security problems with your databases. Threat protection also detects anomalous activities that indicate unusual and potentially harmful attempts to access or exploit your database. It continuously monitors your database for suspicious activities, and provides immediate security alerts on potential vulnerabilities, SQL injection attacks, and anomalous database access patterns. Threat detection alerts provide details of the suspicious activity, and recommend action on how to investigate and mitigate the threat.

Auditing tracks database events and writes them to an audit log in your Azure storage account. Auditing can help you maintain regulatory compliance, understand database activity, and gain insight into discrepancies and anomalies that might indicate business concerns or suspected security violations.

SQL Database helps secure your data by providing encryption that protects data that is stored in the database (*at rest*) and while it is being transferred across the network (*in motion*).

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Even though the Azure SQL services described above work well in many cases, be it facilitating transitions from on-premises business models to the cloud or hosting entire database servers, they might not be the best option in every scenario, such as when using open-source services.

Luckily, Microsoft Azure is highly compatible with open-source software and services as well, which we'll briefly look at next.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Services for Open-source Databases
</edukamu-collapse-hidden-title>

In addition to Azure SQL services, Azure data services are available for other popular relational database systems, including MySQL, MariaDB, and PostgreSQL. The primary reason for these services is to enable organizations that use them in on-premises apps to move to Azure quickly, without making significant changes to their applications.

MySQL, MariaDB, and PostgreSQL are relational database management systems that are tailored for different specializations.

**Note**: If you are not familiar with the services described above, there's no need to worry. You can still review the materials below, but we won't be using the three during this course.


### Azure Database for MySQL

Azure Database for MySQL is a PaaS implementation of MySQL in the Azure cloud, based on the MySQL Community Edition.

The Azure Database for MySQL service includes high availability at no additional cost, and scalability as required. You only pay for what you use. Automatic backups are provided, with point-in-time restore.

The server provides connection security to enforce firewall rules and, optionally, require SSL connections. Many server parameters enable you to configure server settings such as lock modes, maximum number of connections, and timeouts.

Azure Database for MySQL provides a global database system that scales up to large databases without the need to manage hardware, network components, virtual servers, software patches, and other underlying components.

Certain operations aren't available with Azure Database for MySQL. These functions are primarily concerned with security and administration. Azure manages these aspects of the database server itself.


### Azure Database for MariaDB

Azure Database for MariaDB is an implementation of the MariaDB database management system adapted to run in Azure. It's based on the MariaDB Community Edition.

The database is fully managed and controlled by Azure. Once you've provisioned the service and transferred your data, the system requires almost no additional administration.


### Azure Database for PostgreSQL

If you prefer PostgreSQL, you can choose Azure Database for PostgreSQL to run a PaaS implementation of PostgreSQL in the Azure Cloud. This service provides the same availability, performance, scaling, security, and administrative benefits as the MySQL service.

Some features of on-premises PostgreSQL databases aren't available in Azure Database for PostgreSQL. These features are mostly concerned with the extensions that users can add to a database to perform specialized tasks, such as writing stored procedures in various programming languages (other than pgsql, which is available), and interacting directly with the operating system. A core set of the most frequently used extensions is supported, and the list of available extensions is under continuous review.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Exploring Azure Relational Database Services
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

If you have an active Azure subscription, you can explore the services we just covered over at Microsoft’s Learn platform.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/explore-provision-deploy-relational-database-offerings-azure/4-exercise-provision-relational-azure-data-services?pivots=azuresql">Practice: Relational Databases in Azure (Microsoft Learn)</edukamu-button>
<br>

</edukamu-collapse>
<br>


As even the most traditional companies around the world slowly but steadily move from on-premises locations to the digital world, understanding databases is becoming more and more crucial. Relational databases serve as the backbone for applications, offering structured, organized, and secure data management.

As we move forward in the course, the knowledge gained in this chapter lays a solid foundation for understanding advanced database concepts, so make sure to take your time when completing the exercise below!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Additional Database Services
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/adopting-cloud-services-question-scroll.yaml" id="8s91fg8b8283i23d">
<br>

</edukamu-collapse>
<br>


After such a compelling introduction to relational data, it might be easy to forget that other types of data also exist. Non-relational data is up next, and it's just as important a topic as the one we've just concluded!

Do take a moment to relax before continuing. It's easy to get mixed up with the data types, so give your brain some time to adjust.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
