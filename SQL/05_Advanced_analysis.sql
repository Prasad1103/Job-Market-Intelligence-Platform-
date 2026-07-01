SELECT
c.company_name,
ROUND(AVG(f.salary_standardized),2) AS avg_salary
FROM fact_jobs f
JOIN dim_company c
ON f.company_key=c.company_key
WHERE salary_standardized IS NOT NULL
GROUP BY c.company_name
HAVING COUNT(*)>=5
ORDER BY avg_salary DESC
LIMIT 15;

SELECT
l.location,
ROUND(AVG(salary_standardized),2) AS avg_salary
FROM fact_jobs f
JOIN dim_location l
ON f.location_key=l.location_key
GROUP BY l.location
ORDER BY avg_salary DESC
LIMIT 20;

SELECT
s.schedule_type,
ROUND(AVG(salary_standardized),2) AS avg_salary
FROM fact_jobs f
JOIN dim_schedule s
ON f.schedule_key=s.schedule_key
GROUP BY s.schedule_type;

SELECT
ds.skill_name,
COUNT(*) AS demand
FROM job_skills js
JOIN dim_skills ds
ON js.skill_key=ds.skill_key
GROUP BY ds.skill_name
ORDER BY demand DESC
LIMIT 20;

SELECT
c.company_name,
ROUND(AVG(skill_count),2) AS avg_skills
FROM fact_jobs f
JOIN dim_company c
ON f.company_key=c.company_key
GROUP BY c.company_name
HAVING COUNT(*)>=10
ORDER BY avg_skills DESC
LIMIT 20;