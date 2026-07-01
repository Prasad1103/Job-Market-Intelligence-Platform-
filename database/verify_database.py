import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

tables = [
    "dim_company",
    "dim_location",
    "dim_schedule",
    "dim_search_term",
    "dim_skills",
    "fact_jobs",
    "job_skills"
]

print("=" * 50)
print("DATABASE SUMMARY")
print("=" * 50)

for table in tables:

    count = cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()[0]

    print(f"{table:20} : {count}")

conn.close()