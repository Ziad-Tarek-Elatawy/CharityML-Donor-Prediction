# 🌟 CharityML Donor Prediction

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-notebook-orange.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-0.24+-yellow.svg)

## 📖 Project Overview
Welcome to the **CharityML Donor Prediction** project! This project applies supervised machine learning techniques to a modified U.S. Census dataset to predict whether an individual earns more than $50,000 annually. 

Understanding an individual's income bracket helps non-profit organizations like CharityML better determine their donation target audience, significantly reducing the overhead costs of sending outreach emails to the wrong candidates.

---

## 📑 Table of Contents
- [Technologies Used](#-technologies-used)
- [Project Directory Structure](#-project-directory-structure)
- [The Dataset](#-the-dataset)
- [Setup & Installation](#-setup--installation)
- [Usage](#-usage)
- [Results & Evaluation](#-results--evaluation)

---

## 🛠 Technologies Used
- **Python 3.x**
- **Pandas** (Data manipulation and analysis)
- **NumPy** (Numerical computing)
- **Scikit-Learn** (Machine Learning algorithms & evaluation)
- **Matplotlib** (Data visualization)
- **Jupyter Notebook** (Interactive development)

---

## 📂 Project Directory Structure

```text
CharityML Donor Prediction/
│
├── data/                     # Local data storage 
│   ├── raw/                  # Original, immutable dataset (census.csv)
│   └── processed/            # Cleaned data ready for modeling
│
├── notebooks/                # Jupyter Notebooks for analysis and modeling
│   ├── 01_data_baseline.ipynb      
│   ├── 02_model_eval.ipynb         
│   ├── 03_model_tuning.ipynb       
│   ├── 04_feature_analysis.ipynb   
│   └── final_project.ipynb         # Master notebook integrating all work
│
├── src/                      # Source code for repeated functions
│   ├── data_prep.py          # Data cleaning and scaling scripts
│   ├── model_pipeline.py     # Training and evaluation pipelines
│   └── visuals.py            # Custom visualization functions
│
├── reports/                  # Generated analysis reports
│   ├── figures/              # Exported evaluation charts
│   ├── REPORT.md             # Written project report and summary
│   └── Final_Report.html     # HTML export of the final notebook
│
├── README.md                 # Project representation and instructions
├── TASKS.md                  # Project task distribution for the team
└── requirements.txt          # Python package dependencies
```

---

## 📊 The Dataset
The modified census dataset consists of approximately **32k data points**, with each data point having **13 features**. This dataset is a modified version of the dataset published in the paper *"Scaling Up the Accuracy of Naive-Bayes Classifiers: a Decision-Tree Hybrid"* by Ron Kohavi (1996). 

### Target Variable
- `income`: Income Class (<=50K, >50K)

### Selected Features
- `age`: Continuous
- `workclass`: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov...
- `education_level`: Bachelors, Some-college, 11th, HS-grad, Prof-school...
- `education-num`: Continuous
- `marital-status`: Married-civ-spouse, Divorced, Never-married, Separated...
- `occupation`: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial...
- `relationship`: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
- `race`: Black, White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other.
- `sex`: Female, Male.
- `capital-gain`: Continuous
- `capital-loss`: Continuous
- `hours-per-week`: Continuous
- `native-country`: United-States, Cambodia, England, Puerto-Rico, Canada...

---

## 🚀 Setup & Installation

**1. Clone the repository:**
```bash
git clone https://github.com/your-username/CharityML-Donor-Prediction.git
cd CharityML-Donor-Prediction
```

**2. Create a virtual environment (Optional but Recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

**3. Install the required dependencies:**
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

To run the interactive Jupyter Notebook and view the analysis, execute the following command in the terminal from the `notebooks` directory:

```bash
cd notebooks
jupyter notebook final_project.ipynb
```

---

## 🏆 Results & Evaluation
*To be updated once final model evaluation is complete.* 

The primary metric used for evaluating the models in this project is the **F-beta score** (with beta = 0.5), which puts more emphasis on precision over recall, ensuring that CharityML does not waste resources reaching out to individuals who are highly unlikely to donate.
