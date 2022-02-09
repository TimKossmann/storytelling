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
        self.mark_bar = None
        self.type = "Abteilung"

    def get_fail_df(self):
        res = self.fail_df.copy()
        res["Fehlerquote (%)"] = (res["Fehlerquote (%)"]*100).round()        
        return res
    
    def get_lia_df(self):
        data = {
            "Phishing Absichten": ["Link aufrufen", "Daten eingeben", "Anhang öffnen"],
            "Häufigkeit (%)": [68, 23, 9]
        }
        return pd.DataFrame(data)
    
    def get_dropdown_list(self, type):
        res = []
        df = self.fail_df[self.fail_df["Art"] == type]
        df = df.sort_values('Name')
        #df.reset_index(drop=True, inplace=True)

        for index, row in df.iterrows():
            print(row["Name"])
            res.append({"label": row["Name"], "value": row["Name"]})
        return res

    def update_mark_bar(self, mark_name):
        print("MARK NAME: ", mark_name)
        if (mark_name != ""):
            self.mark_bar = mark_name
        

    def update_type(self, type):
        self.mark_bar = None
        self.type = type
    
    def get_fail_bar(self, type_name, mark, darkmode=True):
        if darkmode:
            color = "white"
            avg_line_color = "rgba(255,255,255,0.7)"
        else:
            color = "black" 
            avg_line_color = "rgb(32, 59, 85)"
        df = self.fail_df[self.fail_df["Art"] == type_name]
        df["Fehlerquote (%)"] = (df["Fehlerquote (%)"]*100).round()
        df["Name"] = df["Name"].str.replace(" und ", "& ")
        df["Name"] = df["Name"].str.replace(" ", "<br>")
        df["Name"] = df["Name"].str.replace("&", " &")
        df["Name"] = df["Name"].str.replace("/", "/<br>")
        df.reset_index(drop=True, inplace=True)
        color_map = {}
        for index, row in df.iterrows():
            if row["Name"] == mark:
                color_map[row["Name"]] = 'rgb(159, 90, 253)'
            else:
                color_map[row["Name"]] = 'rgb(32, 59, 85)'
        fig = px.bar(
            df, 
            x="Fehlerquote (%)", 
            y="Name", 
            color='Name', 
            text=[f'{i} %' for i in df['Fehlerquote (%)']], 
            color_discrete_map = color_map,
            
        )
        fig.update_layout(
            title={
                'text': "Fehlerquote im Umgang mit Phishing Mails nach " + type_name,
                'y':0.97,
                'x':0.0,
                'xref': "paper",
                'xanchor': 'left',
                'yanchor': 'top'},
            plot_bgcolor = "rgba(0,0,0,0)",
            paper_bgcolor = "rgba(0,0,0,0)",
            font_color="white"
        )
        fig.update_xaxes(
            showgrid=False,
            ticks = "outside",
            tickwidth = 1,
            tickcolor = color,
            ticklen = 8,
            showline = True,
            linewidth = 1,
            linecolor = color,
            )
        fig.update_yaxes(
            title="",
            showgrid=False,
            ticks = "outside",
            tickwidth = 1,
            tickcolor = "rgba(0, 0, 0, 0)",
            ticklen = 8,
            showline = True,
            linecolor = 'rgba(0, 0, 0, 0)',)
        fig.update_layout(
            height=700,)
        fig.update_layout(
            plot_bgcolor= 'rgba(0, 0, 0, 0)',
            paper_bgcolor= 'rgba(0, 0, 0, 0)',
            showlegend = False,
            font_color=color,
        )
        fig.update_traces(marker_line_width = 0,
                  selector=dict(type="bar"))
        mean = df['Fehlerquote (%)'].mean()
        fig.add_vline(x=mean, line_dash="dot",
              annotation_text=("Mittelwert der Fehlerquote (" +  str(mean) + "%)" ), 
              annotation_position="top",
              annotation_font_size=14,
              annotation_font_color= color,
            line_color=avg_line_color

             )
        return fig

    def get_text_for_dounut(self, dounut_type):
        text_dounut = {
            "link": "68% der Phishing Mails sollen den Nutzer <br> dazu Veranlassen einen Link zu öffnen",
            "input": "Bei 23% der Phishing Mails sollen der Nutzer <br> sensible Daten angeben",
            "attach": "9% aller Phishing Mails zielen darauf ab, den <br> Nutzer den Anhang öffnen zu lassen"
        }
        return text_dounut[dounut_type]

    def get_link_donut(self, darkmode=True, show_text=True):
        fig = px.pie({"link/no_link": ["Link", "No"], "value": [self.link, 100-self.link]}, names="link/no_link", values="value", hole=0.7, color="link/no_link", 
        color_discrete_map={"Link": 'rgb(62, 175, 182)', "No": 'rgb(57, 81, 104)'})
        text = ""
        if show_text:
            text = self.get_text_for_dounut("link")
        return self.update_donut_fig(fig, "E269", "Link aufrufen", darkmode, text)
    
    def get_input_donut(self, darkmode=True, show_text=True):
        fig = px.pie({"input/no_input": ["Input", "No"], "value": [self.input, 100-self.input]}, names="input/no_input", values="value", hole=0.7, color="input/no_input", 
        color_discrete_map={"Input": 'rgb(62, 175, 182)', "No": 'rgb(57, 81, 104)'})
        text = ""
        if show_text:
            text = self.get_text_for_dounut("input")
        return self.update_donut_fig(fig, "2328_color", "Daten eingeben", darkmode, text)
    
    def get_attach_donut(self, darkmode=True, show_text=True):
        fig = px.pie({"attach/no_attach": ["Attach", "No"], "value": [self.attach, 100-self.attach]}, names="attach/no_attach", values="value", hole=0.7, color="attach/no_attach", 
        color_discrete_map={"Attach": 'rgb(62, 175, 182)', "No": 'rgb(57, 81, 104)'})
        text = ""
        if show_text:
            text = self.get_text_for_dounut("attach")
        return self.update_donut_fig(fig, "1F4CE", "Anhang öffnen", darkmode, text)

    def update_donut_fig(self, fig, img_name, txt, darkmode, expl_txt="" ):
        if darkmode:
            color = 'white'
            img = Image.open(f'./assets/{img_name}.png')
        else:
            color = 'black'
            img = Image.open(f'./assets/{img_name}_black.png')

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
            font_size=18,
            font_color=color
        )
        fig.add_annotation(
            text=expl_txt, 
            xref="paper", 
            yref="paper",
            x=0.5, y=0.0,
            showarrow=False,
            font_size=16,
            font_color=color
        )
        fig.update_traces(textinfo='none', sort=False)
        fig.layout.update(showlegend=False, plot_bgcolor= 'rgba(0, 0, 0, 0)',
            paper_bgcolor= 'rgba(0, 0, 0, 0)',)
        return fig


if __name__ == '__main__':
    pg = Phishing_Graphs()
    #pg.get_link_donut()
    #pg.get_input_donut()
    #pg.get_attach_donut()
    pg.get_fail_bar("Abteilung")