import pandas as pd

reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip")
summary_rev = reviews.groupby("country").points.agg(["count", "mean"]).round(1)
summary_rev = summary_rev.rename(columns = {"mean":"points"})

summary_rev.to_csv("data/reviews-per-country.csv")



print(reviews.head())
print(summary_rev.head())
print(summary_rev.info())