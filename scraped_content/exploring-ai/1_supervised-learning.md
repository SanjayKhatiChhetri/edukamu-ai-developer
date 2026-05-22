## Supervised Learning

Let's pause for a while and picture a world inhabited by algorithms. In fact, it's not that different from our own world, but the algorithms are visible and tangible – not just series of written code. The algorithms are moving around seemingly randomly, but once you follow them for a while, you begin to notice something...

The algorithms are not just wandering aimlessly. Instead, they have a mentor, someone to guide them: a dataset that holds the secrets of the past. In practice, supervised learning is very much like this.

As a real-life example of supervised learning, let's consider a spam email filter. In this scenario, the algorithm is trained on a dataset of emails labeled as either "spam" or "not spam." The input features could include the content, sender, and other email attributes, while the output labels indicate whether each email is spam or not. Through this training process, the algorithm learns to recognize patterns associated with spam emails and can then accurately classify new, unseen emails in the future.

In practice, machine learning is of course more complicated than the example above, but many of its prevalent use cases are not that difficult to grasp, as we’ll soon discover.

Next, let's delve deeper into supervised learning. We'll focus on three core aspects: 1) regression, 2) binary classification, and 3) multiclass classification.


<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 1. Regression
</edukamu-collapse-hidden-title>

Regression models are trained to predict numeric label values based on training data that includes both features and known labels. The process for training a regression model (or indeed, any supervised machine learning model) involves multiple iterations in which you use an appropriate algorithm (usually with some parameterized settings) to train a model, evaluate the model's predictive performance, and refine the model by repeating the training process with different algorithms and parameters until you achieve an acceptable level of predictive accuracy.

<edukamu-image url="/graphics/module1/supervised-training.png" alt="Diagram showing the process of training an evaluating a supervised model."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The diagram above shows four key elements of the training process for supervised machine learning models:
1. Split the training data (randomly) to create a dataset with which to train the model while holding back a subset of the data that you'll use to validate the trained model.
2. Use an algorithm to fit the training data to a model. In the case of a regression model, use a regression algorithm such as *linear regression*.
3. Use the validation data you held back to test the model by predicting labels for the features.
4. Compare the known *actual* labels in the validation dataset to the labels that the model predicted. Then aggregate the differences between the *predicted* and *actual* label values to calculate a metric that indicates how accurately the model predicted for the validation data.

After each train, validate, and evaluate iteration, you can repeat the process with different algorithms and parameters until an acceptable evaluation metric is achieved.

### Example: Regression

Let's explore regression with a simplified example in which we'll train a model to predict a numeric label (**y**) based on a single feature value (**x**). Most real scenarios involve multiple feature values, which adds some complexity; but the principle is the same.

For our example, let's stick with the ice cream sales scenario we discussed previously. For our feature, we'll consider the *temperature* (let's assume the value is the maximum temperature on a given day), and the label we want to train a model to predict is the number of ice creams sold that day. We'll start with some historic data that includes records of daily temperatures (**x**) and ice cream sales (**y**):

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="50%">
Temperature (x)
</edukamu-table-header>
<edukamu-table-header width="50%">
Ice cream sales (y)
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
51
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
52
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
67
</edukamu-table-cell>
<edukamu-table-cell >
14
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
65
</edukamu-table-cell>
<edukamu-table-cell >
14
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
70
</edukamu-table-cell>
<edukamu-table-cell >
23
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
69
</edukamu-table-cell>
<edukamu-table-cell >
20
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
72
</edukamu-table-cell>
<edukamu-table-cell >
23
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
75
</edukamu-table-cell>
<edukamu-table-cell >
26
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
73
</edukamu-table-cell>
<edukamu-table-cell >
22
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
81
</edukamu-table-cell>
<edukamu-table-cell >
30
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
78
</edukamu-table-cell>
<edukamu-table-cell >
26
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
83
</edukamu-table-cell>
<edukamu-table-cell >
36
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>


#### Training a Regression Model

We'll start by splitting the data and using a subset of it to train a model. Here's the training dataset:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="50%">
Temperature (x)
</edukamu-table-header>
<edukamu-table-header width="50%">
Ice cream sales (y)
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
51
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
65
</edukamu-table-cell>
<edukamu-table-cell >
14
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
69
</edukamu-table-cell>
<edukamu-table-cell >
20
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
72
</edukamu-table-cell>
<edukamu-table-cell >
23
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
75
</edukamu-table-cell>
<edukamu-table-cell >
26
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
81
</edukamu-table-cell>
<edukamu-table-cell >
30
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

To get an insight of how these x and y values might relate to one another, we can plot them as coordinates along two axes, like this:

<edukamu-image url="/graphics/module1/scatter-plot.png" alt="Diagram of a scatter plot showing x and y."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

Now we're ready to apply an algorithm to our training data and fit it to a function that applies an operation to x to calculate y. One such algorithm is linear regression, which works by deriving a function that produces a straight line through the intersections of the x and y values while minimizing the average distance between the line and the plotted points, like this:

<edukamu-image url="/graphics/module1/regression-line.png" alt="Diagram of the scatter plot with a regression line added."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The line is a visual representation of the function in which the slope of the line describes how to calculate the value of y for a given value of **x**. The line intercepts the **x** axis at 50, so when **x** is 50, **y** is 0. As you can see from the axis markers in the plot, the line slopes so that every increase of 5 along the **x** axis results in an increase of 5 up the **y** axis; so when **x** is 55, **y** is 5; when **x** is 60, **y** is 10, and so on. To calculate a value of **y** for a given value of **x**, the function simply subtracts 50; in other words, the function can be expressed like this:

**f(x) = x-50**

You can use this function to predict the number of ice creams sold on a day with any given temperature. For example, suppose the weather forecast tells us that tomorrow it will be 77 degrees. We can apply our model to calculate *77-50* and predict that we'll sell 27 ice creams tomorrow.

That's regression in a nutshell.

In order to make a model effective, it needs to be thoroughly evaluated. You'll encounter the following concepts as you advance on this study path, so take a moment to get familiar with each one. In practice, they all have to do with comparing the values predicted by the model to the actual numbers.

**Mean Absolute Error (MAE)**: Imagine predicting ice cream sales; MAE measures the average of absolute errors, revealing how much each prediction deviates from reality. In our example, the mean of errors (2, 3, 3, 1, 2, and 3) is 2.33.

**Mean Squared Error (MSE)**: MAE treats all errors equally, but MSE magnifies larger errors by squaring them. The mean of squared errors (4, 9, 9, 1, 4, and 9) in our scenario is 6.

**Root Mean Squared Error (RMSE)**: To interpret errors in the original quantity (ice creams), we take the square root of MSE. Here, √6 equals 2.45 (ice creams).

**Coefficient of determination (R2)**: R2 goes beyond error comparison. It gauges how much of the variance in results can be ascribed to the model rather than random fluctuations. In our ice cream model, an R2 of 0.95 implies a remarkable fit to the validation data.

Don't worry, if the terminology seems difficult to comprehend right now. You'll surely get familiar with the concepts as you keep on broadening your knowledge!

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 2. Binary Classification
</edukamu-collapse-hidden-title>

Classification, like regression, is a *supervised* machine learning technique; and therefore follows the same iterative process of training, validating, and evaluating models. Instead of calculating numeric values like a regression model, the algorithms used to train classification models calculate *probability* values for class assignment and the evaluation metrics used to assess model performance compare the predicted classes to the actual classes.

*Binary classification* algorithms are used to train a model that predicts one of two possible labels for a single class. Essentially, predicting **true** or **false**. In most real scenarios, the data observations used to train and validate the model consist of multiple feature (**x**) values and a **y** value that is either **1** or **0**.


### Example: Binary Classification

To understand how binary classification works, let's look at a simplified example that uses a single feature (**x**) to predict whether the label **y** is 1 or 0. In this example, we'll use the blood glucose level of a patient to predict whether or not the patient has diabetes. Here's the data with which we'll train the model:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="50%">
Blood glucose (x)
</edukamu-table-header>
<edukamu-table-header width="50%">
Diabetic? (y)
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
67
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
103
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
114
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
72
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
116
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
65
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

To train the model, we'll use an algorithm to fit the training data to a function that calculates the *probability* of the class label being *true* (in other words, that the patient has diabetes). Probability is measured as a value between 0.0 and 1.0, such that the *total* probability for *all* possible classes is 1.0. So for example, if the probability of a patient having diabetes is 0.7, then there's a corresponding probability of 0.3 that the patient isn't diabetic.

There are many algorithms that can be used for binary classification, such as *logistic regression*, which derives a *sigmoid* (S-shaped) function with values between 0.0 and 1.0, like this:

<edukamu-image url="/graphics/module1/sigmoid-plot.png" alt="Diagram of a logistic function."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

The function produced by the algorithm describes the probability of **y** being true (y=1) for a given value of **x**. Mathematically, you can express the function like this:

**f(x) = P(y=1 | x)**

For three of the six observations in the training data, we know that **y** is definitely *true*, so the probability for those observations that y=1 is **1.0** and for the other three, we know that **y** is definitely *false*, so the probability that y=1 is **0.0**. The S-shaped curve describes the probability distribution so that plotting a value of **x** on the line identifies the corresponding probability that **y** is **1**.

The diagram also includes a horizontal line to indicate the *threshold* at which a model based on this function will predict *true* (**1**) or *false* (**0**). The threshold lies at the mid-point for **y** (P(*y*) = *0.5*). For any values at this point or above, the model will predict *true* (**1**); while for any values below this point it will predict *false* (**0**). For example, for a patient with a blood glucose level of 90, the function would result in a probability value of 0.9. Since 0.9 is higher than the threshold of 0.5, the model would predict *true* (**1**) - in other words, the patient is predicted to have diabetes.

<edukamu-note class="edukamu-note-icon-info">
Despite its name, in machine learning logistic regression is used for classification, not regression. The important point is the logistic nature of the function it produces, which describes an S-shaped curve between a lower and upper value (0.0 and 1.0 when used for binary classification).
</edukamu-note>
<br>

Notice that we'll only explore the main concepts behind technologies like machine learning on these courses. If you're interested in a more in-depth approach, we recommend that you check out Microsoft's official certificate materials (in this case, AI-900).

</edukamu-collapse>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="aineisto">
### 3. Multiclass Classification
</edukamu-collapse-hidden-title>

Multiclass classification is used to predict to which of multiple possible classes an observation belongs. As a supervised machine learning technique, it follows the same iterative train, validate, and evaluate process as regression and binary classification in which a subset of the training data is held back to validate the trained model.

### Example: Multiclass Classification

Multiclass classification algorithms are used to calculate probability values for multiple class labels, enabling a model to predict the *most probable* class for a given observation.

Let's explore an example in which we have some observations of penguins, in which the flipper length (**x**) of each penguin is recorded. For each observation, the data includes the penguin species (**y**), which is encoded as follows:
* 0: Adelie
* 1: Gentoo
* 2: Chinstrap

As with previous examples, a real scenario would include multiple feature (x) values. We'll use a single feature to keep things simple.

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="50%">
Flipper length (x)
</edukamu-table-header>
<edukamu-table-header width="50%">
Species (y)
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
167
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
172
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
225
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
197
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
189
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
232
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
158
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

To train a multiclass classification model, we need to use an algorithm to fit the training data to a function that calculates a probability value for each possible class. There are two kinds of algorithm you can use to do this:
* One-vs-Rest (OvR) algorithms
* Multinomial algorithms

#### One-vs-Rest (OvR) Algorithms

One-vs-Rest algorithms train a binary classification function for each class, each calculating the probability that the observation is an example of the target class. Each function calculates the probability of the observation being a specific class compared to *any* other class. For our penguin species classification model, the algorithm would essentially create three binary classification functions:
* **f<sup>0</sup>(x) = P(y=0 | x)**
* **f<sup>1</sup>(x) = P(y=1 | x)**
* **f<sup>2</sup>(x) = P(y=2 | x)**

Each algorithm produces a sigmoid function that calculates a probability value between 0.0 and 1.0. A model trained using this kind of algorithm predicts the class for the function that produces the highest probability output.

#### Multinomial Algorithms

As an alternative approach is to use a multinomial algorithm, which creates a single function that returns a multi-valued output. The output is a *vector* (an array of values) that contains the *probability distribution* for all possible classes - with a probability score for each class which when totaled add up to 1.0:

**f(x) =[P(y=0|x), P(y=1|x), P(y=2|x)]**

An example of this kind of function is a *softmax* function, which could produce an output like the following example:

[0.2, 0.3, 0.5]

The elements in the vector represent the probabilities for classes 0, 1, and 2 respectively; so in this case, the class with the highest probability is **2**.

Regardless of which type of algorithm is used, the model uses the resulting function to determine the most probable class for a given set of features (**x**) and predicts the corresponding class label (**y**).

### Evaluating a Multiclass Classification Model

You can evaluate a multiclass classifier by calculating binary classification metrics for each individual class. Alternatively, you can calculate aggregate metrics that take all classes into account.

Let's assume that we've validated our multiclass classifier, and obtained the following results:


<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="33,33%">
Flipper length (x)
</edukamu-table-header>
<edukamu-table-header width="33,33%">
Actual species (y)
</edukamu-table-header>
<edukamu-table-header width="33,33%">
Predicted species (ŷ)
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
165
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
171
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
205
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
195
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
183
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
221
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
214
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
</edukamu-table-row>

</edukamu-table-body>
</edukamu-table>
</edukamu-section>
<br>

The confusion matrix for a multiclass classifier is similar to that of a binary classifier, except that it shows the number of predictions for each combination of *predicted* (**ŷ**) and *actual* class labels (**y**):

<edukamu-image url="/graphics/module1/multiclass-confusion-matrix.png" alt="Diagram of a multiclass confusion matrix."> <!--style="box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;"-->
<!-- <edukamu-section class="edukamu-kuvateksti">
A table and its properties.
</edukamu-section> -->
<br> 

From this confusion matrix, we can determine the metrics for each individual class as follows:

<!--Edukamu-table alkaa-->
<edukamu-section class="edukamu-table-colored-headers edukamu-table-scrollable">
<edukamu-table>
<edukamu-table-head>
<edukamu-table-row>
<edukamu-table-header width="11,11%">
Class
</edukamu-table-header>
<edukamu-table-header width="11,11%">
TP
</edukamu-table-header>
<edukamu-table-header width="11,11%">
TN
</edukamu-table-header>
<edukamu-table-header width="11,11%">
FP
</edukamu-table-header>
<edukamu-table-header width="11,11%">
FN
</edukamu-table-header>
<edukamu-table-header width="11,11%">
Accuracy
</edukamu-table-header>
<edukamu-table-header width="11,11%">
Recall
</edukamu-table-header>
<edukamu-table-header width="11,11%">
Precision
</edukamu-table-header>
<edukamu-table-header width="11,11%">
F1-Score
</edukamu-table-header>
</edukamu-table-row>
</edukamu-table-head>

<edukamu-table-body>
<edukamu-table-row>
<edukamu-table-cell>
0
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
<edukamu-table-cell >
5
</edukamu-table-cell>
<edukamu-table-cell>
0
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
<edukamu-table-cell >
1.0
</edukamu-table-cell>
<edukamu-table-cell>
1.0
</edukamu-table-cell>
<edukamu-table-cell >
1.0
</edukamu-table-cell>
<edukamu-table-cell >
1.0
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
1
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
<edukamu-table-cell >
4
</edukamu-table-cell>
<edukamu-table-cell>
1
</edukamu-table-cell>
<edukamu-table-cell >
0
</edukamu-table-cell>
<edukamu-table-cell >
0.86
</edukamu-table-cell>
<edukamu-table-cell>
1.0
</edukamu-table-cell>
<edukamu-table-cell >
0.67
</edukamu-table-cell>
<edukamu-table-cell >
0.8
</edukamu-table-cell>
</edukamu-table-row>

<edukamu-table-row>
<edukamu-table-cell>
2
</edukamu-table-cell>
<edukamu-table-cell >
2
</edukamu-table-cell>
<edukamu-table-cell >
4
</edukamu-table-cell>
<edukamu-table-cell>
0
</edukamu-table-cell>
<edukamu-table-cell >
1
</edukamu-table-cell>
<edukamu-table-cell >
0.86
</edukamu-table-cell>
<edukamu-table-cell>
0.67
</edukamu-table-cell>
<edukamu-table-cell >
1.0
</edukamu-table-cell>
<edukamu-table-cell >
0.8
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

To calculate the overall accuracy, recall, and precision metrics, you use the total of the *TP*, *TN*, *FP*, and *FN* metrics:
* **Overall accuracy** = (13+6)÷(13+6+1+1) = **0.90**
* **Overall recall** = 6÷(6+1) = **0.86**
* **Overall precision** = 6÷(6+1) = **0.86**

The overall F1-score is calculated using the overall recall and precision metrics:
* **Overall F1-score** = (2x0.86x0.86)÷(0.86+0.86) = **0.86**

Take the time to review the mathematics we just reviewed. You can move at your own pace and rhythm - it's better to focus well now in order to avoid misunderstandings in the future.

</edukamu-collapse>
<br>

<edukamu-section class="slate-section slate-blue">
How was it? Not that difficult if you really pay attention, is it? That’s the key to uncovering artificial intelligence: by paying attention to the details, you’ll start grasping broader concepts bit by bit. You should now have a basic understanding of different types of unsupervised learning.

Complete the exercise below in order to test your skills.
</edukamu-section>
<br>

<edukamu-collapse isCollapsed="true" title-level="4">
<edukamu-collapse-hidden-title collapseType="tehtava">
### Exercise: Supervised Learning
</edukamu-collapse-hidden-title>

Answer the following questions.

<edukamu-text-poll url="/exercises/module1/supervised-learning-text-poll.yaml" id="nmg42u4wo35ogks1"/>
<br>
<edukamu-text-poll url="/exercises/module1/supervised-learning-text-poll-2.yaml" id="66pjro9664427c36"/>
<br>
<edukamu-text-poll url="/exercises/module1/supervised-learning-text-poll-3.yaml" id="aql1662c7u63fzw1"/>
<br>
<edukamu-text-poll url="/exercises/module1/supervised-learning-text-poll-4.yaml" id="623dm96j2kj5n2ch"/>
<br>
<edukamu-text-poll url="/exercises/module1/supervised-learning-text-poll-5.yaml" id="rf48hl4zo3l2k9o2"/>
<br>
<edukamu-text-poll url="/exercises/module1/supervised-learning-text-poll-6.yaml" id="2wyqmh302afy72kz"/>
<br>

<!-- Textpoll mallivastaus kombo: ALKAA-->
<!-- <edukamu-section class="edukamu-task-border">
<edukamu-text-poll url="/exercises/module1/supervised-learning-text-poll.yaml" id="nmg42u4wo35ogks1"/>
<br>
<edukamu-link class="edukamu-button white-text" title="Refresh" url="/1/supervised-learning?question=nmg42u4wo35ogks1">Refresh the page</edukamu-link>
<edukamu-section class="edukamu-kuvateksti">
If you dont see the feedback text below, refresh the page.
</edukamu-section>

<edukamu-answer-check course="gpba5vhjf2wb0iti" question="nmg42u4wo35ogks1" path="completed" value="true">
### Feedback to the task:

Input features include email content, sender, and other attributes. Output labels indicate whether each email is classified as spam or not. This way, a model can be taught to recognize spam by mapping out features often associated with it.
</edukamu-answer-check>
</edukamu-section>
<br> -->
<!-- Textpoll mallivastaus kombo: LOPPUU-->

Now you have the opportunity to go back and **review your answers** and compare them to the example solutions. If you have finished the tasks, please refresh the page by pressing the button below, to make sure example solutions are visible to you.

<edukamu-link class="edukamu-button white-text" title="Refresh" url="/1/supervised-learning?question=nmg42u4wo35ogks1">Refresh the page</edukamu-link>
<br>

</edukamu-collapse>
<br>


Did you manage to complete the exercise? Do notice that in many cases, there are more than one correct solution to open-ended questions such as the ones you just experienced.

Whenever you're happy with your learning on this page, feel free to move on to unsupervised learning!

<br>
<edukamu-image url="/graphics/progress-pallo-grafiikat/da-progress1-2-3.png" alt="Edukamu-progress-in-a-module-image">
