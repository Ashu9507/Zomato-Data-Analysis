"""
Do more restaurants provide online delivery compared to offline services?
Which types of restaurants are most favored by the general public?
What price range do couples prefer for dining out?
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Zomato-data.csv")


# Remove the /5 from rate column such as rate = 4.1/5 to rate=4.1
def handlerate(value):
    value = str(value).split("/")
    value = value[0]
    return float(value)


df["rate"] = df["rate"].apply(handlerate)
df.head()

# Give summary
df.info()

# Check for null
df.isnull().sum()

# Shows categories of restaurant
sns.countplot(x=df["listed_in(type)"])
plt.title("Categories of restaurants")
plt.xlabel("Type of restaurant")

# Online Order Availability
sns.countplot(x=df["online_order"])

# Votes by restaurant type
group_data = df.groupby("listed_in(type)")["votes"].sum()
result = pd.DataFrame({"votes": group_data})
plt.plot(result, c="green", marker="o")
plt.xlabel("Types of restaurant")
plt.ylabel("Votes")

# Most Voted Restaurant
max_votes = df["votes"].max()
resturant_with_max_votes = df.loc[df["votes"] == max_votes, "name"]

print("Restaurant with maximum votes =", resturant_with_max_votes)


# Analysis of ratings
plt.hist(df["rate"], bins=5)
plt.title("Rating analysis")
plt.xlabel("Rating")
plt.show()

# Approximate of two couples cost for food
couple_cost = df["approx_cost(for two people)"]
sns.countplot(x=couple_cost)

# Rating Comparison
plt.figure(figsize=(8, 8))
sns.boxplot(x="online_order", y="rate", data=df)

# Order Mode Prefences by Restaurant Type
pivot_table = df.pivot_table(
    index="listed_in(type)", columns="online_order", aggfunc="size", fill_value=0
)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt="d")
plt.title("Heatmap")
plt.xlabel("Online Order")
plt.ylabel("Listed In (Type)")
plt.show()
