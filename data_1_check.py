from itertools import count
import requests
import pandas as pd

r=requests.get(url='https://api.openbrewerydb.org/breweries')
print(r.status_code)
data = r.json()

df=pd.DataFrame(data)

#Find and print TWO descriptive statistics about your data. This can be absolutely anything, 
# from the mean() or sum() of a column to the number of different categories, to the number 
# of null values in a column. We just want to see two pieces of information.

max=df.brewery_type.max()
min=df.brewery_type.min()
print (min , max)


#Write a query in Pandas to select a particular set of your data. You can use a mask or with 
# .query(), but we want you to pull out a subset based on any parameter you like. This could 
# be "show me every row where HTTPS=False" or anything else.


micro = df.query('brewery_type == "micro"')
print (micro)


#Select and print the SECOND AND THIRD columns of your data frame.
print (df[['name', 'brewery_type']])

#Select and print the FIRST 4 rows of you data frame.
first_4=df.head(4)
print (first_4)