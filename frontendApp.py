from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import random as r
import os


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('test.csv')


def generate_table(dataframe, max_rows=192):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


def generate_bar_chart(df):
    fig = px.bar(df.head(15), x='Country', y='Pollution')
    fig.show()


server = app.server

app.layout = html.Div([
    html.H4(children='Pollution'),
    generate_bar_chart(df)
])

if __name__ == '__main__':
    app.run_server(debug=True)
