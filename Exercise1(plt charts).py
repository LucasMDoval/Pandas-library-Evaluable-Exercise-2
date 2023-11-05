import matplotlib.pyplot as plt
import pandas as pd


data = {
    "season": [17, 18, 19, 20, 21, 22],
    "points": [10, 0, 15, 20, 5, 3]
}
df1 = pd.DataFrame(data)


series_data = {
    "cause": ["COVID 19", "Heart disease", "Brain disease", "Cancer"],
    "number_of_deaths": [31559, 28687, 24558, 22682]
}
series = pd.Series(series_data["number_of_deaths"], index=series_data["cause"])

data_2 = {
    "word": ["traductor", "tiempo", "marca", "youtube"],
    "number of searches": [36960000, 32690000, 31730000, 24450000]
}
df2 = pd.DataFrame(data_2)


plt.figure(figsize=(8, 4))
plt.bar(df1["season"], df1["points"])
plt.xlabel("Season")
plt.ylabel("Points")
plt.title("Westbrook points in the last 4 seasons")
plt.show()


plt.figure(figsize=(6, 6))
plt.pie(series, labels=series.index, startangle=90, autopct='%1.1f%%')
plt.title("Number of Deaths by Causes in 2022 in Spain")
plt.show()


plt.figure(figsize=(8, 4))
plt.plot(df2["word"], df2["number of searches"], marker='o', linestyle='--', color='b')
plt.xlabel("word")
plt.ylabel("number of searches")
plt.title("most searched terms in google in spain (last year)")
plt.show()


df1_sorted = df1.sort_values(by='season', ascending=True)
print("Sorted DataFrame df1:")
print(df1_sorted)

df2_sorted = df2.sort_values(by='number of searches', ascending=False)
print("Sorted DataFrame df2:")
print(df2_sorted)

df1_filtered = df1[df1['points'] > 10]
print("Filtered DataFrame df1:")
print(df1_filtered)

df2_filtered = df2[df2['number of searches'] > 30000000]
print("Filtered DataFrame df2:")
print(df2_filtered)

df1_cleaned = df1.fillna(0)
print("Cleaned DataFrame df1:")
print(df1_cleaned)

df1.to_csv('df1.csv', index=False)

df2.to_excel('df2.xlsx', index=False)