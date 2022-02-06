from dash import dcc, html, Input, Output
import dash
import re

from passwords_wordcloud import Chart_WordCloud

class PasswordPage():
    def __init__(self, app):
        self.app = app
        self.wc = Chart_WordCloud()
        self.kinds = []
        self.years = 0
        self.months = 0
        self.weeks = 0
        self.days = 0
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def check_sc(self, pw):
        special_charachters = "!'#$%&()*+,-./:;<>=?@[\]^_-`{|}~"
        special_charachters += '"'
        for c in pw:
            if c in special_charachters:
                return True
        return False
    
    def get_excel_df(self):
        res = self.wc.df.copy()
        res.drop('size', inplace=True, axis=1)
        res.drop('note', inplace=True, axis=1)
        res = res.rename(
            columns={
                'Password': 'Passwort', 
                'category': 'Kategorie', 
                'rank': 'Platz', })
        return res.to_excel

    def calculate_pw_strength(self, pw):
        if (pw == ""):
            return
        
        pw_per_second = 100000000000

        possibles = 0

        seconds_in_year = 60 * 60 * 24 * 365
        seconds_in_week = 60 * 60 * 24 * 7
        seconds_in_month = 60 * 60 * 24 * 30

        seconds_in_day = 60 * 60 * 24
        seconds_in_hour = 60 * 60
        seconds_in_minute = 60

        self.kinds = []

        if re.search(r'\d', pw):
            self.kinds.append("digits") 
            possibles += 10
        if re.search('[a-z]+', pw):

            self.kinds.append("lowercase") 
            possibles += 26
        if re.search('[A-Z]+', pw):
            self.kinds.append("uppercase") 
            possibles += 26
        if self.check_sc(pw):
            self.kinds.append("special") 
            possibles += 32
        self.seconds = (possibles**len(pw))/pw_per_second
        #seconds = seconds_in_year + seconds_in_month + seconds_in_week + seconds_in_day + seconds_in_hour + seconds_in_minute + 1
        self.years = self.seconds // seconds_in_year
        self.months = (self.seconds - (self.years * seconds_in_year)) // seconds_in_month
        self.weeks = (self.seconds - (self.years * seconds_in_year) - (self.months * seconds_in_month)) // seconds_in_week
        self.days = (self.seconds- (self.years * seconds_in_year) - (self.months * seconds_in_month) - (self.weeks * seconds_in_week)) // seconds_in_day
        self.hours = (self.seconds - (self.years * seconds_in_year) - (self.months * seconds_in_month) - (self.weeks * seconds_in_week) - (self.days * seconds_in_day)) // seconds_in_hour
        self.minutes = (self.seconds - (self.years * seconds_in_year) - (self.months * seconds_in_month) - (self.weeks * seconds_in_week) - (self.days * seconds_in_day) - (self.hours * seconds_in_hour)) // seconds_in_minute
        self.seconds = self.seconds - (self.years * seconds_in_year) - (self.months * seconds_in_month) - (self.weeks * seconds_in_week) - (self.days * seconds_in_day) - (self.hours * seconds_in_hour) - (self.minutes * seconds_in_minute)
        if self.years > 1000000000000:
            self.years = "∞"
            self.months = 0 
            self.weeks = 0 
            self.days = 0 
            self.hours = 0 
            self.minutes = 0
            self.seconds = 0

    def get_pw_analyse(self, pw):
        self.calculate_pw_strength(pw)
        d_text = "Nein"
        lc_text = "Nein"
        uc_text = "Nein"
        sc_text = "Nein"
        for kind in self.kinds:
            if kind == "digits":
                d_text = "Ja"
            if kind == "lowercase":
                lc_text = "Ja"
            if kind == "uppercase":
                uc_text = "Ja"
            if kind == "special":
                sc_text = "Ja"
        return html.Div(
            id="analyse-container",
            children=
            [
            html.Br(),
            html.Div(["Zahlen: ", html.B([d_text])]),
            html.Div(["Kleinbuchstaben: ", html.B([lc_text])]),
            html.Div(["Großbuchstaben: ", html.B([uc_text])]),
            html.Div(["Sonderzeichen: ", html.B([sc_text])]),
            html.Br(),
            html.Br(),
            html.Div(
                id="time-to-crack-minutes",
                children=[
                    html.Div(className="time-day",children=["Stunden: " + str(self.hours)]),
                    html.Div(className="time-day",children=["Minuten: " + str(self.minutes)]),
                    html.Div(className="time-day",children=["Sekunden: " + ("%.4f" % self.seconds)]),
                ]
            ),
            html.Br(),
            html.Br(),

            html.Div(
                id="time-to-crack",
                children=[
                    html.Div(className="time",children=["Jahre: " + str(self.years)]),
                    html.Div(className="time",children=["Monate: " + str(self.months)]),
                    html.Div(className="time",children=["Wochen: " + str(self.weeks)]),
                    html.Div(className="time",children=["Tage: " + str(self.days)]),
                ]
            ),
            
            ]
        )


    def get_layout(self):
        return html.Div(
                id="password-wrapper",
                className="wrapper",
                children=[
                    html.Div(
                        id="left-side",
                        children=[
                            html.H3(id="wordcloud-header", children="Die meist verwendeten Passwörter"),
                            html.Br(),
                            html.Img(className="img", id='wordcloud'),
                        ]
                    ),
                    html.Div(
                        id="right-side",
                        children=[
                            html.H3("Gib dein Passwort hier ein um zu sehen, wie lange ein Computer braucht es zu knacken"),
                            html.Br(),
                            html.H4("Dein Passwort:"),
                            html.Div([
                                dcc.Input(id='my-input', value='', type='text')
                            ]),
                            html.Div(
                                id="pw-analyse"
                            ),
                            
                        ]
                    ),
                    html.Div(
                        className="download-wrapper",
                        children=
                        [
                            html.Button("Daten herunterladen", className="btn_csv", id="password_btn"),
                            dcc.Download(id="download-password-excel"),
                        ]
                    )        
                ]
            )
    


        
    
    
    

