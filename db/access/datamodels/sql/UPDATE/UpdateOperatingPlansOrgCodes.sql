UPDATE OperatingPlans 
SET OperatingPlans.OrgCode = '06'
WHERE OperatingPlans.OrgCode <> '06' 
AND OperatingPlans.OrgCode NOT LIKE '6A%' 
AND OperatingPlans.OrgCode NOT LIKE '0600%';