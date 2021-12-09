import plotly.express as px
import dash
import pandas as pd 

df = pd.read_excel("./datasets/DataBreaches.xlsx")

print(df.head())

fig = px.scatter(df, x="organisation", y="year",
	         size="records lost", color="continent",
                 hover_name="organisation", log_x=True, size_max=60)

fig.show()