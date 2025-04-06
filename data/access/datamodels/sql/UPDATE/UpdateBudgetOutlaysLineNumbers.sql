UPDATE BudgetOutlays
SET BudgetOutlays.LineNumber = LEFT( BudgetOutlays.LineNumber, 4 ) & "-" &
							   RIGHT( BudgetOutlays.LineNumber, 2 )
WHERE LEN( BudgetOutlays.LineNumber ) = 6;