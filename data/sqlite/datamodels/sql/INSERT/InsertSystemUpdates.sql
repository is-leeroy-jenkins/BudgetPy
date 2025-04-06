INSERT INTO Transfers
SELECT *
FROM [Data.accdb].ExternalTransfers
ORDER BY ExternalTransfers.ProcessedDate DESC;


