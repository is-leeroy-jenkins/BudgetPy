PARAMETERS RcCodeArgs TEXT(255);
SELECT PayrollObligations.*
FROM PayrollObligations
WHERE (((PayrollObligations.RcCode) = [RcCodeArgs]));