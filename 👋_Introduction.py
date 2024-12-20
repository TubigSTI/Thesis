import streamlit as st

# # Set up the page
# st.set_page_config(
#     page_title="Preditive Analytics for Small to Medium Business",
#     page_icon="📊",
# )

# # Main title
# st.write("# Predictive Analytics for Determining Optimal Business Location for Small to Medium Enterprise📊")

# # Brief introduction
# # Brief introduction
# st.markdown(
#  """
#     Welcome to the **Business Viability Analysis Tool**, developed as part of our undergraduate thesis to assess 
#     and predict the optimal locations for establishing Small to Medium Enterprises (SMEs) in the Philippines.

#     This tool combines **population demographics**, **Family Income and Expenditure Survey (FIES)** data analytics, 
#     and advanced machine learning techniques to support entrepreneurs and policymakers in making informed decisions. 
#     By leveraging these insights, we aim to predict business viability and identify high-potential regions.

#     ### Project Highlights:
#     - **Population Data Analytics:** 
#         - Analyze regional population density, growth rates, and demographic trends.
#         - Understand how demographics influence market demand and regional opportunities.
#     - **FIES Data Analytics:**
#         - Examine household income, spending behaviors, and economic capacity across regions.
#         - Provide insights into the purchasing power and needs of different communities.
#     - **Clustering Algorithm with FA and PCA:** 
#         - **Factor Analysis (FA):** Identifies underlying socio-economic dimensions such as household size, income, and basic needs.
#         - **PCA (Principal Component Analysis):** Reduces data complexity to focus on critical features affecting business viability.
#         - Clustering groups regions into profiles (e.g., High Potential, Moderate Potential, and Low Potential) based on these factors.
#     - **Business Score Prediction:**
#         - Predict the viability score of specific business types (e.g., retail, food services, or logistics) for a given region.
#         - Leverages FIES data, including income, expenditures, and socio-economic indicators, to estimate the business potential of an area.
#         - Outputs actionable business scores that help identify the best locations for different types of enterprises.
#     - **Actionable Insights:** 
#         - Deliver region-specific recommendations based on market conditions, household capacity, and cluster profiles.

#     ### Objective:
#     The goal of this research is to create a **data-driven framework** that predicts the viability of specific business types 
#     and identifies high-potential regions for SMEs. By combining population analytics, FIES data, clustering techniques, and machine learning, 
#     this tool offers valuable insights for entrepreneurs and policymakers.

#     ### Learn More:
#     - [Thesis Documentation](#)
#     - [Research Approach](#)

#     **👈 Use the sidebar** to navigate between sections and explore the data, methodologies, and results.
#     """
# )
# st.sidebar.success("Select a section to begin exploring.")


import streamlit as st

# Set up the page
st.set_page_config(
    page_title="Predictive Analytics for Small to Medium Business",
    page_icon="📊",
)

logo_url = "logo/SPARK.png"
logo_banner = "logo/logo_banner.png"
# Banner
st.image(logo_banner)
# SPARK
st.write("# SPARK: System Predicting Regional Areas of Key Business")

# Brief introduction
st.markdown(
    """
    Welcome to **SPARK**, your guide to finding the best places to start and grow small businesses in the Philippines.  

    This tool focuses on analyzing household income and spending habits to guide entrepreneurs and policymakers in making smarter decisions. 
    By understanding economic capacity and consumer behavior, it highlights the best locations for businesses like stores, restaurants, or logistics hubs. 

    This tool leverages powerful data analytics to provide actionable insights, helping entrepreneurs and policymakers make smarter, data-driven decisions.  

    ### **How It Works:**
    - **Socioeconomic Segmentation Analytics:**  
    Explore how regions are grouped based on shared economic factors like income and spending habits to understand potential business opportunities.
    - **Business Score Prediction Analytics:**  
    Predict viability scores for different business types, helping you choose the best location based on profitability and demand.
    - **FIES Data Analytics:**  
     Delve into detailed analyses of household income and expenditures to understand economic conditions and consumer behavior.
    - **Population Data Analytics:** *(Supporting Feature)*  
    Gain additional insights into population density and growth trends as supplementary data for decision-making.

    ### **Why Use This Tool?**
    If you're planning to start a business or develop regional policies, this tool offers insights that make decision-making easier and more effective.

    **👈 Use the sidebar** to navigate between sections and explore the data, methodologies, and results.
    """
)

st.sidebar.success("Select a section to begin exploring.")
