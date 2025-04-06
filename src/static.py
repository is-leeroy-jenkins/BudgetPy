'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                static.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="static.py" company="Terry D. Eppler">

     This is a Federal Budget, Finance, and Accounting application.
     Copyright ©  2024  Terry Eppler

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the “Software”),
     to deal in the Software without restriction,
     including without limitation the rights to use,
     copy, modify, merge, publish, distribute, sublicense,
     and/or sell copies of the Software,
     and to permit persons to whom the Software is furnished to do so,
     subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
     ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
     DEALINGS IN THE SOFTWARE.

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    static.py
  </summary>
  ******************************************************************************************
  '''
from enum import Enum, auto

class EXT( Enum ):
    '''Enumeration of database file extensions'''
    NS = auto( )
    DB = auto( )
    ACCDB = auto( )
    XLS = auto( )
    XLSM = auto( )
    XLSX = auto( )
    MDF = auto( )
    HTML = auto( )
    HTM = auto( )
    XHTML = auto( )
    XML = auto( )
    PNG = auto( )
    JPEG = auto( )
    SVG = auto( )


class Provider( Enum ):
    '''
    Constructor:  Provider.Member

    Purpose:  Enumeration of data providers
    '''
    SQLite = 0
    Access = 1
    SqlServer = 2
    Excel = 3
    CSV = 4


class ParamStyle( Enum ):
    '''
    Constructor:  ParamStyle( )

    Purpose:  Enumeration of parameter styles
    '''
    format = 1
    number = 2
    pyformat = 3
    name = 4
    qmark = 5


class SQL( Enum ):
    '''
    Constructor:  SQL.Member

    Purpose:   Enumeration of sqlstatement commands
    '''
    SELECT = 0
    SELECTALL = 1
    INSERT = 2
    UPDATE = 3
    DELETE = 4
    DROPTABLE = 5
    DROPVIEW = 6
    CREATETABLE = 7
    CREATEVIEW = 8
    ALTERTABLE = 9
    ALTERCOLUMN = 10


class Client( Enum ):
    '''
    Constructor:  Client.Member

    Purpose:  Enumeration of auxiliary applications
    '''
    SQLite = auto( )
    Access = auto( )
    Excel = auto( )
    Word = auto( )
    Edge = auto( )
    Chrome = auto( )
    ControlPanel = auto( )
    Calculator = auto( )
    Outlook = auto( )
    Pyscripter = auto( )
    TaskManager = auto( )
    Storage = auto( )


class ICO( Enum ):
    '''
    Constructor:  ICO.Member

    Purpose:  Enumeration of ICO files
    '''
    Access = auto( )
    Browse = auto( )
    CSV = auto( )
    Database = auto( )
    Error = auto( )
    Excel = auto( )
    Ninja = auto( )
    Notification = auto( )
    PDF = auto( )
    Text = auto( )


class ACCDB( Enum ):
    '''
    Constructor:  ACCDB.Member

    Purpose:  Enumeration of access database types used in the application
    '''
    INTEGER = auto( )
    NUMBER = auto( )
    AUTONUMBER = auto( )
    CURRENCY = auto( )
    DATETIME = auto( )
    HYPERLINK = auto( )
    SHORTTEXT = auto( )
    LONGTEXT = auto( )
    RICHTEXT = auto( )
    ATTACHMENT = auto( )
    CALCULATED = auto( )


class DB( Enum ):
    '''
    Constructor:  DB.Member

    Purpose:  Enumeration of SQLite database types used in the application
    '''
    REAL = auto( )
    TEXT = auto( )
    INTEGER = auto( )
    BLOB = auto( )


class MDF( Enum ):
    '''
    Constructor:  MDF.Member

    Purpose:  Enumeration of SQL Server database types used in the application
    '''
    BIT = auto( )
    INT = auto( )
    DECIMAL = auto( )
    MONEY = auto( )
    DATE = auto( )
    TIME = auto( )
    DATETIME = auto( )
    FLOAT = auto( )
    CHAR = auto( )
    TEXT = auto( )
    NCHAR = auto( )
    NTEXT = auto( )
    VARCHAR = auto( )
    NVARCHAR = auto( )
    BINARY = auto( )
    VARBINARY = auto( )
    IMAGE = auto( )
    DATETIMEOFFSET = auto( )


class Holiday( Enum ):
    '''
    Constructor:  Holiday.Member

    Purpose:  Enumberation representing federal holidays
    New Year’s Day, January 1.
    Martin Luther King, the third Monday in January.
    Washington’s Birthday, the third Monday in February.
    Memorial Day, the last Monday in May.
    Juneteenth National Independence Day, June 19.
    Independence Day,  July 4.
    Veterans Day, November 11.
    Labor Day, the first Monday in September.
    Columbus Day, the second Monday in October.
    Thanksgiving Day, the fourth Thursday in November.
    Christmas Day, December 25.
    '''
    NewYearsDay = auto( )
    MartinLutherKingDay = auto( )
    PresidentsDay = auto( )
    MemorialDay = auto( )
    JuneteenthDay = auto( )
    IndependenceDay = auto( )
    VeteransDay = auto( )
    LaborDay = auto( )
    ColumbusDay = auto( )
    ThanksgivingDay = auto( )
    ChristmasDay = auto( )


class Weekday( Enum ):
    '''
    Constructor:

    Purpose:

    '''
    Monday = 1
    Tuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7
    
    
class Month( Enum ):
    '''
    Constructor:

    Purpose:

    '''
    January = 1
    Feburary = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12