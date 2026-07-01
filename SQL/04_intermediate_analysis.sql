SELECT
    c.company_name,
    COUNT(*) AS total_jobs
FROM fact_jobs f
JOIN dim_company c
ON f.company_key=c.company_key
GROUP BY c.company_name
ORDER BY total_jobs DESC
LIMIT 10;

SELECT
    l.location,
    COUNT(*) AS total_jobs
FROM fact_jobs f
JOIN dim_location l
ON f.location_key=l.location_key
GROUP BY l.location
ORDER BY total_jobs DESC
LIMIT 10;

SELECT
    s.schedule_type,
    COUNT(*) AS jobs
FROM fact_jobs f
JOIN dim_schedule s
ON f.schedule_key=s.schedule_key
GROUP BY s.schedule_type
ORDER BY jobs DESC;

SELECT
    st.search_term,
    COUNT(*) AS jobs
FROM fact_jobs f
JOIN dim_search_term st
ON f.search_key=st.search_key
GROUP BY st.search_term
ORDER BY jobs DESC;

SELECT
job_mode,
COUNT(*) AS jobs
FROM fact_jobs
GROUP BY job_mode;

SELECT
salary_category,
COUNT(*) AS jobs
FROM fact_jobs
GROUP BY salary_category;