SELECT *
FROM OpenCommitments
ORDER BY OpenCommitments.BFY DESC, OpenCommitments.FundCode, OpenCommitments.RpioCode, 
    OpenCommitments.AccountCode, OpenCommitments.BocCode;