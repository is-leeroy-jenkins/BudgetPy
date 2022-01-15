class EmailBuilder():
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
    def sender( self, frm ):
        ''' Set the sender's email address '''
        if frm is not None:
            self.__from = str( frm )

    @property
    def receiver( self ):
        ''' Gets the sender's email address '''
        if self.__to is not None:
            return self.__to

    @receiver.setter
    def receiver( self, rec ):
        ''' Sets the receiver's email address '''
        if rec is not None:
            self.__to = str( rec )

    @property
    def subject( self ):
        ''' Gets the email's subject line '''
        if self.__subject is not None:
            return self.__subject

    @subject.setter
    def subject( self, sub ):
        ''' Sets the email's subject line '''
        if sub is not None:
            self.__to = str( sub )

    @property
    def body( self ):
        ''' Gets the email's subject line '''
        if self.__message is not None:
            return self.__message

    @body.setter
    def body( self, msg ):
        ''' Sets the email's subject line '''
        if msg is not None:
            self.__to = str( msg )

    @property
    def copy( self ):
        ''' Gets the addresses to send copies  '''
        if self.__others is not None:
            return self.__others

    @copy.setter
    def copy( self, copy ):
        ''' Sets the address's to send copies  '''
        if copy is not None:
            self.__others = list( copy )

    def __init__( self, frm = None, to = None,
                  body = None, sub = None, copy = None ):
        self.__from = str( frm )
        self.__to = str( to )
        self.__message = str( body )
        self.__others = list( copy )
        self.__subject = str( sub )

    def __str__( self ):
        if self.__message is not None:
            return self.__message

