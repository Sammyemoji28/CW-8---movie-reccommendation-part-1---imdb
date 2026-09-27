
import pandas as pd

movieDF = pd.read_csv("movies.csv")
print(movieDF.head())

# --- DATA CLEANING
# - step 1 : select needed columns
movieDF = movieDF[["title","vote_average","vote_count"]]
# print(movieDF.info())

# - step 2 : removing missing values
movieDF.dropna(inplace = True)
# print(movieDF.info())

print("Average Rating Mean: ",movieDF["vote_average"].mean())
print("Minimum Votes Needed: ",movieDF["vote_count"].quantile(0.7))
# --- FORMULA : WR = ((v/(v + m))* R) + ((m/(v + m))* C)
# - v: number of votes 
# - m: minimum number of votes required
# - R: average rating
# - C: mean of all the votes 
# - WR: weighted rating

C = movieDF["vote_average"].mean()
m = movieDF["vote_count"].quantile(0.7)

def weightedRating(x, m = m, C = C):
    v = x["vote_count"]
    R = x["vote_average"]
    return ((v/(v + m))* R) + ((m/(v + m))* C)

movieDF["weighted_rating"] = movieDF.apply(weightedRating, axis = 1)
# print(movieDF.head(15))

movieDF_sorted = movieDF.sort_values(by = "weighted_rating", ascending = False)
# print(movieDF_sorted.head(10))

def movie_rec(n):
    print(movieDF_sorted[["title","weighted_rating"]].head(n))

movie_rec(10)
