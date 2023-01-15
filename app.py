import streamlit as st
from main import MainPage
from apps import basic, model1

st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 300px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 300px;
        margin-left: -300px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

app = MainPage()

st.write("""# Laundry Shop Modeling """)
st.write("""**Classification**: K-Nearest Neighbour (KNN), Random Forest""")
st.write("""**Ensemble**: Stacking all classification models""")
st.write("""**Clustering**: K-Means Clustering""")
st.write("""**Regression**: Support Vector Regression, Linear Regression""")
st.write("""**Deep Learning**: Neural Network""")



# Add all your application here
if st.button('Test Model'):
    app.add_app("Prediction Models", model1.run)

app.add_app("Exploratory Data Analysis (EDA)", basic.run)
app.run()






