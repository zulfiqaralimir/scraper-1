import streamlit as st
import pandas as pd
# URL of the webpage with the table
url = 'https://www.psx.com.pk/market-summary/'
tables = pd.read_html(url)
df=len(tables)
st.title("CEMENT Sector Market Summary")
import plotly.express as px

# Example Plotly chart
fig = px.bar(tables[5], x='CEMENT', y='CEMENT.7', title='Table Data Volume')
st.plotly_chart(fig)
st.write("Number of Tables:")
st.write(df)
st.write(tables[5])





#Web Scraping with Pandas | Scraping Tables in 2 minutes!
#https://www.youtube.com/watch?v=q0EgxM2iAII
