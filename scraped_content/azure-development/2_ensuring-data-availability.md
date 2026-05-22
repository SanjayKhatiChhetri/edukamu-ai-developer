## Ensuring Data Availability

Have you ever wondered why database solutions are so important? As you know, data is the foundation of all modern applications, but what is the most important duty of a database? It's naturally difficult to determine just one, but ensuring data availability would be a great pick.

Data availability refers to the assurance that your data is always accessible when needed. In the context of Azure Blob Storage, it involves ensuring that your data is stored in the right tier (hot, cool, or archive) based on how frequently it's accessed, and is protected against loss or corruption.

On this page, we'll explore Blob Storage lifecycles, which practically refers to how data is managed from the creation of a database to its eventual deletion. Managing this lifecycle means implementing policies that automatically move data to the most cost-effective storage tiers and remove it when it's no longer needed.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Blob Storage Lifecycles
</edukamu-collapse-hidden-title>

Data sets have unique lifecycles. Early in the lifecycle, people access some data often. But the need for access drops drastically as the data ages. Some data stays idle in the cloud and is rarely accessed once stored. Some data expires days or months after creation, while other data sets are actively read and modified throughout their lifetimes.

### Access Tiers

Azure storage offers different access tiers, allowing you to store blob object data in the most cost-effective manner. Available access tiers include:

- **Hot** - Optimized for storing data that is accessed frequently.
- **Cool** - Optimized for storing data that is infrequently accessed and stored for a minimum of 30 days.
- **Cold tier** - Optimized for storing data that is infrequently accessed and stored for a minimum of 90 days. The cold tier has lower storage costs and higher access costs compared to the cool tier.
- **Archive** - Optimized for storing data that is rarely accessed and stored for at least 180 days with flexible latency requirements, on the order of hours.

The following considerations apply to the different access tiers:

- The access tier can be set on a blob during or after upload.
- Only the hot and cool access tiers can be set at the account level. The archive access tier can only be set at the blob level.
- Data in the cool access tier has slightly lower availability, but still has high durability, retrieval latency, and throughput characteristics similar to hot data.
- Data in the archive access tier is stored offline. The archive tier offers the lowest storage costs but also the highest access costs and latency.
- The hot and cool tiers support all redundancy options. The archive tier supports only LRS, GRS, and RA-GRS.
- Data storage limits are set at the account level and not per access tier. You can choose to use all of your limit in one tier or across all three tiers.

### Managing the Data Lifecycle

Azure Blob storage lifecycle management offers a rich, rule-based policy for General Purpose v2 and Blob storage accounts. Use the policy to transition your data to the appropriate access tiers or expire at the end of the data's lifecycle. The lifecycle management policy lets you:

- Transition blobs to a cooler storage tier (hot to cool, hot to archive, or cool to archive) to optimize for performance and cost
- Delete blobs at the end of their lifecycles
- Define rules to be run once per day at the storage account level
- Apply rules to containers or a subset of blobs (using prefixes as filters)

Consider a scenario in which data gets frequent access during the early stages of the lifecycle, but only occasionally after two weeks. Beyond the first month, the data set is rarely accessed. In this scenario, hot storage is best during the early stages. Cool storage is most appropriate for occasional access. Archive storage is the best tier option after the data ages over a month. By adjusting storage tiers in respect to the age of data, you can design the least expensive storage options for your needs. To achieve this transition, lifecycle management policy rules are available to move aging data to cooler tiers.

**Note**: Data stored in a premium block blob storage account cannot be tiered to Hot, Cool, or Archive using Set Blob Tier or using Azure Blob Storage lifecycle management. To move data, you must synchronously copy blobs from the block blob storage account to the Hot tier in a different account using the Put Block From URL API or a version of AzCopy that supports this API. The Put Block From URL API synchronously copies data on the server, meaning the call completes only once all the data is moved from the original server location to the destination location.

</edukamu-collapse>
<br>

In Azure Blob Storage, the transition of data between the hot, cool, and archive tiers can be automated using Azure's lifecycle management policies, but it does not happen automatically without configuration.

Lifecycle management policies in Azure Blob Storage allow you to set rules based on your data usage patterns and needs. These rules can automate the process of tiering data from hot to cool or from cool to archive after a specified period of inactivity. For example, you can create a policy to move a blob to the cool tier if it hasn't been accessed for 30 days, and further to the archive tier if it remains unaccessed for 180 days.

However, without these policies in place, the data will remain in the tier it was originally placed in, regardless of how frequently it is accessed. This means that if effective cost management is a priority, you need to proactively set up and manage these lifecycle policies according to your specific needs.

Effective lifecycle management is crucial for several reasons, including the following:

- **Cost Management**: Storing all data in the highest performance (and cost) tier can be prohibitively expensive, especially as data volumes grow.
- **Performance Optimization**: Ensuring frequently accessed data is readily available, while archiving or deleting stale data, optimizes performance.
- **Regulatory Compliance**: Certain industries have specific requirements for data retention and deletion, making lifecycle management essential for compliance.

Consider a healthcare application storing patient records and medical images for practical and regulatory reasons. Initially, these records are frequently accessed and stored in the 'hot' tier for immediate availability. Over time, as patient visits become less frequent, the records are moved to the 'cool' tier, where they are less accessible but cheaper to store. Finally, after a regulatory retention period, older records are either archived or securely deleted, ensuring compliance and cost-effectiveness.

Managing data availability throughout its lifecycle is in other words about finding the balance between accessibility, cost, and compliance, making it crucial for any data-driven organization.

Next, let's discover lifecycle policies and their implementation in Azure Blob Storage.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Discovering Lifecycle Policies
</edukamu-collapse-hidden-title>

A lifecycle management policy is a collection of rules in a JSON document. Each rule definition within a policy includes a filter set and an action set. The filter set limits rule actions to a certain set of objects within a container or objects names. The action set applies the tier or delete actions to the filtered set of objects:

JSON

```JSON
{
  "rules": [
    {
      "name": "rule1",
      "enabled": true,
      "type": "Lifecycle",
      "definition": {...}
    },
    {
      "name": "rule2",
      "type": "Lifecycle",
      "definition": {...}
    }
  ]
}
```

A policy is a collection of rules:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Parameter name**
</edukamu-table-header>
<edukamu-table-header>
**Parameter type**
</edukamu-table-header>
<edukamu-table-header>
**Notes**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
`rules`
</edukamu-table-cell>
<edukamu-table-cell>
An array of rule objects
</edukamu-table-cell>
<edukamu-table-cell>
At least one rule is required in a policy. You can define up to 100 rules in a policy.
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

Each rule within the policy has several parameters:

<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="20%">
**Parameter name**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Parameter type**
</edukamu-table-header>
<edukamu-table-header width="40%">
**Notes**
</edukamu-table-header>
<edukamu-table-header width="20%">
**Required**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
`name`
</edukamu-table-cell>
<edukamu-table-cell>
String
</edukamu-table-cell>
<edukamu-table-cell>
A rule name can include up to 256 alphanumeric characters. Rule name is case-sensitive. It must be unique within a policy.
</edukamu-table-cell>
<edukamu-table-cell>
True
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
`enabled`
</edukamu-table-cell>
<edukamu-table-cell>
Boolean
</edukamu-table-cell>
<edukamu-table-cell>
An optional boolean to allow a rule to be temporarily disabled. Default value is true if it's not set.
</edukamu-table-cell>
<edukamu-table-cell>
False
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
`type`
</edukamu-table-cell>
<edukamu-table-cell>
An enum value
</edukamu-table-cell>
<edukamu-table-cell>
The current valid type is Lifecycle.
</edukamu-table-cell>
<edukamu-table-cell>
True
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
`definition`
</edukamu-table-cell>
<edukamu-table-cell>
An object that defines the lifecycle rule
</edukamu-table-cell>
<edukamu-table-cell>
Each definition is made up of a filter set and an action set.
</edukamu-table-cell>
<edukamu-table-cell>
True
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

(A Boolean state variable is a type of variable used in programming that can hold only two possible values: `true` or `false`. This kind of variable is often used to represent a simple on/off or yes/no state in a program, like a switch that can be either turned on or turned off.)

### Rules

Each rule definition includes a filter set and an action set. The filter set limits rule actions to a certain set of objects within a container or objects names. The action set applies the tier or delete actions to the filtered set of objects.

The following sample rule filters the account to run the actions on objects that exist inside `container1` and start with `foo`.

- Tier blob to cool tier 30 days after last modification
- Tier blob to archive tier 90 days after last modification
- Delete blob 2,555 days (seven years) after last modification
- Delete blob snapshots 90 days after snapshot creation

Consider the following JSON example.

JSON

```JSON
{
  "rules": [
    {
      "name": "ruleFoo",
      "enabled": true,
      "type": "Lifecycle",
      "definition": {
        "filters": {
          "blobTypes": [ "blockBlob" ],
          "prefixMatch": [ "container1/foo" ]
        },
        "actions": {
          "baseBlob": {
            "tierToCool": { "daysAfterModificationGreaterThan": 30 },
            "tierToArchive": { "daysAfterModificationGreaterThan": 90 },
            "delete": { "daysAfterModificationGreaterThan": 2555 }
          },
          "snapshot": {
            "delete": { "daysAfterCreationGreaterThan": 90 }
          }
        }
      }
    }
  ]
}
```

### Rule Filters

Filters limit rule actions to a subset of blobs within the storage account. If more than one filter is defined, a logical AND runs on all filters. Filters include:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header width="25%">
**Filter name**
</edukamu-table-header>
<edukamu-table-header width="50%">
**Type**
</edukamu-table-header>
<edukamu-table-header width="25%">
**Is Required**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
blobTypes
</edukamu-table-cell>
<edukamu-table-cell>
An array of predefined enum values.
</edukamu-table-cell>
<edukamu-table-cell>
Yes
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
prefixMatch
</edukamu-table-cell>
<edukamu-table-cell>
An array of strings for prefixes to be match. Each rule can define up to 10 prefixes. A prefix string must start with a container name.
</edukamu-table-cell>
<edukamu-table-cell>
No
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
blobIndexMatch
</edukamu-table-cell>
<edukamu-table-cell>
An array of dictionary values consisting of blob index tag key and value conditions to be matched. Each rule can define up to 10 blob index tag condition.
</edukamu-table-cell>
<edukamu-table-cell>
No
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

### Rule Actions

Actions are applied to the filtered blobs when the run condition is met.

Lifecycle management supports tiering and deletion of blobs and deletion of blob snapshots. Define at least one action for each rule on blobs or blob snapshots.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Action**
</edukamu-table-header>
<edukamu-table-header>
**Base Blob**
</edukamu-table-header>
<edukamu-table-header>
**Snapshot**
</edukamu-table-header>
<edukamu-table-header>
**Version**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
tierToCool
</edukamu-table-cell>
<edukamu-table-cell>
Supported for blockBlob
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
enableAutoTierToHotFromCool
</edukamu-table-cell>
<edukamu-table-cell>
Supported for blockBlob
</edukamu-table-cell>
<edukamu-table-cell>
Not supported
</edukamu-table-cell>
<edukamu-table-cell>
Not supported
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
tierToArchive
</edukamu-table-cell>
<edukamu-table-cell>
Supported for blockBlob
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
delete
</edukamu-table-cell>
<edukamu-table-cell>
Supported for blockBlob and appendBlob
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
<edukamu-table-cell>
Supported
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

**Note**: If you define more than one action on the same blob, lifecycle management applies the least expensive action to the blob. For example, action `delete` is cheaper than action `tierToArchive`. Action `tierToArchive` is cheaper than action `tierToCool`.

The run conditions are based on age. Base blobs use the last modified time to track age, and blob snapshots use the snapshot creation time to track age.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>
**Action run condition**
</edukamu-table-header>
<edukamu-table-header>
**Condition value**
</edukamu-table-header>
<edukamu-table-header>
**Description**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
daysAfterModificationGreaterThan
</edukamu-table-cell>
<edukamu-table-cell>
Integer value indicating the age in days
</edukamu-table-cell>
<edukamu-table-cell>
The condition for base blob actions
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
daysAfterCreationGreaterThan
</edukamu-table-cell>
<edukamu-table-cell>
Integer value indicating the age in days
</edukamu-table-cell>
<edukamu-table-cell>
The condition for blob snapshot actions
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
daysAfterLastAccessTimeGreaterThan
</edukamu-table-cell>
<edukamu-table-cell>
Integer value indicating the age in days
</edukamu-table-cell>
<edukamu-table-cell>
The condition for a current version of a blob when access tracking is enabled
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
daysAfterLastTierChangeGreaterThan
</edukamu-table-cell>
<edukamu-table-cell>
Integer value indicating the age in days after last blob tier change time
</edukamu-table-cell>
<edukamu-table-cell>
This condition applies only to tierToArchive actions and can be used only with the daysAfterModificationGreaterThan condition.
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
### Implementing Lifecycle Policies
</edukamu-collapse-hidden-title>

You can add, edit, or remove a policy by using any of the following methods:

- Azure portal
- Azure PowerShell
- Azure CLI
- REST APIs

The following are the steps and some examples for the Portal and Azure CLI.

### Azure Portal

There are two ways to add a policy through the Azure portal: Azure portal List view, and Azure portal Code view.

### 1. Azure Portal List View

1. Sign in to the Azure portal.
2. Select **All resources** and then select your storage account.
3. Under **Data management**, select **Lifecycle management** to view or change your rules.
4. Select the **List view** tab.
5. Select **Add rule** and then fill out the **Action set** form fields. In the following example, blobs are moved to cool storage if they haven't been modified for 30 days.
6. Select **Filter set** to add an optional filter. Then, select Browse to specify a container and folder by which to filter.
7. Select **Review + add** to review the policy settings.
8. Select **Add** to add the new policy.

### 2. Azure Portal Code View

1. Follow the first three steps in the **List view** section.
2. Select the **Code view** tab. The following JSON is an example of a policy that moves a block blob whose name begins with *log* to the cool tier if it has been more than 30 days since the blob was modified.

JSON

```JSON
{
  "rules": [
    {
      "enabled": true,
      "name": "move-to-cool",
      "type": "Lifecycle",
      "definition": {
        "actions": {
          "baseBlob": {
            "tierToCool": {
              "daysAfterModificationGreaterThan": 30
            }
          }
        },
        "filters": {
          "blobTypes": [
            "blockBlob"
          ],
          "prefixMatch": [
            "sample-container/log"
          ]
        }
      }
    }
  ]
}
```

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
Select <span style="font-weight: bold;">Save</span>.
</li>
</ol>
</edukamu-section>
<br>

### Azure CLI

To add a lifecycle management policy with Azure CLI, write the policy to a JSON file, then call the `az storage account management-policy create` command to create the policy.

Azure CLI

```json
az storage account management-policy create \
    --account-name <storage-account> \
    --policy @policy.json \
    --resource-group <resource-group>
```

A lifecycle management policy must be read or written in full. Partial updates aren't supported.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-pink">
When data is in the archive tier, it is in the most cost-effective storage state but is not readily accessible. This tier is intended for data that you don't expect to access frequently, such as for long-term retention, backup, or compliance purposes.

But what if something changes? What if you need to start accessing archived data more frequently? Azure Blob Storage offers many options for moving data back to a "hotter" tier, which is oftentimes metaphorically referred to as *rehydrating data*.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Rehydrating Data
</edukamu-collapse-hidden-title>

While a blob is in the archive access tier, it's considered to be offline and can't be read or modified. In order to read or modify data in an archived blob, you must first rehydrate the blob to an online tier, either the hot or cool tier. There are two options for rehydrating a blob that is stored in the archive tier:

- **Copy an archived blob to an online tier**: You can rehydrate an archived blob by copying it to a new blob in the hot or cool tier with the Copy Blob or Copy Blob from URL operation. Microsoft recommends this option for most scenarios.
- **Change a blob's access tier to an online tier**: You can rehydrate an archived blob to hot or cool by changing its tier using the Set Blob Tier operation.

Rehydrating a blob from the archive tier can take several hours to complete. Microsoft recommends rehydrating larger blobs for optimal performance. Rehydrating several small blobs concurrently might require extra time.

### Rehydration Priorities

When you rehydrate a blob, you can set the priority for the rehydration operation via the optional `x-ms-rehydrate-priority` header on a Set Blob Tier or **Copy Blob/Copy Blob From URL** operation. Rehydration priority options include:

- **Standard priority**: The rehydration request is processed in the order it was received and might take up to 15 hours.
- **High priority**: The rehydration request is prioritized over standard priority requests and might complete in under one hour for objects under 10 GB in size.

To check the rehydration priority while the rehydration operation is underway, call Get Blob Properties to return the value of the `x-ms-rehydrate-priority` header. The rehydration priority property returns either *Standard* or *High*.

### 1. Copying Archived Blobs to Online Tiers

You can use either the **Copy Blob** or **Copy Blob from URL** operation to copy the blob. When you copy an archived blob to a new blob in an online tier, the source blob remains unmodified in the archive tier. You must copy the archived blob to a new blob with a different name or to a different container. You can't overwrite the source blob by copying to the same blob.

Copying an archived blob to an online destination tier is supported within the same storage account only. You can't copy an archived blob to a destination blob that is also in the archive tier.

The following table shows the behavior of a blob copy operation, depending on the tiers of the source and destination blob.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>

<edukamu-table-row>
<edukamu-table-header>

</edukamu-table-header>
<edukamu-table-header>
**Hot tier source**
</edukamu-table-header>
<edukamu-table-header>
**Cool tier source**
</edukamu-table-header>
<edukamu-table-header>
**Archive tier source**
</edukamu-table-header>
</edukamu-table-row>

</edukamu-table-head>
<edukamu-table-body>

<edukamu-table-row>
<edukamu-table-cell>
Hot tier destination
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
<edukamu-table-cell>
Supported within the same account. Requires blob rehydration.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Cool tier destination
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
<edukamu-table-cell>
Supported within the same account. Requires blob rehydration.
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
Archive tier destination
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
<edukamu-table-cell>
Supported
</edukamu-table-cell>
<edukamu-table-cell>
Unsupported
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

### 2. Changing Blobs' Access Tiers to Online Tiers

The second option for rehydrating a blob from the archive tier to an online tier is to change the blob's tier by calling Set Blob Tier. With this operation, you can change the tier of the archived blob to either hot or cool.

Once a Set Blob Tier request is initiated, it can't be canceled. During the rehydration operation, the blob's access tier setting continues to show as archived until the rehydration process is complete.

**Caution**: Changing a blob's tier doesn't affect its last modified time. If there is a lifecycle management policy in effect for the storage account, then rehydrating a blob with Set Blob Tier can result in a scenario where the lifecycle policy moves the blob back to the archive tier after rehydration because the last modified time is beyond the threshold set for the policy.

Imagine a financial institution that uses Azure Blob Storage for storing customer transaction records. For regulatory compliance, these records are required to be kept for several years, but they are rarely accessed once stored. Therefore, the institution archives these records in the Azure Blob Storage archive tier, benefiting from lower storage costs.

A few years later, there's a legal requirement for an audit of transactions related to a specific customer account due to a suspected financial irregularity. The records from several years ago, currently in the archive tier, are needed for this audit.

In this scenario, the financial institution initiates the rehydration process to move the specific customer's transaction records from the archive tier to the hot tier. Once the data is rehydrated and accessible, auditors can review the transaction history to complete their investigation.

This example illustrates a typical situation in which rehydrating data from the archive tier becomes necessary for compliance and legal inquiries.

</edukamu-collapse>
<br>

Rehydrating data is crucial for scenarios where data, initially deemed infrequently accessible, becomes necessary for business operations, analytics, or compliance checks. It is also worth noting that rehydrating data requires manual initiation. This process involves a specific request and a waiting period for the data to become accessible again.

Ensuring data availability might be the deciding factor between a successful and a failed business, so developers with advanced knowledge of the topic are in high demand.

Take a while to recap before consolidating your new knowledge with another exercise!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Data Availability
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module2/ensuring-data-availability-text-poll-1.yaml" id="3u9465jvwd6ivtjf">

<edukamu-text-poll url="/exercises/module2/ensuring-data-availability-text-poll-2.yaml" id="dh8isiycr6z3ss6s">

<edukamu-text-poll url="/exercises/module2/ensuring-data-availability-text-poll-3.yaml" id="bbfve0pl4pzdlz8k">
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/2/ensuring-data-availability?question=3u9465jvwd6ivtjf">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

Azure Blob Service is an advanced, highly capable data solution available in Microsoft Azure. It's cost-effective for long-term storage, providing scalable and secure solutions.

On the other hand, Azure Cosmos DB is perfect for applications that need fast, global access to structured or semi-structured data, with complex querying and real-time processing capabilities. Choose Blob Storage for bulk, archival storage needs, and Cosmos DB for high-performance, real-time database requirements, taking into account the specifications of the use case at hand.

Do you still remember our second main topic of this unit? It's containerized solutions, which is up next!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
