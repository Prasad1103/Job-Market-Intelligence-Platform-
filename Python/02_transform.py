from pathlib import Path
import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "raw" / "gsearch_jobs.csv"
OUTPUT_FILE = BASE_DIR / "data" / "cleaned" / "jobs_cleaned.csv"

# --------------------------------------------------
# Check Input File
# --------------------------------------------------

if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Input file not found:\n{INPUT_FILE}")

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("Dataset Loaded Successfully")
print("=" * 60)
print(f"Original Shape : {df.shape}")

# --------------------------------------------------
# Remove Unwanted Columns
# --------------------------------------------------

drop_columns = [
    "Unnamed: 0",
    "index",
    "thumbnail",
    "extensions",
    "commute_time",
    "salary",
    "salary_pay",
    "salary_rate",
    "salary_hourly",
    "salary_yearly",
    "date_time"
]

# Drop only columns that actually exist
existing_columns = [col for col in drop_columns if col in df.columns]

df.drop(columns=existing_columns, inplace=True)

print(f"Removed {len(existing_columns)} unnecessary columns.")
print(f"Shape after dropping columns : {df.shape}")

# --------------------------------------------------
# Remove Duplicate Rows
# --------------------------------------------------

duplicates = df.duplicated().sum()
df.drop_duplicates(inplace=True)

print(f"Duplicates Removed : {duplicates}")
print(f"Shape after removing duplicates : {df.shape}")

# --------------------------------------------------
# Fill Missing Values
# --------------------------------------------------

fill_text = ["location", "via", "posted_at", "schedule_type"]

for col in fill_text:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

if "work_from_home" in df.columns:
    df["work_from_home"] = df["work_from_home"].fillna(False)

# --------------------------------------------------
# Missing Value Summary
# --------------------------------------------------

print("\nRemaining Missing Values")
print(df.isnull().sum())

# --------------------------------------------------
# Create Output Folder
# --------------------------------------------------

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Save Cleaned Dataset
# --------------------------------------------------

df.to_csv(OUTPUT_FILE, index=False)

print("\n" + "=" * 60)
print("Cleaning Completed Successfully")
print("=" * 60)
print(f"Cleaned dataset saved to:\n{OUTPUT_FILE}")
print(f"Final Shape : {df.shape}")

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------

print("\nDataset Information")
print(df.info())

print("\nFirst Five Rows")

print(df.head())