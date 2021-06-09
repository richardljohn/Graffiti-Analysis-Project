# -*- coding: utf-8 -*-
#Graffiti-Analysis Project
#Trying to find out whether there was an increase, decrease or no change in 
#Graffiti from 2019 to 2020.

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

url = "/Users/richardjohn/Desktop/Graffiti-Analysis-Project/Graffiti-Analysis(Pandas)/DSNY_Graffiti_Tracking.csv"
df = pd.read_csv(url)

zips = df[["ZIP_CODE"]].value_counts()

dates = df[["CREATED_DATE"]].value_counts(sort = False)

Borough = df[['BOROUGH']].value_counts()

# Manually finding the number of incidents per month 
Jan_2019 = df.iloc[0:2280]
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

def plotMonthlyIncidents():
    x_ax = ["Jan 2019", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan 2020"]
    vals = [len(Jan_2019), len(Feb), len(Mar), len(Apr), len(May), len(Jun), len(Jul), len(Aug), len(Sep), len(Oct), len(Nov), len(Dec), len(Jan_2020)]
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1.2, 1.2])
    ax.bar(x_ax, vals)
    ax.set_title("Graffiti Incidents Jan 2019 - Jan 2020")
    ax.set_xlabel("Months")
    ax.set_ylabel("Number of Incidents")
    plt.show()

def graphDisplayMenu(choice):
    if(choice == 0):
        print("Goodbye.")
    elif(choice == 1):
        zips[:15].plot(kind = 'barh') #The 15 most vandalized Zipcodes
    elif(choice == 2):
        plotMonthlyIncidents()
    elif(choice == 3):
        Borough.plot(kind = 'barh')

'''
user = int(input("Enter a number: "))

def graphDisplayMenu(choice):
    if(choice == 1):
        print("1")
    if(choice == 2):
        print("2")
    if(choice == 3):
        print(3)
'''
    
#For user input
#graphDisplayMenu(user)
switch_bar = int(input("Enter which graph would you like to see\n1. Most Vandalized Zipcodes in NYC\n2. Monthly Incidents\n3. Number of Vandalisms per Borough\n0. Exit\nEnter what you want to do: "))
graphDisplayMenu(switch_bar)