## Prepare Workspace

- Add an incremental primary key column in the db.csv file
- Build the project using docker compose
```
docker-compose up --build
```
- Once both containers are running in the same network run the following
```
docker exec db mkdir /home/db
docker cp .\db\db.csv db:/home\db\db.csv
docker exec -it db mysql -uroot -proot --local-infile=1
```
- Inside Mysql run the following 
```
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
LOAD DATA LOCAL INFILE '/home/db/db.csv'
    INTO TABLE ibm
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 ROWS;
GRANT ALL PRIVILEGES ON multiverse.* to 'rabie'@'%';
```
- To avoid connecting with the root account we can now connect to the mysql database using the user "rabie"

## Handled Operations
NB: These results are obtained after editing the database (Adding and deleting records).
- http://localhost:5000/get?gender=Male ===> "There are 880 Males in this database"
- http://localhost:5000/id?id=10 ===> "The record with ID=10 is 36 years old"
- http://localhost:5000/delete?id=7 ===> "The record with ID=7 has been deleted"
- http://localhost:5000/getall ===> "There are a total of 1482 records in the dataset"
- http://localhost:5000/insert ===> "Record Inserted with id = 1470" {Inserts a dummy record}
```
dummy_record = {'age': 25, 'attrition': 'Yes', 'business_travel': "Travel_Rarely", 'daily_rate': 5000,
                'distance_from_home': 5, 'education': "10", 'education_field': "ECE"}
```
## Choices and Assumptions
- MySql is an open source database and has a large community so debugging should be easy.
- The containers have to be in the same network to be able to communicate and hence, it is recommended to use docker composer. 

