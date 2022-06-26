CREATE TABLE IF NOT EXISTS "ProgramProjectDescriptions" 
(
    "ProgramProjectDescriptionsId"	INTEGER NOT NULL UNIQUE,
    "Code"	TEXT(80) DEFAULT 'NS',
    "Name"	TEXT(80) DEFAULT 'NS',
    "ProgramTitle"	TEXT(80) DEFAULT 'NS',
    "Laws"	TEXT(255) DEFAULT 'NS',
    "Description"	TEXT(255) DEFAULT 'NS',
    "ProgramAreaCode"	TEXT(80) DEFAULT 'NS',
    "ProgramAreaName"	TEXT(80) DEFAULT 'NS',
    PRIMARY KEY("ProgramProjectDescriptionsId" AUTOINCREMENT)
);