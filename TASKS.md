# Finding Donors for CharityML - Project Task Assignments & File Mapping

## Project Overview
This document outlines the detailed task distribution for the "Finding Donors for CharityML" machine learning project. The team consists of 6 members (1 Team Leader and 5 Team Members). 
Tasks have been mapped to specific files in our repository architecture to ensure no merge conflicts and clear technical ownership.

---

### Member 1: Data Engineer & Baseline Analysis
**Role Description:** Responsible for data readiness, preprocessing, and establishing the baseline metric.

**Files to Work On:**
- `notebooks/01_data_baseline.ipynb` (Main workspace)
- `src/data_prep.py` (Functions to clean/scale data)
- Output: `data/processed/census_cleaned.csv`

**Detailed Tasks:**
1. **Implementation: Data Exploration:** Calculate total number of records, number of individuals earning >50K, <=50K, and the percentage of those earning >50K.
2. **Implementation: Data Preprocessing:** Apply logarithmic transformation, scale numerical features (MinMaxScaler), perform one-hot encoding using `pandas.get_dummies()`, and encode the target variable `income`. 
   > *Pro-Tip: Move the final cleaning code into a function inside `src/data_prep.py` so others can import it!*
3. **Question 1: Naive Predictor Performance:** Calculate Accuracy, Precision, Recall, and F-score assuming the model always predicts >50K to establish the baseline performance.

---

### Member 2: Machine Learning Researcher
**Role Description:** Responsible for theoretical research and algorithm selection justification.

**Files to Work On:**
- No direct coding files. Research should be documented as text/markdown to be later added to `reports/REPORT.md`.

**Detailed Tasks:**
1. **Question 2: Model Application:** Select three supervised learning classification models (e.g., Random Forest, AdaBoost, SVM) and for each model:
  - Describe one real-world application.
  - Detail the model's strengths and scenarios where it performs well.
  - Detail the model's weaknesses and scenarios where it performs poorly.
  - Justify why the model is a strong candidate for this specific census dataset.

---

### Member 3: Machine Learning Pipeline Engineer
**Role Description:** Responsible for building the infrastructure to train and evaluate the selected models.

**Files to Work On:**
- `notebooks/02_model_eval.ipynb` (Main workspace)
- `src/model_pipeline.py` (Functions for training and evaluating)

**Detailed Tasks:**
1. **Implementation: Creating a Training and Predicting Pipeline:** Write the `train_predict` function to record training time, prediction time, accuracy score, and F-beta score. Save this function in `src/model_pipeline.py`.
2. **Implementation: Initial Model Evaluation:** Initialize the three selected models from Member 2. Import the cleaned data (`census_cleaned.csv`). Train and test them on varying sample sizes (1%, 10%, 100%) and use `src/visuals.py` to plot performance metrics.

---

### Member 4: Machine Learning Optimization Engineer
**Role Description:** Responsible for hyperparameter tuning and extracting the maximum performance from the winning algorithm.

**Files to Work On:**
- `notebooks/03_model_tuning.ipynb` (Main workspace)

**Detailed Tasks:**
1. **Implementation: Model Tuning:** Utilize `GridSearchCV` and `make_scorer` (with beta=0.5) to search for optimal hyperparameters on the best performing model identified by Member 3.
2. **Question 5: Final Model Evaluation:** Fill out the evaluation table comparing the unoptimized model with the optimized model and the initial naive predictor. Provide written analysis on the improvements achieved.

---

### Member 5: Data Communicator & Analyst
**Role Description:** Responsible for interpreting results logically, drafting the final report, and explaining complex concepts to non-technical stakeholders.

**Files to Work On:**
- `reports/REPORT.md` (Main drafting space)

**Detailed Tasks:**
1. **Question 3: Choosing the Best Model:** Based on Member 3's visualizations, provide a comprehensive written justification for the final chosen model based on F-score, prediction/training time, and data suitability.
2. **Question 4: Describing the Model in Layman's Terms:** Write a clear, non-technical explanation of how the chosen model is trained and how it makes predictions for CharityML stakeholders (avoiding mathematical jargon).
3. **Report Compilation:** Write Sections 1, 2, 3, and 11 of `REPORT.md` and assemble findings from the rest of the team into the final document structure.

---

### Member 6 (Team Leader): Feature Analyst & Project Integrator
**Role Description:** Responsible for final integrations, code review, analyzing feature relevance, and final deliverables.

**Files to Work On:**
- `notebooks/04_feature_analysis.ipynb` (Workspace for feature importance)
- `notebooks/final_project.ipynb` (Final assembled notebook)
- `reports/Final_Report.html` (Exported deliverable)

**Detailed Tasks:**
1. **Question 6: Feature Relevance Observation:** Hypothesize and rank the top 5 features most predictive of an individual's income prior to running programmatic checks.
2. **Implementation: Extracting Feature Importance:** Use the `feature_importances_` attribute of the optimized model to extract the actual top 5 most important features.
3. **Question 7: Extracting Feature Importance:** Compare the initial hypothesis (Q6) with the actual programmatic results and explain any discrepancies.
4. **Question 8: Effects of Feature Selection:** Train a cloned model on only the top 5 features. Analyze the trade-off between reduced training time and model precision/accuracy.
5. **Integration & Code Review:** Consolidate all teammates' code into `notebooks/final_project.ipynb`. Ensure cells run sequentially without errors and export the final HTML report.

---
