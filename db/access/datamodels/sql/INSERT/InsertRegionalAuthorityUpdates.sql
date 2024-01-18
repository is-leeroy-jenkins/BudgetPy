INSERT INTO RegionalAuthority
SELECT *
FROM Rescission
WHERE Rescission.BudgetLevel = 7
  AND Rescission.BocCode <> 17
ORDER BY Rescission.BFY DESC, Rescission.FundCode, Rescission.AccountCode, Rescission.BocCode;
