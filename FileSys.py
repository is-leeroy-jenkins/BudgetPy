import io
from datetime import datetime, date
import os
import zipfile as zp
import openpyxl as xl
from Static import Source, Provider, SQL, Model

# BudgetPath( filepath )
class BudgetPath( ):
    ''' BudgetPath( filename ) initializes the
    BudgetPath class providing filepath information of getsubfolders
    used in the application'''
    __inpath = None
    __path = None
    __ext = None
    __currdir = None
    __report = None
    __drive = None
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
    def name( self ):
        '''Returns string representing the name of the filepath 'base' '''
        if isinstance( self.__name, str ):
            return self.__name

    @name.setter
    def name( self, value ):
        '''Returns string representing the name of the filepath 'base' '''
        if isinstance( value, str ):
            self.__path = str( list( os.path.split( self.__inpath ) )[ 1 ] )

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
        '''Set the currentdirectory directory to 'filepath' '''
        if os.path.exists( value ):
            os.chdir( value )
            self.__currdir = value

    def __init__( self, filepath ):
        self.__inpath = filepath if isinstance( filepath, str ) else None
        self.__path = self.__inpath if isinstance( filepath, str ) else None
        self.__name = os.path.split( self.__inpath )[ 1 ] if isinstance( filepath, str ) else None
        self.__currdir = os.getcwd( )
        self.__ext = os.path.splitext( self.__inpath )[ 1 ] if isinstance( filepath, str ) else None
        self.__drive = os.path.splitdrive( self.__inpath )[ 0 ] if isinstance( filepath, str ) else None
        self.__report = r'etc\templates\report\ReportBase.xlsx'

    def __str__( self ):
       if self.__path is not None:
           return str( self.__path )

    def exists( self ):
        if os.path.exists( self.__inpath ):
            return True
        else:
            return False

    def isfolder( self ):
        if os.path.isdir( self.__inpath ):
            return True
        else:
            return False

    def isfile( self ):
        if os.path.isfile( self.__inpath ):
            return True
        else:
            return False

    def verify( self, other ):
        '''Verifies if the parameter 'other' exists'''
        if os.path.exists( other ):
            return True
        else:
            return False

    def getextension( self, other ):
        '''Returns string representing the file extension of 'other' '''
        if isinstance( other, str ):
            return  os.path.splitext( other )[ 1 ]

    def getreportpath( self ):
        if isinstance( self.__report, str ):
            return self.__report

    def join( self, first, second ):
        ''' Concatenates 'first' to 'second' '''
        if os.path.exists( first ) and os.path.exists( second ):
            return os.path.join( first, second )


class DbPath( ):
    '''class providing database paths'''
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
    def accessdata( self ):
        if isinstance( self.__accessdata, str ) and self.__accessdata != '':
            return os.path.relpath( self.__accessdata )

    @accessdata.setter
    def accessdata( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accessdata = os.path.relpath( value )

    @property
    def accessreference( self ):
        if isinstance( self.__accessreference, str ) and self.__accessreference != '':
            return os.path.relpath( self.__accessreference )

    @accessreference.setter
    def accessreference( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accessreference = os.path.relpath( value )

    @property
    def sqlitedata( self ):
        if isinstance( self.__sqlitedata, str ) and self.__sqlitedata != '':
            return os.path.relpath( self.__sqlitedata )

    @sqlitedata.setter
    def sqlitedata( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sqlitedata = os.path.relpath( value )

    @property
    def sqlitereference( self ):
        if isinstance( self.__sqlitereference, str ) and self.__sqlitereference != '':
            return os.path.relpath( self.__sqlitereference )

    @sqlitereference.setter
    def sqlitereference( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sqlitereference = os.path.relpath( value )

    @property
    def sqldata( self ):
        if isinstance( self.__sqldata, str ) and self.__sqldata != '':
            return os.path.relpath( self.__sqldata )

    @sqldata.setter
    def sqldata( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sqldata = os.path.relpath( value )

    @property
    def sqlreference( self ):
        if isinstance( self.__sqlreference, str ) and self.__sqlreference != '':
            return os.path.relpath( self.__sqlreference )

    @sqlreference.setter
    def sqlreference( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sqlitereference = os.path.relpath( value )

    def __init__( self ):
        self.__sqlitedata = r'C:\Users\teppler\source\repos\BudgetPy' \
                            r'\db\sqlite\datamodels\Data.db'
        self.__sqlitereference = r'C:\Users\teppler\source\repos\BudgetPy' \
                                 r'\db\sqlite\referencemodels\References.db'
        self.__accessdriver = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='
        self.__accessdata = r'C:\\Users\teppler\source\repos\BudgetPy' \
                            r'\db\access\datamodels\Data.accdb'
        self.__accessreference = r'C:\\Users\teppler\source\repos\BudgetPy' \
                                 r'\db\access\referencemodels\References.accdb'
        self.__sqldriver = r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLExpress;'
        self.__sqldata = r'C:\Users\teppler\source\repos\BudgetPy' \
                         r'\db\mssql\datamodels\Data.mdf'
        self.__sqlreference = r'C:\Users\teppler\source\repos\BudgetPy' \
                              r'\db\mssql\referencemodels\References.mdf'


class SqlRepo( ):
    '''class providing paths to the sql getsubfolders'''
    __accessdatamodels = None
    __accessreferencemodels = None
    __sqlitedatamodels = None
    __sqlitereferencemodels = None
    __sqldatamodels = None
    __sqlreferencemodels = None

    @property
    def accessdatamodels( self ):
        if isinstance( self.__accessdatamodels, str ) \
                and self.__accessdatamodels != '':
            return self.__accessdatamodels

    @accessdatamodels.setter
    def accessdatamodels( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accessdatamodels = value

    @property
    def accessreferencemodels( self ):
        if isinstance( self.__accessreferencemodels, str ) \
                and self.__accessreferencemodels != '':
            return self.__accessreferencemodels

    @accessreferencemodels.setter
    def accessreferencemodels( self, value ):
        if isinstance( value, str ) and value != '':
            self.__accessreferencemodels = value

    @property
    def sqlitedatamodels( self ):
        if isinstance( self.__sqlitedatamodels, str ) \
                and self.__sqlitedatamodels != '':
            return self.__sqlitedatamodels

    @sqlitedatamodels.setter
    def sqlitedatamodels( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sqlitedatamodels = value

    @property
    def sqlitereferencemodels( self ):
        if isinstance( self.__sqlitereferencemodels, str ) \
                and self.__sqlitereferencemodels != '':
            return self.__sqlitereferencemodels

    @sqlitereferencemodels.setter
    def sqlitereferencemodels( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sqlitereferencemodels = value

    @property
    def sqldatamodels( self ):
        if isinstance( self.__sqldatamodels, str ) \
                and self.__sqldatamodels != '':
            return self.__sqldatamodels

    @sqldatamodels.setter
    def sqldatamodels( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sqldatamodels = value

    @property
    def sqlreferencemodels( self ):
        if isinstance( self.__sqlreferencemodels, str ) \
                and self.__sqlreferencemodels != '':
            return self.__sqlreferencemodels

    @sqlreferencemodels.setter
    def sqlreferencemodels( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sqlitereferencemodels = value

    def __init__( self ):
        self.__sqlitedatamodels = r'C:\Users\teppler\source\repos\BudgetPy' \
                            r'\db\sqlite\datamodels\sql'
        self.__sqlitereferencemodels = r'C:\Users\teppler\source\repos\BudgetPy' \
                                 r'\db\sqlite\referencemodels\sql'
        self.__accessdatamodels = r'C:\\Users\teppler\source\repos\BudgetPy' \
                            r'\db\access\datamodels\sql'
        self.__accessreferencemodels = r'C:\\Users\teppler\source\repos\BudgetPy' \
                                 r'\db\access\referencemodels\sql'
        self.__sqldatamodels = r'C:\Users\teppler\source\repos\BudgetPy' \
                         r'\db\mssql\datamodels\sql'
        self.__sqlreferencemodels = r'C:\Users\teppler\source\repos\BudgetPy' \
                                 r'\db\mssql\referencemodels\sql'


class SqlFile( ):
    '''class providing access to sql getsubfolders in the application'''
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

    def __init__( self, provider = None, source = None,
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
        self.__command = command if isinstance( command, SQL ) else None
        self.__source = source if isinstance( source, Source ) else None
        self.__provider = provider if isinstance( provider, Provider ) else None

    def getpaths( self ):
        sd = SqlRepo( )
        data = self.__data
        references = self.__references
        folder = ''
        if self.__provider.name == 'SQLite' and self.__source.name in data:
            folder = f'{ sd.sqlitedatamodels }\\{self.__command.name}'
            return BudgetFolder( folder ).getsubfiles( )
        elif self.__provider.name == 'SQLite' and self.__source.name in references:
            folder = f'{ sd.sqlitereferencemodels }\\{self.__command.name}'
            return BudgetFolder( folder ).getsubfiles( )
        elif self.__provider.name == 'Access' and self.__source.name in data:
            folder = f'{ sd.accessdatamodels }\\{self.__command.name}'
            return BudgetFolder( folder ).getsubfiles( )
        elif self.__provider.name == 'Access' and self.__source.name in references:
            folder = f'{ sd.accessreferencemodels }\\{self.__command.name}'
            return BudgetFolder( folder ).getsubfiles( )
        elif self.__provider.name == 'SqlServer' and self.__source.name in data:
            folder = f'{ sd.sqldatamodels }\\{self.__command.name}'
            return BudgetFolder( folder ).getsubfiles( )
        elif self.__provider.name == 'SqlServer' and self.__source.name in references:
            folder = f'{ sd.sqlreferencemodels }\\{self.__command.name}'
            return BudgetFolder( folder ).getsubfiles( )
        else:
            folder = f'{sd.sqlitedatamodels}\\{self.__command.name}'
            return BudgetFolder( folder ).getsubfiles( )

    def getdirectory( self ):
        sd = SqlRepo( )
        data = self.__data
        reference = self.__references
        name = self.__source.name
        folder = ''
        if self.__provider.name == 'SQLite' and self.__source.name in data:
            path = f'{ sd.sqlitedatamodels }\\{ self.__command.name }'
            return os.path.relpath( path )
        elif self.__provider.name == 'SQLite' and self.__source.name in reference:
            path = f'{ sd.sqlitereferencemodels }\\{ self.__command.name }'
            return os.path.relpath( path )
        elif self.__provider.name == 'Access' and self.__source.name in data:
            path = f'{ sd.accessdatamodels }\\{ self.__command.name }'
            return os.path.relpath( path )
        elif self.__provider.name == 'Access' and self.__source.name in reference:
            path = f'{ sd.accessreferencemodels }\\{ self.__command.name }'
            return os.path.relpath( path )
        elif self.__provider.name == 'SqlServer' and self.__source.name in data:
            path = f'{ sd.sqldatamodels }\\{ self.__command.name }'
            return os.path.relpath( path )
        elif self.__provider.name == 'SqlServer' and self.__source.name in reference:
            path = f'{ sd.sqlreferencemodels }\\{ self.__command.name }'
            return os.path.relpath( path )
        else:
            path = f'{ sd.sqlitedatamodels }\\{ self.__command.name }'
            return os.path.relpath( path )

    def getquery( self ):
        table = self.__source.name
        names = self.getpaths( )
        folder = self.getdirectory( )
        query = ''
        for i in names:
            name = os.path.basename( i )
            if name.endswith( table + '.sql' ):
                query = open( i )
                sql = query.read( )
                return sql


# BudgetFile( filepath )
class BudgetFile( ):
    '''BudgetFile( filepath ) initializes the
     BudgetFile Class providing file information for
     getsubfolders used in the application'''
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
        '''Get the name property'''
        if not self.__name == '':
            return self.__name

    @name.setter
    def name( self, value ):
        '''Set the name property'''
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
        '''Set the currentdirectory directory to 'filepath' '''
        if os.path.exists( value ) and os.path.isdir( value ):
            os.chdir( value )
            self.__currdir = value

    def __init__( self, filepath = None ):
        self.__path = filepath if isinstance( filepath, str ) and filepath != '' else None
        self.__name = os.path.basename( filepath )
        self.__size = os.path.getsize( filepath )
        self.__directory = os.path.dirname( filepath )
        self.__extension = list( os.path.splitext( filepath ) )[ 1 ]
        self.__created = os.path.getctime( filepath )
        self.__accessed = os.path.getatime( filepath )
        self.__modified = os.path.getmtime( filepath )
        self.__currdir = os.getcwd( )
        self.__drive = os.path.splitdrive( filepath )[ 0 ] if os.path.isabs( filepath ) \
            else os.path.splitdrive( os.path.join( self.__currdir, filepath ) )[ 0 ]

    def __str__( self ):
        if isinstance( self.__path, str ) and self.__path != '':
            return self.__path

    def rename( self, other ):
        '''Renames the currentdirectory file to 'other' '''
        if isinstance( other, str ) and not other == '':
            src = os.path.abspath( self.__path )
            dst = os.path.join( self.directory, other )
            os.rename( src, dst )
            return dst

    def move( self, destination ):
        '''renames currentdirectory file'''
        if os.path.isdir( destination ):
            return os.path.join( self.__name, destination )

    def create( self, other, lines = None ):
        ''' creates and returns 'filepath' file '''
        if isinstance( other, str ):
            newfile = open( other, 'w' )
            if isinstance( lines, list ) and len( lines ) > 0:
                for line in lines:
                    newfile.write( line )

                newfile.flush( )

    def exists( self, other ):
        '''determines if an external file exists'''
        if other is not None:
            return os.path.exists( other )

    def delete( self, other ):
        ''' deletes file at 'self.__filepath'   '''
        if os.path.isfile( other ):
            os.remove( other )

    def getsize( self, other ):
        '''gets the size of another file'''
        if self.__path is not None and os.path.isfile( other ):
            return os.path.getsize( other )

    def getdrive( self, other ):
        '''gets the drive of another file'''
        if os.path.exists( other ):
            return str( list( os.path.splitdrive( other ) )[ 0 ] )

    def getextension( self, other ):
        ''' gets and returns extension of 'filepath' 'file' '''
        if other is not None and os.path.isfile( other ):
            return str( list( os.path.splitext( other ) )[ 1 ] )

    def readlines( self, other ):
        '''reads all lines in 'other' into a list
            then returns the list '''
        if os.path.isfile( other ):
            file = open( other, 'r' )
            contents = file.readlines( )
            file.close( )
            return contents

    def readall( self, other ):
        '''reads a single line from the file into a string
            then returns the string'''
        contents = ''
        if os.path.isfile( other ):
            file = open( other, 'r' )
            contents = file.read( )
            file.close( )
            return contents

    def writelines( self, lines = None ):
        ''' writes the contents of 'lines' to self.__contents '''
        if isinstance( lines, list ):
            path = os.path.relpath( self.__path )
            contents = open( path, 'a' )
            for line in lines:
                contents.write( line )
            contents.flush( )
            return contents

    def writeall( self, other ):
        ''' writes the contents of 'lines' to self.__contents '''
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


# BudgetFolder( filepath )
class BudgetFolder( ):
    '''BudgetFolder( filepath ) initializes the
     BudgetFolder Class providing file directory information'''
    __path = None
    __name = None
    __parent = None
    __dir = None
    __drive = None
    __current = None

    @property
    def name( self ):
        '''Returns string representing the name of the filepath 'base' '''
        if os.path.exists( self.__path ):
            return str( list( os.path.split( self.__path ) )[ 1 ] )

    @name.setter
    def name( self, value ):
        '''Returns string representing the name of the filepath 'base' '''
        if isinstance( value, str ):
            self.__path = value

    @property
    def directory( self ):
        '''Returns string representing the name of the filepath 'base' '''
        if not self.__dir == '':
            return self.__dir

    @directory.setter
    def directory( self, value ):
        '''Returns string representing the name of the filepath 'base' '''
        if os.path.isdir( value ):
            self.__dir = value

    @property
    def path( self ):
        if not self.__path == '':
            return self.__path

    @path.setter
    def path( self, value ):
        if os.path.exists( value ):
            self.__path = str( value )

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
        self.__path = folderpath if isinstance( folderpath, str ) else None
        self.__name = os.path.basename( folderpath )
        self.__dir = os.path.dirname( folderpath )
        self.__parent = os.path.dirname( folderpath )

    def __str__( self ):
        if self.__path is not None:
            return self.__path

    def getsubfiles( self ):
        '''Iterates getsubfolders in the base directory'''
        path = self.__path
        filenames = [ ]
        for i in os.walk( path ):
            if len( i[ 2 ] ) > 0 and len( i[ 0 ] ) > 0:
                for file in i[ 2 ]:
                    path = os.path.join( i[ 0 ], file )
                    if os.path.isfile( path ):
                        filenames.append( path )

        return filenames

    def getsubfolders( self ):
        '''Iterates getsubfolders in the base directory'''
        path = self.__path
        filenames = [ ]
        for i in os.walk( path ):
            if len( i[ 1 ] ) > 0 and len( i[ 0 ] ) > 0:
                for file in i[ 1 ]:
                    path = os.path.join( i[ 0 ], file )
                    if not os.path.isfile( path ):
                        filenames.append( path )

        return filenames

    def rename( self, new_name ):
        '''renames currentdirectory file'''
        if self.__name is not None and isinstance( new_name, str ):
            return os.rename( self.__name, new_name )

    def move( self, destination ):
        '''renames currentdirectory file'''
        if not destination == '' and not os.path.exists( destination ):
            return os.path.join( self.__name, destination )

    def exists( self, other ):
        '''determines if the base file exists'''
        if not other == '' and os.path.isdir( other ):
            return True

    def create( self, other ):
        if other is not None:
            os.mkdir( other )

    def delete( self, other ):
        ''' deletes 'filepath' directory '''
        if other is not None and os.path.isdir( other ):
            os.rmdir( other )

    def getsize( self, other ):
        ''' gets and returns size of 'filepath' '''
        if other is not None and os.path.isdir( other ):
            return os.path.getsize( other )

    def getdrive( self, other ):
        ''' gets and returns parent directory of 'filepath' '''
        if other is not None and os.path.isdir( other ):
            return os.path.splitdrive( other )[ 0 ]

    def iterate( self ):
        '''iterates getsubfolders in the base directory'''
        if os.path.isdir( self.__path ):
            for i in os.scandir( self.__path ):
                yield i

    def getfiles( self, other ):
        '''iterates getsubfolders in the directory provided by 'other' '''
        if os.path.isdir( other ):
            names = os.listdir( other )
            files = [ ]
            for i in names:
                file = os.path.join( other, i )
                if os.path.isfile( file ):
                    files.append( file )

            return files


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


# ExcelFile( filepath )
class ExcelFile(  ):
    '''ExcelFile( filepath ) class provides
    the spreadsheet for Budget Py reports '''
    __path = None
    __workbook = None
    __worksheet = None
    __name = None

    @property
    def path( self ):
        ''' Get the name of the workbook '''
        if os.path.exists( self.__path ):
            return self.__path

    @path.setter
    def path( self, value ):
        if os.path.exists( value ):
            self.__path = value

    @property
    def name( self ):
        ''' Get the name of the workbook '''
        if self.__name is not None:
            return self.__name

    @name.setter
    def name( self, value ):
        if value is not None and len( value ) > 0:
            self.__name = str( value )

    @property
    def workbook( self ):
        ''' Gets the report template '''
        if self.__path is not None:
            self.__workbook = self.__path
            return self.__workbook

    @workbook.setter
    def workbook( self, value ):
        ''' Gets the report template '''
        if os.path.exists( value ):
            self.__workbook = value

    @property
    def worksheet( self ):
        ''' Gets the workbooks worksheet '''
        if self.__worksheet is not None:
            return self.__worksheet

    @worksheet.setter
    def worksheet( self, value ):
        ''' Gets the workbooks worksheet '''
        if not value == '':
            self.__worksheet = value

    def __str__( self ):
        if self.__path is not None:
            return self.__path

    def __init__( self, filepath ):
        self.__path = filepath if os.path.exists( filepath ) else 'NS'
        self.__name = os.path.split( self.__path )[ 1 ]


# ExcelReport( name, rows = 46, cols = 12 )
class ExcelReport( ):
    '''ExcelReport( name ) class provides
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
        ''' Get the name of the workbook '''
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


# ZipFile( filepath )
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
        if not self.__filepath == '':
            zp.ZipFile( self.__zippath, 'w' ).write( self.__filepath, self.__name )

    def unzip( self ):
        ''' Extracts zip file contents '''
        if os.path.exists( self.__zippath ):
            file = zp.ZipFile( self.__zippath )
            file.extractall( self.__zippath )
