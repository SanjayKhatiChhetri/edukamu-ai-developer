## Recognizing Characters with AI

Artificial intelligence can be trained to do pretty much everything imaginable, and recognizing different shapes, forms, and even people is no exception. AI also excels in recognizing characters, with which we humans might struggle every once in a while.

Character recognition, also known as Optical Character Recognition (OCR), is a field of artificial intelligence that focuses on teaching machines to interpret and understand written or printed text. In simpler terms, it's about empowering computers to recognize and extract textual information from images or documents.

The primary goal of character recognition is to bridge the gap between the physical and digital worlds, allowing machines to comprehend text in a way humans do. This technology plays a crucial role in automating the process of digitizing printed or handwritten content, making it more accessible, searchable, and usable in various applications.

Let’s check out a few use cases for character recognition.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Use Cases of Character Recognition
</edukamu-collapse-hidden-title>

### 1. Document Digitization

Imagine a company in which massive volumes of paper-based documents need to be converted into digital formats for easy storage, retrieval, and analysis.

Character recognition can be employed to automatically extract text from scanned documents, turning piles of paperwork into searchable and editable digital files. This not only saves time and resources but also enhances the efficiency of information management.

### 2. Accessibility for Visually Impaired

Consider individuals with visual impairments who encounter challenges in accessing printed text.

Character recognition, when integrated into assistive technologies, can convert printed text into audible speech or readable Braille. This empowers visually impaired individuals by providing them with real-time access to a wide range of printed materials.

### 3. Translation Services

Picture a scenario in which people encounter documents or data in a language they don't understand.

Character recognition combined with language translation capabilities can automatically translate text from one language to another. This promotes cross-cultural relations and facilitates communication in diverse linguistic environments.

### 4. Data Entry Automation

In businesses or organizations dealing with large amounts of paper forms, manually writing down details can be a huge burden on both the individuals and company resources.

Character recognition can be applied to automatically extract data from forms, reducing the need for manual data entry. This not only minimizes errors but also speeds up processes while allowing for more efficient use of workforce.

### 5. Historical Document Preservation

Think about preserving and digitizing historical handwritten manuscripts or documents. Until recently, museums and other organizations have been spending enormous amounts on manual work.

Character recognition can play a crucial role in converting ancient or delicate documents into digital formats, ensuring their preservation for future generations while making them accessible for research and study – even for the visually impaired, as we just saw.

</edukamu-collapse>
<br>


Please notice that the scenarios described above are just a few examples of the most prominent use cases for character recognition!

At first, character recognition might not sound as exciting as its facial counterpart, but beneath the surface, there are countless possibilities to explore.

Microsoft Azure has all the tools needed for leveraging this amazing technology. The main service is Vision Studio – let’s take a look.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Azure Vision Studio
</edukamu-collapse-hidden-title>

The ability to extract text from images is handled by Azure AI Vision service. One of the services in Azure AI Vision is the *Read API*. You can think of the Read API as an OCR engine that powers text extraction from images, PDFs, and TIFF files.

The Read API uses the latest recognition models and is optimized for images that have a significant amount of text or have considerable visual noise. It can automatically determine the proper recognition model to use taking into consideration the number of lines of text, images that include text, and handwriting.

The results from the Read API are arranged into the following hierarchy:
* **Pages** - One for each page of text, including information about the page size and orientation.
* **Lines** - The lines of text on a page.
* **Words** - The words in a line of text, including the bounding box coordinates and text itself.

Each line and word include bounding box coordinates indicating its position on the page.

Vision Studio provides a graphical user interface and enables you to try out Azure AI Vision service without writing any code.

If you have an active Azure subscription or a trial, you can access the Visual Studio right here:

<edukamu-button url="https://portal.vision.cognitive.azure.com/">Azure Visual Studio</edukamu-button>
<br>

If you have the opportunity to explore Azure and its services manually, please do it as often as possible as you continue moving forward on these courses!

**Reminder**: Here and there within these courses, you’ll find exercises marked *Practice*. They are not a mandatory requirement for completing this course since they may require technical hardware or software not available for everyone or everywhere. We highly recommend that you complete them, if you have the opportunity, but they are not mandatory.

As usual, to use the Azure AI Vision service you must first create a resource for it in your Azure subscription. You can use either of the following resource types:

* **Azure AI Vision**: A specific resource for vision services. Use this resource type if you don't intend to use any other AI services, or if you want to track utilization and costs for your AI Vision resource separately.
* **Azure AI services**: A general resource that includes Azure AI Vision along with many other Azure AI services such as Azure AI Language, Azure AI Speech, and others. Use this resource type if you plan to use multiple Azure AI services and want to simplify administration and development.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
Character recognition with AI is a powerful tool that goes beyond mere automation; it opens up new possibilities for accessibility, communication, and knowledge preservation. As technology continues to advance, character recognition will likely become an integral part of various applications, enriching lives in unforeseen ways.

All right, it’s time for another exercise!
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Character Recognition and AI
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module2/recognizing-characters-text-poll.yaml" id="vc3qyv923he6klf6"/>
<br>
<edukamu-text-poll url="/exercises/module2/recognizing-characters-text-poll-2.yaml" id="pv186141b866ebj0"/>
<br>
<edukamu-text-poll url="/exercises/module2/recognizing-characters-text-poll-3.yaml" id="8spnwm8b51or273x"/>
<br>
<edukamu-text-poll url="/exercises/module2/recognizing-characters-text-poll-4.yaml" id="gg32evw5n39k0xy0"/>
<br>

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/2/recognizing-characters-with-ai?question=vc3qyv923he6klf6">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### YRITYS: Scenarios from Real Life
</edukamu-collapse-hidden-title>
Placeholder: Tähän tulee teksti, jossa kerrotaan tosielämän tilanteista.
</edukamu-collapse>
<br> -->

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
