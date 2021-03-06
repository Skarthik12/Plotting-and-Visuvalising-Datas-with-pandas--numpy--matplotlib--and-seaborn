

### Plotting and Visuvalising Datas with pandas, numpy, matplotlib, and seaborn ###


##pandas
##numpy
##matplotlib
##seaborn

##datasets (cars_sampled, fifateams)




### importing libraries ###

import pandas as pd
import numpy as np

### importing datasets ###
df_original = pd.read_csv("C:/Users/ELCOT/Downloads/cars_sampled.csv")

df_original.head()

df_original.shape


### bar plot ###

from matplotlib import pyplot as plt

x = df_original.iloc[:,:-1].values
x

y = df_original.iloc[:, -1].values
y

df_original['fuelType'].value_counts().head(10).plot.bar()

plt.legend()
plt.title("Bar Graph")
plt.xlabel("Type")
plt.ylabel("count")

df_original['vehicleType'].value_counts().sort_index().plot.bar()

plt.legend()
plt.title("Bar Graph2")
plt.xlabel("model")
plt.ylabel("count")

### Plot Price ###
df_original['price'].value_counts().sort_index().plot.line()

plt.legend()
plt.title("Plot graph")
plt.xlabel("price")
plt.ylabel("count")

df_original['yearOfRegistration'].value_counts().sort_index().plot.area()

plt.legend()
plt.title("Plot graph2")
plt.xlabel("price")
plt.ylabel("count")


### Scatter Plot ###
df_original.plot.scatter(x='seller', y='kilometer')

df_original.plot.hexbin(x='monthOfRegistration', y='price')


### Figsize argument ###
df_original['price'].value_counts().sort_index().plot.bar(
    figsize = (10,5),
    fontsize = 14,
    title = "Count of car prices")


#Adjusting title fontsize using Matplotlib
import matplotlib as mlt

ax = df_original['price'].value_counts().sort_index().plot.bar(
    figsize = (12,6),
    fontsize = 14
)
ax.set_title("Count the car-Price", fontsize = 20)
ax.set_xlabel("Price", fontsize = 20)
ax.set_ylabel("Count", fontsize = 20)


import matplotlib.pyplot as plt

###Creating a frame of rows and columns to place the plots ###
fig, axi = plt.subplots(3,1, figsize = (12,12))

#plot1
df_original['powerPS'].value_counts().plot.bar(
    ax = axi[0],
    fontsize = 14    
)
axi[0].set_title("powerps  of cars", fontsize = 20)

#Plot2
df_original['price'].value_counts().head(10).plot.bar(
    ax = axi[1],
    fontsize = 14
)
axi[1].set_title('price', fontsize = 20)

#plot3
df_original['kilometer'].value_counts().head().plot.bar(
    ax = axi[2],
    fontsize = 14)
axi[2].set_title("No of kilometers")

df_original.isnull().count()

### seaborn ###

###Exploring with seaborn package

import seaborn as sns

sns.countplot(df_original['monthOfRegistration'])

sns.countplot(df_original['powerPS'].head(20))

sns.kdeplot(df_original['price'])

ax = sns.kdeplot(df_original.query('price < 200').price)
ax.set_title("Price of cars")


#KDE 2D plot
sns.kdeplot(df_original[df_original['price']< 2000].loc[:,['price', 'powerPS']].dropna().sample(5000))

###Histogram plot in Seaborn ###

ax = sns.distplot(df_original['powerPS'], bins = 20, kde = False)

df1= df_original[df_original.powerPS.isin(df_original.powerPS.value_counts().head(5).index)]

sns.boxplot(
    x = 'powerPS',
    y = 'monthofRegistration',
    data = df1)

###Facet Grid

df_original.head()

#Extract models count
df = df_original[df_original['model'].isin(['seicento','superb', 'micra', 'golf'])]
g = sns.FacetGrid(df, col = "model", col_wrap = 2)

g = sns.FacetGrid(df, col = "model", col_wrap = 2)
g.map(sns.kdeplot, "price")

g = sns.FacetGrid(df, col = "model", col_wrap = 2)
g.map(sns.boxplot, "price")

g = sns.FacetGrid(df, col = "model", col_wrap = 2)
g.map(sns.kdeplot, "points")

#import plot
import matplotlib.pyplot as plt
g = sns.FacetGrid(df, col = "model", col_wrap = 2)



### Multi-Variant Plots ###
###importing libraries
import re
import numpy as np
import matplotlib.pyplot as plt

#import multivarient data sets
df_fifateams = pd.read_csv("C:/Users/ELCOT/Downloads/teams_fifa21.csv")

df_fifateams.head(3)

df_tmp = df_fifateams.dropna(how='any',axis=0) 

df_tmp.head()

df_tmp2 = df_tmp[['LeagueId', 'Overall', 'Attack', 'Midfield', 'Defence']]
df_tmp2.head()

###plot
sns.pairplot(df_tmp2)

###check the colnaems
df_tmp.columns

### Multivariant ### 
sns.lmplot(x='LeagueId', 
           y='Attack',
          hue = 'Defence',
          data = df_tmp)

sns.lmplot(x='Defence', 
           y='Attack',
          hue = 'League',
          data = df_tmp)

sns.lmplot(x='DomesticPrestige', 
           y='LeagueId',
          hue = 'Overall',
          data = df_tmp)

sns.lmplot(x='DomesticPrestige', 
           y='Midfield',
          hue = 'Players',
          data = df_tmp)

### Grouped boxplot ###

sns.boxplot(x='Players',
           y ='Overall',
           hue = 'DomesticPrestige',
           data = df_tmp.head(50))

sns.boxplot(x='Players',
           y ='DomesticPrestige',
           hue = 'IntPrestige',
           data = df_tmp.head(30))



### Heatplot ###

r = df_tmp2.corr()
sns.heatmap(r)

sns.heatmap(r, annot = True)
