import plotly.express as px
import dash
import pandas as pd 
import numpy as np
import random
import datetime

class Charts_DataBreaches():

    def __init__(self):
        self.df = pd.read_excel("./datasets/DataBreaches.xlsx")
        self.date = datetime.date.today() # aktuelles Datum abrufen
        self.actual_year = int(self.date.strftime("%Y")) # Datum zu nur Jahr formatieren
        self.edit_df()
        self.fig_barplot = None 
        self.create_barplot()
        self.fig_bubblechart = None
        self.update_bubblechart_by_year(self.actual_year)

    # Umwandlung der Datentypen 
    def edit_df(self):
        self.df = self.df.rename(columns= {'year   ':'year'}) # Spalte year umbennenen (aufgrund von Leerzeichen nach "year")
        self.df = self.df.drop(self.df.index[[0]]) # Löschen der ersten Zeile
        self.df["year"] = self.df["year"].astype("int") # Umwandlung des Datentyps von Year von Object in Integer mit der typecasting_from_column-Methode
        self.df["records lost"] = pd.to_numeric(self.df["records lost"]) # Umwandlung des Datentyps von records lost von Object in numeric
        self.df["organisation"] = self.df["organisation"].astype("string") # Umwandlung des Datentyps von Organisation von Object in string
        
        
    
    # Balken-Diagramm erstellen
    def create_barplot(self):
        self.fig_barplot = px.bar(self.df, x="year", y='records lost', color='sector')
        # self.fig_barplot.show()

    # Bubble-Chart erstellen
    def update_bubblechart_by_year(self, year):
        self.fig_bubblechart = px.scatter(self.df[(self.df['year'] == year)], x="records lost", y="date", 
	        size="records lost", color="organisation",
            hover_name="organisation", log_x=True, size_max=60)
        self.fig_bubblechart.update_layout(transition_duration=500)
        return self.fig_bubblechart








