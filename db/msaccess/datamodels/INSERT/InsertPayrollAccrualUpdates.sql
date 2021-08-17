INSERT INTO Payroll
SELECT *
FROM Allocations
WHERE Allocations.BocCode = '10'
ORDER BY Allocations.BFY DESC;


