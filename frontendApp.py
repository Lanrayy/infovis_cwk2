from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import random as r
import os
import time


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('data_bar.csv')
questions = ['Largest % Plastic waste in stream', '2nd Smallest % Inadequately managed waste', 'Smallest % Littered waste', 'Largest Waste Generation (kg/day)', '2nd Smallest Plastic waste generation (kg/day)', 'Smallest Inadequately managed plastic waste (kg/day)', '2nd Largest Plastic waste littered (kg/day)', 'Largest Mismanaged plastic waste (kg/pp)', 'Smallest Mismanaged plastic waste in 2010 (tonnes)', '3rd Largest Mismanaged plastic waste in 2025 (tonnes)']
cols = ['% Plastic waste in stream', '% Inadequately managed waste', '% Littered waste', 'Waste Generation (kg/day)', 'Plastic waste generation (kg/day)', 'Inadequately managed plastic waste (kg/day)', 'Plastic waste littered (kg/day)', 'Mismanaged plastic waste (kg/pp)', 'Mismanaged plastic waste in 2010 (tonnes)', 'Mismanaged plastic waste in 2025 (tonnes)']
captions =["The graph shows the percentage of plastic waste found in streams over time.",
"The chart illustrates the percentage of waste that is inadequately managed over time.",
"This graph displays the percentage of littered waste over time.",
"The graph shows the daily generation of waste in kilograms.",
"This chart illustrates the daily generation of plastic waste in kilograms.",
"The graph displays the daily generation of inadequately managed plastic waste in kilograms.",
"This chart shows the daily amount of plastic waste that is littered in kilograms.",
"The graph illustrates the amount of mismanaged plastic waste per person.",
"This chart displays the total amount of mismanaged plastic waste in 2010 in tonnes.",
"The graph shows the total amount of mismanaged plastic waste in 2025 in tonnes."]

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
            html.H4("Plastic Pollution in different Countries - Bar Chart"),
            #html.H4("Plastic Pollution in different Countries - Chropleth Map"),
            #html.H6("Geographical Map vs Bar Chart")
        ],
    )


def define_question(index):
    return "Click on the country which has the " + questions[index] + "."
def make_bar(index):
    fig_bar = px.bar(df, x=cols[index], y=('Country'))
    fig_bar.update_layout(margin=dict(l=20, r=20, t=20, b=100))
    fig_bar.add_annotation(dict(
                                x=0.45,
                                y=-0.12,
                                showarrow=False,
                                text=captions[index],
                                textangle=0,
                                xanchor='center',
                                xref="paper",
                                yref="paper"))
    fig_bar.update_yaxes(showline=True, linewidth=2, linecolor='black',title_standoff=40,titlefont=dict(size=20))
    fig_bar.update_xaxes(showline=True, linewidth=2, linecolor='black',titlefont=dict(size=20))
    return fig_bar

def make_map(index):
    fig = go.Figure(data=go.Choropleth(
        locations = df['Country Codes'],
        z = df[cols[index]],
        text = df['Country'],
        
        # make the color be spelt wrong to view list of possible colours
        
        colorscale = 'darkmint',
        autocolorscale=False,
        marker_line_color='darkgray',
        #colorbar_title = cols[index],
))


    fig.update_layout(
        title=dict(
            text=cols[index],
            x=1,
            yref=0,
            font=dict(size=20),
            ),
        geo=dict(
            #showframe=False,
            showcoastlines=False,
            projection_type='equirectangular'
        ),
        annotations=[dict(
            x=0.5,
            y=0.2,
            text=captions[index],
            showarrow=False
        )]
            
           
    )
    
    
    return fig
    
    
    
    
    
    


def build_QandA():
    index = choose_index()
    return html.Div(
                className="button options",
                children=[
                    #dcc.Graph(figure=make_map(index),style={'width': '80vh', 'height': '80vh'}),
                    dcc.Graph(figure=make_bar(index),style={'width': '80vh', 'height': '80vh'}),
                    html.Br(),
                    html.H6(define_question(index))]
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
