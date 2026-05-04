# 📊 Employee Dashboard using Streamlit

## 🧠 Overview

This project is an **interactive Employee Analytics Dashboard** built using Streamlit and Python.
It allows users to explore employee data, analyze salary distribution, and visualize key HR metrics in an interactive way.

The dashboard provides insights into **salary, experience, departments, and employee distribution across countries and centers**.

---

## 🚀 Features

* 📂 Load and display employee dataset
* 📊 KPI metrics (salary, experience, overtime, etc.)
* 🎛️ Interactive sidebar filters
* 📈 Department-wise salary analysis
* 🔍 Scatter plots for relationships between variables
* 🥧 Pie charts for distribution analysis
* ⚡ Fully interactive dashboard using Plotly

---

## 🛠️ Technologies Used

* Python 🐍
* Streamlit (Web App Framework)
* Pandas (Data Processing)
* NumPy (Numerical Computing)
* Plotly (Data Visualization)

---

## 📂 Project Structure

```id="a8q3lm"
├── app.py
├── Employees.xlsx
├── employee.jpeg
└── README.md
```

---

## ▶️ How to Run

### 1. Install Dependencies

```bash id="k9x2vn"
pip install streamlit pandas numpy plotly openpyxl
```

### 2. Run the App

```bash id="p5m7qd"
streamlit run app.py
```

---

## 🎯 Dashboard Features Explained

### 📊 KPI Section

* Maximum & minimum years of experience
* Maximum & minimum monthly salary
* Maximum & minimum annual salary
* Overtime statistics

---

### 💰 Salary Analysis

* Monthly salary by department
* Annual salary by department

---

### 📉 Visualizations

* Scatter plots:

  * Monthly Salary vs Department
  * Monthly Salary vs Years of Experience

* Pie charts:

  * Gender distribution
  * Employees per country
  * Employees per center

---

## 📊 Key Insights

* Salary varies significantly across departments
* Experience has a strong influence on salary
* Employee distribution is uneven across countries and centers
* Overtime patterns help identify workload differences

---

## 💡 Future Improvements

* Add machine learning model for salary prediction 🤖
* Add date-based analysis (historical trends) 📅
* Improve UI with advanced Streamlit components
* Add export feature (PDF/Excel reports)
* Deploy on Streamlit Cloud ☁️

---

## 👨‍💻 Author

**Youssef Ayman**
AI Engineer & Data Scientist

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!
