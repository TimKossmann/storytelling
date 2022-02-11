import imp
from turtle import width
import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from powerpoint import Powerpoint
from word import PDF


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
pptx = Powerpoint()
pdf = PDF()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.Div([
        html.Header(children=[
            html.Div(
                id="app-header",
                children=[
                    html.Img(src=app.get_asset_url('LaCTiS_Logo.png'), id="logo"),
                    html.Div(
                        id="no-logo-layer",
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
                    
                ]
            ),
        ]),
        html.Br(),html.Br(),html.Br(),
        html.Div(id="tabs-content"),
        html.Br(),
        html.Div(
            className="download-wrapper",
            children=
            [
                html.Button("PPTX", className="btn_csv", id="powerpoint_btn", style={'margin-right':'20px'}),
                dcc.Download(id="download-powerpoint"),
                html.Button("PDF", className="btn_csv", id="pdf_btn"),
                dcc.Download(id="download-pdf"),
            ]
        )  
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

@app.callback(
    Output("download-powerpoint", "data"),
    Input("powerpoint_btn", "n_clicks"),
    prevent_initial_call=True,
)
def download(n_clicks):
    pptx.create_pp()
    return dcc.send_file('Cyber_Security_LaCTiS.pptx')

@app.callback(
    Output("download-pdf", "data"),
    Input("pdf_btn", "n_clicks"),
    prevent_initial_call=True,
)
def download(n_clicks):
    pdf.create_pdf()
    return dcc.send_file('LaCTiS_Report.pdf')

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

@app.callback(
    Output("download-data-breches-excel", "data"),
    Input("data_breaches_btn", "n_clicks"),
    prevent_initial_call=True,
)
def download(n_clicks):
    dbp.get_excel_data()
    return dcc.send_file('Datenlecks_Kosten.xlsx')
    #return dcc.send_data_frame(dbp.get_excel_data(), "datenlecks.xlsx", sheet_name="Tabellenblatt1")



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

@app.callback(
    Output("download-attack_vectors-excel", "data"),
    Input("attack_vectors_btn", "n_clicks"),
    prevent_initial_call=True,
)
def download(n_clicks):
    dbp.get_excel_data()
    #return dcc.send_file('Datenlecks_Kosten.xlsx')
    return dcc.send_data_frame(dbav.get_excel_df(), "Angriffspunkte.xlsx", sheet_name="Angriffspunkte")

    
############# Phishing-Tab #############

@app.callback(
    Output('failbar-chart', 'figure'),
    Input('phishing-dropdown', 'value'),
    Input('mark-dropdown', 'value'))
def display_attackVectors(phishing_sort, mark):
    print("MARK'"+mark+"'")
    return phishing.pg.get_fail_bar(phishing_sort, mark)

@app.callback(
    Output('mark-header', 'children'),
    Input('phishing-dropdown', 'value'))
def display_attackVectors(clickData):
    return f"Hebe deine {clickData} hervor"

@app.callback(
    Output('mark-dropdown-wrapper', 'children'),
    Input('phishing-dropdown', 'value'))
def display_attackVectors(clickData):
    
    return dcc.Dropdown(
                id='mark-dropdown',
                options=phishing.pg.get_dropdown_list(clickData),
                value=''
            )

@app.callback(
    Output("download-phishing-excel", "data"),
    Input("phishing_btn", "n_clicks"),
    prevent_initial_call=True,
)
def download(n_clicks):
    phishing.get_excel()
    return dcc.send_file('Phishing.xlsx')
    #return dcc.send_data_frame(dbp.get_excel_data(), "datenlecks.xlsx", sheet_name="Tabellenblatt1")



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


@app.callback(
    Output("download-password-excel", "data"),
    Input("password_btn", "n_clicks"),
    prevent_initial_call=True,
)
def download(n_clicks):
    #return dcc.send_file('Datenlecks_Kosten.xlsx')
    return dcc.send_data_frame(pp.get_excel_df(), "Passwörter.xlsx", sheet_name="Passwörter")






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