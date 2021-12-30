from dash import dcc, html, Input, Output
import dash

from passwords_wordcloud import Chart_WordCloud

class PasswordPage():
    def __init__(self, app):
        self.app = app
        self.wc = Chart_WordCloud()

    def get_layout(self): 
        @self.app.callback(
            dash.dependencies.Output('wordcloud', 'src'),
            Input('wordcloud', 'img')
        )
        def make_wordlcloud(img):
            return self.wc.create_wordcloud()
        
        @self.app.callback(
            dash.dependencies.Output('hallo', 'children'),
            Input('my-input', 'value')
        )
        def update_output_div(input_value):
            return "Output: "#{}".format(input_value)

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
                            html.H6("Change the value in the text box to see callbacks in action!"),
                            html.Div([
                                "Input: ",
                                dcc.Input(id='my-input', value='hallo', type='text')
                            ]),
                            html.Div(id='hallo'),
                        ]
                    )         
                ]
            )
    


        
    
    
    

