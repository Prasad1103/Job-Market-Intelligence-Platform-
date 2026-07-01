from pathlib import Path
import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "cleaned" / "jobs_cleaned.csv"
OUTPUT_FILE = BASE_DIR / "data" / "processed" / "jobs_processed.csv"

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
print("FEATURE ENGINEERING")
print("=" * 60)

print(f"Original Shape : {df.shape}")

# --------------------------------------------------
# 1. Job Mode
# --------------------------------------------------

if "work_from_home" in df.columns:

    def job_mode(value):
        if pd.isna(value):
            return "Unknown"
        elif bool(value):
            return "Remote"
        else:
            return "Onsite"

    df["job_mode"] = df["work_from_home"].apply(job_mode)

# --------------------------------------------------
# 2. Salary Category
# --------------------------------------------------

if "salary_standardized" in df.columns:

    def salary_category(salary):
        if pd.isna(salary):
            return "Unknown"
        elif salary < 50000:
            return "Low"
        elif salary < 100000:
            return "Medium"
        elif salary < 150000:
            return "High"
        else:
            return "Very High"

    df["salary_category"] = df["salary_standardized"].apply(salary_category)

# --------------------------------------------------
# 3. Company Name Cleanup
# --------------------------------------------------

if "company_name" in df.columns:
    df["company_name"] = df["company_name"].astype(str).str.strip()

# --------------------------------------------------
# 4. Job Title Cleanup
# --------------------------------------------------

if "title" in df.columns:
    df["title"] = df["title"].astype(str).str.strip()

# --------------------------------------------------
# 5. Skill Count
# --------------------------------------------------

if "description_tokens" in df.columns:
    df["skill_count"] = (
        df["description_tokens"]
        .fillna("")
        .astype(str)
        .apply(lambda x: len([i for i in x.split(",") if i.strip()]))
    )

# --------------------------------------------------
# 6. Description Length
# --------------------------------------------------

if "description" in df.columns:
    df["description_length"] = (
        df["description"]
        .fillna("")
        .astype(str)
        .str.len()
    )

# --------------------------------------------------
# Save Processed Dataset
# --------------------------------------------------

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False)

print("\nFeature Engineering Completed Successfully!")

print(f"\nFinal Shape : {df.shape}")

print(f"\nProcessed dataset saved to:\n{OUTPUT_FILE}")

print("\nFirst Five Rows")
print(df.head())

print("\nDataset Information")
df.info()