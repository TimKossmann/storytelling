import dash
from dash import dcc, html, Input, Output
import plotly.express as px


import pandas as pd

from data_breaches_bar_chart_bubble_plot_actual_year import Charts_DataBreaches 
from passwords_wordcloud import Chart_WordCloud
from data_breaches_attack_vectors_treemap import Chart_AttackVectors
from tab_pages.data_breaches_attack_vectors import AttackVectorsPage
from tab_pages.password import PasswordPage
from tab_pages.data_breaches_costs import DataBreachesPage
import tab_pages.phishing as ph

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

dbr = Charts_DataBreaches() # Klasse Charts_DataBreaches aufrufen
wc = Chart_WordCloud() # Klasse Chart_WordCloud aufrufen
atp = Chart_AttackVectors# Klasse Chart_AttackVectors aufrufen
 
app = dash.Dash(__name__)
pp = PasswordPage(app)
dbav = AttackVectorsPage(app) 
dbp = DataBreachesPage(app)
phishing = ph.PhishingPage() 

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
        html.Br(),html.Br(),html.Br(),
        html.Div(id="tabs-content")
    ]),
     
])

app.css.append_css({
    "external_url":"https://codepen.io/chriddyp/pen/bWLwgP.css"
})



@app.callback(Output('tabs-content', 'children'),
              Input('tabs-container', 'value'))
def render_content(tab):
    if tab == 'tab_password':
        return pp.get_layout()
    elif tab == 'tab_methods':
        return dbav.get_layout()
    elif tab == 'tab_databreaches':
        return dbp.get_layout()
    elif tab == 'tab_phishing':
        return phishing.get_layout()

############# DataBreaches-Tab #############################
@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):
    print(selected_year)
    return dbp.update_bubblechart_by_year(selected_year)

@app.callback(
    Output('year-line-chart', 'figure'),
    Input('year-slider', 'value'))
def update_figure2(selected_year):
    return dbp.create_lineplot(selected_year)

############# Hackermethoden/AttackVectors-Tab #############
@app.callback(
    Output('attack-treemap', 'figure'),
    Input('attack-treemap', 'clickData'))
def display_click_data(clickData):
    return atp.create_treemap()

@app.callback(
    Output('name-attack', 'children'),
    Input('attack-treemap', 'clickData'))
def display_attackVectors(clickData):
    print(clickData)
    return (clickData['points'][0]['label'])
    
        

@app.callback(
    Output('info-attack', 'children'),
    Input('attack-treemap', 'clickData'))
def display_attackVectors(clickData):
    return html.P(dbav.get_information_attackVectors(clickData))
    
############# Phishing-Tab #############

@app.callback(
    Output('failbar-chart', 'figure'),
    Input('phishing-dropdown', 'value'),
    Input('mark-dropdown', 'value'))
def display_attackVectors(phishing_sort, mark):
    print("MARK'"+mark+"'")
    return phishing.pg.get_fail_bar(phishing_sort, mark)


@app.callback(
    Output('mark-dropdown-wrapper', 'children'),
    Input('phishing-dropdown', 'value'))
def display_attackVectors(clickData):
    return dcc.Dropdown(
                id='mark-dropdown',
                options=phishing.pg.get_dropdown_list(clickData),
                value=''
            )



############# Password-Tab #############

@app.callback(
    dash.dependencies.Output('wordcloud', 'src'),
    Input('wordcloud', 'img')
)
def make_wordlcloud(img):
    print("wordcloud")
    return wc.create_wordcloud()

@app.callback(   
    Output('pw-analyse', 'children'),
    Input('my-input', 'value')
)
def update_output_div(input_value):
    return pp.get_pw_analyse(input_value)








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