UPDATE PayrollCostCodes 
INNER JOIN Divisions 
ON Divisions.Code = PayrollCostCodes.RcCode 
SET PayrollCostCodes.DivisionName = Divisions.Title
WHERE PayrollCostCodes.RcCode = Divisions.Code;