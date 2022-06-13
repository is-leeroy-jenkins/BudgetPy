PARAMETERS TableArgs Text ( 255 ), ColumnArgs Text ( 255 ), ActionArgs Text ( 255 ), OldValueArgs Text ( 255 ), NewValueArgs Text ( 255 ), TimeArgs DateTime, MessageArgs Text ( 255 );
INSERT INTO Changes ( TableName, FieldName, [Action], OldValue, NewValue, [TimeStamp], Message )
VALUES (TableArgs, ColumnArgs, ActionArgs, OldValueArgs, NewValueArgs, TimeArgs, MessageArgs);