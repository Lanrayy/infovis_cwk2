from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import random as r
import os
import time


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('data_bar.csv')
questions = ['Largest % Plastic waste in stream', '2nd Smallest % Inadequately managed waste', 'Smallest % Littered waste', 'Largest Waste Generation (kg/day)', '2nd Smallest Plastic waste generation (kg/day)', 'Smallest Inadequately managed plastic waste (kg/day)', '2nd Largest Plastic waste littered (kg/day)', 'Largest Mismanaged plastic waste (kg/pp)', 'Smallest Mismanaged plastic waste in 2010 (tonnes)', '3rd Largest Mismanaged plastic waste in 2025 (tonnes)']
cols = ['% Plastic waste in stream', '% Inadequately managed waste', '% Littered waste', 'Waste Generation (kg/day)', 'Plastic waste generation (kg/day)', 'Inadequately managed plastic waste (kg/day)', 'Plastic waste littered (kg/day)', 'Mismanaged plastic waste (kg/pp)', 'Mismanaged plastic waste in 2010 (tonnes)', 'Mismanaged plastic waste in 2025 (tonnes)']
def choose_index():
    yes = 1
    selected = []
    index = r.randint(0, len(cols)-1)
    for x in selected:
        if x != index:
                yes = 1
        else:
                yes = 0
    if yes == 1:
        selected.append(index)
    return index


def build_banner(df):
    return html.Div(
        className="banner",
        children=[
            html.H5("Plastic Pollution in different Countries"),
            html.H6("Geographical Map vs Bar Chart")
        ],
    )


def define_question(index):
    return questions[index]
def make_bar(index):
    fig_bar = px.bar(df, x=cols[index], y='Country')
    return fig_bar
def build_QandA():
    index = choose_index()
    return html.Div(
                className="button options",
                children=[
                    dcc.Graph(figure=make_bar(index)),
                    html.H6(define_question(index)),
                    html.A(
                        html.Button(children="ENTERPRISE DEMO"),
                        href="https://plotly.com/get-demo/",
                    ),
                    html.Button(
                        children="LEARN MORE", n_clicks=0
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
#fig_bar1 = px.bar(df, x='Country', y=cols[index])
#fig_bar2 = px.bar(df, x='Country', y=cols[index])
server = app.server


app.layout = html.Div([
    build_banner(df),
    #dcc.Graph(figure=fig_bar1),
    build_QandA()
    #dcc.Graph(figure=fig_bar2)
    #generate_bar_chart(df),
    #treemap_develop(df),
])

if __name__ == '__main__':
    app.run_server(debug=True)
