class OpenCommitment:
    '''Defines the commitment class.'''
    __amount = None
    __account = None
    __document = None
    __bfy = None
    __fund = None
    __org = None
    __boc = None
    __data = None
    __dataframe = None

    @property
    def amount( self ):
        if self.__amount is not None:
            return self.__amount

    @amount.setter
    def amount( self, value ):
        if value is not None:
            self.__amount = float( value )
            self.__data[ 'amount' ] = self.__amount

    @property
    def account( self ):
        if self.__account is not None:
            return self.__account

    @account.setter
    def account( self, code ):
        if code is not None:
            self.__account = Account( str( code ) )
            self.__data[ 'account' ] = self.__account

    @property
    def document( self ):
        if self.__document is not None:
            return self.__document

    @document.setter
    def document( self, doc ):
        if doc is not None:
            self.__document = str( doc )
            self.__data[ 'document' ] = self.__document

    @property
    def org( self ):
        if self.__org is not None:
            return self.__org

    @org.setter
    def org( self, code ):
        if code is not None:
            self.__org = Organization( str( code ) )
            self.__data[ 'org' ] = self.__org

    @property
    def bfy( self ):
        if self.__bfy is not None:
            return self.__bfy

    @bfy.setter
    def bfy( self, year ):
        if year is not None:
            self.__bfy = BudgetFiscalYear( str( year ) )
            self.__data[ 'bfy' ] = self.__bfy

    @property
    def fund( self ):
        if self.__fund is not None:
            return self.__fund

    @fund.setter
    def fund( self, code ):
        if code is not None:
            self.__fund = Fund( str( code ) )
            self.__data[ 'fund' ] = self.__fund

    @property
    def boc( self ):
        if self.__boc is not None:
            return self.__boc

    @boc.setter
    def boc( self, code ):
        if code is not None:
            self.__boc = BudgetObjectClass( str( code ) )
            self.__data[ 'boc' ] = self.__boc

    @property
    def data( self ):
        if self.__data is not None:
            return self.__data

    @property
    def table( self ):
        if self.__dataframe is not None:
            return self.__dataframe

    def __init__( self, amount ):
        self.__amount = float( amount )
        self.__data = { 'amount': self.__amount,
                        'account': None,
                        'document': None,
                        'org': None,
                        'bfy': None,
                        'fund': None,
                        'boc': None }
        self.__dataframe = pd.DataFrame

    def __str__( self ):
        if self.__amount is not None:
            return str( self.__amount )


