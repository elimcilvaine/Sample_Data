{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import dash\
from dash import dcc, html, Input, Output\
import plotly.express as px\
import pandas as pd\
\
# Initialize the Dash app\
app = dash.Dash(__name__)\
server = app.server  # For deployment on Render\
\
# Sample data\
df = pd.DataFrame(\{\
    "x": [1, 2, 3, 4, 5],\
    "y": [10, 20, 30, 40, 50],\
    "category": ["A", "B", "A", "B", "A"]\
\})\
\
# Layout of the app\
app.layout = html.Div([\
    html.H1("Sample Dash Dashboard"),\
    html.P("Select a category to filter the data:"),\
    dcc.Dropdown(\
        id="category-filter",\
        options=[\
            \{"label": "All", "value": "All"\},\
            \{"label": "A", "value": "A"\},\
            \{"label": "B", "value": "B"\}\
        ],\
        value="All"\
    ),\
    dcc.Graph(id="scatter-plot")\
])\
\
# Callback to update the graph based on the dropdown\
@app.callback(\
    Output("scatter-plot", "figure"),\
    Input("category-filter", "value")\
)\
def update_graph(selected_category):\
    filtered_df = df if selected_category == "All" else df[df["category"] == selected_category]\
    fig = px.scatter(filtered_df, x="x", y="y", title="Scatter Plot", color="category")\
    return fig\
\
# Run the app\
if __name__ == "__main__":\
    app.run_server(debug=True)\
}