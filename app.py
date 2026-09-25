import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="SmartCart Customer Segmentation", page_icon="🛒", layout="wide")

m = joblib.load("models/smartcart_model.pkl")
scaler, features, centers, labels = m["scaler"], m["feature_columns"], m["cluster_centers"], m["cluster_labels"]

st.title("🛒 SmartCart Customer Segmentation System")
st.markdown("Enter customer information below to identify the customer segment and view its characteristics.")
st.divider()

st.header("👤 Customer Information")
c1, c2, c3 = st.columns(3)

with c1:
    income = st.number_input("Income", min_value=0, value=50000, step=1000)
    age = st.number_input("Age", min_value=18, max_value=100, value=35)
    recency = st.number_input("Recency", min_value=0, value=20)
    children = st.number_input("Total Children", min_value=0, max_value=10, value=1)
    spending = st.number_input("Total Spending", min_value=0, value=500, step=50)

with c2:
    web_visits = st.number_input("Web Visits / Month", min_value=0, value=5)
    web_purchases = st.number_input("Web Purchases", min_value=0, value=3)
    catalog_purchases = st.number_input("Catalog Purchases", min_value=0, value=2)
    store_purchases = st.number_input("Store Purchases", min_value=0, value=5)
    deals_purchases = st.number_input("Deals Purchases", min_value=0, value=2)

with c3:
    education = st.selectbox("Education", ["Undergraduate", "Graduate", "Postgraduate"])
    living_with = st.selectbox("Living With", ["Alone", "Partner"])
    tenure = st.number_input("Customer Tenure (Days)", min_value=0, value=365)
    complain = st.selectbox("Complaint", ["No", "Yes"])
    response = st.selectbox("Campaign Response", ["No", "Yes"])

st.divider()

segments = {
    0: (
        "Lower-Spending, Higher-Visit Customers",
        ["Lower income and the lowest overall spending",
         "Highest website visits among the segments",
         "Lower web, catalog and store purchase activity",
         "Higher average number of children"],
        "Customers show relatively high website engagement but limited purchasing activity. Targeted promotions and personalised recommendations could potentially improve conversion.",
        ["🏷️ Targeted Promotions", "🎯 Personalised Recommendations", "📈 Conversion Offers"]
    ),
    1: (
        "High-Value Customers",
        ["Highest income and significantly higher overall spending",
         "Highest web, catalog and store purchase activity",
         "Lower website visits compared with other segments",
         "Lower average number of children"],
        "Customers demonstrate strong purchasing value across multiple channels. Loyalty-focused initiatives and personalised recommendations could potentially be considered for this segment.",
        ["🍷 Wine Products", "🥩 Meat Products", "✨ Gold Products"]
    ),
    2: (
        "Moderate-Spending Customers",
        ["Moderate income and spending",
         "Higher store purchase activity than lower-spending customers",
         "Moderate website engagement",
         "Lower campaign response compared with the other segments"],
        "Customers demonstrate moderate purchasing activity but relatively lower response. Targeted engagement strategies could potentially be explored to improve customer response and retention.",
        ["🎯 Targeted Engagement", "🏷️ Promotional Offers", "🔄 Retention Offers"]
    )
}

if st.button("🔍 Analyse Customer", use_container_width=True):

    x = {f: 0 for f in features}
    x.update({
        "Income": income, "Recency": recency,
        "NumDealsPurchases": deals_purchases,
        "NumWebPurchases": web_purchases,
        "NumCatalogPurchases": catalog_purchases,
        "NumStorePurchases": store_purchases,
        "NumWebVisitsMonth": web_visits,
        "Complain": int(complain == "Yes"),
        "Response": int(response == "Yes"),
        "Customer Tenure": tenure, "Age": age,
        "Total_Children": children, "Total_Spending": spending
    })

    for col in [f"Education_{education}", f"Living_With_{living_with}"]:
        if col in x:
            x[col] = 1

    X = scaler.transform(np.array([[x[f] for f in features]]))
    cluster = labels[np.argmin(np.linalg.norm(centers - X, axis=1))]
    name, chars, business, recommendations = segments[cluster]

    st.header("🎯 Customer Segment")
    st.success(f"Customer belongs to **{name}**")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Customer Segment**")
        st.markdown(f"### {name}")
    with c2:
        st.metric("Income", f"{income:,}")
    with c3:
        st.metric("Total Spending", f"{spending:,}")

    st.divider()

    st.subheader("📊 Cluster Characterisation")
    st.markdown("\n".join(f"- {x}" for x in chars))

    st.subheader("💡 Business Interpretation")
    st.info(business)

    st.subheader("🛍️ Potential Recommendations")
    r1, r2, r3 = st.columns(3)
    for col, text in zip((r1, r2, r3), recommendations):
        with col:
            st.info(text)

    st.divider()
    st.caption("Recommendations are based on the characteristics of the identified customer segment.")