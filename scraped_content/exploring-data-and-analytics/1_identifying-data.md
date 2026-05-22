<edukamu-video content="/videos/devai-3-unit1-video.yaml"/>
<br>

## Identifying Data

During the recent decades, our lives have become more and more reliant on data. Data is important, fundamental, and sometimes even dangerous – data is quite literally *everything*! But have you ever stopped to wonder what data actually *is*? Why are we willing to spend billions on protecting it?

At its core, data is not merely a collection of facts and figures; it's the raw material from which insights are extracted, decisions are informed, and innovations are born. Data encompasses a rich tapestry of information, spanning from traditional databases to cutting-edge streams of real-time data, and it comes in many formats, such as structured, semi-structured, and unstructured.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Why is Data so Important?
</edukamu-collapse-hidden-title>

In the digital age, data is the heartbeat of every organization. It fuels business intelligence, empowers artificial intelligence, and guides strategic decision-making. The ability to harness and analyze data has become a competitive advantage, driving efficiency, innovation, and growth.

In our daily lives, data is woven seamlessly into countless scenarios, shaping experiences and driving decisions. Consider the following examples.

### 1. E-Commerce Insights

Imagine a bustling e-commerce platform on which every click, purchase, and customer interaction generates a wealth of data. From user preferences and browsing history to transaction details, this data fuels personalized recommendations, improves user experiences, and optimizes supply chain logistics, creating a dynamic and responsive marketplace.

### 2. Healthcare Analytics

In the world of healthcare, data takes center stage in patient care and medical research. Electronic health records (EHRs), diagnostic data, and treatment outcomes are meticulously analyzed to enhance diagnostic accuracy, personalize treatment plans, and contribute to medical breakthroughs that can transform the landscape of healthcare delivery.

### 3. Smart Cities and IoT

Picture a modern city in which data makes urban life effortless for everyone. IoT devices embedded in streetlights, traffic signals, and public transportation continuously collect and transmit data. This information is harnessed to optimize traffic flow, reduce energy consumption, and enhance public safety – transforming cities into intelligent, responsive ecosystems.

### 4. Social Media Engagement

On the vast landscape of social media, data takes the form of user interactions, content preferences, and engagement metrics which are all closely monitored – for better or worse. Social platforms leverage this data to deliver personalized content, target advertisements effectively, and analyze trends that shape the digital conversations of millions.

### 5. Financial Decision-Making

In the financial sector, data is the cornerstone of informed decision-making. Market trends, customer transactions, and risk analysis are meticulously examined to guide investment strategies, detect fraudulent activities, and ensure the stability of financial ecosystems.

</edukamu-collapse>
<br>


As we advance on this course, keep these examples in mind, as they vividly illustrate the transformative power of data in our interconnected world.

On this course, we’ll also learn how raw data becomes actionable intelligence, and actually we’re about to begin. The first step is identifying data – let’s get started!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### How to Classify Data?
</edukamu-collapse-hidden-title>

Data is a collection of facts such as numbers, descriptions, and observations used to record information. Data structures in which this data is organized often represents entities that are important to an organization (such as customers, products, sales orders, and so on). Each entity typically has one or more attributes, or characteristics (for example, a customer might have a name, an address, a phone number, and so on).

You can classify data as structured, semi-structured, or unstructured.

### 1. Structured Data

Structured data is data that adheres to a fixed schema, so all of the data has the same fields or properties. Most commonly, the schema for structured data entities is tabular - in other words, the data is represented in one or more tables that consist of rows to represent each instance of a data entity, and columns to represent attributes of the entity. For example, the following image shows tabular data representations for Customer and Product entities.

<edukamu-image url="/graphics/module1/2-tabular-diagram.png" alt="Image showing how structured data is represented in tables."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Structured data is often stored in a database in which multiple tables can reference one another by using key values in a relational model, which we'll explore in more depth later.

### 2. Semi-structured Data

Semi-structured data is information that has some structure, but which allows for some variation between entity instances. For example, while most customers may have an email address, some might have multiple email addresses, and some might have none at all.

One common format for semi-structured data is *JavaScript Object Notation* (JSON). The example below shows a pair of JSON documents that represent customer information. Each customer document includes address and contact information, but the specific fields vary between customers.

<edukamu-image url="/graphics/module1/json.png" alt="Image demonstrated the code relater to Customer 1 and Customer 2."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

**Note**: JSON is just one of many ways in which semi-structured data can be represented. The point here is not to provide a detailed examination of JSON syntax, but rather to illustrate the flexible nature of semi-structured data representations.

### 3. Unstructured Data

Not all data is structured or even semi-structured. For example, documents, images, audio and video data, and binary files might not have a specific structure. This kind of data is referred to as *unstructured* data.


<edukamu-image url="/graphics/module1/2-unstructured-data.png" alt="Image showing unstructured data in documents."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

### Data Stores

Organizations typically store data in structured, semi-structured, or unstructured format to record details of entities (for example, customers and products), specific events (such as sales transactions), or other information in documents, images, and other formats. The stored data can then be retrieved for analysis and reporting later.

There are two broad categories of data store in common use:
* File stores
* Databases

We'll explore both of these types of data store in subsequent topics.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### How to Store Data?
</edukamu-collapse-hidden-title>

The ability to store data in files is a core element of any computing system. Files can be stored in local file systems on the hard disk of your personal computer, and on removable media such as USB drives; but in most organizations, important data files are stored centrally in some kind of shared file storage system. Increasingly, that central storage location is hosted in the cloud, enabling cost-effective, secure, and reliable storage for large volumes of data.

The specific file format used to store data depends on a number of factors, including:
* The type of data being stored (structured, semi-structured, or unstructured).
* The applications and services that will need to read, write, and process the data.
* The need for the data files to be readable by humans, or optimized for efficient storage and processing.

Let’s explore a few common file formats.

### 1. Delimited Text Files

Data is often stored in plain text format with specific field delimiters and row terminators. The most common format for delimited data is comma-separated values (CSV) in which fields are separated by commas, and rows are terminated by a carriage return / new line. Optionally, the first line may include the field names. Other common formats include tab-separated values (TSV) and space-delimited (in which tabs or spaces are used to separate fields), and fixed-width data in which each field is allocated a fixed number of characters. Delimited text is a good choice for structured data that needs to be accessed by a wide range of applications and services in a human-readable format.

The following example shows customer data in comma-delimited format

>FirstName,LastName,Email<br>
>Joe,Jones,joe@litware.com<br>
>Samir,Nadoy,samir@northwind.com<br>


### 2. JavaScript Object Notation (JSON)

JSON is a ubiquitous format in which a hierarchical document schema is used to define data entities (objects) that have multiple attributes. Each attribute might be an object (or a collection of objects); making JSON a flexible format that's good for both structured and semi-structured data.

The following example shows a JSON document containing a collection of customers. Each customer has three attributes (*firstName*, *lastName*, and *contact*), and the *contact* attribute contains a collection of objects that represent one or more contact methods (email or phone). Note that objects are enclosed in braces ({..}) and collections are enclosed in square brackets ([..]). Attributes are represented by *name* : *value* pairs and separated by commas (,).

```
{
  "customers":
  [
    {
      "firstName": "Joe",
      "lastName": "Jones",
      "contact":
      [
        {
          "type": "home",
          "number": "555 123-1234"
        },
        {
          "type": "email",
          "address": "joe@litware.com"
        }
      ]
    },
    {
      "firstName": "Samir",
      "lastName": "Nadoy",
      "contact":
      [
        {
          "type": "email",
          "address": "samir@northwind.com"
        }
      ]
    }
  ]
}
```

### 3. Extensible Markup Language (XML)

XML is a human-readable data format that was popular in the 1990s and 2000s. It's largely been superseded by the less verbose JSON format, but there are still some systems that use XML to represent data. XML uses tags enclosed in angle-brackets (<../>) to define *elements* and *attributes*, as shown in this example:

```xml
<Customers>
  <Customer name="Joe" lastName="Jones">
    <ContactDetails>
      <Contact type="home" number="555 123-1234"/>
      <Contact type="email" address="joe@litware.com"/>
    </ContactDetails>
  </Customer>
  <Customer name="Samir" lastName="Nadoy">
    <ContactDetails>
      <Contact type="email" address="samir@northwind.com"/>
    </ContactDetails>
  </Customer>
</Customers>
```

### 4. Binary Large Object (BLOB)

Ultimately, all files are stored as binary data (1's and 0's), but in the human-readable formats discussed above, the bytes of binary data are mapped to printable characters (typically through a character encoding scheme such as ASCII or Unicode).

Some file formats however, particularly for unstructured data, store the data as raw binary that must be interpreted by applications and rendered. Common types of data stored as binary include images, video, audio, and application-specific documents.

When working with data like this, data professionals often refer to the data files as BLOBs (Binary Large Objects).

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Optimized File Formats
</edukamu-collapse-hidden-title>

While human-readable formats for structured and semi-structured data can be useful, they're typically not optimized for storage space or processing. Over time, some specialized file formats that enable compression, indexing, and efficient storage and processing have been developed.

Some common optimized file formats you might see include *Avro*, *ORC*, and *Parquet*:
* *Avro* is a row-based format. It was created by Apache. Each record contains a header that describes the structure of the data in the record. This header is stored as JSON. The data is stored as binary information. An application uses the information in the header to parse the binary data and extract the fields it contains. Avro is a good format for compressing data and minimizing storage and network bandwidth requirements.
* *ORC* (Optimized Row Columnar format) organizes data into columns rather than rows. It was developed by HortonWorks for optimizing read and write operations in Apache Hive (Hive is a data warehouse system that supports fast data summarization and querying over large datasets). An ORC file contains *stripes* of data. Each stripe holds the data for a column or set of columns. A stripe contains an index into the rows in the stripe, the data for each row, and a footer that holds statistical information (count, sum, max, min, and so on) for each column.
* *Parquet* is another columnar data format. It was created by Cloudera and Twitter. A Parquet file contains row groups. Data for each column is stored together in the same row group. Each row group contains one or more chunks of data. A Parquet file includes metadata that describes the set of rows found in each chunk. An application can use this metadata to quickly locate the correct chunk for a given set of rows, and retrieve the data in the specified columns for these rows. Parquet specializes in storing and processing nested data types efficiently. It supports very efficient compression and encoding schemes.

</edukamu-collapse>
<br>

<edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="elisa-logo">
### Use Scenario: Streamlining Data Solutions  
</edukamu-collapse-hidden-title>

GreenThrive Networks is a pioneering provider of large-scale, gardening-focused digital solutions, serving millions of devices across thousands of customers to enhance and simplify their horticultural experiences. GreenThrive Networks has developed a custom billing system to bill their customers. GreenThrive Networks uses raw data that comes directly from IoT system. 

Raw billing data comes in a CSV-formatted file. With many customers and many different meters in raw data, the amount of data is huge. Data needs to be processed with customer specific configuration parameters to count the actual price. There are rules about consolidating some of the products in the single line in the bill. Some customers have agreed discounts. 

The old solution was built on Azure SQL and bit by bit growing from original small-scale usage to current size. The solution was not performing well and was very costly as SQL database had to be large to make views run in acceptable time. Data load from CSV files to billing systems took over 4 hours. 

GreenThrive Networks decided to refactor the solution to use more powerful tools in Azure. They wanted to achieve streamlined configuration for billing and IoT-system configurations. At the end they decided to centralize configuration data to Azure CosmosDB. NoSQL-based backend provides flexibility and scalability as their IoT system grows and develops at the same time when the data is used in various scenarios. 

Billing line data was loaded, transformed, and stored with Azure Databricks. Databricks provides advanced capabilities to transform or manipulate data. This is preparation for the future, when the service develops and needs more advanced features for data handling. Databricks saves the data in Azure storage accounts, using parquet files as the format. 

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
You might be beginning to realize that there’s a lot more to know about data than what meets the eye. During this course, we’ll explore data from various angles – without forgetting Microsoft Azure, the go-to service for everything data-related.

It’s time for the first exercise of this course. Remember that you can always take time to prepare before jumping in!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Data Basics
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/identifying-data-question-scroll.yaml" id="1tqww654g8c6u78r">
<br>

</edukamu-collapse>
<br>


Now that we know the fundamentals of data, it’s the perfect time to explore how data is handled. We’re talking about databases and processing, our next topics.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
