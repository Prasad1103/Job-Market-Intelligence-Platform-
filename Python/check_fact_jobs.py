import pandas as pd

df = pd.read_csv("data/powerbi/fact_jobs.csv")

print(df.info())

print("\nRows with missing job_key:")
print(df[df["job_key"].isna()].head(20))

print("\nDuplicate job_key:")
print(df[df["job_key"].duplicated()].head())

print("\nData types:")
print(df.dtypes)