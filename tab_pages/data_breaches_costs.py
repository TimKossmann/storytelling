from dash import dcc, html, Input, Output
import dash

from data_breaches_bar_chart_bubble_plot_actual_year import Charts_DataBreaches

class DataBreachesPage():
    def __init__(self, app):
        self.app = app
        self.dbr = Charts_DataBreaches()

    def update_bubblechart_by_year(self, year):
        return self.dbr.update_bubblechart_by_year(year)

   
    
    def get_layout(self):
        
        return html.Div(
                id="dataBreaches-wrapper",
                children=[
                    html.Div(id="year-overview",
                        children=[
                            html.H3(id="dataBreaches-header", children="data breaches"),
                            dcc.Graph(className="graph", id='graph-with-slider'),
                            dcc.Slider(
                            id='year-slider',
                            min=self.dbr.df['year'].max() - 10 ,
                            max=self.dbr.df['year'].max(),
                            value=self.dbr.df['year'].max(),
                            marks={str(year): str(year) for year in self.dbr.df['year'].unique()},
                            step=None
                            ),
    
                            
                        ]),
                    html.Div(id="dataBreach",
                        children=[
                            html.H6("Informationen über ???"),
                            dcc.Graph(className="graph", id='graph-with-slider2'),
                            dcc.Slider(
                            id='year-slider2',
                            min=self.dbr.df['year'].max() - 10 ,
                            max=self.dbr.df['year'].max(),
                            value=self.dbr.df['year'].max(),
                            marks={str(year): str(year) for year in self.dbr.df['year'].unique()},
                            step=None
                            ),
                        ]
                    )         
                ]
            )
        