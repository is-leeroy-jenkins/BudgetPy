INSERT INTO EmployeeLeave
SELECT EmployeeData.LastName                                                AS LastName,
	   EmployeeData.FirstName                                               AS FirstName,
	   EmployeeData.EmployeeId                                              AS EpaNumber,
	   Sum( EmployeeData.HoursEarnedYearToDate )                            AS HoursEarnedYearToDate,
	   Sum( EmployeeData.CarryoverHours )                                   AS CarryoverHours,
	   Sum( EmployeeData.HoursAdjustedYearToDate )                          AS HoursAdjustedYearToDate,
	   Sum( EmployeeData.HoursBalance )                                     AS HoursBalance,
	   Sum( EmployeeData.ProjectedAnnualHours )                             AS ProjectedAnnualHours,
	   Sum( EmployeeData.ProjectedNextPeriodHours )                         AS ProjectedNextPeriodHours,
	   Sum( EmployeeData.HoursTakenYearToDate )                             AS HoursTakenYearToDate,
	   DLookUp( "RcCode", "Employees",
				"Employees.EpaNumber = '" & EmployeeData.EmployeeId & "'" ) AS RcCode,
	   DLookUp( "DivisionName", "Employees",
				"Employees.EpaNumber = '" & EmployeeData.EmployeeId & "'" ) AS DivisionName
FROM EmployeeData
GROUP BY EmployeeData.EmployeeId, EmployeeData.LastName, EmployeeData.FirstName
HAVING ((Not (EmployeeData.LastName) = IsNull( [EmployeeData].[LastName] )))
ORDER BY EmployeeData.LastName;
