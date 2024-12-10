{\rtf1\ansi\ansicpg1252\cocoartf2820
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import dash\
from dash import dcc, html\
import plotly.graph_objs as go\
\
# Sample data\
x = [1, 2, 3, 4, 5]\
y = [10, 11, 12, 13, 14]\
\
# Create a Dash app\
app = dash.Dash(__name__)\
server = app.server\
# Layout with a simple plot\
app.layout = html.Div([\
    html.H1("Simple Dash Dashboard"),\
    dcc.Graph(\
        id='line-plot',\
        figure=\{\
            'data': [\
                go.Scatter(x=x, y=y, mode='lines', name='Sample Line')\
            ],\
            'layout': go.Layout(title='Simple Line Plot')\
        \}\
    )\
])\
\
if __name__ == '__main__':\
    app.run_server(debug=True)}