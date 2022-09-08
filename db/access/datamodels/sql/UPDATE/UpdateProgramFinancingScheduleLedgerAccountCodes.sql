UPDATE ProgramFinancingSchedule 
SET ProgramFinancingSchedule.LedgerAccountCode = 'NS'
WHERE IsNull(ProgramFinancingSchedule.LedgerAccountCode) 
OR ProgramFinancingSchedule.LedgerAccountCode = ' ';