import plotly.graph_objects as go
import plotly
import chart_studio
import chart_studio.plotly as py


t_c=data.iloc[0,1]
t_a=data.iloc[0,4]
t_r=data.iloc[0,2]
t_d=data.iloc[0,3]

fig=go.Figure()

fig.add_trace(go.Indicator(
    mode = "number",
    value = t_c,
    title="Confirmed",
    domain = {'row': 0, 'column': 1}))

fig.update_layout(
    margin=dict(l=20, r=20, t=20, b=20))

unique_url = py.plot(fig, filename="C-Indicator")



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

data= pd.read_csv("F:\\semester 8\\Advanced Analytics\\package\\state_wise.csv")
data.head()
data=data[data.columns[:6]]
s_data=data.drop(data.index[0])

fig = go.Figure(data=[go.Table(
    header=dict(values=list(s_data.columns[:4]),
                fill_color='tomato',
                align='left'),
    cells=dict(values=[s_data.State, s_data.Confirmed, s_data.Recovered, s_data.Deaths],
               fill_color='rgb(255, 200, 200)',
               align='left'))
])

unique_url = py.plot(fig, filename="State_Data")