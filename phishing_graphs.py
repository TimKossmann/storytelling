from numpy.core.fromnumeric import size
import plotly.express as px
from PIL import Image 

import dash
import pandas as pd 
import numpy as np
import random
import datetime

class Phishing_Graphs():

    def __init__(self):
        self.link = 68
        self.input = 23
        self.attach = 9
    
    def get_link_donut(self):
        img = Image.open('./assets/E269_black.png')
        fig = px.pie({"link/no_link": ["Link", "No"], "value": [self.link, 100-self.link]}, names="link/no_link", values="value", hole=0.7, color="link/no_link", 
        color_discrete_map={"Link": 'rgb(22, 160, 133)', "No": 'rgb(236, 236, 236)'})
        fig.add_layout_image(
            dict(
                source=img,
                xref="paper", yref="paper",
                x=0.5, y=0.6,
                sizex=0.3, sizey=0.3,
                xanchor="center", yanchor="middle"
            )
        )
        fig.add_annotation(
            text="Link", 
            xref="paper", 
            yref="paper",
            x=0.5, y=0.5,
            size=28,
            showarrow=False
        )
        fig.update_traces(textinfo='none')
        fig.layout.update(showlegend=False)
        fig.show()


if __name__ == '__main__':
    pg = Phishing_Graphs()
    pg.get_link_donut()