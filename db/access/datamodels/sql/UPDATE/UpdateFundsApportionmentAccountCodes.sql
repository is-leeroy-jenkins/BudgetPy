UPDATE Funds 
SET Funds.ApportionmentAccountCode = IIF(Funds.EFY = 'NS', "68-" & Funds.MainAccount & ' /X', 
"68-" & Funds.MainAccount & " " & Funds.BFY & "/" & Funds.EFY);