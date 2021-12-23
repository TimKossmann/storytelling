import dash
from dash import dcc, html, Input, Output
import plotly.express as px


import pandas as pd

from data_breaches_bar_chart_bubble_plot_actual_year import Charts_DataBreaches 
from passwords_wordcloud import Chart_WordCloud

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dbr = Charts_DataBreaches() # Klasse Charts_DataBreaches aufrufen
wc = Chart_WordCloud() # Klasse Chart_WordCloud aufrufen
 
app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backroudColor': 'green'}, children=[
    html.Div([
        html.Header(children=[
            html.Title(
                children='Hier sollte der Titel stehen',
                 style={
                    'textAlign': 'left ',
                    'color': 'purple'
                }
            ),
            html.H1(
                children='Welcome to LaCTiS',
                 style={
                    'textAlign': 'left ',
                    'color': 'purple'
                }
            ),
            html.H1(
                children='Test',
                style={
                    'textAlign': 'center',
                    'color': 'blue'
                }
            )
        ]),
        html.Body(children=[
            html.H2(
                children='Hier steht wohl noch nix im Body',
                style={
                    'textAlign': 'center',
                    'color': 'purple'
                }
            )
        ]),    
    ]),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=dbr.df['year'].max() - 15 ,
        max=dbr.df['year'].max(),
        value=dbr.df['year'].max(),
        marks={str(year): str(year) for year in dbr.df['year'].unique()},
        step=None
    ),
    html.Div([
        html.Img(id = 'wordcloud')
    ])
])

app.css.append_css({
    "external_url":"https://codepen.io/chriddyp/pen/bWLwgP.css"
})


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    return dbr.update_bubblechart_by_year(selected_year)

@app.callback(
    dash.dependencies.Output('wordcloud', 'src'),
    Input('wordcloud', 'img')
)
def make_wordlcloud(img):
    return wc.create_wordcloud()


if __name__ == '__main__':
    app.run_server(debug=True)