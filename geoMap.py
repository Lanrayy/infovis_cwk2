import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data_bar.csv')

# replace names with array

fig = go.Figure(data=go.Choropleth(
    locations = df['Country Codes'],
    z = df["% Plastic waste in stream"],
    text = df['Country'],
    
    # make the color be spelt wrong to view list of possible colours
    
    colorscale = 'algae',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '$',
    colorbar_title = "% Plastic waste in stream",
))

fig.update_layout(
    title_text="% Plastic waste in stream",
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.cia.gov/library/publications/the-world-factbook/fields/2195.html">\
            CIA World Factbook</a>',
        showarrow = False
    )]
)

fig.show()