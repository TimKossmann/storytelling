from dash import dcc, html, Input, Output
import dash

from passwords_wordcloud import Chart_WordCloud

class PasswordPage():
    def __init__(self, app):
        self.app = app
        self.wc = Chart_WordCloud()

    def get_layout(self):
        
        return html.Div(
                id="password-wrapper",
                className="wrapper",
                children=[
                    html.Div(
                        id="left-side",
                        children=[
                            html.H3(id="wordcloud-header", children="Most common Passwords"),
                            html.Img(className="img", id='wordcloud'),
                        ]
                    ),
                    html.Div(
                        id="right-side",
                        children=[
                            html.H6("Gib dein Passwort ein und berechne wie lange ein moderner Computer braucht es zu knacken"),
                            html.Div([
                                dcc.Input(id='my-input', value='', type='text')
                            ]),
                            html.Div(id='hallo', children=html.H3(["hi"])),
                        ]
                    )         
                ]
            )
    


        
    
    
    

