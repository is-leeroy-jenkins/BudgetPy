CREATE TABLE Changes
(
	    ChangeId INTEGER NOT NULL UNIQUE CONSTRAINT PrimaryKeyChanges PRIMARY KEY,
	    TableName TEXT(255) NULL,
	    FieldName TEXT(255) NULL,
	    ActionType TEXT(255) NULL,
	    OldValue TEXT(255) NULL,
	    NewValue TEXT(255) NULL,
	    ChangeDate DATETIME NULL,
	    Message TEXT(255) NULL
);