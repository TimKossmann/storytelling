from dash import dcc, html, Input, Output
from phishing_graphs import Phishing_Graphs
import pandas as pd


class PhishingPage():
    def __init__(self):
        self.pg = Phishing_Graphs()
        self.type = "Abteilung"

    def get_excel(self):
        writer = pd.ExcelWriter('Phishing.xlsx', engine="xlsxwriter")
        copytoexcel = pd.DataFrame(self.pg.get_fail_df())
        copytoexcel.to_excel(writer, sheet_name="Fehlerquoten")
        copytoexcel = pd.DataFrame(self.pg.get_lia_df())
        copytoexcel.to_excel(writer, sheet_name="Phishing Absichten")
        writer.save()

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
                html.Br(),
                html.H3("Wer besonders anfällig ist für Phishing Attacken"),
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
                        html.Div(
                        className="download-wrapper",
                        children=
                        [
                            html.Button("Excel herunterladen", className="btn_csv", id="phishing_btn"),
                            dcc.Download(id="download-phishing-excel"),
                        ]
                    )
                    ]
                )


            ])

if __name__ == "__main__":
    pp = PhishingPage()
