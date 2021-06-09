# -*- coding: utf-8 -*-
#Graffiti-Analysis Project
#Trying to find out whether there was an increase, decrease or no change in 
#Graffiti from 2019 to 2020.

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import matplotlib.pyplot as plt
import numpy as np

url = "/Users/richardjohn/Desktop/Graffiti-Analysis-Project/Graffiti-Analysis(Pandas)/DSNY_Graffiti_Tracking.csv"
df = pd.read_csv(url)

#print(df.info())

zips = df[["ZIP_CODE"]].value_counts()

#date = df.groupby("CREATED_DATE") #Worthless
dates = df[["CREATED_DATE"]].value_counts(sort = False)

sliced_dates = dates.iloc[0:365:2]

sliced_dates.to_frame()

# Manually finding the number of incidents per month 
Jan_2019 = df.iloc[1:2280]
Feb = df.iloc[2281:3904]
Mar = df.iloc[3905:5670]
Apr = df.iloc[5671:7535]
May = df.iloc[7536:9303]
Jun = df.iloc[9304:11686]
Jul = df.iloc[11687:13100]
Aug = df.iloc[13101:13968]
Sep = df.iloc[13696:14593]
Oct = df.iloc[14594:16228]
Nov = df.iloc[16229:17095]
Dec = df.iloc[17096:21294]
Jan_2020 = df.iloc[21295: 22141]


#print(sliced_dates)


x_ax = ["Jan '19", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan '20"]
vals = [len(Jan_2019), len(Feb), len(Mar), len(Apr), len(May), len(Jun), len(Jul), len(Aug), len(Sep), len(Oct), len(Nov), len(Dec), len(Jan_2020)]

fig = plt.figure()
ax = fig.add_axes([0, 0, 1.2, 1.2])
ax.bar(x_ax, vals)
ax.set_title("Graffiti Incidents Jan 2019 - Jan 2020")
ax.set_xlabel("Months")
ax.set_ylabel("Number of Incidents")
plt.show()

#It worked. 
'''
ax1 = plt.axes()
ax1.yaxis.set_label_text('Number of Incidents')
ax1.axes.get_xaxis().set_visible(False)
ax1.xaxis.set_label_text('Jan 2019 - Jan 2020')
#ax1.xaxis.label.set_label(x_ax) #Didnt work :(. Yet :)
ax1.xaxis.label.set_visible(True)
#ax1.set_xlabels(['two', 'four','six', 'eight', 'ten'])
plt.title("Graffiti Incidents Jan 2019 - Jan 2020")
axs = sliced_dates.plot()
'''

'''
def slicedDatesGraph():
    ax1 = plt.axes()
    ax1.yaxis.set_label_text('Number of Incidents')
    ax1.axes.get_xaxis().set_visible(False)
    ax1.xaxis.set_label_text('Jan 2019 - Jan 2020')
    #ax1.xaxis.label.set_label(x_ax) #Didnt work :(. Yet :)
    ax1.xaxis.label.set_visible(True)
    #ax1.set_xlabels(['two', 'four','six', 'eight', 'ten'])
    plt.title("Graffiti Incidents Jan 2019 - Jan 2020")
    axs = sliced_dates.plot()
'''

#boroughs = df.groupby("BOROUGH")
Borough = df[['BOROUGH']].value_counts()

#print(dates)

'''
#For User input
switch_bar = int(input("Enter which graph would you like to see\n1. Zipcodes\n2. Dates\n3. Boroughs\n0. Exit\nEnter what you want to do: "))

def graphDisplay(choice):
    switcher = { 
        1: zips[:15].plot(kind = 'barh'), #The 15 most vandalized Zipcodes
        2: slicedDatesGraph(),
        3: Borough.plot(kind = 'barh'),
        0: print("Goodbye.")
    }

graphDisplay(switch_bar)
'''

'''
Bar Graphs
'''

#zips[:15].plot(kind = 'barh') #The 15 most vandalized Zipcodes
#dates[:10].plot()#The top 10 days of the years (2019-2020) of when vandalized occurred the most.
#Borough.plot(kind = 'barh') #The total number of vandalism in each borough.


'''
Line Graphs
'''

#dates.plot()

#print(zipc, "\n") #The amount of graffiti tags in each zipcode.
#print(dates, "\n") #The amount of graffiti tags that occurred on a specific day.
#print(Borough, "\n") #The amount of graffiti tags in each borough. 