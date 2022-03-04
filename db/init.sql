CREATE DATABASE multiverse;
use multiverse;
CREATE TABLE ibm (id INT NOT NULL PRIMARY KEY, age INT, attrition CHAR(200), business_travel CHAR(200), daily_rate FLOAT,
department CHAR(200), distance_from_home FLOAT, education INT, education_field CHAR(200),
employee_count INT, employee_number INT, environment_satisfaction INT, gender CHAR(200),
hourly_rate FLOAT, job_involvment FLOAT, job_level INT, job_role CHAR(200), job_satisfaction  FLOAT,
marital_status CHAR(200), monthly_income FLOAT, monthy_rate FLOAT, num_companies_worked INT, over18 CHAR(200),
over_time CHAR(200), percent_salary_hike FLOAT, performance_rating FLOAT, relationship_satisfaction FLOAT,
standard_hours FLOAT, stock_option_level FLOAT, total_working_years FLOAT, training_times_last_year INT,
work_life_balance FLOAT, years_at_company FLOAT, years_in_role FLOAT, years_since_last_promotion FLOAT,
years_with_current_manager FLOAT);

set global local_infile=true;

CREATE USER 'rabie' IDENTIFIED BY 'rabie';

GRANT ALL PRIVILEGES ON multiverse.* to 'rabie'@'%';