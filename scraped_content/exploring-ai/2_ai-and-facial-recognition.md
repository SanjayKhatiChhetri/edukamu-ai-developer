## AI and Facial Recognition

Facial recognition is something the most of us might already have witnessed on our phones, tablets, or when crossing international borders. We’re talking about a sphere of AI in which machines not only see but recognize – a world where your face becomes a key.

This technology is, naturally, present in Microsoft Azure as well. Let’s dig in!

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Introduction to Facial Recognition
</edukamu-collapse-hidden-title>

Face detection and analysis is an area of artificial intelligence (AI) which uses algorithms to locate and analyze human faces in images or video content.

There are many applications for face detection, analysis, and recognition. For example,
* Security - facial recognition can be used in building security applications, and increasingly it is used in smart phones operating systems for unlocking devices.
* Social media - facial recognition can be used to automatically tag known friends in photographs.
* Intelligent monitoring - for example, an automobile might include a system that monitors the driver's face to determine if the driver is looking at the road, looking at a mobile device, or shows signs of tiredness.
* Advertising - analyzing faces in an image can help direct advertisements to an appropriate demographic audience.
* Missing persons - using public cameras systems, facial recognition can be used to identify if a missing person is in the image frame.
* Identity validation - useful at ports of entry kiosks where a person holds a special entry permit.

Facial recognition can be divided into two parts: **face detection** and **face analysis**.

Face detection involves identifying regions of an image that contain a human face, typically by returning *bounding box* coordinates that form a rectangle around the face, like this:

<edukamu-image url="/graphics/module2/face-detection.png" alt="An image with two faces highlighted in rectangles."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

With face analysis, facial features can be used to train machine learning models to return other information, such as facial features such as nose, eyes, eyebrows, lips, and others.

<edukamu-image url="/graphics/module2/landmarks-1.png" alt="Facial landmarks image showing data around face characteristics." style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px">
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 


### Combining the Two: Facial Recognition

A further application of facial analysis is to train a machine learning model to identify known individuals from their facial features. This is known as facial recognition, and uses multiple images of an individual to train the model. This trains the model so that it can detect those individuals in new images on which it wasn't trained.

<edukamu-image url="/graphics/module2/facial-recognition.png" alt="A person identified as “Wendell”"> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

When used responsibly, facial recognition is an important and useful technology that can improve efficiency, security, and customer experiences. Next we'll explore Azure AI Face service, which provides pre-trained models to detect, recognize, and analyze faces.

</edukamu-collapse>
<br>


Microsoft Azure provides multiple Azure AI services that you can use to detect and analyze faces, including:
* **Azure AI Vision**, which offers face detection and some basic face analysis, such as returning the bounding box coordinates around an image.
* **Azure AI Video Indexer**, which you can use to detect and identify faces in a video.
* **Azure AI Face**, which offers pre-built algorithms that can detect, recognize, and analyze faces.

Of these, Face offers the widest range of facial analysis capabilities.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure Face Service
</edukamu-collapse-hidden-title>

The Azure Face service can return the rectangle coordinates for any human faces that are found in an image, as well as a series of attributes related to those face such as:
* **Accessories**: indicates whether the given face has accessories. This attribute returns possible accessories including headwear, glasses, and mask, with confidence score between zero and one for each accessory.
* **Blur**: how blurred the face is, which can be an indication of how likely the face is to be the main focus of the image.
* **Exposure**: such as whether the image is underexposed or over exposed. This applies to the face in the image and not the overall image exposure.
* **Glasses**: whether or not the person is wearing glasses.
* **Head pose**: the face's orientation in a 3D space.
* **Mask**: indicates whether the face is wearing a mask.
* **Noise**: refers to visual noise in the image. If you have taken a photo with a high ISO setting for darker settings, you would notice this noise in the image. The image looks grainy or full of tiny dots that make the image less clear.
* **Occlusion**: determines if there might be objects blocking the face in the image.

Anyone can use the Face service to:
* Detect the location of faces in an image.
* Determine if a person is wearing glasses.
* Determine if there's occlusion, blur, noise, or over/under exposure for any of the faces.
* Return the head pose coordinates for each face in an image.

The Limited Access policy requires customers to [submit an intake form](https://aka.ms/facerecognition)(target="_blank") to access additional Azure AI Face service capabilities including:
* The ability to compare faces for similarity.
* The ability to identify named individuals in an image.

**Please notice** that, in order to use the Face service, you must create one of the following types of resource in your Azure subscription:
* **Face**: Use this specific resource type if you don't intend to use any other Azure AI services, or if you want to track utilization and costs for Face separately.
* **Azure AI services**: A general resource that includes Azure AI Face along with many other Azure AI services such as Azure AI Content Safety, Azure AI Language, and others. Use this resource type if you plan to use multiple Azure AI services and want to simplify administration and development.


### Tips for Accuracy

There are some considerations that can help improve the accuracy of the detection in the images:
* Image format - supported images are JPEG, PNG, GIF, and BMP.
* File size - 6 MB or smaller.
* Face size range - from 36 x 36 pixels up to 4096 x 4096 pixels. Smaller or larger faces will not be detected.
* Other issues - face detection can be impaired by extreme face angles, extreme lighting, and occlusion (objects blocking the face such as a hand).

</edukamu-collapse>
<br>


Facial recognition technology can greatly improve our everyday lives by making it easier to make transactions, confirm identities, and even reduce crime.

However, facial recognition also brings forth a host of ethical concerns, calling for careful consideration and responsible implementation. Let’s explore three of them, along with Microsoft’s efforts to address them.

<edukamu-tabs theme="edukamu-tabs1">

<edukamu-tabs-tab title="Concern 1: Privacy">
### Issue

Facial recognition can lead to unwarranted intrusions into personal privacy. The collection and storage of facial data raise concerns about unauthorized surveillance and potential misuse.

### Microsoft's Approach

Microsoft has taken a principled stand on privacy, advocating for the transparent and responsible use of facial recognition. They support the development of comprehensive privacy laws and guidelines to govern the use of this technology. Microsoft is committed to providing users with control over their data, ensuring transparency in data practices, and urging policymakers to establish clear regulations.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="Concern 2: Bias and Fairness">
### Issue

Facial recognition systems may exhibit biases, leading to inaccurate results, particularly for individuals from certain demographic groups. This raises concerns about fairness and the potential for discriminatory outcomes.

### Microsoft's Approach

Microsoft acknowledges the importance of addressing bias in facial recognition algorithms. Microsoft is committed to advancing research and development to reduce both glaring and subtle biases in these systems. Microsoft encourages third-party testing of facial recognition technology to ensure fairness and accuracy. Additionally, the company believes in giving customers the tools to understand, evaluate, and control these systems.
</edukamu-tabs-tab>

<edukamu-tabs-tab title="Concern 3: Human Rights">
### Issue

The use of facial recognition by governments for surveillance purposes raises concerns about potential violations of human rights, including freedom of speech and the right to privacy.

### Microsoft's Approach

Microsoft has advocated for government regulation to govern the use of facial recognition technology. They believe in clear guidelines that ensure the technology is used ethically, avoiding scenarios that infringe upon fundamental human rights. Microsoft has, in fact, called for a temporary ban on the use of facial recognition technology by government agencies until appropriate regulations are in place.

If you’re interested in exploring this topic further, feel free to get familiar with [Microsoft’s Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement)(target="_blank"). There, you’ll find detailed information on how Microsoft is ensuring the privacy and safety of every used – including Azure developers.
</edukamu-tabs-tab>

</edukamu-tabs>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Concern 1: Privacy
</edukamu-collapse-hidden-title>

## Issue

Facial recognition can lead to unwarranted intrusions into personal privacy. The collection and storage of facial data raise concerns about unauthorized surveillance and potential misuse.

## Microsoft's Approach

Microsoft has taken a principled stand on privacy, advocating for the transparent and responsible use of facial recognition. They support the development of comprehensive privacy laws and guidelines to govern the use of this technology. Microsoft is committed to providing users with control over their data, ensuring transparency in data practices, and urging policymakers to establish clear regulations.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Concern 2: Bias and Fairness
</edukamu-collapse-hidden-title>

## Issue

Facial recognition systems may exhibit biases, leading to inaccurate results, particularly for individuals from certain demographic groups. This raises concerns about fairness and the potential for discriminatory outcomes.

## Microsoft's Approach

Microsoft acknowledges the importance of addressing bias in facial recognition algorithms. Microsoft is committed to advancing research and development to reduce both glaring and subtle biases in these systems. Microsoft encourages third-party testing of facial recognition technology to ensure fairness and accuracy. Additionally, the company believes in giving customers the tools to understand, evaluate, and control these systems.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Concern 3: Human Rights
</edukamu-collapse-hidden-title>

## Issue

The use of facial recognition by governments for surveillance purposes raises concerns about potential violations of human rights, including freedom of speech and the right to privacy.

## Microsoft's Approach

Microsoft has advocated for government regulation to govern the use of facial recognition technology. They believe in clear guidelines that ensure the technology is used ethically, avoiding scenarios that infringe upon fundamental human rights. Microsoft has, in fact, called for a temporary ban on the use of facial recognition technology by government agencies until appropriate regulations are in place.

If you’re interested in exploring this topic further, feel free to get familiar with [Microsoft’s Privacy Statement](https://privacy.microsoft.com/en-us/privacystatement)(target="_blank"). There, you’ll find detailed information on how Microsoft is ensuring the privacy and safety of every used – including Azure developers.

</edukamu-collapse>
<br> -->

<edukamu-section class="slate-section slate-blue">
In summary, Microsoft recognizes both the various possibilities as well as the possible ethical challenges surrounding facial recognition and is actively working to address them through technological advancements, advocacy for privacy laws, and a commitment to fairness and transparency.

If you continue on your path towards mastering Microsoft Azure, you’ll surely get to work with facial recognition in the future.

Now, answer the following questions about facial recognition before moving on.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Facial Recognition
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/ai-and-facial-recognition-question-scroll.yaml" id="xz4i609z82aa631m">
<br>

</edukamu-collapse>
<br>


How do you, personally feel about facial recognition? Will it be used more in the future – and in what ways? Are you excited about the possibilities or worried about the risks? Maybe even both?

It’s always good to pause for a minute when exploring new technologies and just ponder your thoughts for a while. That will make you more capable of solving potential issues along the way.

On the next page, we’ll still focus on recognition, but we’ll leave faces aside for a moment.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
