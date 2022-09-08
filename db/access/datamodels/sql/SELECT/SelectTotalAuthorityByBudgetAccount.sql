SELECT DISTINCT AppropriationLevelAuthority.BudgetAccountCode AS [OMB Account Code], AppropriationLevelAuthority.BudgetAccountName AS [OMB Account Name], AppropriationLevelAuthority.FundCode, AppropriationLevelAuthority.FundName, SUM(Budgeted) AS Budgeted, SUM(Posted) AS Posted, SUM(CarryOut) AS CarryOut, SUM(CarryIn) AS CarryIn, SUM(EstimatedReimbursements) AS EstimatedReimbursements, SUM(EstimatedRecoveries) AS EstimatedRecoveries
FROM AppropriationLevelAuthority
WHERE NOT IsNull(AppropriationLevelAuthority.BudgetAccountCode)
GROUP BY AppropriationLevelAuthority.BudgetAccountCode, AppropriationLevelAuthority.BudgetAccountName, AppropriationLevelAuthority.FundCode, AppropriationLevelAuthority.FundName
ORDER BY AppropriationLevelAuthority.FundCode;