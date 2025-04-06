UPDATE SiteActivity
SET SiteActivity.StartDate = 'NS'
WHERE IsNull( SiteActivity.StartDate );
