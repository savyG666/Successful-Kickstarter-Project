# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 16:40:57 2023

@author: cex
"""
import pandas as pd 
import matplotlib.pyplot as plt
MostFunded = pd.read_csv("C:\\Users\\cex\\OneDrive\\Desktop\\DataScience\\DataScienceProjects\\Most Funded Kickstarted Projects\\most_funded_feb_2023.csv")

"""We want to find out which category is most successful"""
MostFundedCols = MostFunded[['id', 'backers_count', 'category_name', 'category_parent_name','usd_pledged']]
MostPop = MostFundedCols['category_name'].value_counts().head(10)
MostPop.plot(kind='bar')
plt.title('Categories of Most Funded Kickstarter Projects')
plt.ylabel('Number of Projects')
plt.xlabel('Category of Project')
plt.show()

""""We can see that the Tabletop games category is most successful, so let's subset this and randomly sample the description of 5 projects, 
this will give us qualative data showing which projects have been successful"""
TabletopGames = MostFunded[MostFunded['category_name']=='Tabletop Games']
TabletopSamples = TabletopGames.sample(5, replace=False)
print(TabletopSamples['profile_blurb'])

"""Now let's find where the most successful projects are based"""
LocCols = MostFunded[['location_country',
'location_name', 'location_state', 'location_type']]
MostCountry = LocCols['location_country'].value_counts().head(5)
MostCountry.plot(kind='bar')
plt.title('Countries of Most Funded Kickstarter Projects')
plt.ylabel('Number of Projects')
plt.xlabel('Category of Project')
plt.show()

MostState = LocCols['location_state'].value_counts().head(10)
MostState.plot(kind='bar')
plt.title('States of Most Funded Kickstarter Projects')
plt.ylabel('Number of Projects')
plt.xlabel('State of Project')
plt.show()

"""The state with the most successful projects was California, by quite a large margin."""

PickCols = MostFunded['staff_pick'].value_counts()
print(round((PickCols[True]/PickCols.sum())*100, 1), '% of top projects were a Staff Pick')

"""
