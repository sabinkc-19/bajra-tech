#TASK 1 SQL create scripts
-- serial key for employee id
CREATE SEQUENCE serial_employees
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 
 -- Employee table created
CREATE TABLE Employee (
    EmployeeID integer DEFAULT nextval('serial_employees'::regclass) NOT NULL,
    FirstName character varying NOT NULL,
    MiddleName character varying,
    LastName character varying NOT NULL,
    JoinDate Date,
    MonthlySalary float,
    DeptID integer NOT NULL,
	CONSTRAINT pk_employee PRIMARY KEY (EmployeeID)
);
ALTER TABLE Employee OWNER TO postgres;

-- Department table created
CREATE TABLE Department (
    DeptID integer  NOT NULL,
    DeptName character varying NOT NULL,
    DeptCode character varying,
    ParentDeptID integer NOT NULL,
    ManagerID integer,
    Description character varying,
    Active Boolean NOT NULL,
	CONSTRAINT pk_dept PRIMARY KEY (DeptID)
);
ALTER TABLE Department OWNER TO postgres;


-- Q.1 ANS Query to get total earnings of employees grouped by departments 
select DeptID,
SUM(MonthlySalary * (extract(day from current_date::timestamp - JoinDate::timestamp))/30)::float as total_earnings 
from Employee
group by DeptID;

-- Q.2 ANS Query to get list of employees having worked more than 6 months
select EmployeeID from Employee e
inner join Department d on d.DeptId = e.DeptID
where d.DeptID = 1
group by EmployeeID
having ((extract(day from current_date::timestamp - JoinDate::timestamp)/30) > 6)

-- Q.3 ANS
#firstly manager table created in the db to access manager name through manager ID field
CREATE TABLE Manager (
    ManagerID integer  NOT NULL,
    FullName character varying NOT NULL,
    Address character varying,
    ContactNo bigint NOT NULL,
    CONSTRAINT pk_manager PRIMARY KEY (ManagerID)
);
ALTER TABLE Manager OWNER TO postgres;
#then folowing query executed

select e.EmployeeID, d.DeptName, m.ManagerID, m.FullName as ManagerName
from Department d
join Employee e on e.DeptID = d.DeptID
join Manager m on m.ManagerId = d.ManagerID