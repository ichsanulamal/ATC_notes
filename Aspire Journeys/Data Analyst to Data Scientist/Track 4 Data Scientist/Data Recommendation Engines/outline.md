### Objectives

1. **Understand Recommendation Engines**
   - Describe what a Recommendation Engine does and its applications.
   - Discuss the types of Recommendation Engines and the reasons for their use.

2. **Comparison of Recommendation Engines**
   - Compare different types of Recommendation Engines.
   - Explore how they can be utilized to address various recommendation problems.

3. **Data Collection and Preparation**
   - Describe the process of collecting data for Recommendation Engines.
   - Explain the importance of data sets for learning, training, and evaluating the engine.

4. **Data Manipulation in R**
   - Use R to import, filter, and transform data into suitable data sets.

5. **Scoring Mechanisms**
   - Describe how Similarity and Neighborhoods can score users and items against another user or new item.
   - Create an R function to score a user against another user for similarity comparison.
   - Develop an R function to score an unseen item for a user based on other users' ratings and similarity scores.
   - Create an R function that identifies similar users and recommends products they liked.

6. **Item Similarity Calculation**
   - Use R to create an Item-to-Item similarity or content score to recommend similar items.

7. **Evaluation of Recommendation Engines**
   - Evaluate a Recommendation Engine using known data and metrics to calculate the accuracy of recommendations.
   - Validate and score a Recommendation System using R and an evaluation data set.

8. **System Building Requirements**
   - Describe the types and interfaces required to build a Recommendation System.

---

To evaluate a recommendation engine, we typically use known data (historical or test set) and specific metrics to calculate how accurately the engine predicts user preferences or interactions. Here's a step-by-step guide, including key metrics and some relevant code to help calculate accuracy:

### Step 1: Problem Setup

- **User-Item Interaction Matrix**: This is a matrix where each row represents a user, each column represents an item, and each cell contains a value (e.g., rating, purchase, click) indicating the interaction between a user and an item.
  
- **Recommendation Engine Output**: The recommendation engine predicts items for each user, which can be either:
  - **Ranking-based**: Producing a ranked list of items for a user.
  - **Rating-based**: Predicting the rating a user would give an item.

### Step 2: Evaluation Metrics
There are several evaluation metrics to assess the accuracy of recommendations:

#### 1. **Precision@K** and **Recall@K**
Precision and recall measure how many of the recommended items are relevant (in the known data).

- **Precision@K**: Measures how many of the top K recommended items are relevant.
  \[
  \text{Precision@K} = \frac{\text{Number of relevant items in top K}}{K}
  \]
  
- **Recall@K**: Measures how many of the relevant items have been recommended out of all relevant items for a user.
  \[
  \text{Recall@K} = \frac{\text{Number of relevant items in top K}}{\text{Total number of relevant items}}
  \]

For example, let's say we know User A interacted with 10 items, and we recommend 5 items for them, out of which 3 are relevant. Here’s how to calculate precision and recall:
  
```python
# Example: Calculate Precision@K and Recall@K

# True relevant items for the user
relevant_items = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# Recommended top-K items
recommended_items = [3, 6, 10, 11, 15]

# Precision@5
precision_at_5 = len(set(recommended_items) & relevant_items) / 5

# Recall@5
recall_at_5 = len(set(recommended_items) & relevant_items) / len(relevant_items)

precision_at_5, recall_at_5
```

#### 2. **Mean Average Precision (MAP)**
MAP evaluates how well-ranked the relevant items are in a ranked list. It computes the average precision across all users, considering multiple positions in the ranked list.

For a user, the precision is recalculated every time a relevant item is found, and the overall score is averaged.

- **Formula**:
  \[
  \text{AP} = \frac{1}{m} \sum_{k=1}^{N} P(k) \times \text{rel}(k)
  \]
  Where:
  - \( P(k) \) is the precision at position \( k \).
  - \( \text{rel}(k) \) is 1 if the item at position \( k \) is relevant, 0 otherwise.
  - \( N \) is the number of recommended items.
  - \( m \) is the total number of relevant items for the user.

#### 3. **Root Mean Squared Error (RMSE)**
For rating-based recommendations, RMSE is commonly used to evaluate how close the predicted ratings are to the actual ratings. Lower RMSE indicates better accuracy.

- **Formula**:
  \[
  \text{RMSE} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (r_i - \hat{r}_i)^2}
  \]
  Where:
  - \( r_i \) is the actual rating.
  - \( \hat{r}_i \) is the predicted rating.
  - \( N \) is the total number of predictions.

Here’s how to calculate RMSE:

```python
import numpy as np

# Example: Actual and predicted ratings
actual_ratings = [4, 3, 5, 2, 1]
predicted_ratings = [3.8, 2.9, 5.1, 2.2, 1.1]

# Calculate RMSE
rmse = np.sqrt(np.mean((np.array(actual_ratings) - np.array(predicted_ratings)) ** 2))
rmse
```

#### 4. **Mean Reciprocal Rank (MRR)**
MRR evaluates the rank of the first relevant item in the recommendation list. It averages the reciprocal of the rank at which the first relevant item is found for each user.

- **Formula**:
  \[
  \text{MRR} = \frac{1}{|U|} \sum_{u=1}^{|U|} \frac{1}{\text{rank}_u}
  \]
  Where:
  - \( \text{rank}_u \) is the position of the first relevant item for user \( u \).

MRR is useful when the focus is on finding at least one relevant recommendation early in the list.

### Step 3: Calculate Metrics for a Set of Users
In real-world scenarios, we evaluate recommendations for many users. The metrics are computed for each user and averaged over the entire set of users.

Here’s an example that combines these metrics for a recommendation system.

```python
# Example data: Actual items interacted by users
user_actual_items = {
    'user1': {1, 2, 3},
    'user2': {3, 4, 5},
    'user3': {1, 5, 6},
}

# Example data: Recommended items by the engine
user_recommended_items = {
    'user1': [2, 3, 7, 8],
    'user2': [1, 5, 6, 10],
    'user3': [2, 5, 6, 11],
}

# Calculate Precision@K for each user
precision_k_values = []
recall_k_values = []

K = 4  # Top-K recommendations

for user, actual_items in user_actual_items.items():
    recommended_items = user_recommended_items[user]
    
    # Precision@K
    precision_k = len(set(recommended_items[:K]) & actual_items) / K
    precision_k_values.append(precision_k)
    
    # Recall@K
    recall_k = len(set(recommended_items[:K]) & actual_items) / len(actual_items)
    recall_k_values.append(recall_k)

# Average Precision@K and Recall@K across all users
avg_precision_k = np.mean(precision_k_values)
avg_recall_k = np.mean(recall_k_values)

avg_precision_k, avg_recall_k
```

### Step 4: Interpreting the Results
After computing the evaluation metrics, you can interpret the results:

- **High precision** means most of the recommended items are relevant, but it doesn't account for how many relevant items were missed.
- **High recall** means most relevant items were found, but there may be many irrelevant items recommended.
- **RMSE** should be minimized in rating-based systems. A lower RMSE means the predicted ratings are closer to actual ratings.
- **MAP** and **MRR** are more focused on ranking accuracy and are useful when the position of relevant items in the recommendation list matters.

### Summary of Key Metrics
| Metric        | Definition                                          | Formula                                                                                   |
|---------------|-----------------------------------------------------|-------------------------------------------------------------------------------------------|
| Precision@K   | Relevant items in top K                             | \( \frac{\text{Relevant in Top-K}}{K} \)                                                  |
| Recall@K      | Relevant items found out of all relevant items      | \( \frac{\text{Relevant in Top-K}}{\text{Total Relevant}} \)                              |
| RMSE          | Rating prediction error                             | \( \sqrt{\frac{1}{N} \sum_{i=1}^{N} (r_i - \hat{r}_i)^2} \)                               |
| MAP           | Precision averaged over all relevant items          | \( \frac{1}{m} \sum_{k=1}^{N} P(k) \times \text{rel}(k) \)                                |
| MRR           | Rank of first relevant item                         | \( \frac{1}{|U|} \sum_{u=1}^{|U|} \frac{1}{\text{rank}_u} \)                              |

### Conclusion
By using these metrics, you can measure the accuracy of recommendations, which helps fine-tune your recommendation engine to provide more relevant and personalized suggestions for users.