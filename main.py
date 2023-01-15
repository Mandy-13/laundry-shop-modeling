import streamlit as st
import pandas as pd
import datetime as dt

class MainPage:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        def catToNum(df, num):
            temp_dict_Race = {'malay': 0, 'chinese': 1, 'indian': 2, 'foreigner': 3} 
            temp_dict_Body_Size = {'thin': 0, 'moderate': 1, 'fat': 2} 
            temp_dict_Kids_Category = {'No kid': 0, 'Baby': 1, 'Toddler': 2, 'Young': 3} 
            temp_dict_Basket_colour = {'red': 0, 'blue': 1, 'black': 2, 'pink': 3, 'purple': 4, 'yellow': 5, 'white': 6, 'orange': 7, 'brown': 8, 'green': 9, 'grey': 10} 
            temp_dict_Shirt_Colour = {'red': 0, 'blue': 1, 'black': 2, 'pink': 3, 'purple': 4, 'yellow': 5, 'white': 6, 'orange': 7, 'brown': 8, 'green': 9, 'grey': 10}  
            temp_dict_Pants_Colour = {'red': 0, 'blue': 1,  'black': 2, 'pink': 3, 'purple': 4, 'yellow': 5, 'white': 6, 'orange': 7, 'brown': 8, 'green': 9, 'grey':10, 'blue_jeans':11} 
            temp_dict_Day = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thrusday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7} 

            if num == 1:
                df['Race']= df.Race.map(temp_dict_Race)  
                df['Body_Size']= df.Body_Size.map(temp_dict_Body_Size)  
                df['Basket_colour']= df.Basket_colour.map(temp_dict_Basket_colour)  
                df['Shirt_Colour']= df.Shirt_Colour.map(temp_dict_Shirt_Colour)  
                df['Pants_Colour']= df.Pants_Colour.map(temp_dict_Pants_Colour)  
                df['Day']= df.Day.map(temp_dict_Day)  
                 
            else:
                df['Basket_colour']= df.Basket_colour.map(temp_dict_Basket_colour)  
                df['Kids_Category']= df.Kids_Category.map(temp_dict_Kids_Category)  
                df['Pants_Colour']= df.Pants_Colour.map(temp_dict_Pants_Colour)
                df['Shirt_Colour']= df.Shirt_Colour.map(temp_dict_Shirt_Colour)  
                df['Day']= df.Day.map(temp_dict_Day)   
                df['Race']= df.Race.map(temp_dict_Race) 

            return df

        with st.sidebar:
            st.markdown('### **Settings**')
            #create dataframe
            columns_cla = ['TimeSpent_minutes', 'Age_Range', 'humidity(%)', 'Hour', 'TotalSpent_RM',
                        'Basket_colour', 'Pants_Colour', 'windspeed(km/h)', 'Shirt_Colour', 'Day', 'temperature(Celcius)',
                        'Body_Size','Dryer_No','Washer_No', 'Race']
            df_cla = pd.DataFrame(columns = columns_cla)

            columns_reg = ['Hour','Age_Range', 'TimeSpent_minutes', 'humidity(%)', 'Basket_colour',
                            'Pants_Colour', 'Shirt_Colour', 'buyDrinks','windspeed(km/h)', 'Day', 
                            'temperature(Celcius)', 'Race', 'Washer_No', 'Num_of_Baskets', 'Kids_Category']
            df_reg = pd.DataFrame(columns = columns_reg)


            hour = st.sidebar.slider('What time the customer reached (hours)', 0, 23, 4, key = "1")
            timespent = st.sidebar.slider('How long the cutomer spent there (in minute)?', 11, 60, 32, key = "2")
            age_range = st.sidebar.slider('How old is the cutomer (years)?', 18, 60, 30, key = "3")
            humidity = st.sidebar.slider('Define the humidity in percentage.', 64, 94, 70, key = "4")
            total_spent = st.sidebar.slider('How much does the customer spent?', 7.0, 21.0, 14., key = "5")
            basket_colour = st.selectbox('Which colour of basket the customer chooose?', ('red', 'blue', 'black', 'pink', 'purple', 'yellow', 'white', 'orange', 'brown', 'green', 'grey'), key = "6")
            pants_colour = st.selectbox('What is the colour of pants the customer wore?', ('red', 'blue', 'black', 'pink', 'purple', 'yellow', 'white', 'orange', 'brown', 'green', 'grey', 'blue_jeans'), key = "7")
            windspeed = st.sidebar.slider('Define the windspeed in km/h.', 2.49, 13.8, 6.2, key = "8")
            shirt_colour = st.selectbox('What is the colour of pants the customer wore?', ('red', 'blue', 'black', 'pink', 'purple', 'yellow', 'white', 'orange', 'brown', 'green', 'grey'), key = "9")
            day = st.selectbox('What day is it?', ('Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday'), key = "10")
            temperature = st.sidebar.slider('Define the temperature in celcius', 23.7, 29.6, 25.5, key = "11")
            body_size = st.radio("Customer's body size", ('thin', "moderate", 'fat'), key = "12")
            dryer_number = st.radio("What number of dryer the customer choose?", ('7', "8", '9', '10'), key = "13")
            washer_number = st.radio("What number of washer the customer choose?", ('3', "4", '5', '6'), key = "14")
            race = st.radio("What race is the customer?", ('malay', "chinese", 'indian', 'foreigner'), key = "15")
            buy_drink = st.radio('Did the customer brought any drink, how many did he/she brought?', ('0','1','2','3','4','5'), key = "16")
            number_of_basket = st.radio("How many basket the customer use?", ('1', "2", '3'), key = "17")
            kid_category = st.selectbox("What is the categorise of customer kids", ('No kid', "Baby", 'Toddler', 'Young'), key = "18")

            record_cla = {'TimeSpent_minutes': timespent, 'Age_Range': age_range, 'humidity(%)': humidity, 'Hour': hour, 
                        'TotalSpent_RM': total_spent,'Basket_colour': basket_colour, 'Pants_Colour': pants_colour, 'windspeed(km/h)': windspeed, 
                        'Shirt_Colour': shirt_colour, 'Day': day, 'temperature(Celcius)': temperature,
                        'Body_Size': body_size,'Dryer_No': dryer_number,'Washer_No': washer_number, 'Race': race}
            df_cla = df_cla.append(record_cla, ignore_index=True)
            df_cla = df_cla.rename(index={0: 'Your Input'})
            df_cla = catToNum(df_cla, 1)

            record_reg = {'Hour': hour,'Age_Range': age_range, 'TimeSpent_minutes': timespent, 'humidity(%)': humidity, 'Basket_colour': basket_colour,
                            'Pants_Colour': pants_colour, 'Shirt_Colour': shirt_colour, 'buyDrinks': buy_drink,'windspeed(km/h)': windspeed, 'Day': day, 
                            'temperature(Celcius)': temperature, 'Race': race, 'Washer_No': washer_number, 'Num_of_Baskets': number_of_basket, 'Kids_Category': kid_category}
            df_reg = df_reg.append(record_reg, ignore_index=True)
            df_reg = df_reg.rename(index={0: 'Your Input'})
            df_reg = catToNum(df_reg, 2)

            #df_for_display = df.copy().astype(int)
            #st.table(df_for_display)

        app = st.selectbox(
            'Navigation Bar',
            self.apps,
            format_func = lambda app: app['title'])

        st.write('**For Classification Prediction**')
        st.write(df_cla.head())
        st.write('**For Regression Prediction**')
        st.write(df_reg.head())

        app['function'](df_cla, df_reg)





