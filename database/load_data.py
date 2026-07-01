import sqlite3
import pandas as pd

# -----------------------------
# Connect Database
# -----------------------------
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# -----------------------------
# Load Processed Dataset
# -----------------------------
df = pd.read_csv("../data/processed/jobs_processed.csv")

print(f"Rows Loaded : {len(df)}")

# ==========================================================
# LOAD DIMENSION TABLES
# ==========================================================

print("\nLoading Dimension Tables...")

# ---------- Company ----------
companies = (
    df["company_name"]
    .dropna()
    .drop_duplicates()
    .sort_values()
)

for company in companies:
    cursor.execute(
        """
        INSERT OR IGNORE INTO dim_company(company_name)
        VALUES(?)
        """,
        (company,),
    )

# ---------- Location ----------
locations = (
    df["location"]
    .dropna()
    .drop_duplicates()
    .sort_values()
)

for location in locations:
    cursor.execute(
        """
        INSERT OR IGNORE INTO dim_location(location)
        VALUES(?)
        """,
        (location,),
    )

# ---------- Schedule ----------
schedules = (
    df["schedule_type"]
    .dropna()
    .drop_duplicates()
    .sort_values()
)

for schedule in schedules:
    cursor.execute(
        """
        INSERT OR IGNORE INTO dim_schedule(schedule_type)
        VALUES(?)
        """,
        (schedule,),
    )

# ---------- Search Terms ----------
terms = (
    df["search_term"]
    .dropna()
    .drop_duplicates()
    .sort_values()
)

for term in terms:
    cursor.execute(
        """
        INSERT OR IGNORE INTO dim_search_term(search_term)
        VALUES(?)
        """,
        (term,),
    )

conn.commit()

print("Dimension Tables Loaded.")

# ==========================================================
# BUILD LOOKUP DICTIONARIES
# ==========================================================

company_lookup = dict(
    cursor.execute(
        "SELECT company_name, company_key FROM dim_company"
    ).fetchall()
)

location_lookup = dict(
    cursor.execute(
        "SELECT location, location_key FROM dim_location"
    ).fetchall()
)

schedule_lookup = dict(
    cursor.execute(
        "SELECT schedule_type, schedule_key FROM dim_schedule"
    ).fetchall()
)

search_lookup = dict(
    cursor.execute(
        "SELECT search_term, search_key FROM dim_search_term"
    ).fetchall()
)

print("Lookup Dictionaries Created.")

# ==========================================================
# LOAD FACT TABLE
# ==========================================================

print("\nLoading Fact Table...")

for _, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO fact_jobs(

        job_id,
        title,
        company_key,
        location_key,
        schedule_key,
        search_key,
        posted_at,
        salary_avg,
        salary_min,
        salary_max,
        salary_standardized,
        job_mode,
        salary_category,
        skill_count,
        description_length

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        """,
        (
            row["job_id"],
            row["title"],
            company_lookup.get(row["company_name"]),
            location_lookup.get(row["location"]),
            schedule_lookup.get(row["schedule_type"]),
            search_lookup.get(row["search_term"]),
            row["posted_at"],
            row["salary_avg"],
            row["salary_min"],
            row["salary_max"],
            row["salary_standardized"],
            row["job_mode"],
            row["salary_category"],
            row["skill_count"],
            row["description_length"],
        ),
    )

conn.commit()

print("Fact Table Loaded.")

# ==========================================================
# LOAD SKILLS DIMENSION
# ==========================================================

print("\nExtracting Skills...")

skills = set()

for tokens in df["description_tokens"].fillna(""):

    token_list = str(tokens).split(",")

    for token in token_list:

        token = token.strip()

        if token != "":
            skills.add(token)

skills = sorted(skills)

for skill in skills:

    cursor.execute(
        """
        INSERT OR IGNORE INTO dim_skills(skill_name)
        VALUES(?)
        """,
        (skill,),
    )

conn.commit()

print(f"Unique Skills : {len(skills)}")

# ==========================================================
# BUILD SKILL LOOKUP
# ==========================================================

skill_lookup = dict(
    cursor.execute(
        "SELECT skill_name, skill_key FROM dim_skills"
    ).fetchall()
)

# ==========================================================
# LOAD BRIDGE TABLE
# ==========================================================

print("\nCreating Job-Skill Relationships...")

job_keys = cursor.execute(
    """
    SELECT job_key, job_id
    FROM fact_jobs
    """
).fetchall()

job_lookup = dict()

for key, job in job_keys:
    job_lookup[job] = key

for _, row in df.iterrows():

    job_key = job_lookup[row["job_id"]]

    token_list = str(row["description_tokens"]).split(",")

    for token in token_list:

        token = token.strip()

        if token == "":
            continue

        skill_key = skill_lookup.get(token)

        if skill_key is not None:

            cursor.execute(
                """
                INSERT OR IGNORE INTO job_skills
                VALUES(?,?)
                """,
                (
                    job_key,
                    skill_key,
                ),
            )

conn.commit()

print("Bridge Table Loaded.")

conn.close()

print("\nETL Completed Successfully.")