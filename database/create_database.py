import sqlite3

conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

cursor.executescript("""

DROP TABLE IF EXISTS job_skills;
DROP TABLE IF EXISTS fact_jobs;

DROP TABLE IF EXISTS dim_company;
DROP TABLE IF EXISTS dim_location;
DROP TABLE IF EXISTS dim_schedule;
DROP TABLE IF EXISTS dim_search_term;
DROP TABLE IF EXISTS dim_skills;


CREATE TABLE dim_company(

company_key INTEGER PRIMARY KEY AUTOINCREMENT,

company_name TEXT UNIQUE

);

CREATE TABLE dim_location(

location_key INTEGER PRIMARY KEY AUTOINCREMENT,

location TEXT UNIQUE

);

CREATE TABLE dim_schedule(

schedule_key INTEGER PRIMARY KEY AUTOINCREMENT,

schedule_type TEXT UNIQUE

);

CREATE TABLE dim_search_term(

search_key INTEGER PRIMARY KEY AUTOINCREMENT,

search_term TEXT UNIQUE

);

CREATE TABLE dim_skills(

skill_key INTEGER PRIMARY KEY AUTOINCREMENT,

skill_name TEXT UNIQUE

);


CREATE TABLE fact_jobs(

job_key INTEGER PRIMARY KEY AUTOINCREMENT,

job_id TEXT,

title TEXT,

company_key INTEGER,

location_key INTEGER,

schedule_key INTEGER,

search_key INTEGER,

posted_at TEXT,

salary_avg REAL,

salary_min REAL,

salary_max REAL,

salary_standardized REAL,

job_mode TEXT,

salary_category TEXT,

skill_count INTEGER,

description_length INTEGER,

FOREIGN KEY(company_key)
REFERENCES dim_company(company_key),

FOREIGN KEY(location_key)
REFERENCES dim_location(location_key),

FOREIGN KEY(schedule_key)
REFERENCES dim_schedule(schedule_key),

FOREIGN KEY(search_key)
REFERENCES dim_search_term(search_key)

);


CREATE TABLE job_skills(

job_key INTEGER,

skill_key INTEGER,

PRIMARY KEY(job_key,skill_key),

FOREIGN KEY(job_key)
REFERENCES fact_jobs(job_key),

FOREIGN KEY(skill_key)
REFERENCES dim_skills(skill_key)

);

""")

conn.commit()

conn.close()

print("Database Created Successfully")