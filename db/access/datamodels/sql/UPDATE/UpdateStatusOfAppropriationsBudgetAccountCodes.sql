UPDATE StatusOfAppropriations 
SET StatusOfAppropriations.OmbAccountCode = "020-00-" & StatusOfAppropriations.OmbAccountCode
WHERE LEN(StatusOfAppropriations.OmbAccountCode) = 4;