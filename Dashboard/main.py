# Do you like titles?
# NS 5 does not start from 0 because of smoothing. Could make it not smooth, but it would be ugly.
# Pie chart sizes ok? Not misleading?
# Flourish map looks weird when everything is 0

import os
import pandas as pd
import plotly.express as px
import streamlit as st
import math
import json

# ==================
# COLOURS AND STYLES
# ==================

# Make the page wide
st.set_page_config(layout="wide")

# Bootstrap

st.markdown(
    """
<head>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" 
  integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" 
  integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</head>
""", unsafe_allow_html=True)

# =====================
# ===== LOAD DATA =====
# =====================

# Define data file locations
location_top_universities = os.path.abspath("../data/top-universities.csv")
location_cumulative_winners = os.path.abspath("../data/cumulative-winners.csv")
location_winners_per_100_mil = os.path.abspath("../data/winners-per-100-mil.csv")
location_overview = os.path.abspath("../data/overview.csv")
location_world_path = os.path.abspath('../data/custom.geo.json')

# Load the data
df_top_universities = pd.read_csv(location_top_universities)
df_cumulative_winners = pd.read_csv(location_cumulative_winners)
df_winners_per_100_mil = pd.read_csv(location_winners_per_100_mil)
df_overview = pd.read_csv(location_overview)

with open(location_world_path) as f:
    geo_world = json.load(f)


# =================
# =================
# ===== PLOTS =====
# =================
# =================


# =================
# ===== Intro =====
# =================

st.markdown('''
<div class="jumbotron text-center">
  <h1 style="margin: auto;">Mathematics Awards Interactive Dashboard</h1>
  <div class="row justify-content-center">
    <div class="col-sm-3" style="background-color: #c0f9fa; border-radius: 40px;">
        <p style="margin: auto; text-align: center; color: #000; font-size: 12px"><i>For best experience use 
        fullscreen mode and light theme<br>(☰ → Settings → Theme → Light)</i></p>
        <p style="margin: auto; text-align: center; color: #000; font-size: 12px"><i>Awards used: Fields Medal & Abel Prize</i></p>
        <p style="margin: auto; text-align: center; color: #000; font-size: 12px"><i>Data: 1935-2021</i></p>
    </div>
    <p style="margin: auto; width: 100%;">\00</p>
  </div>
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
top_country_result = df_overview['Winner Result'][0]
top_country_capita = df_overview['Winner per Capita Country'][0]
top_country_100_mil_result = df_overview['Winner per 100 Million Inhabitants Result'][0]

# Round top country result as number of laureates is a whole number
top_country_result = round(top_country_result)
# Round per capita results to 3 significant figures
sig_fig = 3
top_country_100_mil_result = round(top_country_100_mil_result, sig_fig -
                                   int(math.floor(math.log10(abs(top_country_100_mil_result)))) - 1)

# Assign the fields to Number Story 1 boxes and set other NS1 settings
box_1_sign = 'Total Fields Medals'
box_2_sign = 'Total Abel Awards'
box_3_sign = 'Country with the most laureates'
box_4_sign = 'Country with the most laureates per capita'
box_1_value = str(fields_total)
box_2_value = str(abel_total)
box_3_value = str(top_country)
box_4_value = str(top_country_capita)
box_3_value_2 = 'with ' + str(top_country_result) + ' laureates'
box_4_value_2 = 'with ' + str(top_country_100_mil_result) + ' laureates per 100 million inhabitants'

st.markdown('''
<div class="jumbotron text-center"  style='padding: 0;'>
  <div class="row justify-content-md-center" style='width: 100%; margin: auto;'>
    <div class="col-sm-2" style="font-size: 15px; vertical-align: bottom;">
        <div style="background-color: #64e987; border-radius: 40px; vertical-align: bottom;">
          <p style='text-align: center; font-weight: 400; color: #000; position: relative; top: 10px'>'''
            + box_1_sign + '''</p>
          <p style='text-align: center; font-size: 47.5px; font-weight: bold; color: #000; 
          position: relative; bottom: 3px'>''' + box_1_value + '''</p>
          <p style='text-align: center; font-size: 0px; color: blue'>\00</p>
        </div>
    </div>
    <div class="col-sm-2" style='font-size: 15px;'>
        <div style="background-color: #92f294; border-radius: 40px; vertical-align: middle;">
          <p style='text-align: center; font-weight: 400; color: #000; position: relative; top: 10px'>''' + box_2_sign
            + '''</p>
          <p style='text-align: center; font-size: 47.5px; font-weight: bold; color: #000; position: relative; 
          bottom: 3px'>''' + box_2_value + '''</p>
          <p style='text-align: center; font-size: 0px; color: #000'>\00</p>
        </div>
    </div>
    <div class="col-sm-3" style='font-size: 15px;'>
        <div style="background-color: #88cefb; border-radius: 40px; vertical-align: middle;">
          <p style='text-align: center; font-weight: 400; color: #000; position: relative; top: 10px'>''' + box_3_sign
            + '''</p>
          <p style='text-align: center; font-size: 35px; font-weight: bold; color: #000'>''' + box_3_value + '''</p>
          <p style='text-align: center; font-size: 13px; color: #000; position: relative; bottom: 10px'>'''
            + box_3_value_2 + '''</p>
        </div>
    </div>
    <div class="col-sm-3" style='font-size: 15px;'>
        <div style="background-color: #fccccc; border-radius: 40px">
          <p style='text-align: center; font-weight: 400; color: #000; position:relative; top:10px'>''' +
            box_4_sign + '''</p>
          <p style='text-align: center; font-size: 35px; font-weight: bold; color: #000'>''' + box_4_value + '''</p>
          <p style='text-align: center; font-size: 13px; color: #000; position: relative; bottom: 10px'>''' +
            box_4_value_2 + '''</p>
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
    <div class="row" style='width: 100%; margin: auto;'>
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
     <h1 style="margin: auto; width: 100%;"></h1>
    ''',
    unsafe_allow_html=True
)


# ==============================
# ===== Number Story 4 & 5 =====
# ==============================
# > Line chart cumulative awards
# > Line chart cumulative awards per capita

column_1, column_2 = st.columns(2)
chart_height = 600
plot_1_title = '<b>Laureates per country</b>'
plot_2_title = '<b>Laureates per country per 100 million inhabitants</b>'

with column_1:
    fig = px.line(df_cumulative_winners, x="Year", y=df_cumulative_winners.columns, line_shape='spline',
                  height=chart_height, title=plot_1_title, color_discrete_sequence=px.colors.qualitative.Light24)

    fig.update_layout(xaxis_title="Year", yaxis_title="Laureates", legend=dict(title='<b>Country</b>'),
                      font=dict(size=13), title=dict(y=0.9, xanchor='left', yanchor='top', font={'size': 23}))

    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

with column_2:
    fig = px.line(df_winners_per_100_mil, x="Year", y=df_winners_per_100_mil.columns, line_shape='spline',
                  height=chart_height, title=plot_2_title, color_discrete_sequence=px.colors.qualitative.Light24)

    fig.update_layout(xaxis_title="Year", yaxis_title="Laureates per 100 million inhabitants",
                      legend=dict(title='<b>Country</b>'), font=dict(size=13),
                      title=dict(y=0.9, xanchor='left', yanchor='top', font={'size': 23}))

    st.plotly_chart(fig, use_container_width=True, sharing="streamlit")

    st.markdown(
        '''
        <h1 style="margin: auto; width: 100%;"></h1>
        ''',
        unsafe_allow_html=True
    )


# ==========================
# ===== Number Story 7 =====
# ==========================
# > Universities by awards pie chart

fig = px.pie(df_top_universities, values='Winners', names='University',
             title='<b>Laureates by institutes of affiliation</b>', height=1000, labels={'Winners': 'Laureates'})

fig.update_traces(textinfo='percent+label', textposition='inside')
fig.update_layout(title={'font': {'size': 30}}) # , title_x = 0.25)
st.plotly_chart(fig, use_container_width=True)


# ==========================
# ===== Number Story 6 =====
# ==========================
# > Choropleth map with total winners

df_2021 = df_cumulative_winners.iloc[-1]
countries = df_2021.drop('Year').to_frame(name='Laureates')
countries_geo = []

# Looping over the GeoJSON file
for country in geo_world['features']:

    # Country name detection
    country_name = country['properties']['name']

    # Getting information from both GeoJSON file and dataFrame
    geometry = country['geometry']

    countries_geo.append({
        'type': 'Feature',
        'geometry': geometry,
        'id': country_name
    })

geo_world_ok = {'type': 'FeatureCollection', 'features': countries_geo}

# Create figure
fig = px.choropleth_mapbox(
    countries,
    geojson=geo_world_ok,
    locations=countries.index,
    color=countries['Laureates'],
    color_continuous_scale='Reds',
    range_color=(0, countries['Laureates'].max()),
    hover_name=countries.index,
    hover_data={'Laureates': True},
    mapbox_style='carto-positron',
    zoom=1,
    center={'lat': 19, 'lon': 11},
    opacity=0.6,
    height=830,
    title='<b>Mathematics award laureates by country</b>',
    labels={'index': 'Country'},
)

fig.update_layout(title={'font': {'size': 29}})
st.plotly_chart(fig, use_container_width=True)
