import re
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
        self.clickdata = {}
        self.edit_df()
        self.create_treemap()

    # Umwandlung der Datentypen 
    def edit_df(self):
        self.df = self.df.drop(self.df.index[[0]]) # Löschen der zweiten Zeile
        self.df["durchschnittliche Gesamtkosten"] = pd.to_numeric(self.df["durchschnittliche Gesamtkosten"]) # Umwandlung des Datentyps von average total costs von Object in numeric
        print(self.df.columns)

    # Treemap erstellen
    def create_treemap(self):
        self.fig = px.treemap(
            self.df,  
            path=[px.Constant("Angriffsziele"), 'Fehler','Angriffspunkt'], 
            values='Häufigkeit von Data Breaches',
            labels= 'Angriffspunkt',
            color_continuous_scale=[[0, 'rgb(7, 37, 66)'], [1.0, 'rgb(77, 219, 227)']], 
            maxdepth = 2, 
            color='Häufigkeit von Data Breaches', 
            hover_data=['Angriffspunkt'],
        )
        self.fig.update_layout(clickmode='event+select')
        self.fig.update_layout(
            #uniformtext=dict(minsize=12, mode='show'),
            margin = dict(t=50, l=25, r=25, b=25), 
            plot_bgcolor= 'rgba(0, 0, 0, 0)',
            paper_bgcolor= 'rgba(0, 0, 0, 0)',
            showlegend = False,
            )
        self.fig.update_coloraxes(showscale=False)
        #self.fig.update_traces(root_color="lightgrey", marker_coloraxis=None)

        
    # Information zu Angriffspunkt auslesen
    def get_information_attackVectors(self, clickData):
        self.clickdata = clickData['points'][0]
        if clickData['points'][0]['label'] == "Angriffsziele":
            return "Hacker haben verschiedene Angriffsziele. Zunächst denkt man dabei an Hackerangriffe auf Systeme, bei dem der Angreifer die Schwächen des System ausnuzt. Allerdings können auch Menschen in das Ziel von Hackern geraten. Dabei ist das Ziel oft Menschen zu manipulieren oder sie bestimmte Handlungen ausführen zu lassen, dass der Angreifer Zugang zum System bekommt."
        if clickData['points'][0]['label'] == "Mensch":
            return "Menschliches Fehlverhalten sind eine häufige Ursache für Datenlecks. Meist rührt das Fehlverhalten von Unwissenheit oder Unachtsamkeit. Gegen Unachtsamkeit und mutwilliges Böswilliges Verhalten kann leider schwer etwas unternommen werden. Aber gegen Unwissenheit helfen Schulungen und Sensibilisierungskurse, die maßgeblich zum Schutz des Unternehmens beiträgt."
        if clickData['points'][0]['label'] == "System":
            return "Systemschwächen sind häufig Ziele von Hackern. Dabei können alle möglichen Systeme angegriffen werden, die mit dem Internet verbunden sind. Um mögliche Schwachstellen in Systemen zu finden können externe Sicherheitsfirmen beauftragt werden, die einen Angriff simuliert."
        return self.df.loc[self.df['Angriffspunkt'] == clickData['points'][0]['label']]['Information']

    # Treemap-Mensch erstellen
    def create_treemap_mensch(self):
        self.edit_df()
        df = self.df[self.df['Fehler']=='Mensch']
        fig_mensch = px.treemap(self.df,  path=[px.Constant("Mensch"), 'Angriffspunkt'], values='Häufigkeit von Data Breaches',labels= 'Angriffspunkt',color_continuous_scale=[[0, 'rgb(7, 37, 66)'], [1.0, 'rgb(77, 219, 227)']], maxdepth = 2, color='Häufigkeit von Data Breaches', 
        hover_data=['Angriffspunkt'])
        fig_mensch.update_layout(clickmode='event+select')
        fig_mensch.update_layout(
            margin = dict(t=50, l=25, r=25, b=25), 
            plot_bgcolor= 'rgba(0, 0, 0, 0)',
            paper_bgcolor= 'rgba(0, 0, 0, 0)',
            showlegend = False,
            )
        fig_mensch.update_coloraxes(showscale=False)
        return fig_mensch
        #self.fig.update_traces(root_color="lightgrey", marker_coloraxis=None)
    