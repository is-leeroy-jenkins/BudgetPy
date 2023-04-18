UPDATE Actuals 
SET Actuals.AccountCode = REPLACE(Actuals.AccountCode, LEFT(Actuals.AccountCode, 3), '000')
WHERE NOT IsNull(Actuals.AccountCode);
