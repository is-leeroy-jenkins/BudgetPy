UPDATE Allocations
SET Allocations.GoalCode      = LEFT( Allocations.AccountCode, 1 ),
	Allocations.ObjectiveCode = RIGHT( LEFT( Allocations.AccountCode, 3 ), 2 );