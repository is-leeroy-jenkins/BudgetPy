INSERT INTO DocumentControlNumbers (RpioCode, RpioName, DocumentType, DocumentNumber,
									DocumentPrefix, DocumentControlNumber)
SELECT DISTINCT RpioCode,
				RpioName,
				DocumentType,
				DocumentNumber,
				substr( DocumentControlNumber, 4, 4 ) AS DocumentPrefix,
				DocumentControlNumber
FROM Obligations
WHERE DocumentControlNumber NOT LIKE % NS %;