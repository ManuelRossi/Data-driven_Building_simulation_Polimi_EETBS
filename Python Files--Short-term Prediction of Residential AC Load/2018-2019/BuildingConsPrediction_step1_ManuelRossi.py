# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os 
# importing the external files
ExternalFilesFolder = r"C:\Users\Famiglia\Documents\Manuel\Polimi\MAGISTRALE\PRIMO ANNO\Primo semestre\Bezhad\python4ScientificComputing_Numpy_Pandas_MATPLotLIB\ExternalFiles"
ConsumptionFileName= "consumption_5545.csv"
TemperatureFileName= "Austin_weather_2014.csv"
IrradianceFileName= "irradiance_2014_gen.csv"

path_consumptionFile = os.path.join(ExternalFilesFolder,ConsumptionFileName)
path_TemperatureFile = os.path.join(ExternalFilesFolder,TemperatureFileName)
path_IrradianceFile = os.path.join(ExternalFilesFolder,IrradianceFileName)

DF_consumption = pd.read_csv(path_consumptionFile,sep=",", index_col=0)
DF_consumption.head()
DF_consumption.tail(10)

PreviousIndex = DF_consumption.index
NewParsedIndex= pd.to_datetime(PreviousIndex)
DF_consumption.index =NewParsedIndex 

DF_consumption.head()
DF_consumption.index.hour
DF_consumption.index.month
DF_consumption.index.dayofweek

DF_consumption_someDaysInJuly=DF_consumption["2014-07-01 00:00:00":"2014-07-03 23:00:00"]

plt.figure()
plt.plot(DF_consumption_someDaysInJuly)
plt.xlabel("Time")
plt.ylabel("AC Power (W)")
plt.show()

# There is asecond way of doing this !!!
plt.figure()
DF_consumption_someDaysInJuly.plot()
plt.xlabel("Time")
plt.ylabel("AC Power (W)")
plt.show()

#This is better !!

# LEt's import the weather data 

DF_weather = pd.read_csv(path_TemperatureFile,sep=";",index_col=0)
DF_weather.head(24)
previousIndex_weather=DF_weather.index
newIndex_weather=pd.to_datetime(previousIndex_weather)
DF_weather.index = newIndex_weather
DF_weather.columns
Series_Temperature = DF_weather["temperature"]

DF_Temperature= DF_weather[["temperature"]]
DF_Temperature.head()


DF_irradianceSource = pd.read_csv(path_IrradianceFile,sep=";",index_col=1)
DF_irradianceSource.head(24)

DF_irradiance=DF_irradianceSource[["gen"]]
DF_irradiance.head(24)

DF_irradiance["gen"]<0
DF_irradiance[DF_irradiance["gen"]<0] = 0
DF_irradiance.head(24)

DF_joined = DF_consumption.join([DF_Temperature,DF_irradiance])
DF_joined.head(24)

DF_joined_cleaned = DF_joined.dropna()
DF_joined_cleaned.head(24)

DF_joined_cleaned_chosenDates=DF_joined_cleaned["2014-08-01":"2014-08-02"]
DF_joined_cleaned_chosenDates.head(24)

DF_joined_cleaned_chosenDates.describe()



DF_joined_cleaned_chosenDates_min = DF_joined_cleaned_chosenDates.min()
DF_joined_cleaned_chosenDates_max = DF_joined_cleaned_chosenDates.max()
DF_joined_cleaned_chosenDates_Nornamlized=(DF_joined_cleaned_chosenDates-DF_joined_cleaned_chosenDates_min)/(DF_joined_cleaned_chosenDates_max-DF_joined_cleaned_chosenDates_min)
DF_joined_cleaned_chosenDates_Nornamlized.plot()

DF_joined_cleaned_chosenDates.to_csv("MyDataFrame.csv",sep=";")

df_lagged=DF_joined_cleaned_chosenDates.copy()
df_lagged["Temperature-1h"]=df_lagged["temperature"].shift(1)

#Renaming the column name before applying the function
#First way
DF_mod.columns=["AC_consumption","Temperature","Irradiance" ]

#Second way
DF_mod=DF_mod.rename(columns={"air_conditioner_5545":"AC_consumption","temperature":"Temperature","gen":"Irradiance"})
