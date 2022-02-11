import plotly.express as px
import plotly.graph_objects as go
import dash
import pandas as pd 
import numpy as np
import random
import datetime
import json

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output




df = pd.read_excel("./datasets/DataBreaches_initialAttackVectors.xlsx")



# Löschen der zweiten Zeile
df = df.drop(df.index[[0]])


df.dtypes
# Umwandlung des Datentyps von average total costs von Object in numeric
df["average total costs"] = pd.to_numeric(df["average total costs"])
df.dtypes


fig = px.treemap(df,  path=[px.Constant("all"), 'Attack vector'], values='frenquency of data breaches', hover_name= 'average total costs',
                
                  
                  )


fig.update_layout(clickmode='event+select')
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.update_traces(root_color="lightgrey")


app = dash.Dash(__name__)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}

app.layout = html.Div([

    html.Div(children=[
    
        html.Div([
            dcc.Markdown("""
                **Click Data**

                Click on points in the graph.
            """),
            html.Pre(id='click-data', style=styles['pre']),
        ]),
       dcc.Graph(
        id='basic-interactions', 
        figure = fig
        
    ),
    ]),

    

    
])





@app.callback(
    Output('basic-interactions', 'figure'),
    Input('basic-interactions', 'clickData'))
def display_click_data(clickData):
    
    
    """if clickData != None:

        fig.add_annotation(x=0.5,y=0.5,

                    text="entstandener Schaden (in US$)", #textangle=-90,
                        xref="paper",
                        yref="paper",
                        valign="top",
        showarrow=False)

    print (clickData)"""
    #return fig




if __name__ == '__main__':
    app.run_server(debug=True)