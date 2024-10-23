# Final Exam Data Scientist

Examine the Python code.


1.import numpy as np
2.import matplotlib.pyplot as plot
3.nations = ['China', 'USA', 'India', 'japan', 'England']
4.product1 = np.array([38, 17, 26, 19, 15])
5.product2 = np.array([37, 23, 18, 18, 10])
6.product3 = np.array([46, 27, 26, 19, 17])
7.ind = [x for x, _ in enumerate(nations)]
8.plot.bar(ind, product1, width=0.8, label='product1', color='blue', 9.bottom=product2+product3)
10.plot.bar(ind, product2, width=0.8, label='product2', color='green', bottom=product3)
11.plot.bar(ind, product3, width=0.8, label='product3', color='red' )
12.plot.xticks(ind,nations]
13 //insert code segment here
14 plot.show()

You want to label the stacked bar chart where the x-axis is titled as nations, y-axis as products sold and the stacked bar chart as nationwise product sales statistics. Which code segment would you use in line 13?


Option 1

plot.ylabel("products sold")
plot.xlabel("nations")
plot.text()
plot.title("nationwise product sales statistics")

T Option 2

plot.ylabel("products sold")
plot.xlabel("nations")
plot.legend()
plot.title("nationwise product sales statistics")

Option 3

plot.label("products Sold")
plot.label("nations")
plot.legend("upper left")
plot.heading("nationwise product sales statistics")

Option 4

plot.ydata("products sold")
plot.xdata("nations")
plot.legend("lower left")
plot.title("nationwise product sales statistics")

---

Examine the code written in Node.js.


01. var express = require("express");
02. var bodyParser = require("body-parser");
03. var routes = require("./routes/routes.js");
04. var app = express();
05. app.use(bodyParser.json());
06. app.use(bodyParser.urlencoded({ extended: true }));
07. routes(app);
08. //insert code here

Which code segment would you insert in line 8 to define the port of the server?


Option 1

app.listen(‘port’:3000)

T Option 2

var server = app.listen(3000, function () {
}
);

Option 3

app.listen(3000,”hello server);

Option 4

app.listen(3000);

---

Examine the R code. The assumed standard deviation is 7.


01. scores <- c(84, 93, 101, 86, 82, 86, 88, 94, 89, 94, 93, 83, 95, 86, 94, 87,
02. 91, 96, 89, 79, 99, 98, 81, 80, 88, 100, 90, 100, 81, 98, 87, 95, 94)
03. library(BSDA)
04. //insert code segment here

Which code segment would you use in line 4 to determine and interpret the 99% confidence interval of the population mean?

Instruction: Choose the option that best answers the question. 

z.test(scores, conf.level = 0.99)

z.test(conf.level = 0.99)

z.test(scores, sigma.x = 0.99)

T z.test(scores, sigma.x = 7, conf.level = 0.99)

---

Examine the R code.

01. library("recommenderlab")
02. affinity.data<-read.csv("data.csv")
03. affinity.matrix<- as(affinity.data,"RatingMatrix")
04. //insert code segment here

You want to create a user-based Collaborative filtering model which is trained with 10,000 users. Which code segment would you insert in line 4?

Instruction: Choose the option that best answers the question. 

Rec.model<-Recommender(affinity.matrix[1:100000], method = "IBCF")

Rec.model<-Recommender(affinity.data[1:10000)

Rec.model<-Recommender(affinity.data[1:10000], method = "UBCF")

T Rec.model<-Recommender(affinity.matrix[1:10000], method = "UBCF")

---

You have implemented a Tableau workbook containing certain dashboards and it is made accessible publicly. As a part of a new requirement you want to restrict the dashboard and visualizations in the workbook to be shared internally within the team. Which Tableau implementation would you adopt to restrict the dashboard access?

Instruction: Choose the option that best answers the question. 

T Publish workbook to Tableau server

Use Ldap

Restrict access using tokens

Send a url to team by publishing it to tableau public

---

You have to select an appropriate type of chart that you can use to represent the number of unique visitors visiting a landing page based on country and the products that are popular among the existing customers. 
Which chart type would you select?

Line chart

T Bar chart

Area chart

Column chart

---

Examine the Python code and refer to the exhibit.


01. import numpy as np
02. import matplotlib.pyplot as plt
03. team1_means, team1_std = (19, 33, 27,33, 25), (1, 2, 3, 1, 2)
04. team2_means, team2_std = (24, 31, 33, 19, 24), (2, 4, 1, 2, 2)
05. ind = np.arange(len(team1_means))
06. width = 0.33
07. fig, ax = plt.subplots()
08. rects1 = ax.bar(ind - width/2, team1_means, width, yerr=team1_std,
09. color='Red', label='team1')
10. rects2 = ax.bar(ind + width/2, team2_means, width, yerr=team2_std,
11. color='Blue', label='team2')
12. //insert code segment here


Which code segment would you use in line 10 to label the graph as indicated in the exhibit?


T Option 1

ax.set_ylabel('Scores')
ax.set_title('Scores by team1 and team2')
ax.set_xticks(ind)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()
plt.show()

Option 2

ax.set_xticks(ind)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()
plt.show()

Option 3

ax.set_ylabel('Scores')
ax.set_title('Scores by team1 and team2',G1,G2,G3,G4,G5)
plt.show()

Option 4

ax.set_title('Scores by team1 and team2',G1,G2,G3,G4,G5)
ax.legend()
plt.show()

Instruction: Choose the option that best answers the question. 

---

You have to create a plot for a given dataset titled patientdata, containing the height and weight of patients visiting a hospital. Which of the following R statement would create a ggplot?


Option 1

ggplot(data = patientdata, mapping = aes(x = height, y = height))

Option 2

ggplot(data = patientdata)

Option 3

ggplot(data = surveyspatientdata, mapping = aes(x = height, y = weight),geom_point())

T Option 4

ggplot(data = patientdata, mapping = aes(x = height, y = weight)) +
geom_point()

---

You want to build a Recommender Engine which is based on analyzing information of users’ preferences and behaviors for your online shopping application in order to predict what they would like to buy next? 
What type of Recommender Engine would work best in this given scenario?

Result: Incorrect. The correct answer is indicated. 

Hybrid recommender Engine
Not selected
Correct answer.

Content based filtering Recommender
Not selected. Not selected is correct.

Collaborative Filtering Recommender
Selected
Incorrect answer.

Sentiment Recommender Engine
Not selected. Not selected is correct.

---

You want to automate and orchestrate the processes and configuration management in Azure. Which Azure framework would you adopt to facilitate the automation?

Result: Incorrect. The correct answer is indicated. 

Chef
Selected
Incorrect answer.

Azure automation
Not selected
Correct answer.

Puppet
Not selected. Not selected is correct.

Service fabric
Not selected. Not selected is correct.

---

Examine a scenario where you have created a dashboard using Tableau and you want to implement the following features:


01. Utilize d3.js to add custom visualization.
02. Filter replacement.


Which Tableau implementation would you use to get the desired features?

Instruction: Choose the option that best answers the question. 

Use d3.js to pull tabeau opensource library

Use tabcmd command

T Use Tableau dashboard extensions

Using javascript library

---

Examine the Python.


01. import pandas as pd
02. import matplotlib.pyplot as plt
03. data = [['E001', 'M', 34, 10000, 'Accounts'],
04. ['E002', 'F', 40, 11000, 'Finance'],
05. ['E003', 'F', 37, 13500, 'Project'],
06. ['E004', 'M', 30, 13900, 'Inventory'],
07. ['E005', 'F', 44, 11700, 'Inventory'],
08. ]
09. //insert code segment here

You want to create a histogram for the numeric data. Which code segment would you use in line 10?


T Option 1

df = pd.DataFrame(data, columns = ['EMPID', 'Gender',
'Age', 'Salary',
'dept'] )
df.hist()

> show plot
plt.show()

Option 2

data.hist()

> show plot
plt.show(data,’EMPID’,’gender’,’AGE’,’Salary’)

Option 3

plt.hist(data,1,4)
.show()

Option 4

plt.hist(df,[:3])
.show()
Instruction: Choose the option that best answers the question. 

---

You have to identify a visualization element for model identification and to check randomness in datasets. Which visualization element would you choose for this scenario?

Result: Incorrect. The correct answer is indicated. 

Histogram
Selected
Incorrect answer.

Boxplot
Not selected. Not selected is correct.

Correlogram
Not selected
Correct answer.

Timeseries
Not selected. Not selected is correct.

---

You have to transfer data from a MySQL table titled employee into HDFS. Your database administrator has provided the following information about the database.


Database: mysql
url: jdbc:mysql://localhost:3306/empdb
username: allen
password: xxxxx

You want to use Sqoop to migrate data from the database to HDFS. Which command would you use?


T Option 1

sqoop import --connect jdbc:mysql://localhost:3306/empdb \
--table EMPLOYEE
\
--username allen \
--password xxxxx

Option 2

sqoop export --connect jdbc:mysql://localhost:3306/empdb \
--table EMPLOYEE \
--username allen \
--password xxxxx

Option 3

sqoop import --connect jdbc:mysql://localhost:3306/empdb \
--table EMPLOYEES \
--username allen \
--password xxxxx

Option 4

sqoop import \
--connect jdbc:mysql://localhost:3306/empdb \
--table EMPLOYEE
Instruction: Choose the option that best answers the question. 

---

You have to select a framework that provides the capability of ingesting, storing, visualizing and creating alerts with metrics data to simplify analytics. 
Which framework would you select for this given scenario?

Result: Correct. Great job! 

NiFi
Not selected. Not selected is correct.

Kafka
Not selected. Not selected is correct.

Sqoop
Not selected. Not selected is correct.

Wavefront
Selected
Correct answer.

---

Examine the R code.


01. w1 <-
02. read.csv(file="w1.dat",sep=",
03. ",head=TRUE)
04. //insert code segment here

The name of one of the columns is col1. You want to plot a histogram and name the chart as distribution. Which code segment would you use in line 4?

Instruction: Choose the option that best answers the question. 

hist(w1$col1)

hist(main=w1$col1)

hist(w1$col1,main=""Distribution "",xlab=""w1"")

hist(w1$col1,breaks=2)

---

You’ve implemented Hadoop to manage the 4 Vs of big data. You want to bring in data warehousing capability to utilize Hadoop data lakes for querying and analysis. Which framework would you choose for this given scenario?

Result: Correct. Great job! 

Use Yarn
Not selected. Not selected is correct.

Use database as extension
Not selected. Not selected is correct.

Use Hive
Selected
Correct answer.

Use Tez
Not selected. Not selected is correct.

---

Examine the R code.


01. library(plotly)
02. m <- matrix(rnorm(8), nrow = 4, ncol = 2)
03. p <- plot_ly(
04. x = c("a", "b", "c"), y = c("d", "e", "f"),
05. z = m, type = "heatmap"
06. )
07. //insert code segment here

You have to create a shareable link for the chart. Which code segment would you use in line 7?


Option 1

chart_link = create(p, filename="heatmap-grey")
chart_link

Option 2

chart_link = link_create(p, filename="heatmap-grey")
chart_link

T Option 3

chart_link = api_create(p, filename="heatmap-sample")
chart_link

Option 4

chart_link
Instruction: Choose the option that best answers the question. 

---

You are using Tableau to build a dashboard, the current layout of the dashboard is horizontal, and you want to adjust the height of the views. Which action would you perform to complete the adjustment?

Result: Incorrect. The correct answer is indicated. 

Format layout container
Not selected. Not selected is correct.

Set item size
Not selected. Not selected is correct.

Add a layout container
Not selected. Not selected is correct.

Change the layout to vertical
Not selected
Correct answer.

---

You have to make architectural changes to the existing architecture due to the following fallacies that you’ve identified in the existing architecture:


01. Not scalable, and to extend scalability you need to add more computing resources which is a costly affair.
02. Infrastructure maintenance impacts application uptime.
03. Infrastructural and environment changes impact the development of application components.
04. Unable to scale up and scale down for concurrent access.


Which architectural changes would you implement to eliminate these problems?

Result: Correct. Great job! 

Containerize applications
Not selected. Not selected is correct.

Deploy applications in Cloud Virtual machines
Not selected. Not selected is correct.

Use VMware virtual machines and port applications to Docker
Not selected. Not selected is correct.

Adopt Serverless architecture
Selected
Correct answer.

---

You have to adopt the right framework to manage the challenges attributed to the 4 Vs of big data. Which of the following open-source frameworks would work best in this given scenario?

Result: Correct. Great job! 

DynamoDB
Not selected. Not selected is correct.

Informatica
Not selected. Not selected is correct.

BigML
Not selected. Not selected is correct.

Hadoop
Selected
Correct answer.

---

Examine a scenario where you’ve been given the task of integrating Wavefront with AWS. You have to setup a read-only-access to the AWS account, for which you’ve attached ReadOnlyAccess on the new role that you created using AWS IAM. What other Wavefront account information would you need to specify to complete the integration?

Instruction: Choose the option that best answers the question. 

Account ID, Internal ID, MFA

"AWS account ID, Internal ID, Role"

T Account ID, External ID, Uncheck Require MFA

Account ID, Internal ID, Uncheck MFA

---

You’ve been tasked to declutter existing visualizations, for which you’re provided with multiple charts containing borders and gridlines. Which of the following tasks would you perform to declutter the provided visualization while ensuring you’re following the Gestalt law?

Result: Incorrect. The correct answer is indicated. 

Remove gridline and retain border
Selected
Incorrect answer.

Retain border and retain gridline
Not selected. Not selected is correct.

Remove gridlines and remove borders
Not selected
Correct answer.

Retain border and remove gridline
Not selected. Not selected is correct.

---

You’ve written a Node.js REST API which handles all the REST calls. Now you want to use a module which provides built-in load balancer and can keep the applications alive forever. Which module would you use?

Instruction: Choose the option that best answers the question. 

Express

Node Schedule

Nodemon

T PM2

---

You’ve been given the responsibility of managing the architecture of enterprise applications to handle big data. As a part of your analysis you found that the system is not robust and searching data can be a time-consuming task, which in turn degrades the user experience as the dashboards and other pages are slow to load. Which of the following attributes contributed to the degrading user experience?

Result: Incorrect. The correct answer is indicated. 

Data transfer
Selected
Incorrect answer.

Network bandwidth
Not selected. Not selected is correct.

Volume
Not selected
Correct answer.

Network failure
Not selected. Not selected is correct.

---

Examine the R code.


01. install.packages("RMySQL")
02. library(RMySQL)
03. testDB =dbConnect(MySQL(),user=allen', password='xxxx',
04. dbname='sales,
05. host='localhost')
06. //insert code segment here

You want to retrieve data from a table titled products and create a dataframe? Which code segment would you insert in line 6?


Option 1

rs=dbSendQuery(testdb,”select * from products”)
df=reteriveAll()

T Option 2

rs=dbSendQuery(testdb,”select * from products”)
df=fetch(rs,n=-1)

Option 3

df=dbSendQuery(testdb,”select * from products”)

Option 4

rs=dbSendQuery(testdb,”select * from products”)
df=getAll(rs,n=-1)

---

In a given scenario the volume of enterprise data is increasing because of data sharing and connected device data availability. You have to provide a solution for connected enterprises to enable data sharing internally within the organization and externally outside the organization. You also need to ensure the adopted solution provides secure online transactions. Which solution would you adopt for this given scenario?

Result: Incorrect. The correct answer is indicated. 

Blockchain
Not selected
Correct answer.

pCloud
Not selected. Not selected is correct.

Encrypted data store
Selected
Incorrect answer.

Datalakes
Not selected. Not selected is correct.

---

Question
 
You have adopted batch pipeline to manage review comments against the feedback of various products. The pipeline has two tasks:


01. Every 12 hours a batch job of Spark runs and takes all the new comments to review and applies a filter to filter fraudulent reviews from legitimate ones.
02. The batch job computes new stats of reviews for the products, where the stats include all time average rating.


You want to convert the batch pipeline implementation to a real-time pipeline where the job runs as soon as new review comments are made. What architectural component would you use?

Instruction: Choose the option that best answers the question. 

T Kafka

Hadoop

Flink

Storm

---

Examine the Python code.


01. import numpy as np
02. np.random.seed(0)
03. from sklearn import dataset
04. from sklearn.naive_bayes import GaussianNB
05. from sklearn.linear_model import LogisticRegression
06. from sklearn.ensemble import RandomForestClassifier
07. from sklearn.svm import LinearSVC
08. X, y
09. =datasets.make_classification(
10. data_samples=5000,
11. Data_features=10,data_informative=2,
12. Data_redundant=2)
13. train_datasamples = 400
14. X_train = X[:train_datasamples]
15. X_test = X[train_datasamples:]
16. y_train = y[:train_datasamples]
17. y_test = y[train_datasamples:]
18. //insert code segment here

From the 400 data samples we’ve generated the train and test datasets and we want to create a linear support vector classification. Which code segment would you insert in line 18?

Instruction: Choose the option that best answers the question. 

T svc = LinearSVC(C=1.0)

lr = LogisticRegression(solver='lbfgs')

gnb = GaussianNB()

rfc = RandomForestClassifier(n_estimators=100)

---

You want to implement a robust practice of storytelling with data to explore the relevance of data for business intelligence. What would be the first step involved in the storytelling process?

Result: Incorrect. The correct answer is indicated. 

Eliminating clutters
Not selected. Not selected is correct.

Data collection
Selected
Incorrect answer.

Selecting visualizations
Not selected. Not selected is correct.

Understanding the scenario context
Not selected
Correct answer.

---

Examine the Python.


01. import numpy as np
02. import dask.array as da
03. array1=np.arrange(10)
04. //insert code segment here

You want to convert the NumPy array to a Dask array to enable parallel computing. Which code segment would you insert in line 4?


Option 1

daskArray=da.from_array(array1)
dataArray.compute(chunks=5)

Option 2

Array1.compute(chunks=5)

T Option 3

daskArray=da.from_array(array1,chunks=5)
dataArray.compute()

Option 4

daskArray=da.from_array(array1,chunks=5)

---

You’ve been tasked to build visualizations using Tableau for a given normalized data that are stored in a database with two tables, a territory table and a sales table. You have to design a Tableau report depicting country wise sales. Which Tableau feature would you use to collate the data and build the report?

Instruction: Choose the option that best answers the question. 

T Join

Union

Intersect

Connect

---

Examine the Python code.


01. import pandas
02. import scipy
03. import numpy
04. from sklearn.preprocessing import
05. MinMaxScaler
06. url = "https://skillsoft/data/Datasets/master/tespatientdata.csv"
07. diseaseTypes = ['type1', 'type2', 'type3', 'type4', 'type5']
08. dataframe = pandas.read_csv(url, names=diseaseTypes)
09. array = dataframe.values
10. X = array[:,0:8]
11. Y = array[:,8]
12. //insert code segment here

You have to rescale the train dataset between 0 and 1. Which code segment would you use in line 12 to rescale the data?


Option 1

scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

Option 2

scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)

Option 3

binarizer = Binarizer(threshold=0.0).fit(X)
binaryX = binarizer.transform(X)

T Option 4

scaler = MinMaxScaler(feature_range=(0, 1))
scaledX = scaler.fit_transform(X)

---

Examine the Python code.


01. import seaborn as sns
02. sns.set()
03. iris = sns.load_dataset("iris")
04. //insert code segment here

You want to explore the correlations between multi-dimensional data by plotting all the pairs of values against each other. Which code block would you use in line 4 to create the pair plots?

Instruction: Choose the option that best answers the question. 

sns.relplot(iris, size=2.5, hue='species')

sns.pairplot(size=2.5, hue=’iris’,iris);

T sns.pairplot(iris, hue='species', size=2.5);

sns.pairplot(hue='species', size=2.5);

---

Examine the Python code.


01. Import luigi
02. class SampleTask(luigi.Task):
03. def output(self):
04. return luigi.LocalTarget('out.txt')
05. //insert code segment here
06. with self.output().open("w") as file:
07. file.write("Hello from luigi task")

While executing the pipeline you’ve discovered that the essential task which executes the business logic is missing. You want to add the missing task with a test message that reads “Hello World”. Which code segment would you insert in line 5?


Option 1

def inpute(self): print("Hello World")

Option 2

def requires(self):

return HelloWorldTask()

Option 3

def output():
return luigi.LocalTarget('out.txt')

T Option 4

def run(self): print("Hello World")

---

Examine the code written in Hapi.js.


01. const Hapi=require('hapi');
02. //insert code segment here
03. server.route({
04. method: 'GET',
05. path:'/apis',
06. handler: (request, h) =>
07. {
08. return 'Basic Get Call!';
09. }
10. });
11. await server.start();
12. console.log('server started and running to receive request’);
13. };
14. init();

In order to test the GET call you have to create a server running on localhost and port 4000. Which code segment would you insert in line 3?


Option 1

Hapi.server({port:4000,host:0.0.0.0});

Option 2

Server({port:4000,host:127.0.0.1});

T Option 3

const init = async () => {

const server = Hapi.server({
port: 4000,
host: 'localhost'
});

Option 4

const server = Hapi.server({
port: 4000,
host: 'localhost'
});
Instruction: Choose the option that best answers the question. 

---

You’ve been given the responsibility of improvising appropriate performance levels in the existing Machine learning model implemented for prediction. Which of the following parameters would you configure to ensure that you get the right performance level?

Result: Correct. Great job! 

Activation function
Not selected. Not selected is correct.

Learning rate
Not selected. Not selected is correct.

Dropouts
Not selected. Not selected is correct.

Hidden units
Selected
Correct answer.