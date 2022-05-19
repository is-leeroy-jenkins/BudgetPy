PARAMETERS PrcIdArgs Short, AmountArgs IEEEDouble;
UPDATE Allocations SET Allocations.Amount = [AmountArgs]
WHERE (((Allocations.PrcId)=[PrcIdArgs]));
