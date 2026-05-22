## Relational Databases in Azure

In a world filled with data, everything needs to be kept tidy and secure, stored in an orderly manner. Luckily, Microsoft Azure provides a powerful platform for managing and leveraging relational databases.

In the context of Azure, these databases play a pivotal role in supporting a wide range of applications, from simple data storage to complex business solutions. In essence, we're talking about structured and organized systems that excel at handling structured data and enforcing relationships between different data entities.

Databases are used by countless companies around the world, and their role is oftentimes fundamental. Take the case of handling customer information, for example: Customer profiles, including names, contact details, purchase history, and preferences, are stored in the database, which in turn enables personalized marketing, targeted promotions, and efficient customer support.

When talking about databases, Azure SQL is one of the most capable solutions available. Let's start by exploring its characteristics.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure SQL
</edukamu-collapse-hidden-title>

SQL stands for *Structured Query Language* and is used to communicate with a relational database. It's the standard language for relational database management systems. SQL statements are used to perform tasks such as update data in a database or retrieve data from a database. Some common relational database management systems that use SQL include Microsoft SQL Server, MySQL, PostgreSQL, MariaDB, and Oracle.

You can use SQL statements such as **SELECT**, **INSERT**, **UPDATE**, **DELETE**, **CREATE**, and **DROP** to accomplish almost everything that you need to do with a database. Although these SQL statements are part of the SQL standard, many database management systems also have their own additional proprietary extensions to handle the specifics of that database management system. These extensions provide functionality not covered by the SQL standard and include areas such as security management and programmability.

For example, Microsoft SQL Server, and Azure database services that are based on the SQL Server database engine, use Transact-SQL. This implementation includes proprietary extensions for writing stored procedures and triggers (application code that can be stored in the database) and managing user accounts. PostgreSQL and MySQL also have their own versions of these features.

Some popular dialects of SQL include:
* *Transact-SQL (T-SQL)*. This version of SQL is used by Microsoft SQL Server and Azure SQL services.
* *pgSQL*. This is the dialect, with extensions implemented in PostgreSQL.
* *PL/SQL*. This is the dialect used by Oracle. PL/SQL stands for Procedural Language/SQL.

Users who plan to work specifically with a single database system should learn the intricacies of their preferred SQL dialect and platform.

**Note**: The SQL code examples in this course are based on the Transact-SQL dialect, unless otherwise indicated. The syntax for other dialects is generally similar but may vary in some details.

</edukamu-collapse>
<br>

Next, take some time to study the terminology described below. Understanding the concepts will help you grasp the concepts behind the Azure SQL system as well.

In order to interact with relational databases, you'll need something called SQL statements. They are grouped into three main logical groups:
* Data Definition Language (DDL)
* Data Control Language (DCL)
* Data Manipulation Language (DML)

Let's explore each statement type in more detail, since choosing the correct ones is important for handling data effectively and securely.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. DDL Statements
</edukamu-collapse-hidden-title>

You use DDL statements to create, modify, and remove tables and other objects in a database (table, stored procedures, views, and so on).

The most common DDL statements are:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="30%">
Statement
</edukamu-table-header>
<edukamu-table-header width="70%">
Description
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
CREATE
</edukamu-table-cell>
<edukamu-table-cell >
Create a new object in the database, such as a table or a view.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
ALTER
</edukamu-table-cell>
<edukamu-table-cell >
Modify the structure of an object. For instance, altering a table to add a new column.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DROP
</edukamu-table-cell>
<edukamu-table-cell >
Remove an object from the database.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
RENAME
</edukamu-table-cell>
<edukamu-table-cell >
Rename an existing object.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

**Warning**: The DROP statement is very powerful. When you drop a table, all the rows in that table are lost. Unless you have a backup, you won't be able to retrieve this data.

The following example creates a new database table. The items between the parentheses specify the details of each column, including the name, the data type, whether the column must always contain a value (NOT NULL), and whether the data in the column is used to uniquely identify a row (PRIMARY KEY). Each table should have a primary key, although SQL doesn't enforce this rule.
 
**Note**: Columns marked as NOT NULL are referred to as mandatory columns. If you omit the NOT NULL clause, you can create rows that don't contain a value in the column. An empty column in a row is said to have a NULL value.

```
CREATE TABLE Product
(
    ID INT PRIMARY KEY,
    Name VARCHAR(20) NOT NULL,
    Price DECIMAL NULL
);
```

Notice that the datatypes available for columns in a table will vary between database management systems. However, most database management systems support numeric types such as INT (an integer, or whole number), DECIMAL (a decimal number), and string types such as VARCHAR (*VARCHAR* stands for variable length character data). For more information, see the documentation for your selected database management system.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. DCL Statements
</edukamu-collapse-hidden-title>

Database administrators generally use DCL statements to manage access to objects in a database by granting, denying, or revoking permissions to specific users or groups.

The three main DCL statements are:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="30%">
Statement
</edukamu-table-header>
<edukamu-table-header width="70%">
Description
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
GRANT
</edukamu-table-cell>
<edukamu-table-cell >
Grant permission to perform specific actions
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DENY
</edukamu-table-cell>
<edukamu-table-cell >
Deny permission to perform specific actions
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
REVOKE
</edukamu-table-cell>
<edukamu-table-cell >
Remove a previously granted permission
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


For example, the following GRANT statement permits a user named user1 to read, insert, and modify data in the Product table.

```
GRANT SELECT, INSERT, UPDATE
ON Product
TO user1;
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. DML Statements
</edukamu-collapse-hidden-title>

You use DML statements to manipulate the rows in tables. These statements enable you to retrieve (query) data, insert new rows, or modify existing rows. You can also delete rows if you don't need them anymore.

The four main DML statements are:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="30%">
Statement
</edukamu-table-header>
<edukamu-table-header width="70%">
Description
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
SELECT
</edukamu-table-cell>
<edukamu-table-cell >
Read rows from a table
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
INSERT
</edukamu-table-cell>
<edukamu-table-cell >
Insert new rows into a table
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
UPDATE
</edukamu-table-cell>
<edukamu-table-cell >
Modify data in existing rows
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
DELETE
</edukamu-table-cell>
<edukamu-table-cell >
Delete existing rows
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

The basic form of an INSERT statement will insert one row at a time. By default, the SELECT, UPDATE, and DELETE statements are applied to every row in a table. You usually apply a WHERE clause with these statements to specify criteria; only rows that match these criteria will be selected, updated, or deleted.

**Warning**: SQL doesn't provide are you sure? prompts, so be careful when using DELETE or UPDATE without a WHERE clause because you can lose or modify a lot of data.

The following code is an example of a SQL statement that selects all columns (indicated by *) from the **Customer** table where the **City** column value is "Seattle":

```
SELECT *
FROM Customer
WHERE City = 'Seattle';
```

To retrieve only a specific subset of columns from the table, you list them in the SELECT clause, like this:

```
SELECT FirstName, LastName, Address, City
FROM Customer
WHERE City = 'Seattle';
```

If a query returns many rows, they don't necessarily appear in any specific sequence. If you want to sort the data, you can add an **ORDER BY** clause. The data will be sorted by the specified column:

```
SELECT FirstName, LastName, Address, City
FROM Customer
WHERE City = 'Seattle'
ORDER BY LastName;
```

You can also run SELECT statements that retrieve data from multiple tables using a **JOIN** clause. Joins indicate how the rows in one table are connected with rows in the other to determine what data to return. A typical join condition matches a foreign key from one table and its associated primary key in the other table.

The following query shows an example that joins **Customer** and **Order** tables. The query makes use of table *aliases* to abbreviate the table names when specifying which columns to retrieve in the **SELECT** clause and which columns to match in the **JOIN** clause.

```
SELECT o.OrderNo, o.OrderDate, c.Address, c.City
FROM Order AS o
JOIN Customer AS c
ON o.Customer = c.ID
```

The next example shows how to modify an existing row using SQL. It changes the value of the **Address** column in the **Customer** table for rows that have the value 1 in the **ID** column. All other rows are left unchanged:

```
UPDATE Customer
SET Address = '123 High St.'
WHERE ID = 1;
```

**Warning**: If you omit the WHERE clause, an UPDATE statement will modify every row in the table.

Use the **DELETE** statement to remove rows. You specify the table to delete from, and a **WHERE** clause that identifies the rows to be deleted:

```
DELETE FROM Product
WHERE ID = 162;
```

**Warning**: If you omit the WHERE clause, a DELETE statement will remove every row from the table.

The **INSERT** statement takes a slightly different form. You specify a table and columns in an **INTO** clause, and a list of values to be stored in these columns. Standard SQL only supports inserting one row at a time, as shown in the following example. Some dialects allow you to specify multiple **VALUES** clauses to add several rows at a time:

```
INSERT INTO Product(ID, Name, Price)
VALUES (99, 'Drill', 4.99);
```

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
The technology behind SQL was originally standardized by the American National Standards Institute (ANSI) in 1986 and by the International Organization for Standardization (ISO) in 1987. Since then, the standard has been extended several times as relational database vendors have added new features to their systems.

Nowadays, SQL is used around the world to empower businesses and promoting inventions across numerous fields.

Next, let's explore what can be done with Azure's SQL services.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure SQL Capabilities
</edukamu-collapse-hidden-title>

Azure SQL is a collective term for a family of Microsoft SQL Server based database services in Azure. Specific Azure SQL services include:
* **SQL Server on Azure Virtual Machines (VMs)** - A virtual machine running in Azure with an installation of SQL Server. The use of a VM makes this option an infrastructure-as-a-service (IaaS) solution that virtualizes hardware infrastructure for compute, storage, and networking in Azure; making it a great option for "lift and shift" migration of existing on-premises SQL Server installations to the cloud.
* **Azure SQL Managed Instance** - A platform-as-a-service (PaaS) option that provides near-100% compatibility with on-premises SQL Server instances while abstracting the underlying hardware and operating system. The service includes automated software update management, backups, and other maintenance tasks, reducing the administrative burden of supporting a database server instance.
* **Azure SQL Database** - A fully managed, highly scalable PaaS database service that is designed for the cloud. This service includes the core database-level capabilities of on-premises SQL Server, and is a good option when you need to create a new application in the cloud.
* **Azure SQL Edge** - A SQL engine that is optimized for Internet-of-things (IoT) scenarios that need to work with streaming time-series data.

### Comparing Azure SQL Services

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="25%">
<!-- SQL Server on Azure VMs -->
</edukamu-table-header>
<edukamu-table-header width="25%">
SQL Server on Azure VMs
</edukamu-table-header>
<edukamu-table-header width="25%">
Azure SQL Managed Instance
</edukamu-table-header>
<edukamu-table-header width="25%">
Azure SQL Database
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Type of cloud service
</edukamu-table-cell>
<edukamu-table-cell >
IaaS
</edukamu-table-cell>
<edukamu-table-cell>
PaaS
</edukamu-table-cell>
<edukamu-table-cell >
PaaS
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
SQL Server compatibility
</edukamu-table-cell>
<edukamu-table-cell >
Fully compatible with on-premises physical and virtualized installations. Applications and databases can easily be "lift and shift" migrated without change.
</edukamu-table-cell>
<edukamu-table-cell>
Near-100% compatibility with SQL Server. Most on-premises databases can be migrated with minimal code changes by using the [Azure Database Migration service](https://learn.microsoft.com/en-us/azure/dms)(target="_blank").
</edukamu-table-cell>
<edukamu-table-cell >
Supports most core database-level capabilities of SQL Server. Some features depended on by an on-premises application may not be available.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Architecture
</edukamu-table-cell>
<edukamu-table-cell >
SQL Server instances are installed in a virtual machine. Each instance can support multiple databases.
</edukamu-table-cell>
<edukamu-table-cell>
Each managed instance can support multiple databases. Additionally, *instance pools* can be used to share resources efficiently across smaller instances.
</edukamu-table-cell>
<edukamu-table-cell >
You can provision a *single database* in a dedicated, managed (logical) server; or you can use an *elastic pool* to share resources across multiple databases and take advantage of on-demand scalability.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Availability
</edukamu-table-cell>
<edukamu-table-cell >
99.99%
</edukamu-table-cell>
<edukamu-table-cell>
99.99%
</edukamu-table-cell>
<edukamu-table-cell >
99.995%
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Management
</edukamu-table-cell>
<edukamu-table-cell >
You must manage all aspects of the server, including operating system and SQL Server updates, configuration, backups, and other maintenance tasks.
</edukamu-table-cell>
<edukamu-table-cell>
Fully automated updates, backups, and recovery.
</edukamu-table-cell>
<edukamu-table-cell >
Fully automated updates, backups, and recovery.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Use cases
</edukamu-table-cell>
<edukamu-table-cell >
Use this option when you need to migrate or extend an on-premises SQL Server solution and retain full control over all aspects of server and database configuration.
</edukamu-table-cell>
<edukamu-table-cell>
Use this option for most cloud migration scenarios, particularly when you need minimal changes to existing applications.
</edukamu-table-cell>
<edukamu-table-cell >
Use this option for new cloud solutions, or to migrate applications that have minimal instance-level dependencies.
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

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### SQL Server and Azure Virtual Machines
</edukamu-collapse-hidden-title>

SQL Server on Virtual Machines enables you to use full versions of SQL Server in the Cloud without having to manage any on-premises hardware. This is an example of the IaaS approach.

SQL Server running on an Azure virtual machine effectively replicates the database running on real on-premises hardware. Migrating from the system running on-premises to an Azure virtual machine is no different than moving the databases from one on-premises server to another.

This approach is suitable for migrations and applications requiring access to operating system features that might be unsupported at the PaaS level. SQL virtual machines are *lift-and-shift* ready for existing applications that require fast migration to the cloud with minimal changes. You can also use SQL Server on Azure VMs to extend existing on-premises applications to the cloud in hybrid deployments.

**Note**: A *hybrid deployment* is a system where part of the operation runs on-premises, and part in the cloud. Your database might be part of a larger system that runs on-premises, although the database elements might be hosted in the cloud.

You can use SQL Server in a virtual machine to develop and test traditional SQL Server applications. With a virtual machine, you have the full administrative rights over the DBMS and operating system. It's a perfect choice when an organization already has IT resources available to maintain the virtual machines.

These capabilities enable you to:
* Create rapid development and test scenarios when you don't want to buy on-premises non-production SQL Server hardware.
* Become lift-and-shift ready for existing applications that require fast migration to the cloud with minimal changes or no changes.
* Scale up the platform on which SQL Server is running, by allocating more memory, CPU power, and disk space to the virtual machine. You can quickly resize an Azure virtual machine without the requirement that you reinstall the software that is running on it.

</edukamu-collapse>
<br>


Running SQL Server on virtual machines allows you to meet unique and diverse business needs through a combination of on-premises and cloud-hosted deployments, while using the same set of server products, development tools, and expertise across these environments.

It's not always easy for businesses to switch their DBMS to a fully managed service. There may be specific requirements that must be satisfied in order to migrate to a managed service that requires making changes to the database and the applications that use it. For this reason, using virtual machines can offer a solution, but using them doesn't eliminate the need to administer your DBMS as carefully as you would on-premises.

After the following exercise, we'll explore the different Azure SQL capabilities a little further.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Introduction to Relational Databases
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module2/relational-databases-in-azure-text-poll.yaml" id="u34933j7zhq3yv5e"/>
<br>
<edukamu-text-poll url="/exercises/module2/relational-databases-in-azure-text-poll-2.yaml" id="l96kg4480td31ou3"/>
<br>
<edukamu-text-poll url="/exercises/module2/relational-databases-in-azure-text-poll-3.yaml" id="dmh4565i2927mma5"/>
<br>
<edukamu-text-poll url="/exercises/module2/relational-databases-in-azure-text-poll-4.yaml" id="qx90011983wv8du5"/>
<br>
<edukamu-text-poll url="/exercises/module2/relational-databases-in-azure-text-poll-5.yaml" id="b896m305ed22gg38"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/2/relational-databases-in-azure?question=u34933j7zhq3yv5e">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


On the next page, we'll see how Azure SQL services operate in the cloud, which makes even the largest databases more efficient and thus a lot easier to handle.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
