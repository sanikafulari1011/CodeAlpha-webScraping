import pandas as pd
import matplotlib.pyplot as plt


# Read CSV
df = pd.read_csv(r"C:\Users\sanik\OneDrive\Desktop\Codealpha\WebScraping\quotes.csv")


print("Dataset Loaded Successfully")
print(df.head())

# Create Quote Length column
df["Length"] = df["Quote"].str.len()

# -------------------------------
# Top 10 Authors
# -------------------------------

top10 = df["Author"].value_counts().head(10)

plt.figure(figsize=(10,5))
top10.plot(kind="bar", color="skyblue")
plt.title("Top 10 Authors")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Top10Authors_Task3.png")
plt.show()

# -------------------------------
# Pie Chart
# -------------------------------

plt.figure(figsize=(8,8))
top10.plot(kind="pie", autopct="%1.1f%%")
plt.title("Top 10 Authors Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("PieChart_Task3.png")
plt.show()

# -------------------------------
# Histogram
# -------------------------------

plt.figure(figsize=(8,5))
plt.hist(df["Length"], bins=15)
plt.title("Quote Length Distribution")
plt.xlabel("Quote Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Histogram_Task3.png")
plt.show()

# -------------------------------
# Horizontal Bar Chart
# -------------------------------

plt.figure(figsize=(10,5))
top10.sort_values().plot(kind="barh", color="orange")
plt.title("Top 10 Authors")
plt.xlabel("Number of Quotes")
plt.tight_layout()
plt.savefig("HorizontalBar_Task3.png")
plt.close()

# -------------------------------
# Box Plot
# -------------------------------

plt.figure(figsize=(6,5))
plt.boxplot(df["Length"])
plt.title("Quote Length Box Plot")
plt.ylabel("Length")
plt.tight_layout()
plt.savefig("BoxPlot_Task3.png")
plt.close()

print("\nTask 3 Completed Successfully!")