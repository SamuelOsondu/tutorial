# The Mystery of the Messy Sales Data
# You just got hired as a data analyst at a fast-growing e-commerce company. Your boss, Mr. Ade, is frustrated
# because their sales data is a mess.
#
# Mr. Ade: "We have thousands of orders coming in daily, but I can’t make sense of the numbers. Which products are
# selling the most? Where are our customers coming from? Can we spot trends?"
#
# Your task? Find insights from the chaotic data.
#
# At first, you think about checking the data manually in Excel, but the file is too large and crashes when you try
# opening it. You realize:
#
# Scrolling through 100,000+ rows is impossible.
# You need to filter out missing values and clean the data first.
# Merging multiple files is necessary to get the full picture.
# The Solution: Pandas
# With Pandas, you can:
# ✅ Load massive datasets into Python quickly.
# ✅ Inspect and clean data in seconds (fix missing values, remove duplicates).
# ✅ Filter and group sales by product category, location, and time.
# ✅ Merge customer data with sales records for deeper insights.
# ✅ Visualize trends with easy-to-generate charts.
#
# By the end of this week, you'll be able to:
# 📌 Read and manipulate large datasets like a pro.
# 📌 Make informed business decisions from raw data.
# 📌 Present data in clear, visual formats for stakeholders.



# Week 8: Data Analysis with Pandas
# 1️⃣ Introduction to Pandas: Series and DataFrames
# What is Pandas?
# Pandas is a powerful Python library for data analysis and manipulation. It provides two key structures:
#
# Series – A one-dimensional labeled array (like a list with an index).
# DataFrame – A two-dimensional table (like an Excel sheet).
# 📌 Installing Pandas
# If you haven’t installed Pandas yet, use:

import pandas as pd

# 2️⃣ Data Operations: Loading, Inspecting, and Cleaning Data
# Loading Data into Pandas
# Pandas can read data from multiple sources, including CSV, Excel, and JSON files.
#
# Loading a CSV file:

df = pd.read_csv("sales_data.csv")
print(df.head())  # Displays the first 5 rows

# 📌 Checking the Data

print(df.info())  # General info about columns
print(df.describe())  # Summary statistics
print(df.columns)  # List of column names

# 📌 Handling Missing Values

df = df.dropna()  # Removes rows with missing values
df.fillna(0, inplace=True)  # Replaces missing values with 0

df.rename(columns={"old_name": "new_name"}, inplace=True)

# 3️⃣ Data Manipulation: Filtering, Grouping, Merging
# Filtering Data

filtered_df = df[df["Sales"] > 1000]  # Select rows where sales are greater than 1000
print(filtered_df)

# Grouping Data
grouped = df.groupby("Category")["Sales"].sum()
print(grouped)

# Merging DataFrames

df1 = pd.read_csv("customers.csv")
df2 = pd.read_csv("orders.csv")

merged_df = pd.merge(df1, df2, on="customer_id", how="inner")  # Merges on 'customer_id'
print(merged_df.head())

# 4️⃣ Data Visualization: Plotting with Pandas
# Pandas integrates with Matplotlib to create quick visualizations.
#
# 📌 Import Matplotlib

import matplotlib.pyplot as plt

# Plotting Sales Trends
df["Sales"].plot(kind="line", title="Sales Over Time")
plt.show()

# Bar Chart: Sales by Category

df.groupby("Category")["Sales"].sum().plot(kind="bar", title="Sales by Category")
plt.show()

# 🔹 Summary of What You Learned
# ✔️ How to load and inspect datasets using Pandas.
# ✔️ How to clean data (handle missing values, rename columns).
# ✔️ How to filter, group, and merge datasets for analysis.
# ✔️ How to create simple visualizations to find insights.
