import pandas as pd
import plotly.express as px
 
df = pd.read_csv("covid_scatter.csv")
fig = px.scatter(df, x="Country", y="cases",
size = "Percentage", color = "country",
size_max=60)
 
fig.show()
