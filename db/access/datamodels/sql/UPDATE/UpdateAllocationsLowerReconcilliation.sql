UPDATE Allocations 
INNER JOIN LowerReconcilliation 
ON Allocations.PrcId = LowerReconcilliation.PrcId 
SET Allocations.Amount = LowerReconcilliation.System
WHERE Allocations.PrcId = LowerReconcilliation.PrcId;