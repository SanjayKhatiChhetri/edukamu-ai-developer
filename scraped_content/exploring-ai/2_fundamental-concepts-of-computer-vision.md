<edukamu-video content="/videos/devai-2-unit2-video.yaml"/>
<br>

## Fundamental Concepts of Computer Vision

Welcome to the second unit! In this unit, we'll explore an interesting concept within Azure, namely, Computer Vision. We're about to embark on a journey into the very heart of visual intelligence!

At its core, Computer Vision empowers machines to interpret and comprehend the visual world, mirroring the way humans perceive and understand images. It's the technological art of granting computers the ability to extract meaningful information from visual data.

From a technological perspective, computer vision is an area of artificial intelligence in which software systems are designed to perceive the world visually through cameras, images, and video. 

Before delving in, let's go through a practical example of how this technology can be used to enhance something the most of us do almost daily, shopping for groceries.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Computer Vision and Groceries
</edukamu-collapse-hidden-title>

Imagine strolling into a futuristic retail store in which traditional checkout hassles are no more. Thanks to Computer Vision, this is not just a fantasy but a reality.

1. **Automated Item Recognition**:
   * As you pick items from the shelf, overhead cameras equipped with Computer Vision identify each product through visual recognition.
   * No need to scan barcodes; the system effortlessly recognizes items based on their appearance.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 2;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Seamless Shopping Experience</span>:
</li>
</ol>
</edukamu-section>
* Toss your selected items into your bag, and the smart cart updates your digital tab.
* Computer Vision algorithms continuously analyze the contents of your cart in real-time.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 3;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Intelligent Payment Processing</span>:
</li>
</ol>
</edukamu-section>
* Ready to leave? No queues, no scanning. The store's payment system, powered by Computer Vision, effortlessly tallies your selections.
* The system ensures accuracy, even distinguishing between similar-looking products.

<edukamu-section class="styled-list-not-in-order">
<ol> 
<li style="counter-increment: any-name 4;"> <!--Merkataan any-namen perään numero mikä halutaan non-ordered listaan tähän kohtaan-->
<span style="font-weight: bold">Automated Receipt Generation</span>:
</li>
</ol>
</edukamu-section>
* Your purchase is complete. A digital receipt is instantly generated, detailing your items and the total cost.
* No more fumbling with paper receipts – everything is stored digitally.

<!-- 2. **Seamless Shopping Experience**:
  * Toss your selected items into your bag, and the smart cart updates your digital tab.
  * Computer Vision algorithms continuously analyze the contents of your cart in real-time.
3. **Intelligent Payment Processing**:
  * Ready to leave? No queues, no scanning. The store's payment system, powered by Computer Vision, effortlessly tallies your selections.
  * The system ensures accuracy, even distinguishing between similar-looking products.
4. **Automated Receipt Generation**:
  * Your purchase is complete. A digital receipt is instantly generated, detailing your items and the total cost.
  * No more fumbling with paper receipts – everything is stored digitally. -->

**Benefits**:
* **Efficiency**: Say goodbye to long queues. The streamlined process enhances the shopping experience, saving time for both customers and retailers.
* **Accuracy**: Computer Vision reduces the risk of errors in item identification and pricing, providing a highly accurate transaction process.
* **Personalized Offers**: The system, aware of your preferences, can offer personalized discounts and recommendations based on your shopping history. Similar technologies are, of course, largely used already across countless online marketplaces.

This is just one glimpse of how Computer Vision transforms mundane tasks into futuristic, hassle-free experiences. From retail to healthcare, manufacturing to entertainment, the applications of this exciting technology are reshaping the way we interact with the world.

</edukamu-collapse>
<br>


Computer vision is one of the core areas of artificial intelligence. As you’ve just learned, it focuses on creating solutions that enable AI applications to "see" the world and make sense of it.

Of course, computers don't have biological eyes that work the way ours do, but they're capable of processing images; either from a live camera feed or from digital photographs or videos. This ability to process images is the key to creating software that can emulate human visual perception.

We'll begin by connecting something we've already covered, namely machine learning, to computer vision. Shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Machine Learning and Computer Vision
</edukamu-collapse-hidden-title>

The ability to use filters to apply effects to images is useful in image processing tasks, such as you might perform with image editing software. However, the goal of computer vision is often to extract meaning, or at least actionable insights, from images; which requires the creation of machine learning models that are trained to recognize features based on large volumes of existing images.

The following materials might be challenging at this point. If this is the case, remember that you can always leave them aside for a while and circle back to this page at a later stage.

### Convolutional Neural Networks (CNNs)

One of the most common machine learning model architectures for computer vision is a *convolutional neural network* (CNN). CNNs use filters to extract numeric feature maps from images, and then feed the feature values into a deep learning model to generate a label prediction. For example, in an *image classification* scenario, the label represents the main subject of the image (in other words, what is this an image of?). You might train a CNN model with images of different kinds of fruit (such as apple, banana, and orange) so that the label that is predicted is the type of fruit in a given image.

During the *training* process for a CNN, filter kernels are initially defined using randomly generated weight values. Then, as the training process progresses, the models predictions are evaluated against known label values, and the filter weights are adjusted to improve accuracy. Eventually, the trained fruit image classification model uses the filter weights that best extract features that help identify different kinds of fruit.

The following diagram illustrates how a CNN for an image classification model works:

<edukamu-image url="/graphics/module2/convolutional-neural-network.png" alt="Diagram of a convolutional neural network."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Images with known labels (for example, 0: apple, 1: banana, or 2: orange) are fed into the network to train the model.

1. One or more layers of filters is used to extract features from each image as it is fed through the network. The filter kernels start with randomly assigned weights and generate arrays of numeric values called *feature maps*.
2. The feature maps are flattened into a single dimensional array of feature values.
3. The feature values are fed into a fully connected neural network.
4. The output layer of the neural network uses a *softmax* or similar function to produce a result that contains a probability value for each possible class, for example [0.2, 0.5, 0.3].

During training the output probabilities are compared to the actual class label - for example, an image of a banana (class 1) should have the value [0.0, 1.0, 0.0]. The difference between the predicted and actual class scores is used to calculate the *loss* in the model, and the weights in the fully connected neural network and the filter kernels in the feature extraction layers are modified to reduce the loss.

The training process repeats over multiple *epochs* until an optimal set of weights has been learned. Then, the weights are saved and the model can be used to predict labels for new images for which the label is unknown.


### Multi-modal Models (Microsoft Florence)

The success of transformers as a way to build language models has led AI researchers to consider whether the same approach would be effective for image data. The result is the development of *multi-modal* models, in which the model is trained using a large volume of captioned images, with no fixed *labels*.

In essence, an image encoder extracts features from images based on pixel values and combines them with text embeddings created by a language encoder. The overall model encapsulates relationships between natural language token embeddings and image features, as shown here:

<edukamu-image url="/graphics/module2/multi-modal-model.png" alt="Diagram of a multi-modal model that encapsulates relationships between natural language vectors and image features."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The Microsoft *Florence* model is just such a model. Trained with huge volumes of captioned images from the Internet, it includes both a language encoder and an image encoder. Florence is an example of a *foundation* model. In other words, a pre-trained general model on which you can build multiple *adaptive* models for specialist tasks. For example, you can use Florence as a foundation model for adaptive models that perform:
* *Image classification*: Identifying to which category an image belongs.
* *Object detection*: Locating individual objects within an image.
* *Captioning*: Generating appropriate descriptions of images.
* *Tagging*: Compiling a list of relevant text tags for an image.

<edukamu-image url="/graphics/module2/florence-model.png" alt="Diagram of a Florence model as a foundation model with multiple adaptive models built on it."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Multi-modal models like Florence are at the cutting edge of computer vision and AI in general, and are expected to drive advances in the kinds of solution that AI makes possible.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
As you continue on your path towards Azure expertise, seemingly complicated concepts such as the previous one will start to seem simpler and simpler. Maybe you'll suddenly think back to this moment one day in the future, as you're preparing your own *CNNs*...

Let's continue! In Azure, there's a neat service called Azure AI Vision. It's designed for making the machine learning process easier to grasp and employ.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure AI Vision
</edukamu-collapse-hidden-title>

While you can train your own machine learning models for computer vision, the architecture for computer vision models can be complex; and you require significant volumes of training images and compute power to perform the training process.

Microsoft's Azure AI Vision service provides prebuilt and customizable computer vision models that are based on the Florence foundation model and provide various powerful capabilities. With Azure AI Vision, you can create sophisticated computer vision solutions quickly and easily; taking advantage of "off-the-shelf" functionality for many common computer vision scenarios, while retaining the ability to create custom models using your own images.

To use Azure AI Vision, you need to create a resource for it in your Azure subscription. You can use either of the following resource types:
* **Azure AI Vision**: A specific resource for the Azure AI Vision service. Use this resource type if you don't intend to use any other Azure AI services, or if you want to track utilization and costs for your Azure AI Vision resource separately.
* **Azure AI services**: A general resource that includes Azure AI Vision along with many other Azure AI services; such as Azure AI Language, Azure AI Custom Vision, Azure AI Translator, and others. Use this resource type if you plan to use multiple AI services and want to simplify administration and development.

</edukamu-collapse>
<br>


With Azure AI Vision, you can easily activate prebuilt tools for various use cases. One of them is image analysis, which we'll spend some time exploring a bit later during this unit.

Azure AI Vision can be used for analyzing texts and recognizing characters, among other things.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure AI Vision and Image Analysis
</edukamu-collapse-hidden-title>

After you've created a suitable resource in your subscription, you can submit images to the Azure AI Vision service to perform a wide range of analytical tasks.

Azure AI Vision supports multiple various image analysis capabilities, including:
* Optical character recognition (OCR) - extracting text from images.
* Generating captions and descriptions of images.
* Detection of thousands of common objects in images.
* Tagging visual features in images.

Let's take a look into few common use cases for image analysis.


### 1. Optical Character Recognition

Azure AI Vision service can use optical character recognition (OCR) capabilities to detect text in images. For example, consider the following image of a nutrition label on a product in a grocery store:

<edukamu-image url="/graphics/module2/nutrition-label.png" alt="Image of a nutrition label."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The Azure AI Vision service can analyze this image and extract the following text:

>Nutrition Facts Amount Per Serving<br>
>Serving size: 1 bar (40g)<br>
>Serving Per Package: 4<br>
>Total Fat 13g<br>
>Saturated Fat 1.5g<br>
>Amount Per Serving<br>
>Trans Fat 0g<br>
>calories 190<br>
>Cholesterol 0mg<br>
>ories from Fat 110<br>
>Sodium 20mg<br>
>ntDaily Values are based on<br>
>Vitamin A 50<br>
>calorie diet<br>


### 2. Describing Images

Azure AI Vision has the ability to analyze an image, evaluate the objects that are detected, and generate a human-readable phrase or sentence that can describe what was detected in the image. For example, consider the following image:

<edukamu-image url="/graphics/module2/skateboard.png" alt="Image of a man on a skateboard."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Azure AI Vision returns the following caption for this image:

*A man jumping on a skateboard*


### 3. Detecting Common Objects

Azure AI Vision can identify thousands of common objects in images. For example, when used to detect objects in the skateboarder image discussed previously, Azure AI Vision returns the following predictions:
* *Skateboard (90.40%)*
* *Person (95.5%)*

The predictions include a confidence score that indicates the probability the model has calculated for the predicted objects.

In addition to the detected object labels and their probabilities, Azure AI Vision returns bounding box coordinates that indicate the top, left, width, and height of the object detected. You can use these coordinates to determine where in the image each object was detected, like this:

<edukamu-image url="/graphics/module2/bounding-boxes.png" alt="Diagram of a skateboarder with bounding boxes around detected objects."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 


### 4. Tagging Visual Features

Azure AI Vision can suggest tags for an image based on its contents. These tags can be associated with the image as metadata that summarizes attributes of the image and can be useful if you want to index an image along with a set of key terms that might be used to search for images with specific attributes or contents.

For example, the tags returned for the skateboarder image (with associated confidence scores) include:

* *sport (99.60%)*
* *person (99.56%)*
* *footwear (98.05%)*
* *skating (96.27%)*
* *boardsport (95.58%)*
* *skateboarding equipment (94.43%)*
* *clothing (94.02%)*
* *wall (93.81%)*
* *skateboarding (93.78%)*
* *skateboarder (93.25%)*
* *individual sports (92.80%)*
* *street stunts (90.81%)*
* *balance (90.81%)*
* *jumping (89.87%)*
* *sports equipment (88.61%)*
* *extreme sport (88.35%)*
* *kickflip (88.18%)*
* *stunt (87.27%)*
* *skateboard (86.87%)*
* *stunt performer (85.83%)*
* *knee (85.30%)*
* *sports (85.24%)*
* *longboard (84.61%)*
* *longboarding (84.45%)*
* *riding (73.37%)*
* *skate (67.27%)*
* *air (64.83%)*
* *young (63.29%)*
* *outdoor (61.39%)*

</edukamu-collapse>
<br>


Imagine: All of the above (and a lot more!) are available as prebuilt models. In essence, this means that all the hard work has already been done for you.

But what if you, some day, want to employ a model of your own? Maybe design something more specified? No problem!

Before getting into custom models, let’s briefly discover how Azure processes images! In short, they’re broken down into numbers and so-called pixel arrays, but what does this mean in practice?
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Image Processing in Azure
</edukamu-collapse-hidden-title>
Before we can explore image processing and other computer vision capabilities, it's useful to consider what an image actually is in the context of data for a computer program.


### Images as Pixel Arrays

To a computer, an image is an array of numeric pixel values. For example, consider the following array:

<edukamu-section class="edukamu-array-table">
|       |       |       |       |       |       |       |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   | 
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |
|   0   |   0   |  255  |  255  |  255  |   0   |   0   |
|   0   |   0   |  255  |  255  |  255  |   0   |   0   |
|   0   |   0   |  255  |  255  |  255  |   0   |   0   |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |
</edukamu-section>
<br>

<!-- <edukamu-section class="centered edukamu-border">

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;  255 255 255  0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;  255 255 255  0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;  255 255 255  0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

</edukamu-section>
<br> -->

The array consists of seven rows and seven columns, representing the pixel values for a 7x7 pixel image (which is known as the image's resolution). Each pixel has a value between 0 (black) and 255 (white); with values between these bounds representing shades of gray. The image represented by this array looks similar to the following (magnified) image:

<edukamu-image url="/graphics/module2/white-square.png" alt="Diagram of a grayscale image.">
<br>

The array of pixel values for this image is two-dimensional (representing rows and columns, or x and y coordinates) and defines a single rectangle of pixel values. 

A single layer of pixel values like this represents a grayscale image. In reality, most digital images are multidimensional and consist of three layers (known as channels) that represent red, green, and blue (RGB) color hues. 

For example, we could represent a color image by defining three channels of pixel values that create the same square shape as the previous grayscale example:


Red:
<edukamu-section class="edukamu-array-table">
|       |       |       |       |       |       |       |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  150  |  150  |  150  |  150  |  150  |  150  |  150  | 
|  150  |  150  |  150  |  150  |  150  |  150  |  150  |
|  150  |  150  |  255  |  255  |  255  |  150  |  150  |
|  150  |  150  |  255  |  255  |  255  |  150  |  150  |
|  150  |  150  |  255  |  255  |  255  |  150  |  150  |
|  150  |  150  |  150  |  150  |  150  |  150  |  150  |
|  150  |  150  |  150  |  150  |  150  |  150  |  150  |
</edukamu-section>
<br>

<!-- <edukamu-section class="centered edukamu-border">

 150&nbsp;&nbsp;   150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   150&nbsp;&nbsp;   150&nbsp;&nbsp; 

 150&nbsp;&nbsp;   150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   150&nbsp;&nbsp;   150&nbsp;&nbsp; 

 150&nbsp;&nbsp;   150&nbsp;&nbsp;   &nbsp;&nbsp;255   &nbsp;&nbsp;255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp; 

 150&nbsp;&nbsp;   150&nbsp;&nbsp;   &nbsp;&nbsp;255   &nbsp;&nbsp;255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp; 

 150&nbsp;&nbsp;   150&nbsp;&nbsp;   &nbsp;&nbsp;255   &nbsp;&nbsp;255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp; 

 150&nbsp;&nbsp;   150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   150&nbsp;&nbsp;   150&nbsp;&nbsp; 

 150&nbsp;&nbsp;   150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   &nbsp;&nbsp;150&nbsp;&nbsp;   150&nbsp;&nbsp;   150&nbsp;&nbsp; 

</edukamu-section>
<br> -->

Green:
<edukamu-section class="edukamu-array-table">
|       |       |       |       |       |       |       |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   | 
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |
|   0   |   0   |  255  |  255  |  255  |   0   |   0   |
|   0   |   0   |  255  |  255  |  255  |   0   |   0   |
|   0   |   0   |  255  |  255  |  255  |   0   |   0   |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |
</edukamu-section>
<br>

<!-- <edukamu-section class="centered edukamu-border">

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp; 

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   255  255  255   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   255  255  255   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   255  255  255   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

</edukamu-section>
<br> -->

Blue:
<edukamu-section class="edukamu-array-table">
|       |       |       |       |       |       |       |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|  255  |  255  |  255  |  255  |  255  |  255  |  255  |
|  255  |  255  |  255  |  255  |  255  |  255  |  255  |
|  255  |  255  |   0   |   0   |   0   |  255  |  255  |
|  255  |  255  |   0   |   0   |   0   |  255  |  255  |
|  255  |  255  |   0   |   0   |   0   |  255  |  255  |
|  255  |  255  |  255  |  255  |  255  |  255  |  255  |
|  255  |  255  |  255  |  255  |  255  |  255  |  255  |
</edukamu-section>
<br>

<!-- <edukamu-section class="centered edukamu-border">

 255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   255&nbsp;&nbsp;   255&nbsp;&nbsp;

 255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   255&nbsp;&nbsp;   255&nbsp;&nbsp;

 255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;

 255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;

 255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;

 255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   255&nbsp;&nbsp;   255&nbsp;&nbsp;

 255&nbsp;&nbsp;   255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   &nbsp;&nbsp;255&nbsp;&nbsp;   255&nbsp;&nbsp;   255&nbsp;&nbsp;

</edukamu-section>
<br> -->

Here's the resulting image:
<edukamu-image url="/graphics/module2/color-square.png" alt="Diagram of a colour image.">
<br>

The purple squares are represented by the combination:

*Red: 150*<br> 
*Green: 0*<br> 
*Blue: 255*<br> 

The yellow squares in the center are represented by the combination:<br>
*Red: 255*<br>
*Green: 255*<br>
*Blue: 0*<br>


### Filters and Image Processing

A common way to perform image processing tasks is to apply filters that modify the pixel values of the image to create a visual effect. A filter is defined by one or more arrays of pixel values, called filter *kernels*. 

For example, you could define filter with a 3x3 kernel as shown in this example:

-1 -1 -1<br>
-1  8 -1<br>
-1 -1 -1<br>

The kernel is then *convolved* across the image, calculating a weighted sum for each 3x3 patch of pixels and assigning the result to a new image. It's easier to understand how the filtering works by exploring a step-by-step example.

Let's start with the grayscale image we explored previously:

<edukamu-section class="edukamu-array-table">
|       |       |       |       |       |       |       |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   | 
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |
|   0   |   0   |  255  |  255  |  255  |   0   |   0   |
|   0   |   0   |  255  |  255  |  255  |   0   |   0   |
|   0   |   0   |  255  |  255  |  255  |   0   |   0   |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |
|   0   |   0   |   0   |   0   |   0   |   0   |   0   |
</edukamu-section>
<br>

<!-- <edukamu-section class="centered edukamu-border">

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;  

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;  255 255 255  0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;  255 255 255  0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;  255 255 255  0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 0&nbsp;&nbsp;   0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   &nbsp;&nbsp;0&nbsp;&nbsp;   0&nbsp;&nbsp;   0&nbsp;&nbsp;

 </edukamu-section>
 <br> -->


First, we apply the filter kernel to the top left patch of the image, multiplying each pixel value by the corresponding weight value in the kernel and adding the results:

(0 x -1) + (0 x -1) + (0 x -1) +<br>
(0 x -1) + (0 x 8) + (0 x -1) +<br>
(0 x -1) + (0 x -1) + (255 x -1) = -255<br>

The result (-255) becomes the first value in a new array. Then we move the filter kernel along one pixel to the right and repeat the operation:

(0 x -1) + (0 x -1) + (0 x -1) +<br>
(0 x -1) + (0 x 8) + (0 x -1) +<br>
(0 x -1) + (255 x -1) + (255 x -1) = -510<br>

Again, the result is added to the new array, which now contains two values:

-255  -510

The process is repeated until the filter has been convolved across the entire image, as shown in this animation:

<edukamu-image url="/graphics/module2/filter.gif" alt="Diagram of a filter.">
<br>

The filter is convolved across the image, calculating a new array of values. Some of the values might be outside of the 0 to 255 pixel value range, so the values are adjusted to fit into that range. 

Because of the shape of the filter, the outside edge of pixels isn't calculated, so a padding value (usually 0) is applied. The resulting array represents a new image in which the filter has transformed the original image. 

In this case, the filter has had the effect of highlighting the edges of shapes in the image.

To see the effect of the filter more clearly, here's an example of the same filter applied to a real image:

<edukamu-image url="/graphics/module2/ori-fil.png" alt="Diagram of a banana and a filtered banana.">
<br>

Because the filter is convolved across the image, this kind of image manipulation is often referred to as *convolutional filtering*. 

The filter used in this example is a particular type of filter (called a *laplace filter*) that highlights the edges on objects in an image. 

There are many other kinds of filter that you can use to create blurring, sharpening, color inversion, and other effects. If you have the time, feel free to explore them on your own!

</edukamu-collapse>


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Custom Models in Azure AI Vision
</edukamu-collapse-hidden-title>

If the built-in models provided by Azure AI Vision don't meet your needs, you can use the service to train a custom model for *image classification or object detection*. Azure AI Vision builds custom models on the pre-trained foundation model, meaning that you can train sophisticated models by using relatively few training images.

### Image classification

An image classification model is used to predict the category, or class of an image. For example, you could train a model to determine which type of fruit is shown in an image, like an apple, banana, or an orange.

Later, you could design an object detection model.

Object detection models detect and classify objects in an image, returning bounding box coordinates to locate each object. In addition to the built-in object detection capabilities in Azure AI Vision, you can train a custom object detection model with your own images. For example, you could use photographs of fruit to train a model that detects multiple fruits in an image, like this:

<edukamu-image url="/graphics/module2/object-detection-2.png" alt="Diagram of multiple detected fruits in an image."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

There's an endless ocean of opportunities just waiting to be discovered in Azure AI Vision. And that's just the tip of the iceberg, as you'll soon see.

</edukamu-collapse>
<br>


Computer vision enables machines to see the world as we humans do and, in turn, interact with us more naturally. They can’t perceive surroundings exactly like us, of course, since they’re machines, after all. This isn’t necessarily a bad thing, though, since it means they’re not bound by the same limitations that we face on a daily basis…

All right, it’s time to summarize our new knowledge with an exercise!


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Introduction to Computer Vision
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module2/fundamental-concepts-question-scroll.yaml" id="x3ma96p8i9d9f2w5">
<br>

</edukamu-collapse>
<br>


Computer vision is one of those AI technologies that are already changing the world, whether we notice it or not. There's a lot left to cover, though, so let's keep on moving.

Next up is a topic that can be quite controversial. We're talking about facial recognition.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-3mod-progress1.png" alt="Edukamu-progress-in-a-module-image">
