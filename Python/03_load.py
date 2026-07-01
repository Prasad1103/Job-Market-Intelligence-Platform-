from pathlib import Path
import pandas as pd

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / "data" / "cleaned" / "jobs_cleaned.csv"

# --------------------------------------------------
# Check File Exists
# --------------------------------------------------

if not INPUT_FILE.exists():
    raise FileNotFoundError(f"Cleaned dataset not found:\n{INPUT_FILE}")

# --------------------------------------------------
# Load Dataset
# --------------------------------------------------

df = pd.read_csv(INPUT_FILE)

print("=" * 60)
print("JOB MARKET DATA ANALYSIS")
print("=" * 60)

# --------------------------------------------------
# Dataset Shape
# --------------------------------------------------

print(f"\nDataset Shape : {df.shape}")

# --------------------------------------------------
# First Five Rows
# --------------------------------------------------

print("\nFirst 5 Rows")
print("-" * 60)
print(df.head())

# --------------------------------------------------
# Dataset Information
# --------------------------------------------------

print("\nDataset Information")
print("-" * 60)
df.info()

# --------------------------------------------------
# Missing Values
# --------------------------------------------------

print("\nMissing Values")
print("-" * 60)
print(df.isnull().sum())

# --------------------------------------------------
# Duplicate Rows
# --------------------------------------------------

print("\nDuplicate Rows")
print("-" * 60)
print(df.duplicated().sum())

# --------------------------------------------------
# Statistical Summary
# --------------------------------------------------

print("\nStatistical Summary")
print("-" * 60)
print(df.describe(include="all").transpose())

print("\nAnalysis Completed Successfully.")