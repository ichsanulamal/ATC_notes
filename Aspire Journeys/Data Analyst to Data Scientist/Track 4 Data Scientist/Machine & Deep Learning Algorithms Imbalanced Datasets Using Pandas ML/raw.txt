Machine & Deep Learning Algorithms: Imbalanced Datasets Using Pandas ML
The imbalanced-learn library that integrates with Pandas ML (machine learning) offers several techniques to address the imbalance in datasets used for classification. In this course, explore oversampling, undersampling, and a combination of techniques. Begin by using Pandas ML to explore a data set in which samples are not evenly distributed across target classes. Then apply the technique of oversampling with the RandomOverSampler class in the imbalanced-learn library; build a classification model with oversampled data; and evaluate its performance. Next, learn how to create a balanced data set with the Synthetic Minority Oversampling Technique and how to perform undersampling operations on a data set by applying Near Miss, Cluster Centroids, and Neighborhood cleaning rules techniques. Next, look at ensemble classifiers for imbalanced data, applying combination samplers for imbalanced data, and finding correlations in a data set. Learn how to build a multilabel classification model, explore the use of principal component analysis, or PCA, and how to combine use of oversampling and PCA in building a classification model. The exercise involves working with imbalanced data sets.

Table of Contents
    1. Video: Course Overview (it_dsmdladj_04_enus_00)

    2. Video: Analyzing an Imbalanced Dataset (it_dsmdladj_04_enus_01)

    3. Video: The RandomOverSampler (it_dsmdladj_04_enus_02)

    4. Video: The SMOTE Oversampler (it_dsmdladj_04_enus_03)

    5. Video: Undersampling Using imbalanced-learn (it_dsmdladj_04_enus_04)

    6. Video: Ensemble Classifiers for Imbalanced Data (it_dsmdladj_04_enus_05)

    7. Video: Combination Samplers (it_dsmdladj_04_enus_06)

    8. Video: Finding Correlations in a Dataset (it_dsmdladj_04_enus_07)

    9. Video: Building a Multi-Label Classification Model (it_dsmdladj_04_enus_08)

    10. Video: Dimensionality Reduction with PCA (it_dsmdladj_04_enus_09)

    11. Video: Imbalanced Learn and PCA (it_dsmdladj_04_enus_10)

    12. Video: Exercise: Working with Imbalanced Datasets (it_dsmdladj_04_enus_11)

    Course File-based Resources

1. Video: Course Overview (it_dsmdladj_04_enus_00)

No Objectives
[Video description begins] Topic title: Course Overview. Your host for this session is Kishan Iyer. [Video description ends]

Hi and welcome to this course, working with imbalanced datasets using Pandas ML.

My name is Kishan Iyer, and I will be your instructor for this course. A little about myself first, I have a Master's Degree in Computer Science from Colombia University, and have previously worked in companies such as Deutsche Bank and WebMD in New York. I presently work for Loonycorn, a studio for high quality video content.

Machine learning is one of the hottest fields right now and it is applied nearly everywhere. From movie recommendations on streaming platforms, to fraud detection on credit card transactions. There are multiple applications for machine learning, and numerous techniques available to solve a variety of problems.

This course is very much hands-on and contains only labs. The focus is on using the imbalance learn library to build classification models using data sets which contain skewed samples, where some categories are represented to a far greater degree than others.

We cover the use of oversamplers to create more instances of the under represented categories. And then apply undersampling techniques to filter out some of the points from classes which are over represented.

And then we apply a combination of the undersampling and oversampling techniques. These methods will help us create a more balanced data set which can help build better classification models.

We also explore the use of principal component analysis or PCA to implement dimensionality reduction on a data set which contains a lot of correlated fields.

Doing all of the labs in this course will equip you with the skills needed to work with imbalanced data sets in order to build better classification models. You will also learn how to apply principal component analysis on data sets which contain several correlated features. This will prepare you to work with various kinds of data sets when building your machine learning models.

2. Video: Analyzing an Imbalanced Dataset (it_dsmdladj_04_enus_01)

Learn how to use Pandas ML to explore a dataset where the samples are not evenly distributed across the target classes.
use Pandas ML to explore a dataset where the samples are not evenly distributed across the target classes
[Video description begins] Topic title: Analyzing an Imbalanced Dataset. Your host for this session is Kishan Iyer. [Video description ends]

In this demo, we will take a look at various ways to handle imbalanced datasets.

When building classification models, we may often come across a dataset where the data is not evenly distributed across the classes. We may end up with some classes being over represented to a great degree. And this skewness in the dataset can lead to problems when it comes to detecting anomalous behavior.

For instance, if you are building a model to predict whether a transaction is fraudulent. Then it is likely that you will be working with a dataset where nearly all of the transactions are legitimate, with only a handful of fraudulent transactions. To address the skewness in any dataset, we can make use of the imbalanced-learn library.

We will cover the various options available within this library to address skewed datasets. And we will be writing our code in a Jupyter notebook, and I've created a new notebook named ImbalancedData for this purpose.

[Video description begins] A Jupyter notebook named ImbalancedData displays. A cell in the form of an empty input box displays with the command prompt: In [ ] : to the left of it. The cursor blinks in this input box. [Video description ends]

The first thing we need to do is to install the imbalanced-learn library. We can simply do that by running a pip install command. To run this from a cell in your Jupyter notebook, you can simply add an exclamation point at the beginning, and then run pip install imbalanced-learn --upgrade.

[Video description begins] In the input box of the first cell, he types and executes the following command:! pip install imbalanced - learn - - upgrade. The number 1 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

This will install the imbalanced-learn library, if you don't have it already, or upgrade it if there is a newer version available.

[Video description begins] The output displays. It says requirement already up-to-date and skipping upgrade. [Video description ends]

So, in my case, I already have the latest version, which as of this recording, is version 1.1.0. With the installation out of the way, we're now ready to go ahead and begin coding our notebook.

The first thing we will do is to import all of the libraries which we require, starting with the pandas_ml library.

[Video description begins] In the input box of the next cell, he types and executes the following command: import pandas _ ml as pdml. [Video description ends]

And this is what we will be using in order to access the imbalanced-learn functions. We will need the pandas library in order to initially load our dataset from a CSV file. And we will be making use of matplotlib, specifically the pyplot object in order to render a plot of our data within the Jupyter notebook.

[Video description begins] He adds a second line of command in the same cell: import pandas as pd . He adds a third line of command in the same cell: import matplotlib.pyplot as plt. The number 2 now appears within the square brackets after the word 'In' in the command prompt next to the second input box. [Video description ends]

Next, I'm going to simply disable warnings within this notebook.

[Video description begins] In the input box of the next cell, he types and executes the following command: import warnings. He adds a second line of command in the same cell: warnings.filterwarnings("ignore"). The number 3 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And this is because there are some deprecation warnings which may come up due to the dependencies of the libraries we are using. These may become a bit of a distraction in the demo, which is why I'm simply suppressing the warnings.

And once all our import statements are out of the way, we can now go ahead and import the dataset we will be using for this demo. This is a dataset we have used previously in this learning path, and it contains records for a number of patients from the Pima Indian community. It includes various health related metrics, and whether the patient has diabetes or not.

[Video description begins] In the input box of the next cell, he types and executes the following command: df=pd.read_csv ('datasets/diabetes.csv'). [Video description ends]

The dataset can be downloaded from www.kaggle.com/uciml/pima-indians-diabetes-database. It is also available as part of the course material. And in my case, I'm simply loading this dataset from a CSV file on my local file system into this pandas dataframe. We then create a pandas_ml ModelFrame out of the contents of the dataframe, for which we pass along the dictionary version of our dataframe to the ModelFrame constructor.

[Video description begins] He adds another line of command in the same cell: mf = pdml.ModelFrame(df.to_dict()). The number 4 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

We will then quickly take a look at the top five rows of this ModelFrame, and

[Video description begins] In the input box of the next cell, he types and executes the following command: mf.head( ). The number 5 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

you can see the various metrics available for each patient. The number of pregnancies, the glucose levels, blood pressure, and so on. And when we build our classification model, we will be using most of these columns as the features. And then we need to predict the outcome, whether the patient has diabetes or not.

[Video description begins] The output displays. It is a table with five rows and ten columns. The columns are labeled: pregnancies, Glucose, Blood pressure, skin thickness, Insulin , BMI, diabetes pedigree function, age and outcome. [Video description ends]

1 represents a patient who has diabetes, and 0 is when the patient does not have it. Now in our ModelFrame, the first thing we need to do is to specify the target column. And for that we set the target_name field of this ModelFrame to be the outcome column.

[Video description begins] In the input box of the next cell, he types and executes the following command: : mf.target_name='Outcome'. The number 6 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

Following that, we quickly confirm that the target has indeed been set by invoking the has_target method of the ModelFrame.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf . has _ target ( ). The number 7 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And we have that confirmation here.

[Video description begins] The output displays. It is True. [Video description ends]

We also check that we can access the contents of the Outcome column by referencing the target field of the ModelFrame.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf.target.head( ). The number 8 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And the values in the Outcome column are indeed available here.

[Video description begins] The output displays. It is a table of five rows and two columns. [Video description ends]

It is now time for us to check how balanced our dataset is.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf.target.value_counts ( ). The number 9 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

So how many of the patients in our dataset have diabetes, and how many do not? To get the number of data points in each category in the target column, we can simply invoke the value_counts method. Which will give us the number of rows in the dataset corresponding to each category in the target column. And this output shows us that our dataset is in fact not evenly distributed across the classes in the Outcome column.

[Video description begins] The output displays. It is a table of two rows and two columns. A line displays below the table. It reads : Name: Outcome and dtype: int 64. [Video description ends]

So we have two-thirds of the patients who do not have diabetes, and about a third who do. So this is not a highly skewed dataset, however for the purposes of this demo, we will see how we can address the imbalance in this case. So that you can apply the same techniques later on to datasets where the skewness is far more extreme. We will be building classification models using this data. And we will also be using various techniques to address the imbalance in the training data.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_train, mf_test=mf.dot_selection\ .train_test_split (test_size=0.3). The number 10 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

To do that though, we need to divide our dataset into training and test sets, for which we make use of the train_test_split method available through the ModelFrame object. So 70% of this dataset will be used for training and the remaining 30% for testing. So once this split has occurred, let us take a look at the value counts within the training dataset.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_train.target.value_counts ( ). The number 11 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And we see here that once again, this is also skewed with about a two to one split among patients who don't have diabetes, and those who do.

[Video description begins] The output displays. It is a table with two rows and two columns. A line displays below the table. It reads : Name: Outcome and dtype: int 64. [Video description ends]

We can in fact visualize the skewness by generating a scatter plot.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_train.plot.scatter (x='Glucose', y='BMI', , c='Outcome', cmap= 'rainbow'). He adds a second line of command in the same cell: plt.show( ). The number 12 now appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

So there will be dots on this plot, representing each patient in the training dataset. The x coordinate of the dot will represent their glucose levels, and the y coordinate, their BMI numbers. You could in fact use any of the feature columns as your x and y values. What we're really interested in though, is to generate different colored dots or markers, depending on the value in the Outcome column for that patient. So we use the c parameter here to say that the plot's color should be based on the value in the Outcome field. And the colors can be obtained from the rainbow color map. And from the scatter plot which is generated, we can see that there is a preponderance of purple dots representing the patients without diabetes. And the red dots representing the diabetic patients are a little more spread out, but definitely fewer in number.

[Video description begins] The output displays. It is a scatter plot with BMI number listed on one end and the outcome numbers listed on the other end. The scatter plot displays a cluster of purple dots representing patients without diabetes interspersed with fewer red dots representing patients with diabetes. [Video description ends]

So now that we have the numbers for the distribution of data in each category of the Outcome column, and have also visualized this distribution with the scatter plot. Let us now address the imbalance in the dataset by making use of an over sampler. That is precisely what we will do in the next clip.

3. Video: The RandomOverSampler (it_dsmdladj_04_enus_02)

In this video, you will learn how to apply the technique of oversampling using the RandomOverSampler class in the imbalanced-learn library. You will also build a classification model with the oversampled data, and evaluate its performance.
apply the technique of oversampling using the RandomOverSampler class in the imbalanced-learn library, build a classification model with the oversampled data, and evaluate its performance
[Video description begins] Topic Title: The RandomOverSampler. Your host for this session is Kishan Iyer. [Video description ends]

We are now about to apply the technique of over sampling, to address the skewness in our data set.

An oversampler will increase the number of instances in the minority class, by using various techniques. It will simply replicate the data which is already present in the data set. Or it could manufacture synthetic data, which will fall into the minority class.

We will start off by making use of a random over sampler which can be accessed from the model frames, imbalance.oversampling module. This will produce a more balanced data set by effectively duplicating the values in the minority class. That is, it will duplicate the patients with diabetes within our data set. And once this oversampler has been initialized, we can see what has been created, along with all of the default parameters since we did not specify any explicitly. The sampling strategy of auto,

[Video description begins] A Jupyter notebook named ImbalancedData displays. A cell in the form of an empty input box displays with the command prompt: In [ ] : to the left of it. The cursor blinks in this input box. In the input box of the 13th cell, he types and executes the following command: over sampler =mf_train.imbalance.over_sampling.Randomoversampler(). He adds another line of command in the same cell: oversampler . The number 13 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

means that all of the non majority classes will be over sampled.

So over sampling can be used, not just for binary classification as we're doing right now, but also for multi category classification. If you'd like to define a ratio for the number of data points in the majority class versus those in the minority classes. You can do so using the sampling strategy parameter rather than the ratio since the latter has now been deprecated.

[Video description begins] The output displays: random over sampler (random_state=None, ratio = None , return _ indices=false, sampling_strategy='auto'). [Video description ends]

We will now proceed however, and then apply this over sampling technique on our training data.

So for that, we will call our mf_train model frames fit_sample method and then pass to it our oversampler as the argument. This will result in a random over sampling of our training data, and

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_oversamp=mf_train.fit _ sample (oversampler) . He adds another line of command in the same cell: mf_oversamp.tail(). The number 14 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

the results will be returned in this mf_oversamp model frame. We can then view the last few rows of this model frame, and we view that all of these rows have a value of 1 in the outcome column.

[Video description begins] The output displays. It is a table of six rows and ten columns. The column headings are: outcome, pregnancies, glucose, blood pressure, skin thickness, insulin, BMI, diabetes pedigree function, and age. [Video description ends]

This is because this represents all of the duplicated data, since it was a minority class which was over sampled. Looking at the index on the left, we can see that this contains 704 rows of data now. And we will now check, how this data is distributed in terms of the representation for each of the outcome values. Has this over sampling resulted in a more even spread of patient with diabetes and without?

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_oversamp.target.value_counts ( ). The number 15 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And the answer is yes, so there is now an exact 50/50 split of data in each of the categories for the outcome. So just to confirm whether this over sampling resulted in any duplicate roles

[Video description begins] The output displays. It is a table of 2 rows and 2 columns. A line below the table reads: name : outcome, dtype: int 64. [Video description ends]

being generated. We can make use of the duplicated method of the model frame,

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_oversamp.duplicated( ). The number 16 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

which will indicate whether a particular row is a duplicate value of a row which already exists in the data frame. Note that the first occurrence of a particular row of data will not be marked as duplicate by default. So when we run this, we see that at the beginning there are no duplicate values. However, when we scroll further down in this model frame, we see that pretty much all of these rows have been duplicated. So the random over sampler has clearly duplicated a lot of

[Video description begins] The output displays. It is a boolean table of 704 rows and 2 columns. A line below the table reads : Length 704, dtype: bool. [Video description ends]

the rows in the model frame, but how many exactly? Well for that, we can simply sum up the number of true values from our previous output to get the number of duplicates in our model frame.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_oversamp.duplicated ( ).sum( ) . The number 17 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And the output shows us that a 167 rows in all have been replicated. This number is in fact the exact difference between,

[Video description begins] The output displays. It is167. [Video description ends]

the number of non-diabetic and diabetic patients in our training data. So now that we know from the numbers that we have a more balanced data set after this over sampling.

Let us now try to visualize this, to see whether there is a more even split between the diabetic and the non-diabetic patients. So we generate a scatter plot once more,

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_oversamp.plot.scatter (x='Glucose', y='BMI', c='Outcome', cmap = 'rainbow') . He adds another line of command in the same cell: plt.show( ). The number 18 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

and in this occasion we see a higher number of red dots. On the right you see the scatter plot generated on the original training data, before over sampling was performed.

[Video description begins] The output displays. It is a scatter diagram of red and purple dots. BMI values are listed on the y axis and outcome values are listed on the x axis. There are more red dots in this diagram than purple dots. The scatter plot of training data also displays and he compares the two scatter plots. [Video description ends]

And on the left we see the results after the over sampling. So now that we have a more balanced data set, we can use it in order to train a classification model.

But first let us quickly take a look at the shapes of the data we're working with. This includes our training data which is in fact our oversampled model frame, and then the test data which we have left unaltered.

[Video description begins] In the input box of the next cell, he executes the following command: print (' Training data shape: ', mf_oversamp.shape) . He adds another line of command in the same cell: print ('Test data shape: ', mf_test.shape) . The number 19 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And we see that we have 704 rows of data in our training set. We will quickly confirm that the target name has been set in our

[Video description begins] The output displays : Training data shape : (704, 9). Test data shape: (231,9) . [Video description ends]

training data, and yes the outcome column is the target.

[Video description begins] In the input cell of the next cell, he types and executes the following command :mf_oversamp.target_name. The output displays. It is 'Outcome'. The number 20 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

We now initialize our classifier which will be a Linear SVC model, which we can access from the model frames svm.LinearSVCclass. We initialize this model by specifying a max iter value of 100,000, to ensure that this classification model will converge during the training process. And once this classifier has been initialized,

[Video description begins] In the input cell of the next cell, he types and executes the following command : estimator = mf_oversamp. svn. linerarsvc(max_iter=100000) . The number 22 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

it is now time to fit our training data to this classifier. And for that we will call the fit method in our model frame, and then pass as argument this estimator which we have just initialized.

[Video description begins] In the input cell of the next cell, he types and executes the following command : mf_oversamp.fit(estimator). The number 23 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

So with that, our training is complete and our model is now ready to make predictions.

[Video description begins] The output displays: LinearSVC (c=1, class_weight=none, dual = true, fit_intercept= true, intercept _ scaling=1, loss='squared _ hinge', max_iter=100000, multi_class='ovr', penalty='12', random_state=none, tol=0.0001, verbose=0). [Video description ends]

In order to make predictions using the test data, we will invoke the test model frames predict method, and pass to it as an argument. This estimator which we have just initialized and then trained. This will return a set of predictions on the test data which we capture

[Video description begins] In the input cell of the next cell, he types and executes the following command : predictions= mf_test.predict(estimator) . He adds another line of command in the same cell: predictions .head( ). The number 24 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

in this prediction's variable. We will also preview the first 5 rows of the predictions, and the data looks fine in here. So for the first 4 rows of data in our test set the predicted outcome is 0,

[Video description begins] The output displays. It is a table of 5 rows and 2 columns. A line displays below the table. It reads : dtype int64. [Video description ends]

that is the patient does not have diabetes. And for the fifth patient the outcome is predicted as 1. We can compare these predicted values with the actual values by examining the first five rows of the test set. And the contents of the outcome column shows us that 4 out of the first

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_test. head ( ) . The number 25 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

5 predictions have in fact been accurate.

[Video description begins] The output displays. It is a table of 6 rows and 10 columns. The columns are labeled outcome, pregnancies, glucose, bloodpressure, skin thickness, insulin, BMI, diabetes pedigree function, and age. [Video description ends]

However, to gauge the accuracy of our model on all of the test data, we can call the metrics.accuracy score method, accessible from our test model frame, and then pass to it our trained estimator. The test data will then be passed to the estimator, which will make predictions on it, and then compare the predicted values with the actual values in the training set. And the output shows us that this model is able to make

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_test.metrics.accuracy_score(estimator) . The number 26 appears within the square brackets after the word 'In' in the command prompt next to this input box.The output displays. It is 0.75757. [Video description ends]

accurate predictions on the test data about 76% of the times. However, when using machine learning models to predict whether a particular patient has a disease or not. It is often useful to evaluate the model not on the overall accuracy, but on the precision score. That is what proportion of the positive predictions were actually correct?

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_test.metrics.precision_score(estimator) . The number 27 appears within the square brackets after the word 'In' in the command prompt next to this input box.The output displays. It is 0.72881. [Video description ends]

For that we can make use of the precision_score function, available as part of the metrics of the model frame. And this shows us that when our model predicts that a patient has diabetes, it is accurate about 73% of the time. There are also metrics available to calculate the recall score of our model. So invoking the recall_score function, we can see that among the patients who did have diabetes, our model was only able to predict that correctly 52% of the time. In fact, to get a good view of how our predictions have been distributed

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_test.metrics.recall_score(estimator) . The number 28 appears within the square brackets after the word 'In' in the command prompt next to this input box.The output displays. It is 0.518. [Video description ends]

across the actual and predictive values. We can make use of a ConfusionMatrix which we can import from the pandas_ml library.

[Video description begins] In the input box of the next cell, he types and executes the following command : from pandas_ml import confusion matrix . The number 29 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

Following that, we initialize this confusion matrix, with the actual values from our test data and the predicted values,

[Video description begins] In the input box of the next cell, he types and executes the following command : confusion_matrix= confusion matrix (mf_test.target.values, predictions.values). The number 30 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

and this generates the confusion matrix for us. We can see the true positives and the true negatives over here,

[Video description begins] In the input box of the next cell, he types and executes the following command : confusion_matrix. The number 31 appears within the square brackets after the word 'In' in the command prompt next to this input box. The output displays. It is a table of 4 rows and 4 columns depicting the predicted and actual values of true, false, and all. [Video description ends]

and then also the false positives and the false negatives. So we have now learned, how we can address the skewness in our training data, by making use of the imbalanced learn library's random over sampler. We will now go ahead, and take a look at some of the other techniques available, including one more over sampling method.

4. Video: The SMOTE Oversampler (it_dsmdladj_04_enus_03)

In this video, you will learn how to create a balanced dataset using the Synthetic Minority Oversampling Technique and build and evaluate a classification model with that data.
create a balanced dataset using the Synthetic Minority Oversampling Technique and build and evaluate a classification model with that data
[Video description begins] Topic title: The SMOTE oversampler . Your host for this session is Kishan Iyer. [Video description ends]

In the previous demo, we saw how we can apply the technique of random oversampling. In order to effectively duplicate several rows in a dataset, which represent the minority class.

In this demo we will cover one more oversampling technique, specifically the synthetic minority oversampling, or SMOT. This works by creating synthetic observations based on the existing minority observations. So rather than simply replicating the data in the minority class, it'll create new data which belongs to that class.

Before we proceed, however, let us quickly remind ourselves of the distribution of data along the target column.

[Video description begins] A Jupyter notebook named ImbalancedData displays. A cell in the form of an empty input box displays with the command prompt: In [ ] : to the left of it. The cursor blinks in this input box. In the input box of the 32nd cell, he types and executes the following command: mf_train.target.value_counts( ). The number 32 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And we view that in our dataset, there are roughly twice as many patients without diabetes as there are patients with the disease.

[Video description begins] The output displays. It is a table of 2 rows and 2 columns. Below the table a line displays that reads: Name: Outcome, dtype: int 64. [Video description ends]

So moving along now to address the imbalance in our dataset using an oversampler, we will make use of the SMOTE oversampler. Which is available in our model frame's imbalance.over_sampling.SMOTE class. So we initialize this using the default constructor.

[Video description begins] In the input box of the next cell, he executes the following command: oversampler = mf_train. imbalance.over_sampling. SMOTE( ). He adds another line of command in the same cell: oversampler. The number 33 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And we can view all of the configuration parameters available for this particular oversampler.

[Video description begins] The output displays: SMOTE ( k _ neighbours = 5 , kind = ' deprecated ' , m _neighbours = ' deprecated ' , n _jobs = 1 , out _ step = ' deprecated ' , random _state = None , ratio = None , sampling _strategy = ' auto ' , svm _estimator= ' deprecated ' ). [Video description ends]

You will observe that a lot of these parameters have now been deprecated.

So now that we have our SMOTE oversampler, let us apply this on our training data. So we will call our training set's fit_sample method and pass to it our initialized SMOTE oversampler.

[Video description begins] In the input box of the next cell, he executes the following command: mf_oversamp = mf_train.fit_sample (oversampler). The number 34 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

Now that oversampling has been applied, we can take a look at the distribution of data based on the value in the target column.

[Video description begins] In the input box of the next cell, he executes the following command: mf_oversamp. target.value_counts( ). The number 35 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And just as with the random oversampler, we have an even split once more. So while the random oversampler made up the difference between the two

[Video description begins] The output displays. It is a table of 2 rows and 2 columns . Below the table is a line that reads: Name : Outcome, dtype: int 64. [Video description ends]

classes in our dataset. By duplicating values in the minority class, has the same technique been applied by the SMOTE sampler as well? Well, we will check for that by counting the number of duplicates

[Video description begins] In the input box of the next cell, he executes the following command: mf_oversamp. duplicated( ).sum( ) . The number 36 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

in our oversample data, and there are in fact none. So rather than simply replicating the minority observations,

[Video description begins] The output displays. It is zero. [Video description ends]

the SMOTE oversampler has generated some synthetic data which belongs to the minority class.

We will now generate a scatter plot to visualize the dataset which includes the newly added synthetic data. And we observe that when compared to the use of the random oversampler.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_oversamp.plot.scatter (x='Glucose', y='BMI', c='Outcome', cmap = 'rainbow') . He adds another line of command in the same cell: plt.show( ). The number 37 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

The red dots do seem to be a little more tightly packed. How does that affect the performance of a classifier which is built on this

[Video description begins] The output displays. It is a scatter diagram with a cluster of red and purple dots . BMI values are listed on the y axis and outcome values are listed on the x axis. There are more red dots in this diagram than purple dots. [Video description ends]

oversample data, though? Well, you simply recreate the estimator. So we rebuild this linear SVC estimator

[Video description begins] In the input cell of the next cell, he types and executes the following command : estimator = mf_oversamp. svn. linearsvc(max_iter=100000) . He adds another line of command in the same cell: mf _ oversamp . fit ( estimator ). The number 38 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

and then fit it to our new oversample data. And then following that,

[Video description begins] The output displays: LinearSVC (c=1.0, class_weight=none, dual = true, fit_intercept= true, intercept _ scaling=1, loss='squared _ hinge', max_iter=100000, multi_class='ovr', penalty='12', random_state=none, tol=0.0001, verbose=0). [Video description ends]

we will use our test data to make predictions using this estimator.

[Video description begins] In the input cell of the next cell, he types and executes the following command : predictions= mf_test.predict(estimator) . He adds another line of command in the same cell: predictions .head( ). The number 39 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And when we calculate the accuracy score, well coincidentally we get the exact same score as we did previously when we applied random oversampling on our training data.

[Video description begins] The output displays. It is 0.75757. [Video description ends]

However, this is not the only metric which is of importance to us. We would also like to calculate the precision and recall scores of this model on the test data.

[Video description begins] In the input box of the next cell, he executes the following command: print (' Precision: ', mf_test.metrics .precision _ score ( estimator ) ). He adds another line of command in the same cell: print ('Recall: ', mf_test.metrics . recall _ score ( estimator ). The number 40 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And the precision score which we get now is about 65%. Which is in fact a little less than what we saw previously when we applied random oversampling. On the other hand, the recall score is significantly higher. Up from about 52% to nearly 69%. So among patients with diabetes,

[Video description begins] The output displays: Precision: 0.6551 . Recall: 0.6867. [Video description ends]

this particular model using the SMOTE oversampler has been significantly better at predicting the occurrence of the disease. We can now view the confusion matrix in order to see how the predicted and actual values line up.

[Video description begins] In the input box of the next cell, he types and executes the following command : confusion_matrix= confusion matrix (mf_test.target.values, predictions.values). He adds another line of command in the same cell: confusion _matrix. The number 41 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And we see that among patients with diabetes, our model was successfully able to detect the presence of the disease in 57 out of the 83 patients.

[Video description begins] The output displays. It is a table of 4 rows and 4 columns that displays the predicted versus actual True and False values. [Video description ends]

5. Video: Undersampling Using imbalanced-learn (it_dsmdladj_04_enus_04)

Learn how to perform undersampling operations on a dataset by applying the Near Miss, Cluster Centroids, and Neighborhood Cleaning Rule techniques.
perform undersampling operations on a dataset by applying the Near Miss, Cluster Centroids, and Neighborhood Cleaning Rule techniques
[Video description begins] Topic title: Undersampling Using imbalanced-learn. Your host for this session is Kishan Iyer. [Video description ends]

We have previously seen how we can make use of oversampling in order to address the imbalance in our training data.

In this demo, we will take a look at some undersampling techniques where the imbalance in the data set is addressed by undersampling the majority class. We can continue in the same Jupyter notebook as we have used previously.

[Video description begins] A Jupyter notebook named ImbalancedData displays. A cell in the form of an empty input box displays with the command prompt: In [ ] : to the left of it. The cursor blinks in this input box. [Video description ends]

But first, we will remind ourselves of the distribution of all the data for each of the classes in our target column.

[Video description begins] In the input box of the 42nd cell, he types and executes the following command: mf_train.target.value_counts(). The number 42 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So there is a two to one split here with exactly 185 data points in the minority class.

[Video description begins] The output displays. It is a table with 2 rows and 2 columns. Below the table is a line that reads : Name: Outcome, dtype: int64. [Video description ends]

We will now go ahead and initialize our undersampler.

And the first technique we will apply is known as the near miss approach. In this technique,

[Video description begins] In the input box of the next cell, he types and executes the following command : undersampler = mf_train.imbalance.under_sampling.NearMiss(). He adds a second line of command in the same cell : undersampler. The number 43 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

only those samples from the majority class will be selected which happen to be rather close to the points belonging to the minority class. So this is a cluster based approach, where the distance is calculated between each of the points in the dataset. So once we initialize our NearMiss undersampler, we can take a look at some of the configurable parameters.

[Video description begins] The output displays: NearMiss(n_jobs=1, n_neighbors=3, n_neighbors_ver3=3, random_state=None, ratio=None, return_indices=False, sampling_strategy='auto', version=1). [Video description ends]

But following that, you will go ahead and apply this near miss undersampling on our training data.

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_undersamp = mf_train.fit_sample(undersampler). He adds a second line of command in the same cell : mf_undersamp.target.value_counts(). The number 44 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So we'll call the fit_samplemethod to which we pass along our initialized undersampler. And then we will count the distribution of data in each of the target classes after the undersampling. And what we observe is that there is once more an even split between the diabetic patients and a non diabetic ones. However, the imbalance has been addressed by undersampling the majority class data.

[Video description begins] The output displays. It is a table with three rows and two columns. Below the table is a line that reads : Name: Outcome, dtype: int64. [Video description ends]

So we still have a 185 patients with diabetes in this particular dataset. However, the number of non diabetic patients has been reduced to bring it to the same level as the diabetic ones. And when we check whether this transformation of the training data has resulted in any duplicate roles we see that there is no replicated data in this transformed dataset. So while this distribution of values is kind of expected with the under

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_undersamp.duplicated().sum(). The number 45 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is zero. [Video description ends]

sampling technique, what is of more interest to us is to see how the data points have been distributed. For that, we will generate the scatter plot once more. And what we observe here, is that all of the purple dots which were furthest

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_undersamp.plot.scatter(x = 'Glucose', y = 'BMI', c = 'Outcome', cmap = 'rainbow') . He adds a second line of command in the same cell :plt.show(). The number 46 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

away from the red dots have effectively been dropped from the dataset. So only those points from the majority class which can be considered to be near misses in terms of their proximity to the minority class points have been included in the undersample dataset. The distribution in data is made stark when you compare these undersample points on the left with the oversampled ones on the right. So now that we have applied the near miss method on our training data,

[Video description begins] The output displays. It is a scatter plot. The word, BMI is written next to the y-axis. BMI ranges from 0 to 70 and has 7 intervals of 10 each. This scatter plot contains a cluster of red and a cluster of purple dots. On the right side of the scatter plot, a color range, Outcome, is provided. This color range starts from 0.0 to 1.0 and has 5 intervals of 0.2 each. He also compares the code and its output with the code previously entered in the input cell 37 and its output, which is also a scatter plot. This comparison code is placed on the right side of the screen. [Video description ends]

how does this affect the quality of a model which we can build from it? Well, we will re-initialize our linear SVC estimator.

[Video description begins] In the input box of the next cell, he types and executes the following command : estimator = mf_undersamp.svm.LinearSVC(max_inter=10000). He adds a second line of command in the same cell :mf_undersamp.fit(estimator). The number 47 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And on this occasion, this estimator will be trained using our undersampled data. So once this training has been complete,

[Video description begins] The output displays: LinearSVC(C=1.0, class_weight=None, dual=True, fit_intercept=True, intercept_scaling=1, loss='squared_hinge', max_iter=10000, multi_class='ovr', penalty='12', random_state=None, tol=0.0001, verbose=0) . [Video description ends]

we can use it to make predictions on the test data. And we see that for the first five patients,

[Video description begins] In the input box of the next cell, he types and executes the following command: predictions = mf _test . predict ( estimator ). He adds another line of code in the same cell: predictions. head ( ). The number 48 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

our model has predicted that all of them have diabetes. We know from the previous examination of our test data that this is in fact not accurate.

[Video description begins] The output displays. It is a table with 2 columns and 5 rows. Below the table is a line that reads : dtype : int64. [Video description ends]

However, in order to calculate the accuracy score across the entire test data, we will make use of the accuracy_scoremetric.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ test . metrics . accuracy _ score ( estimator ). The number 49 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 0.5151. [Video description ends]

And this shows us that this particular model is accurate only 51% of the time across our test data. So this is clearly not a good score in terms of overall accuracy. However, what maybe more important in some cases are the precision and recall scores which we will estimate using the metrics for those.

[Video description begins] In the input box of the next cell, he executes the following command: print (' Precision: ', mf_test.metrics .precision _ score ( estimator ) ). He adds another line of command in the same cell: print ('Recall: ', mf_test.metrics . recall _ score ( estimator ). The number 50 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

And we get a precision value of about 42%. So when our model predicted that a patient has diabetes, it was accurate just 42% of the time. On the other hand, the recall score is extremely high. So among patients who did in fact have diabetes, our model estimated the presence of the disease nearly all the time.

[Video description begins] The output displays. It is Precision: 0.42408 and Recall : 0.9759. [Video description ends]

With such a low precision score however, there are clearly a lot of false positives, but how many exactly? Well, we can gather that by generating a confusion matrix for our test data and compare it with the predictions.

[Video description begins] In the input box of the next cell, he types and executes the following command: confusion_matrix = ConfusionMatrix ( mf _ test . target . values , predictions . values ). He adds another line of code in the same cell: confusion _ matrix. The number 51 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And we see that these are the true positives and the true negatives. However, the number of false positives is about 110 in this particular case. So clearly, at least in the case of this particular dataset,

[Video description begins] The output displays. It is a table of 4 rows and 4 columns that displays the predicted versus actual True and False values. [Video description ends]

the near miss undersampling technique will lead to a lot of false alarms. That is, a lot of patients will be scared into thinking they have diabetes, when in fact they don't. This is not a knock on the near miss method in general, just that it doesn't work for this particular data set. It is quite possible, however, that you will find use for it using some other data. It may also be the case that a particular undersampling technique will not work for your data but something else might. We will now see how we can make use of the cluster centroids technique, in order to under sample the majority class data. This method uses the k-means clustering algorithm in order

[Video description begins] In the input box of the next cell, he types and executes the following command: undersampler = mf _ train . imbalance . under _ sampling . ClusterCentroids ( ). He adds another line of code in the same cell: undersampler. The number 52 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

to find the cluster centroids for the majority class data. And while the cluster centroids are retained, the undersampling is performed by eliminating a lot of the other points which are very close to it. So in this way, the majority class data points will be much more evenly spread out in the data set. So once we initialize this undersampler, we can take a look at some of the configurable parameters.

[Video description begins] The output displays: ClusterCentroids(estimator=None, n_jobs=1, random_state=None, ratio=None, sampling_strategy='auto', voting='auto') . [Video description ends]

So we won't get into the details of that, but we will simply go ahead and apply this undersampler on our training data.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_undersamp = mf_train.fit_sample(undersampler) . He adds another line of command in the same cell: mf_undersamp = mf_train.fit_sample(undersampler). The number 53 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So just as before we call the fit_sample method and then count the number of data points in each target class. And we see that once more, there are exactly 185 samples in each class here. We check for duplicates in this data set, and there are none.

[Video description begins] The output displays. It is a table with 2 columns and 5 rows. Below the table is a line that reads :Outcome, dtype : int64. In the input box of the next cell, he executes the following command: mf_oversamp. duplicated( ).sum( ) . The number 54 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is zero. [Video description ends]

However, the most interesting thing for us is to visualize which of the majority class samples have been selected by plotting a scatter plot. And once this is generated we can see that the purple

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_undersamp.plot.scatter(x = 'Glucose', y = 'BMI', c = 'Outcome', cmap = 'rainbow') . He adds a second line of command in the same cell :plt.show(). The number 55 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

points representing the non-diabetic patients in the majority class are much more evenly distributed. Especially when compared to a near miss undersampling technique, whose scatter plot you can see on the right.

[Video description begins] The output displays. It is a scatter plot. The word, BMI is written next to the y-axis. BMI ranges from 0 to 70 and has 7 intervals of 10 each. This scatter plot contains a cluster of red and a cluster of purple dots. On the right side of the scatter plot, a color range, Outcome, is provided. This color range starts from 0.0 to 1.0 and has 5 intervals of 0.2 each. He also compares the code and its output with the code previously entered in the input cell 37 and its output, which is also a scatter plot. This comparison code is placed on the right side of the screen. [Video description ends]

In the cluster centroid plot, we see that the density of the purple dots is lower in the middle of the graph, where a number of points in close proximity to the centroids have been discarded. You will notice however, that there are a few purple dots which are still visible towards the right of the plot. These purple dots are surrounded by red dots and there is an undersampling technique which we can apply to get rid of those. So this is the neighbourhood cleaning rule which makes use of a technique called the edited nearest neighbor's rule. So this will go through each of the majority samples in the dataset and

[Video description begins] In the input box of the next cell, he types and executes the following command: undersampler = mf _ train . imbalance . under _ sampling . NeighbourhoodCleaningRule ( ). The number 56 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

examine its nearest neighbors. If the nearest neighbors happen to be from a different class, then that sample is dropped from the dataset. So let us apply this technique on our training data. So we call the fit_sample method once more and perform a count of the values. And from the output, we see that the majority class has been

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_undersamp = mf_train.fit_sample(undersampler) . He adds a second line of command in the same cell : mf_undersamp.target.value_counts(). The number 57 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

undersampled to the degree where it now becomes a minority.

[Video description begins] The output displays. It is a table with 2 columns and 2 rows. Below the table is a line that reads :Outcome, dtype : int64. [Video description ends]

We can confirm that there are no duplicates in this undersample dataset.

[Video description begins] In the input box of the next cell, he executes the following command: mf_oversamp. duplicated( ).sum( ) . The number 54 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is zero. [Video description ends]

And when we generate a scatter plot to see how the samples are distributed, we observe that there are now far fewer purple dots towards the right of this graph.

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_undersamp.plot.scatter(x = 'Glucose', y = 'BMI', c = 'Outcome', cmap = 'rainbow') . He adds a second line of command in the same cell :plt.show(). The number 59 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So those majority samples which were surrounded by minority samples, have been dropped. And this is how the undersampling has been performed. So we have now explored three different undersampling techniques

[Video description begins] The output displays. It is a scatter plot. The word, BMI is written next to the y-axis. BMI ranges from 0 to 70 and has 7 intervals of 10 each. This scatter plot contains a cluster of red and a cluster of purple dots. On the right side of the scatter plot, a color range, Outcome, is provided. This color range starts from 0.0 to 1.0 and has 5 intervals of 0.2 each. [Video description ends]

which are available in the imbalanced-learn library. There are several others which you can also use including one called the condensed nearest neighbors one-sided selection. And there is also a random undersampler. Based on the characteristics of your data set, one of these undersampling methods should be applicable in order to produce accurate classification models.

6. Video: Ensemble Classifiers for Imbalanced Data (it_dsmdladj_04_enus_05)

In this video, learn how to use the EasyEnsembleClassifier and BalancedRandomForestClassifier available in the imbalanced-learn library to build classification models with imbalanced data.
use the EasyEnsembleClassifier and BalancedRandomForestClassifier available in the imbalanced-learn library to build classification models with imbalanced data
[Video description begins] Topic title: Ensemble Classifiers for Imbalanced Data. Your host for this session is Kishan Iyer. [Video description ends]

So far in this course, we have been applying undersampling or oversampling techniques on our training data. And then feeding it into a classifier which we build on our own. This two-step process can be simplified, however, if we make use of one of the ensemble-based classifiers available within the imbalanced-learn library. To that, we can simply feed in our skewed data set. And these classifiers will perform an undersampling on their own, and then generate a classification model.

In this demo, we will cover the use of two of these classifiers available. These are the easy ensemble classifier and the balanced random forest classifier. To begin, we examine the distribution of values in our training data. So we count the number of samples in each class of a target value.

[Video description begins] A Jupyter notebook named ImbalancedData displays. A cell in the form of an empty input box displays with the command prompt: In [ ] : to the left of it. The cursor blinks in this input box. [Video description ends]

And we see that there are 352 patients without diabetes

[Video description begins] In the input box of the 61st cell, he types and executes the following command: mf_train.target.value_counts(). The number 61 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

and a 185 who have the disease. So there is some imbalance in this data set.

[Video description begins] The output displays. It is a table with 2 rows and 2 columns. Below the table is a line that reads : Name: Outcome, dtype: int64. [Video description ends]

Whereas previously we have used an oversampler or an undersampler to address this imbalance and then build a classification model. On this occasion we move straight to building the model itself. And we will make use of the easy ensemble classifier, which is included in the imbalanced-learn library and is part of the imblearn.ensemble module.

[Video description begins] In the input box of the next cell, he types and executes the following command: from imblearn.ensemble import EasyEnsembleClassifier. He adds a second line of command in the same cell : ensemble _ clf. The number 63 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So once we have imported this into our notebook we will initialize this classifier and set the number of estimators to be created to 20. So if you're familiar with ensemble learning, you will know that this works

[Video description begins] In the input box of the next cell, he types and executes the following command: ensemble_clf = EasyEnsembleClassifier(n_estimators = 20). The number 62 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

on the principle of having a number of weak learners whose combined efforts often produce very good classification results. The individual learners in the easy ensemble classifier, will be using the AdaBoost technique, and we will have a total of 20 of them. So once we initialize this classifier, we get all the configurable parameters for it. And then moving along, we will go ahead

[Video description begins] The output displays: EasyEnsembleClassifier(base_estimator=None, n_estimators=20, n_jobs=1, random_state=None, replacement=False, sampling_strategy='auto', verbose=0, warm_start=False). [Video description ends]

and fit this classifier to our training data. For that we simply call the fit method on our training data and pass to it the classifier we have just initialized.

[Video description begins] In the input box of the next cell, he types and executes the following command : mf_train .fit ( ensemble _ clf). The number 64 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And once this ensemble classifier is ready, we can go ahead and use it to make predictions on our test data. So we call the predict method from our test model frame.

[Video description begins] The output displays: EasyEnsembleClassifier(base_estimator=None, n_estimators=20, n_jobs=1, random_state=None, replacement=False, sampling_strategy='auto', verbose=0, warm_start=False) . [Video description ends]

This returns a model series with our predictions. And we examine the first five rows of it. And when you compare this output with the first five rows in our test data,

[Video description begins] In the input box of the next cell, he types and executes the following command: predictions = mf _test . predict ( ensemble _ clf ). He adds another line of code in the same cell: predictions. head ( ). The number 65 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

we see that it's a perfect match. So for this particular model, the first five predictions are accurate. However, this may just be misleading.

[Video description begins] The output displays. It is a table with six rows and two columns. The first row has values 556 and 0. The second row has values 214 and 1. The third row has values 536 and 0. The fourth row has values 705 and 0. The fifth row has values 712 and 1. Below the table is a line that reads: dtype: and int64. [Video description ends]

So let us calculate the accuracy for the entire test data. And this gives us a score of about 74%. So while this score is in line with what we saw when we applied oversampling

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ test . metrics . accuracy _ score (ensemble_clf ). The number 66 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 0.7359. [Video description ends]

on our training data, when we previously used the near miss undersampling technique, the accuracy was significantly lower. To get a complete evaluation for this model though, we will need to calculate the precision and recall values. And with a precision score of 0.61,

[Video description begins] In the input box of the next cell, he executes the following command: print (' Precision: ', mf_test.metrics .precision _ score ( estimator ) ). He adds another line of command in the same cell: print ('Recall: ', mf_test.metrics . recall _ score ( estimator ). The number 67 appears within the square brackets after the word 'In' in the command prompt next to this input box. [Video description ends]

we see that there are still a fair number of false positives. However, with a recall value of about 74%, our model does capture most instances where the patient does have diabetes. We can now generate a confusion matrix to see how these predictions line up

[Video description begins] The output displays. It is Precision: 0.61 and Recall : 0.7349. [Video description ends]

with the actual values. And we can see the high number of false positives here,

[Video description begins] In the input box of the next cell, he types and executes the following command: confusion_matrix = ConfusionMatrix ( mf _ test . target . values , predictions . values ). He adds another line of code in the same cell: confusion _ matrix. The number 68 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

which leads to the low precision score. So with the use of this easy ensemble classifier,

[Video description begins] The output displays. It is a table of 4 rows and 4 columns that displays the predicted versus actual True and False values. The first row has the following values: False, 109, 39, and 148. The second row has the following values: True, 22, 61, and 83. The third row has the following values: _all_, 131, 100, and 231. [Video description ends]

we do not need to explicitly perform an undersampling on our dataset. So this does save a lot of time when building a classification model using imbalanced data. Another ensemble classifier which is available in the IMB learn library is the BalancedRandomForestClassifier. This will use an ensemble of decision trees rather than add a boost learners in order to perform the classification.

[Video description begins] In the input box of the next cell, he types and executes the following command: from imblearn.ensemble import BalancedRandomForestClassifier. The number 69 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So let us import this into our notebook and then initialize this. And we don't pass any parameters explicitly. We simply make use of the default values to initialize this classifier, and then train it using our imbalanced training data. Following that, we can view all of the configurable parameters.

[Video description begins] In the input box of the next cell, he types and executes the following command: ensemble_clf = BalancedRandomForestClassifier ( ). He adds another line of code in the same cell: mf_train.fit(ensemble_clf). The number 70 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And there are many more in this case, when compared to the easy ensemble classifier. Moving on to the predictions using this balanced random forest classifier,

[Video description begins] The output displays: BalancedRandomForestClassifier(bootstrap=True, class_weight=None, criterion='gini', max_depth=None, max_features='auto', max_leaf_nodes=None, min_impurity_decrease=0.0, min_samples_leaf=2, min_samples_split=2, min_weight_fraction_leaf=0.0, n_estimators=100, n_jobs=1, oob_score=False, random_state=None, replacement=False, sampling_strategy ='auto', verbose=0, warm_start=False). [Video description ends]

we simply make use of the predict method of our test data. And then we move straight ahead to evaluating the accuracy of this model.

[Video description begins] In the input box of the next cell, he types and executes the following command: predictions = mf _test . predict ( ensemble _ clf ). The number 71 now appears within the square brackets after the word 'In' in the command prompt next to the input box. He enters the following line of code: predictions = mf_test.predict(ensemble_clf) [Video description ends]

And we get a score of about 75%, which is a shade better than what we saw for the easy ensemble classifier. Let us take a look at the precision and recall scores, however.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ test . metrics . accuracy _ score (ensemble_clf ). The number 72 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 0.7532. [Video description ends]

And the precision score is about the same.

[Video description begins] In the input box of the next cell, he executes the following command: print (' Precision: ', mf_test.metrics .precision _ score ( estimator ) ). He adds another line of command in the same cell: print ('Recall: ', mf_test.metrics . recall _ score ( estimator ). The number 73 appears within the square brackets after the word 'In' in the command prompt next to this input box. He enters two lines of code in the input cell. The first line is: print ('Precision: ', mf_test.metrics.precision_score(estimator)). The second line is: print ('Recall: ', mf_test.metrics.recall_score(estimator)). [Video description ends]

However, the recall score is about six points higher at nearly 80% for this particular model.

[Video description begins] The output displays. It is Precision: 0.6226 and Recall : 0.7951. [Video description ends]

So while the number of false positives in this case is roughly the same, the proportion of false negatives is a shade lower. We can get more details when we produce the confusion matrix, and

[Video description begins] In the input box of the next cell, he types and executes the following command: confusion_matrix = ConfusionMatrix ( mf _ test . target . values , predictions . values ). He adds another line of code in the same cell: confusion _ matrix. The number 74 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

we see that there are 17 false negatives in total. So with that, we have now covered two of the ensemble classifiers

[Video description begins] The output displays. It is a table of 4 rows and 4 columns that displays the predicted versus actual True and False values. The first row has the following values: False, 108, 40, and 148. The second row has the following values: True, 17, 66, and 83. The third row has the following values: _all_, 125, 106, and 231. [Video description ends]

which are available as part of the IMB learn library. Both of which apply the technique of under sampling on the data, and then make use of a number of ensemble learners.

There are other ensemble methods available within the IMB learn library. And this includes the balanced cascade, the balanced bagging classifier and also the random under sampling boost classifier. IMB learn also integrates with the deep learning frameworks, Keras and TensorFlow in order to make use of their utilities to deal with imbalanced data sets.

7. Video: Combination Samplers (it_dsmdladj_04_enus_06)

In this video, learn how to apply a combination of oversampling and undersampling using the SMOTE and Tomek techniques.
apply a combination of oversampling and undersampling using the SMOTETomek and SMOTEENN techniques
[Video description begins] Topic title: Combination Samplers. The host for this session is Kishan Iyer. [Video description ends]

Previously in this course, we have explored a few undersampling, as well as a handful of oversampling techniques in order to address the imbalance in our datasets. In this demo, we will explore a few options which are available to combine those two techniques in order to produce a balanced data set. The first of these we will explore is the SMOTETomek technique.

And this combines the SMOTE technique which we saw previously for oversampling and combines that with the Tomek links undersampling method. So while the SMOTE technique oversamples the minority class by generating synthetic data points, the Tomek links technique will remove a lot of the majority class samples which overlap with minority class samples. So the combined sampler we will now use is an instance of the class modelframe.imbalance.combine.SMOTETomek.

[Video description begins] A jupyter notebook named ImbalancedData, displays. He types and executes the following command: combined = mf _ train . imbalance . combine . SMOTETomek ( ). He adds another line of command in the same cell: combined. The number 75 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So once this sampler has been initialized, we will go ahead and

[Video description begins] The output displays: SMOTETomek ( random _state = None , ratio = None , sampling _strategy = ' auto ' , smote = None , tomek = None ). [Video description ends]

fit our training data to it.

[Video description begins] He executes the following command: mf _comb = mf _train . fit _sample ( combined ). He adds another command to the same cell : mf _ comb . tail ( ) . The number 76 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So once more, we call the fit_sample method and then examine the last five rows of our resulting dataset. So we see here that the outcome column contains all 1s, which is likely a product of the SMOTE oversampling technique. We then perform a count of the samples in each target class.

[Video description begins] The output displays. It is a table with 9 columns labeled Outcome, Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, DiabetesPedigreeFunction, and Age. There are 5 rows in the table. He executes the following command: mf _comb . target . value _ counts ( ). The number 77 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And we see that this is now a 50-50 split. But this has been achieved by oversampling the number of data points corresponding to a target value of 1.

[Video description begins] The output displays. It is a table with 2 columns and 2 rows. The table is followed by a line that reads : Name : Outcome, dtype : int64. [Video description ends]

So this has been up'd from about a 185 to 328. And the number of points corresponding to a target of 0 has been downsampled from about 352 to 328. Given that some oversampling was involved, it is good for us to check whether any rows were duplicated in the process.

[Video description begins] He executes the following command: mf _comb . duplicated( ). sum ( ). The output displays. It is zero. The number 78 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

But since the SMOTE method manufacturers synthetic data rather than simply replicating some of the rows which already exist, there are no duplicates in this data set. We can now visualize the distribution of points by making use of a scatter plot once more.

[Video description begins] He executes the following command: mf _comb . plot . scatter( x = ' Glucose ', y = ' BMI ' , c = ' Outcome ' , cmap = ' rainbow ' ). He adds another line of command in the same cell: plt . show ( ). The number 79 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And though we see that compared to the original data set, there are fewer purple dots towards the extreme right when we use the combined sampling. There are still more of these overlapping points in this combined sampler output when compared to the plot generated after applying the neighborhood cleaning rule, undersampling technique.

[Video description begins] The output displays. It is a scatter map with BMI on the y-axis and an unlabeled x-axis. Values on the y-axis range from 0 to 70. The right side of the plot has a legend in which Outcome from 0.0 to 1.0 is shown represented by different colors. He pastes the scatter plot from cell 59 outcome and compares the two plots. [Video description ends]

This is because the undersampling in a combined sampler resulted in only 24 points from the majority class being dropped. With our data now ready, we can go ahead and create our estimator and then evaluate it to see how well it performs using this combined sampling technique.

[Video description begins] He executes the following command: estimator= mf _ comb .svm. LinearSVC (max _iter = 10000 ). He adds another line of code in the same cell: mf _ comb . fit ( estimator ). The number 80 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So we initialize this linear SVC model and then we fit our training data to this estimator. Once the training is complete, we can use this model in order to make predictions which we will capture in this predictions model series.

[Video description begins] The output displays: LinearSVC ( C = 1.0, class _ weight = None , dual = True , fit _ intercept = True , intercept _ scaling 1 , loss = ' squared _ hinge ' , max _ iter = 10000 , multi _class = ' ovr ' , penalty = ' 12 ' , random _state = None, tol = 0.0001 , verbose= 0 ). The number 80 now appears within the square brackets after the word 'In' in the command prompt next to the input box. In the input box of the next cell, he executes the following command: predictions = mf _test . predict ( estimator ). He adds another line of code in the same cell: predictions. head ( ). The number 81 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And we get the first five values of the predictions here. I can tell you that four of these are in fact accurate.

[Video description begins] The output displays. It is a table with 2 columns and 5 rows. There is a line below the table that reads: dtype: int64. [Video description ends]

However, to get the big picture for the accuracy, we need to calculate the accuracy score across the entire test data set. And this gives us a score of about 66%, which is not exactly that great.

[Video description begins] He executes the following command: mf _ test . metrics . accuracy _ score ( estimator ). The number 82 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 0.66233. [Video description ends]

The previous models we used had accuracy scores in the high 70s. However, perhaps this can redeem itself by scoring well on the precision and recall scores.

[Video description begins] In the input box of the next cell, he types and executes the following command: print ( ' Precision : ' , mf _test . metrics . precision _ score ( estimator ) ) . He adds another line of command in the same cell : print ( ' Recall : ' , mf _test . metrics . recall _ score ( estimator ) ) . The number 83 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

In fact, the precision score is rather low at about 51% which shows that there were a lot of false positives. But a recall value of close to 94% shows that there were very few false negatives.

[Video description begins] The output displays: Precision : 0.51655 and Recall : 0.93975. [Video description ends]

We can generate the confusion_matrix and

[Video description begins] In the input box of the next cell, he executes the following command: confusion_matrix = ConfusionMatrix ( mf _ test . target . values , predictions . values ). He adds another line of code in the same cell: confusion _ matrix. The number 84 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

we can see the raw numbers behind these percentages. We move along now to explore one more combined sampler.

[Video description begins] The output displays. It is a table with 3 columns and 3 rows. The columns show the predicted values as false, true, and all. The rows show Actual values as false, true, and all. In the input box of the next cell, he types and executes the following command: combined = mf _train . imbalance . combine . SMOTEENN( ). He adds another command to the same cell : combined. The number 85 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And this combines the oversampling applied by the SMOTE technique with the undersampling performed by the ENN or Edited Nearest Neighbors method. The ENN method will remove those instances whose class label is different from those of its nearest neighbors. That is, if there are any samples which are surrounded by other samples of different classes, then that sample will be dropped from the data set. So let us employ this other combined sampler and then see how well it performs. So once this has been initialized,

[Video description begins] The output displays: SMOTEENN ( enn = None , random _state = None , ratio = None , sampling_strategy = ' auto ' , smote = None ). [Video description ends]

we will fit it to our training data and then perform a value count to see how many samples fall into each of the categories in our target column.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_comb = mf _train . fit _sample ( combined ). He adds another command to the same cell : mf _ comb . target . value _ counts ( ). The number 86 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And the result shows us that the minority class has now become the majority. In fact, this has been oversampled from a 185 to 206 points. Whereas the majority class has been undersampled from over 350 to just 155.

[Video description begins] The output displays. It is a table with 2 columns and 2 rows. There is a line below the table that reads : Nam : Outcome , dtype: int64. [Video description ends]

So this result in data set is also a little skewed, but in the opposite direction to what we started off with. Let us quickly check whether the oversampling resulted in any duplication.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _comb . duplicated( ). sum ( ). The output displays. It is zero. The number 87 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And the answer is no. We can now generate a scatter plot to see how the points are separated.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _comb . plot . scatter( x = ' Glucose ', y = ' BMI ' , c = ' Outcome ' , cmap = ' rainbow ' ). He adds another line of command in the same cell: plt . show ( ). The number 88 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And in fact, we see that the use of this SMOTE ENN technique results in a much wider separation of the points. There are no purple dots over on the right side of the plot and no red dots over to the left. That is a result of applying the Edited Nearest Neighbors technique, with those points which are surrounded by neighbors from a different class are dropped.

[Video description begins] The output displays. It is a scatter map with BMI on the y-axis and an unlabeled x-axis. Values on the y-axis range from 0 to 50. The right side of the plot has a legend in which Outcome from 0.0 to 1.0 is shown represented by different colors. He pastes the scatter plot from cell 79 outcome and compares the two plots. [Video description ends]

This is in fact a stark contrast to the previous use of a combined sampler, where a lot of the points were in fact overlapping. The big question, however, is how does this combined sampling technique affect the quality of the predictions made by a classifier which is built from it. So we recreate our linear SVC classifier and then fit it to the training

[Video description begins] In the input box of the next cell, he types and executes the following command: estimator= mf _ comb .svm. LinearSVC (max _iter = 10000 ). He adds another line of code in the same cell: mf _ comb . fit ( estimator ). The number 89 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

data, which has been transformed by means of this combined sampler. Once the model has been trained, we make the predictions using that once more. And then we get these first 5 predictions.

[Video description begins] The output displays: LinearSVC ( C = 1.0, class _ weight = None , dual = True , fit _ intercept = True , intercept _ scaling 1 , loss = ' squared _ hinge ' , max _ iter = 10000 , multi _class = ' ovr ' , penalty = ' 12 ' , random_state = None, tol = 0.0001 , verbose= 0 ). In the input box of the next cell, he executes the following command: predictions = mf _test . predict ( estimator ). He adds another line of code in the same cell: predictions. head ( ). The number 90 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is a table with 2 columns and 5 rows. There is a line below the table that reads: dtype: int64. [Video description ends]

And then we check the accuracy across the entire test set.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ test . metrics . accuracy _ score ( estimator ). The number 91 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 0.69696. [Video description ends]

So this score of nearly 70% is marginally better than what the previous model was able to produce. We'll now evaluate the precision and recall values. And the precision number is slightly higher,

[Video description begins] In the input box of the next cell, he types and executes the following command: print ( ' Precision : ' , mf _test . metrics . precision _ score ( estimator ) ) . He adds another line of command in the same cell : print ( ' Recall : ' , mf _test . metrics . recall _ score ( estimator ) ) . The number 92 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

indicating that there are fewer false positives. However, the recall value is lower by about nine percentage points, which shows that there are now more false negatives.

[Video description begins] The output displays: Precision : 0.5511 and Recall : 0.8433. [Video description ends]

And when we generate the confusion_matrix, we can see that there

[Video description begins] In the input box of the next cell, he types and executes the following command: confusion_matrix = ConfusionMatrix ( mf _ test . target . values , predictions . values ). He adds another line of code in the same cell: confusion _ matrix. The number 93 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

were a total of 57 false positives and 13 false negatives. So while the use of a combine sampler did not produce great results for this particular data set, these may in fact be the best option for a different data set.

[Video description begins] The output displays. It is a table with 3 columns and 3 rows. The columns show the predicted values as false, true, and all . The rows show Actual values as false, true, and all. [Video description ends]

8. Video: Finding Correlations in a Dataset (it_dsmdladj_04_enus_07)

In this video, find out how to use Pandas and Seaborn to visualize the correlation between fields in a dataset.
use Pandas and Seaborn to visualize the correlated fields in a dataset
[Video description begins] Topic title: Finding Correlations in a Dataset. The host for this session is Kishan Iyer. [Video description ends]

In this demo, we will explore the technique of principal component analysis in order to achieve dimensionality reduction. If we reduce the number of dimensions of any data set, it becomes easier to store the data. And if we wish to use that information in order to build and train a model, that process will also be quicker when we have fewer dimensions to work with.

In the case of data sets which have a very ClassificationWithPCA.large number of features, many of the features will in fact be highly colinear. And any issues arising out of multi colinearity can be eliminated by applying dimensionality reduction. To understand how exactly this can be applied, we will now create a new Jupyter notebook. And this I have named ClassificationWithPCA.

[Video description begins] A jupyter notebook named ClassificationWithPCA displays. A cell in the form of an empty input box displays with the command prompt: In [ ] : to the left of it. The cursor blinks in this input box. [Video description ends]

We begin by importing the libraries which we will require, starting with the pandas_ml library, and also the pandas library. I'm going to disable warnings in this notebook since the deprecation

[Video description begins] In the input box of the first cell, he executes the following command: import pandas _ ml as pdml. He adds another line of command in the same cell: import pandas as pd. The number 1 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

warnings thrown by some of the dependencies of the libraries we are using can be rather distracting.

[Video description begins] In the input box of the next cell, he types and executes the following command: import warnings warnings . filterwarnings ( " ignore " ). The number 2 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

We will now go ahead and input the data set we will need for this demo. This is known as the wine dataset in many locations.

[Video description begins] In the input box of the next cell, he types and executes the following command: wine_data = pd . read _ csv ( ' datasets / winequality - red . csv ' ). He adds another line of command in the same cell: wine _ data . head ( ). The number 3 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And this can be downloaded from www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009. This is also included as part of the course material and I'm loading it from my own file system, using the pandas read_csv method. Once this data is in a panda's data frame, we can examine the top five rows. And we can see exactly what this contains. These are various metrics which describe the properties of the wine.

[Video description begins] The output displays. It is a table with 12 columns labeled fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, density, pH, sulphates, alcohol, and quality. There are 5 rows in the table. [Video description ends]

What the acidity of the wine is, how much residual sugar it contains, the density and Ph of the wine as well as its alcohol content. All of these factors can in fact affect the quality of a red wine, and in fact the column on the extreme right contains a quality rating which ranges from 3 through 8.

We will be building a classification model in this demo, and the aim will be to use all of the features in order to predict the quality of the wine. We start off by understanding our data set by first examining its shape. So this contains nearly 1600 rows of data and a total of 12 columns. Out of these 11 are feature columns and then we have a single target column for the quality.

[Video description begins] In the input box of the next cell, he types and executes the following command: wine _ data . shape. The number 4 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 1599, 12. [Video description ends]

Given that this data set includes a lot of factors which may in fact be correlated. For example, the fixed acidity and the Ph of the wine, it makes sense to generate a correlation matrix to understand the degree of correlation.

[Video description begins] In the input box of the next cell, he types and executes the following command: wine _data . corr ( ) . The number 5 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

A correlation matrix can be generated for the contents of a pandas data frame by simply calling the core function for the data frame. So once we run this, we can see that along the diagonals, all the values are 1. And this is because it represents the correlation of one column with itself. However, to get the correlation between some of the other columns,

[Video description begins] The output displays. It is a 12 by 12 matrix showing correlation of the 12 parameters under consideration. [Video description ends]

we can take a look at the other cells. For example, the correlation value between the fixed acidity and the citric acid fields is 0.67. So they are not only positively correlated but there is a fairly high degree of positive correlation. There is a similar degree of correlation between the total sulfur dioxide and free sulfur dioxide columns in this data frame. You will also notice that a number of the fields are also negatively correlated.

When we have such a large number of features, it is often rather painstaking to sift through all of the numbers in order to find the correlation values between the fields. If we would like our attention to be drawn to those fields which are either very strongly positively or strongly negatively correlated, we can make use of a heat map.

To do that, we'll need to import a few other libraries. Firstly we'll need to make use of the matplotlib.pyplot object and also import the seaborn visualization library. Seaborn is what we will use to generate the heat map.

[Video description begins] In the input box of the next cell, he types and executes the following command: import matplotlib . pyplot as plt . He adds another line of command in the same cell: import seaborn as sns . The number 6 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So with that done, you'll first define the size of a plot. So I have defined a matplotlib figure object and initialized the figure size to 12 units wide and 7 units high. I have specified these dimensions so that the plot will fit on the screen in front of you. I'm also setting the font size so

[Video description begins] In the input box of the next cell, he types and executes the following command: plt . figure ( figsize = ( 12 , 7 ) ) . He adds a second line of command in the same cell:sns . set ( font _ scale = 0.9 ) . He adds a third line of command: sns . heatmap ( wine _data . corr ( ), vmax = 0.8 , square = True , annot = True , fmt = ' .2f ' , cmap = ' inferno ' ). He adds a fourth line of command : plt . show ( ). The number 7 now appears within the square brackets after the word 'In' in the command prompt next to the input box [Video description ends]

that the correlation values will be clearly visible. And then, we will generate the heat map using the seaborn heat map method. The data which which is fed into it is actually the correlation matrix which we saw previously for our wine_data dataframe.

And then we specify a number of parameters in order to format the look of the heat map. I will not get into the details of each of these parameters. But it will include the correlation values rounded to two decimal places. So once the heat map has been generated, we can see that the highly positively correlated fields are in light yellow. While the fields which are strongly negatively correlated appear in a darker shade.

[Video description begins] The output displays. It is a heatmap of the 12 parameters plotted against themselves. A legend on the right side shows the different colors that represent different correlation values ranging from -0.50 to 0.75, at increments of 0.25. [Video description ends]

So for example the correlation between the citric acid and the fixed acidity fields is 0.67, which is rather high. And the fixed acidity also seems to determine the density of the wine. And there are also fields which are negatively correlated. For example, the density and the alcohol columns.

If you were to build any machine learning model using a data set which includes a large number of very highly correlated fields, it could result in poor performance of the model due to multi collinearity. This issue can be mitigated by performing dimensionality reduction using some technique such as PCA. So that only the principal components of the data set will be used in order to train the model and then later to make predictions. So before we go ahead and build our model, we will create a pandas_ml model frame out of the contents of our data frame.

[Video description begins] In the input box of the next cell, he types and executes the following command: wine_mf = pdml . ModelFrame ( wine _ data .to _ dict ( ) ) . The number 8 now appears within the square brackets after the word 'In' in the command prompt next to the input box [Video description ends]

So we make use of the two_dict method so that the data frame contents are translated to a dictionary which we can use in order to initialize this model frame. And with the data loaded, we can examine the shape of the data portion of the model frame. Which is exactly the same as what we saw in our data frame. However, we will need to specify the target column for this data frame.

[Video description begins] In the input box of the next cell, he types and executes the following command: wine _ data . shape. The number 9 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 1599, 12. [Video description ends]

Which we do so by setting a value for the target_name field and

[Video description begins] In the input box of the next cell, he types and executes the following command: wine _ mf. target _ name = ' quality '. The number 10 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

this is going to be the quality column of this model frame. So once that is set, let us examine all of the unique values in this quality column.

[Video description begins] In the input box of the next cell, he types and executes the following command: wine _ mf . target . unique ( ). The number 11 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And the output shows us that there are six unique ratings for all of the wines in our data set.

[Video description begins] The output displays. It is an array with 6 values 5, 6, 7 , 4 , 8 , and 3. [Video description ends]

This ranges from a minimum of 3 up to a maximum of 8. So given there are 6 distinct values, if you were to blindly guess the quality rating for a particular wine, we should be accurate about 16% of the time. That'll serve as the baseline for the model we will build soon. So that needs to do significantly better than 16% in terms of prediction accuracy.

Moving along, we will now split this data set into training and test sets, for which we make use of the train test split method. Which is available in the model frames, model selection module. So here we specify that 30% of this data set should be reserved for testing.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ train , mf _ test = wine _ mf . model _ selection \ . train _ test _ split ( test _ size = 0.3 ). The number 12 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

Note that this train_test_split method will also shuffle the data set before it splits it up. So once the split is complete, we examine the shapes of the training and test sets.

[Video description begins] In the input box of the next cell, he types and executes the following command: print ( ' Training data shape : ' , mf _train . shape ). He adds another line of command in the same cell : print ( ' Test data shape : ' , mf _test . shape ) . The number 13 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And we see that the training set has a little over 1,100 rows of data and we have nearly 500 samples for testing.

[Video description begins] The output displays: Training data shape : ( 1119, 12 ) Test data shape : ( 480 , 12 ). [Video description ends]

9. Video: Building a Multi-Label Classification Model (it_dsmdladj_04_enus_08)

In this video, you will learn how to train and evaluate a classification model to predict the quality ratings of red wines.
train and evaluate a classification model to predict the quality ratings of red wines
[Video description begins] Topic title: Building a Multi-Label Classification Model. The host for this session is Kishan Iyer. [Video description ends]

Before we apply the technique of PCA in order to achieve dimensionality reduction, though, we will use all of the features available in order to build a classifier and then evaluate it. We will start off by initializing this classifier and we will be making use of the svm.svc classifier. So this is a support vector classifier. This is also accessible from the model frame.

So we initialize it with the default values. And following that, we will fit our training data to this classifier by calling the model frame's fit method. Once our trained classifier is ready, we can go ahead and

[Video description begins] A jupyter notebook named ClassificationWithPCA, displays. In the input box, he types and executes the following command: mf _ train .fit ( svc _ clf ). The number 15 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays: SVC ( C = 1.0, cache _ size = 200, class _ weight = None , coef 0 =0.0, decision _ function _ shape = ' ovr ' , degree = 3 , gamma = ' auto _ deprecated ' , kernel = ' rbf ' , max _ iter = -1 , probability = False , random_state = None , shrinking = True , tol = 0.001, verbose= False ). [Video description ends]

make predictions using that. So for that we invoke the predict method of the test data model frame.

[Video description begins] In the input box of the next cell, he types and executes the following command: predictions = mf _test . predict ( svc _ clf ) . He adds another line of code in the same cell : predictions .head ( ). The number 16 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And then pass along our initialized and trained classifier as argument. We will then preview the first five predictions made by this model. And we see that this includes wine which have been rated as either 5 or 6.

[Video description begins] The output displays: it is a table with 2 columns and 5 rows . The values in column 2 are 5 or 6. There is a line below the table that reads : dtype: int64. [Video description ends]

We can now quickly confirm the type of the mf_train variable just to ensure that it is indeed a ModelFrame. And then we move along, and then evaluate the model which we have just built.

[Video description begins] In the input box of the next cell, he types and executes the following command: type ( mf _ train ). The number 17 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays: pandas _ ml . core . frame . ModelFrame. [Video description ends]

To check the accuracy of this model's predictions against the test data,

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _test . metrics . accuracy _score ( svc _ clf ). The number 18 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

we reference the test ModelFrame's metrics.accuracy_score method. And the argument we pass to it is the classifier we have just initialized, and then trained with the training data. So we should expect that this model should do much better than 16% in terms of accuracy, given there are six different classes in the target column. And we get a score of about 55%.

So overall, this does seem to be a rather robust classifier. However, you see how all of the predictions are scattered? We can generate a confusion matrix, for which we import the confusion matrix class from the Pandas ML library. Following that, we create the confusion matrix by passing to it the actual

[Video description begins] In the input box of the next cell, he types and executes the following command: from pandas _ ml import ConfusionMatrix. The number 19 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

values of our target column and also the predictions made by our classifier. And then upon viewing this confusion matrix,

[Video description begins] In the input box of the next cell, he types and executes the following command: confusion_matrix = ConfusionMatrix ( mf _ test . target . values , predictions . values ). He adds another line of code in the same cell: confusion _ matrix. The number 20 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

we can see exactly what the actual values are for the ratings for all of the wines, and what our model has predicted. For example, there were 144 occasions when the wine was rated with

[Video description begins] The output displays. It is a table with 8 columns and 7 rows. The columns are named predicted actual, 3, 4, 5, 6, 7, 8, and all. The rows have values from 3 to 8 in the predicted actual column, at increments of 1, and the last row has the value all in this column. [Video description ends]

a quality of 5, and this is exactly what the model predicted, as well. There were 200 wines in the dataset, which had a rating of 6. On a 114 occasions our model also predicted a rating of 6. There were 82 instances where our model gave a rating of 5. And then 4 instances when our model rated the wine as 7. So these are the results of our model which was built using a support vector classifier where we did not perform any dimensionality reduction. Next, we will cover how we can implement dimensionality reduction using principal components analysis. And then see what effect it has on the performance of our classification model.

10. Video: Dimensionality Reduction with PCA (it_dsmdladj_04_enus_09)

In this video, you will transform a dataset containing multiple features to a handful of principal components and build a classification model using the reduced dimensions of the dataset.
transform a dataset containing multiple features to a handful of principal components and build a classification model using the reduced dimensions of the dataset
[Video description begins] Topic title: Dimensionality Reduction with PCA. The host for this session is Kishan Iyer. [Video description ends]

In the previous demo, we made use of the red wine dataset in order to build a classification model to predict the quality of the wines in the dataset. During that demo, we also visualized the correlations in the dataset using a heat map, and we saw that a number of the fields are in fact very strongly correlated.

In datasets with a very large number of features where there could be dozens, or even hundreds of them such strongly correlated features can lead to poor predictions from the models and this is due to multicollinearity. In this demo, we will see how this issue can be mitigated by extracting the principal components from the features of a dataset. That is, we will be performing dimensionality reduction. The technique we will apply in order to reduce the number of dimensions is principal components analysis, or PCA.

[Video description begins] A jupyter notebook named ClassificationWithPCA, displays. In the input box, he types and executes the following command: pca = mf _ train.decomposition.PCA ( n _ components = 8 ). The number 21 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So there is a PCA class available in the model frames, decomposition module. So here we initialize this principal component analyser, and we set it to extract eight principle components from the data. Once this has been initialized, we can apply the technique of PCA on the features of a dataset.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _train.data = mf_ train.data.fit_ transform ( pca ). He adds another line of command in the same cell: mf _train.data.head ( ). The number 22 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So here we overwrite the current features, which is available through the data field of our training data. This presently uses 11 features in total. And now we are going to make use of the PCA object in order to transform those into eight principal components. We do this by calling our training model frames, fit_transform method.

And we pass to it the PCA object which we have just initialized to extract eight principal components. Once this transformation has been applied, we can view the top five rows of the data frame. And we can now see how the 11 features, have been reduced to eight principal components.

[Video description begins] The output displays. It is a table with 8 columns labeled from 0 to 7. There are five rows with datasets for 428, 544, 948, 1367, and 1289. [Video description ends]

So the 11 dimensional dataset has now been reduced to 8 dimensions. And the values in each dimension have also been scaled. One of the reasons for performing dimensionality reduction is that just a handful of the principal components may explain much of the variance in the underlying data. In fact, in order to view the variance explained by each of the dimensions we can access the explained_variance_field of this PCA object.

[Video description begins] In the input box of the next cell, he types and executes the following command: pca . explained _variance_. The number 23 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

When dimensionality reduction is performed using PCA, then the principal components are arranged in the decreasing order of their explained variance. And in fact, this is exactly what we see with the first of these components, explains most of the variance in the data.

[Video description begins] The output displays. It is an array of values such as 1.13004632e + 03. The variance component decreases from 03 to - 02. [Video description ends]

The second component also explain some of the variance, but not as much as the first one. And the explained variance numbers keeps decreasing right up to the last principal component. This is raw number for the explained variance can be somewhat confusing, which is why we have a field called the explained variance ratio.

[Video description begins] In the input box of the next cell, he types and executes the following command: pca . explained _variance _ ratio _ . The number 24 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And this shows us the proportion of the variance which is explained by each of the principal components. In fact, the first principle component explains nearly 95% of the variance in the underlying data. The explained variance for the second principal component is a shade under 5%. And between the first two principal components, nearly all of the variance in the data can be explained. We can also visualize the Explained Variance Ratios in

[Video description begins] The output displays. It is an array of values. The first value is 9.47113153 e - 01. [Video description ends]

something known as a scree plot. So we will make use of the matplotlib visualization library in order to plot the Explained Variance Ratios for each of the Dimensions. So here the x-axis will represent each of the principal components, and the y

[Video description begins] In the input box of the next cell, he types and executes the following command: plt . plot ( pca . explained _variance _ ratio _ ) . Then, he adds two lines of command in the same cell. The first line is : plt . xlabel ( ' Dimension ' ). The second line is : plt . ylabel ( ' Explain Various Ratio ' ). Then, he adds another line of command in the same cell: plt . show ( ). The number 25 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

axis represents the Explained Variance Ratios for each of those components. So this will be a line plot which is generated. And from the output, we can see that following the first principal component, there is a precipitor's drop. That is we drop from nearly 95% to a shade below 5%. In fact, following the third principal component,

[Video description begins] The output displays. It is a 2-dimensional line graph with explain various ratio plotted on the y-axis and dimension on the x-axis. The values on the x-axis range from 0 to 7 and those on the y-axis from 0.0 to above 0.8. The line graph starts from a high above 0.8 for dimension value equal to 0, and drops down to nearly 0 for dimension value equal to 1. Then, it shows a further drop to 0 at dimension value 2. Thereafter, it becomes a horizontal line for the rest of the dimensions. [Video description ends]

the remaining ones hardly explain any of the variance in the data. Looking at the scree plot, there is a case to be made that we can reduce the number of dimensions even further from 8 to perhaps 2 or 3. However we will first test, how well a model performs when it is trained using eight principal components.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _train . target . head ( ). The number 26 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is a table with 2 columns and 5 rows. Below the table is a line that reads : Name : quality, dtype : int64. [Video description ends]

So while we transform the data field of this mf_train model frame to include eight principal components, we will first ensure that the target column has not been affected. So the target column still contains the raw values for the wine quality ratings. Following that, we will now go ahead and initialize our support vector classifier model.

[Video description begins] In the input box of the next cell, he types and executes the following command: estimator= mf _ train .svm. SVC ( ). The number 27 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So once this is created, we will train this model using the eight principal components which have been extracted from our data set. Once the training has been completed we can now use this model in order to

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _train . fit ( estimator ). The number 28 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

make predictions. But before we do that, we will also need to apply TCA on our test data.

[Video description begins] The output displays: SVC ( C = 1.0, cache _ size = 200, class _ weight = None , coef 0 =0.0, decision _ function _ shape = ' ovr ' , degree = 3 , gamma = ' auto _ deprecated ' , kernel = ' rbf ' , max _ iter = -1 , probability = False , random_state = None , shrinking = True , tol = 0.001, verbose= False ). In the input box of the next cell, he types and executes the following command: mf _test . data = mf _ test . data . fit _transform ( pca ). The number 29 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

That is, we will need to extract eight principal components from our test set since our model now expects eight input features. So after transforming our test data we will use that in order to make predictions.

[Video description begins] In the input box of the next cell, he types and executes the following command: predictions = mf _test . predict ( estimator ). He adds another line of code in the same cell: predictions. head ( ). The number 30 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So we capture the predictions in this predictions model series, and preview it's first five rows, and we see that the wine quality has been predicted to be either five, six, or seven.

[Video description begins] The output displays. It is a table with 2 columns and 5 rows. The values in column 2 are 5, 6, or 7. Below the table is a line that reads : dtype : int64. [Video description ends]

So this does appear some what promising so far. However, it is now time for us to calculate the accuracy across the entire test set.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ test . metrics . accuracy _ score ( estimator ). The number 31 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 0.5375. [Video description ends]

So we make use of the accuracy_score method, available as part of the metrics. And this accuracy of nearly 54% is very much the same as what we saw previously when we used all of the 11 input features. So in spite of using eight principal components rather than 11 input features, the accuracy of the model is pretty much the same. Let us now generate a confusion metrics to see exactly what the distribution of the predictions and actual value are.

[Video description begins] In the input box of the next cell, he types and executes the following command: confusion_matrix = ConfusionMatrix ( mf _ test . target . values , predictions . values ). He adds another line of code in the same cell: confusion _ matrix. The number 32 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And we see that this is not that much different from what we saw previously.

[Video description begins] The output displays. It is a table with 8 columns and 7 rows. The columns are named predicted actual, 3, 4, 5, 6, 7, 8, and all. The rows have values from 3 to 8 in the predicted actual column, at increments of 1, and the last row has the value all in this column. [Video description ends]

So just a shade of a half of the scores have been predicted perfectly, and when the predictions were inaccurate, they were not really off by much. So in spite of performing dimensionality reduction, we see that the performance of the model has not really been affected. We will now see if we can reduce the number of dimensions even further, and see how that affects the performance of the model.

So here we will need to regenerate our training and test sets since we previously transform those to eight principal components. So we take the original model frame and then use the train test split method once more in order to generate a train and test sets. Following that, we need to create the PCA object, and on this occasion, when we initialize it, we say that we need it to extract just three principal components from the data.

[Video description begins] In the input box of the next cell, he types and executes the following command: pca = mf _train . decomposition . PCA ( n _ components = 3 ). He adds another line of code in the same cell: mf _train.data = mf_ train.data.fit_ transform ( pca ). He adds a second line of command in the same cell: mf _train.data.head ( ). The number 34 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

We then perform dimensionality reduction on our training data, and use the PCA object for that. And following this when we preview the first five rows, we see that the features have now been reduced to three principal components.

[Video description begins] The output displays. It is a table with 3 columns for the 3 principle components, 0, 1, and 2. There are 5 rows in the table. [Video description ends]

We will once again generate a scree plot to see how much each of the principal components explain the underlying variance.

[Video description begins] In the input box of the next cell, he types and executes the following command: plt . plot ( pca . explained _variance _ ratio _ ) . Then, he adds two lines of command in the same cell. The first line is : plt . xlabel ( ' Dimension ' ). The second line is : plt . ylabel ( ' Explain Various Ratio ' ). Then, he adds another line of command in the same cell: plt . show ( ). The number 35 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And we notice that this is very similar to what we saw previously. There's a very sharp drop from the first principal component to the second one. And now, it's time for

[Video description begins] The output displays. It is a 2-dimensional line graph with explain various ratio plotted on the y-axis and dimension on the x-axis. The values on the x-axis range from 0.00 to 2.00, at increments of 0.25, and the values on the y-axis range from 0.0 to above 0.8, at increments of 0.2. The line graph starts from a high above 0.8 from y-axis and then drops to 1.00 on x-axis. it furthers drops to 2.00 on the x-axis. [Video description ends]

us to check whether this transformation will affect the quality of the model.

[Video description begins] In the input box of the next cell, he types and executes the following command: estimator= mf _ train .svm. SVC ( ). He adds another line of code in the same cell: mf _ train . fit ( estimator ). The number 36 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

So we will now re-create this model, and then we will train it using the three principal components in our training data.

[Video description begins] The output displays: SVC ( C = 1.0, cache _ size = 200, class _ weight = None , coef 0 =0.0, decision _ function _ shape = ' ovr ' , degree = 3 , gamma = ' auto _ deprecated ' , kernel = ' rbf ' , max _ iter = -1 , probability = False , random_state = None , shrinking = True , tol = 0.001, verbose= False ). [Video description ends]

Once the model has been trained, we will transform the test data as well to three principal components. And then use that in order to make predictions using our classifier.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _test . data = mf _ test . data . fit _transform ( pca ). He adds a line of code in the same cell: predictions = mf _test . predict ( estimator ). He adds another line of code in the same cell: predictions. head ( ). The number 37 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

Examining the first five predictions, we see that our model has rated the wines 5 or 6.

[Video description begins] The output displays. It is a table with 2 columns and 5 rows. The values in column 2 are 5 or 6. Below the table is a line that reads : dtype : int64. [Video description ends]

We can now check the accuracy of the model across the entire test data, and

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ test . metrics . accuracy _ score ( estimator ). The number 38 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 0.4125. [Video description ends]

on this occasion, we get a significantly lower accuracy score. So this has dropped from nearly 54% to about 41%. To see exactly where the accuracy has gone off, we can generate a confusion matrix.

[Video description begins] In the input box of the next cell, he types and executes the following command: confusion_matrix = ConfusionMatrix ( mf _ test . target . values , predictions . values ). He adds another line of code in the same cell: confusion _ matrix. The number 39 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And from the output, we can see that when the actual quality rating for the wine was 6. There were a 124 occasions when our model rated the wine as a 5, and there were just 57 occasions when they were accurately labeled as 6.

[Video description begins] The output displays. It is a table with 8 columns and 7 rows. The columns show the predicted values from 3 to 8 and all the values in the last column. The rows Actual values from 3 to 8 , at increments of 1, and the last row has the value all in this column. [Video description ends]

So this seems to be the biggest difference between our current model with three dimensions versus the earlier one with eight. For wines with a rating of 5, there were 205 such samples in our test set, and a 136 of them were currently identified as 5. So even when reducing the number of dimensions from the original 11 to 3, a model still performs reasonably well.

11. Video: Imbalanced Learn and PCA (it_dsmdladj_04_enus_10)

In this video, you will learn how to use oversampling and PCA together to build a classification model.
combine the use of oversampling and PCA in building a classification model
[Video description begins] Topic title: Imbalanced Learn andPCA. The host for this session is Kishan Iyer. [Video description ends]

Previously in this learning path, we have covered the use of the imbalanced learn library in order to work with imbalanced datasets. That is, datasets where the samples are not evenly distributed among the different classes in the target column. In the red wine dataset we have been using so far in this course, we have seen that most of the wines in the dataset have a rating of either five, six or seven. Wines with ratings of 3, 4, and 8 are rather rare.

And as a result, our model does not really make predictions which fall into those categories. In this demo, we will make use of an over-sampler and then combine it with principal components analysis to work with data with more evenly distributed samples. And also reduce the number of dimensions in the input data. So we can create a new Jupyter Notebook for this particular demo. And I have called this ImbalancedLearnAndPCA since we will be combining two of the techniques we have covered during this learning path,

[Video description begins] A jupyter notebook named ImbalancedLearnAndPCA, displays. A cell in the form of an empty input box displays with the command prompt: In [ ] : to the left of it. The cursor blinks in this input box. [Video description ends]

working with imbalanced data and principle components analysis to achieve dimensionality reduction. We begin by importing all of the libraries which we need including pandas_ml, pandas matplotlib.pyplot object, the ConfusionMatrix. And I'm also disabling warnings for myself. Following that, we load the contents of the winequality

[Video description begins] In the input box of the first cell, he types and executes a command: import pandas _ ml as pdml. He adds another line of command in the same cell: import pandas as pd. He adds another line of command in the same cell: import matplotlib . pyplot as plt from pandas _ ml import ConfusionMatrix. Finally, he adds a fourth line of command in the same cell: import warnings warnings.filterwarnings ( " ignore " ). The number 1 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

dataset from the CSV file into a Pandas dataframe.

[Video description begins] In the input box of the next cell, he types and executes a command: wine _ data = pd . read _ csv ( ' datasets / winequality - red . csv ' ). [Video description ends]

And then we initialize a new model frame with its contents by passing along the dataframe contents as a dictionary.

[Video description begins] He adds another line of command in the same cell: wine _ mf = pdml . ModelFrame ( wine _ data . to _ dict ( ) ). [Video description ends]

So once our model frame has been initialized, we can examine the first five rows, and this is exactly what we saw previously in this course.

[Video description begins] He adds a second line of command in the same cell: wine _ mf . head ( ). The number 2 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is a table with 12 columns . The columns are labeled fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates, alcohol, and quality. The rows are labeled 0 to 4, at increments of 1. [Video description ends]

We will now move along and then define the target for this particular model frame, which is the quality column. So we access the target_name field of the model frame and set it to quality.

[Video description begins] The quality column is highlighted. It has values 5, 5, 5, 6, and 5 in respective 5rows. In the input box of the next cell, he types and executes a command: wine _mf . target _ name = ' quality ' . The number 3 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And then following that, our model frame is ready, and we can split it into train and test sets using the train-test-split method.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ train , mf _ test = wine _ mf . model_selection \ . train _ test _split ( test _ size = 0.3 ). The number 4 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

Just as we did previously, we reserve 30% of the data for testing. Now, just to examine the distribution of all of the data in the different categories of quality, we will perform a value counts operation on the target column. And the output confirms to us, that overwhelmingly,

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ train . target . value_ counts ( ). The number 5 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

the wines in our dataset have a quality rating of either 5 or 6. There are several wines rated 7, but there are very few which are rated 3, 4 or 8.

[Video description begins] The output displays. It is a table with 2 columns and 6 rows. The values in column 1 are 5, 6, 7, 4, 8, and 3 in respective rows. Below the table is a line that reads : name quality, dtype : int64. [Video description ends]

Now, there will be cases where you would like your model to detect the truly exceptional wines. Those which are exceptionally good and those which are terrible. So we would like our model to make more predictions of 3, 4, and 8. Rather, we need more accurate predictions in those categories. We will now check whether oversampling in those categories will lead to better predictions for wine ratings of 3, 4 and 8. So here, we make use of a random oversampler. This will effectively duplicate the samples in the underrepresented

[Video description begins] In the input box of the next cell, he types and executes the following command: combined = mf _train . imbalance . over _sampling . RandomOverSampler ( ). He adds another command to the same cell : combined. The number 6 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

categories, so that there is a more even distribution in the dataset. So we initialize this oversampler by calling the model frames imbalance.over_sampling.RandomOverSampler constructor. And with the oversampler initialized,

[Video description begins] The output displays : RandomOverSampler ( random _state = None , ratio = None , return _ indices = False , sampling _strategy = ' auto ' ). [Video description ends]

we can pass along our training data to it. So we call our training model frames fit_sample method, to which we pass along our oversampler.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf_comb = mf _train . fit _sample ( combined ) . He adds another command to the same cell : mf _ comb . tail ( ). The number 7 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

We then examine the last five rows of the resultant model frame, and we see that the wine quality rating is 8 for all of them. So these are the new data points which have been inserted into our model frame.

[Video description begins] The output displays. It is the same table as before. [Video description ends]

We also notice that it now contains over 2,700 rows of data. This is compared to the original size of a little over 1,100 rows. So now that we have performed the oversampling, we can take a look at the number of data points in each of the target classes. So we make use of the value counts method for that, and

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ comb . target . value _ counts ( ). The number 8 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

we observe that there are exactly 461 samples in each class over here.

[Video description begins] The output displays. It is a table with 2 columns and 6 rows. The values in column 1 are 7, 5, 3, 8, 6, and 4 in respective rows. All the rows have value 461 in column 2. Below the table is a line that reads : name quality, dtype : int64. [Video description ends]

But how many of these are duplicated?

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ comb . duplicated ( ) . sum ( ). The number 9 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

Well, a full 1776 of them are in fact rows which have been replicated from the original model frame. When we examine the first five rows of the model frame,

[Video description begins] The output displays: 1776. [Video description ends]

we notice that this is exactly the same. So the oversampling has not affected the beginning of the model frame.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ comb . head( ). The number 10 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is the same table as shown before. [Video description ends]

Well, now that we have performed an oversampling, we will perform one more transformation of our data. And on this occasion, we would perform a dimensionality reduction using the principle components analysis technique.

[Video description begins] In the input box of the next cell, he types and executes the following command: pca = mf _comb . decomposition . PCA ( n _ components = 3 ). [Video description ends]

We first initialize the PCA object, so that it can extract the three most significant principle components from the dataset. We follow that up by passing along our oversampled data to this PCA object. So that it's 11 features will be reduced to its 3 principle components.

[Video description begins] He adds another line of code in the same cell: mf _comb.data = mf_ comb.data.fit_ transform ( pca ). [Video description ends]

And then following that, we view the first five rows of this transform dataframe. And we see the 3 principle components here along with the target column.

[Video description begins] He adds a third line of command in the same cell: mf _comb.data.head ( ). The number 10 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is a table with 4 columns labeled quality, 0, 1, and 2. [Video description ends]

So now that we have the principle components, we can generate a scree plot once more just to view the explained variance for

[Video description begins] In the input box of the next cell, he types and executes the following command: plt . plot ( pca . explained _variance _ ratio _ ) . [Video description ends]

each of the principal components. So once more, we will plot along the x axis the dimensions and the y axis will represent the explained variance scores.

[Video description begins] Then, he adds two lines of command in the same cell. The first line is : plt . xlabel ( ' Dimension ' ). The second line is : plt . ylabel ( ' Explain Various Ratio ' ). Then, he adds another line of command in the same cell: plt . show ( ). The number 11 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And then once more we see that the first principal component explains nearly all of the variance in the data. The second dimension represents some of it, and then the third dimension explains nearly none of the variance. So now that we have prepared our data, by first applying an over sampler, and

[Video description begins] The output displays. It is a 2-dimensional line graph with explain various ratio plotted on the y-axis and dimension on the x-axis. The values on the x-axis range from 0.00 to 2.00, at increments of 0.25, and the values on the y-axis range from 0.0 to above 0.8, at increments of 0.2. The line graph starts from a high above 0.8 from the y-axis dimension and drops down to nearly 0 on the x-axis. Then, it shows a consistent drop till it reaches 0 at dimension value 2 on the x-axis. [Video description ends]

then applying dimensionality reduction, we can now go ahead and initialize our classifier. Following the initialization,

[Video description begins] In the input box of the next cell, he types and executes the following command: estimator= mf _ comb .svm. SVC ( ). He adds another line of code in the same cell: mf _ comb . fit ( estimator ). The number 12 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

we will fit the classifier to our training data. And this data you will remember contains three dimensions, and a more balanced distribution of the samples across all the target classes.

[Video description begins] The output displays: SVC ( C = 1.0, cache _ size = 200, class _ weight = None , coef 0 =0.0, decision _ function _ shape = ' ovr ' , degree = 3 , gamma = ' auto _ deprecated ' , kernel = ' rbf ' , max _ iter = -1 , probability = False , random _state = None , shrinking = True , tol = 0.001, verbose= False ). [Video description ends]

So now that we have a train model, we can use it for predictions, but we first need to transform the test data into three dimensions.

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _test . data = mf _ test . data . fit _transform ( pca ). [Video description ends]

Following that, we will make the predictions using our estimator.

[Video description begins] He adds a line of code in the same cell: predictions = mf _test . predict ( estimator ). He adds another line of code in the same cell: predictions. head ( ). The number 14 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And then, previewing the predictions, we see that the wine qualities have been predicted as either 5 or 6, at least in the first five rows. Following that, we can evaluate the model by checking

[Video description begins] The output displays. It is a table with 2 columns and 5 rows. The values in column 2 are 5 or 6. Below the table is a line that reads : dtype : int64. [Video description ends]

its accuracy across the test data. And we get a score of nearly 44%, so this is a little better than the 41% we

[Video description begins] In the input box of the next cell, he types and executes the following command: mf _ test . metrics . accuracy _ score ( estimator ). The number 15 now appears within the square brackets after the word 'In' in the command prompt next to the input box. The output displays. It is 0.4375. [Video description ends]

saw when we previously used 3 dimensions, without applying any oversampling. However, the difference in accuracy score is not that significant. We can now generate the ConfusionMatrix and check whether this model is any better than the previous ones we have built in detecting the exceptional wines. Both the exceptionally good ones and the exceptionally bad ones.

[Video description begins] In the input box of the next cell, he types and executes the following command: confusion_matrix = ConfusionMatrix ( mf _ test . target . values , predictions . values ). He adds another line of code in the same cell: confusion _ matrix. The number 16 now appears within the square brackets after the word 'In' in the command prompt next to the input box. [Video description ends]

And from this output, we can see all of the predicted values, which are represented along the columns, and the actual values along the rows. And as expected, there are lot of wines which are rated 5 and 6, and our model has predicted those ratings accurately. When it comes to the extreme values however, it seems that this model does not do a particularly good job in detecting the exceptional wines.

For example, our model just made two predictions of 3 as the quality of the wine. One of them was actually rated 7 and the other was rated 5. There were four wines in the dataset which were rated as 8 and our model has rated them 3 or 6.

[Video description begins] The output displays. It is a table with 8 columns and 7 rows. The columns show the predicted values from 3 to 8 and all the values in the last column. The rows Actual values from 3 to 8 , at increments of 1, and the last row has the value all in this column. [Video description ends]

So we have now seen how we can combine the techniques of oversampling and principal component analysis in order to achieve dimensionality reduction, and then build a classification model. Though the model did not perform as well as we might have hoped, this could be done to a number of different factors.

And perhaps using a different sampler, rather than a random oversampler, will improve the model's accuracy. Given the vast array of samplers which are available in the Imbalanced Learn Library, you could try each of them on this particular dataset to see if they produce a better result.

12. Video: Exercise: Working with Imbalanced Datasets (it_dsmdladj_04_enus_11)

Upon completion of this video, you will be able to recall the techniques used by algorithms for undersampling and oversampling data, as well as the use of combined samplers.
recall the techniques used by algorithms for undersampling and oversampling data and the use of combined samplers
[Video description begins] Topic title: Exercise: Working with Imbalanced Datasets. Your host for this session is Kishan Iyer. [Video description ends]

In this exercise, you will distinguish between two of the oversampling techniques which we covered during this course, the RandomOverSampler, and SMOTE. Both of these approaches address the imbalance in a dataset by generating more samples which belong to the minority classes. However, there is a clear distinction in the way they generate these instances. You will need to identify what the differences are.

For the next task, you will identify some of the undersampling techniques which are available in the Imbalanced Learn Library. There were three different undersamplers which we used during this course, and there were a few more which I had mentioned. You will need to recollect the three undersamplers which we used, and then there are bonus points if you can identify a few more.

For the next task, you will recall some of the combined samplers which we used during this course. So these will combine both oversampling as well as undersampling techniques in order to address the imbalance in the dataset. What exactly are these combined samplers though?

And finally, you'll identify one method of viewing the correlations in your dataset using both the Pandas and the Seaborn libraries. If you're making use of a dataset with a large number of columns, many of those are likely to be correlated with each other. When there are many fields which are strongly correlated, there is a case to be made that some of those features need to be dropped.

Or alternatively, you could make use of dimensionality reduction using some technique such as principal components analysis in order to extract a certain number of principal components from your dataset, rather than using the features in their current form. However, before you go down either of those paths, it is best to visualize the correlations in your dataset.

So that you know whether it'll be worthwhile in trimming the features or applying dimensionality reduction. How would you do this using Pandas and Seaborn? All of these topics were discussed during this course. So please pause this video, and then take some time to perform these tasks on your own. For the first task, you needed to distinguish between two of the oversamplers which we used during this course, the RandomOversampler and

[Video description begins] Solution [Video description ends]

the synthetic minority oversampling technique or SMOTE. So while both of these techniques generate new samples which belong to the minority classes in your dataset, in the case of the RamdomOverSampler, the technique which is adopted is rather naive. In fact, it simply duplicates the samples from the underrepresented classes which are already present in your dataset.

And the number of rows which are replicated will depend on what is required in order to make your dataset balanced. However, in the case of the SMOTE technique, this will generate entirely new data and these synthetic samples are created by using interpolation. These samples will belong to the minority classes. And once again, the number of samples will be determined by what is required in order to make your dataset balanced. When we did use SMOTE, we noticed that there were no duplicates which were created in our dataset.

For the next task, you needed to recall some of the undersampling techniques which were employed during this course. The first technique which we adopted was the NearMiss approach. This is where those samples which belong to the majority class and happen to be closest in distance to the minority class samples are the ones which are retained in the dataset. Whereas the others are dropped.

The name is due to the fact that the retained samples are the ones which qualify as near misses, where they could very easily have belonged to one of the other classes. One more undersampler which we applied was the ClusterCentroids technique. And in this case, a clustering algorithm such as k-means is applied on the majority class samples. The number of clusters generated is equal to how many samples from the majority are required in order to create a balanced dataset.

And then all the majority class samples are dropped and then replaced by the ClusterCentroids. We also took a look at the NeighbourhoodCleaningRule which makes use of the ENN or edited nearest neighbor's technique in order to drop those majority class samples which are surrounded by instances of the minority class. So while these were the three undersamplers which we used in the course, there are several others which are available in the Imbalance Learn Library.

This includes the RandomUnderSampler which, as the name suggests, will randomly drop samples which belong to the majority class. There is also the TomekLinks approach where all samples which are very close to other samples belonging to a different class are dropped from the dataset. And then there is also the EditedNearestNeighbours approach, and this is something which is used by the neighborhood cleaning rule. But we can also make use of it directly and then configure its parameters according to our requirement.

For the next task, you needed to identify the combined samplers which we used during the course. Combined samplers, as the name implies, will combine the use of undersampling as well as oversampling in order to address the imbalance in a dataset. As of this recording, there were two combined samplers available in the Imbalance Learn Library, both of which were used during this course.

The first of those was the SMOTETomek combine sampler. And the name gives away the fact that it uses SMOTE in order to oversample the underrepresented classes, and then applies Tomek links in order to perform an undersampling. There is also the SMOTEENN combined sampler and this makes use of SMOTE for oversampling, and the edited nearest neighbors rule in order to do an undersampling.

For the final task in the exercise, you needed to recall how we can compute the correlations between the various columns in our dataset and then visualize them using Pandas, as well as Seaborn. In order to view the correlations between every pair of columns in a Pandas data frame, Pandas very conveniently provides us with a way to generate a correlation matrix. Specifically, we can call the data frames corr method and this will generate a matrix which gives all the correlation values.

However, when there are multiple columns in the dataset, sifting through the matrix in order to get the correlation values can be rather painstaking. Which is why it is often convenient to visualize the correlations using a heatmap. This is something which is provided by Seaborn, where we can call the Seaborn library's heatmap method. And we can pass to it as argument, the correlation metrics which we generated using Pandas.

[Video description begins] The command displays: seaborn. heatmap ( ) [Video description ends]

Course File-based Resources
•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets

•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets

•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets

•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets

•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets

•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets

•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets

•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets

•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets

•	Data Scientist 20: Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML - Assets
© 2023 Skillsoft Ireland Limited - All rights reserved.