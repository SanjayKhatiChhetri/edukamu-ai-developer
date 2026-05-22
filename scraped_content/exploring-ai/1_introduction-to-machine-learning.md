## Introduction to Machine Learning

As you learned before, machine learning is all about, you know it, machines learning. In practice, the process is a lot more interesting and multi-faceted than that.

Machine learning is already used across a variety of cases. Picture a scenario in which medical professionals harness the power of machine learning algorithms to analyze vast datasets of patient records, genetic information, and diagnostic images. In this real-world application, capable of saving lives, machine learning aids in identifying subtle patterns and correlations that might elude the human eye.

Machines can be taught to not replace humans but to empower them to reach goals and complete tasks that were thought impossible just a while ago. 

Let's dig deeper, shall we?

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Origins of Machine Learning
</edukamu-collapse-hidden-title>

Machine learning has its origins in statistics and mathematical modeling of data. The fundamental idea of machine learning is to use data from past observations to predict unknown outcomes or values. For example:

* The proprietor of an ice cream store might use an app that combines historical sales and weather records to predict how many ice creams they're likely to sell on a given day, based on the weather forecast.
* A doctor might use clinical data from past patients to run automated tests that predict whether a new patient is at risk from diabetes based on factors like weight, blood glucose level, and other measurements.
* A researcher in the Antarctic might use past observations automate the identification of different penguin species (such as Adelie, Gentoo, or Chinstrap) based on measurements of a bird's flippers, bill, and other physical attributes.

Because machine learning is based on mathematics and statistics, it's common to think about machine learning models in mathematical terms. Fundamentally, a machine learning model is a software application that encapsulates a *function* to calculate an output value based on one or more input values. The process of defining that function is known as *training*. After the function has been defined, you can use it to predict new values in a process called *inferencing*.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Interfencing in Action
</edukamu-collapse-hidden-title>

At its core, machine learning is all about mathematics, as you've just learned. Let's review an example of these calculations in practice.

First, take a look at the following picture and then explore the information below. Take your time, it's fundamental to understand the basics!

<edukamu-image url="/graphics/module1/machine-learning.png" alt="Diagram showing the training and inferencing phases in machine learning."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The training data consists of past observations. In most cases, the observations include the observed attributes or *features* of the thing being observed, and the known value of the thing you want to train a model to predict (known as the *label*).

In mathematical terms, you'll often see the features referred to using the shorthand variable name **x**, and the label referred to as **y**. Usually, an observation consists of multiple feature values, so **x** is actually a *vector* (an array with multiple values), like this: **[x1,x2,x3,...]**.

To make this clearer, let's consider the examples described previously:
* In the ice cream sales scenario, our goal is to train a model that can predict the number of ice cream sales based on the weather. The weather measurements for the day (temperature, rainfall, windspeed, and so on) would be the *features* (**x**), and the number of ice creams sold on each day would be the *label* (**y**).
* In the medical scenario, the goal is to predict whether or not a patient is at risk of diabetes based on their clinical measurements. The patient's measurements (weight, blood glucose level, and so on) are the *features* (**x**), and the likelihood of diabetes (for example, *1* for at risk, *0* for not at risk) is the *label* (**y**).
* In the Antarctic research scenario, we want to predict the species of a penguin based on its physical attributes. The key measurements of the penguin (length of its flippers, width of its bill, and so on) are the *features* (**x**), and the species (for example, *0* for Adelie, *1* for Gentoo, or 2 for Chinstrap) is the *label* (**y**).
2.	An *algorithm* is applied to the data to try to determine a relationship between the features and the label, and generalize that relationship as a calculation that can be performed on **x** to calculate **y**. The specific algorithm used depends on the kind of predictive problem you're trying to solve (more about this later), but the basic principle is to try to *fit* the data to a function in which the values of the features can be used to calculate the label.
3.	The result of the algorithm is a *model* that encapsulates the calculation derived by the algorithm as a *function* - let's call it **f**. In mathematical notation: **y = f(x)**
4.	Now that the *training* phase is complete, the trained model can be used for *inferencing*. The model is essentially a software program that encapsulates the function produced by the training process. You can input a set of feature values, and receive as an output a prediction of the corresponding label. Because the output from the model is a prediction that was calculated by the function, and not an observed value, you'll often see the output from the function shown as **ŷ** (which is rather delightfully verbalized as "y-hat").

Let's consider a few real-life examples to broaden our understanding of the basic mathematical concepts behind machine learning.

* In predicting ice cream sales based on weather, the weather measurements (temperature, rainfall, etc.) are features (x), and the number of ice creams sold is the label (y).
* In a medical scenario, patient measurements (weight, blood glucose) are features (x), and the likelihood of diabetes (1 for at risk, 0 for not at risk) is the label (y).
* In Antarctic research, penguin measurements (flipper length, bill width) are features (x), and the penguin species is the label (y).

In short: During training, an algorithm determines a relationship between features and labels, creating a model represented by a function: y = f(x). The model encapsulates the learned calculation.

In the inferencing phase, the trained model acts as a software program, taking feature values as input and providing predictions of corresponding labels as output. In the examples above, the prediction is often denoted as ŷ, symbolizing that it's a calculated prediction, not an observed value.

This process allows the model to generalize and make predictions on new, unseen data based on its learning from the training phase.

</edukamu-collapse>
<br>


There are multiple types of machine learning, and you must apply the appropriate type depending on what you're trying to predict. A breakdown of common types of machine learning is shown in the following diagram.

<edukamu-image url="/graphics/module1/machine-learning-types.png" alt="Diagram showing supervised machine learning (regression and classification) and unsupervised machine learning (clustering)."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

As you see, machine learning can be divided into two main categories, namely supervised and unsupervised learning. We'll spend a while exploring both in a while, so let's begin with an introduction.

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Supervised Machine Learning
</edukamu-collapse-hidden-title>

*Supervised* machine learning is a general term for machine learning algorithms in which the training data includes both *feature* values and known *label* values. Supervised machine learning is used to train models by determining a relationship between the features and labels in past observations, so that unknown labels can be predicted for features in future cases.

### Regression

*Regression* is a form of supervised machine learning in which the label predicted by the model is a numeric value. For example:
* The number of ice creams sold on a given day, based on the temperature, rainfall, and wind speed.
* The selling price of a property based on its size in square feet, the number of bedrooms it contains, and socio-economic metrics for its location.
* The fuel efficiency (in miles-per-gallon) of a car based on its engine size, weight, width, height, and length.

### Classification

*Classification* is a form of supervised machine learning in which the label represents a categorization, or *class*. There are two common classification scenarios.

#### 1. Binary Classification

In *binary classification*, the label determines whether the observed item is (or *isn't*) an instance of a specific class. Or put another way, binary classification models predict one of two mutually exclusive outcomes. For example:
* Whether a patient is at risk for diabetes based on clinical metrics like weight, age, blood glucose level, and so on.
* Whether a bank customer will default on a loan based on income, credit history, age, and other factors.
* Whether a mailing list customer will respond positively to a marketing offer based on demographic attributes and past purchases.

In all of these examples, the model predicts a binary *true/false* or *positive/negative* prediction for a single possible class.

#### 2. Multiclass Classification

*Multiclass classification* extends binary classification to predict a label that represents one of multiple possible classes. For example,
* The species of a penguin (*Adelie*, *Gentoo*, or *Chinstrap*) based on its physical measurements.
* The genre of a movie (*comedy*, *horror*, *romance*, *adventure*, or *science fiction*) based on its cast, director, and budget.

In most scenarios that involve a known set of multiple classes, multiclass classification is used to predict mutually exclusive labels. For example, a penguin can't be both a *Gentoo* and an *Adelie*. However, there are also some algorithms that you can use to train *multilabel* classification models, in which there may be more than one valid label for a single observation. For example, a movie could potentially be categorized as both *science fiction* and *comedy*.

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### Unsupervised Machine Learning
</edukamu-collapse-hidden-title>

*Unsupervised* machine learning involves training models using data that consists only of feature values without any known labels. Unsupervised machine learning algorithms determine relationships between the features of the observations in the training data.

### Clustering

The most common form of unsupervised machine learning is *clustering*. A clustering algorithm identifies similarities between observations based on their features, and groups them into discrete clusters. For example:
* Group similar flowers based on their size, number of leaves, and number of petals.
* Identify groups of similar customers based on demographic attributes and purchasing behavior.

In some ways, clustering is similar to multiclass classification; in that it categorizes observations into discrete groups. The difference is that when using classification, you already know the classes to which the observations in the training data belong; so, the algorithm works by determining the relationship between the features and the known classification label. In clustering, there's no previously known cluster label and the algorithm groups the data observations based purely on similarity of features.

In some cases, clustering is used to determine the set of classes that exist before training a classification model. For example, you might use clustering to segment your customers into groups, and then analyze those groups to identify and categorize different classes of customer (*high value* - *low volume*, *frequent small purchaser*, and so on). You could then use your categorizations to label the observations in your clustering results and use the labeled data to train a classification model that predicts to which customer category a new customer might belong.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
That, in a nutshell, is machine learning. After this short introduction, we'll start exploring this topic a bit further, starting with supervised learning.

Not so fast, though. Complete the next exercise before moving on.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Machine Learning Basics
</edukamu-collapse-hidden-title>

<edukamu-question-scroll url="/exercises/module1/intro-to-ml-question-scroll.yaml" id="79n43dofu449mhk1">
<br>

</edukamu-collapse>
<br>

<!-- <edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### YRITYKSEN NIMI: Career in the World of AI
</edukamu-collapse-hidden-title>

Hello, future data professional! At YRITYS, we work with services like Microsoft Azure every day, solving problems and improving the business of our clients and customers.

Microsoft Azure is among the best platforms to develop the AI solutions that shape our future, and in the world of AI, there are roles available for everyone!

On the following video, Nimi Niminen, Ammattinimike at Yritys talks about his/her job and career in this fascinating world.

VIDEO

If you’re interested in working with us, you can share your details with us after reaching the end of the course! Now, do your best on the course!

</edukamu-collapse>
<br> -->


Keep in mind that you should take pauses to relax and recap every once in a while, since you'll need a strong basis on which to build. This is especially true if you're planning to complete the entire micro degree, which we highly recommend!

Next up, supervised learning!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2.png" alt="Edukamu-progress-in-a-module-image">
