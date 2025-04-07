# Falcon 9 Landing Success Prediction Project 🚀

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*Academic project for IBM Data Science Professional Certificate - Capstone Course*

## Project Overview 📌
This repository contains the complete workflow for predicting SpaceX Falcon 9 first stage landing success. Developed as part of IBM's Data Science Professional Certificate capstone project, it demonstrates end-to-end data science skills including:

- Data collection via REST API and web scraping
- SQL and Python-based EDA
- Interactive visualization with Folium and Plotly
- Machine learning classification models

**Key Question:** *What factors determine successful Falcon 9 first stage landings, and can we predict them accurately?*

## Learning Objectives 🎯
This project demonstrates:
- API data collection and web scraping techniques
- Data wrangling with Pandas/Numpy
- Exploratory Analysis using SQL and Python
- Interactive dashboard development
- Machine learning model development/deployment
- Professional reporting and presentation skills

## Repository Structure 📂
├── 01-jupyter-labs-spacex-data-collection-api.ipynb # SpaceX API data collection
├── 02-jupyter-labs-webscraping.ipynb # Wikipedia launch history scraping
├── 03-labs-jupyter-spacex-Data wrangling.ipynb # Data cleaning & preprocessing
├── 04-jupyter-labs-eda-sql-coursera_sqllite.ipynb # SQL-based EDA
├── 05-jupyter-labs-eda-dataviz-v2.ipynb # Visualization & feature engineering
├── 06-lab_jupyter_launch_site_location.ipynb # Interactive Folium maps
├── 07-SpaceX_Machine Learning Prediction_Part_5.ipynb # Predictive modeling
├── dataset_part_*.csv # Processed datasets
└── requirements.txt # Python dependencies

text

## Installation ⚙️
1. Clone repository:
git clone https://github.com/runciter2078/Falcon9-Landing-Success-Prediction.git

text
2. Install dependencies:
pip install -r requirements.txt

text

## Usage 🖥️
Execute notebooks in numerical order:
jupyter notebook 01-jupyter-labs-spacex-data-collection-api.ipynb

text

Key components:
- **Data Collection:** Mix of SpaceX API (real-time) and Wikipedia scraping (historical)
- **EDA:** SQL queries and statistical analysis in Jupyter
- **Visualization:** Folium maps for launch sites, Plotly dashboards
- **Modeling:** Logistic Regression, SVM, Decision Trees, KNN

## Key Findings 🔍
- Launch success rate: 60% (2010-2020)
- Critical factors: 
  - Payload mass (optimal range: 4,000-8,000 kg)
  - Launch site (CCAFS SLC-40: 72% success)
  - Orbit type (LEO: 85% success)
- Best model: **Logistic Regression** (92% accuracy)

## License 📄
This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

**Developed as academic work for IBM Data Science Professional Certificate**  
*Note: SpaceX data used for educational purposes only*
