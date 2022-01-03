import dash
from dash import dcc, html, Input, Output
import plotly.express as px


import pandas as pd

from data_breaches_bar_chart_bubble_plot_actual_year import Charts_DataBreaches 
from passwords_wordcloud import Chart_WordCloud
from tab_pages.password import PasswordPage

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dbr = Charts_DataBreaches() # Klasse Charts_DataBreaches aufrufen
wc = Chart_WordCloud() # Klasse Chart_WordCloud aufrufen
 
app = dash.Dash(__name__)
pp = PasswordPage(app)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backroudColor': 'green'}, children=[
    html.Div([
        html.Header(children=[
            html.Div(
                id="app-header",
                children=[
                    html.H1(
                        id="app-title",
                        children='Welcome to LaCTiS',
                        style={
                            
                        }
                    ),
            
                    dcc.Tabs(
                        id="tabs-container", 
                        value='tab_databreaches', 
                        parent_className='custom-tabs',

                        children=[
                            dcc.Tab(
                                className="custom-tab", 
                                label='Schaden durch Hacks', 
                                value='tab_databreaches',
                                selected_className='custom-tab--selected'
                            ),
                            dcc.Tab(
                                className="custom-tab", 
                                label='Hackermethoden', 
                                value='tab_methods',
                                selected_className='custom-tab--selected'
                            ),
                            dcc.Tab(
                                className="custom-tab", 
                                label='Phishing', 
                                value='tab_phishing',
                                selected_className='custom-tab--selected'
                            ),
                            dcc.Tab(
                                className="custom-tab", 
                                label='Passwortsicherheit', 
                                value='tab_password',
                                selected_className='custom-tab--selected'
                            ),
                        ]
                    ),  
                ]
            ),
        ]),
        html.Div(id="tabs-content")
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


@app.callback(Output('tabs-content', 'children'),
              Input('tabs-container', 'value'))
def render_content(tab):
    if tab == 'tab_password':
        return pp.get_layout()



############# Password-Tab #############

@app.callback(
    dash.dependencies.Output('wordcloud', 'src'),
    Input('wordcloud', 'img')
)
def make_wordlcloud(img):
    print("wordcloud")
    return wc.create_wordcloud()

@app.callback(
    Output('hallo', 'children'),
    Input('my-input', 'value')
)
def update_output_div(input_value):
    return html.H3(["Output: " + input_value])#{}".format(input_value)


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    return dbr.update_bubblechart_by_year(selected_year)

@app.callback(
    Output('graph-with-slider2', 'figure'),
    Input('year-slider2', 'value'))
def update_figure(selected_year):
    return dbr.update_bubblechart_by_year(selected_year)





if __name__ == '__main__':
    app.run_server(debug=True)

"""html.Div(
            id="wrapper",
            children=[
            html.Div(
                id="left-side",
                children=[
                dcc.Graph(className="graph", id='graph-with-slider'),
                dcc.Slider(
                    id='year-slider',
                    min=dbr.df['year'].max() - 10 ,
                    max=dbr.df['year'].max(),
                    value=dbr.df['year'].max(),
                    marks={str(year): str(year) for year in dbr.df['year'].unique()},
                    step=None
                ),
            ]),
            html.Div(
                id="right-side",
                children=[
                    dcc.Graph(className="graph", id='graph-with-slider2'),
                dcc.Slider(
                    id='year-slider2',
                    min=dbr.df['year'].max() - 10 ,
                    max=dbr.df['year'].max(),
                    value=dbr.df['year'].max(),
                    marks={str(year): str(year) for year in dbr.df['year'].unique()},
                    step=None
                ),
                #html.Img(id = 'wordcloud')
                
            ]),
            

        ])"""