INSERT INTO OperatingPlan
SELECT *
FROM ExternalOperatingPlan
ORDER BY ExternalOperatingPlan.BFY DESC, ExternalOperatingPlan.FundCode,
		 ExternalOperatingPlan.AccountCode, ExternalOperatingPlan.BocCode;

