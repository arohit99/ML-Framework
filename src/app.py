import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


plt.style.use('fivethirtyeight')

st.title('ML Framework')

input_file_path = './data/raw_data/CustomerChurn.csv'

df = pd.read_csv(input_file_path)


st.subheader('raw data')

st.dataframe(df)

st.markdown('Execution complete')

