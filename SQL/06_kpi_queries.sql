SELECT COUNT(*) AS Total_Jobs
FROM fact_jobs;

SELECT COUNT(*) AS Companies
FROM dim_company;

SELECT COUNT(*) AS Locations
FROM dim_location;

SELECT COUNT(*) AS Skills
FROM dim_skills;

SELECT ROUND(AVG(salary_standardized),2)
FROM fact_jobs;

SELECT
ROUND(
100.0 *
SUM(CASE WHEN job_mode='Remote' THEN 1 ELSE 0 END)
/COUNT(*),2)
AS Remote_Percentage
FROM fact_jobs;

SELECT
ROUND(AVG(skill_count),2)
FROM fact_jobs;

