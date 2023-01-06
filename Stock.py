# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 10:58:18 2023

@author: Afroz

"""
import streamlit as st 
import pandas as pd
import numpy as np 
import yfinance as yf
import plotly.express as px

st.title("Stock Dashboad")
ticker = st.sidebar.text_input("Ticker")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")


data = yf.download(ticker, start=start_date, end=end_date)
fig = px.line(data , x = data.index, y = data['Adj Close'],title = ticker)
st.plotly_chart(fig)

pricing_data, fundamental_data, news = st.tabs(['Pricing Data', "Fundamental Data", "Top 10 News"])

with pricing_data:
    st.header('Pricing Moments')
    data2 = data
    data2['% Change'] = data['Adj Close']/data['Adj Close'].shift(1) - 1
    data2.dropna(inplace = True)
    st.write(data2)
    annual_return = data2['% Change'].mean()*252*100
    st.write("Annual Return is ", annual_return, "%")
    stdev = np.std(data2["% Change"])*np.sqrt(252)
    st.write('Standard Deviation is' , stdev*100,"%")
    st.write("Risk Adj. Return is ", annual_return/(stdev*100))
   
