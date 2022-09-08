UPDATE Allocations 
SET Allocations.NpmCode = MID(Allocations.AccountCode, 4, 1)
WHERE Allocations.NpmCode <> MID(Allocations.AccountCode, 4, 1);