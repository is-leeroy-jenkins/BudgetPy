PARAMETERS BudgetLevelArgs Text ( 255 ), RpioArgs Text ( 255 ), AhCodeArgs Text ( 255 ), FiscalYearArgs Text ( 255 ), FundCodeArgs Text ( 255 ), OrgCodeArgs Text ( 255 ), AccountCodeArgs Text ( 255 ), BocCodeArgs Text ( 255 ), RcCodeArgs Text ( 255 ), AmountArgs Text ( 255 ), PrcIdArgs Short;
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
