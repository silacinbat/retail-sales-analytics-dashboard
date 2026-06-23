
import pandas as pd

df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")

# Convert dates
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Check for duplicates
duplicates = df.duplicated().sum()

print("Duplicate Rows:", duplicates)

# Create new columns
df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month

# Calculate shipping time
df["Days To Ship"] = (
    df["Ship Date"] - df["Order Date"]
).dt.days

# Calculate profit margin 
df["Profit Margin"] = (
    df["Profit"] / df ["Sales"]
) * 100

# Save cleaned file
df.to_csv(
    "clean_superstore.csv",
    index=False
)

print ("File saved successfully.")

print (df[[
    "Sales",
    "Profit",
    "Profit Margin",
    "Days To Ship"
]].round(2).head())


# Display results
print(df[["Order Date", "Year", "Month"]].head())


print("\nTOTAL SALES")
print(df["Sales"].round(2).sum())

print("\nTOTAL PROFIT")
print(round(df["Profit"].sum(), 2))

print("\nAVERAGE SHIPPING TIME")
print(round(df["Days To Ship"].mean(), 2))

print("\nTOP 10 STATES BY SALES")
print(
    df.groupby("State")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .round(2)
      .head(10)
)
