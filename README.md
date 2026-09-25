# 🛒 SmartCart Customer Segmentation

SmartCart is a small machine learning project I built to understand different types of customers based on their purchasing and engagement behaviour.

I used clustering techniques to group similar customers and then built a simple Streamlit app where you can enter customer details and see which type of customer they are most similar to.

## Live Demo

Try SmartCart: (https://smartcart-vbtz3vkxy9uxdasx2pmgei.streamlit.app/)

## What I did

- Cleaned and prepared the customer data
- Created useful features such as Age, Customer Tenure and Total Spending
- Encoded categorical features
- Scaled the data
- Used PCA to visualise the data
- Compared K-Means and Agglomerative Clustering
- Characterised the resulting customer segments
- Built a Streamlit application for interactive predictions

## Customer Segments

**Lower-Spending, Higher-Visit Customers**  
Customers with relatively lower spending but higher website engagement.

**High-Value Customers**  
Customers with higher income, spending and purchasing activity across different channels.

**Moderate-Spending Customers**  
Customers with moderate purchasing activity and relatively lower campaign response.

## Tech Stack

Python · Pandas · NumPy · Scikit-learn · Matplotlib · Seaborn · Streamlit · Joblib

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
