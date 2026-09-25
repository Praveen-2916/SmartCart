# 🛒 SmartCart Customer Segmentation

SmartCart is a customer segmentation system that uses unsupervised machine learning to group customers based on their demographic, purchasing, and engagement behaviour.

## 📌 Project Overview

The project includes:

- Data cleaning and preprocessing
- Feature engineering
- Categorical feature encoding
- Feature scaling
- PCA for dimensionality reduction and visualization
- K-Means clustering
- Agglomerative Hierarchical Clustering
- Cluster evaluation using WCSS and Silhouette Score
- Customer cluster characterization
- Business interpretation of customer segments
- Streamlit web application for customer segmentation

## 🎯 Customer Segments

### Lower-Spending, Higher-Visit Customers
Customers with relatively lower spending but higher website engagement.

### High-Value Customers
Customers with higher income, spending, and purchasing activity across multiple channels.

### Moderate-Spending Customers
Customers with moderate purchasing activity and relatively lower campaign response.

## 🖥️ Streamlit Application

The Streamlit application allows users to enter customer information and identify the corresponding customer segment along with its characteristics and potential recommendations.

## 🛠️ Packages Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Kneed
- Joblib
- Streamlit

## 📁 Project Structure

```text
SmartCart/
├── app.py
├── SmartCart_Final.ipynb
├── smartcart_customers.csv
├── requirements.txt
├── README.md
├── .gitignore
└── models/
    └── smartcart_model.pkl
