CREATE TABLE PurchaseRequestNumbers (
	PurchaseRequestId	INTEGER NOT NULL UNIQUE,
	RcCode	 TEXT(255),
	PurchaseRequest	 TEXT(255),
	PRIMARY KEY(PurchaseRequestId AUTOINCREMENT)
)