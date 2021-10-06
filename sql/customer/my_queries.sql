SELECT * 
FROM company;

SELECT *
FROM facility;


SELECT facility.id as "Facility ID", facility.company_name, facility.size_sq_ft, facility.city, facility.state
FROM company
JOIN facility
ON company.company_name = facility.company_name
WHERE facility.primary_use = "farm"
;
