CREATE TABLE Images
(
	ImagesId      INT           NOT NULL UNIQUE,
	FileName      NVARCHAR(150) NULL DEFAULT ('NS'),
	FilePath      NVARCHAR(150) NULL DEFAULT ('NS'),
	FileExtension NVARCHAR(150) NULL DEFAULT ('NS'),
	ImageFile     image         NULL,
	Attachments   NVARCHAR(MAX) NULL,
	CONSTRAINT ImagesPrimaryKey PRIMARY KEY
		(
		  ImagesId ASC
			)
);
