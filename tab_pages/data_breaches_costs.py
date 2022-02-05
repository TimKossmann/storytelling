from dash import dcc, html, Input, Output
import dash

from data_breaches_bar_chart_bubble_plot_actual_year import Charts_DataBreaches

class DataBreachesPage():
    def __init__(self, app):
        self.app = app
        self.dbr = Charts_DataBreaches()

    def update_bubblechart_by_year(self, year):
        return self.dbr.update_bubblechart_by_year(year)

    def create_lineplot(self, year):
        return self.dbr.create_lineplot(year)

    def get_excel_data(self):
        return self.dbr.df.to_excel
    
    def get_layout(self):
        
        return html.Div(
                id="dataBreaches-wrapper",
                children=[
                    html.Div(
                        id="databreach-chart-wrapper",
                        children=[
                        html.H3("Schaden der durch Hackerattacken entsteht"),
                        html.P("Hier finden Sie eine Übersicht, wieviel Schaden durch Hacks weltweit entstehen."),
                        html.Div(id="dataBreach",
                            children=[
                                #html.H6("Informationen über ???"),
                                dcc.Graph(className="graph", id='year-line-chart'),
                                
                            ]
                        ),
                        html.Div(id="year-overview",
                            children=[
                                #html.H3(id="dataBreaches-header", children="data breaches"),
                                dcc.Graph(className="graph", id='graph-with-slider'),
                                
        
                                
                            ]),
                        ]
                    ),
                    html.Div(
                        id="slider-wrapper",
                        children=[
                        dcc.Slider(
                                id='year-slider',
                                min=self.dbr.df['year'].max() - 7 ,
                                max=self.dbr.df['year'].max(),
                                value=self.dbr.df['year'].max(),
                                marks={str(year): str(year) for year in self.dbr.df['year'].unique()},
                                step=None
                                ),
                        ]
                    ),
                    html.Div(
                        className="download-wrapper",
                        children=
                        [
                            html.Button("CSV herunterladen", className="btn_csv", id="data_breaches_btn"),
                            dcc.Download(id="download-data-breches-excel"),
                        ]
                    )
                ]
            )
        