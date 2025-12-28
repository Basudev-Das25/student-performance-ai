This project demonstrates a complete Machine Learning workflow, including data preprocessing, regression modeling, evaluation, deployment, and responsible AI practices. The application is deployed live and allows users to interact with a trained ML model through a clean web interface.

# 🎓 Student Performance Predictor (Machine Learning Web App)

🔗 **Live Demo:** https://student-performance-ai-p30z.onrender.com  
📂 **GitHub Repository:** https://github.com/YOUR_USERNAME/student-performance-ai  

An end-to-end Machine Learning web application that predicts student academic performance based on study behavior and historical data. The project demonstrates the full ML lifecycle from data preprocessing and model training to deployment and responsible AI practices.

---

## 🚀 Project Overview

This application uses a **Linear Regression** model to predict a student’s final score using:
- Hours studied
- Attendance percentage
- Previous exam score

The trained model is integrated into a **Flask-based web application** that allows users to enter inputs and receive predictions in real time.

---

## 🧠 Machine Learning Workflow

1. Data loading and preprocessing using **pandas**
2. Feature selection and target definition
3. Model training using **scikit-learn**
4. Model serialization using **pickle**
5. Model inference through a Flask web interface

---

## 🏗️ Project Architecture

student-performance-ai/
│
├── data/
│ └── students.csv # Dataset
│
├── model/
│ └── train_model.py # Model training script
│
├── app/
│ ├── app.py # Flask application
│ ├── model.pkl # Trained ML model
│ └── templates/
│ └── index.html # Frontend UI
│
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignored files


---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Machine Learning:** scikit-learn  
- **Data Processing:** pandas, NumPy  
- **Backend Framework:** Flask  
- **Model Deployment:** Gunicorn  
- **Version Control:** Git & GitHub  
- **Hosting:** Render  

---

## 📊 Dataset

The dataset consists of academic indicators such as:
- Hours studied
- Attendance percentage
- Previous scores
- Final score (target variable)

Sample data:
```csv
hours_studied,attendance,previous_score,final_score
5,90,70,75
8,95,85,88
