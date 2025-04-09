select d.name as Department,e.name as Employee,e.salary as Salary from employee e join department d where e.departmentId=d.id and e.salary = (
    SELECT MAX(e2.salary)
    FROM employee e2
    WHERE e2.departmentId = e.departmentId
);

