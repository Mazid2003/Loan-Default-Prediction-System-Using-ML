# 💸 Loan Default Prediction using Machine Learning

This project aims to build a robust Machine Learning model that predicts whether a loan applicant is likely to default or repay based on historical financial data. It involves data preprocessing, exploratory data analysis (EDA), model building, evaluation, and comparison of multiple algorithms.

**🎯 Project Objective**

To predict the likelihood of loan default using customer demographics and financial behavior, enabling banks and financial institutions to make informed loan approval decisions.

**📂 Dataset Overview**

The dataset contains 14 features and a target column:

| Feature         | Description                                              |
| --------------- | -------------------------------------------------------- |
| `Age`           | Applicant's age                                          |
| `Experience`    | Years of professional experience                         |
| `Income`        | Annual income (in \$1000s)                               |
| `Family`        | Family size (number of dependents)                       |
| `CCAvg`         | Average monthly credit card spend                        |
| `Education`     | Education level (1: Undergrad, 2: Graduate, 3: Advanced) |
| `Mortgage`      | Value of house mortgage                                  |
| `Personal Loan` | **Target** (1: Loan accepted, 0: Rejected)               |
| Other fields    | ZIPCode, Online banking, Credit Card use, etc.           |

## 🔧 Workflow

### ✅ 1. Data Preprocessing

Removed unnecessary columns (ID, ZIPCode)

Handled missing values (if any)

Scaled features (e.g., Income, CCAvg, Mortgage)

Renamed target column to Loan_Status

**📊 2. Exploratory Data Analysis (EDA)**

Distribution plots for features like Income, CCAvg, Mortgage

Countplots to compare Loan_Status with:

Education

Family

Online banking

Heatmap of correlation matrix

🤖 3. Model Building
Split data into training and test sets (80–20)

Trained three classification models:

Logistic Regression

Decision Tree

Random Forest

📈 4. Model Evaluation
Evaluated each model using:

Accuracy

Confusion Matrix

Precision, Recall, F1-score

🏆 Model Performance Comparison
Model	Accuracy	F1-Score (Class 1)
Random Forest	99.1%	0.96
Decision Tree	98.8%	0.94
Logistic Regression	95.0%	0.75

✅ Best Model: Random Forest – due to its superior accuracy and balanced precision-recall.

📌 Key Insights from EDA
Customers with higher income, advanced education, and existing credit cards are more likely to accept loans.

Most loan approvals come from applicants with family sizes of 1 or 4.

Online banking users are more likely to get loans approved.

🧠 Tech Stack Used
Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

✅ Deliverables
Cleaned and annotated Jupyter Notebook

EDA with visualizations

Final model with evaluation

PDF report (optional)

🚀 How to Run
Clone this repo

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Jupyter notebook:

bash
Copy
Edit
jupyter notebook Loan_Default_Prediction.ipynb
📌 License
This project is open-source and free to use under the MIT License.

> 📍 This project is part of the Machine Learning Trainee Program by **InnovateCloud Solutions** (2025).
