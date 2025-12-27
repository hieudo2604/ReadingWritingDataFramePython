#import the library
import pandas as pd 

#read the csv file
df = pd.read_csv("data.csv")

#print the csv file
print(df.to_string())

print()

#print the first few rows in the csv file
print(df.head())

#print()

#print the last few rows in the csv file
print(df.tail())

#print()

#print the total rows of the csv file
print(f"The number of rows are {len(df)}") 