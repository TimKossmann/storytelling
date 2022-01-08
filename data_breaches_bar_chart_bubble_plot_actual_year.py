import plotly.express as px
import dash
import pandas as pd 
import numpy as np
import random
import datetime

class Charts_DataBreaches():

    def __init__(self):
        self.df = pd.read_excel("./datasets/DataBreaches.xlsx")
        #self.date = datetime.date.today() # aktuelles Datum abrufen
        #self.actual_year = int(self.date.strftime("%Y")) # Datum zu nur Jahr formatieren
        self.actual_year = 2021
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
        for x in range( 2005, 2022):
            self.df['organisation_name'] = np.where((self.df['year'] == x) & (self.df['records lost'] >= self.df['records lost'].max()*0.005), self.df['organisation'], '')
            print('das Jahr:' , x)
        
        
    
    # Balken-Diagramm erstellen
    def create_barplot(self):
        self.fig_barplot = px.bar(self.df, x="year", y='records lost', color='sector')
        # self.fig_barplot.show()

    #     

    '''# Bubble-Chart erstellen
    def update_bubblechart_by_year(self, year):
        self.fig_bubblechart = px.scatter(self.df[(self.df['year'] == year)], x="records lost", y="date", 
	        size="records lost", color="organisation",
            hover_name="organisation", log_x=True, size_max=60)
        self.fig_bubblechart.update_layout(transition_duration=500)
        return self.fig_bubblechart
'''
    # Bubble-Chart erstellen
    def update_bubblechart_by_year(self, year):
        self.fig_bubblechart = px.scatter(self.df[(self.df['year'] == year)], x="date", y="records lost", 
	        size="records lost", color="organisation",
            hover_name="organisation", size_max=60, text = "organisation_name", 
            labels={
                        "date": "Monat Jahr",
                        "records lost": "entstandener Schaden (in US$)",
                        },
                        title='Testtitle')
        self.fig_bubblechart.update_layout(
                title={
        'text': "Plot Title",
        'y':0.87,
        'x':0.0,
        'xref': "paper",
        'xanchor': 'left',
        'yanchor': 'top'},
        plot_bgcolor = "rgba(0,0,0,0)",
        paper_bgcolor = "rgba(255,255,255,1)",
        #uniformtext_minsize = 12 ,
        #uniformtext_mode = 'hide',
        
            xaxis= dict(
                    #tickformat="%b\n%Y",
                    #ticklabelmode="period"
                    # dtick= 500000,
                    ticks = "outside",
                    tickwidth = 1,
                    tickcolor = "black",
                    ticklen = 8,
                    tickfont = dict(family = 'Arial', size = 14),
                    showline = True,
                    linewidth = 1,
                    linecolor = 'black',
                    showgrid = False,
                    
                    

                    
                    ),
            yaxis = dict(
                    #range=[self.df['records lost'].min(), self.df['records lost'].max()+(self.df['records lost'].max()/1.5)],
                    tickformat="%b\n%Y",
                    ticklabelmode="period",
                    tick0 = self.df['records lost'].max()-100000,
                    #dtick= 1000000,
                    ticks = "outside",
                    tickwidth = 1,
                    tickcolor = "black",
                    ticklen = 8,
                    tickfont = dict(family = 'Arial', size = 14),
                    showline = True,
                    linewidth = 1,
                    linecolor = 'black',
                    #zeroline = True,
                    showgrid = False,
                    ),
            uniformtext_minsize=8, uniformtext_mode='hide',   
            transition_duration=500)
        return self.fig_bubblechart







