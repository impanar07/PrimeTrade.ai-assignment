import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os

st.write(os.getcwd())

st.title("Trader Sentiment Analysis Dashboard")

merged = pd.read_csv("merged_dataset.csv")

st.header("Dataset")

st.write(merged.head())

st.header("Market Sentiment")

st.bar_chart(
merged.groupby('classification')['Closed PnL'].mean()
)

st.header("Trade Frequency")

st.line_chart(
merged.groupby('date').size()
)

st.header("Long vs Short")

st.bar_chart(
merged['Side'].value_counts()
)

st.header("Leverage Distribution")

fig,ax = plt.subplots()

ax.hist(
merged['Leverage'],
bins=30
)

st.pyplot(fig)