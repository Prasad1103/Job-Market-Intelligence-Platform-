from pathlib import Path
import sqlite3
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent

db_path = PROJECT_ROOT / "database" / "jobs.db"
output_folder = PROJECT_ROOT / "data" / "powerbi"
output_folder.mkdir(parents=True, exist_ok=True)

conn = sqlite3.connect(db_path)

tables = [
    "fact_jobs",
    "dim_company",
    "dim_location",
    "dim_schedule",
    "dim_search_term",
    "dim_skills",
    "job_skills"
]

for table in tables:
    df = pd.read_sql_query(f"SELECT * FROM {table}", conn)

    output_file = output_folder / f"{table}.xlsx"

    df.to_excel(output_file, index=False)

    print(f"Exported {table}")

conn.close()