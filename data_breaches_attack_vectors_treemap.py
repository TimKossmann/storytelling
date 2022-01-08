import plotly.express as px
import plotly.graph_objects as go
import dash
import pandas as pd 
import numpy as np


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

class Chart_AttackVectors():

    def __init__(self):
        self.df = pd.read_excel("./datasets/DataBreaches_initialAttackVectors(2).xlsx") # Excel einlesen
        self.fig = None
        self.create_treemap()

    # Umwandlung der Datentypen 
    def edit_df(self):
        self.df = self.df.drop(self.df.index[[0]]) # Löschen der zweiten Zeile
        self.df["durchschnittliche Gesamtkosten"] = pd.to_numeric(self.df["durchschnittliche Gesamtkosten"]) # Umwandlung des Datentyps von average total costs von Object in numeric
        print(self.df.columns)

    # Treemap erstellen
    def create_treemap(self):
        self.edit_df()
        self.fig = px.treemap(self.df,  path=[px.Constant("all"), 'Fehler','Angriffspunkt'], values='Häufigkeit von Data Breaches',labels= 'Angriffspunkt',color_continuous_scale = None, maxdepth = 2, color='Häufigkeit von Data Breaches', 
        hover_data=['Angriffspunkt'])
        self.fig.update_layout(clickmode='event+select')
        self.fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        self.fig.update_traces(root_color="lightgrey", marker_coloraxis=None)

        
    # Information zu Angriffspunkt auslesen
    def get_information_attackVectors(self, clickData):
        return self.df.loc[self.df['Angriffspunkt'] == clickData['points'][0]['label']]['Information']
    