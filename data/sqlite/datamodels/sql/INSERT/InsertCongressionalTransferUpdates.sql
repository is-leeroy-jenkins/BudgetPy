INSERT INTO Allocations ( RPIO, BudgetLevel, AhCode, BFY, FundCode, OrgCode, AccountCode, ActivityCode, BocCode, RcCode, Amount, AllocationRatio, FundName, BocName, Division, DivisionName, NpmCode, NpmName, ProgramProjectCode, ProgramProjectName, ProgramAreaCode, ProgramAreaName, GoalCode, GoalName, ObjectiveCode, ObjectiveName )
VALUES ([Forms]![AccountEditor]![RpioCodeTextBox], [Forms]![AccountEditor]![BudgetLevelTextBox], [Forms]![AccountEditor]![AhTextBox], [Forms]![AccountEditor]![BfyTextBox], [Forms]![AccountEditor]![FundCodeTextBox], [Forms]![AccountEditor]![OrgCodeTextBox], [Forms]![AccountEditor]![AccountCodeTextBox], [Forms]![AccountEditor]![ActivityCodeTextBox], [Forms]![AccountEditor]![BocCodeTextBox], [Forms]![AccountEditor]![RcCodeTextBox], 0, 0, 
Nz(DLookUp("FundName","Allocations","Allocations.FundCode=[FundCode]"),"NS"), 
Nz(DLookUp("BocName","Allocations","Allocations.BocCode=[BocCode]"),"NS"), 
Nz(DLookUp("Division","Allocations","Allocations.RcCode=[RcCode]"),"NS"),
Nz(DLookUp("DivisionName","Allocations","Allocations.RcCode=[RcCode]"),"NS"), Nz(MID([Forms]![AccountEditor]![AccountCodeTextBox], 3, 2), "NS"), 
Nz(DLookUp("NpmName", "Allocations", "Allocations.NpmCode=MID([Forms]![AccountEditor]![AccountCodeTextBox], 3, 2)"), "NS"), Nz(DLookUp("ProgramProjectCode", "Allocations", "Allocations.ProgramProjectCode=MID([Forms]![AccountEditor]![AccountCodeTextBox], 5, 2)"), "NS"), 
Nz(DLookUp("ProgramProjectName", "Allocations", "Allocations.ProgramProjectCode=MID([Forms]![AccountEditor]![AccountCodeTextBox], 5, 2)"), "NS"), 
Nz(DLookUp("ProgramAreaCode", "Allocations", "Allocations.ProgramProjectCode=MID([Forms]![AccountEditor]![AccountCodeTextBox], 5, 2)"), "NS"), 
Nz(DLookUp("ProgramAreaName", "Allocations", "Allocations.ProgramProjectCode=MID([Forms]![AccountEditor]![AccountCodeTextBox], 5, 2)"), "NS"), 
Nz(DLookUp("GoalCode", "Allocations", "Allocations.GoalCode=Nz(LEFT([Forms]![AccountEditor]![AccountCodeTextBox], 0, 1)"), "0"), 
Nz(DLookUp("GoalName", "Allocations", "Allocations.GoalCode=Nz(LEFT([Forms]![AccountEditor]![AccountCodeTextBox], 0, 1)"), "0"), 
Nz(DLookUp("ObjectiveCode", "Allocations", "Allocations.ObjectiveCode=Nz(MID([Forms]![AccountEditor]![AccountCodeTextBox], 1, 2)"), "00"),
 Nz(DLookUp("ObjectiveName", "Allocations", "Allocations.ObjectiveCode=Nz(MID([Forms]![AccountEditor]![AccountCodeTextBox], 1, 2)"), "00"));
