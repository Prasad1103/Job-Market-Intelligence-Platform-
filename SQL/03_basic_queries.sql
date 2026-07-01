-- SQLite
SELECT COUNT(*) AS total_jobs
FROM fact_jobs;


SELECT COUNT(*) AS total_companies
FROM dim_company;

SELECT COUNT(*) AS total_locations
FROM dim_location;

SELECT COUNT(*) AS total_skills
FROM dim_skills;

SELECT ROUND(AVG(salary_standardized),2) AS average_salary
FROM fact_jobs;

SELECT MAX(salary_standardized)
FROM fact_jobs;

SELECT MIN(salary_standardized)
FROM fact_jobs
WHERE salary_standardized IS NOT NULL;

SELECT ROUND(AVG(skill_count),2) AS average_skills
FROM fact_jobs;