import streamlit as st

# Title of the dashboard
st.title("Observatoire de l'IA dans les Mairies")

# Sidebar for user input
st.sidebar.header("User Input")

# Input fields
city = st.sidebar.text_input("Nom de la Mairie")

# Sample Data (This would be replaced with actual data fetched from an API or database)
data = {
    "Mairie A": "Data about Mairie A",
    "Mairie B": "Data about Mairie B",
}

# Display data on selected city
if city in data:
    st.write(data[city])
else:
    st.write("Aucune donnée disponible pour cette mairie.")

# Bar chart example (placeholder)
import pandas as pd
import numpy as np

# Sample DataFrame
df = pd.DataFrame({
    'Mairie': ['Mairie A', 'Mairie B'],
    'Valeur': [10, 20]
})

st.bar_chart(df.set_index('Mairie'))