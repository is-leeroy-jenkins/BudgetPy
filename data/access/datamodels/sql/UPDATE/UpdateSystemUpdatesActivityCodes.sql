UPDATE SystemUpdates
	INNER JOIN ActivityCodes
ON SystemUpdates.ActivityCode = ActivityCodes.Code
SET SystemUpdates.ActivityCode = ActivityCodes.Code, 
    SystemUpdates.ActivityName = ActivityCodes.Title;