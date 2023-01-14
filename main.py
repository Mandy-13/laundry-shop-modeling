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
        def change_time(hms):    
            #minutes = (hms.hour * 60) + hms.minute + (hms.second / 60)
            minutes = int(hms.strftime("%H%M%S"))
            return minutes

        with st.sidebar:
            #create dataframe
            columns = ['Time(minute)','Temperature(celcius)','Windspeed(km/h)','Humidity(%)','Timespent(minute)','Age Range']
            df = pd.DataFrame(columns = columns)


            time = change_time(st.time_input('Reach Time', dt.time(8, 45), key = "1"))
            windspeed = st.sidebar.slider('Define the windspeed in km/h', 2.49, 13.8, 6.2, key = "2")
            temperature = st.sidebar.slider('Define the temperature in celcius', 23.7, 29.6, 25.5, key = "3")
            humidity = st.sidebar.slider('Define the humidity in percentage', 64, 94, 70, key = "4")
            timespent = st.sidebar.slider('How long the cutomer spent there (in minute)', 11, 60, 32, key = "5")
            ageRange = st.sidebar.slider('How old is the cutomer (years)', 18, 60, 30, key = "6")

            record = {'Time(minute)': time,'Temperature(celcius)': temperature,'Windspeed(km/h)': windspeed,'Humidity(%)': humidity,'Timespent(minute)': timespent,'Age Range': ageRange}
            df = df.append(record, ignore_index=True)
            df = df.rename(index={0: 'Your Input'})

            df_for_display = df.copy().astype(int)
            st.table(df_for_display)

        app = st.selectbox(
            'Navigation Bar',
            self.apps,
            format_func = lambda app: app['title'])

        app['function'](df)





