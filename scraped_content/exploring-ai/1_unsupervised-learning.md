## Unsupervised Learning

Once again, close your eyes for a while and return to the world in which tangible, three-dimensional algorithms roam free... It kind of feels like you've just been here, doesn't it?

But something is different. The world you imagined before was *supervised*. In this new world, many things are similar, but the underlying nature of things is very different.

The algorithms still wander around, but there's a notable difference. Unlike their supervised counterparts, with mentors and labeled datasets, these algorithms are pioneers exploring the uncharted territories of the unknown by themselves. Welcome to the dimension of unsupervised learning!

Unsupervised learning is akin to a solo expedition into the wilderness of data. Even this expedition not without rules or patterns, though. Let's dig in to 1) clustering and 2) deep learning.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Clustering
</edukamu-collapse-hidden-title>

Clustering is a form of unsupervised machine learning in which observations are grouped into clusters based on similarities in their data values, or features. This kind of machine learning is considered unsupervised because it doesn't make use of previously known label values to train a model. In a clustering model, the label is the cluster to which the observation is assigned, based only on its features.

### Example: Clustering

For example, suppose a botanist observes a sample of flowers and records the number of leaves and petals on each flower:

<edukamu-image url="/graphics/module1/flowers.png" alt="Diagram of some flowers."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

There are no known labels in the dataset, just two features. The goal is not to identify the different types (species) of flower; just to group similar flowers together based on the number of leaves and petals.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="30%">
Leaves (x1)
</edukamu-table-header>
<edukamu-table-header width="70%">
Petals (x2)
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
0
</edukamu-table-cell>
<edukamu-table-cell >
5
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
0
</edukamu-table-cell>
<edukamu-table-cell >
6
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
1
</edukamu-table-cell>
<edukamu-table-cell >
3
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
1
</edukamu-table-cell>
<edukamu-table-cell >
3
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
1
</edukamu-table-cell>
<edukamu-table-cell >
6
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
1
</edukamu-table-cell>
<edukamu-table-cell >
8
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
2
</edukamu-table-cell>
<edukamu-table-cell >
3
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
2
</edukamu-table-cell>
<edukamu-table-cell >
7
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
2
</edukamu-table-cell>
<edukamu-table-cell >
8
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

There are multiple algorithms you can use for clustering. One of the most commonly used algorithms is *K-Means* clustering, which consists of the following steps:

1. The feature (**x**) values are vectorized to define *n*-dimensional coordinates (where *n* is the number of features). In the flower example, we have two features: number of leaves (**x1**) and number of petals (**x2**). So, the feature vector has two coordinates that we can use to conceptually plot the data points in two-dimensional space (**[x1,x2]**).
2. You decide how many clusters you want to use to group the flowers - call this value *k*. For example, to create three clusters, you would use a *k* value of 3. Then k points are plotted at random coordinates. These points become the center points for each cluster, so they're called *centroids*.
3. Each data point (in this case a flower) is assigned to its nearest centroid.
4. Each centroid is moved to the center of the data points assigned to it based on the mean distance between the points.
5. After the centroid is moved, the data points may now be closer to a different centroid, so the data points are reassigned to clusters based on the new closest centroid.
6. The centroid movement and cluster reallocation steps are repeated until the clusters become stable or a predetermined maximum number of iterations is reached.

The following animation shows this process:

<edukamu-image url="/graphics/module1/clustering.gif" alt="Diagram of an animation showing the k-means clustering process."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

### Evaluating a Clustering Model

Since there's no known label with which to compare the predicted cluster assignments, evaluation of a clustering model is based on how well the resulting clusters are separated from one another.

There are multiple metrics that you can use to evaluate cluster separation, including:
* **Average distance to cluster center**: How close, on average, each point in the cluster is to the centroid of the cluster.
* **Average distance to other center**: How close, on average, each point in the cluster is to the centroid of all other clusters.
* **Maximum distance to cluster center**: The furthest distance between a point in the cluster and its centroid.
* **Silhouette**: A value between -1 and 1 that summarizes the ratio of distance between points in the same cluster and points in different clusters (The closer to 1, the better the cluster separation).

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Deep Learning
</edukamu-collapse-hidden-title>

*Deep learning* is an advanced form of machine learning that tries to emulate the way the human brain learns. The key to deep learning is the creation of an artificial *neural network* that simulates electrochemical activity in biological neurons by using mathematical functions, as shown here.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="50%">
Biological neural network
</edukamu-table-header>
<edukamu-table-header width="50%">
Artificial neural network
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
Neurons fire in response to electrochemical stimuli. When fired, the signal is passed to connected neurons.
</edukamu-table-cell>
<edukamu-table-cell >
Each neuron is a function that operates on an input value (**x**) and a *weight* (**w**). The function is wrapped in an activation function that determines whether to pass the output on.
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

Artificial neural networks are made up of multiple layers of neurons - essentially defining a deeply nested function. This architecture is the reason the technique is referred to as deep learning and the models produced by it are often referred to as deep neural networks (DNNs). You can use deep neural networks for many kinds of machine learning problem, including regression and classification, as well as more specialized models for natural language processing and computer vision.

Just like other machine learning techniques discussed here, deep learning involves fitting training data to a function that can predict a label (y) based on the value of one or more features (x). The function (f(x)) is the outer layer of a nested function in which each layer of the neural network encapsulates functions that operate on x and the weight (w) values associated with them. 

The algorithm used to train the model involves iteratively feeding the feature values (x) in the training data forward through the layers to calculate output values for ŷ, validating the model to evaluate how far off the calculated ŷ values are from the known y values (which quantifies the level of error, or loss, in the model), and then modifying the weights (w) to reduce the loss. The trained model includes the final weight values that result in the most accurate predictions.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Deep Learning and Classification
</edukamu-collapse-hidden-title>

To better understand how a deep neural network model works, let's explore an example in which a neural network is used to define a classification model for penguin species.

<edukamu-image url="/graphics/module1/deep-classification.png" alt="Diagram of a neural network used to classify a penguin species."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The feature data (**x**) consists of some measurements of a penguin. Specifically, the measurements are:
* The length of the penguin's bill.
* The depth of the penguin's bill.
* The length of the penguin's flippers.
* The penguin's weight.

In this case, **x** is a vector of four values, or mathematically, **x=[x1,x2,x3,x4]**.

The label we're trying to predict (y) is the species of the penguin, and that there are three possible species it could be:
* Adelie
* Gentoo
* Chinstrap

This is an example of a classification problem, in which the machine learning model must predict the most probable class to which an observation belongs. A classification model accomplishes this by predicting a label that consists of the probability for each class. In other words, y is a vector of three probability values; one for each of the possible classes: **[P(y=0|x), P(y=1|x), P(y=2|x)]**.

The process for inferencing a predicted penguin class using this network is:

1.	The feature vector for a penguin observation is fed into the input layer of the neural network, which consists of a neuron for each x value. In this example, the following **x** vector is used as the input: **[37.3, 16.8, 19.2, 30.0]**
2.	The functions for the first layer of neurons each calculate a weighted sum by combining the **x** value and **w** weight, and pass it to an activation function that determines if it meets the threshold to be passed on to the next layer.
3.	Each neuron in a layer is connected to all of the neurons in the next layer (an architecture sometimes called a *fully connected network*) so the results of each layer are fed forward through the network until they reach the output layer.
4.	The output layer produces a vector of values; in this case, using a *softmax* or similar function to calculate the probability distribution for the three possible classes of penguin. In this example, the output vector is: **[0.2, 0.7, 0.1]**
5.	The elements of the vector represent the probabilities for classes 0, 1, and 2. The second value is the highest, so the model predicts that the species of the penguin is **1** (Gentoo).


### Neural Networks and Learning

The weights in a neural network are central to how it calculates predicted values for labels. During the training process, the model learns the weights that will result in the most accurate predictions. Let's explore the training process in a little more detail to understand how this learning takes place.

Let's start with a picture and then explore it further.

<edukamu-image url="/graphics/module1/neural-network-training.png" alt="Diagram of a neural network being trained, evaluated, and optimized."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The training and validation datasets are defined, and the training features are fed into the input layer.
1. The neurons in each layer of the network apply their weights (which are initially assigned randomly) and feed the data through the network.
2. The output layer produces a vector containing the calculated values for **ŷ**. For example, an output for a penguin class prediction might be **[0.3. 0.1. 0.6]**.
3. A *loss function* is used to compare the predicted **ŷ** values to the known y values and aggregate the difference (which is known as the *loss*). For example, if the known class for the case that returned the output in the previous step is *Chinstrap*, then the **y** value should be **[0.0, 0.0, 1.0]**. The absolute difference between this and the **ŷ** vector is **[0.3, 0.1, 0.4]**. In reality, the loss function calculates the aggregate variance for multiple cases and summarizes it as a single *loss* value.
4. Since the entire network is essentially one large nested function, an optimization function can use differential calculus to evaluate the influence of each weight in the network on the loss, and determine how they could be adjusted (up or down) to reduce the amount of overall loss. The specific optimization technique can vary, but usually involves a *gradient descent* approach in which each weight is increased or decreased to minimize the loss.
5. The changes to the weights are *backpropagated* to the layers in the network, replacing the previously used values.
6. The process is repeated over multiple iterations (known as *epochs*) until the loss is minimized and the model predicts acceptably accurately.

While it's easier to think of each case in the training data being passed through the network one at a time, in reality the data is batched into matrices and processed using linear algebraic calculations. For this reason, neural network training is best performed on computers with graphical processing units (GPUs) that are optimized for vector and matrix manipulation.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
How does it seem? Are you beginning to understand the differences between supervised and unsupervised learning?

Without supervised learning's structured guidance, unsupervised learning is an adventure into the unexplored, where algorithms forge their own path through the data wilderness, revealing insights that might have remained hidden otherwise.

After this little adventure into the world of unsupervised learning, completing the exercise below shouldn't be a problem.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Unsupervised Learning
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/unsupervised-learning-question-scroll.yaml" id="3u31261x5fr38t28">
<br>

</edukamu-collapse>
<br>



All clear? Sweet! Before moving on, there's one more thing left to cover.

As this micro degree revolves around Microsoft Azure, let's spend a while learning about the ways in which machine learning is present within the platform.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Azure and Machine Learning
</edukamu-collapse-hidden-title>

There's an entire service within Azure that's designed with machine learning in mind. The service is, logically, called Microsoft Azure Machine Learning. It operates in the cloud, which makes it available for basically anyone interested in the technology.

Microsoft Azure Machine Learning is a cloud service for training, deploying, and managing machine learning models. It's designed to be used by data scientists, software engineers, and other professionals to manage the end-to-end lifecycle of machine learning projects, including:
* Exploring data and preparing it for modeling.
* Training and evaluating machine learning models.
* Registering and managing trained models.
* Deploying trained models for use by applications and services.
* Reviewing and applying responsible AI principles and practices.

### Features and Capabilities

Azure Machine Learning provides the following features and capabilities to support machine learning workloads:
* Centralized storage and management of datasets for model training and evaluation.
* On-demand compute resources on which you can run machine learning jobs, such as training a model.
* Automated machine learning (AutoML), which makes it easy to run multiple training jobs with different algorithms and parameters to find the best model for your data.
* Visual tools to define orchestrated *pipelines* for processes such as model training or inferencing.
* Integration with common machine learning frameworks such as MLflow, which make it easier to manage model training, evaluation, and deployment at scale.
* Built-in support for visualizing and evaluating metrics for responsible AI, including model explainability, fairness assessment, and others.

If you ever get to work with Microsoft Azure and artificial intelligence, you'll most certainly get very familiar with machine learning.

</edukamu-collapse>
<br>


All right, let's move on! 

Next, we'll take a little more comprehensive look at how Microsoft Azure is enhanced by features leveraging AI capabilities.

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3-4.png" alt="Edukamu-progress-in-a-module-image">
