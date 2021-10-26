# TODO data loading
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


# ==================
# COLOURS AND STYLES
# ==================

colors = {
    'background': '#FFFFFF',
    'text': '#000000'
}


# ====
# DATA
# ====

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})


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
