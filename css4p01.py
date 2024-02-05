# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 09:30:48 2024

@author: Q Mazibuko
"""

import pandas as pd

from collections import Counter



df1 = pd.read_csv("movie_dataset.csv")

print(df1)

print(df1.info())

print(df1.describe())

# #Display max and min year

print(df1["Year"].min())
print(df1["Year"].max())

# #I want to see all rows so I can identify Nan"Not a Number"

pd.set_option("display.max_rows", None)

print(df1)



#Sorting data chronologically - Assuming column is just called 'Year'

df1 = df1.sort_values(by='Year') 

df1.to_csv('data_sorted.csv', index=False)

#Replacing empty values - read page 10/18 day 2 notes
# 1- replace empty cells with a zero

df1 = df1.fillna(0)

print(df1)

#Q1
#To find out who has the highest rating in the data, we can use the .idxmax() method in pandas.
# This returns the index value of the maximum value in a series or dataframe column.
#We then use .loc[] to lookup the 'Name' value at that index row.

max_rating = df1["Rating"].idxmax()

highest_rating_name = df1.loc[max_rating, "Title" ]


print(f"Highest rating: {highest_rating_name}")

#Q2

mean_revenue = df1["Revenue (Millions)"].mean()

print(f"Average revenue : {mean_revenue}")

#Q4
#Filter to only get the rows for year 2016
#If the movie data is provided only as titles rather than numeric counts, you can use the .value_counts() method in pandas to count occurrences.
#Run .value_counts() on the 'Movie' column to get release count
#Take .count() of the value_counts output to total numbers

df1_2016 = df1[df1["Year"]==2016]

total_movies_2016 = df1_2016["Title"].value_counts().count()

print(total_movies_2016)

#Q5

Christopher_Nolan = df1["Director"].str.contains("Christopher Nolan")

Chris_directed_movies = df1.loc[Christopher_Nolan, "Title"]

#count rows with Christopher
#Take shape[0] to count rows

count_movies = df1[Christopher_Nolan].shape[0]

print(f" Movies directed by ChristopherNolan; {count_movies}")

print(Chris_directed_movies)

#Q6
# Filter movies with a rating of at least 8.0
# Count the number of movies in the filtered DataFrame
#len is a built-in function that is used to get the length or the number of elements in a sequence or a collection

print(df1["Rating"])

movie_rating = df1[df1["Rating"]>=8.0]

movie_rating_count = len(movie_rating)

print(f" Number of movies greater and equal to 8; {movie_rating_count}")

#Q7
# Filter movies directed by Christopher Nolan
# Calculate the median rating

chris_directed_median = df1[df1["Director"]=="Christopher Nolan"]

median_rating = chris_directed_median["Rating"].median()

print(f" Median rating of movies directed by Christopher Nolan; {median_rating}")

#Q8
#Determine ratings for each year
#Determine year with maximum evarage/mean
#The groupby function is used to group the DataFrame by the 'year' 
#The mean function is applied to calculate the average rating for each year
#The idxmax function is used to find the year with the highest average rating.

mean_rating_per_year = df1.groupby("Year")["Rating"].mean()

year_highest_average_rating = mean_rating_per_year.idxmax()

print(f" year with the highest average rating; {year_highest_average_rating}")

#Q9
#Must first look at filtering movies released in year 2006 and 2016
#Determine no. of movies for each year
#Calculate percenatge increase = (2016 movies - 2006 movies)/2006 movies *100

df1_2006 = df1[df1["Year"]==2006]
df1_2016 = df1[df1["Year"]==2016]

total_movies_2006 = len(df1_2006)
total_movies_2016 = len(df1_2016)

percentage_increase = ((total_movies_2016 - total_movies_2006) / total_movies_2006) * 100

print(f"The percentage increase in the number of movies between 2006 and 2016 is {percentage_increase:.2f}%.")

#Q10
#Concatenate all the lists of actors from the 'Actors' column
#The str.split(', ') is used to split the cast information into lists, and then a list comprehension is used to flatten these lists.

all_actors = [actor for sublist in df1["Actors"].dropna().str.split(', ') for actor in sublist]

# Find the most common actor
most_common_actor, most_common_actor_count = Counter(all_actors).most_common(1)[0]

print(f"The most common actor in all the movies is {most_common_actor} with {most_common_actor_count} appearances.")

# Identify movies where the most common actor appears
movies_with_most_common_actor = df1[df1['Actors'].str.contains(most_common_actor)]

# Display information about movies with the most common actor
print(f"\nMovies with {most_common_actor}:")
print(movies_with_most_common_actor[['Genre', 'Year', 'Rating']])



#Q11
#Extract and flatten the genres from the 'genres' column
#Count the number of unique genres
#The str.split(', ') is used to split the genre information into lists, and then a list comprehension is used to flatten these lists
#The set is used to obtain unique genres, and len is used to count the number of unique genres

all_genres = [genre for sublist in df1["Genre"].dropna().str.split(', ') for genre in sublist]

number_unique_genres = len(set(all_genres))

print(f"There are {number_unique_genres} unique genres in the dataset.")

#Q12

import matplotlib.pyplot as plt

from scipy.stats import linregress


# Correlation between 'Runtime' and 'Rating'
plt.scatter(df1['Runtime (Minutes)'], df1['Rating'])

# Fit a linear regression line
slope, intercept, r_value, p_value, std_err = linregress(df1['Runtime (Minutes)'], df1['Rating'])
line = slope * df1['Runtime (Minutes)'] + intercept

# Plot the regression line
plt.plot(df1['Runtime (Minutes)'], line, color='red', label='Linear Regression Line')

plt.title('Scatter Plot of Runtime vs. Rating with Regression Line')
plt.xlabel('Runtime (Minutes)')
plt.ylabel('Rating')
plt.legend()
plt.show()


# Correlation between 'Revenue' and 'Rating'

plt.scatter(df1['Revenue (Millions)'], df1['Rating'])

# Fit a linear regression line
slope, intercept, r_value, p_value, std_err = linregress(df1['Revenue (Millions)'], df1['Rating'])
line = slope * df1['Revenue (Millions)'] + intercept

# Plot the regression line
plt.plot(df1['Revenue (Millions)'], line, color='red', label='Linear Regression Line')

plt.title('Scatter Plot of Revenue vs. Rating with Regression Line')
plt.xlabel('Revenue (Millions)')
plt.ylabel('Rating')
plt.legend()
plt.show()

# Correlation between 'Votes' and 'Rating'

plt.scatter(df1['Votes'], df1['Rating'])

# Fit a linear regression line
slope, intercept, r_value, p_value, std_err = linregress(df1['Votes'], df1['Rating'])
line = slope * df1['Votes'] + intercept

# Plot the regression line
plt.plot(df1['Votes'], line, color='red', label='Linear Regression Line')

plt.title('Scatter Plot of Votes vs. Rating with Regression Line')
plt.xlabel('Votes')
plt.ylabel('Rating')
plt.legend()
plt.show()
