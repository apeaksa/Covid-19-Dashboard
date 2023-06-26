import plotly.offline as py
from PIL import Image
import numpy as np
import plotly.graph_objs as go
import plotly.tools as tls
import matplotlib.pyplot as plt

Img=Image.open('F:\semester 8\Advanced Analytics\package\plot.jpg')
im=np.array(Img)
im.size

from lifelines import KaplanMeierFitter


time_data=pd.read_csv("F:\\semester 8\\Advanced Analytics\\package\\case_time_series.csv")
time_data.head()
time_data.columns

time_data['Time']=list(range(len(time_data['Date'])))


kmf = KaplanMeierFitter() 
kmf.fit(durations =time_data['Time'],  event_observed = time_data['Total Deceased'])
kmf.survival_function_
kmf.cumulative_density_
kmf.plot()

c_data=time_data.drop(columns=['Date'])
from lifelines import CoxPHFitter
f=plt.Figure()
cph = CoxPHFitter()   
cph.fit(c_data ,'Time' , event_col='Total Deceased')  
cph.print_summary()    
cph.plot()
