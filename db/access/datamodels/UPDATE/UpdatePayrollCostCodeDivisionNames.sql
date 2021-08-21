UPDATE PayrollCostCodes 
INNER JOIN HumanResourceOrganizations 
ON HumanResourceOrganizations.Code = PayrollCostCodes.HrOrgCode 
SET PayrollCostCodes.HrOrgName = HumanResourceOrganizations.Name
WHERE PayrollCostCodes.HrOrgCode = HumanResourceOrganizations.Code
AND (IsNull(PayrollCostCodes.HrOrgName) 
    OR PayrollCostCodes.HrOrgName <> HumanResourceOrganizations.Name);