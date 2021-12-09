import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import datetime

import pandas as pd

df = pd.read_excel("./datasets/DataBreaches.xlsx")


def front(self, n):
    return self.iloc[:, :n]

pd.DataFrame.front=front
df = df.drop(df.index[[0]])
df = df.rename(columns= {'year   ':'year'})
df["records lost"] = pd.to_numeric(df["records lost"])
df["organisation"] = df["organisation"].astype("string")
df["year"] = pd.to_numeric(df["year"])


app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])




@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'))
def update_figure(selected_year):


    fig = px.scatter(df[(df['year'] == selected_year)], x="records lost", y="date", 
                size="records lost", color="organisation",
                    hover_name="organisation", log_x=True, size_max=60)
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)