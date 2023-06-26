import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

time_data=pd.read_csv("F:\\semester 8\\Advanced Analytics\\package\\case_time_series.csv")
time_data.head()
time_data.columns

mod = sm.tsa.statespace.SARIMAX(time_data['Total Confirmed'],
                                order=(1, 1, 1),
                                seasonal_order=(0, 1, 1, 12),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

results = mod.fit()
forecast= results.predict(start=len(time_data['Total Confirmed']), end=len(confirmed)+10)
plt.plot(time_data['Total Confirmed'],label='Confirmed')
plt.plot(forecast,color='red',label='Forecasted')
plt.title('Covid-19 Cases in India')
plt.legend()
plt.xlabel('No. of Days')
plt.ylabel('No. of cases')
#plt.plot(results.fittedvalues, color='red')
plt.show()