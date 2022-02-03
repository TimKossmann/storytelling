import re
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
        self.df["records lost"] = (self.df["records lost"]/1000000).round()
        self.df["organisation"] = self.df["organisation"].astype("string") # Umwandlung des Datentyps von Organisation von Object in string
        self.df['organisation_name'] = ''
        for year in range( 2004, 2022):
            self.df['organisation_name'] = np.where((self.df['year'] == year) & (self.df['records lost'] >= self.df['records lost'].max()*0.1), self.df['organisation'], self.df['organisation_name'])
            for month in range(1, 13):
                date = str(year) + '-' + str(month).zfill(2) + '-01'

                new_df = self.df.loc[(self.df["date"] == date)]

                step = 30//(new_df.shape[0]+1)
                start = 0
                for index, row in new_df.iterrows():
                    self.df.loc[index, 'date'] = '%s-%s-%s' % (year, str(month).zfill(2), str(start+step).zfill(2))
                    start += step

    # Linien-Diagramm erstellen 
    def create_lineplot(self, year, darkmode=True): 
        if darkmode:
            color = "white"
        else:
            color = "black"  
        df_fig1 = (pd.DataFrame(self.df.groupby(by=['year'])['records lost'].sum()/1000).reset_index())
        df_fig1 = df_fig1.loc[df_fig1["year"]>= 2014]
        # print(df_fig1.head())
        fig = px.line(df_fig1, x="year", y="records lost", 
                                labels={
                                "year": "Jahre",
                                "records lost": "entstandener Schaden (in Mrd. US$)",

                                },
                                

                                title='Testtitle', markers=True)

        fig.update_xaxes(showgrid=False, title_font_family="Arial", title_font_color=color)
        fig.update_yaxes(showgrid=False, title_font_family="Arial", title_font_color=color)
        fig.update_layout(
            title={
                'text': "Plot Title",
                'y':0.87,
                'x':0.0,
                'xref': "paper",
                'xanchor': 'left',
                'yanchor': 'top'},
            plot_bgcolor = "rgba(0,0,0,0)",
            paper_bgcolor = "rgba(0,0,0,0)",
            font_color=color,

        
            xaxis= dict(
                range=[self.df['year'].max() - 7 - 0.5, self.df['year'].max() + 0.5],
                dtick= 1,
                ticks = "outside",
                tickwidth = 1,
                tickcolor = color,
                ticklen = 8,
                tickfont = dict(family = 'Arial', size = 14),
                showline = False,
                linewidth = 1,
                linecolor = color,
                
                

                
                ),
            yaxis = dict(
                range=[0, df_fig1['records lost'].max()*1.2],
                ticks = "outside",
                tickwidth = 1,
                tickcolor = color,
                ticklen = 8,
                ticklabelposition="outside",
                showline = True,
                linewidth = 1,
                linecolor = color,
                
                ),
            )

        fig.update_traces(
            marker = dict(
                color = '#4DDBE3',
                size = 10,
                opacity = 0.8,
            ),
            line = dict(
                color = '#4DDBE3',
                width = 2
            ),
        )
        #Add Annotation under Title
        """
        fig.add_annotation(x=0,y=1.1,

                        text="entstandener Schaden (in Mrd. US$)", #textangle=-90,
                            xref="paper",
                            valign="top",
            yref="y domain", showarrow=False)
        """


        fig2 = px.scatter(df_fig1.loc[df_fig1["year"] == year], x="year", y="records lost")


        fig2.update_traces(
            marker = dict(
                color = 'rgb(159, 90, 253)',
                size = 15,
                

            ),
        )

        fig.add_trace(fig2.data[0])

        return fig


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
    def update_bubblechart_by_year(self, year, darkmode=True):
        if darkmode:
            color = "white"
        else:
            color = "black"

        self.fig_bubblechart = px.scatter(self.df[(self.df['year'] == year)], x="date", y="records lost", 
	        size="records lost", color="organisation",
            hover_name="organisation", size_max=60, text = "organisation_name", 
            labels={
                        "date": "Monat Jahr",
                        "records lost": "entstandener Schaden (in Mio. US$)",
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
        paper_bgcolor = "rgba(0,0,0,0)",
        font_color=color,
        showlegend = False,
        #uniformtext_minsize = 12 ,
        #uniformtext_mode = 'hide',
        
            xaxis= dict(
                    #tickformat="%b\n%Y",
                    #ticklabelmode="period"
                    # dtick= 500000,
                    ticks = "outside",
                    tickwidth = 1,
                    tickcolor = color,
                    ticklen = 8,
                    tickfont = dict(family = 'Arial', size = 14),
                    showline = True,
                    linewidth = 1,
                    linecolor = color,
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
                    tickcolor = color,
                    ticklen = 8,
                    tickfont = dict(family = 'Arial', size = 14),
                    showline = True,
                    linewidth = 1,
                    linecolor = color,
                    zeroline = False,
                    showgrid = False,
                    ),
            uniformtext_minsize=8, uniformtext_mode='hide',   
            transition_duration=500)
        return self.fig_bubblechart







