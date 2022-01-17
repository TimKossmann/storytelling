from turtle import position
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image 
import pandas as pd




class Phishing_Graphs():

    def __init__(self):
        self.link = 68
        self.input = 23
        self.attach = 9
        self.fail_df = pd.read_excel("./datasets/PhishingFail.xlsx")
    
    def get_fail_bar(self, type):
        df = self.fail_df[self.fail_df["Art"] == type]
        fig = px.bar(df, x="Fehlerquote", y="Name")
        fig.update_layout(bargap=0.5)

        fig.show()
    
    def get_fail_bar_go(self, type):
        df = self.fail_df[self.fail_df["Art"] == type]
        print(df.head())
        fig = go.Figure(
            [go.Bar(
                x=df["Fehlerquote"], 
                y=df["Name"],
                orientation='h'
            )]
        )
        fig.update_layout(
            yaxis=dict(
                title=type,
            ),
        )
        fig.update_yaxes() 
        fig.show()

    def get_link_donut(self):
        img = Image.open('./assets/E269_black.png')
        fig = px.pie({"link/no_link": ["Link", "No"], "value": [self.link, 100-self.link]}, names="link/no_link", values="value", hole=0.7, color="link/no_link", 
        color_discrete_map={"Link": 'rgb(22, 160, 133)', "No": 'rgb(236, 236, 236)'})
        return self.update_donut_fig(fig, img, "Link aufrufen")
    
    def get_input_donut(self):
        img = Image.open('./assets/2328_color.png')
        fig = px.pie({"input/no_input": ["Input", "No"], "value": [self.input, 100-self.input]}, names="input/no_input", values="value", hole=0.7, color="input/no_input", 
        color_discrete_map={"Input": 'rgb(134, 55, 114)', "No": 'rgb(236, 236, 236)'})
        return self.update_donut_fig(fig, img, "Daten eingeben")
    
    def get_attach_donut(self):
        img = Image.open('./assets/2709_black.png')
        fig = px.pie({"attach/no_attach": ["Attach", "No"], "value": [self.attach, 100-self.attach]}, names="attach/no_attach", values="value", hole=0.7, color="attach/no_attach", 
        color_discrete_map={"Attach": 'rgb(205, 143, 90)', "No": 'rgb(236, 236, 236)'})
        return self.update_donut_fig(fig, img, "Anhang öffnen")

    def update_donut_fig(self, fig, img, txt):
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
            text=txt, 
            xref="paper", 
            yref="paper",
            x=0.5, y=0.45,
            showarrow=False,
            font_size=24
        )
        fig.update_traces(textinfo='none', sort=False)
        fig.layout.update(showlegend=False)
        return fig


if __name__ == '__main__':
    pg = Phishing_Graphs()
    #pg.get_link_donut()
    #pg.get_input_donut()
    #pg.get_attach_donut()
    pg.get_fail_bar_go("Abteilung")