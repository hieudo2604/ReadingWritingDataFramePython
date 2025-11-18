#import the library
import pandas as pd 

#read the csv file
df = pd.read_csv("data.csv")

#sort the dataframe by "Age" from youngest to oldest
df = df.sort_values(by="Age", ascending=True)

#write the new csv file
df.to_csv("data1.csv", index=False)

#print 
print(df)