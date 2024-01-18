CREATE VIEW WorkCodes
AS
SELECT DISTINCT WorkCode AS Code, WorkCodeName AS Name
FROM PayrollActivity;