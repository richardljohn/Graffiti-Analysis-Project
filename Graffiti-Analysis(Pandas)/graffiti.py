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

#print(sliced_dates)

#ax1.set_frame_on(False)

x_ax = ["Jan 2019", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan 2020"]

#It worked. 
ax1 = plt.axes()
ax1.yaxis.set_label_text('Number of Incidents')
ax1.axes.get_xaxis().set_visible(False)
ax1.xaxis.set_label_text('Jan 2019 - Jan 2020')
#ax1.xaxis.label.set_label(x_ax) #Didnt work :(. Yet :)
ax1.xaxis.label.set_visible(True)
#ax1.set_xlabels(['two', 'four','six', 'eight', 'ten'])

plt.title("Graffiti Incidents Jan 2019 - Jan 2020")

axs = sliced_dates.plot()


#boroughs = df.groupby("BOROUGH")
Borough = df[['BOROUGH']].value_counts()

#print(dates)


#For User input
#switch_bar = int(input("Enter which graph would you like to see\n1. Zipcodes\n2. Dates\n3.Boroughs\n0. Nothing\nSelect "))

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