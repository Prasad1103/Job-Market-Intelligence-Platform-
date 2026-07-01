from pathlib import Path
import pandas as pd

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# File paths
RAW_DATA = BASE_DIR / "data" / "raw" / "gsearch_jobs.csv"
OUTPUT_DATA = BASE_DIR / "data" / "processed" / "jobs_processed.csv"

print(f"Reading file from:\n{RAW_DATA}")

# Check file exists
if not RAW_DATA.exists():
    raise FileNotFoundError(f"\nCSV file not found:\n{RAW_DATA}")

# Read CSV
df = pd.read_csv(RAW_DATA)

print("\nDataset Loaded Successfully!")
print(f"Rows    : {df.shape[0]}")
print(f"Columns : {df.shape[1]}")

print("\nFirst 5 rows:")
print(df.head())

# Create processed folder if missing
OUTPUT_DATA.parent.mkdir(parents=True, exist_ok=True)

# Save processed file
df.to_csv(OUTPUT_DATA, index=False)

print(f"\nProcessed file saved to:\n{OUTPUT_DATA}")