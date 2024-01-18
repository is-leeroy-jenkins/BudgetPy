UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '01*A',
	StateGrantObligations.StateName = 'TRIBAL RESOURCES – REGION 1'
WHERE StateGrantObligations.RpioCode = '01'
  AND IsNull( StateGrantObligations.StateCode )
  AND StateGrantObligations.ProgramProjectCode IN ( '15', '17' );

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '01*A',
	StateGrantObligations.StateName = 'TRIBAL RESOURCES – REGION 1'
WHERE StateGrantObligations.RpioCode = '01'
  AND IsNull( StateGrantObligations.StateCode )
  AND (StateGrantObligations.OrgCode LIKE '01%T'
	OR StateGrantObligations.OrgCode LIKE '01T%');

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0110',
	StateGrantObligations.StateName = 'CONNECTICUT'
WHERE (StateGrantObligations.RpioCode = '01'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '01%1'
		OR StateGrantObligations.OrgCode LIKE '011%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0120',
	StateGrantObligations.StateName = 'MAINE'
WHERE (StateGrantObligations.RpioCode = '01'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '01%2'
		OR StateGrantObligations.OrgCode LIKE '012%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0130',
	StateGrantObligations.StateName = 'MASSACHUSETTS'
WHERE (StateGrantObligations.RpioCode = '01'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '01%3'
		OR StateGrantObligations.OrgCode LIKE '013%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0140',
	StateGrantObligations.StateName = 'NEW HAMPSHIRE'
WHERE (StateGrantObligations.RpioCode = '01'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '01%4'
		OR StateGrantObligations.OrgCode LIKE '014%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0150',
	StateGrantObligations.StateName = 'RHODE ISLAND'
WHERE (StateGrantObligations.RpioCode = '01'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '01%5'
		OR StateGrantObligations.OrgCode LIKE '015%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0160',
	StateGrantObligations.StateName = 'VERMONT'
WHERE (StateGrantObligations.RpioCode = '01'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '01%6'
		OR StateGrantObligations.OrgCode LIKE '016%');

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '01*A',
	StateGrantObligations.StateName = 'TRIBAL RESOURCES – REGION 1'
WHERE (StateGrantObligations.RpioCode = '01'
	AND (StateGrantObligations.OrgName LIKE '%TRIB%'
		OR StateGrantObligations.OrgName LIKE '%NATIO%'
		OR StateGrantObligations.OrgName LIKE '%BAND%'
		OR StateGrantObligations.OrgName LIKE '%CREEK%'
		OR StateGrantObligations.OrgName LIKE '%SOUI%'
		OR StateGrantObligations.OrgName LIKE '%INDIA%')
	AND IsNull( StateGrantObligations.StateCode ));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '01*X',
	StateGrantObligations.StateName = 'UNDISTRIBUTED NATIONAL RESOURCES – REGION 1'
WHERE StateGrantObligations.RpioCode = '01'
  AND IsNull( StateGrantObligations.StateCode )
  AND IsNull( StateGrantObligations.StateCode );


--****************************
--      REGION 2
--****************************

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '02*A',
	StateGrantObligations.StateName = 'TRIBAL RESOURCES – REGION 2'
WHERE StateGrantObligations.RpioCode = '02'
  AND IsNull( StateGrantObligations.StateCode )
  AND StateGrantObligations.ProgramProjectCode IN ( '15', '17' );

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '02*A',
	StateGrantObligations.StateName = 'TRIBAL RESOURCES – REGION 2'
WHERE StateGrantObligations.RpioCode = '02'
  AND IsNull( StateGrantObligations.StateCode )
  AND (StateGrantObligations.OrgCode LIKE '02%T'
	OR StateGrantObligations.OrgCode LIKE '02T%');

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0210',
	StateGrantObligations.StateName = 'NEW JERSEY'
WHERE (StateGrantObligations.RpioCode = '02'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '02%1'
		OR StateGrantObligations.OrgCode LIKE '021%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0220',
	StateGrantObligations.StateName = 'NEW YORK'
WHERE (StateGrantObligations.RpioCode = '02'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '02%2'
		OR StateGrantObligations.OrgCode LIKE '022%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0230',
	StateGrantObligations.StateName = 'PUERTO RICO'
WHERE (StateGrantObligations.RpioCode = '02'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '02%3'
		OR StateGrantObligations.OrgCode LIKE '023%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0240',
	StateGrantObligations.StateName = 'VIRGIN ISLANDS'
WHERE (StateGrantObligations.RpioCode = '02'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '02%4'
		OR StateGrantObligations.OrgCode LIKE '024%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '02*A',
	StateGrantObligations.StateName = 'TRIBAL RESOURCES – REGION 2'
WHERE (StateGrantObligations.RpioCode = '02'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgName LIKE '%TRIB%'
		OR StateGrantObligations.OrgName LIKE '%NATIO%'
		OR StateGrantObligations.OrgName LIKE '%BAND%'
		OR StateGrantObligations.OrgName LIKE '%CREEK%'
		OR StateGrantObligations.OrgName LIKE '%SOUI%'
		OR StateGrantObligations.OrgName LIKE '%INDIA%')
	AND IsNull( StateGrantObligations.StateCode ));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '02*X',
	StateGrantObligations.StateName = 'UNDISTRIBUTED NATIONAL RESOURCES – REGION 2'
WHERE StateGrantObligations.RpioCode = '02'
  AND IsNull( StateGrantObligations.StateCode );


--****************************
--      REGION 3
--***************************

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '03*A',
	StateGrantObligations.StateName = 'TRIBAL RESOURCES – REGION 3'
WHERE StateGrantObligations.RpioCode = '03'
  AND IsNull( StateGrantObligations.StateCode )
  AND StateGrantObligations.ProgramProjectCode IN ( '15', '17' );

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '03*A',
	StateGrantObligations.StateName = 'TRIBAL RESOURCES – REGION 3'
WHERE StateGrantObligations.RpioCode = '03'
  AND IsNull( StateGrantObligations.StateCode )
  AND (StateGrantObligations.OrgCode LIKE '03%T'
	OR StateGrantObligations.OrgCode LIKE '03T%');

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0310',
	StateGrantObligations.StateName = 'DELAWARE'
WHERE (StateGrantObligations.RpioCode = '03'
	AND (StateGrantObligations.OrgCode LIKE '03%1'
		OR StateGrantObligations.OrgCode LIKE '031%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0320',
	StateGrantObligations.StateName = 'DIST. OF COLUMBIA'
WHERE (StateGrantObligations.RpioCode = '03'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '03%2'
		OR StateGrantObligations.OrgCode LIKE '032%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0330',
	StateGrantObligations.StateName = 'MARYLAND'
WHERE (StateGrantObligations.RpioCode = '03'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '03%3'
		OR StateGrantObligations.OrgCode LIKE '033%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0340',
	StateGrantObligations.StateName = 'PENNSYLVANIA'
WHERE (StateGrantObligations.RpioCode = '03'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '03%4'
		OR StateGrantObligations.OrgCode LIKE '034%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0350',
	StateGrantObligations.StateName = 'VIRGINIA'
WHERE (StateGrantObligations.RpioCode = '03'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '03%5'
		OR StateGrantObligations.OrgCode LIKE '035%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '0360',
	StateGrantObligations.StateName = 'WEST VIRGINIA'
WHERE (StateGrantObligations.RpioCode = '03'
	AND IsNull( StateGrantObligations.StateCode )
	AND (StateGrantObligations.OrgCode LIKE '03%6'
		OR StateGrantObligations.OrgCode LIKE '036%'));

UPDATE StateGrantObligations
SET StateGrantObligations.StateCode = '03*X',
	StateGrantObligations.StateName = 'UNDISTRIBUTED NATIONAL RESOURCES – REGION 3'
WHERE StateGrantObligations.RpioCode = '03'
  AND IsNull( StateGrantObligations.StateCode );