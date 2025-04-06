UPDATE SiteActivity
SET SiteActivity.EndDate = 'NS'
WHERE IsNull( SiteActivity.EndDate );