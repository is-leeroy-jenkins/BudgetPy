INSERT INTO AppropriationLevelAuthority
SELECT DISTINCT StatusOfAppropriations.BFY AS BFY, 
StatusOfAppropriations.EFY AS EFY,
StatusOfAppropriations.AppropriationFundCode AS FundCode, 
StatusOfAppropriations.BudgetAccountCode AS BudgetAccountCode,
StatusOfAppropriations.TreasurySymbol As TreasuryAccountCode,
SUM(StatusOfAppropriations.TotalBudgeted) AS Budgeted, 
SUM(StatusOfAppropriations.TotalCarriedForwardIn) AS CarryOver, 
SUM(StatusOfAppropriations.TotalActualReimbursements) AS TotalReimbursements, 
SUM(StatusOfAppropriations.TotalAccrualRecoveries) AS TotalRecoveries,
SUM(StatusOfAppropriations.TotalBudgeted) + 
SUM(StatusOfAppropriations.TotalCarriedForwardIn) + 
SUM(StatusOfAppropriations.TotalActualReimbursements) + 
SUM(StatusOfAppropriations.TotalAccrualRecoveries) AS TotalAuthority
FROM StatusOfAppropriations
WHERE StatusOfAppropriations.Availability <> "CANCELLED"
AND StatusOfAppropriations.Availability <> "EXPIRED"
GROUP BY StatusOfAppropriations.BFY, StatusOfAppropriations.EFY, StatusOfAppropriations.AppropriationFundCode,StatusOfAppropriations.BudgetAccountCode, StatusOfAppropriations.TreasurySymbol
HAVING StatusOfAppropriations.BFY IN ("2022", "2023") 
AND (SUM(StatusOfAppropriations.TotalBudgeted) > 0 
OR SUM(StatusOfAppropriations.TotalCarriedForwardIn) > 0
OR SUM(StatusOfAppropriations.TotalActualReimbursements) > 0
OR SUM(StatusOfAppropriations.TotalAccrualRecoveries) > 0);

