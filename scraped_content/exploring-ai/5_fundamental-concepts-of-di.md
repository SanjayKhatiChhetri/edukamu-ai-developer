<edukamu-video content="/videos/devai-2-unit5-video.yaml"/>
<br>

## Fundamental Concepts of DI

Welcome to the fifth and final unit of this course!

We’ll spend this unit focusing on a topic that might be a bit difficult to grasp at first, but one that’s generated a lot of excitement across a variety of fields during the recent years. We’re talking about document intelligence.

In today's digital age, the abundance of unstructured data in various forms, such as text documents, images, and PDFs, presents both a challenge and an opportunity. Aspiring AI developers like yourself stand at the forefront of leveraging artificial intelligence to unlock the valuable insights hidden within these documents.

Document Intelligence is a specialized field within AI that empowers machines to comprehend, analyze, and derive meaningful information from unstructured data. It is not just an abstract concept; it's a practical toolkit that holds immense relevance across industries. Whether you're interested in automating administrative tasks, processing invoices, or extracting insights from vast datasets, the principles we’re about to learn will serve as the building blocks for creating intelligent document-centric AI solutions.

Let’s start from the basics. After exploring the fundamental principles of document intelligence, or DI for short, we’ll spend a while focusing on knowledge mining and Azure Cognitive Search.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Document Intelligence
</edukamu-collapse-hidden-title>

Document intelligence describes AI capabilities that support processing text and making sense of information in text. As an extension of optical character recognition (OCR), document intelligence takes the next step a person might after reading a form or document. It automates the process of extracting, understanding, and saving the data in text.

Consider an organization that needs to process large numbers of receipts for expenses claims, project costs, and other accounting purposes. Suppose someone needs to manually enter the information into a database. The manual process is relatively slow and potentially error-prone.

Using document intelligence, the company can take a scanned image of a receipt, digitize the text with OCR, and pair the field items with their field names in a database. Document intelligence can identify specific data such as the merchant's name, merchant's address, total value, and tax value.

**Azure AI Document Intelligence** supports features that can analyze documents and forms with prebuilt and custom models. During the course of this unit, we’ll explore the main features within the service.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Document Intelligence Capabilities
</edukamu-collapse-hidden-title>

Document intelligence relies on machine learning models that are trained to recognize data in text. The ability to extract text, layout, and key-value pairs are known as document analysis. Document analysis provides locations of text on a page identified by bounding box coordinates.

<edukamu-image url="/graphics/module5/contoso-receipt-small.png" alt="A screenshot of a scanned receipt for the purchase of a Surface Pro and a Surface Pen."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

For example, the information in on the receipt *123 Main Street* is saved as a *key, address* and a *value, 123 Main Street*. Document analysis could record the location of the field value as bounding box coordinates [4.1, 2.2], [4.3, 2.2], [4.3, 2.4], [4.1, 2.4]. Machine learning models can interpret the data in a document or form because they are trained to recognize patterns in bounding box coordinate locations and text.

A challenge for automating the process of analyzing documents is that forms and documents come in all different formats. For example, while tax forms and driver's license documents both include an individual's name, the bounding box coordinates for the name differ. Separate machine learning models need to be trained to provide high quality results for different forms and documents. In this way, sometimes you might be able to use prebuilt machine learning models that have been trained on commonly used document formats. Other times, you might need to customize a machine learning model to recognize a unique document format.

Automating the process of reading text and recording data can accelerate operations, create better customer experiences, improve decision making, and more.

</edukamu-collapse>
<br>


The capabilities mentioned above are just a fraction of the possibilities offered by document intelligence. But what’s AI’s role in all this?

Let’s find out!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Document Intelligence and AI
</edukamu-collapse-hidden-title>

Document Intelligence is a subfield of AI that leverages advanced algorithms and models to make sense of unstructured data within documents. The following AI technologies play a crucial role in document intelligence:
1. **Natural Language Processing (NLP)**: NLP enables machines to understand and interpret human language, making it possible to extract information, identify entities, and comprehend the context of textual content in documents.
2. **Computer Vision**: Computer vision is utilized to analyze and interpret visual information within documents, such as images or scanned pages. It enables the extraction of data from images and the recognition of text, shapes, and structures.
3. **Machine Learning**: Machine learning algorithms are employed for tasks like document classification, sentiment analysis, and entity recognition. These algorithms can be trained on large datasets to improve their ability to understand and categorize diverse document types.
4. **Data Extraction Techniques**: Document intelligence involves techniques for extracting structured data from unstructured documents, enabling the conversion of information into a format that can be easily processed and analyzed.


### Why is Document Intelligence Important for Beginning AI Developers?

For beginning AI developers, understanding document intelligence is crucial for several reasons:
1. **Real-World Applications**: Document intelligence has a wide range of real-world applications across various industries. From automating data entry and processing invoices to extracting insights from research papers, the ability to work with document data is invaluable.
2. **Versatility**: Document intelligence techniques can be applied to different types of documents, including text-based files, images, PDFs, and more. This versatility makes it applicable to a diverse set of scenarios.
3. **Problem-Solving Skills**: Working with document intelligence challenges developers to think critically about how to extract meaningful information from unstructured data. It enhances problem-solving skills and requires a holistic understanding of AI technologies.
4. **Integration with Business Processes**: Many businesses rely on handling vast amounts of document-based information. Document intelligence allows developers to create AI solutions that seamlessly integrate with existing business processes, improving efficiency and accuracy.
5. **Foundation for Advanced AI Projects**: Document intelligence serves as a foundational knowledge area for more advanced AI projects. As developers progress in their AI journey, the skills learned in document intelligence can be extended to tackle more complex challenges in natural language understanding, image recognition, and other domains.

In summary, document intelligence provides a practical entry point for AI developers, offering them opportunities to apply AI concepts to solve real-world problems with tangible impacts.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Document intelligence can work as a steppingstone towards more complex AI applications. That’s why you, an upcoming Azure developer, should also pay close attention to it!

On the next page, we’ll inspect DI from the perspective of Microsoft Azure. Let’s take a little false start and begin exploring right now.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### DI and Azure: Receipt Analysis 
</edukamu-collapse-hidden-title>

Azure AI Document Intelligence is a set of tools focused entirely on document intelligence. Its capabilities can be categorized into three categories:

* **Prebuilt models** - pretrained models that have been built to process common document types such as invoices, business cards, ID documents, and more. These models are designed to recognize and extract specific fields that are important for each document type.
* **Custom models** - can be trained to identify specific fields that are not included in the existing pretrained models.
* **Document analysis** - general document analysis that returns structured data representations, including regions of interest and their inter-relationships.

Let’s explore prebuilt models in a bit more detail, since they are the go-to solution for beginning developers.

### Prebuilt Models

The prebuilt models apply advanced machine learning to accurately identify and extract text, key-value pairs, tables, and structures from forms and documents. These capabilities include extracting:
* customer and vendor details from invoices
* sales and transaction details from receipts
* identification and verification details from identity documents
* health insurance details
* business contact details
* agreement and party details from contracts
* taxable compensation, mortgage interest, student loan details and more

For example, consider the prebuilt receipt model. It processes receipts by:
* Matching field names to values
* Identifying tables of data
* Identifying specific fields, such as dates, telephone numbers, addresses, totals, and others

The receipt model has been trained to recognize data on several different receipt types, such as thermal receipts (printed on heat-sensitive paper), hotel receipts, gas receipts, credit card receipts, and parking receipts.

Fields recognized include:
* Name, address, and telephone number of the merchant
* Date and time of the purchase
* Name, quantity, and price of each item purchased
* Total, subtotals, and tax values

Each field and data pair has a confidence level, indicating the likely level of accuracy. This could be used to automatically identify when a person needs to verify a receipt.

The model has been trained to recognize several different languages, depending on the receipt type. For best results when using the prebuilt receipt model, images should be:
* JPEG, PNG, BMP, PDF, or TIFF format
* File size less than 500 MB for paid (S0) tier and 4 MB for free (F0) tier
* Between 50 x 50 pixels and 10000 x 10000 pixels
* For PDF documents, no larger than 17 inches x 17 inches
* One receipt per document

You can get started with training models in the [Document Intelligence Studio](https://formrecognizer.appliedai.azure.com/studio)(target="_blank"), a user interface for testing document analysis, prebuilt models, and creating custom models.

</edukamu-collapse>
<br>


This is once again a great time to remind you to take advantage of your Azure subscription. If you have one, spend as much time as possible exploring the platform; it will surely pay off during your studies!

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Practice: Document Intelligence
</edukamu-collapse-hidden-title>

**Reminder**: The exercises marked *Practice* are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

If you have an active Azure subscription, you can do some document intelligence of your own over at Microsoft’s Learn platform.

<edukamu-button url="https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/10-document-intelligence.html">Practice: Document Intelligence (Microsoft Learn)</edukamu-button>
<br>

</edukamu-collapse>
<br> -->


All right, let’s finish off this section with the following exercises.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Basics of Document Intelligence
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module5/fundamental-concepts-text-poll.yaml" id="f8699306478c9gs1"/>
<br>
<edukamu-text-poll url="/exercises/module5/fundamental-concepts-text-poll-2.yaml" id="50cl16zm7988z57o"/>
<br>
<edukamu-text-poll url="/exercises/module5/fundamental-concepts-text-poll-3.yaml" id="3vk5kd67o81y59e3"/>
<br>
<edukamu-text-poll url="/exercises/module5/fundamental-concepts-text-poll-4.yaml" id="c5h0n4v598ykg652"/>
<br>
<edukamu-text-poll url="/exercises/module5/fundamental-concepts-text-poll-5.yaml" id="x5tw8kj7gcm2w7af"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/5/fundamental-concepts-of-di?question=f8699306478c9gs1">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="digital-workforce-logo">
### Scenario Exercise
</edukamu-collapse-hidden-title>

Yardability is an imaginary company that focuses on garden planning and related services. Their business was struggling some time ago, but in the past year they have automated many of their business processes and now business is booming! This has generated a new problem though – their back office is drowning in paperwork and various customer service tasks. 

They do have partial automation – they have a system capable of opening the company email inbox and reading email text contents and metadata. Currently any email from a given list of subcontractor email addresses is automatically forwarded to the billing department for invoice processing. But this is no longer enough. They have identified a few main challenges that they cannot automate with basic scripts or automation tools. You have been hired as a consultant to advise them which AI-tools might be most suitable for the tasks at hand.

Get familiar with the scenarios presented below and come up with your solutions! You can also check out our model answers afterwards.

</edukamu-collapse> -->

<!-- <edukamu-collapse isCollapsed="true" title-level="4" theme="microsoft-mainos-collapse">
<edukamu-collapse-hidden-title collapseType="aineisto">
### YRITYS: Taking it a Step Further
</edukamu-collapse-hidden-title>

Placeholder: Tähän teksti, jossa on tietoiskuja tai pohdintaa.

</edukamu-collapse>
<br> -->

Next, we’ll focus a while on Azure services related to document intelligence. More precisely, we’ll get acquainted with something called cognitive search.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1.png" alt="Edukamu-progress-in-a-module-image">
