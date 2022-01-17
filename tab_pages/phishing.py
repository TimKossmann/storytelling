from dash import dcc, html, Input, Output
from phishing_graphs import Phishing_Graphs


class PhishingPage():
    def __init__(self):
        self.pg = Phishing_Graphs()

    def get_input_dount(self):
        return self.pg.get_input_donut()

    def get_link_donut(self):
        return self.pg.get_link_donut()

    def get_attach_donut(self):
        return self.pg.get_attach_donut()

    def get_layout(self):
        return html.Div(
            id="phishing-wrapper", 
            children=[
                
                html.H3("Was der Email-Emfänge mit Phishing Mails tun soll"),
                html.Div(
                    id="what-phishing-wants",
                    children=[
                        dcc.Graph(figure=self.get_link_donut()),
                        dcc.Graph(figure=self.get_input_dount()),
                        dcc.Graph(figure=self.get_attach_donut()),
                    ]
                )
            ])

if __name__ == "__main__":
    pp = PhishingPage()
