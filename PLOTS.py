import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from lifelines import KaplanMeierFitter
import geopandas as gpd
#import matplotlib.dates as mdates
#from matplotlib.dates import DateFormatter
#from datetime import datetime
import matplotlib.ticker as plticker

data= pd.read_csv("F:\\semester 8\\Advanced Analytics\\package\\state_wise.csv")
data.head()
data=data[data.columns[:6]]


#bar chart
sns.set_style("ticks")
plt.figure(figsize = (10,10))
plt.barh(data["State"], data["Confirmed"],align = 'center', color = 'red', edgecolor = 'darkred')
plt.xlabel('No. of Confirmed cases', fontsize = 14)
plt.ylabel('State', fontsize = 14)
plt.gca().invert_yaxis()
plt.xticks(fontsize = 12) 
plt.yticks(fontsize = 12)
plt.title('Total Confirmed Cases Statewise', fontsize = 16)
for index, value in enumerate(data["Confirmed"]):
    plt.text(value, index, str(value), fontsize = 12, verticalalignment = 'center')
plt.show()  

# Pie chart
group_size = [data['Active'][0], data['Recovered'][0], data['Deaths'][0]]
group_labels = ['Active\n' + str(group_size[0]), 
                'Recovered\n' + str(group_size[1]), 
                'Deceased\n'  + str(group_size[2])]
custom_colors = ['skyblue','lightgreen','red']
plt.figure(figsize = (5,5))
plt.pie(group_size, labels = group_labels, colors = custom_colors)
fig = plt.gcf()
plt.rc('font', size = 12) 
plt.title('Nationwide total Active, Recovered and Deceased Cases', fontsize = 16)
plt.show()

#time based line graph
time_data=pd.read_csv("F:\\semester 8\\Advanced Analytics\\package\\case_time_series.csv")
time_data.head()
time_data.columns

f=plt.figure()
ax = f.add_subplot(111)
ax.yaxis.tick_right()
ax.yaxis.set_label_position("right")

plt.plot(time_data['Date'], time_data['Total Confirmed'],color="red", label='Confirmed')
plt.plot(time_data['Date'], time_data['Total Recovered'],color="green",label='Recovered')
plt.plot(time_data['Date'], time_data['Total Active'],color="blue",label='Active')
plt.plot(time_data['Date'], time_data['Total Deceased'],color="black",label='Deceased')
loc = plticker.MultipleLocator(base=7.0) 
ax.xaxis.set_major_locator(loc)
plt.title('Covid cases in India')
plt.legend()
ax.set_ylabel('No. of cases')
plt.show()


# state wise projection of India in a GeoDataFrame 
map_data = gpd.read_file('F:\\semester 8\\Advanced Analytics\\package\\Indian_States.shp')
map_data.rename(columns = {'st_nm':'State'}, inplace = True)
map_data.head()

map_data['State'] = map_data['State'].str.replace('&', 'and')
map_data['State'].replace('Arunanchal Pradesh', 'Arunachal Pradesh', inplace = True)
map_data['State'].replace('Dadara and Nagar Havelli', 'Dadra and Nagar Haveli', inplace = True)
map_data['State'].replace('Andaman and Nicobar Island', 'Andaman and Nicobar Islands', inplace = True)
map_data['State'].replace('NCT of Delhi', 'Delhi', inplace = True)

m_data=data.drop(data.index[0])

merged_data = pd.merge(map_data, m_data, how = 'left', on = 'State')
merged_data.fillna(0, inplace = True)
#merged_data.drop('Sr.No', axis = 1, inplace = True)
merged_data.head()
fig, ax = plt.subplots(1, figsize=(20, 12))
ax.axis('off')
ax.set_title('Covid-19 State-wise Data - Confirmed Cases', fontdict = {'fontsize': '25', 'fontweight' : '3'})
merged_data.plot(column = 'Confirmed', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend = True)
plt.show()
