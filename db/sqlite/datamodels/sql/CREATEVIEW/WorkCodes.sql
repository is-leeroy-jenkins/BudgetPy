CREATE VIEW IF NOT EXISTS "WorkCodes" 
AS SELECT DISTINCT WorkCode AS Code, WorkCodeName AS Name 
FROM PayrollActivity;