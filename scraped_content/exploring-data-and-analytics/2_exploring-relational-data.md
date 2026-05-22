<edukamu-video content="/videos/devai-3-unit2-video.yaml"/>
<br>

## Exploring Relational Data

Welcome to the second unit!

Now that we understand all the core principles and characteristics of data, the backbone of any modern society, it's the perfect time to dig in a little deeper. In the second unit, we'll focus on relational and non-relational data.

Before getting down to the details, let's review the main characteristics and differences between the two, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Two Types of Data
</edukamu-collapse-hidden-title>

In the intricate world of data management, two primary approaches stand out: relational and non-relational databases. For the untrained eye, they might seem close to identical, but there are a few key differences. Let's review the main characteristics of each data type.

**Relational Data**:
* **Structure**: Organized into tables with predefined schema.
* **Schema**: Strict and fixed structure, enforced by the database.
* **Relationships**: Emphasizes relationships between tables using primary and foreign keys.
* **Query Language**: Utilizes SQL (Structured Query Language) for data manipulation.
* **Examples**: MySQL, PostgreSQL, Microsoft SQL Server.

**Non-relational Data**:
* **Structure**: Diverse structures, including key-value pairs, documents, columns, or graphs.
* **Schema**: Flexible, dynamic, and may vary within the dataset.
* **Relationships**: Relationships are often implicit, with no strict dependencies.
* **Query Language**: NoSQL databases use varied query languages, not necessarily SQL.
* **Examples**: MongoDB (document store), Cassandra (column-family store), Redis (key-value store).

### Relational Data: A Structured Foundation

Relational data is akin to a well-organized library in which information is neatly categorized into tables with a predefined structure known as a schema. These tables establish a robust framework, emphasizing relationships between data points through the use of primary and foreign keys. The adoption of SQL (Structured Query Language) provides a standardized means to interact with relational databases, facilitating seamless data manipulation.

Consider a scenario in which a company tracks customer orders and products in a structured manner. A relational database would organize this data into tables such as "Customers," "Orders," and "Products," with clear relationships defined by unique identifiers.

### Non-Relational Data: Embracing Diversity

Contrasting with the structured nature of relational databases, non-relational data offers a more flexible and adaptive environment. Picture a dynamic ecosystem in which data can take various forms, from key-value pairs to documents, columns, or intricate graphs.

Therefore, the schema in non-relational databases is not fixed; it evolves with the dataset, accommodating changes effortlessly. Unlike relational databases, relationships in the non-relational realm are often implicit, allowing for a more intuitive data organization.

Imagine a social media platform where user profiles are stored along with their preferences and interactions. In a non-relational database, this could be represented as a document, where each user profile contains unique attributes, and relationships are established organically.

</edukamu-collapse>
<br>


Understanding the distinction between relational and non-relational databases is fundamental for AI developers. Relational databases offer a structured and standardized approach suitable for scenarios demanding strict data relationships. On the other hand, non-relational databases provide the flexibility needed to adapt to ever-changing data landscapes.

Now that we’re familiar with the basics, it's time to start exploring relational data in more detail!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Understanding Relational Data
</edukamu-collapse-hidden-title>

In a relational database, you model collections of entities from the real world as tables. An entity can be anything for which you want to record information, typically important objects and events. For example, in a retail system example, you might create tables for customers, products, orders, and line items within an order. A table contains rows, and each row represents a single instance of an entity.

In the retail scenario, each row in the customer table contains the data for a single customer, each row in the product table defines a single product, each row in the order table represents an order made by a customer, and each row in the line-item table represents a product that was included in an order.

<edukamu-image url="/graphics/module2/relational-tables.png" alt="Example of a relational model, showing tables for customers, products, orders, and line items."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Relational tables are a format for structured data, and each row in a table has the same columns; though in some cases, not all columns need to have a value – for example, a customer table might include a **MiddleName** column; which can be empty (or *NULL*) for rows that represent customers with no middle name or whose middle name is unknown).

Each column stores data of a specific datatype. For example, an **Email** column in a **Customer** table would likely be defined to store character-based (text) data (which might be fixed or variable in length), a **Price** column in a **Product** table might be defined to store decimal numeric data, while a **Quantity** column in an **Order** table might be constrained to integer numeric values; and an **OrderDate** column in the same **Order** table would be defined to store date/time values.

The available datatypes that you can use when defining a table depend on the database system you are using; though there are standard datatypes defined by the American National Standards Institute (ANSI) that are supported by most database systems.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
When working with relational data, a process called *normalization* is of great importance. In essence, it all comes down to designing schemas.

If the term *schema* is still a bit blurry, don't worry! Check out the following instead, before moving on to normalization.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Schemas and Data
</edukamu-collapse-hidden-title>

In the context of data, a schema is a blueprint or structural definition that outlines the organization and format of a database. It serves as a framework for how data is stored, arranged, and accessed within a database system.

There are two main types of schemas:
1. **Physical Schema**: Describes how data is stored in the underlying storage system, including details such as data file format, indexing mechanisms, and partitioning.
2. **Logical Schema**: Describes the organization of data without detailing how it is physically stored. This includes defining tables, attributes, and relationships between tables.

The schema defines the structure of tables, specifying the fields or attributes each table contains, the data type of each attribute, and any constraints or rules that govern the relationships between tables. As such, choosing a schema is particularly crucial when handling relational data since it ensures data integrity and consistency.

</edukamu-collapse>
<br>


At this stage, please make sure that you understand the concept of data schemas. Once you do, feel free to move on! As mentioned before, normalization has to do with designing said schemas.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Relational Data and Normalization
</edukamu-collapse-hidden-title>

Normalization is a term used by database professionals for a schema design process that minimizes data duplication and enforces data integrity.

While there are many complex rules that define the process of refactoring data into various levels (or *forms*) of normalization, a simple definition for practical purposes is:
1. Separate each *entity* into its own table.
2. Separate each discrete *attribute* into its own column.
3. Uniquely identify each entity instance (row) using a *primary key*.
4. Use *foreign key* columns to link related entities.

To understand the core principles of normalization, suppose the following table represents a spreadsheet that a company uses to track its sales.

<edukamu-image url="/graphics/module2/unnormalized-data.png" alt="Order data in a single, un-normalized table."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Notice that the customer and product details are duplicated for each individual item sold and that the customer name, postal address, and the product name and price are combined in the same spreadsheet cells.

Now let's look at how normalization changes the way the data is stored.

<edukamu-image url="/graphics/module2/normalized-data.png" alt="Order data in a normalized tabular schema."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Each entity that is represented in the data (customer, product, sales order, and line item) is stored in its own table, and each discrete attribute of those entities is in its own column.

Recording each instance of an entity as a row in an entity-specific table removes duplication of data. For example, to change a customer's address, you need only modify the value in a single row.

The decomposition of attributes into individual columns ensures that each value is constrained to an appropriate data type – for example, product prices must be decimal values, while line item quantities must be integer numbers. Additionally, the creation of individual columns provides a useful level of granularity in the data for querying - for example, you can easily filter customers to those who live in a specific city.

Instances of each entity are uniquely identified by an ID or other key value, known as a *primary key*; and when one entity references another (for example, an order has an associated customer), the primary key of the related entity is stored as a *foreign key*.

You can look up the address of the customer (which is stored only once) for each record in the **Order** table by referencing the corresponding record in the **Customer** table. Typically, a relational database management system (RDBMS) can enforce referential integrity to ensure that a value entered into a foreign key field has an existing corresponding primary key in the related table – for example, preventing orders for non-existent customers.

In some cases, a key (primary or foreign) can be defined as a *composite* key based on a unique combination of multiple columns. For example, the **LineItem** table in the example above uses a unique combination of **OrderNo** and **ItemNo** to identify a line item from an individual order.

</edukamu-collapse>
<br>


In practice, normalization is a technique that helps us get the most out of our data. By designing an effective schema, companies around the world can be empowered, not confused or overwhelmed, by their data.


<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="elisa-logo">
### Scenario: Improving Data Processing 
</edukamu-collapse-hidden-title>

GreenThrive Networks’ old solution used SQL database to store raw data and the customer parameters in multiple tables. Data from tables was joined and filtered using views to create the actual billing lines and detailed information needed for the reporting. 

The new solution uses Azure Databricks that is an Apache Spark based data storage and intelligence platform. Databricks uses Delta Lake to store the data. Delta Lake is built on top of Storage Account and Parquet files and provides a very fast and cost-effective way to query the data. 

If we compare the speed to calculate the views, the calculation that in old solution used lasted over an hour, now takes less than 5 minutes. Mainly this is since Apache Spark enables massive scaling compute that is decoupled from the storage and Databricks uses storage that is highly optimized for large data operations. 

</edukamu-collapse>
<br>

In addition to tables, a relational database can contain other structures that help to optimize data organization, encapsulate programmatic actions, and improve the speed of access. Three of these structures are particularly useful and thus common: views, stored procedures, and indexes.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Views
</edukamu-collapse-hidden-title>

A view is a virtual table based on the results of a **SELECT** query. You can think of a view as a window on specified rows in one or more underlying tables. For example, you could create a view on the **Order** and **Customer** tables that retrieves order and customer data to provide a single object that makes it easy to determine delivery addresses for orders:

```
CREATE VIEW Deliveries
AS
SELECT o.OrderNo, o.OrderDate,
       c.FirstName, c.LastName, c.Address, c.City
FROM Order AS o JOIN Customer AS c
ON o.Customer = c.ID;
```

You can query the view and filter the data in much the same way as a table. The following query finds details of orders for customers who live in Seattle:

```
SELECT OrderNo, OrderDate, LastName, Address
FROM Deliveries
WHERE City = 'Seattle';
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Stored Procedures
</edukamu-collapse-hidden-title>

A stored procedure defines SQL statements that can be run on command. Stored procedures are used to encapsulate programmatic logic in a database for actions that applications need to perform when working with data.

You can define a stored procedure with parameters to create a flexible solution for common actions that might need to be applied to data based on a specific key or criteria. For example, the following stored procedure could be defined to change the name of a product based on the specified product ID.

```
CREATE PROCEDURE RenameProduct
        @ProductID INT,
        @NewName VARCHAR(20)
AS
UPDATE Product
SET Name = @NewName
WHERE ID = @ProductID;
```

When a product must be renamed, you can execute the stored procedure, passing the ID of the product and the new name to be assigned:

```
EXEC RenameProduct 201, 'Spanner';
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. Indexes
</edukamu-collapse-hidden-title>

An index helps you search for data in a table. Think of an index over a table like an index at the back of a book. A book index contains a sorted set of references, with the pages on which each reference occurs. When you want to find a reference to an item in the book, you look it up through the index. You can use the page numbers in the index to go directly to the correct pages in the book. Without an index, you might have to read through the entire book to find the references you're looking for.

When you create an index in a database, you specify a column from the table, and the index contains a copy of this data in a sorted order, with pointers to the corresponding rows in the table. When the user runs a query that specifies this column in the **WHERE** clause, the database management system can use this index to fetch the data more quickly than if it had to scan through the entire table row by row.

For example, you could use the following code to create an index on the **Name** column of the **Product** table:

```
CREATE INDEX idx_ProductName
ON Product(Name);
```

The index creates a tree-based structure that the database system's query optimizer can use to quickly find rows in the **Product** table based on a specified **Name**.

<edukamu-image url="/graphics/module2/index.png" alt="Visualization demonstrates an example of the index."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

For a table containing few rows, using the index is probably not any more efficient than simply reading the entire table and finding the rows requested by the query (in which case the query optimizer will ignore the index). However, when a table has many rows, indexes can dramatically improve the performance of queries.

You can create many indexes on a table. So, if you also wanted to find products based on price, creating another index on the **Price** column in the **Product** table might be useful. However, indexes aren't free. An index consumes storage space, and each time you insert, update, or delete data in a table, the indexes for that table must be maintained. This additional work can slow down insert, update, and delete operations. You must strike a balance between having indexes that speed up your queries versus the cost of performing other operations.

</edukamu-collapse>
<br>


Is relational data starting to make more sense? At all times, remember the fundamental difference between the two data types: Relational data is structured in tables with predefined schemas, emphasizing rigid relationships, while non-relational data offers flexibility, accommodating various structures and relationships in a dynamic environment.

All right, it's time to hone your relational-data-related skills with an exercise!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Relational Data
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/exploring-relational-data-question-scroll.yaml" id="yhe999u6z57e67lj">
<br>

</edukamu-collapse>
<br>


In the world of data, there's always more to explore. After getting to know the basic principles of relational data, it's time to spend a few moments exploring relational databases and the Azure services associated with them.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1.png" alt="Edukamu-progress-in-a-module-image">
