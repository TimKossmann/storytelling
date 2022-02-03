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
                
                html.H3("Was der Email-Emfänge mit Phishing Mails tun soll"),
                html.Div(
                    id="what-phishing-wants",
                    children=[
                        dcc.Graph(figure=self.pg.get_link_donut()),
                        dcc.Graph(figure=self.pg.get_input_donut()),
                        dcc.Graph(figure=self.pg.get_attach_donut()),
                    ]
                ),
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
                                html.H6("Wähle ob du nach deiner Abteilung oder deiner Branche filtern möchtest:"),
                                dcc.Dropdown(
                                    id='phishing-dropdown',
                                    options=[
                                        {'label': 'Abteilung', 'value': 'Abteilung'},
                                        {'label': 'Branche', 'value': 'Branche'},
                                    ],
                                    value=self.type
                                ),
                                html.H6(f"Hebe deine {self.type} hervor"),
                                html.Div(id="mark-dropdown-wrapper"),
                                
                            ]
                        ),
                    ]
                )


            ])

if __name__ == "__main__":
    pp = PhishingPage()
