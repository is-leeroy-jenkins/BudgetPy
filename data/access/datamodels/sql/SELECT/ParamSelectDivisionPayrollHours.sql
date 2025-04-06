PARAMETERS RcCodeArgs TEXT(255);
SELECT PayrollHours.*
FROM PayrollHours
WHERE (((PayrollHours.RcCode) = [RcCodeArgs]));