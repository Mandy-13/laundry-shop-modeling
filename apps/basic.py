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
    # -----------------------------------------------------------------------------------------------
    # Load Dataset
    df0 = pd.read_csv('fullDataset.csv').drop('Unnamed: 0', axis=1)

    # -----------------------------------------------------------------------------------------------
    st.text("")
    st.text("")
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Exploratory Data Analysis (EDA)</p>', unsafe_allow_html=True)

    st.text("")
    st.markdown(f'<p style="color:Blue;font-size: 24px;font-weight: bold;">Question 1</p>', unsafe_allow_html=True)
    st.markdown('###### **What are the extra Data Points that I can include?**')
    st.markdown('We extracted an external weather dataset from Open Meteo API. In the API, we used the URL builder to extract 4 variables that we decided that might be impactful, which are the rainfall(mm), temperature(celcius), humidity(%), and wind speed(ms/hour).')

    # -----------------------------------------------------------------------------------------------
    st.text("")
    st.markdown(f'<p style="color:Blue;font-size: 24px;font-weight: bold;">Question 2 & 6</p>', unsafe_allow_html=True)
    st.markdown('###### **How to visualise the content abd what is the relationship between variables?**')


    st.text("")
    st.text("")
    st.markdown('##### **---Customer Segmentation---**')


    st.text("")
    st.markdown('**1. Bar Chart - Distribution of Age of Customers**')
    st.markdown('From the figure below, we can see that most customers who visit the laundry in the dataset are from 40 to 50  years old.  The second and third most frequent groups are 30 to 40 years old, and 50 to 60 years old. 60 years old and above is the least.')
    open_image('histogram_age.png')

    st.text("")
    st.markdown('**2. Stacked Bar Chart - Distribution of Race and Gender of Customers**')
    st.markdown('In general, more males are going to the laundry compared to females except for the Indians and Malays.')
    open_image('stacked_race_gender.png') 

    st.text("")
    st.markdown('**3. Bar Chart - Relationship of bringing kids along and the kids category**')
    st.markdown('This can be explained that a toddler needs high attention to take care of the parents as they just started to walk and it would be dangerous to leave them alone at home.')
    open_image('bar-chart-customer-with-kids.png') 


    # -----------------------------------------------------------------------------------------------
    st.text("")
    st.text("")
    st.markdown('##### **---Time Series Trend of the Laundry Shop---**')

    st.text("")
    st.markdown('**1. Time Sries Plot - Month on Month Trend of Count of Customers and Revenue (RM)**')
    st.markdown('This can be explained by the monsoon season in Malaysia of always raining around the end of the year and some maybe cleaning up for the new year. Therefore, the company may grab this opportunity to organise sales and promotions to attract more customers to visit the shop. ')
    open_image('month-trend-custumer-count-revenue.png') 

    st.text("")
    st.markdown('**2. Line Graph - Count of Customers by Time (Hour)**')
    st.markdown('The highest peak hour is at 4am. The second highest peak is after 9pm to 11pm and the third highest peak is around 10a.m. The most deserted time is 6am.')
    open_image('line_graph_customer_by_time.png') 

    # -----------------------------------------------------------------------------------------------
    st.text("")
    st.text("")
    st.markdown('##### **---Relation Between Features---**')

    st.text("")
    st.markdown('**1. Pairwise Correlation Heatmap to understand the relationship of the continuous variables in our dataset**')
    st.markdown('A strong negative correlation of -0.75 between temperature (Celcius) and humidity(%), and also -0.64 between wind speed(km/h) and humidity. When the temperature and wind speed increases, humidity decreases as evaporation occurs faster. Furthermore, the correlation between wind speed and temperature is 0.56, a strong positive correlation.')
    open_image('pairwise_correlation_heatmap.png')

    st.text("")
    st.markdown('**2. Stacked Bar Chart - Relationship between wash item and basket size**')
    st.markdown('The percentage of bringing big basket with clothes has high chance than small basket.')
    open_image('stacked-basket-size-wash-item.png') 


    # -----------------------------------------------------------------------------------------------
    st.text("")
    st.markdown(f'<p style="color:Blue;font-size: 24px;font-weight: bold;">Question 3</p>', unsafe_allow_html=True)
    st.markdown('###### **What data transformation to the dataset?**')
    st.markdown('- Removing duplication records, if there is any.')
    st.markdown('- Change features type. Example object to datetime.')
    st.markdown('- Data correction. The records for With_Kids and Kids_Category columns are wrong.')
    st.markdown('- Replace null values using KNN Clustering for imputation. ')

    
    # -----------------------------------------------------------------------------------------------
    st.text("")
    st.markdown(f'<p style="color:Blue;font-size: 24px;font-weight: bold;">Question 4</p>', unsafe_allow_html=True)
    st.markdown('###### **Do I need to perform data imbalance treatment?**')
    st.markdown('The **???BuyDrinkLabel???** is used in the classification models. It is an imbalanced class as the data of customers who bought drinks are far greater than customers who did not buy drinks.')
    st.markdown('######**Solution: SMOTE Oversampling**')

    st.text("")
    st.markdown("**Data Sampling of original BuyDrinkLabel**")
    open_image('bar-chart-bias.png')
    st.warning('0 - Did not buy Drink: 442')
    st.warning('1 - Buy Drink: 2358')

    st.text("")
    st.markdown("**Data Sampling of BuyDrinkLabel after resampling**")
    open_image('bar-chart-smote-bias.png') 
    st.warning('0 - Did not buy Drink: 2358') 
    st.warning('1 - Buy Drink: 2358')
    
    
    # -----------------------------------------------------------------------------------------------
    st.text("")
    st.markdown(f'<p style="color:Blue;font-size: 24px;font-weight: bold;">Question 5</p>', unsafe_allow_html=True)
    st.markdown('###### **How about outliers and missing values?**')
    st.markdown('Null values are handled by using **KNN Clustering** for imputation for both numerical and categorical values.')

    st.text("")
    st.markdown('###### **Before KNN Clustering: Count NULL Value for each column using bar chart** ')
    open_image('ori-dataset-count-null.png')

    st.text("")
    st.markdown('###### **After KNN Clustering: Count NULL Value for each column using bar chart** ')
    st.info(df0.isnull().sum())


    # -----------------------------------------------------------------------------------------------

    return 'basic'
    