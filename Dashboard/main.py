# TODO number story 1
# TODO number story 2
# TODO number story 3
# TODO number story 4
# TODO number story 5
# TODO number story 6
# TODO number story 7
# TODO layout


import dash
import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = dash.Dash(__name__)

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


# ====
# LOAD DATA
# ====

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

# =====
# PLOTS
# =====

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


# ======
# LAYOUT
# ======

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for your data.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)
