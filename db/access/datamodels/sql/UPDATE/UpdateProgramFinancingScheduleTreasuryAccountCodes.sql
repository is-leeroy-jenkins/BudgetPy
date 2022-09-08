UPDATE ProgramFinancingSchedule 
SET ProgramFinancingSchedule.TreasuryAgencyCode = '0' & ProgramFinancingSchedule.TreasuryAgencyCode
WHERE LEN(ProgramFinancingSchedule.TreasuryAgencyCode) = 2;