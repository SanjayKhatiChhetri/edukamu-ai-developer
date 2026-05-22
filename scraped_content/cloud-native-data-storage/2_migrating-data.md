## Migrating Data

After carefully assessing the specific needs of a use scenario, planning resources, and creating an implementation strategy, it's time to start thinking about data. Or, in other words, about bringing our precious data over into a brand-new NoSQL database.

Migrating data is a crucial aspect of managing and evolving your NoSQL solutions, and Azure Cosmos DB provides robust tools and features to facilitate this process seamlessly. When using NoSQL solutions, understanding how to efficiently move data in and out of Azure Cosmos DB is an essential skill.

Data migration is not just about moving data from one place to another; it's a strategic process that involves planning, execution, and validation. Effective data migration ensures that your applications continue to run smoothly, adapt to changing requirements, and leverage the capabilities of the NoSQL service in use.

Let's get familiar with the data migration services provided by Azure Cosmos DB. We'll review a total of three methods: 1) Azure Data Factory, 2) Stream Analytics, and 3) Cosmos DB Spark connector.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Migrating Data with Azure Data Factory
</edukamu-collapse-hidden-title>

**Azure Data Factory** is a native service to extract data, transform it, and load it across sinks and stores in an entirely serverless fashion. From a data integration perspective, this means you can marshal data from one datastore to another, regardless of the nuances of each, as long as you can reasonably transform the data between each data paradigm.

### Setup Process

Azure Cosmos DB for NoSQL is available as a **linked service** within Azure Data Factory. This type of linked service is supported both as a source of data ingest and as a target (**sink**) of data output. For both, the configuration is identical. You can configure the service using the Azure portal, or alternatively using a JSON object.

JSON

```JSON
{
    "name": "<example-name-of-linked-service>",
    "properties": {
        "type": "CosmosDb",
        "typeProperties": {
            "connectionString": "AccountEndpoint=<cosmos-endpoint>;AccountKey=<cosmos-key>;Database=<cosmos-database>"
        }
    }
}
```

Alternatively, you can use service principals or managed identities to connect to an Azure Cosmos DB for NoSQL account with Azure Data Factory.


### Reading from Azure Cosmos DB

In Azure Data Factory, when reading data from Azure Cosmos DB for NoSQL, we must configure our linked service as a **source**. This will read data in. To configure this, we must create a SQL query of the data we want to read in. For example, we may write a query such as SELECT id, categoryId, price, quantity, name FROM products WHERE price > 500 to filter the items from the container that we want to read in from Azure Cosmos DB for NoSQL to Azure Data Factory to be transformed and then eventually loaded into our destination data store.

In Azure Data Factory, our **source** activity has a configuration JSON object that we can use to set properties such as the query:

JSON

```JSON
{
    "source": {
        "type": "CosmosDbSqlApiSource",
        "query": "SELECT id, categoryId, price, quantity, name FROM products WHERE price > 500",
        "preferredRegions": [
            "East US",
            "West US"
        ]        
    }
}
```

### Writing to Azure Cosmos DB

In Azure Data Factory, when storing data to Azure Cosmos DB for NoSQL, we must configure our linked service as a **sink**. This will load our data. To configure this, we must set our write behavior. For example, we may always want to insert our data, or we may want to upsert our data and overwrite any items that may have a matching unique identifier (**id** field).

Our **sink** activity also had a configuration JSON object:

JSON

```JSON
"sink": {
    "type": "CosmosDbSqlApiSink",
    "writeBehavior": "upsert"
}
```

</edukamu-collapse>
<br>


When talking about data migration, reading refers to the process of *retrieving* data from Azure Cosmos DB, either as individual documents or as the result of queries. Writing, on the other hand, is *inserting*, *updating*, or *deleting* data to a NoSQL database. It involves adding new documents, modifying existing ones, or removing data from the database.

Building on the above, notice that data migration is a two-way-street. In other words, you can migrate data both in and out of a NoSQL solution, and Azure Data Factory, for example, works both ways.

Keep these perspectives in mind as you explore the other methods of data migration!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Migrating Data with Stream Analytics
</edukamu-collapse-hidden-title>

**Azure Stream Analytics** is a real-time event-processing engine designed to process fast streaming data from multiple sources simultaneously. It can aggregate, analyze, transform, and even move data around to other data stores for more profound and further analysis.

Configuring the Azure Cosmos DB for NoSQL output consists of either selecting the account within your subscription or providing your credentials, which commonly include:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>

<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
Property
</edukamu-table-header>
<edukamu-table-header>
Description
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>

<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Output alias
</edukamu-table-cell>
<edukamu-table-cell>
An alias to refer to this output in the query
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Account ID
</edukamu-table-cell>
<edukamu-table-cell>
Account endpoint URI
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Account Key
</edukamu-table-cell>
<edukamu-table-cell>
Account key
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Database
</edukamu-table-cell>
<edukamu-table-cell>
Name of the database resource
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Container name
</edukamu-table-cell>
<edukamu-table-cell>
Name of the container
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>

</edukamu-table>
</edukamu-section>
<br>

The database and container must already exist in the Azure Cosmos DB for NoSQL account before using the output sink.

### Writing to Azure Cosmos DB

Query results from Azure Stream Analytics will be processed as JSON output when written to Azure Cosmos DB for NoSQL.

Additionally, items are **upserted** to Azure Cosmos DB for NoSQL based on the value of the **id** field. Items are typically inserted into Azure Cosmos DB for NoSQL. If an item already exists with the same unique id, then the operation is assumed to be an **update** operation instead of an **insert** operation.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. Migrating Data with Azure Cosmos DB Spark Connectors
</edukamu-collapse-hidden-title>

With **Azure Synapse Analytics** and **Azure Synapse Link** for **Azure Cosmos DB**, you can create a cloud-native hybrid transactional and analytical processing (HTAP) to run analytics over your data in Azure Cosmos DB for NoSQL. This connection enables integration over your data pipeline on both ends of your data world, Azure Cosmos DB and Azure Synapse Analytics.

### Setup Process

First, you should make sure **Synapse Link** is enabled at the account level. This can be accomplished using the Azure portal or by using the Azure CLI:

```PowerShell
az cosmosdb create --name <name> --resource-group <resource-group> --enable-analytical-storage true
```

You can also use Azure PowerShell:

```PowerShell
New-AzCosmosDBAccount -ResourceGroupName <resource-group> -Name <name>  -Location <location> -EnableAnalyticalStorage true
```

When creating a container, you should enable analytical storage at the container level on a per container basis. Again, this can be accomplished with the portal.

This can also be accomplished with the CLI:

```PowerShell
az cosmosdb sql container create --resource-group <resource-group> --account <account> --database <database> --name <name> --partition-key-path <partition-key-path> --throughput <throughput> --analytical-storage-ttl -1
```

Or with Azure PowerShell:

```PowerShell
New-AzCosmosDBSqlContainer -ResourceGroupName <resource-group> -AccountName <account> -DatabaseName <database> -Name <name> -PartitionKeyPath <partition-key-path> -Throughput <throughput> -AnalyticalStorageTtl -1
```

### Reading from Azure Cosmos DB

**Note:** The next Python examples should be performed within your Azure Synapse Analytics workspace. Keep this in mind if you plan on trying the following on your own.

There are two options to query data from Azure Cosmos DB for NoSQL. First, you can choose to load to a Spark DataFrame where the metadata is cached. This example uses Python to load a Spark DataFrame that points to an Azure Cosmos DB for NoSQL account.

```Python
productsDataFrame = spark.read.format("cosmos.olap")\
    .option("spark.synapse.linkedService", "cosmicworks_serv")\
    .option("spark.cosmos.container", "products")\
    .load()
```

Alternatively, you can create a Spark table that points to the Azure Cosmos DB for NoSQL directly. You can then run SparkSQL queries against the Spark table without impacting the underlying store. This example uses Python to create a Spark table.

```Python
create table products_qry using cosmos.olap options (
    spark.synapse.linkedService 'cosmicworks_serv',
    spark.cosmos.container 'products'
)
```

### Writing to Azure Cosmos DB

If we want to write new data to Azure Cosmos DB from our Spark DataFrame, we can use the following Python script to append the data in a DataFrame to an existing container.

```Python
productsDataFrame.write.format("cosmos.oltp")\
    .option("spark.synapse.linkedService", "cosmicworks_serv")\
    .option("spark.cosmos.container", "products")\
    .mode('append')\
    .save()
```

(Notice that the above operation will impact our existing transaction workloads and will consume request units on the Azure Cosmos DB for NoSQL container[s].)

We can even take it further and stream data from a DataFrame, starting from a checkpoint. We can also append this streaming data to an existing container using this example Python script.

```Python
query = productsDataFrame\
    .writeStream\
    .format("cosmos.oltp")\
    .option("spark.synapse.linkedService", "cosmicworks_serv")\
    .option("spark.cosmos.container", "products")\
    .option("checkpointLocation", "/tmp/runIdentifier/")\
    .outputMode("append")\
    .start()

query.awaitTermination()
```

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Migrating Data with Azure Data Factory
</edukamu-collapse-hidden-title>

**Reminder:** The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

This practice exercise also requires a lab environment to be completed. You'll once again get to use a Windows-based virtual machine provided by Microsoft. You'll also be provided step-by-step instructions on using Azure Data Factory to migrate data to Azure Cosmos DB.

You can access the lab environment by navigating to Microsoft Learn and using the button to activate the lab.

<edukamu-button url="https://learn.microsoft.com/en-us/training/modules/move-data-azure-cosmos-db-sql-api/6-exercise-migrate-existing-data-using-azure-data-factory">Lab: Migrating Data with Azure Data Factory</edukamu-button>
<br>

Should you run any issues, please refer to the more detailed instructions on the page *Components of Cosmos DB for NoSQL*.

If you decide to take on the practice exercise, good luck! Enjoy the process!

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
Migrating data in and out of Azure Cosmos DB is made simple with the tools we've just covered. By using simple commands, data can be brought into or taken out of the service, which facilitates the configuring process of the global database platform.

Next, take some time to recap and review before completing the last exercise of this unit.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Data Migration
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module2/migrating-data-text-poll-1.yaml" id="bmqwgfqo2bupmnt4">

<edukamu-text-poll url="/exercises/module2/migrating-data-text-poll-2.yaml" id="4mbbbuij1b5nzkeg">

<edukamu-text-poll url="/exercises/module2/migrating-data-text-poll-3.yaml" id="movimtj7fkmtso0g">

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/2/migrating-data?question=bmqwgfqo2bupmnt4">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


After completing this unit, equipped with a solid foundation for understanding of NoSQL planning, throughput methods, and data migration nuances, you should be well prepared to start planning and implementing robust data solutions with the Azure Cosmos DB ecosystem.

In the third unit, we'll start digging a lot deeper into the capabilities of Azure Cosmos DB. Remember to take a long break before continuing, though! You should also take some time to recap every now and then.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-4mod-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
