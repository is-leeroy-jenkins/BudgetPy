UPDATE Funds 
SET Funds.TreasuryAccountCode = IIF( Funds.MultiyearIndicator <> 'NS' AND Funds.AllocationTransferAgency = 'NS', 
Funds.AgencyIdentifier & 'X' & Funds.MainAccount, 
IIF(Funds.MultiyearIndicator = 'NS' AND Funds.AllocationTransferAgency <> 'NS', Funds.AllocationTransferAgency & '-' & Funds.AgencyIdentifier &  'X' & Funds.MainAccount, 
IIF( Funds.MultiyearIndicator = 'NS' AND Funds.AllocationTransferAgency <> 'NS' AND Funds.EFY <> 'NS', Funds.AgencyIdentifier & RIGHT(Funds.BFY, 2) & '/' & RIGHT(Funds.EFY, 2) & Funds.MainAccount, Funds.AgencyIdentifier & 'X' & Funds.MainAccount)));