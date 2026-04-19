import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("vgsales.csv")
df = df.dropna()
df["Year"] = df["Year"].astype(int)

print(f"{df.shape[0]:,} rows by {df.shape[1]} columns")
print(f"{df['Year'].max() - df['Year'].min()} years covered")
print(f"{df['Platform'].nunique()} platforms")
print(f"{df['Genre'].nunique()} genres")
print(f"{df['Publisher'].nunique()} publishers")

print("\nSales by Region (in Millions):")
print(df[["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales"]].describe().round(2))

sales_by_genre = df.groupby("Genre")["Global_Sales"].sum().sort_values(ascending=False)
print(sales_by_genre.head(10))

fig, ax = plt.subplots(figsize=(15, 8))
sns.barplot(x=sales_by_genre.index, y=sales_by_genre.values, ax=ax)
ax.set_title("Total Sales by Genre")
ax.set_xlabel("Genre")
ax.set_ylabel("Sales (in Millions)")
plt.show()

annual_sales = df[df['Year'].between(df['Year'].min(), df['Year'].max())].groupby('Year')["Global_Sales"].sum()

fig, ax = plt.subplots(figsize=(15, 8))
ax.fill_between(annual_sales.index, annual_sales.values, alpha=0.5, color = "hotpink")
ax.plot(annual_sales.index, annual_sales.values, color="black", linewidth = 2)
ax.set_title("Total Sales by Year")
ax.set_xlabel("Year")
ax.set_ylabel("Sales (in Millions)")
plt.show()