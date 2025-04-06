INSERT INTO ReferenceTables
SELECT name AS TableName
FROM MSysObjects
WHERE name NOT LIKE "_#%"
  AND name NOT LIKE "#%"
  AND name NOT LIKE "f_#%"
  AND name NOT LIKE "f_%"
  AND name NOT LIKE "tbl_%"
  AND name NOT LIKE "USys%"
  AND name NOT LIKE "MSys%"
  AND name NOT LIKE "ReferenceTables"
  AND name NOT LIKE "%TMP%"
  AND type = 1;
