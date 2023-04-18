INSERT INTO ApplicationTables
SELECT name AS TableName, "EXECUTION" AS Model
FROM [Data.accdb].MSysObjects
WHERE name NOT LIKE "_#%" AND
    name NOT LIKE "#%" AND
    name NOT LIKE "f_#%" AND
    name NOT LIKE "f_%" AND
    name NOT LIKE "tbl_%" AND
    name NOT LIKE "USys%" AND
    name NOT LIKE "%~TMP%" AND
    name NOT LIKE "MSys%" AND 
    name NOT LIKE "ExecutionTables%" AND
    name NOT LIKE "ApplicationTables%" AND
    type = 1
ORDER BY name;

