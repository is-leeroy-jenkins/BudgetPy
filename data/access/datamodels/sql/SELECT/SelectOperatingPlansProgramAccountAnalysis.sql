SELECT DISTINCT StatusOfFunds.BFY                         AS BFY,
				StatusOfFunds.RpioCode                    AS RpioCode,
				StatusOfFunds.RpioName                    AS RpioName,
				StatusOfFunds.FundCode                    AS FundCode,
				UCase( StatusOfFunds.FundName )           AS FundName,
				StatusOfFunds.AccountCode                 AS AccountCode,
				UCase( StatusOfFunds.ProgramProjectName ) AS ProgramProjectName,
				StatusOfFunds.ProgramProjectCode,
				StatusOfFunds.ProgramAreaCode,
				StatusOfFunds.BocCode                     AS BocCode,
				UCase( StatusOfFunds.BocName )            AS BocName,
				StatusOfFunds.Amount                      AS System,
				CCur( OperatingPlans.Amount )             AS OperatingPlan,
				IIf( StatusOfFunds.Amount - OperatingPlans.Amount < 0, "DECREASE",
					 "INCREASE" )                         AS NET,
				CCur( Round( Abs( StatusOfFunds.Amount - OperatingPlans.Amount ),
							 2 ) )                        AS Delta
FROM StatusOfFunds
		 INNER JOIN OperatingPlans
					ON (StatusOfFunds.RpioCode = OperatingPlans.RpioCode)
						AND (StatusOfFunds.BocCode = OperatingPlans.BocCode)
						AND (StatusOfFunds.AccountCode = OperatingPlans.AccountCode) AND
					   (StatusOfFunds.FundCode = OperatingPlans.FundCode) AND
					   (StatusOfFunds.BFY = OperatingPlans.BFY)
WHERE (((StatusOfFunds.BFY) = '2021')
	AND ((StatusOfFunds.RpioCode) In ( '01', '02', '03', '04', '05', '06', '07', '08', '09', '10' ))
	AND ((StatusOfFunds.BocCode) = '38'))
ORDER BY StatusOfFunds.RpioCode, StatusOfFunds.FundCode, StatusOfFunds.AccountCode,
		 StatusOfFunds.BocCode, StatusOfFunds.BFY DESC;
