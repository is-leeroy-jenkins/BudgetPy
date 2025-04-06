UPDATE ProgramFinancingSchedule
SET ProgramFinancingSchedule.LineDescription = 'NOT SPECIFIED'
WHERE IsNull( ProgramFinancingSchedule.LineDescription )
   OR ProgramFinancingSchedule.LineDescription = ' ';