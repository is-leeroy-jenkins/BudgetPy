INSERT INTO BenefitCharges
SELECT *
FROM PeoplePlus
WHERE PeoplePlus.ReportingCodeName NOT IN ("Regular Basic Pay", "Telework Regular Hours")
AND NOT IsNull(PeoplePlus.Hours);
