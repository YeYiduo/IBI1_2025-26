import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir('C:\\Users\\ASUS\\Desktop\\IBI practical\\practical10')
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#show the third and fourth columns (the year and the DALYs) for the first 10 rows (inclusive)
print(dalys_data.iloc[0:10,2:4])
#What year reported the maximum DALYs across the first 10 years for which DALYs were recorded in Afghanistan?
max_year=0
max_DALYs=0
for i in range(10):
    current_year=dalys_data.iloc[i,2]
    current_DALYs=dalys_data.iloc[i,3]
    if current_DALYs>max_DALYs:
        max_DALYs=current_DALYs
        max_year=current_year
print("the maximum DALYs in Afghanistan is",max_DALYs,"in",max_year,"years")
# used a Boolean to show all years for which DALYs were recorded in Zimbabwe.
#  a comment stating the first and last year for which these data were recorded.
my_rows=[]
for i in range(len(dalys_data)):
    if dalys_data.iloc[i,0]=="Zimbabwe":
        my_rows.append(True)
    else:
        my_rows.append(False)
print(dalys_data.iloc[my_rows,2:4].to_string(index=False))
print("the first year for which these data were recorded in Zimbabwe is",dalys_data.iloc[my_rows,2].min(),
      "and the last year is",dalys_data.iloc[my_rows,2].max())
#the first year for which these data were recorded in Zimbabwe is 1990 and the last year is 2019

#which countries reported the largest and smallest DALYs
#values in the most recent year for which data are available (2019).
recent_data = dalys_data.loc[dalys_data.Year == 2019, ["Entity", "DALYs"]]
max_DALYs_country = recent_data.loc[recent_data.DALYs.idxmax(), "Entity"]
min_DALYs_country = recent_data.loc[recent_data.DALYs.idxmin(), "Entity"]
print("the country with the largest DALYs in 2019 is", max_DALYs_country)
print("the country with the smallest DALYs in 2019 is", min_DALYs_country)
#the country with the largest DALYs in 2019 is Lesotho
#the country with the smallest DALYs in 2019 is Singapore


target_country=dalys_data.loc[dalys_data.iloc[:,0]==max_DALYs_country,["Year","DALYs"]]
plt.plot(target_country.Year,target_country.DALYs, 'bo')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title("DALYs in "+max_DALYs_country)
plt.xticks(target_country.Year,rotation=-90)
plt.show()

#What was the distribution of DALYs across the top 10 countries in 2006?
data_2006 = dalys_data.loc[dalys_data.Year == 2006, "DALYs"]
data_2006 = data_2006.nlargest(10)
countrys_2006 = dalys_data.loc[dalys_data.Year == 2006, "Entity"]
countrys_2006 = countrys_2006.loc[data_2006.index]
labels = countrys_2006
sizes = data_2006
plt.figure(figsize=(10, 10))
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Distribution of DALYs across the top 10 countries in 2006")
plt.show()



