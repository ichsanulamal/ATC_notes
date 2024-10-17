# Machine & Deep Learning Algorithms Imbalanced Datasets Using Pandas ML

Sure! Here’s a more detailed look at each technique, including algorithms and how they work:

### A. SMOTE (Synthetic Minority Over-sampling Technique)

**Algorithm**:
1. For each instance in the minority class, identify its \( k \) nearest neighbors (often \( k = 5 \)).
2. Randomly select one or more of these neighbors.
3. Generate synthetic instances by interpolating between the selected minority instance and its neighbor. This is done using the formula:
   \[
   \text{Synthetic} = \text{Instance} + \text{rand}(0, 1) \times (\text{Neighbor} - \text{Instance})
   \]
4. Repeat until the desired level of balance is achieved.

**Use Case**: Effective for datasets where the minority class is significantly underrepresented.

---

### B. Tomek Links

**Algorithm**:
1. For each instance in the majority class, find its nearest neighbor in the minority class.
2. If these two instances are neighbors, and they belong to different classes, classify this pair as a Tomek Link.
3. Remove the majority class instance from the dataset, as it is likely to be noisy or close to the decision boundary.

**Use Case**: Useful for cleaning the dataset and clarifying class boundaries.

---

### C. Near Miss

**Algorithm**:
1. Determine the number of instances you want to keep in the minority class.
2. For each minority instance, identify the nearest majority instances.
   - **Near Miss 1**: Keep all minority instances and select the majority instances that are closest to the minority class.
   - **Near Miss 2**: Keep minority instances and select majority instances that are the furthest away from the minority instances.
   - **Near Miss 3**: A variation where a fixed number of nearest majority instances are chosen for each minority instance.

**Use Case**: Effective for reducing the size of the majority class while maintaining relevant instances.

---

### D. Neighborhood Cleaning Rule (NCR)

**Algorithm**:
1. For each instance in the majority class, identify its \( k \) nearest neighbors (from both classes).
2. If a majority instance is surrounded by a higher number of minority instances than majority ones (i.e., it is in a minority-heavy neighborhood), it can be removed.
3. This is done iteratively until no more majority instances can be removed without violating the neighborhood rule.

**Use Case**: Good for cleaning up noisy data and improving the clarity of the decision boundary.

---

### Summary

- **SMOTE** increases minority samples by generating new instances, helpful for training.
- **Tomek Links** removes ambiguous majority instances to improve class boundaries.
- **Near Miss** selectively downsamples the majority class, maintaining its relevance.
- **NCR** cleans up majority class noise, focusing on the neighborhood density of instances.

These techniques can be combined for better results, depending on your specific dataset and problem context. If you have a particular application in mind, I can help you tailor the approach!