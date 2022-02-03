import imp
from operator import imod
from dash import dcc, html, Input, Output
from phishing_graphs import Phishing_Graphs

import dash
import re


class PhishingPage():
    def __init__(self):
        self.pg = Phishing_Graphs()

    def get_donuts(self):
        return html.Div(
            id="donut-wrapper",
            children=[
                
            ]
        )

    def get_layout(self):
        return html.Div(
            id="phishing-wrapper",
            children=[

            ]
        )