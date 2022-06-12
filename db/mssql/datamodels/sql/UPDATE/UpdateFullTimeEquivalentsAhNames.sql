UPDATE FullTimeEquivalents
INNER JOIN Allocations
ON FullTimeEquivalents.RpioCode = Allocations.RpioCode
SET FullTimeEquivalents.RpioName = Allocations.RpioName
WHERE FullTimeEquivalents.RpioName <> Allocations.RpioName;