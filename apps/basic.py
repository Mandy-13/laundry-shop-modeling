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
    df = pd.read_csv('fullDataset.csv').drop('Unnamed: 0', axis=1)

    # -----------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Exploratory Data Analysis (EDA)</p>', unsafe_allow_html=True)

    st.markdown('##### **Question 1: What are the extra Data Points that I can include?**')
    st.markdown('We extracted an external weather dataset from Open Meteo API. In the API, we used the URL builder to extract 4 variables that we decided that might be impactful, which are the rainfall(mm), temperature(celcius), humidity(%), and wind speed(ms/hour).')

    st.text("")
    st.markdown('##### **Question 2: How to visualise the content?**')

    st.markdown('**1. Bar Chart - Distribution of Age of Customers**')
    st.markdown('From the figure below, we can see that most customers who visit the laundry in the dataset are from 40 to 50  years old.  The second and third most frequent groups are 30 to 40 years old, and 50 to 60 years old. 60 years old and above is the least.')
    open_image('histogram_age.png')

    st.markdown('**2. Stacked Bar Chart - Distribution of Race and Gender of Customers**')
    st.markdown('In general, more males are going to the laundry compared to females except for the Indians and Malays.')
    open_image('stacked_race_gender.png') 

    st.markdown('**3. Line Graph - Count of Customers by Month**')
    st.markdown('This can be explained by the monsoon season in Malaysia of always raining around the end of the year and some maybe cleaning up for the new year. ')
    open_image('line_graph_customer_by_month.png') 
    
    st.markdown('**4. Line Graph - Count of Customers by Time (Hour)**')
    st.markdown('The highest peak hour is at 4am. The second highest peak is after 9pm to 11pm and the third highest peak is around 10a.m. The most deserted time is 6am.')
    open_image('line_graph_customer_by_time.png') 

    st.markdown('**5. Bar Chart - Relationship of bringing kids along and the kids category**')
    st.markdown('This can be explained that a toddler needs high attention to take care of the parents as they just started to walk and it would be dangerous to leave them alone at home.')
    open_image('bar-chart-customer-with-kids.png') 

    st.markdown('**6. Stacked Bar Chart - Relationship between wash item and basket size**')
    st.markdown('The percentage of bringing big basket with clothes has high chance than small basket.')
    open_image('stacked-basket-size-wash-item.png') 

    st.text("")

    # -----------------------------------------------------------------------------------------------
    st.markdown('##### **Question 3: What data transformation to the dataset?**')
    st.markdown('- Removing duplication records, if there is any.')
    st.markdown('- Change features type. Example object to datetime.')
    st.markdown('- Data correction. The records for With_Kids and Kids_Category columns are wrong.')
    st.markdown('- Replace null values using KNN Clustering for imputation. ')


    # -----------------------------------------------------------------------------------------------
    st.markdown('##### **Question 4: Do I need to perform data imbalance treatment?**')
    st.markdown('The **“BuyDrinkLabel”** is used in the classification models. It is an imbalanced class as the data of customers who bought drinks are far greater than customers who did not buy drinks.')
    st.markdown('Solution: ') ###

    st.markdown("**Data Sampling of original BuyDrinkLabel**")
    open_image('bar-chart-bias.png')
    st.warning('0 - Did not buy Drink: 442')
    st.warning('1 - Buy Drink: 2358')

    st.markdown("**Data Sampling of BuyDrinkLabel after resampling**")
    open_image('bar-chart-bias.png') ###
    st.warning('0 - Did not buy Drink: 442') ###
    st.warning('1 - Buy Drink: 2358') ###
    

    # -----------------------------------------------------------------------------------------------
    st.markdown('##### **Question 5: How about outliers and missing values?**')
    st.markdown('Null values are handled by using **KNN Clustering** for imputation for both numerical and categorical values.')
    st.markdown('##### **Before KNN Clustering: Count NULL Value for each column using bar chart** ')
    open_image('ori-dataset-count-null.png')
    st.markdown('##### **After KNN Clustering: Count NULL Value for each column using bar chart** ')
    st.info(df.isnull().sum())

    # -----------------------------------------------------------------------------------------------
    st.markdown('##### **Question 6: Relationships between variables?**')
    st.markdown('**Pairwise Correlation Heatmap** to understand the relationship of the continuous variables in our dataset')
    open_image('pairwise_correlation_heatmap.png')
    st.markdown('A strong negative correlation of -0.75 between temperature (Celcius) and humidity(%), and also -0.64 between wind speed(km/h) and humidity. When the temperature and wind speed increases, humidity decreases as evaporation occurs faster. Furthermore, the correlation between wind speed and temperature is 0.56, a strong positive correlation.')
    st.info(df.isnull().sum())


    # -----------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Association Rule Mining</p>', unsafe_allow_html=True)
    st.markdown('**What features of customer is likely to spend more than RM20 in the laundry (High ROI customer)**')
    st.markdown('#### Solution: Frequent Patterns')
    st.markdown('There are 3 ways to intepret the result.')
    st.markdown('- Support Metric for single feature') #1,2,3,4
    st.markdown('- Top 5 Association Rule') #support, lift, confident 

    df = pd.read_csv('association.csv').drop('Unnamed: 0', axis=1)
    st.write(df.head())

    st.markdown('By ranking from the confidence level (from highest to lower)')
    st.markdown('- Casual attire, no spectacles -> buy drinks')
    st.markdown('- Big basket, no spectacles, clothes item -> buy drinks')
    st.markdown('- Casual attire, big basket -> buy drinks')
    st.markdown('- No spectacles, female -> buy drinks')
    st.markdown('- 31-50 age, no spectacles -> buy drinks')

    st.text("")

    # -----------------------------------------------------------------------------------------------

    return 'basic'
    