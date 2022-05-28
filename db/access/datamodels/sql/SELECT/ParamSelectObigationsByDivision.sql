PARAMETERS RcCodeArgs Text ( 255 );
SELECT TravelObligations.*
FROM TravelObligations
WHERE TravelObligations.RcCode = [RcCodeArgs];
