from dash import dcc, html, Input, Output
import dash

from data_breaches_attack_vectors_treemap import Chart_AttackVectors

class AttackVectorsPage():
    def __init__(self, app):
        self.app = app
        self.atp = Chart_AttackVectors()

   
    def get_information_attackVectors(self, clickData):
        return self.atp.get_information_attackVectors(clickData)
    
    def get_excel_df(self):
        return self.atp.get_df_for_excel().to_excel

    def get_layout(self):
        
        return html.Div(
                id="attackVector-wrapper",
                className="wrapper",
                children=[
                    html.Div(
                        id="left-side",
                        children=[
                            html.H3("Hackerarten und Angriffsziele"),
                            html.Pre(id='click-data'),
                            dcc.Graph(
                                id='attack-treemap', 
                                figure = self.atp.fig
                                ),
                        ]),
                    html.Div(
                        id="right-side",
                        children=[
                            html.H3("Informationen"),
                            html.Div(
                                id="information-wrapper", 
                                children=[
                                    html.H4(id='name-attack',
                                        children=[
                                            "Hinweis"
                                        ]
                                    ),
                                    html.Div(id='info-attack',
                                        children=[
                                            html.P("Klicken Sie links auf die Bereiche zu denen Sie genauere Informationen haben möchten.")
                                        ]
                                    ),
                                ]
                            ),
                        ]
                    ),
                    html.Div(
                        className="download-wrapper",
                        children=
                        [
                            html.Button("CSV herunterladen", className="btn_csv", id="attack_vectors_btn"),
                            dcc.Download(id="download-attack_vectors-excel"),
                        ]
                    )         
                ]
            )
        