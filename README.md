# Covid-19-Dashboard

COVID-19 TRACKER INDIA:
The Corona virus datasets ( state_wise, state_wise_daily, time_series) has been used to plot the different data plots. The Dashboard API (Python) by Plotly has been used to create the dashboard and create plots. SARIMA from statsmodels api (python) was used to forecast the covid-19 cases. And kaplan meier survival analysis was done on the data based on deceased people in the timeline and the survival probability has been plotted. India states shape file was used using geopandas in python to plot a choropleth map of India by the total confirmed state wise cases.

PLOTS.py- different plots plotted in python. (Pie chart, Choropleth map of India, Confirmed recovered deceased and active multiplot, State wise covid cases plot.)

Forecast.py- Forecasting Covid cases and  plot using SARIMA.

Model.py – Kaplan meier survival probability calculation and ploting.

Indicator and Table.py- Forming Indicators and displaying data in  plotly dashboard using API.

Dashboard.ipynb – Plotting Pie chart, Confirmed recovered deceased and active multiplot, State wise covid cases plot, kmf plot, displaying data and creating layout for dashboard and formatting using plotly dashboard API online.

Choropleth Plotly.ipynb- Getting Geopandas data of INDIA STATE and creating a choropleth map in plotly dashboard online API using the confirmed  state wise cases in India.

Thankyou,

Dashboard link:  https://plotly.com/~apeaksa2208/0/covid-19-tracker-india/

