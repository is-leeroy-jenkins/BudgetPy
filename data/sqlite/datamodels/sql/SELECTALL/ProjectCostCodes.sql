SELECT *
FROM ProjectCostCodes
ORDER BY ProjectCostCodes.BFY DESC, ProjectCostCodes.FundCode,
		 ProjectCostCodes.RpioCode, ProjectCostCodes.AccountCode, ProjectCostCodes.BocCode;