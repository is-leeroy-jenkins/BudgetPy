PARAMETERS BudgetLevelArgs TEXT( 255 ), RpioArgs TEXT( 255 ), AhCodeArgs TEXT( 255 ), FiscalYearArgs TEXT( 255 ),       FundCodeArgs TEXT( 255 ), OrgCodeArgs TEXT( 255 ), AccountCodeArgs TEXT( 255 ), BocCodeArgs TEXT( 255 ), RcCodeArgs TEXT( 255 ), AmountArgs TEXT( 255 ), PrcIdArgs Short;
UPDATE Allocations 
SET Allocations.RPIO = [RpioArgs], 
    Allocations.AhCode = [AhCodeArgs], 
    Allocations.BFY = [FiscalYearArgs], 
    Allocations.FundCode = [FundCodeArgs], 
    Allocations.OrgCode = [OrgCodeArgs], 
    Allocations.AccountCode = [AccountCodeArgs], 
    Allocations.BocCode = [BocCodeArgs], 
    Allocations.RcCode = [RcCodeArgs], 
    Allocations.Amount = [AmountArgs]
WHERE (((Allocations.PrcId)=[PrcIdArgs]));
