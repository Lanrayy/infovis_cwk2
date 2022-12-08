from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import random as r
import os
import time


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('test.csv')

def build_banner(df):
    return html.Div(
        id="banner",
        children=[
            html.H5("Plastic Pollution in different Countries"),
            html.H6("Geographical Map vs Bar Chart"),
        ],
    )
questions = ['this1?', 'this2']
index = 0
def define_question(index):
    return questions[index]

def build_QandA():
    return html.Div(
                id="button options",
                children=[
                    html.H6(questions[index]),
                    html.A(
                        html.Button(children="ENTERPRISE DEMO"),
                        href="https://plotly.com/get-demo/",
                    ),
                    html.Button(
                        id="learn-more-button", children="LEARN MORE", n_clicks=0
                    )
                ]
    )
'''
def treemap_develop(df):
    cols = ['Pollution', 'Density']
    titles = ['Most to least Polluted Countries',
              'Most to least Density Countries']
    yes = 1
    done = 0
    selected = []
    while done < 30:
        index = r.randint(0, len(cols)-1)
        for x in selected:
            if x != index:
                yes = 1
            else:
                yes = 0
        if yes == 1:
            selected.append(index)
            fig = px.treemap(df.head(16), path=[
                             'Country', cols[index]], values=cols[index], width=1100, height=800)
            fig.update_layout(
                margin=dict(t=50, l=25, r=25, b=25),
                font_size=14,
                title=titles[index],
                template="plotly_dark"),
            fig.show()
            time.sleep(5)
            done += 1
        else:
            continue


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




def place_buttons():
    return html.Div([
        html.H4("Pollution")])

'''
fig_bar = px.bar(df.head(15), x='Country', y='Pollution')
server = app.server

def increment_index(index):
    index += 1

app.layout = html.Div([
    build_banner(df),
    dcc.Graph(figure=fig_bar),
    build_QandA(),
    increment_index(index)
    #generate_bar_chart(df),
    #treemap_develop(df),
])

if __name__ == '__main__':
    app.run_server(debug=True)
