INSERT INTO WorkCodes (Code, Name)
SELECT DISTINCT WorkCode as Code, WorkCodeName AS Name
FROM PayrollActivity;