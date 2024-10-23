# Handling Anomalies

### Sources of Data Anomalies

In the video, data anomalies are defined as observations that deviate from the expected behavior or norms in a dataset. These can also be referred to as "outliers" or "exceptions." Several key sources of data anomalies include:

1. **Bad Data**: This refers to erroneous, misleading, or improperly formatted data that can corrupt analysis.
2. **Missing Values**: When data is incomplete or contains gaps, it may negatively impact the accuracy of outcomes.
3. **Calculation and Manipulation Errors**: Mistakes made during data calculations or transformations can create anomalies.
4. **Irrelevant Data**: Data that lacks relevance to the specific business scenario or domain can lead to false insights.

### Data Verification vs. Data Validation

While both data verification and validation aim to ensure data quality, they differ in focus and methodology.

1. **Data Verification**:
   - **Purpose**: Ensures that the data entered into a system matches the intended input.
   - **Process**: Verification involves checking that no mistakes are made during data entry, regardless of whether it's done manually or by machines.
   - **Example**: Double data entry, where a user inputs the data twice to confirm accuracy.

2. **Data Validation**:
   - **Purpose**: Ensures that the entered or processed data meets the accuracy requirements of the system.
   - **Process**: Validation focuses on confirming that the data conforms to predefined standards or rules (e.g., data formats, value ranges).
   - **Example**: Range checks, where the system checks if the data falls within a valid range of values.

### Key Differences Between Verification and Validation:
- **Verification**: Focuses on preventing errors during data entry.
- **Validation**: Focuses on ensuring the data already entered is accurate and meets required standards.

By addressing both verification and validation, organizations can detect and minimize data anomalies, leading to more accurate analysis and decision-making.

---

### Approaches to Decomposition and Forecasting

Decomposition is a widely-used method in forecasting, as it simplifies complex data patterns by breaking down the data into its constituent components. This approach allows for a more accurate forecast by addressing each of these components individually. Decomposition separates time series data into several key components: **trend**, **seasonality**, **cycle**, **randomness**, and **mean**. Once the data is decomposed, forecasting can be done by analyzing and projecting these components forward.

### Steps in Decomposition-Based Forecasting

The process of decomposition-based forecasting follows several key steps:

1. **Load the Data**: Begin by loading the dataset to be forecasted.
2. **Select the Appropriate Method**: Choose a methodology such as LOESS (Locally Estimated Scatterplot Smoothing), Bayesian Structural Time Series (BSTS), or Generalized Additive Models (GAM) to fit the data.
3. **Identify Data Points**: Use these data points to help identify patterns and compute forecasting outcomes.
4. **Decompose the Time Series**: Break down the data into its components: mean, trend, seasonality, cycle, and randomness.
5. **Forecast**: Once the components are isolated, a forecast can be generated by analyzing and projecting each component.

### Decomposition Formula

The decomposition method utilizes the following formula to represent the data:

\[
X_t = U \cdot T_t \cdot C_t \cdot S_t \cdot R_t
\]

Where:
- \( X_t \) = Observed series value at time \( t \)
- \( U \) = Mean of the series
- \( T_t \) = Trend component at time \( t \)
- \( C_t \) = Cycle component
- \( S_t \) = Seasonality component
- \( R_t \) = Random error component
- \( t \) = Time period

Each of these components is multiplied together to calculate the observed value at each time period. The formula can also be applied to the log of the series, depending on the specific data.

### Steps to Implement Decomposition

1. **Remove the Mean**: Divide each value in the series by the overall mean to normalize the data, resulting in values near 1.
2. **Calculate the Moving Average**: This step smooths out the data by computing the mean over a fixed window, typically a year, to highlight the trend.
3. **Calculate the Trend**: Remove the trend component by analyzing moving averages and calculating deviations from the long-term trend.
4. **Calculate the Cycle**: Divide the moving average by the computed trend to isolate the cyclical component.
5. **Calculate the Seasonality**: Divide the original series by the moving average to reveal seasonal fluctuations.
6. **Calculate the Randomness**: Identify the random error by dividing the series values by the seasonality component. This residual noise represents randomness in the data.

### Forecasting with Decomposition

Once the decomposition process is complete and each component has been isolated, forecasters can project the components forward based on past behavior, resulting in an accurate forecast. By addressing trend, cycle, seasonality, and randomness individually, decomposition-based forecasting ensures that each factor is properly accounted for, making the forecast more reliable. 

### Summary of Formulas and Steps

- **Formula**: \( X_t = U \cdot T_t \cdot C_t \cdot S_t \cdot R_t \)
- **Steps**:
   1. Remove mean
   2. Calculate moving average
   3. Calculate trend
   4. Calculate cycle
   5. Calculate seasonality
   6. Calculate randomness

These steps and formulas, when followed, enable decomposition-based forecasting to yield accurate and understandable predictions.

---

### Data Examination Approaches

In this video, the approaches for examining data focus on using randomization tests, the null hypothesis, and the Monte Carlo method. These methods are non-parametric and computational techniques that help explore patterns in data without relying on traditional parametric assumptions like normal distributions or population parameters.

### Randomization Test

A **randomization test** is a statistical method used to examine data without requiring random samples from a population. It compares results across different groups to test the null hypothesis and doesn't involve estimating population parameters. 

#### Steps in a Randomization Test:
1. **Define a Metric**: Choose a metric to measure the effect, such as the T-statistic or the difference between group means.
2. **Calculate Test Statistic**: Calculate the initial test statistic (e.g., T-statistic) for the actual data.
3. **Randomize Data**: Shuffle the data across groups and recalculate the test statistic for this randomized data.
4. **Repeat N Times**: Repeat the randomization process at least 1000 times to build a distribution of test statistics from reshuffled data.
5. **Count Occurrences**: Count how often the test statistic from the randomized data exceeds the original test statistic.
6. **Calculate Probability**: Divide the count by N (the total number of repetitions) to obtain the probability of getting a higher statistic under the null hypothesis.
7. **Decision**: Based on this probability, decide whether to reject or retain the null hypothesis.

### Null Hypothesis

The **null hypothesis** is a fundamental concept in hypothesis testing. It assumes that there is no significant difference or effect between groups, and any observed differences are due to chance.

#### Key Points in Null Hypothesis Testing:
- It is tested in randomization tests by comparing test statistics from original and reshuffled data.
- The decision to reject or retain the null hypothesis is based on the probability that the observed test statistic could occur by chance.

### Monte Carlo Method

The **Monte Carlo method** is a computational technique that uses random sampling to estimate numerical results. Rather than computing every possible combination of data (which may be infeasible), the Monte Carlo method generates random samples and evaluates the outcomes.

#### Steps in the Monte Carlo Method:
1. **Generate Random Data**: Start by generating random input data or variables.
2. **Run Deterministic Model**: Apply a deterministic model (like harmonic load-flow) to the random data.
3. **Store Outputs**: Record the output variables generated by the model.
4. **Compare with Predetermined Variables**: Compare the output with known or predetermined variable samples.
5. **Evaluate Statistics**: If the output and sample variables are comparable, evaluate the statistical properties of the output.
6. **Repeat if Necessary**: If not, repeat the process until a valid comparison is achieved.

### Summary of Key Concepts

- **Randomization Test**: A non-parametric test used to compare groups by reshuffling data and testing the null hypothesis.
  - No need for population parameters.
  - Repeated shuffling creates a distribution of test statistics to compare with the original data.

- **Null Hypothesis**: Assumes no effect or difference exists between groups. If the probability of observing the test statistic by chance is low, the null hypothesis is rejected.

- **Monte Carlo Method**: Relies on repeated random sampling to estimate outcomes in complex systems.
  - Instead of calculating all possible combinations, the method uses randomness to approximate results.

By applying these techniques, data can be examined in more flexible and computationally efficient ways, especially when traditional parametric methods aren't appropriate or feasible.

---

### Anomaly Detection Scenarios

Anomaly detection involves identifying unusual patterns or behaviors in data that differ significantly from the norm. These anomalies can indicate issues such as fraud, equipment malfunctions, or other unexpected events. There are three main scenarios or types of anomalies:

1. **Point Anomalies**: These occur when a single data point stands out as an anomaly compared to the rest of the data. It is the most common type of anomaly.  
   - **Example**: Detecting credit card fraud based on an unusually high transaction amount compared to typical spending patterns.

2. **Contextual Anomalies**: These are anomalies that occur in a specific context. The data might be normal in one context but anomalous in another.
   - **Example**: A sudden spike in electricity usage during the middle of the night, which is unusual for that specific time period.

3. **Collective Anomalies**: These occur when a group or collection of related data points is anomalous, even though individual data points in the group may not be unusual on their own.
   - **Example**: Detecting a series of connected cyber-attacks that, together, indicate an anomaly, while each individual attack may seem normal on its own.

### Categories of Anomaly Detection Techniques

Different techniques are used to detect anomalies depending on the type of data and the domain. These techniques can be grouped into the following categories:

1. **Static Rule-Based Approach**:
   - Involves setting predefined rules to detect known anomalies. 
   - **Pros**: Simple and straightforward.
   - **Cons**: Can be brittle and complex over time; lacks flexibility to handle new anomalies.
   - **Example**: A rule-based system that flags transactions above a certain threshold as fraudulent.

2. **Information Theory Approach**:
   - Based on the concept that anomalies tend to contain more information due to irregularities. The goal is to find data points with the highest irregularities.
   - **Example**: Detecting anomalies by identifying patterns in data with unexpectedly high entropy.

3. **Dimensionality Reduction**:
   - Reduces the number of variables in data while preserving as much variance as possible, which helps identify complex anomaly patterns.
   - Common techniques include **Principal Component Analysis (PCA)** and **Autoencoders**.
   - **Example**: Detecting network anomalies by reducing traffic flow data to key variables and identifying irregular patterns.

4. **Graph-Based Analysis**:
   - Useful for systems with interacting participants, forming graphs of dependencies. Anomalies can be detected by analyzing changes in these interaction patterns.
   - **Example**: Detecting fraudulent social network activity by analyzing the structure of user interactions.

### Anomaly Detection with Machine Learning

Anomaly detection can also be categorized based on machine learning techniques, which are typically divided into **supervised** and **unsupervised** methods:

1. **Supervised Learning for Anomaly Detection**:
   - Requires labeled datasets where normal and anomalous data points are clearly identified. The model learns from the labeled data to detect anomalies in new data.
   - **Techniques**: Support Vector Machines (SVM), Artificial Neural Networks (ANNs), Decision Trees, and Statistical Models.
   - **Example**: Using supervised learning to classify transactions as fraudulent or legitimate based on historical data with known outcomes.

2. **Unsupervised Learning for Anomaly Detection**:
   - No labeled data is required. The algorithm identifies hidden patterns or deviations in the data, detecting anomalies by analyzing features like distance and density.
   - **Techniques**: Clustering (e.g., k-means), Nearest Neighbor, and Statistical Methods.
   - **Example**: Detecting server malfunctions by analyzing data clusters of normal server activity and flagging outliers.

### Summary of Key Concepts

- **Anomaly Types**: Point anomalies (single outliers), contextual anomalies (outliers in certain contexts), and collective anomalies (anomalies in groups of data).
- **Detection Techniques**: Static rules, information theory, dimensionality reduction, and graph-based analysis.
- **Machine Learning Approaches**:
  - **Supervised**: Requires labeled data and uses methods like SVM or ANNs.
  - **Unsupervised**: Detects anomalies in unlabeled data based on patterns, often using clustering and nearest-neighbor techniques.

These techniques and scenarios provide a structured way to identify and handle anomalies in diverse datasets.

---

### Prominent Anomaly Detection Techniques

This video focuses on three key unsupervised anomaly detection techniques used to identify unusual data patterns. These techniques—clustering, k-nearest neighbor (KNN), and statistical outlier detection—are widely used for detecting anomalies in unlabeled datasets.

### 1. **Clustering-Based Anomaly Detection**

Clustering is an unsupervised technique that groups data points with similar features into clusters. It works well for finding patterns in multidimensional data and can be applied in two forms: unsupervised clustering (working entirely with unlabeled data) and semi-supervised clustering (which combines labeled and unlabeled data). The core concept involves analyzing the behavior of data points in relation to clusters.

#### Key Assumptions:
- **New Data Outside Clusters**: Data points that do not fit into existing clusters are considered anomalies.
- **Cluster Distance**: Normal data points lie closer to the cluster centroid, while anomalous points are further away, allowing distance scores to be used for anomaly detection.
- **Cluster Size**: The majority of data points form larger, denser clusters, while anomalies are often found in smaller, sparser clusters.

#### Example:
- In cybersecurity, clustering can help detect unusual network behavior by grouping normal activities and flagging outliers (such as unauthorized access attempts).

---

### 2. **K-Nearest Neighbor (KNN) for Anomaly Detection**

KNN is a simple and intuitive machine learning algorithm used for classifying data based on the proximity of data points to their nearest neighbors. It assumes that normal data points exist in dense areas, while anomalies are isolated, far from these dense clusters.

#### Key Concept:
- **Distance Metrics**: KNN relies on calculating the distance or similarity between data points. If a point is far from its nearest neighbors, it is considered an anomaly.
- **K-Nearest Neighbor Outlier Score**: Anomalies are detected using two key calculations—distance to the nearest neighbors and the relative density of the data points.

#### Example:
- In fraud detection, KNN can identify fraudulent transactions by analyzing whether the behavior (e.g., spending patterns) of a customer is significantly different from their previous transactions.

---

### 3. **Statistical Outlier Detection**

Statistical methods rely on building probabilistic models based on the data's distribution. Anomalies are detected by assessing how well data points fit into these models. This technique is classified into two approaches:

- **Parametric Approach**: Assumes the data follows a known probability distribution.
- **Non-Parametric Approach**: Does not assume a specific probability distribution.

#### Model Types:
Depending on the combination of error types, trend, and seasonality, different models can be used for detecting anomalies:
- **ANA (Additive error, Additive seasonality, No trend)**.
- **AAA (Additive error, Additive trend, Additive seasonality)**.
- **MNM (Multiplicative error, Multiplicative seasonality, No trend)**.
- **MNA (Multiplicative error, Additive seasonality, No trend)**.
- **AAN (Additive error, Additive trend, No seasonality)**.

#### Example:
- In stock market analysis, statistical models can identify unusual price movements by assessing whether a particular trend fits the expected behavior based on historical data.

---

### Summary of Techniques

- **Clustering**: Groups similar data points and uses cluster size and distance from centroids to detect anomalies.
- **K-Nearest Neighbor (KNN)**: Uses the proximity of data points to their neighbors for classification, flagging isolated points as anomalies.
- **Statistical Outlier Detection**: Utilizes probability models to detect data points that deviate significantly from the expected distribution.

By applying these techniques, organizations can effectively detect anomalies in diverse datasets across industries like finance, cybersecurity, and healthcare.

---

### Prominent Anomaly Detection Tools and Their Key Components

In this video, we explore several popular anomaly detection tools and their core components. These tools help identify anomalies in various types of data, such as time series or multivariate datasets. Here are the key tools and the essential programming environments used in anomaly detection.

---

### 1. **Twitter’s AnomalyDetection**
- **Type**: Open-source R package.
- **Key Components**:
  - **Seasonality and Trend Detection**: Detects both global and local anomalies by analyzing seasonality and trends.
  - **Use Cases**: Can be applied to system metrics, customer engagement, financial engineering, and more.
  - **Installation**: Requires installation of the R package.
  
---

### 2. **Netflix’s Surus**
- **Type**: Open-source OSS project using Pig and Hive.
- **Key Components**:
  - **User-Defined Functions**:
    - **Score PMML**: A tool for scoring predictive models.
    - **RAD**: Robust implementation of PCA (Principal Component Analysis) for outlier detection.
  - **Use Cases**: Surus is used for model scoring and outlier detection in large-scale data environments.

---

### 3. **NASA’s Telemanom**
- **Type**: Framework for detecting anomalies in multivariate time series data.
- **Key Components**:
  - **LSTMs (Long Short-Term Memory)**: Uses Keras and TensorFlow to train models and identify anomalies based on sensor data.
  - **Thresholding**: Anomalous sequences are identified based on deviations from expected behavior.
  - **Use Cases**: Originally developed for detecting anomalies in spacecraft sensor data.

---

### 4. **LinkedIn’s Luminol**
- **Type**: Lightweight Python library for time series analysis.
- **Key Components**:
  - **Time Series Anomaly Detection**: Detects anomalies within time windows and assigns severity scores.
  - **Correlation Support**: Can analyze correlations in data.
  - **Flexibility**: Can work with any custom algorithm to detect anomalies.
  - **Use Cases**: Commonly used for time-stamped data to track anomalies over time.

---

### Programming Languages and IDEs for Anomaly Detection

1. **Python**:
   - **Type**: General-purpose programming language.
   - **Key Features**: Supports multiple paradigms (object-oriented, functional, etc.) and has an extensive standard library for building large-scale applications.
   - **Use Case**: Widely used for developing anomaly detection logic due to its flexibility and large community support.

2. **R**:
   - **Type**: Programming language and environment.
   - **Key Features**: Designed for statistical computing, commonly used by statisticians for data analysis and anomaly detection.
   - **Use Case**: Essential for developing statistical models for detecting anomalies.

3. **Azure Machine Learning Studio (ML Studio)**:
   - **Type**: Cloud-based tool by Microsoft.
   - **Key Features**: A collaborative, drag-and-drop environment for building, testing, and deploying machine learning models.
   - **Use Case**: Simplifies the development and deployment of anomaly detection models with a cloud-managed service.

---

### Steps for Detecting Anomalies Using Tools
1. **Problem Identification**: Define the anomaly detection problem based on the data context.
2. **Define Data Schema**: Outline the source and schema of the data.
3. **Parse and Pre-process Data**: Prepare the data for analysis by cleaning and transforming it.
4. **Design the Model**: Develop the anomaly detection model tailored to the data.
5. **Execute the Model**: Run the model to detect anomalies, analyze the outcomes.
6. **Investigate the Results**: Examine anomalies detected, or lack thereof, to evaluate model performance.
7. **Update the Model**: Based on the outcome, refine and improve the model to increase its detection accuracy.

This process involves multiple iterations to improve the model until it performs optimally in detecting anomalies.

---

### Essential Rules for Anomaly Detection

In this video, we discuss the fundamental rules used for anomaly detection. These rules help streamline the detection of abnormal patterns in data and are crucial for building effective anomaly detection models.

---

### Key Anomaly Detection Rules

1. **Threshold Rules**
   - **Definition**: These rules detect anomalies when data events or flows exceed or fall below a specified range.
   - **Use Cases**:
     - Monitoring application bandwidth changes.
     - Detecting failed services.
     - Identifying the number of users connected to a VPN.
     - Detecting large outbound data transfers by comparing against predefined thresholds.
   - **How It Works**: Events or activities outside the defined thresholds are flagged as anomalies. This method is simple yet effective for scenarios with clearly defined upper or lower limits.

---

2. **Behavioral Rules**
   - **Definition**: Behavioral rules identify anomalies by examining volume changes in regular data patterns over time.
   - **Key Concepts**:
     - **Seasonality**: Establishes baseline behavior over predefined seasons.
     - **Current Traffic Level**: Compares the present data to the baseline, indicating whether it remains unchanged.
     - **Current Traffic Trend**: Calculates changes in data over specified intervals, revealing trends or deviations.
     - **Predicted Value**: Helps scale baselines and adjust the sensitivity of alert systems.
   - **Use Cases**:
     - Detecting outliers in regularly recurring data patterns.
     - Tuning behavioral rules for better accuracy by observing long-term data trends.
   - **How It Works**: By running these rules for longer periods, they become more accurate in identifying deviations from the norm, especially for volume-based anomalies.

### How Anomaly Detection Rules Work
- **Event Testing**: Anomaly rules test data events or flow traffic over short time periods, comparing them to longer time frames to detect unusual behavior.
- **Saved Searches**: Grouping searches around common parameters, based on domain and context, helps focus on relevant anomalies.
- **Time Series Graphs**: Visualizing data over time can highlight anomalies related to availability, trends, and behavioral shifts.