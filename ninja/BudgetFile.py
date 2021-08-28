import os

class BudgetFile():
    '''Defines the BudgetFile Class'''
    # pseudo-private backing fields
    __base = None
    __name = None
    __path = None
    __size = None
    __extension = None
    __parent_folder = None
    __drive = None
    __created = None
    __modified = None
    __accessed = None
    __current = None

    @property
    def base( self ):
        return self.__base

    @property
    def name( self ):
        return os.path.basename( self.__base )

    @property
    def path( self ):
        if self.__path is not None:
            return self.__path

    @property
    def size( self ):
        if self.__parent_folder is not None:
            return self.__size

    @property
    def extension( self ):
        if self.__extension is not None:
            return self.__extension

    @property
    def parent_folder( self ):
        if self.__parent_folder is not None:
            return self.__parent_folder

    @property
    def drive( self ):
        if self.__drive is not None:
            return self.__drive

    @property
    def modified( self ):
        if self.__modified is not None:
            return self.__modified

    @property
    def accessed( self ):
        if self.__accessed is not None:
            return self.__accessed

    @property
    def created( self ):
        if self.__created is not None:
            return self.__created

    # Constructor
    def __init__( self, base ):
        self.__base = base
        self.__name = os.path.basename( base )
        self.__path = os.path.abspath( base )
        self.__size = os.path.getsize( base )
        self.__extension = list( os.path.splitext( base ) )[ 1 ]
        self.__created = os.path.getctime( base )
        self.__accessed = os.path.getatime( base )
        self.__modified = os.path.getmtime( base )
        self.__parent_folder = os.path.dirname( base )

    def get_current_directory( self ):
        '''gets the current directory'''
        self.__current = os.getcwd()
        return self.__current

    def rename( self, new_name ):
        '''renames current file'''
        return os.rename( self.__name, new_name )

    def move( self, destination_path ):
        '''renames current file'''
        return os.path.join( self.__name, destination_path )

    def exists( self ):
        '''determines if the base file exists'''
        if os.path.isfile( self.__base ):
            return True

    def get_drive( self ):
        '''get the file's drive'''
        return list(os.path.splitdrive( self.__path ))[0]

    def verify( self, other_filepath ):
        '''determines if an external file exists'''
        if other_filepath != '':
            return os.path.exists( other_filepath )

    def get_size( self ):
        '''gets the size of the base file'''
        return os.path.getsize( self.__name )

