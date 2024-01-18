INSERT INTO DivisionPersonnel (RcCode, DivisionName, EmployeeId, LastName, FirstName, JobTitle,
							   Grade, Step, HireDate, LastIncrease, GradeEntry, StepEntry,
							   WigiDueDate, Tenure, HrOrgName, Email, MailCode, PhoneNumber, Office,
							   SupervisorId, SupervisorLastName, SupervisorFirstName, Supervisor)
SELECT DISTINCT Employees.RcCode,
				DLookUp( "Title", "Divisions",
						 "Divisions.Code = '" & RcCode & "'" )                  AS DivisionName,
				EmployeeData.EmployeeId,
				EmployeeData.LastName,
				EmployeeData.FirstName,
				EmployeeData.JobTitle,
				EmployeeData.Grade,
				EmployeeData.Step,
				EmployeeData.HireDate,
				EmployeeData.LastIncrease,
				EmployeeData.GradeEntry,
				EmployeeData.StepEntry,
				EmployeeData.WigiDue,
				DateDiff( "yyyy", HireDate, Now( ) )                            AS Tenure,
				EmployeeData.HrOrgName,
				LocatorData.Email,
				LocatorData.MailCode,
				LocatorData.PhoneNumber,
				LocatorData.Office,
				DLookUp( "SupervisorId", "EmployeeData",
						 "EmployeeData.EmployeeId = '" & [SupervisorId] & "'" ) AS SupervisorId,
				DLookUp( "LastName", "EmployeeData",
						 "EmployeeData.EmployeeId = '" & [SupervisorId] &
						 "'" )                                                  AS SupervisorLastName,
				DLookUp( "FirstName", "EmployeeData",
						 "EmployeeData.EmployeeId = '" & [SupervisorId] &
						 "'" )                                                  AS SupervisorFirstName,
				LEFT( SupervisorFirstName, 1 ) & ". " & SupervisorLastName      AS Supervisor
FROM LocatorData
		 INNER JOIN (Employees INNER JOIN EmployeeData
					 ON Employees.EpaNumber = EmployeeData.EmployeeId)
					ON (LocatorData.FirstName = EmployeeData.FirstName) AND
					   (LocatorData.LastName = EmployeeData.LastName)
ORDER BY Employees.RcCode, EmployeeData.LastName;

