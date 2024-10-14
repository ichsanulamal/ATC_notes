## 1. Machine Learning Anomaly Detection Techniques

### 1. Supervised Anomaly Detection

#### Concept
- **Definition:** This approach uses labeled training datasets, where both normal and anomalous instances are identified.
- **Data Requirements:** The training dataset must contain examples of both normal and anomalous data across different scenarios and devices.

#### Process
1. **Data Preparation:** Combine datasets that represent various anomaly scenarios.
2. **Modeling:** 
   - Split the dataset into training and testing subsets for cross-validation.
   - Identify and label the training data for normal and anomalous instances.
3. **Cross-Validation:** 
   - Validate new datasets against the modeled training dataset to identify anomalies.

#### Advantages
- Availability of labeled data aids in accurate anomaly detection.

#### Challenges
1. **Imbalance in Data:** Anomalous instances are often fewer than normal instances, leading to potential misinterpretations.
2. **Labeling Difficulty:** Accurately labeling anomalies can be challenging due to their rarity.

#### Example
- **Architecture Overview:** 
   - Start with a complex raw dataset.
   - Separate it into training and test datasets through cross-validation.
   - Calculate the Class Outlier Score (COS) and run a distance-based classifier.
   - Adjust parameters using grid search to improve performance.

### 2. Unsupervised Anomaly Detection

#### Concept
- **Definition:** This approach does not require labeled training data, allowing for broader application.
- **Data Requirements:** The dataset combines different anomaly scenarios without pre-labeled classes.

#### Process
1. **Data Preparation:** Combine datasets representing different anomalies.
2. **Modeling:** 
   - Use the entire dataset to identify patterns without labels.
3. **Normal Behavior Clustering:** 
   - Initialize parameters based on clustering techniques.
   - Identify and separate normal from abnormal data.

#### Example
- **Normal Behavior Model:** 
   - Use unlabeled archived data to build a normal behavior model.
   - Apply unsupervised classification techniques to detect and remove anomalies from real-time data.

## 2. Comparing Anomaly Detection Algorithms

### Anomaly Detection Algorithms Comparison

| **Algorithm**         | **Pros**                                                      | **Cons**                                                        |
|-----------------------|--------------------------------------------------------------|-----------------------------------------------------------------|
| **K-Nearest Neighbor (KNN)** | - Easy to understand and implement<br>- Works well with non-standard data types | - Requires large storage<br>- Sensitive to similarity functions<br>- Computationally expensive<br>- Lacks a principled method for choosing K |
| **Neural Networks**   | - Handles complex tasks that linear algorithms can’t<br>- Can generate various combinations for predictions<br>- Parallel execution allows for resilience to failures | - Requires intensive training<br>- High processing time<br>- Complex architecture |
| **Local Outlier Factor** | - Effective for detecting local anomalies<br>- No need for interconnectivity between distributed elements | - Relies on direct neighborhoods<br>- Poor performance with global anomalies<br>- Not suitable for distributed computing |
| **K-Means**           | - Simple to implement<br>- Uses well-defined centroid identification | - Assumes equal observations in clusters<br>- Requires numerical data only<br>- Sensitive to initial cluster choices |
| **Support Vector Machine (SVM)** | - Finds the best separation hyperplane<br>- Effective with multi-dimensional data | - Requires both positive and negative examples<br>- High memory consumption<br>- Numerical stability issues depend on kernel choice |
| **OLINDDA**           | - Works well with continuous and categorical data<br>- Single pass of the dataset required | - Struggles with purely continuous data<br>- Complex to implement<br>- Sensitive to chosen number of clusters |
| **Hoeffding Tree**    | - Requires less memory<br>- Efficient memory utilization with statistical sampling | - Needs positive and negative labels<br>- Limited to top two attributes<br>- Can be slow to execute with complex structures |

## 3. Online Anomaly Detection Components

### Properties of Online Anomaly Detection
1. **Continuous Learning:** 
   - Systems learn continuously without storing previous data points.
   - Utilizes information from prior detections for current requirements.

2. **Automation:** 
   - Operates automatically without manual parameter adjustments.

3. **Adaptability:** 
   - Can adapt to dynamic environments and changing data statistics.

---

### Essential Components of Online Anomaly Detection Systems

1. **Input Data:**
   - Consists of data points or instances necessary for detecting anomalies.

2. **Input Dataset Identification:**
   - Requires identifiers for datasets to facilitate easy recognition.

3. **Dependencies Between Data Points:**
   - Understanding relationships among data points is crucial.

4. **Anomaly Detection Mechanism:**
   - A robust mechanism is needed to quickly identify and present anomalies.

---

### Detailed Components

#### 1. Input for Anomaly Detector
- Defined using a variable \( X \) representing various data points.
- Can be expressed using linear algebra (e.g., \( X_{n,d} \) as a matrix of data).

#### 2. Input Dataset Identification Techniques
- **Univariate Analysis:** 
  - Analyzes one variable at a time, identifying missing values and outliers.
  - Applies central tendency and spread measures for continuous variables; frequency tables for categorical variables.
  
- **Multivariate Analysis:** 
  - Examines relationships among multiple variables using correlation and covariance.

#### 3. Dependencies Between Data Points
- **Types of Dependencies:**
  - **Sequences:** Maintained through data pipelines for analytical applications.
  - **Spatial Data:** Geospatial data helps extract information about physical locations.
  - **Graphs:** Used to represent non-linear data through nodes and edges.
  - **Spatial-Temporal Data:** Reflects both spatial and temporal qualities, requiring appropriate management techniques.

---

### Output of Anomaly Detection
- Different algorithms can be used to classify the outcomes of anomaly detection, including:

1. **Scoring Anomaly Detector:**
   - Represents anomalies based on scoring functions derived from nearest neighbor graphs.

2. **Labeling Anomaly Detector:**
   - Utilizes provided labels to evaluate anomaly quality, typically using supervised algorithms.

### Summary
This structured overview of online anomaly detection systems emphasizes the continuous learning, automation, and adaptability of such systems, along with the essential components needed for effective anomaly detection.

## 4. Online Anomaly Detection Approaches

### Approaches to Detecting Anomalies

#### 1. Real-Time Anomaly Detection
- **Concept Drift:** 
  - Refers to changes in data that affect the relationship between input and output variables.
  
- **Detection Process:**
  1. **Data Ingestion:** Ingest data from various sources.
  2. **Anomaly Detection:** Use an anomaly detector to identify potential anomalies.
  3. **Concept Drift Detection:** Implement a concept drift detector to confirm if a drift has occurred.
  4. **Relearning:** If concept drift is detected, discard outdated models and relearn the anomaly detector using updated data points.

---

#### 2. Anomaly Detection in Time Series
- **Definition:** 
  - Time series analysis incorporates the temporal aspect of data, helping to identify trends and anomalies over time.

- **Detection Process:**
  1. **Identify Sequences:** Analyze the input dataset as a sequence over time.
  2. **Labeling and Variation Tracking:** 
     - Label data points and track their variations to depict normal data trends.
  3. **Detection Formula:** Apply appropriate detection formulas to identify anomalies based on unexpected changes, such as sudden growth in metrics.

---

#### 3. Anomaly Detection with Windowing
- **Windowing Concept:**
  - Windowing involves segmenting the data into smaller, manageable windows for analysis.

- **Detection Process:**
  1. **Data Generation:** Generate input data of various types using a data generator.
  2. **Pass to Anomaly Detection Window:** Input data is sent to an anomaly detection window that contains essential components:
     - **Estimators:** Used to evaluate normal behavior within the data.
     - **Deviation Detectors:** Identify deviations from expected patterns.
  3. **Learning Approaches:** 
     - Use both supervised and unsupervised learning techniques within the windowing framework.
  4. **Alarm Mechanism:** 
     - Once deviations are detected, alarms can be triggered to notify relevant stakeholders for action.

## 5. Anomaly Detection Use Cases

### Real-World Use Cases of Anomaly Detection

#### 1. Anomaly Detection in Process Modeling
- **Purpose:** Prevent fraud and security breaches by ensuring process model integrity.
  
- **Steps:**
  1. **Data Source Identification:** Identify the original source of data for the process model.
  2. **Data Acquisition:** Acquire the relevant data from the identified source.
  3. **Data Filtering:**
     - Apply filters based on the criteria defined in the process model.
     - Scope the data between original and filtered datasets.
  4. **Data Splitting:**
     - Use a data splitter to categorize data into "normal" and "anomalous."
     - Store the selected data in a storage facility for further analysis.
  5. **Process Discovery Algorithms:** 
     - Apply algorithms to the filtered data to enhance process execution and maintain data logs with appropriate labels for each process stage.

---

#### 2. Anomaly Detection in Network Function Virtualization (NFV)
- **System Architecture:**
  - Involves various participants, including physical resources, hypervisors, virtual resources, and virtual network functions (VNFs).
  
- **Steps:**
  1. **Data Generation:** All resources generate monitoring data.
  2. **Self-Stabilization Pipeline:** 
     - Implement a pipeline for data analysis and monitoring.
     - Execute the pipeline with stabilizing actions to format and analyze the acquired data.
  3. **Outcome Generation:**
     - Generate catalogs for recovery actions and fault scenarios, providing a complete system architecture overview.
  4. **Anomaly Management:**
     - Use the pipeline to detect, correct, and classify anomalies for effective fault management and recovery planning.

---

#### 3. Anomaly Detection in Healthcare
- **System Architecture:**
  - Focuses on collecting and analyzing medical data over time.

- **Steps:**
  1. **Data Collection:** Collect patient medical data at specific time intervals.
  2. **Sensor Value Prediction:** Predict the sensor value for the given time interval.
  3. **Accuracy Calculation:**
     - Apply an error calculation algorithm to assess sensor accuracy.
     - Compare the recorded error against a defined threshold:
       - If greater than the threshold, assign to **Assign 1** (indicating a potential issue).
       - If less, assign to **Assign 0** (indicating normal operation).
  4. **Majority Observation Calculation:** 
     - After processing multiple observations, calculate the majority outcome.
     - If the majority is **1**, generate an alarm for a medical situation.
     - If the majority is **0**, classify it as a sensor anomaly (false alarm).
  5. **Database Update:** Update the database with the outcomes for future reference.