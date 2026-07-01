
SELECT
    f.job_key,
    f.title,
    c.company_name,
    l.location,
    s.schedule_type,
    st.search_term,
    f.salary_standardized,
    f.job_mode,
    f.salary_category,
    f.skill_count
FROM fact_jobs f
JOIN dim_company c
    ON f.company_key = c.company_key
JOIN dim_location l
    ON f.location_key = l.location_key
JOIN dim_schedule s
    ON f.schedule_key = s.schedule_key
JOIN dim_search_term st
    ON f.search_key = st.search_key;