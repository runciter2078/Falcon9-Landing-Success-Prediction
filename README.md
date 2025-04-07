# Falcon 9 Landing Success Prediction 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This repository contains all the work completed as part of the **IBM Data Science Professional Certificate - Capstone Project**. The goal of this project is to predict whether the first stage of the SpaceX Falcon 9 rocket will successfully land, enabling cost reduction through reusable rocket technology.

---

## Project Overview 📌

### **Objective**
The main objective of this project is to determine the factors that influence the success of Falcon 9's first stage landing and to develop a predictive model to assess landing success.

### **Context**
SpaceX has revolutionized the space industry by reducing launch costs through reusable rocket technology. By predicting landing success, a competing company (hypothetically named "Space Y") can optimize its operations and compete effectively in the commercial space market.

### **Key Steps**
1. Data collection using SpaceX's REST API and web scraping from Wikipedia.
2. Data cleaning and wrangling to prepare datasets for analysis.
3. Exploratory Data Analysis (EDA) using SQL and Python visualizations.
4. Interactive visual analytics with Folium maps and Plotly Dash dashboards.
5. Machine learning modeling to predict landing success using classification techniques.
6. Presentation of findings in a professional format.

---

## Repository Structure 📂

├── notebooks/
│ ├── 01-jupyter-labs-spacex-data-collection-api.ipynb # SpaceX API data collection
│ ├── 02-jupyter-labs-webscraping.ipynb # Web scraping from Wikipedia
│ ├── 03-labs-jupyter-spacex-data-wrangling.ipynb # Data cleaning and preparation
│ ├── 04-jupyter-labs-eda-sql-coursera_sqllite.ipynb # SQL-based exploratory data analysis
│ ├── 05-jupyter-labs-eda-dataviz-v2.ipynb # Data visualization with Python
│ ├── 06-lab_jupyter_launch_site_location.ipynb # Interactive Folium maps
│ ├── 07-SpaceX_Machine Learning Prediction_Part_5.ipynb # Machine learning models
├── datasets/
│ ├── dataset_part_1.csv # Cleaned dataset (API + web scraping)
│ ├── dataset_part_2.csv # Dataset after EDA and feature engineering
│ ├── dataset_part_3.csv # Final dataset for machine learning
├── presentation/
│ ├── Falcon9_Landing_Success_Presentation.pdf # Final presentation in PDF format
├── README.md # This file
└── requirements.txt # Python dependencies

text

---

## Installation ⚙️

1. Clone this repository:
git clone https://github.com/runciter2078/Falcon9-Landing-Success-Prediction.git
cd Falcon9-Landing-Success-Prediction

text

2. Install required Python libraries:
pip install -r requirements.txt

text

3. Run Jupyter Notebooks:
jupyter notebook

text

---

## Notebooks Overview 📓

### **1. Data Collection**
- **Notebook:** `01-jupyter-labs-spacex-data-collection-api.ipynb`  
- Collected launch data using SpaceX's REST API.
- Extracted information about rockets, payloads, launch sites, and landing outcomes.

- **Notebook:** `02-jupyter-labs-webscraping.ipynb`  
- Scraped historical launch data from Wikipedia for additional insights.

### **2. Data Wrangling**
- **Notebook:** `03-labs-jupyter-spacex-data-wrangling.ipynb`  
- Cleaned and transformed raw data into structured datasets.
- Handled missing values, standardized formats, and created new features.

### **3. Exploratory Data Analysis (EDA)**
- **Notebook:** `04-jupyter-labs-eda-sql-coursera_sqllite.ipynb`  
- Performed SQL-based queries to explore relationships in the data.

- **Notebook:** `05-jupyter-labs-eda-dataviz-v2.ipynb`  
- Created visualizations to analyze payload mass, orbit types, launch sites, and landing success rates.

### **4. Interactive Visual Analytics**
- **Notebook:** `06-lab_jupyter_launch_site_location.ipynb`  
- Built interactive maps with Folium to visualize launch site locations and proximity to key areas.

- **Dashboard:** Plotly Dash application (code embedded in notebooks).  
- Developed a dynamic dashboard for analyzing payload vs. landing success interactively.

### **5. Predictive Modeling**
- **Notebook:** `07-SpaceX_Machine Learning Prediction_Part_5.ipynb`  
- Trained machine learning models (Logistic Regression, SVM, Decision Trees, KNN).
- Optimized hyperparameters using GridSearchCV.
- Evaluated models based on accuracy and confusion matrices.

---

## Results Summary 🔍

### Key Insights:
1. Launch success rates vary significantly based on payload mass, orbit type, and launch site.
2. Logistic Regression was the best-performing model with an accuracy of **92%** on test data.
3. Interactive maps revealed that proximity to coastal areas influences landing success rates.

---

## Presentation 📊

The final presentation summarizes all findings from this project:
- [Falcon9_Landing_Success_Presentation.pdf](./presentation/Falcon9_Landing_Success_Presentation.pdf)

It includes:
1. Executive Summary.
2. Introduction to the problem statement.
3. Methodology: Data collection, wrangling, EDA, visualization, and modeling.
4. Results: Key insights from EDA, SQL queries, interactive maps, dashboards, and machine learning models.
5. Conclusion: Recommendations for future research and applications.

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments 🙌

This project was developed as part of the IBM Data Science Professional Certificate on Coursera.

Special thanks to:
- IBM for providing the course materials.
- The SpaceX API team for making their data publicly available.
- The Coursera community for peer reviews and feedback.

---
