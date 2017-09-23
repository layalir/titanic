# -*- coding: utf-8 -*-
"""
Created on Mon Aug 07 13:16:14 2017

@author: layal
"""
from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

titanic_df = pd.read_csv("titanic-data.csv")
titanic_df = titanic_df.drop(["SibSp","Parch","Ticket","Cabin","Embarked"],axis=1)
'''
First thing I did is to look at describe() and head() outputs.
Found the following interesting facts:
  Between 50% and 75% of the passengers did not survive.
  Less than 25% of the passengers were of Pclass 1.
  75% of the passengers were 38 years old or younger.
  75% of the passengers paid $31 of less to get into the ship. Average fare was $32.20.
The output of describe show the following problems with data:
  The output of count in Age is less than total number of rows.
  The minimum Fare is zero, it is a little unsual to have passengers who paid $0.

print titanic_df.describe()
print titanic_df.head()
'''

'''
There are 177 rows missing Age cell. I have a total of 891 rows so it is not feasible to delete rows
with missing Age. I looked at these rows and they look okay. I also checked if
rows with missing Age have a Fare of 0 in which case I would have discard the entire 
row, but that was not the case, therefore I choose to keep these rows and replace the missing Age
with the median Age.

rows_with_empty_age = titanic_df.loc[titanic_df["Age"].isnull()]
print len(rows_with_empty_age.loc[titanic_df["Fare"].isnull()])
#Check if passengers are unique
print titanic_df["Name"].nunique() == len(titanic_df)

'''
age_median = titanic_df["Age"].median()
titanic_df["Age"].fillna(age_median, inplace = True)

'''
Next I look at passengers with $0 Fare and found that other cells look okay
These passengers may have been crew members

print titanic_df.loc[titanic_df["Fare"]==0].head()

I noticed that Fare field include cents to four decimal points, I'm not sure
if that was possible at that time or if this is an error. E.g., Row 1 has a Fare 
of $71.2833.
'''
'''
I noticed that there are so many rows that are missing the Cabin cell, but I decide
to leave these cells as NaN because there are too many to be fixed

print len(titanic_df.loc[titanic_df["Cabin"].isnull()])

'''

'''
Questions to investigate

(1) How would the gender correlate to survival rate?
(2) How would the passanger class correlate to survival rate?
(3) What is the age distribution of passengers at the Titanic
(4) How would the passanger age correlate to survival rate?
(5) How does the fare prices look like to Titanic passender?

'''
'''
  Question (1)
   How would the gender correlate to survival rate?

'''
#sns.countplot(x="Survived", data=titanic_df, hue="Sex")
#plt.title("Survival by gender")
'''
  Answer (1)
   Women have a much higher survival rate than men. It must be because men were
   helping out in the rescue mission and favouring the weaker gender when loading rescue boats
'''

'''
 Question (2)
  How would the passanger class correlate to survival rate?
'''

#sns.factorplot(x="Pclass",y="Survived",data=titanic_df,hue="Sex",col="Sex")

'''
  Answer (2)
  Passengers at class 1 have a better rescue rate, I think this is because of (1) Usually
first class passengers rent cabins that are in higher floors in the ship and therefore they can
evacuate the ship faster and load the rescue boats quicker. (2) Passengers of elite classes are fewer
so higher percentage of these classes can be rescued with the limited number of rescue boats available.
'''
'''
(3) What is the age distribution of passengers at the Titanic

'''
#sns.boxplot(data=titanic_df["Age"])
#plt.title("Age distribution among Titanic passengers")
#plt.ylabel("Age in years")

'''
Answer (3)
The median of passengers age is about 28 years old. There are a few outliers where
the oldest passenger is about 80 years old.
'''

'''
 Question (4)
  How does the passenger age correlate to survival rate?
'''

#sns.swarmplot(y="Age", x="Sex", data=titanic_df, hue="Survived", split=True)
#sns.swarmplot(y="Age", x="Pclass", data=titanic_df, hue="Survived", split=True)


'''
  Answer (4)
  Young children (younger than 10 years old) regardless of gender, have about 60% survival rate.
  The survival rate increases with increasing the age for female passengers. This is consistent
  with previous finding that female passengers have relatively high survival rate when compared to
  male passengers. Male passengers other than children have survival rates that is lower than 22%.
'''

#classGenderGroupedData = 100*(titanic_df.groupby(["Pclass","Sex"]).sum()/\
#                       titanic_df.groupby(["Pclass","Sex"]).count())

#plot4 = classGenderGroupedData["Survived"].plot.bar()
#plot4.set_ylabel("Survival Rate (%)")
#plt.show()
'''
Question (5)
How does the fare prices look like to Titanic passender?
'''
#sns.lmplot(x="Age", y="Fare",data=titanic_df, hue="Pclass", fit_reg=False)
#plt.title('Fare prices among different passenger classes and ages')
#plt.xlabel("Age in years")
#plt.ylabel("Fare in dollars")
#plt.ylim(0, None)
#plt.xlim(0, None)


'''
Answer (5)
From the scatter figure it looks like the price ranges for different classes are overlapping.
There are instances where Class 1 passengers have paid less than what Class 3 passengers
have paid. Maybe these passengers got discounts.
Furthermore, there are few outliers in Class 1 who paid about $512. Following are fare price ranges
for different classes.
class 1: [10.5, 512]
class 2: [10.5,73.5]
class 3: [5, 512]
'''

'''
From this figure I see that females have higher survival rates than males regardless of class.
In particular, class 1-femal passengers have just above 90% survival rate. The lowest survival rate
belongs to males residing in class 3.
'''
'''
In conclusion, the Titanic ship survival rates decrease when age increases, are higher for females 
and class 1 passengers. Males in first class have higher survival rates than males in class 2
 and class 3.
Data in this project is a 891-passenger sample of the Titanic passenger 
population of 2,435. Therefore, any conclusions from the sample should be verified using hypothesis
testing to see if findings are plausible statements about the Titanic passengers.
Further, there are 177 out of the 891 that don't have Age information in this dataset. These entries
were replaced with the median age but there is no guarantee that these passengers don't include
outliers. I didn't find that missing data belong to particular category of the passengers.
Also, if Cabin field has more data then I can use that to draw conclusions about survival rates of various
cabins. I found that fare ranges among classes to be stange, one would not expect them to overlap,
we need to verify the correctness of this data and to find other variables on which the fare
price depend on other than the class type.
'''
