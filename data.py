import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Crop Production Analysis")
file = st.file_uploader("Upload your Dataset in CSV")
if file is not None:
    df = pd.read_csv(file)
    total_production = df['Production'].sum()/1e9
    st.metric("Total Production",f"{total_production:.2f}","Billions")
    topstate = df.groupby('State_Name')['Production'].sum().sort_values(ascending=False).head(5)
    st.bar_chart(topstate,sort=False)
    fig, ax = plt.subplots()
    df.groupby('State_Name')['Production'].sum().head(10).plot(kind='pie', ax=ax, autopct='%1.1f%%')
    ax.set_ylabel('')
    st.pyplot(fig)
    st.dataframe(df)