# 🎓 Student Score Predictor  

A Machine Learning project that predicts student exam scores based on multiple academic and lifestyle factors such as study hours, attendance, sleep hours, mental health rating, and part-time job status.  

---

## 📌 Overview
Academic performance depends on much more than just study hours. Lifestyle choices and personal responsibilities play a major role in shaping outcomes.  
This project uses **Machine Learning models** to predict exam scores, helping to analyze how various factors impact student success.  

It combines **machine learning** with an easy-to-use **Streamlit web app** for deployment.

This project predicts students' exam scores based on multiple factors such as:
- Study Hours ⏳
- Attendance 📅
- Sleep Hours 😴
- Mental Health Rating 🧠
- Part-Time Job Status 💼

It combines **machine learning** with an easy-to-use **Streamlit web app** for deployment.
---

## 📊 Dataset
The dataset contains student records with the above features and corresponding exam scores (0–100).  
Data was preprocessed to handle missing values, encode categorical variables, and normalize features for better model accuracy.  

---
## Project Workflow 🛠️

1. **Data Preprocessing & EDA**
   - Performed in Jupyter Notebook (`notebooks/StudentScorePredictor.ipynb`)
   - Includes data cleaning, visualization, and feature engineering

2. **Model Training & Evaluation**
   - Trained regression models to predict student scores
   - Evaluated with metrics like R², MAE, and RMSE

3. **Deployment**
   - Streamlit app (`app.py`) built for real-time predictions

---

## 🛠️ Tech Stack
- **Python**  
- **Scikit-learn** – ML algorithms  
- **Pandas & NumPy** – Data handling  
- **Matplotlib & Seaborn** – Visualization  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Vithikasharma06/Student-Score-Predictor.git
   cd Student-Score-Predictor

2. Create a virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

3. Install dependencies
   numpy==1.26.5
   pandas==2.2.0
   matplotlib==3.8.1
   seaborn==0.12.3
   scikit-learn==1.3.2
   jupyter==1.0.0
   notebook==7.7.2
   streamlit==1.26.0
  Save the above text in a file named requirements.txt in your project root folder.
  Install all dependencies with:
  pip install -r requirements.txt

5. Open notebooks/StudentScorePredictor.ipynb to explore data cleaning, EDA, and training.

6. Run the Streamlit App

   streamlit run app.py 



**How it Works 🔮**
  User enters details like study hours, attendance, sleep, etc.
  Model processes inputs using trained regression algorithm.
  Streamlit app displays predicted exam score instantly.
