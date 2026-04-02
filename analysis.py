import pandas as pd

df = pd.read_csv("output/input.csv")

print(df.head())

result = df.groupby("vaccinated")["covid_positive"].mean()

print("Infection rate by vaccination:")
print(result)
