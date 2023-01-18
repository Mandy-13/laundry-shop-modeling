import streamlit as st
from PIL import Image
import pandas as pd
import warnings

warnings.filterwarnings("ignore")


# -----------------------------------------------------------------------------------------------

st.markdown("""
<style>
.padding {
    line-height: 5px;
}
</style>
""", unsafe_allow_html=True)


def open_image(imageName):
    image = Image.open("images/"+imageName)
    st.image(image, use_column_width=True, clamp=255)


# -----------------------------------------------------------------------------------------------

def run(x, y):
    
    st.text("")
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Association Rule Mining</p>', unsafe_allow_html=True)
    st.markdown('**What features of customer is likely to spend more than RM20 in the laundry (High ROI customer)**')
    st.markdown('#### Solution: Frequent Patterns')

    st.text("")
    st.markdown('There are 2 ways to intepret the result.')
    st.markdown('- Support Metric for single item') 
    st.markdown('- Top 5 Association Rule') 

    st.text("")
    st.markdown('##### **Choose your item to view the support metric** ')
    col1, col2, col3, col4 = st.columns([1,1,1,1])
    df = pd.read_csv('supportItemset1.csv').drop('Unnamed: 0', axis=1)
    with col1:
        if st.button('Feature 1'):
            df = pd.read_csv('supportItemset1.csv').drop('Unnamed: 0', axis=1)
    with col2:
        if st.button('Feature 2'):
            df = pd.read_csv('supportItemset2.csv').drop('Unnamed: 0', axis=1)
    with col3:
        if st.button('Feature 3'):
            df = pd.read_csv('supportItemset3.csv').drop('Unnamed: 0', axis=1)
    with col4:
        if st.button('Feature 4'):
            df = pd.read_csv('supportItemset4.csv').drop('Unnamed: 0', axis=1)
    st.write(df.head())

    st.text("")
    st.markdown('##### **Choose a feature to view the Top 5 Association Rule** ')
    col5, col6, col7 = st.columns([1,1,1])
    df2 = pd.read_csv('associationSupport.csv').drop('Unnamed: 0', axis=1)
    with col5:
        if st.button('Support'):
            df2 = pd.read_csv('associationSupport.csv').drop('Unnamed: 0', axis=1)
    with col6:
        if st.button('Confidence'):
            df2 = pd.read_csv('associationConfidence.csv').drop('Unnamed: 0', axis=1)
    with col7:
        if st.button('Lift'):
            df2 = pd.read_csv('associationLift.csv').drop('Unnamed: 0', axis=1)
    st.write(df2.head())

    st.text("")
    st.markdown('#### **Conclusion**')
    st.markdown('**By ranking from the confidence level (from highest to lower)**')
    st.markdown('- Casual attire, no spectacles -> buy drinks')
    st.markdown('- Big basket, no spectacles, clothes item -> buy drinks')
    st.markdown('- Casual attire, big basket -> buy drinks')
    st.markdown('- No spectacles, female -> buy drinks')
    st.markdown('- 31-50 age, no spectacles -> buy drinks')

    st.text("")

    # -----------------------------------------------------------------------------------------------

    return 'association'
    
