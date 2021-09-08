PARAMETERS RpioArgs TEXT(255), BudgetLevelArgs TEXT(255), AhCodeArgs TEXT(255), FiscalYearArgs TEXT(255), FundCodeArgs TEXT(255), OrgCodeArgs TEXT(255), AccountCodeArgs TEXT(255), ActivityCodeArgs TEXT(255), BocCodeArgs TEXT(255), RcCodeArgs TEXT(255), AmountArgs DOUBLE;
INSERT INTO Allocations ( RPIO, BudgetLevel, AhCode, BFY, FundCode, OrgCode, AccountCode, ActivityCode, BocCode, RcCode, Amount, AllocationRatio, FundName, BocName, Division, DivisionName, NpmCode, NpmName, ProgramProjectCode, ProgramProjectName, ProgramAreaCode, ProgramAreaName, GoalCode, GoalName, ObjectiveCode, ObjectiveName )
VALUES (RpioCodeArgs, BudgetLevelArgs, AhCodeArgs, FiscalYearArgs, FundCodeArgs, OrgCodeArgs, AccountCodeArgs, ActivityCodeArgs, BocCodeArgs, RcCodeArgs, AmountArgs, 0, 
Nz(DLookUp("FundName","Allocations","Allocations.FundCode=[FundCodeArgs]"),"NS"), 
Nz(DLookUp("BocName","Allocations","Allocations.BocCode=[BocCodeArgs]"),"NS"), 
Nz(DLookUp("Division","Allocations","Allocations.RcCode=[RcCodeArgs]"),"NS"), 
Nz(DLookUp("DivisionName","Allocations","Allocations.RcCode=[RcCodeArgs]"),"NS"), 
Nz(MID(AccountCodeArgs, 3, 2), "NS"), 
Nz(DLookUp("NpmName", "Allocations", "Allocations.NpmCode=MID(AccountCodeArgs, 3, 2)"), "NS"), 
Nz(DLookUp("ProgramProjectCode", "Allocations", "Allocations.ProgramProjectCode=MID(AccountCodeArgs, 5, 2)"), "NS"), 
Nz(DLookUp("ProgramProjectName", "Allocations", "Allocations.ProgramProjectCode=MID(AccountCodeArgs, 5, 2)"), "NS"), 
Nz(DLookUp("ProgramAreaCode", "Allocations", "Allocations.ProgramProjectCode=MID(AccountCodeArgs, 5, 2)"), "NS"), 
Nz(DLookUp("ProgramAreaName", "Allocations", "Allocations.ProgramProjectCode=MID(AccountCodeArgs, 5, 2)"), "NS"), 
Nz(DLookUp("GoalCode", "Allocations", "Allocations.GoalCode=Nz(LEFT(AccountCodeArgs, 0, 1)"), "NS"), 
Nz(DLookUp("GoalName", "Allocations", "Allocations.GoalCode=Nz(LEFT(AccountCodeArgs, 0, 1)"), "NS"), 
Nz(DLookUp("ObjectiveCode", "Allocations", "Allocations.ObjectiveCode=Nz(MID(AccountCodeArgs, 1, 2)"), "NS"), 
Nz(DLookUp("ObjectiveName", "Allocations", "Allocations.ObjectiveCode=Nz(MID(AccountCodeArgs, 1, 2)"), "NS"));