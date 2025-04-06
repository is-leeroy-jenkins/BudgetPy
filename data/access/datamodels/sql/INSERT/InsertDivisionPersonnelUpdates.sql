INSERT INTO DivisionAuthority
SELECT *
FROM Rescission
WHERE Rescission.BudgetLevel = '8'
  AND Rescission.BocCode NOT IN ( '10', '17' )
ORDER BY Rescission.BFY DESC, Rescission.FundCode, Rescission.AccountCode, Rescission.BocCode;
