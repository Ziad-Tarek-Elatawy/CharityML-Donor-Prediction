# Finding Donors for CharityML - Project Task Assignments

## Project Overview
This document outlines the task distribution for the "Finding Donors for CharityML" machine learning project. The team consists of 6 members (1 Team Leader and 5 Team Members). Tasks have been divided equally to ensure a fair workload and to align with each member's role in the complete machine learning pipeline.

---

### Member 1: Data Engineer & Baseline Analysis
**Role Description:** Responsible for data readiness, preprocessing, and establishing the baseline metric.

**Assigned Tasks:**
- **Implementation: Data Exploration:** Calculate total number of records, number of individuals earning >50K, <=50K, and the percentage of those earning >50K.
- **Implementation: Data Preprocessing:** Apply logarithmic transformation, scale numerical features (MinMaxScaler), perform one-hot encoding using `pandas.get_dummies()`, and encode the target variable `income`.
- **Question 1: Naive Predictor Performance:** Calculate Accuracy, Precision, Recall, and F-score assuming the model always predicts >50K to establish the baseline performance.

---

### Member 2: Machine Learning Researcher
**Role Description:** Responsible for theoretical research and algorithm selection justification.

**Assigned Tasks:**
- **Question 2: Model Application:** Select three supervised learning classification models (e.g., Random Forest, AdaBoost, SVM) and for each model:
  - Describe one real-world application.
  - Detail the model's strengths and scenarios where it performs well.
  - Detail the model's weaknesses and scenarios where it performs poorly.
  - Justify why the model is a strong candidate for this specific census dataset.

---

### Member 3: Machine Learning Pipeline Engineer
**Role Description:** Responsible for building the infrastructure to train and evaluate the selected models.

**Assigned Tasks:**
- **Implementation: Creating a Training and Predicting Pipeline:** Write the `train_predict` function to record training time, prediction time, accuracy score, and F-beta score.
- **Implementation: Initial Model Evaluation:** Initialize the three selected models from Member 2. Train and test them on varying sample sizes (1%, 10%, 100%) and use the evaluation pipeline to visualize performance metrics.

---

### Member 4: Machine Learning Optimization Engineer
**Role Description:** Responsible for hyperparameter tuning and extracting the maximum performance from the winning algorithm.

**Assigned Tasks:**
- **Implementation: Model Tuning:** Utilize `GridSearchCV` and `make_scorer` (with beta=0.5) to search for optimal hyperparameters on the best performing model from Member 3's evaluation.
- **Question 5: Final Model Evaluation:** Fill out the evaluation table comparing the Unoptimized Model with the Optimized Model and the initial Naive Predictor. Provide written analysis on the improvements achieved.

---

### Member 5: Data Communicator & Analyst
**Role Description:** Responsible for interpreting results logically and explaining complex concepts to non-technical stakeholders.

**Assigned Tasks:**
- **Question 3: Choosing the Best Model:** Based on Member 3's visualizations, provide a comprehensive written justification for the final chosen model based on F-score, prediction/training time, and data suitability.
- **Question 4: Describing the Model in Layman's Terms:** Write a clear, non-technical explanation of how the chosen model is trained and how it makes predictions for CharityML stakeholders (avoiding mathematical jargon).

---

### Member 6 (Team Leader): Feature Analyst & Project Integrator
**Role Description:** Responsible for final integrations, code review, and analyzing feature relevance.

**Assigned Tasks:**
- **Question 6: Feature Relevance Observation:** Hypothesize and rank the top 5 features most predictive of an individual's income prior to running programmatic checks.
- **Implementation: Extracting Feature Importance:** Use the `feature_importances_` attribute of the optimized model to extract the actual top 5 most important features.
- **Question 7: Extracting Feature Importance:** Compare the initial hypothesis (Q6) with the actual programmatic results and explain any discrepancies.
- **Question 8: Effects of Feature Selection:** Train a cloned model on only the top 5 features. Analyze the trade-off between reduced training time and model precision/accuracy.
- **Integration & Code Review:** Consolidate all teammates' code and text answers into the master Jupyter Notebook. Ensure cells run sequentially without errors and export the final HTML report.

---
