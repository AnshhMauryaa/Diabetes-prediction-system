# Diabetes-prediction-system
Developed a binary classification model using Support Vector Machine (SVM) with a linear kernel on the Pima Indians Diabetes Dataset (768 samples, 8 features), incorporating feature standardization and stratified train-test splitting for robust model training
Diabetes Prediction System using Machine Learning
Overview

The Diabetes Prediction System is a Machine Learning project that predicts whether a person is diabetic or non-diabetic based on key medical and demographic attributes. The project leverages a Support Vector Machine (SVM) classifier trained on the Pima Indians Diabetes Dataset and provides a complete pipeline from data preprocessing to prediction.

The primary objective of this project is to demonstrate the application of machine learning techniques in healthcare by assisting in the early identification of diabetes risk using patient health indicators.

Features
Diabetes risk prediction using Machine Learning
Data preprocessing and feature standardization
Binary classification using Support Vector Machine (SVM)
Real-time prediction on new patient data
Model and scaler serialization using Pickle
Reproducible training and evaluation pipeline
Dataset

The project uses the Pima Indians Diabetes Dataset, which contains 768 patient records and 8 input features.

Input Features
Pregnancies
Glucose Level (mg/dL)
Blood Pressure (mmHg)
Skin Thickness
Insulin
Body Mass Index (BMI)
Diabetes Pedigree Function
Age
Target Variable
0 → Non-Diabetic
1 → Diabetic
Project Workflow
1. Data Loading

The dataset is loaded into a Pandas DataFrame for analysis and preprocessing.

2. Data Preprocessing
Separation of features and target labels
Feature scaling using StandardScaler
Transformation of input data into standardized format
3. Train-Test Split

The dataset is divided using an 80:20 stratified split to preserve class distribution.

4. Model Training

A Support Vector Machine (SVM) with a Linear Kernel is trained on the standardized training dataset.

5. Model Evaluation

The model is evaluated on both training and testing datasets using classification accuracy.

6. Prediction

The trained model can predict diabetes status for new patient records after applying the same preprocessing steps used during training.

7. Model Persistence

The trained model and scaler are saved using Pickle for future deployment and inference.

Model Performance
Metric	Value
Training Accuracy	78.66%
Test Accuracy	77.27%
Technologies Used
Python
NumPy
Pandas
Scikit-learn
Pickle
Project Structure
Diabetes-Prediction/
│
├── diabetes.csv
├── diabetes_prediction.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
Installation
Clone the Repository
git clone https://github.com/your-username/Diabetes-Prediction.git
cd Diabetes-Prediction
Install Dependencies
pip install -r requirements.txt
Run the Project
python diabetes_prediction.py
Example Input
input_data = (1,89,66,23,94,28.1,0.167,21)
Example Output
The person is not diabetic
Future Improvements
Hyperparameter tuning for improved accuracy
Comparison with Random Forest, XGBoost, and Logistic Regression
Cross-validation-based evaluation
Streamlit web application deployment
Model explainability using SHAP and feature importance analysis
Integration with healthcare monitoring systems
Learning Outcomes

Through this project, I gained practical experience in:

Data preprocessing and feature engineering
Feature scaling using StandardScaler
Binary classification using Support Vector Machines
Model evaluation and performance analysis
Machine Learning workflow implementation
Model deployment preparation using Pickle serialization
Author

Ansh Maurya

This project was developed as part of my Machine Learning learning journey to understand classification algorithms and their application in healthcare analytics.
