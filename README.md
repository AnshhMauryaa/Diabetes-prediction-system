# 🩺 Diabetes Prediction System using Machine Learning

## 📌 Project Overview

This project implements a **Diabetes Prediction System** using **Machine Learning** to predict whether a person is diabetic or non-diabetic based on key medical attributes. The model is trained on the **Pima Indians Diabetes Dataset** and utilizes a **Support Vector Machine (SVM)** classifier for binary classification.

The project demonstrates the practical application of machine learning in healthcare by assisting in the early detection of diabetes through data-driven prediction.

---

## 🚀 Key Features

- ✅ Diabetes prediction using Support Vector Machine (SVM)
- ✅ Data preprocessing and feature standardization
- ✅ Real-time prediction on new patient data
- ✅ Model persistence using Pickle
- ✅ End-to-end machine learning pipeline
- ✅ Healthcare-focused classification project

---

## 📊 Dataset Information

The model is trained on the **Pima Indians Diabetes Dataset**, containing **768 patient records** and **8 clinical features**.

### Input Features

| Feature | Description |
|----------|------------|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| Blood Pressure | Diastolic blood pressure (mmHg) |
| Skin Thickness | Triceps skin fold thickness |
| Insulin | 2-Hour serum insulin |
| BMI | Body Mass Index |
| Diabetes Pedigree Function | Genetic predisposition score |
| Age | Age of the patient |

### Target Variable

| Value | Meaning |
|--------|---------|
| 0 | Non-Diabetic |
| 1 | Diabetic |

---

## ⚙️ Machine Learning Workflow

```text
Data Collection
       ↓
Data Preprocessing
       ↓
Feature Standardization
       ↓
Train-Test Split (80:20)
       ↓
SVM Model Training
       ↓
Model Evaluation
       ↓
Prediction on New Data
       ↓
Model Serialization
```

---

## 🧠 Model Details

| Parameter | Value |
|------------|--------|
| Algorithm | Support Vector Machine (SVM) |
| Kernel | Linear |
| Feature Scaling | StandardScaler |
| Train-Test Split | 80:20 |
| Dataset Size | 768 Records |
| Number of Features | 8 |

---

## 📈 Performance Metrics

| Metric | Score |
|----------|----------|
| Training Accuracy | **78.66%** |
| Test Accuracy | **77.27%** |

The close training and testing accuracies indicate that the model generalizes reasonably well without significant overfitting.

---

## 💻 Tech Stack

- Python
- NumPy
- Pandas
- Scikit-learn
- Pickle

---

## 📂 Project Structure

```bash
Diabetes-Prediction-System/
│
├── diabetes.csv
├── diabetes_prediction.py
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ Installation & Usage

### Clone the Repository

```bash
git clone https://github.com/your-username/Diabetes-Prediction-System.git
cd Diabetes-Prediction-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python diabetes_prediction.py
```

---

## 🔍 Sample Prediction

### Input

```python
input_data = (1, 89, 66, 23, 94, 28.1, 0.167, 21)
```

### Output

```text
The person is not diabetic
```

---

## 🎯 Future Improvements

- Hyperparameter tuning for improved accuracy
- Comparison with Random Forest and XGBoost
- Cross-validation based evaluation
- Streamlit web application deployment
- Model explainability using SHAP
- Integration with healthcare analytics dashboards

---

## 📚 Skills Demonstrated

- Machine Learning
- Data Preprocessing
- Feature Engineering
- Feature Scaling
- Classification Algorithms
- Support Vector Machines (SVM)
- Model Evaluation
- Python Programming
- Model Deployment

---

## 👨‍💻 Author

**Ansh Maurya**

Aspiring Software Engineer | Machine Learning Enthusiast | Data Science Learner

⭐ If you found this project useful, consider giving it a star!

