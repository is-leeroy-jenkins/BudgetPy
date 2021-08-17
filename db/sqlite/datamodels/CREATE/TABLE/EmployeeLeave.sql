CREATE TABLE IF NOT EXISTS EmployeeLeave
(
   EmployeeLeaveId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyEmployeeLeave PRIMARY KEY,
   LastName TEXT(255),
   FirstName TEXT(255),
   EmployeeId TEXT(255),
   HoursEarnedYearToDate FLOAT,
   CarryoverHours FLOAT,
   HoursAdjustedYearToDate FLOAT,
   HoursBalance FLOAT,
   ProjectedAnnualHours FLOAT,
   ProjectedNextPeriodHours FLOAT,
   HoursTakenYearToDate FLOAT
);
