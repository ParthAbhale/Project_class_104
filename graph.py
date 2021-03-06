import plotly.express as px
import pandas as pd

data = pd.read_csv("data.csv")

graph = px.scatter(data,x="date",y="cases",color="country")

graph.show()