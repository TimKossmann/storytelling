from dash import dcc, html, Input, Output
from phishing_graphs import Phishing_Graphs


class PhishingPage():
    def __init__(self):
        self.pg = Phishing_Graphs()
        self.type = "Abteilung"

    def get_layout(self):
        return html.Div(
            id="phishing-wrapper", 
            children=[
                
                html.H3("Was der Email-Emfänger mit Phishing Mails tun soll"),
                html.Div(
                    id="what-phishing-wants",
                    children=[
                        html.Div(className="donut-wrapper", children=[
                            dcc.Graph(className="dounut", figure=self.pg.get_link_donut()),
                        ]),
                        html.Div(className="donut-wrapper", children=[
                            dcc.Graph(className="dounut",figure=self.pg.get_input_donut()),
                        ]),
                        html.Div(className="donut-wrapper", children=[
                            dcc.Graph(className="dounut",figure=self.pg.get_attach_donut()),
                        ]),
                        
                    ]
                ),
                html.H3("Wer besonders anfällig ist für Phishing Attacken"),
                html.Br(),
                html.Br(),
                html.Div(
                    id="fail-bar-chart-wrapper",
                    children=[
                        html.Div(
                            id="failbar-wrapper",
                            children=[
                                dcc.Graph(id="failbar-chart"),
                            ]
                        ),
                        html.Div(
                            id="failinfo-wrapper",
                            children=[
                                html.H4("Wähle ob du nach deiner Abteilung oder deiner Branche filtern möchtest:"),
                                dcc.Dropdown(
                                    id='phishing-dropdown',
                                    className="dropdown", 
                                    options=[
                                        {'label': 'Abteilung', 'value': 'Abteilung'},
                                        {'label': 'Branche', 'value': 'Branche'},
                                    ],
                                    value=self.type
                                ),
                                html.H4(id="mark-header"),#f"Hebe deine {self.type} hervor"),
                                html.Div(className="dropdown", id="mark-dropdown-wrapper"),
                                
                            ]
                        ),
                    ]
                )


            ])

if __name__ == "__main__":
    pp = PhishingPage()
