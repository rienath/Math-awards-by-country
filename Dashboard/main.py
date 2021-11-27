# TODO number story 2
# TODO number story 3
# TODO number story 4
# TODO number story 5
# TODO number story 6
# TODO number story 7
# TODO layout
# TODO colours
# TODO theme/2021/AbelField disclaimer


#import dash
import pandas as pd
#from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import streamlit as st
import math

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

# Make the page wide
st.set_page_config(layout="wide")

# Bootstrap

st.markdown(
    """<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" 
  integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" 
  integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>

  <style>
  body{
      background-color: #fff;
      font-size: 40px;
  }

  </style>
</head>""", unsafe_allow_html=True
)

# =====================
# ===== LOAD DATA =====
# =====================

# Define data file locations
data_folder = '../data/'

location_top_universities = data_folder + 'top-universities.csv'
location_cumulative_winners = data_folder + 'cumulative-winners.csv'
location_winners_per_capita = data_folder + 'winners-per-capita.csv'
location_overview = data_folder + 'overview.csv'

# Load the data
df_top_universities = pd.read_csv(location_top_universities)
df_cumulative_winners =  pd.read_csv(location_cumulative_winners)
df_winners_per_capita  = pd.read_csv(location_winners_per_capita)
df_overview = pd.read_csv(location_overview)


# =================
# =================
# ===== PLOTS =====
# =================
# =================


# =================
# ===== Intro =====
# =================

st.markdown('''
<div class="jumbotron text-center" style='background-color: #fff'>
  <h1 style="margin: auto; width: 100%;">Mathematics Awards Interactive Dashboard</h1>
  <h1 style="margin: auto; width: 100%;"></h1>
</div>
''', unsafe_allow_html=True)


# ==========================
# ===== Number Story 1 =====
# ==========================
# > The overview

# Get the data fields
fields_total = df_overview['Fields Medals'][0]
abel_total = df_overview['Abel Prizes'][0]
top_country = df_overview['Winner Country'][0]
top_country_result = df_overview['Winner result'][0]
top_country_capita = df_overview['Winner per Capita Country'][0]
top_country_capita_result = df_overview['Winner per Capita result'][0]

# Round top country result as number of laureates is a whole number
top_country_result = round(top_country_result)
# Make per capita results per million inhabitants instead of 1
top_country_capita_result = top_country_capita_result * 1000000
# Round per capita results to 3 significant figures
sig_fig = 3
top_country_capita_result = round(top_country_capita_result, sig_fig -
                                  int(math.floor(math.log10(abs(top_country_capita_result)))) - 1)

# Assign the fields to Number Story 1 boxes and set other NS1 settings
box_background_colour = '#fccccc'
box_1_sign = 'Total Fields Medals'
box_2_sign = 'Total Abel Medals'
box_3_sign = 'Country with the most laureates'
box_4_sign = 'Country with the most laureates per capita'
box_1_value = str(fields_total)
box_2_value = str(abel_total)
box_3_value = str(top_country)
box_4_value = str(top_country_capita)
box_3_value_2 = 'with ' + str(top_country_result) + ' laureates'
box_4_value_2 = 'with ' + str(top_country_capita_result) + ' laureates per million inhabitants'

st.markdown('''
<div class="jumbotron text-center"  style='padding: 0;'>
  <div class="row justify-content-md-center" style='background-color: #fff; width: 100%; margin: auto;'>
    <div class="col-sm-2" style="font-size: 15px; vertical-align: bottom;">
        <div style="background-color: '''+box_background_colour+'''; border-radius: 40px; vertical-align: bottom;">
          <p style='text-align: center; font-weight: 400; color: #000; vertical-align: bottom;'>'''+box_1_sign+'''</p>
          <p style='text-align: center; font-size: 50px; font-weight: bold; color: #000'>'''+box_1_value+'''</p>
          <p style='text-align: center; font-size: 0px; color: blue'>\00</p>
        </div>
    </div>
    <div class="col-sm-2" style='font-size: 15px;'>
        <div style="background-color: '''+box_background_colour+'''; border-radius: 40px; vertical-align: middle;">
          <p style='text-align: center; font-weight: 400; color: #000'>'''+box_2_sign+'''</p>
          <p style='text-align: center; position: relative; vertical-align: center; font-size: 50px; font-weight: bold; color: #e73631'>'''+box_2_value+'''</p>
          <p style='text-align: center; font-size: 0px; color: blue'>\00</p>
        </div>
    </div>
    <div class="col-sm-3" style='font-size: 15px;'>
        <div style="background-color: '''+box_background_colour+'''; border-radius: 40px; vertical-align: middle;">
          <p style='text-align: center; font-weight: 400; color: #000'>'''+box_3_sign+'''</p>
          <p style='text-align: center; font-size: 35px; font-weight: bold; color: #70a82c'>'''+box_3_value+'''</p>
          <p style='text-align: center; font-size: 15px; color: #70a82c'>'''+box_3_value_2+'''</p>
        </div>
    </div>
    <div class="col-sm-3" style='font-size: 15px;'>
        <div style="background-color: '''+box_background_colour+'''; border-radius: 40px">
          <p style='text-align: center; font-weight: 400; color: #000'>'''+box_4_sign+'''</p>
          <p style='text-align: center; font-size: 35px; font-weight: bold; color: blue'>'''+box_4_value+'''</p>
          <p style='text-align: center; font-size: 15px; color: blue'>'''+box_4_value_2+'''</p>
        </div>
    </div>
  </div>
</div>
''', unsafe_allow_html=True)


# =============================
# ===== Number Story 2 & 3=====
# =============================
# > Bar plot race total
# > Bar plot race per capita

st.markdown(
    '''
    <h1 style="margin: auto; width: 100%;"></h1>
    <div class="row" style='background-color: #fff; width: 100%; margin: auto;'>
        <div class="col-sm-6" style="font-size: 15px; border-radius: 30px">
            <iframe src='https://flo.uri.sh/visualisation/7956000/embed' frameborder='0' scrolling='no' 
                style='width:100%; height:600px;'> </iframe>
            <div style='width:100%!; margin-top:4px!important; text-align:right!important;'></div>
        </div>
        <div class="col-sm-6" style="font-size: 15px; border-radius: 30px">
            <iframe src='https://flo.uri.sh/visualisation/7956357/embed' frameborder='0' scrolling='no' 
                style='width:100%; height:600px;'></iframe>
            <div style='width:100%!; margin-top:4px!important; text-align:right!important;'></div>
        </div>
     </div>
    ''',
    unsafe_allow_html=True
)


# ==========================
# ===== Number Story 4 =====
# ==========================
# > Line chart cumulative awards



# ==========================
# ===== Number Story 5 =====
# ==========================
# > Line chart cumulative awards per capita



# ==========================
# ===== Number Story 6 =====
# ==========================
# > Choropleth map with total winners



# ==========================
# ===== Number Story 7 =====
# ==========================
# > Universities by awards pie chart

#df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
#fig = px.pie(df_top_universities, values='University', names='Winners', title='Population of European continent')