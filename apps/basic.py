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

def run(df):
    # -----------------------------------------------------------------------------------------------
    # Load Dataset
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Basic processing</p>', unsafe_allow_html=True)
    st.markdown('### Load the Pre-processed Dataset')
    df = pd.read_csv('fullDataset.csv').drop('Unnamed: 0', axis=1)
    st.write(df.head())
    st.text("")
    st.markdown('**This dataset is the preprocessed datasset of the combination of the original dataset, city column, raining status, temperature, humidity and windspeed**')
    st.markdown('**The pre-processes have been handled in Jupyter Notebook. The processes have include:**')
    st.markdown('- Removing duplication records, if there is any.')
    st.markdown('- Change features type. Example object to datetime.')
    st.markdown('- Data correction. The records for With_Kids and Kids_Category columns are wrong.')
    st.markdown('- Replace null values using KNN Clustering for imputation. ')
    st.text("")
    st.text("")
    st.text("")
    st.markdown('##### **Before KNN Clustering: Count NULL Value for each column using bar chart** ')
    open_image('ori-dataset-count-null.png')

    st.text("")
    st.text("")
    st.markdown('##### **After KNN Clustering: Count NULL Value for each column using bar chart** ')
    # Check dataset
    st.markdown('### Check dataset')
    st.markdown('##### Shape of dataset')
    st.info(df.shape)
    st.markdown('##### Check null values')
    st.info(df.isnull().sum())

    st.text("")

    # -----------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Exploratory Data Analysis (EDA)</p>', unsafe_allow_html=True)

    st.markdown('##### **Question 1: What are the extra Data Points that I can include?**')
    st.markdown('We extracted an external weather dataset from Open Meteo API. In the API, we used the URL builder to extract 4 variables that we decided that might be impactful, which are the rainfall(mm), temperature(celcius), humidity(%), and wind speed(ms/hour).')

    st.text("")
    st.markdown('##### **Question 2: How to visualise the content?**')
    st.markdown('**1. Binned the ages and visualised the count of each bin using a histogram**')
    open_image('histogram_age.png')
    st.markdown('**2. Stacked barchart to visualise the distribution of Race and Gender of customers who visit the laundry**')
    open_image('stacked_race_gender.png')
    st.markdown('**3. Line graph to visualise the count of customers by each day from October 2015 to March 2016 (the time range of the dataset)**')
    open_image('line_graph_customer_each_day.png')
    st.markdown('**4. Line graph to visualise the count of customers by the time of their visit from January 2015 till December 2016**')
    open_image('line_graph_customer_by_time.png')
    st.markdown('**5. Pairwise Correlation Heatmap to understand the relationship of the continuous variables in our dataset**')
    open_image('pairwise_correlation_heatmap.png')
    st.markdown('**6. Dython Correlation Heatmap to find correlation between categorical-continuous variables using Correlation Ratio**')
    open_image('dython_correlation.png')
    st.markdown('**7. Comparative bar chart to visualise the relationship between customers with kids or no versus the number of baskets the customers bring along to store their laundry.**')
    open_image('comparative-bar-chart-basket-kids.png')
    st.markdown('**8.  Bar chart to visualise the relationship between customers with kids and the category of the kids in the dataset.**')
    open_image('bar-chart-customer-with-kids.png')
    st.markdown('**9. Crosstab to visualise the shirt colours of the customers and the usage of the different washers in the laundry.**')
    open_image('cosstab-shirt-solour-washer-number.png')
    st.markdown('**10. Stacked bar chart to visualise the relationship between the basket size and the wash_items.**')
    open_image('stacked-basket-size-wash-item.png')
    st.markdown('**11. Comparative boxplot to analyse if there is any significant relationship between the number of baskets a customer brings and the time spent by the customer in the laundry.**')
    open_image('comparative-num-basket-time-spent.png')

    st.text("")

    # -----------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Association Rule Mining </p>', unsafe_allow_html=True)
    st.markdown('#### Solution: Frequent Patterns')
    st.markdown('The reason choosing fp over apriori is because fp result will show in descending order')

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
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Feature Selection Methods Comparison</p>', unsafe_allow_html=True)
    st.markdown('#### Solution: **Boruta** and **Recursive Feature Elimination (RFE)**')

    st.text("")
    st.markdown("**Boruta Top 10 Features**")
    open_image('boruta-top-10.png')
    st.text("")
    st.markdown("**RFE Top 10 Features**")
    open_image('rfe-top-10.png')
    
    st.markdown('##### Conclusion: **Boruta** is selected as the result seems more reliable. From the graph below, the final decision on number of features is chosen as 6.')
    open_image('accuracy-trend-for-different-classifiers.png')

    st.text("")

    # -----------------------------------------------------------------------------------------------
    st.markdown(f'<p style="color:Purple;font-size: 30px;font-weight: bold;">Data Resampling Target</p>', unsafe_allow_html=True)
    st.markdown('#### Solution: SMOTE')

    st.text("")
    st.markdown("**Data Sampling of original BuyDrinkLabel**")
    open_image('bar-chart-bias.png')
    st.warning('0 - Did not buy Drink: 442')
    st.warning('1 - Buy Drink: 2358')

    st.text("")
    st.markdown("**Data Sampling after Applying SMOTE**")
    open_image('bar-chart-smote-bias.png')
    st.success('0 - Did not buy Drink: 2358')
    st.success('1 - Buy Drink: 2358')

    st.text("")


    return 'basic'



"""     # Data pre-processing

    # Turn string values to categorical code values
    for column, content in df.items():
        if pd.api.types.is_string_dtype(content):
            df[column] = content.astype("category").cat.as_ordered()
            df[column] = pd.Categorical(content).codes

    st.markdown('##### Turn string values to categorical code values')
    st.write(df.dtypes.astype(str))

    # Resample - oversample

    # create two different dataframe of majority and minority class
    df_majority = df[(df['Decision'] == 0)]
    df_minority = df[(df['Decision'] == 1)]

    # oversampled minority class
    df_minority_oversampled = resample(df_minority,
                                       replace=True,  # sample with replacement
                                       n_samples=1769,  # to match majority class
                                       random_state=42)  # reproducible results

    # Combine majority class with oversampled minority class
    df_oversampled = pd.concat([df_minority_oversampled, df_majority])

    st.markdown('##### Oversampled minority class then combine with majority class')
    st.markdown('Value count after resampling')
    st.write(df_oversampled["Decision"].value_counts())
    st.markdown('Shape after resampling')
    st.info(df_oversampled.shape)

    # shuffle dataframe
    df_oversampled = df_oversampled.sample(frac=1)
    st.markdown('Dataframe after resampling')
    st.write(df_oversampled)

    # Split data to X and y, x for training features and y is target variable
    X = df_oversampled.drop("Decision", axis=1)
    y = df_oversampled["Decision"]

    bestFeatures = SelectKBest(score_func=chi2, k=10)  # take 10 best features using chi-square
    fit = bestFeatures.fit(X, y)
    dfScores = pd.DataFrame(fit.scores_)
    dfColumns = pd.DataFrame(X.columns)

    # concat two dataframes for better visualization
    featureScores = pd.concat([dfColumns, dfScores], axis=1)
    featureScores.columns = ['Feature', 'Score']  # naming the dataframe columns
    selection = featureScores.nlargest(10, 'Score')  # print 10 best features

    col = selection.Feature.unique()
    df_afterSelection = df_oversampled.filter([x for x in col])
    df_afterSelection['Decision'] = df_oversampled['Decision']

    st.markdown('##### Feature selection using chi2 (choose 10 best features)')
    st.markdown('Shape after selection')
    st.info(df_afterSelection.shape)
    st.markdown('Feature scores')
    st.write(selection)
    st.markdown('Dataframe after selection')
    st.write(df_afterSelection)

    # success
    st.success("All done, now go to next page -->")

    # Decision vs others
    st.markdown('##### Check correlation of decision vs other variables using Spearman’s correlation coefficient')
    for col in df:
        coef, p = spearmanr(df['Decision'], df[col])
        st.write(f'<p class="padding">{col:>40}: {coef:.4f}</p>', unsafe_allow_html=True)

    # Compare Accept and Reject
    st.markdown('##### Let\'s compare the number of Accept and Reject')

    st.write(df["Decision"].value_counts())

    # plot
    fig2 = plt.figure(figsize=(10, 4))
    df['Decision'].value_counts().plot(kind='bar', title='Accept vs Reject', color=["salmon","lightblue"])
    st.pyplot(fig2) """

    
