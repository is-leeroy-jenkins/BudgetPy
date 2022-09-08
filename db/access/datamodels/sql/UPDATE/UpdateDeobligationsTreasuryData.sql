UPDATE Funds 
SET Funds.ApportionmentAccountCode = IIF(Funds.EFY = 'NS', "68-" & Funds.MAIN & ' /X', 
"68-" & Funds.MAIN & " " & Funds.BFY & "/" & Funds.EFY);