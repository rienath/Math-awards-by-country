# TODO number story 1
# TODO number story 2
# TODO number story 3
# TODO number story 4
# TODO number story 5
# TODO number story 6
# TODO number story 7
# TODO layout


#import dash
import pandas as pd
#from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import streamlit as st

#app = dash.Dash(__name__)

# ================
# ===== JUNK =====
# ================
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})


# ==================
# COLOURS AND STYLES
# ==================

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}


# =====================
# ===== LOAD DATA =====
# =====================

# Define data file locations
data_folder = '../data/'

location_top_universities = data_folder + 'top-universities.csv'
location_cumulative_winners = data_folder + 'cumulative-winners.csv'
location_winners_per_capita = data_folder + 'winners-per-capita.csv'
location_overview = data_folder + 'overview.csv'

df_top_universities = pd.read_csv(location_top_universities)
df_cumulative_winners =  pd.read_csv(location_cumulative_winners)
df_winners_per_capita  = pd.read_csv(location_winners_per_capita)
df_overview = pd.read_csv(location_overview)

# =================
# ===== PLOTS =====
# =================
def local_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

local_css("style.css")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.header("A cat")
    st.write('AFDSF')
    st.write('dsfgdf')
    st.image("https://static.streamlit.io/examples/cat.jpg")
    st.write('')

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with col4:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
