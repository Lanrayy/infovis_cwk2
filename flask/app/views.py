from flask import render_template
from app import app
# from dash import Dash, dcc, html, Input, Output
# import dash_bootstrap_components as dbc
import plotly.express as px
import plotly
import pandas as pd
import random as r
import os
import time
import json

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('./test.csv')


def generate_bar_chart(df):
    fig = px.bar(df.head(15), x='Country',
                 y='Pollution', width=800, height=400)
    # fig.show()
    return fig


@app.route('/')
def index():
    user = {'name': 'Sam Wilson'}
    fig = generate_bar_chart(df)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html',
                           title='Simple template example',
                           fig=fig,
                           graphJSON=graphJSON,
                           user=user)
