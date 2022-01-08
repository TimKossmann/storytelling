from dash import dcc, html, Input, Output
import dash

from data_breaches_attack_vectors_treemap import Chart_AttackVectors

class AttackVectorsPage():
    def __init__(self, app):
        self.app = app
        self.atp = Chart_AttackVectors()

   
    def get_information_attackVectors(self, clickData):
        return self.atp.get_information_attackVectors(clickData)

    def get_layout(self):
        
        return html.Div(
                id="attackVector-wrapper",
                className="wrapper",
                children=[
                    html.Div(
                        id="left-side",
                        children=[
                            html.H3(id="attackVector-header", children="attack vectors"),
                            html.Div(className="figure", id='attackVectors'),
                            
    
                            html.Div([
                                dcc.Markdown("""
                                    **Click Data**

                                    Click on points in the graph.
                                """),
                                html.Pre(id='click-data'),
                            ]),
                            dcc.Graph(
                                id='basic-interactions', 
                                figure = self.atp.fig
                                ),
                        ]),
                    html.Div(
                        id="right-side",
                        children=[
                            html.H6("Informationen über Angriffspunkte für Cyber Attacken"),
                            html.H5(id='name-attack'),
                            html.Div(id='info-attack'),
                        ]
                    )         
                ]
            )
        