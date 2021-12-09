import dash
from dash import dcc, html, Input, Output
import plotly.express as px


import pandas as pd

from data_breaches_bar_chart_bubble_plot_actual_year import Charts_DataBreaches 

dbr = Charts_DataBreaches() # Klasse Charts_DataBreaches aufrufen


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=dbr.df['year'].max() - 10 ,
        max=dbr.df['year'].max(),
        value=dbr.df['year'].max(),
        marks={str(year): str(year) for year in dbr.df['year'].unique()},
        step=None
    )
])




@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    return dbr.update_bubblechart_by_year(selected_year)


if __name__ == '__main__':
    app.run_server(debug=True)