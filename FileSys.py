import io
from datetime import datetime, date
import os
import zipfile as zp
import openpyxl as xl
from openpyxl import Workbook
from openpyxl.chart import ( AreaChart, AreaChart3D, BarChart, BarChart3D,
                             Reference, Series, PieChart,  PieChart3D,
                             ProjectedPieChart, LineChart, LineChart3D )
from openpyxl.chart.series import DataPoint
from openpyxl.styles import ( NamedStyle, PatternFill, Border, Side,
                              Protection, Font, Fill, Color,
                              GradientFill, Alignment )
from openpyxl.formatting import Rule
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.comments import Comment
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import units
from Static import Source, Provider, SQL, Model
import enum
from Booger import Error, ErrorDialog
import sys
from sys import exc_info

# BudgetPath( selectedpath )
class BudgetPath( ):
    ''' BudgetPath( filename ) initializes the
    BudgetPath class providing selectedpath information of getsubfolders
    used in the application'''
    __path = None
    __ext = None
    __currdir = None
    __report = None
    __drive = None

    @property
    def name( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__name, str ):
            return self.__name

    @name.setter
    def name( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ):
            self.__path = str( list( os.path.split( self.__infile ) )[ 1 ] )

    @property
    def path( self ):
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    @path.setter
    def path( self, value ):
        if isinstance( value, str ) and value != '':
            self.__path = value

    @property
    def drive( self ):
        if isinstance( self.__drive, str ) and self.__drive != '':
            return self.__drive

    @drive.setter
    def drive( self, value ):
        if isinstance( value, str ):
            self.__drive = os.path.splitdrive( value )[ 0 ]

    @property
    def extension( self ):
        if  isinstance( self.__ext, str ):
            return str( self.__ext )

    @extension.setter
    def extension( self, value ):
        if  isinstance( value, str ):
            self.__ext = str( value )

    @property
    def currentdirectory( self ):
        if os.path.exists( self.__currdir ):
            return self.__currdir

    @currentdirectory.setter
    def currentdirectory( self, value ):
        '''Set the currentdirectory directory to 'selectedpath' '''
        if os.path.exists( value ):
            os.chdir( value )
            self.__currdir = value

    def __init__( self, filepath ):
        self.__path = filepath if isinstance( filepath, str ) else None
        self.__name = os.path.split( self.__path )[ 1 ] if isinstance( filepath, str ) else None
        self.__currdir = os.getcwd( )
        self.__ext = os.path.splitext( self.__path )[ 1 ] if isinstance( filepath, str ) else None
        self.__drive = os.path.splitdrive( self.__infile )[ 0 ] if isinstance( filepath, str ) else None
        self.__report = r'etc\templates\report\Excel.xlsx'

    def __str__( self ):
       if self.__path is not None:
           return str( self.__path )

    def exists( self ):
        '''Method returning a boolean value indicating whether or not the
        internal 'self.__path' exists'''
        try:
            if os.path.exists( self.__path ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetPath'
            exc.method = 'exists( self )'
            err = ErrorDialog( exc )
            err.show( )

    def isfolder( self ):
        '''Method returning boolean value indicating whether
        or not self.__path is a folder'''
        try:
            if os.path.isdir( self.__path ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetPath'
            exc.method = 'isfolder( self )'
            err = ErrorDialog( exc )
            err.show( )

    def isfile( self ):
        '''Method returning boolean value indicating whether
        or not self.__path is a file'''
        try:
            if os.path.isfile( self.__path ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetPath'
            exc.method = 'isfile( self )'
            err = ErrorDialog( exc )
            err.show( )

    def verify( self, other ):
        '''Method returns a boolean value indicating if
        the external path 'other' exists'''
        try:
            if os.path.exists( other ):
                return True
            else:
                return False
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetPath'
            exc.method = 'verify( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getextension( self, other ):
        '''Returns string representing the file extension of 'other' '''
        try:
            if isinstance( other, str ) and os.path.exists( other ):
                return  os.path.splitext( other )[ 1 ]
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetPath'
            exc.method = 'getextension( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getreportpath( self, ext = EXT.XLSX ):
        '''Method returns string representing the relative path
        to the report template
        '''
        try:
            if isinstance( self.__report, str ):
                return self.__report
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetPath'
            exc.method = 'getreportpath( self )'
            err = ErrorDialog( exc )
            err.show( )

    def join( self, first, second ):
        ''' Method concatenates the path provided by the argument 'first'
        to the path provided by argument 'second' '''
        try:
            if os.path.exists( first ) and os.path.exists( second ):
                return os.path.join( first, second )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetPath'
            exc.method = 'join( self, first, second )'
            err = ErrorDialog( exc )
            err.show( )


class SqlPath( ):
    '''class providing relative paths to the sql subfolders'''
    __accessdriver = None
    __accessdata = None
    __accessreference = None
    __sqlitedriver = None
    __sqlitedata = None
    __sqlitereference = None
    __sqldriver = None
    __sqldata = None
    __sqlreference = None

    @property
    def sqlitedriver( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__sqlitedriver, str ):
            return self.__sqlitedriver

    @sqlitedriver.setter
    def sqlitedriver( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqlitedriver = value

    @property
    def sqlitedata( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__sqlitedata, str ):
            return self.__sqlitedata

    @sqlitedata.setter
    def sqlitedata( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqlitedata = value

    @property
    def sqlitereference( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__sqlitereference, str ):
            return self.__sqlitereference

    @sqlitereference.setter
    def sqlitereference( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqlitereference = value

    @property
    def accessdriver( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__accessdriver, str ):
            return self.__accessdriver

    @accessdriver.setter
    def accessdriver( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__accessdriver = value

    @property
    def accessdata( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__accessdata, str ):
            return self.__accessdata

    @accessdata.setter
    def accessdata( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__accessdata = value

    @property
    def accessreference( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__accessreference, str ):
            return self.__accessreference

    @accessreference.setter
    def accessreference( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__accessreference = value

    @property
    def sqlitedriver( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__sqlitedriver, str ):
            return self.__sqlitedriver

    @sqlitedriver.setter
    def sqlitedriver( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqlitedriver = value

    @property
    def sqldata( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__sqldata, str ):
            return self.__sqldata

    @sqldata.setter
    def sqldata( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqldata = value

    @property
    def sqlreference( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( self.__sqlreference, str ):
            return self.__sqlreference

    @sqlreference.setter
    def sqlreference( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ) and value != '':
            self.__sqlreference = value

    def __init__( self ):
        self.__sqlitedriver = 'sqlite3'
        self.__sqlitedata =  r'db\sqlite\datamodels\sql'
        self.__sqlitereference = r'db\sqlite\referencemodels\sql'
        self.__accessdriver = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='
        self.__accessdata = r'db\access\datamodels\sql'
        self.__accessreference = r'db\access\referencemodels\sql'
        self.__sqldriver = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLExpress;'
        self.__sqldata = r'db\mssql\datamodels\sql'
        self.__sqlreference = r'db\mssql\referencemodels\sql'


# SqlFile( source, provider, command )
class SqlFile( ):
    '''Class providing access to sql getsubfolders in the application'''
    __data = None
    __reference = None
    __command = None
    __source = None
    __provider = None

    @property
    def provider( self ):
        if isinstance( self.__provider, Provider ):
            return self.__provider

    @provider.setter
    def provider( self, value ):
        if isinstance( value, Provider ):
            self.__provider = value

    @property
    def source( self ):
        if isinstance( self.__source, Source ):
            return self.__source

    @source.setter
    def source( self, value ):
        if isinstance( value, Source ):
            self.__source = value

    @property
    def command( self ):
        if isinstance( self.__command, SQL ):
            return self.__command

    @command.setter
    def command( self, value ):
        if isinstance( value, SQL ):
            self.__command = value

    def __init__( self, source = None, provider = None,
                  command = None ):
        self.__data = [ 'Allocations', 'Actuals', 'ApplicationTables', 'Apportionments', 'AppropriationDocuments',
                       'BudgetaryResourceExecution', 'BudgetControls', 'BudgetDocuments', 'BudgetOutlays',
                       'CarryoverEstimates', 'CarryoverSurvey', 'Changes', 'CongressionalReprogrammings',
                       'Deobligations', 'Defactos', 'DocumentControlNumbers',
                       'Obligations', 'OperatingPlans', 'OperatingPlanUpdates',
                       'ObjectClassOutlays', 'CarryoverOutlays',
                       'QueryDefinitions', 'RegionalAuthority', 'SpendingRates',
                       'GrowthRates', 'ReimbursableAgreements', 'ReimbursableFunds',
                       'ReimbursableSurvey', 'Reports', 'StatusOfAppropriations' 
                       'Reprogrammings', 'SiteActivity', 'SiteProjectCodes', 'SpecialAccounts',
                       'StatusOfFunds', 'Supplementals', 'Transfers', 'HumanResourceOrganizations'
                       'HeadquartersAuthority', 'TravelObligations', 'StatusOfAppropriations',
                       'StatusOfJobsActFunding', 'StatusOfSupplementalFunding', 'SuperfundSites',
                       'PayrollAuthority', 'TransTypes', 'ProgramFinancingSchedule',
                       'PayrollRequests', 'CarryoverRequests', 'CompassLevels',
                       'AdministrativeRequests', 'OpenCommitments', 'Expenditures',
                       'UnliquidatedObligations', 'UnobligatedAuthority' ]
        self.__references = [ 'Accounts', 'ActivityCodes', 'AllowanceHolders',
                             'Appropriations', 'BudgetObjectClasses',
                             'CostAreas', 'CPIC', 'Divisions',
                             'Documents', 'FederalHolidays', 'FinanceObjectClasses',
                             'FiscalYears', 'FiscalYearsBackUp', 'Funds',
                             'FundSymbols', 'Goals', 'GsPayScales', 'Images',
                             'Messages', 'NationalPrograms', 'Objectives',
                             'Organizations', 'ProgramAreas', 'ProgramDescriptions',
                             'ProgramProjects', 'Projects', 'Providers', 'RegionalOffices'
                             'ReferenceTables', 'ResourcePlanningOffices', 'ResponsibilityCenters',
                             'SchemaTypes', 'StateOrganizations', 'Sources' ]
        self.__command = command if isinstance( command, SQL ) else SQL.SELECTALL
        self.__source = source if isinstance( source, Source ) else Source.StatusOfFunds
        self.__provider = provider if isinstance( provider, Provider ) else Provider.SQLite

    def getpath( self ):
        '''Method returning a string representing
         the absolute path to the SQL file used to execute the
         command 'self.__command' against the table given by the
         member self.__source depending on the member self.__provider'''
        try:
            sqlpath = SqlPath( )
            data = self.__data
            references = self.__references
            provider = self.__provider.name
            source = self.__source.name
            command = self.__command.name
            current = os.getcwd( )
            path = ''
            if provider == 'SQLite' and source in data:
                path = f'{ sqlpath.sqlitedata }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'SQLite' and source in references:
                path = f'{ sqlpath.sqlitereference }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'Access' and source in data:
                path = f'{ sqlpath.accessdata }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'Access' and source in references:
                path = f'{ sqlpath.accessreference }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'SqlServer' and source in data:
                path = f'{ sqlpath.sqldata }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            elif provider == 'SqlServer' and source in references:
                path = f'{ sqlpath.sqlreference }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
            else:
                path = f'{ sqlpath.sqlitedata }\\{ command }\\{ source }.sql'
                return os.path.join( current, path )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'SqlFile'
            exc.method = 'getpath( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getdirectory( self ):
        '''Method creates and returns a string representing
        the parent directory where the SQL file resides'''
        try:
            sqlpath = SqlPath( )
            data = self.__data
            reference = self.__references
            source = self.__source.name
            provider = self.__provider.name
            command = self.__command.name
            current = os.getcwd( )
            folder = ''
            if provider == 'SQLite' and source in data:
                folder = f'{ sqlpath.sqlitedata }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'SQLite' and source in references:
                folder = f'{ sqlpath.sqlitereference }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'Access' and source in data:
                folder = f'{ sqlpath.accessdata }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'Access' and source in references:
                folder = f'{ sqlpath.accessreference }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'SqlServer' and source in data:
                folder = f'{ sqlpath.sqldata }\\{ command }'
                return os.path.join( current, folder )
            elif provider == 'SqlServer' and source in references:
                folder = f'{ sqlpath.sqlreference }\\{ command }'
                return os.path.join( current, folder )
            else:
                folder = f'{ sqlpath.sqlitedata }\\{ command }'
                return os.path.join( current, folder )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'SqlFile'
            exc.method = 'getdirectory( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getquery( self ):
        '''Method reads the given '.sql' file and returns
        a string representing the text used the sql query'''
        try:
            source = self.__source.name
            paths = self.getpath( )
            folder = self.getdirectory( )
            sql = ''
            for name in os.listdir( folder ):
                if name.endswith( '.sql' ) and os.path.splitext( name )[ 0 ] == source:
                    path = os.path.join( folder, name )
                    query = open( path )
                    sql = query.read( )
                    return sql
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'SqlFile'
            exc.method = 'getquery( self, other )'
            err = ErrorDialog( exc )
            err.show( )


# BudgetFile( selectedpath )
class BudgetFile( ):
    '''BudgetFile( selectedpath ) initializes the
     BudgetFile Class providing file information for
     getsubfolders used in the application'''
    __absolute = None
    __name = None
    __path = None
    __size = None
    __extension = None
    __directory = None
    __drive = None
    __created = None
    __modified = None
    __accessed = None
    __currdir = None
    __contents = [ ]

    @property
    def name( self ):
        '''Get the sheetname property'''
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, value ):
        '''Set the sheetname property'''
        if os.path.exists( value ):
            self.__name = os.path.basename( value )

    @property
    def path( self ):
        if os.path.isfile( self.__path ):
            return str( self.__path )

    @path.setter
    def path( self, value ):
        if os.path.exists( value ):
            self.__path = str( value )

    @property
    def absolute( self ):
        if isinstance( self.__absolute, str ):
            return self.__absolute

    @absolute.setter
    def absolute( self, value ):
        if os.path.exists( value ) and os.path.isabs( value ):
            self.__absolute = value

    @property
    def size( self ):
        if isinstance( self.__size, int ):
            return self.__size

    @size.setter
    def size( self, value ):
        if isinstance( value, int ):
            self.__size = value

    @property
    def directory( self ):
        if self.__directory is not None:
            return self.__directory

    @directory.setter
    def directory( self, value ):
        if os.path.isdir( value ):
            self.__directory = str( os.path.dirname( value ) )

    @property
    def extension( self ):
        if self.__extension is not None:
            return self.__extension
        else:
            return 'NS'

    @extension.setter
    def extension( self, value ):
        if value is not None:
            self.__extension = value

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @drive.setter
    def drive( self, value ):
        if os.path.ismount( value ):
            self.__drive = str( value )

    @property
    def modified( self ):
        if isinstance( self.__modified, datetime ):
            return self.__modified

    @modified.setter
    def modified( self, value ):
        if isinstance( value, float ):
            self.__modified = value

    @property
    def accessed( self ):
        if self.__accessed is not None:
            return self.__accessed

    @accessed.setter
    def accessed( self, value ):
        if isinstance( value, float ):
            self.__accessed = value

    @property
    def created( self ):
        if self.__created is not None:
            return self.__created

    @created.setter
    def created( self, value ):
        if isinstance( value, float ):
            self.__created = value

    @property
    def current( self ):
        if os.path.exists( self.__currdir ):
            return str( self.__currdir )

    @current.setter
    def current( self, value ):
        '''Set the currentdirectory directory to 'selectedpath' '''
        if os.path.exists( value ) and os.path.isdir( value ):
            os.chdir( value )
            self.__currdir = value

    def __init__( self, filepath = None ):
        self.__absolute = filepath if os.path.isabs( filepath ) else os.getcwd( ) +'\\' + filepath
        self.__path = filepath if not os.path.isabs( filepath ) else os.path.relpath( filepath )
        self.__name = os.path.basename( filepath )
        self.__size = os.path.getsize( filepath )
        self.__directory = os.path.dirname( filepath )
        self.__extension = list( os.path.splitext( filepath ) )[ 1 ]
        self.__created = os.path.getctime( filepath )
        self.__accessed = os.path.getatime( filepath )
        self.__modified = os.path.getmtime( filepath )
        self.__currdir = os.getcwd( )
        self.__drive = os.path.splitdrive( filepath )[ 0 ] if os.path.ismount( filepath ) \
            else os.path.splitdrive( os.path.join( self.__currdir, filepath ) )[ 0 ]

    def __str__( self ):
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    def exists( self ):
        if isinstance( self.__path, str ) and os.path.exists( self.__path ):
            return True
        else:
            return False

    def rename( self, other ):
        '''Renames the currentdirectory file to 'other' '''
        try:
            if isinstance( other, str ) and not other == '':
                src = os.path.abspath( self.__path )
                dst = os.path.join( self.directory, other )
                os.rename( src, dst )
                return dst
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'rename( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def move( self, destination ):
        '''renames currentdirectory file'''
        try:
            if os.path.isdir( destination ):
                return os.path.join( self.__name, destination )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'move( self, destination )'
            err = ErrorDialog( exc )
            err.show( )

    def create( self, other, lines = None ):
        ''' creates and returns 'selectedpath' file '''
        try:
            if isinstance( other, str ):
                newfile = open( other, 'r+' )
                if isinstance( lines, list ) and len( lines ) > 0:
                    for line in lines:
                        newfile.write( line )

                    newfile.flush( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'create( self, other, lines = None )'
            err = ErrorDialog( exc )
            err.show( )

    def verify( self, other ):
        '''determines if an external file exists'''
        try:
            if other is not None:
                return os.path.exists( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'verify( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def delete( self, other ):
        ''' deletes file at 'self.__selecteditem'   '''
        try:
            if os.path.isfile( other ):
                os.remove( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'delete( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getsize( self, other ):
        '''gets the size of another file'''
        try:
            if self.__path is not None and os.path.isfile( other ):
                return os.path.getsize( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'getsize( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getdrive( self, other ):
        '''gets the drive of another file'''
        try:
            if os.path.exists( other ):
                return str( list( os.path.splitdrive( other ) )[ 0 ] )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'getdrive( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getextension( self, other ):
        ''' gets and returns extension of 'selectedpath' 'file' '''
        try:
            if other is not None and os.path.isfile( other ):
                return str( list( os.path.splitext( other ) )[ 1 ] )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'getextension( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def readlines( self, other ):
        '''reads all lines in 'other' into a list
            then returns the list '''
        try:
            if os.path.isfile( other ):
                file = open( other, 'r' )
                contents = file.readlines( )
                file.close( )
                return contents
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'realines( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def readall( self, other ):
        '''reads a single line from the file into a string
            then returns the string'''
        try:
            contents = ''
            if os.path.isfile( other ):
                file = open( other, 'r' )
                contents = file.read( )
                file.close( )
                return contents
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'readall( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def writelines( self, lines = None ):
        ''' writes the contents of 'lines' to self.__contents '''
        try:
            if isinstance( lines, list ):
                path = os.path.relpath( self.__path )
                contents = open( path, 'a' )
                for line in lines:
                    contents.write( line )
                contents.flush( )
                return contents
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'writelines( self, lines = None )'
            err = ErrorDialog( exc )
            err.show( )

    def writeall( self, other ):
        ''' writes the contents of 'lines' to self.__contents '''
        try:
            contents = [ ]
            lines = [ ]
            if os.path.isfile( other ):
                path = os.path.relpath( self.__path )
                contents = open( path, 'a' )
                lines = open( other, 'r' )
                for line in lines.readlines( ):
                    contents.write( line )
                contents.flush( )
                lines.close( )
                return contents
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFile'
            exc.method = 'writeall( self, other )'
            err = ErrorDialog( exc )
            err.show( )


# BudgetFolder( selectedpath )
class BudgetFolder( ):
    '''BudgetFolder( selectedpath ) initializes the
     BudgetFolder Class providing file directory information'''
    __absolute = None
    __path = None
    __name = None
    __parent = None
    __dir = None
    __drive = None
    __current = None

    @property
    def name( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if os.path.exists( self.__path ):
            return str( list( os.path.split( self.__path ) )[ 1 ] )

    @name.setter
    def name( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if isinstance( value, str ):
            self.__path = value

    @property
    def directory( self ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if not self.__name == '':
            return self.__name

    @directory.setter
    def directory( self, value ):
        '''Returns string representing the sheetname of the selectedpath 'base' '''
        if os.path.isdir( value ):
            self.__name = value

    @property
    def path( self ):
        if isinstance( self.__path, str ):
            return self.__path

    @path.setter
    def path( self, value ):
        if os.path.exists( value ):
            self.__path = str( value )

    @property
    def absolute( self ):
        if isinstance( self.__absolute, str ) and self.__absolute != '':
            return self.__absolute

    @absolute.setter
    def absolute( self, value ):
        if os.path.exists( value ) and os.path.isabs( value ):
            self.__absolute = value

    @property
    def parent( self ):
        if self.__parent is not None:
            return self.__parent

    @parent.setter
    def parent( self, value ):
        if os.path.isdir( value ):
            self.__parent = str( value )

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @drive.setter
    def drive( self, value ):
        if os.path.ismount( value ):
            self.__drive = str( value )

    @property
    def current( self ):
        if self.__current is not None:
            return self.__current

    @current.setter
    def current( self, value ):
        if os.path.exists( value ):
            os.chdir( value )

    def __init__( self, folderpath ):
        self.__current = os.getcwd( )
        self.__path = folderpath if not os.path.ismount( folderpath ) else os.path.relpath( folderpath )
        self.__name = os.path.dirname( folderpath )
        self.__parent = os.path.basename( folderpath )
        self.__absolute = os.getcwd( ) + '\\' + self.__path

    def __str__( self ):
        if self.__path is not None:
            return self.__path

    def getsubfiles( self ):
        '''Iterates subfolders in the base directory
        and returns a list of subfile paths'''
        try:
            filenames = os.listdir( self.__absolute )
            files = [ ]
            for file in filenames:
                    path = os.path.join( self.__absolute, file )
                    files.append( path )

            return filenames
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'getsubfiles( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getsubfolders( self ):
        '''Iterates getsubfolders in the base directory'''
        try:
            current = self.__current
            abspath = self.__abspath
            filenames = [ ]
            for i in os.walk( abspath ):
                if len( i[ 1 ] ) > 0:
                    for file in i[ 1 ]:
                        path = os.path.join( abspath, file )
                        if not os.path.isdir( path ):
                            filenames.append( path )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'getsubfolders( self )'
            err = ErrorDialog( exc )
            err.show( )

        return filenames

    def rename( self, new_name ):
        '''renames currentdirectory file'''
        try:
            if self.__name is not None and isinstance( new_name, str ):
                return os.rename( self.__name, new_name )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'rename( self, new_name )'
            err = ErrorDialog( exc )
            err.show( )

    def move( self, destination ):
        '''renames currentdirectory file'''
        try:
            if not destination == '' and not os.path.exists( destination ):
                return os.path.join( self.__name, destination )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'move( self, destination )'
            err = ErrorDialog( exc )
            err.show( )

    def exists( self, other ):
        '''determines if the base file exists'''
        try:
            if not other == '' and os.path.isdir( other ):
                return True
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'exists( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def create( self, other ):
        try:
            if other is not None:
                os.mkdir( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'create( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def delete( self, other ):
        ''' deletes 'selectedpath' directory '''
        try:
            if other is not None and os.path.isdir( other ):
                os.rmdir( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'delete( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def getsize( self, other ):
        ''' gets and returns size of 'selectedpath' '''
        try:
            if other is not None and os.path.isdir( other ):
                return os.path.getsize( other )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = ''
            err = ErrorDialog( exc )
            err.show( )

    def getdrive( self, other ):
        ''' gets and returns parent directory of 'selectedpath' '''
        try:
            if other is not None and os.path.isdir( other ):
                return os.path.splitdrive( other )[ 0 ]
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'getdrive( self, other )'
            err = ErrorDialog( exc )
            err.show( )

    def iterate( self ):
        '''iterates getsubfolders in the base directory'''
        try:
            if os.path.isdir( self.__path ):
                for i in os.scandir( self.__path ):
                    yield i
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'iterate( self )'
            err = ErrorDialog( exc )
            err.show( )

    def getfiles( self, other ):
        '''iterates getsubfolders in the directory provided by 'other' '''
        try:
            if os.path.isdir( other ):
                names = os.listdir( other )
                files = [ ]
                for i in names:
                    file = os.path.join( other, i )
                    if os.path.isfile( file ):
                        files.append( file )

                return files
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'BudgetFolder'
            exc.method = 'getfiles( self, other )'
            err = ErrorDialog( exc )
            err.show( )


# EmailMessage( sender, receiver, body, subject, copy )
class EmailMessage( ):
    '''EmailMessage( frm, to, body, subject ) initializes
    class providing email behavior '''
    __sender = None
    __receiver = None
    __subject = None
    __message = None
    __others = None

    @property
    def sender( self ):
        ''' Gets the sender's email address '''
        if self.__sender is not None:
            return self.__sender

    @sender.setter
    def sender( self, value ):
        ''' Set the sender's email address '''
        if value is not None:
            self.__sender = str( value )

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if self.__receiver is not None:
            return [ self.__receiver, ]

    @receiver.setter
    def receiver( self, value ):
        ''' Sets the receiver's email address '''
        if value is not None:
            self.__receiver = str( value )

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if self.__subject is not None:
            return self.__subject

    @subject.setter
    def subject( self, value ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__receiver = str( value )

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if self.__message is not None:
            return self.__message

    @body.setter
    def body( self, value ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__receiver = str( value )

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if self.__others is not None:
            return self.__others

    @copy.setter
    def copy( self, value ):
        ''' Sets the address's to send copies  '''
        if value is not None:
            self.__others = list( value )

    def __init__( self, sender, receiver, body, subject, copy = None ):
        self.__sender = sender if isinstance( sender, str ) and sender != '' else None
        self.__receiver = receiver if isinstance( receiver, str ) and receiver != '' else None
        self.__message = body if isinstance( body, str ) and bocy != '' else None
        self.__others = copy if isinstance( copy, list ) and len( copy ) > 0 else None
        self.__subject = subject if isinstance( subject, str ) and subject != '' else None

    def __str__( self ):
        if isinstance( self.__body, str ) and self.__body != '':
            return self.__body


# EmailBuilder( sender, receiver, body, subject, copy )
class EmailBuilder( ):
    ''' Helper class for generating email messages '''
    __from = None
    __to = None
    __subject = None
    __message = None
    __others = None

    @property
    def sender( self ):
        ''' Gets the sender's email address '''
        if self.__from is not None:
            return self.__from

    @sender.setter
    def sender( self, value ):
        ''' Set the sender's email address '''
        if value is not None:
            self.__from = str( value )

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if self.__to is not None:
            return self.__to

    @receiver.setter
    def receiver( self, value ):
        ''' Sets the receiver's email address '''
        if value is not None:
            self.__to = str( value )

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if self.__subject is not None:
            return self.__subject

    @subject.setter
    def subject( self, value ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__to = str( value )

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if self.__message is not None:
            return self.__message

    @body.setter
    def body( self, value ):
        ''' Sets the email's subject line '''
        if value is not None:
            self.__to = str( value )

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if self.__others is not None:
            return self.__others

    @copy.setter
    def copy( self, value ):
        ''' Sets the address's to send copies  '''
        if value is not None:
            self.__others = list( value )

    def __init__( self, sender, receiver, body, subject, copy = None ):
        self.__from = sender if isinstance( sender, str ) and sender != '' else None
        self.__to = receiver if isinstance( receiver, str ) and receiver != '' else None
        self.__message = body if isinstance( body, str ) and body != '' else None
        self.__others = copy if isinstance( copy, str ) and copy != '' else None
        self.__subject = subject if isinstance( subject, str ) and subject != '' else None

    def __str__( self ):
        if self.__message is not None:
            return self.__message


# ExcelFile( selectedpath )
class ExcelFile(  ):
    '''ExcelFile( selectedpath ) class provides
    the spreadsheet for Budget Py reports '''
    __path = None
    __workbook = None
    __worksheet = None
    __name = None
    __title = None

    @property
    def path( self ):
        ''' Get the sheetname of the workbook '''
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    @path.setter
    def path( self, value ):
        if isinstance( value, str ) and os.path.exists( value ):
            self.__path = value

    @property
    def name( self ):
        ''' Get the sheetname of the workbook '''
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None and len( value ) > 0:
            self.__name = str( value )

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if isinstance( self.__workbook, Workbook ):
            return self.__workbook

    @workbook.setter
    def workbook( self, value ):
        ''' Gets the report template '''
        if isinstance( value, Workbook ):
            self.__workbook = value

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if isinstance( self.__workbook, xl.Workbook ):
            return self.__workbook.active

    @worksheet.setter
    def worksheet( self, value ):
        ''' Gets the workbooks worksheet '''
        if isinstance( value, xl.Workbook ):
            self.__name = value.active

    def __init__( self, folderpath, sheetname = None ):
        self.__path = folderpath if isinstance( folderpath, str ) else os.getcwd( )
        self.__name = os.path.split( folderpath )[ 1 ] if isinstance( folderpath, str ) else None
        self.__title = sheetname if isinstance( sheetname, str ) else os.path.splitext( self.__name )[ 0 ]
        self.__workbook = xl.Workbook( )
        self.__worksheet = self.__workbook.create_sheet( self.__title, 0 )

    def __str__( self ):
        if self.__path is not None:
            return self.__path

    def save( self ):
        try:
            if isinstance( self.__workbook, Workbook ):
                name = self.__name
                self.__workbook.save( name )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'ExcelFile'
            exc.method = 'save( self )'
            err = ErrorDialog( exc )
            err.show( )

# ExcelReport( sheetname, rows = 46, cols = 12 )
class ExcelReport( ):
    '''ExcelReport( sheetname ) class provides
    the spreadsheet for Budget Py reports '''
    __path = None
    __workbook = None
    __worksheet = None
    __name = None
    __rows = None
    __columns = None
    __dimensions = None

    @property
    def name( self ):
        ''' Get the sheetname of the workbook '''
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None and len( value ) > 0:
            self.__name = str( value )

    @property
    def rows( self ):
        if self.__rows is not None:
            return self.__rows

    @rows.setter
    def rows( self, value ):
        if isinstance( value, int ) and value > 0:
            self.__rows = value

    @property
    def columns( self ):
        if self.__columns is not None:
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, int ) and value > 0:
            self.__columns = value

    @property
    def dimensions( self ):
        if self.__dimensions is not None:
            return self.__dimensions

    @dimensions.setter
    def dimensions( self, value ):
        if isinstance( value, tuple ) and len( value ) <= 2:
            self.__dimensions = value

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if self.__path is not None:
            self.__workbook = xl.open( self.__path )
            return self.__workbook

    @workbook.setter
    def workbook( self, value ):
        ''' Gets the report template '''
        if value is not None and os.path.exists( value ):
            self.__workbook = xl.open( value )

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if self.__worksheet is not None:
            return self.__worksheet

    @worksheet.setter
    def worksheet( self, value ):
        ''' Gets the workbooks worksheet '''
        if self.__workbook is not None and value is not None:
            self.__workbook.worksheets.clear( )
            self.__worksheet = self.__workbook.create_sheet( title = value, index = 1 )

    def __init__( self, name, rows = 46, cols = 12 ):
        self.__path = r'etc/templates/report/Excel.xlsx'
        self.__name = name if isinstance( name, str ) and name != '' else None
        self.__rows = rows if isinstance( rows, int ) and rows > -1 else None
        self.__columns = cols if isinstance( cols, int ) and cols > -1 else None
        self.__dimensions = (self.__rows, self.__columns)


# ZipFile( selectedpath )
class ZipFile( ):
    __infile = None
    __name = None
    __filepath = None
    __extension = None
    __zippath = None
    __zipextension = None

    @property
    def path( self ):
        if not self.__filepath == '':
            return self.__filepath

    @path.setter
    def path( self, value ):
        if os.path.exists( value ) and os.path.isfile( value ):
            self.__filepath = value

    @property
    def name( self ):
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, value ):
        if not value == '':
            self.__name = value

    def __init__( self, filepath ):
        self.__infile = filepath if isinstance( filepath, str ) and filepath != '' else None
        self.__zipextension = '.zip'
        self.__filepath = filepath if os.path.isfile( filepath ) else None
        self.__extension = os.path.splitext( filepath )
        self.__zippath = self.__filepath.replace( self.__extension, self.__zipextension )
        self.__name = os.path.basename( filepath )

    def create( self ):
        ''' Creates zip file'''
        try:
            if not self.__filepath == '':
                zp.ZipFile( self.__zippath, 'w' ).write( self.__filepath, self.__name )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'ZipFile'
            exc.method = 'create( self )'
            err = ErrorDialog( exc )
            err.show( )


    def unzip( self ):
        ''' Extracts zip file contents '''
        try:
            if os.path.exists( self.__zippath ):
                file = zp.ZipFile( self.__zippath )
                file.extractall( self.__zippath )
        except Exception as e:
            exc = Error( e )
            exc.module = 'FileSys'
            exc.cause = 'ZipFile'
            exc.method = 'unzip( self )'
            err = ErrorDialog( exc )
            err.show( )
