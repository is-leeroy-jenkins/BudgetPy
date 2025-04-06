SELECT *
FROM TravelActivity
ORDER BY TravelActivity.EndDate DESC, TravelActivity.BFY DESC, TravelActivity.FundCode,
		 TravelActivity.RpioCode, TravelActivity.AccountCode, TravelActivity.FocCode,
		 TravelActivity.LastName;