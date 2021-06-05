#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#import dataset
df = pd.read_csv('C:\DAY4\a4/whr.csv')
#First thirty rows
whr = df.head(10)
#Display the table
st.table(whr)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
whr.plot(kind='bar')
st.pyplot()
#joinplot
st.subheader("JointPlot")
sns.jointplot(x='Country name',y='Healthy life expectancy',data=whr,kind='scatter')
st.pyplot()
#Displot
st.subheader("Displot")
sns.displot(whr ['Country name'])
st.pyplot()
#Rugplot
st.subheader("Rugplot")
sns.rugplot(whr['Social support'])
st.pyplot()
#Correation
st.subheader("Heatmap")
sns.heatmap(whr.corr(),cmap='coolwarm',annot=True)
st.pyplot()
#pairplot
st.subheader("Pairplot")
sns.pairplot(whr,hue='Regional indicator',palette='rainbow')
st.pyplot()

