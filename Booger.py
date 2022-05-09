import os
from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
import fitz
from sys import exit
import Static
from Ninja import *
from Static import *
import textwrap
import datetime
import random
import io
from googlesearch import search
from Minion import App
import smtplib as smtp
from email.message import EmailMessage



# ButtonIcon( png )
class ButtonIcon( ):
    '''class representing form images'''
    __button = None
    __name = None
    __filepath = None

    @property
    def folder( self ):
        if isinstance( self.__button, str ) and self.__button != '':
            return self.__button

    @folder.setter
    def folder( self, value ):
        if isinstance( value, str ) and value != '':
            self.__button = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ):
            self.__name = value

    @property
    def filepath( self ):
        if isinstance( self.__filepath, str ) and self.__filepath != '':
            return self.__filepath

    @filepath.setter
    def filepath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__filepath = value

    def __init__( self, png ):
        self.__name = png.name if isinstance( png, PNG ) else None
        self.__button = r'C:\Users\terry\source\repos\BudgetPy\etc\img\button'
        self.__filepath = self.__button + r'\\' + self.__name + '.png'

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath


# TitleIcon( ico )
class TitleIcon( ):
    '''class representing form images'''
    __folder = None
    __name = None
    __filepath = None

    @property
    def folder( self ):
        if isinstance( self.__button, str ) and self.__button != '':
            return self.__button

    @folder.setter
    def folder( self, value ):
        if isinstance( value, str ) and value != '':
            self.__button = value

    @property
    def name( self ):
        if isinstance( self.__name, str ) and self.__name != '':
            return self.__name

    @name.setter
    def name( self, value ):
        if isinstance( value, str ):
            self.__name = value

    @property
    def filepath( self ):
        if isinstance( self.__filepath, str ) and self.__filepath != '':
            return self.__filepath

    @filepath.setter
    def filepath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__filepath = value

    def __init__( self, ico ):
        self.__name = ico.name if isinstance( ico, ICO ) else None
        self.__folder = r'C:\Users\terry\source\repos\BudgetPy\etc\ico'
        self.__filepath = self.__folder + r'\\' + self.__name + r'.ico'

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath


class Sith( ):
    '''Base class for the dark-mode controls'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __themefont = None

    @property
    def themebackground( self ):
        if isinstance( self.__themebackground, str ) and self.__themebackground != '':
            return self.__themebackground

    @themebackground.setter
    def themebackground( self, value ):
        if isinstance( value, str ) and value != '':
            self.__themebackground = value

    @property
    def elementbackcolor( self ):
        if isinstance( self.__elementbackcolor, str ) and self.__elementbackcolor != '':
            return self.__elementbackcolor

    @elementbackcolor.setter
    def elementbackcolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__elementbackcolor = value

    @property
    def elementforecolor( self ):
        if isinstance( self.__elementforecolor, str ) and self.__elementforecolor != '':
            return self.__elementforecolor

    @elementbackcolor.setter
    def elementforecolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__elementforecolor = value

    @property
    def textforecolor( self ):
        if isinstance( self.__themetextcolor, str ) and self.__themetextcolor != '':
            return self.__themetextcolor

    @textforecolor.setter
    def textforecolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__themetextcolor = value

    @property
    def textbackcolor( self ):
        if isinstance( self.__textbackcolor, str ) and self.__textbackcolor != '':
            return self.__textbackcolor

    @textbackcolor.setter
    def textbackcolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__textbackcolor = value

    @property
    def inputbackcolor( self ):
        if isinstance( self.__inputbackcolor, str ) and self.__inputbackcolor != '':
            return self.__inputbackcolor

    @inputbackcolor.setter
    def inputbackcolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__inputbackcolor = value

    @property
    def inputforecolor( self ):
        if isinstance( self.__inputforecolor, str ) and self.__inputforecolor != '':
            return self.__inputforecolor

    @inputforecolor.setter
    def inputforecolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__inputforecolor = value

    @property
    def buttoncolor( self ):
        if isinstance( self.__buttoncolor, str ) and self.__buttoncolor != '':
            return self.__buttoncolor

    @buttoncolor.setter
    def buttoncolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__buttoncolor = value

    @property
    def iconpath( self ):
        if isinstance( self.__icon, str ) and self.__icon != '':
            return self.__icon

    @iconpath.setter
    def iconpath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__icon = value

    @property
    def themefont( self ):
        if isinstance( self.__themefont, tuple ) :
            return self.__themefont

    @themefont.setter
    def themefont( self, value ):
        if isinstance( value, tuple ) :
            self.__themefont = value

    def __init__( self ):
        self.__themebackground = '#0F0F0F'
        self.__themetextcolor = '#D3D3D3'
        self.__elementbackcolor = '#0F0F0F'
        self.__elementforecolor = '#D3D3D3'
        self.__textbackcolor = '#0F0F0F'
        self.__inputforecolor = '#FFFFFF'
        self.__inputbackcolor = '#282828'
        self.__buttoncolor = '#163754'
        self.__icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        self.__themefont = ( 'Roboto', 9 )
        sg.theme_background_color( self.__themebackground )
        sg.theme_element_background_color( self.__elementbackcolor )
        sg.theme_element_text_color( self.__elementforecolor )
        sg.theme_input_text_color( self.__inputforecolor )
        sg.theme_text_element_background_color( self.__textbackcolor )
        sg.theme_input_background_color( self.__inputbackcolor )
        sg.theme_text_color( self.__themetextcolor )
        sg.theme_button_color( self.__buttoncolor )


# FileDialog( ) -> str
class FileDialog( Sith ):
    '''class that renames a file'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __themefont = None
    __filepath = None
    __formsize = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def filepath( self ):
        if isinstance( self.__filepath, str ) and self.__filepath != '':
            return self.__filepath

    @filepath.setter
    def filepath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__filepath = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__filepath = None

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath

    def show( self ):
        layout = [ [ sg.Text( r'' ) ],
           [ sg.Text( 'Search for File' ) ],
           [ sg.Text( r'' ) ],
           [ sg.Input( key = '-PATH-' ), sg.FileBrowse( size = ( 15, 1 ) ) ],
           [ sg.Text( r'' ) ],
           [ sg.Text( r'' ) ],
           [ sg.OK( size = ( 8, 1 ),  ), sg.Cancel( size = ( 10, 1 )  ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            font = self.__themefont,
            icon = self.__icon,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel' ):
                break
            elif event == 'OK':
                self.__filepath = values[ '-PATH-' ]
                sg.popup_ok( self.__filepath,
                    title = 'Results',
                    icon = self.__icon,
                    font = self.__themefont )

        window.close( )


# FolderDialog( ) -> str
class FolderDialog( Sith ):
    '''class that renames a folder'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __folderpath = None


    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def folderpath( self ):
        if isinstance( self.__folderpath, str ) and self.__folderpath != '':
            return self.__folderpath

    @folderpath.setter
    def folderpath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__folderpath = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__folderpath = None

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath

    def show( self ):
        layout = [ [ sg.Text( r'' ) ],
           [ sg.Text( 'Search for Directory' ) ],
           [ sg.Text( r'' ) ],
           [ sg.Input( ), sg.FolderBrowse( size = ( 15, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.OK( size = ( 8, 1 ) ), sg.Cancel( size = ( 10, 1 ) ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            font = self.__themefont,
            icon = self.__icon,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel' ):
                break

        window.close( )


# SaveFileDialog( path )
class SaveFileDialog( Sith ):
    '''class provides form to located file destinations'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __original = None
    __filename = None

    @property
    def text( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    @text.setter
    def text( self, value ):
        if isinstance( value, str ) and value != '':
            self.__text = value

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def original( self ):
        if isinstance( self.__original, str ) and self.__original != '':
            return self.__original

    @original.setter
    def original( self, value ):
        if isinstance( value, str) and os.path.exists( value ):
            self_original = value

    def __init__( self, path = None ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 400, 200 )
        self.__original = path if isinstance( path, str) and os.path.isfile( path ) else None

    def show( self ):
        username = os.environ.get( 'USERNAME' )
        startpath = f'C:\\Users\\{username}\\Desktop'
        filename = sg.popup_get_file( 'Select Location / Enter File Name',
            default_path = startpath,
            title = 'Budget Execution',
            font = self.__themefont,
            icon = self.__icon,
            save_as = True )

        if isinstance( self.__original, str) and os.path.exists( self.__original ):
            src = io.open( self.__original, 'r' ).read( )
            new = io.open( filename, 'w+' ).write( src )


# GoogleDialog(  ) -> list
class GoogleDialog( Sith ):
    '''class that renames a folder'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None
    __querytext = None
    __results = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def search( self ):
        if isinstance( self.__querytext, str ) and self.__querytext != '':
            return self.__querytext

    @search.setter
    def search( self, value ):
        if isinstance( value, str ) and value != '':
            self.__querytext = value

    @property
    def image( self ):
        if isinstance( self.__image, str ) and self.__image != '':
            return self.__image

    @image.setter
    def image( self, value ):
        if isinstance( value, str ) and value != '':
            self.__image = value

    @property
    def results( self ):
        if isinstance( self.__results, str ) and self.__results != '':
            return self.__results

    @search.setter
    def results( self, value ):
        if isinstance( value, str ) and value != '':
            self.__results = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\google.png'
        self.__querytext = None
        self.__results = [ ]

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath

    def show( self ):
        layout =  [ [ sg.Text( r'' ) ],
            [ sg.Image( filename = self.__image ) ],
            [ sg.Text( '', size = ( 10, 1 ) ), sg.Input( '', key = '-QUERY-', size = ( 40, 2 ) ) ],
            [ sg.Text( r'', size = ( 100, 1 ) ) ],
            [ sg.Text( r'', size = ( 100, 1 ) ) ],
            [ sg.Text( r'', size = ( 10, 1 ) ), sg.Submit( size = ( 15, 1 ) ),
              sg.Text( r'', size = ( 10, 1 ) ), sg.Cancel( size = ( 15, 1 ) ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_X_EVENT, sg.WIN_CLOSED, 'Cancel' ):
                break
            elif event == 'Submit':
                self.__querytext = values[ '-QUERY-' ]
                window.close( )
                query = search( term = self.__querytext, num_results = 5, lang = 'en' )
                chrome = Client.Chrome
                app = App( chrome )
                for result in query:
                    app.runargs( result )

        window.close( )


class EmailDialog( Sith ):
    '''class that renames a folder'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __image = None
    __formsize = None
    __themefont = None
    __folderpath = None


    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def folderpath( self ):
        if isinstance( self.__folderpath, str ) and self.__folderpath != '':
            return self.__folderpath

    @folderpath.setter
    def folderpath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__folderpath = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\outlook.png'
        self.__formsize = ( 600, 500 )
        self.__folderpath = None

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath

    def show( self ):
        btn = ( 20, 1 )
        inp = ( 35, 1 )
        spc = ( 5, 1 )
        layout = [ [ sg.T( ' ', size = spc ), ],
           [ sg.T( ' ', size = spc ), sg.Image( filename = self.__image ) ],
           [ sg.T( ' ', size = spc ), ],
           [ sg.T( ' ', size = spc ), sg.T( 'From:', size = btn ), sg.Input( key = '-EMAIL FROM-', size = ( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ), sg.T( 'To:', size = btn ),  sg.Input(key = '-EMAIL TO-', size = ( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ), sg.T( 'Subject:', size = btn ), sg.Input( key = '-EMAIL SUBJECT-', size = ( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ), sg.T( '' ) ],
           [ sg.T( ' ', size = spc ), sg.T( 'Username:', size = btn ), sg.Input( key='-USER-', size=( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ), sg.T( 'Password:', size = btn ), sg.Input(password_char='*', key = '-PASSWORD-', size= ( 35,1 ) ) ],
           [ sg.T( ' ', size = spc ) ],
           [ sg.T( ' ', size = spc ), sg.Multiline( 'Type your message here', size = ( 65, 10 ), key = '-EMAIL TEXT-' ) ],
           [ sg.T( ' ', size = ( 100, 1 ) ) ],
           [ sg.T( ' ', size = spc ),  sg.Button( 'Send', size = btn ),
             sg.T( ' ', size = btn ), sg.Button( 'Cancel', size = ( 20, 1 ) ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            icon = self.__icon,
            background_color = self.__themebackground,
            font = self.__themefont,
            button_color = self.__buttoncolor,
            size = self.__formsize )

        while True:  # Event Loop
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Cancel', 'Exit' ):
                break
            if event == 'Send':
                sg.popup_quick_message( 'Sending your message... this will take a moment...', background_color='red')
                send_an_email( from_address = values[ '-EMAIL FROM-' ],
                    to_address=values['-EMAIL TO-'],
                    subject=values['-EMAIL SUBJECT-'],
                    message_text=values['-EMAIL TEXT-'],
                    user=values['-USER-'],
                    password=values['-PASSWORD-'])

        window.close()


# Message( text )
class MessageDialog( Sith ):
    ''' class that provides form to display informational messages '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __text = None

    @property
    def text( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    @text.setter
    def text( self, value ):
        if isinstance( value, str ) and value != '':
            self.__text = value

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self, text ):
        self.__text = text if isinstance( text, str ) and text != '' else None
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 400, 200 )

    def __str__( self ):
        if isinstance( self.__text, str ):
            return self.__text

    def show( self ):
        layout = [ [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = (100, 1) ) ],
           [ sg.Text( r'', size = ( 5, 1 ) ),  sg.Text( self.__text, font = ( 'Roboto', 9, 'bold' ), text_color = '#FFFFFF', size = ( 80, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = ( 100, 1 ) ) ],
           [ sg.Text( r'', size = (5, 1) ), sg.Ok( size = (10, 1) ), 
             sg.Text( r'', size = (15, 1) ), sg.Cancel( size = (10, 1) ) ] ]

        window = sg.Window( r'  Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Ok', 'Cancel' ):
                break

        window.close( )


# Error( exception )
class ErrorDialog( Sith ):
    '''class that displays error message'''
    __message = None
    __cause = None
    __method = None
    __exception = None
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def message( self ):
        if isinstance( self.__message, str ) and self.__message != '':
            return self.__message

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__message = value

    def __init__( self, exception = None ):
        super( Sith, self ).__init__()
        self.__exception = exception if isinstance( exception, BudgetException ) else None
        self.__message = self.__exception.message if isinstance( exception, BudgetException ) else None
        self.__cause = self.__exception.cause if isinstance( exception, BudgetException ) else ''
        self.__method = self.__exception.method if isinstance( exception, BudgetException ) else ''
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 500, 275 )

    def __str__( self ):
        if isinstance( self.__message, str ):
            return self.__message

    def show( self ):
        layout = [ [ sg.Text( r'', size = ( 150, 1 ) ) ],
           [ sg.Text( 'Source:', size = ( 10, 1 ) ), sg.Text( self.__cause, size = ( 80, 1 ) ) ],
           [ sg.Text( 'Method:', size = ( 10, 1 ) ), sg.Text( self.__method, size = ( 80, 1 ) ) ],
           [ sg.Text( r'', size = ( 150, 1 ) ) ],
           [ sg.Multiline( self.__message, size = ( 80, 7 ) ) ],
           [ sg.Text( r'' ) ],
           [ sg.Text( r'', size = ( 20, 1 ) ), sg.Cancel( size = ( 15, 1 ) ),
             sg.Text( r'', size = ( 10, 1 ) ), sg.Ok( size = ( 15, 1 ), key = '-OK-' ) ] ]

        window = sg.Window( r'  Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, '-OK-' ):
                break

        window.close( )


# Input( question )
class InputDialog( Sith ):
    '''class that produces a contact input form'''
    __question = None
    __response = None
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def question( self ):
        if isinstance( self.__question, str ) and self.__question != '':
            return self.__question

    @question.setter
    def question( self, value ):
        if isinstance( value, str ) and value != '':
            self.__question = value

    @property
    def response( self ):
        if isinstance( self.__response, str ) and self.__response != '':
            return self.__response

    @response.setter
    def response( self, value ):
        if isinstance( value, str ) and value != '':
            self.__response= value

    def __init__( self, question ):
        super( Sith, self ).__init__()
        self.__question = question if isinstance( question, str ) and question != '' else None
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__response = None

    def show( self ):
        layout =  [ [ sg.Text( r'' ) ],
            [ sg.Text( self.__question, font = ( 'Roboto', 9, 'bold' ) ) ],
            [ sg.Text( r'' ) ],
            [ sg.Text( 'Enter:', size = ( 10, 2 ) ), sg.InputText( '1', key = '-INPUT-', size = ( 40, 2 ) ) ],
            [ sg.Text( r'', size = ( 100, 1 ) ) ],
            [ sg.Text( r'', size = ( 100, 1 ) ) ],
            [ sg.Text( r'', size = ( 10, 1 ) ), sg.Submit( size = ( 10, 1 ), key = '-SUBMIT-' ),
              sg.Text( r'', size = ( 10, 1 ) ), sg.Cancel( size = ( 10, 1 ), key = '-CANCEL-' ) ] ]

        window = sg.Window( ' Budget Input', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            sg.popup( event, values, values[ '-INPUT-' ],
                text_color = self.__themetextcolor,
                font = self.__themefont,
                icon = self.__icon )

            if event in ( sg.WIN_X_EVENT, sg.WIN_CLOSED, 'Cancel' ):
                break

        window.close( )


# ContactForm( contact )
class ContactForm( Sith ):
    '''class that produces a contact input form'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\outlook.png'
        self.__formsize = ( 450, 200 )

    def show( self ):
        sg.theme_background_color( self.__themebackground )
        sg.theme_element_background_color( self.__elementbackcolor )
        sg.theme_element_text_color( self.__elementforecolor )
        sg.theme_input_text_color( self.__inputforecolor )
        sg.theme_text_element_background_color( self.__textbackcolor )
        sg.theme_input_background_color( self.__inputbackcolor )
        sg.theme_text_color( self.__themetextcolor )
        sg.theme_button_color( self.__buttoncolor )

        layout =  [ [ sg.Text( r'', size = ( 100, 1 ) ) ],
                    [ sg.Text( r'Enter Contact Details' ) ],
                    [ sg.Text( r'', size = ( 100, 1 ) ) ],
                    [ sg.Text( 'Name', size = ( 10, 1 ) ), sg.InputText( '1', size = ( 80, 1 ),  key = '-NAME-' ) ],
                    [ sg.Text( 'Address', size = ( 10, 1 ) ), sg.InputText( '2', size = ( 80, 1 ), key = '-ADDRESS-' ) ],
                    [ sg.Text( 'Phone', size = ( 10, 1 ) ), sg.InputText( '3', size = ( 80, 1 ), key = '-PHONE-' ) ],
                    [ sg.Text( r'', size = ( 100, 1 ) ) ],
                    [ sg.Text( r'', size = ( 100, 1 ) ) ],
                    [ sg.Text( r'', size = ( 10, 1) ), sg.Submit( size = ( 10, 1 ) ),
                      sg.Text( r'', size = ( 20, 1) ),  sg.Cancel( size = ( 10, 1 ) ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            sg.popup( 'Results', values, values[ '-NAME-' ],
                values[ '-ADDRESS-' ],
                values[ '-PHONE-' ],
                text_color = self.__themetextcolor,
                font = self.__themefont,
                icon = self.__icon )

            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel' ):
                break

        window.close( )


class GridForm( Sith ):
    '''object providing form that simulates a datagrid '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __fieldwidth = None
    __themefont = None
    __rows = None
    __columns = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def fieldwidth( self ):
        if isinstance( self.__fieldwidth, tuple ):
            return self.__fieldwidth

    @fieldwidth.setter
    def fieldwidth( self, value ):
        if isinstance( value, tuple ) and len( value ) == 2:
            self.__fieldwidth = value

    @property
    def rows( self ):
        if isinstance( self.__rows, int ):
            return self.__rows

    @rows.setter
    def rows( self, value ):
        if isinstance( value, int ):
            self.__rows = value

    @property
    def columns( self ):
        if isinstance( self.__columns, str ) and self.__columns != '':
            return self.__columns

    @columns.setter
    def columns( self, value ):
        if isinstance( value, int ):
            self.__columns = value

    def __init__( self, rows = 10, columns = 4 ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\outlook.png'
        self.__fieldwidth = ( 17, 1 )
        self.__rows = rows
        self.__columns = columns

    def show( self ):
        headings = [ 'HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4' ]
        space = [ [ sg.Text( ' ' ) ] ]
        header = [ [ sg.Text( ' ' ) ] + [ sg.Text( h, size = ( 15, 1 ) ) for h in headings ] ]
        records = [ [ [ sg.Input( size = self.__fieldwidth, pad = ( 0, 0 ), font = self.__themefont ) for c in range( self.__columns ) ] for r in range( self.__rows ) ],
                 [ sg.Text( '' ) ] ]
        buttons = [ [ sg.Text( '', size = ( 35, 1 ) ), sg.Submit( size = ( 10, 1 ), key = '-SUBMIT-'  ),
                      sg.Text( '', size = ( 5, 1 ) ), sg.Cancel( size = ( 10, 1 ), key = '-CANCEL-' ) ] ]
        layout = space + header + records + buttons

        window = sg.Window( 'Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont  )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, '-CANCEL-' ):
                break

        window.close( )


class LoadingPanel( Sith ):
    '''object providing form loading behavior '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\outlook.png'
        self.__formsize = ( 800, 600 )

    def show( self ):
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ( 'Bodoni MT', 40 ) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

        window = sg.Window( 'Loading', layout,
            icon = self.__icon,
            element_justification = 'c',
            margins = ( 0, 0 ),
            size = ( 800, 600 ),
            element_padding = ( 0, 0 ), finalize = True )

        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( self.__image ).info[ 'duration' ]

        while True:
            for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )

        window.close()


class WaitingPanel( Sith ):
    '''object providing form loader behavior '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\outlook.png'
        self.__themefont = ( 'Roboto', 9 )
        self.__formsize = ( 800, 600 )

    def show( self ):
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

        window = sg.Window( 'Loading', layout,
            icon = self.__icon,
            element_justification = 'c',
            margins = ( 0, 0 ),
            element_padding = ( 0, 0 ),
            size = ( 800, 600 ),
            finalize = True )

        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( self.__image ).info[ 'duration' ]

        while True:
            for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )

        window.close()


class ProcessingPanel( Sith ):
    '''object providing form processing behavior '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\web\outlook.png'
        self.__formsize = ( 800, 600 )

    def show( self ):
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

        window = sg.Window( 'Loading', layout,
            element_justification = 'c',
            icon = self.__icon,
            margins = ( 0, 0 ),
            size = ( 800, 600 ),
            element_padding = ( 0, 0 ),
            finalize = True )

        window[ '-T-' ].expand( True, True, True )
        interframe_duration = Image.open( self.__image ).info[ 'duration' ]

        while True:
            for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )

        window.close()


# Notification( message )
class Notification( Sith ):
    '''Class provides splash notification behaviors'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __image = None
    __message = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def message( self ):
        if isinstance( self.__message, str ) and self.__message != '':
            return self.__message

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__message = value

    @property
    def imagepath( self ):
        if isinstance( self.__image, str ) and image != '':
            return self.__image

    @imagepath.setter
    def imagepath( self, value ):
        if isinstance( value, str ) and value != '':
            return self.__image


    def __init__( self, message ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__image = r'C:\Users\terry\source\repos\BudgetPy\etc\img\app\notification\Ninja.png'
        self.__message = message if isinstance( message, str ) and message != '' else None

    def show( self ):
        sg.popup_notify( self.__message,
            title = 'Budget Execution',
            icon = self.__image,
            display_duration_in_ms = 9000,
            fade_in_duration = 5000,
            alpha = 1 )


class PdfForm( Sith ):
    '''Creates form to view a PDF'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 600, 400 )

    def show( self ):
        filename = sg.popup_get_file( 'Budget PDF', 'PDF file to open',
            file_types = ( ("PDF Files", "*.pdf"),
                           ("XPS Files", "*.*xps"),
                           ("Epub Files", "*.epub"),
                           ("Fiction Books", "*.fb2"),
                           ("Comic Books", "*.cbz"),
                           ("HTML",   "*.htm*") ),
            icon = self.__icon )

        if filename is None:
            sg.popup_cancel( 'Cancelling', icon = self.__icon  )
            exit( 0 )

        document = fitz.open( filename )
        pages = len( document )
        tablist = [ None ] * pages
        title = f'Budget Execution display of { filename }, pages: { pages }'

        def get_page( pno, zoom = 0 ):
            displaylist = tablist[ pno ]
            if not displaylist:
                tablist[ pno ] = document[ pno ].get_displaylist( )
                displaylist = tablist[ pno ]

            r = displaylist.rect
            mp = r.tl + ( r.br - r.tl ) * 0.5
            mt = r.tl + ( r.tr - r.tl ) * 0.5
            ml = r.tl + ( r.bl - r.tl ) * 0.5
            mr = r.tr + ( r.br - r.tr ) * 0.5
            mb = r.bl + ( r.br - r.bl ) * 0.5
            mat = fitz.Matrix( 2, 2 )

            if zoom == 1:
                clip = fitz.Rect( r.tl, mp )
            elif zoom == 4:
                clip = fitz.Rect( mp, r.br )
            elif zoom == 2:
                clip = fitz.Rect( mt, mr )
            elif zoom == 3:
                clip = fitz.Rect( ml, mb )
            if zoom == 0:
                pix = displaylist.get_pixmap( alpha = False )
            else:
                pix = displaylist.get_pixmap( alpha = False,
                    matrix = mat, clip = clip )

            return pix

        currentpage = 0
        data = get_page( currentpage )
        image_elem = sg.Image( data = data )
        goto = sg.InputText( str( currentpage + 1 ), size = ( 5, 1 ) )

        layout = [ [ sg.Button( 'Prev' ), sg.Button( 'Next' ), sg.Text( 'Page:' ), goto, ],
                   [ sg.Text( 'Zoom:' ), sg.Button( 'Top-L' ), sg.Button( 'Top-R' ),
                     sg.Button( 'Bot-L' ),  sg.Button( 'Bot-R' ), ],
                   [ image_elem ],  ]

        pdfkeys = ( 'Next', 'Next:34', 'Prev', 'Prior:33',
            'Top-L', 'Top-R', 'Bot-L', 'Bot-R', 'MouseWheel:Down', 'MouseWheel:Up' )
        zoombuttons = ( 'Top-L', 'Top-R', 'Bot-L', 'Bot-R' )
        window = sg.Window( title, layout,
            return_keyboard_events = True,
            icon = self.__icon,
            use_default_focus = False )

        oldpage = 0
        oldzoom = 0

        while True:
            event, values = window.read( timeout = 100 )
            zoom = 0
            forcepage = False
            if event == sg.WIN_CLOSED:
                break
            if event in ( 'Escape:27', ):
                break
            if event[ 0 ] == chr( 13 ):
                try:
                    while currentpage < 0:
                        currentpage += pages
                except:
                    currentpage = 0
                goto.update( str( currentpage + 1 ) )
            elif event in ( 'Next', 'Next:34', 'MouseWheel:Down' ):
                currentpage += 1
            elif event in ( 'Prev', 'Prior:33', 'MouseWheel:Up' ):
                currentpage -= 1
            elif event == 'Top-L':
                zoom = 1
            elif event == 'Top-R':
                zoom = 2
            elif event == 'Bot-L':
                zoom = 3
            elif event == 'Bot-R':
                zoom = 4
            if currentpage >= pages:
                currentpage = 0
            while currentpage < 0:
                currentpage += pages
            if currentpage != oldpage:
                zoom = oldzoom = 0
                forcepage = True
            if event in zoombuttons:
                if 0 < zoom == oldzoom:
                    zoom = 0
                    forcepage = True

                if zoom != oldzoom:
                    forcepage = True
            if forcepage:
                data = get_page( currentpage, zoom )
                image_elem.update( data = data )
                oldpage = currentpage
            oldzoom = zoom
            if event in pdfkeys or not values[ 0 ]:
                goto.update( str( currentpage + 1 ) )


# CalendarDialog( ) -> ( mm, dd, yyyy )
class CalendarDialog( Sith ):
    '''class creates form providing date selection behavior'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __date = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 250 )

    def show( self ):
        __btnsize = ( 20, 1 )
        __calendar = ( 200, 200 )

        months = [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
        'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ]

        days = [ 'SUN', 'MON', 'TUE', 'WEC', 'THU', 'FRI', 'SAT' ]

        cal = sg.popup_get_date( title = 'Calendar',
                                 no_titlebar = False,
                                 icon = self.__icon,
                                 month_names = months,
                                 day_abbreviations = days,
                                 close_when_chosen = True )


class DatePanel( Sith ):
    ''' Desktop widget displaying date time text'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __date = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 450, 250 )

    def show( self ):
        ALPHA = 0.9  # Initial alpha until user changes
        THEME = 'Dark green 3'  # Initial theme until user changes
        refresh_font = title_font = 'Courier 8'
        main_info_font = 'Courier 20'
        main_info_size = (10, 1)
        UPDATE_FREQUENCY_MILLISECONDS = 1000 * 60 * 60  # update every hour by default until set
        # by user

        def choose_theme( location, size ):
            """
            A window to allow new themes to be tried out.
            Changes the theme to the newly chosen one and returns theme's name
            Automaticallyi switches to new theme and saves the setting in user settings file

            :param location: (x,y) location of the Widget's window
            :type location:  Tuple[int, int]
            :param size: Size in pixels of the Widget's window
            :type size: Tuple[int, int]
            :return: The name of the newly selected theme
            :rtype: None | str
            """
            layout = [ [ sg.Text( 'Try a theme' ) ],
                       [ sg.Listbox( values = sg.theme_list( ), size = (20, 20), key = '-LIST-',
                           enable_events = True ) ],
                       [ sg.OK( ), sg.Cancel( ) ] ]

            window = sg.Window( 'Look and Feel Browser', layout, location = location,
                keep_on_top = True )
            old_theme = sg.theme( )
            while True:  # Event Loop
                event, values = window.read( )
                if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
                    break
                sg.theme( values[ '-LIST-' ][ 0 ] )
                window.hide( )
                # make at test window to the left of the current one
                test_window = make_window(
                    location = ((location[ 0 ] - size[ 0 ] * 1.2, location[ 1 ])),
                    test_window = True )
                test_window.read( close = True )
                window.un_hide( )
            window.close( )

            # after choice made, save theme or restore the old one
            if event == 'OK' and values[ '-LIST-' ]:
                sg.theme( values[ '-LIST-' ][ 0 ] )
                sg.user_settings_set_entry( '-theme-', values[ '-LIST-' ][ 0 ] )
                return values[ '-LIST-' ][ 0 ]
            else:
                sg.theme( old_theme )
            return None

        def make_window( location, test_window = False ):
            """
            Defines the layout and creates the window for the main window
            If the parm test_window is True, then a simplified, and EASY to close version is shown

            :param location: (x,y) location to create the window
            :type location: Tuple[int, int]
            :param test_window: If True, then this is a test window & will close by clicking on it
            :type test_window: bool
            :return: newly created window
            :rtype: sg.Window
            """
            title = sg.user_settings_get_entry( '-title-', '' )
            if not test_window:
                theme = sg.user_settings_get_entry( '-theme-', THEME )
                sg.theme( theme )

            # ------------------- Window Layout -------------------
            # If this is a test window (for choosing theme), then uses some extra Text Elements
            # to display theme text
            # and also enables events for the elements to make the window easy to close
            if test_window:
                top_elements = [ [ sg.Text( title, size = (20, 1), font = title_font,
                    justification = 'c', k = '-TITLE-', enable_events = True ) ],
                                 [ sg.Text( 'Click to close', font = title_font,
                                     enable_events = True ) ],
                                 [ sg.Text( 'This is theme', font = title_font,
                                     enable_events = True ) ],
                                 [ sg.Text( sg.theme( ), font = title_font,
                                     enable_events = True ) ] ]
                right_click_menu = [ [ '' ], [ 'Exit', ] ]
            else:
                top_elements = [ [ sg.Text( title, size = (20, 1), font = title_font,
                    justification = 'c', k = '-TITLE-' ) ] ]
                right_click_menu = [ [ '' ],
                                     [ 'Choose Title', 'Edit Me', 'New Theme', 'Save Location',
                                       'Refresh', 'Set Refresh Rate', 'Show Refresh Info',
                                       'Hide Refresh Info', 'Alpha',
                                       [ str( x ) for x in range( 1, 11 ) ], 'Exit', ] ]

            layout = top_elements + \
                     [ [ sg.Text( '0', size = main_info_size, font = main_info_font,
                         k = '-MAIN INFO-', justification = 'c', enable_events = test_window ) ],
                       [ sg.pin( sg.Text( size = (15, 2), font = refresh_font, k = '-REFRESHED-',
                           justification = 'c',
                           visible = sg.user_settings_get_entry( '-show refresh-', True ) ) ) ] ]

            # ------------------- Window Creation -------------------
            return sg.Window( 'Desktop Widget Template', layout, location = location,
                no_titlebar = True, grab_anywhere = True, margins = (0, 0),
                element_justification = 'c',
                element_padding = (0, 0),
                alpha_channel = sg.user_settings_get_entry( '-alpha-', ALPHA ), finalize = True,
                right_click_menu = right_click_menu, keep_on_top = True )

        def main( location ):
            """
            Where execution begins
            The Event Loop lives here, but the window creation is done in another function
            This is an important design pattern

            :param location: Location to create the main window if one is not found in the user
            settings
            :type location: Tuple[int, int]
            """

            window = make_window( sg.user_settings_get_entry( '-location-', location ) )

            refresh_frequency = sg.user_settings_get_entry( '-fresh frequency-',
                UPDATE_FREQUENCY_MILLISECONDS )

            while True:  # Event Loop
                # Normally a window.read goes here, but first we're updating the values in the
                # window, then reading it
                # First update the status text
                window[ '-MAIN INFO-' ].update( 'Your Info' )
                # for debugging show the last update date time
                window[ '-REFRESHED-' ].update(
                    datetime.datetime.now( ).strftime( "%m/%d/%Y\n%I:%M:%S %p" ) )

                # -------------- Start of normal event loop --------------
                event, values = window.read( timeout = refresh_frequency )
                print( event, values )
                if event in (sg.WIN_CLOSED, 'Exit'):  # standard exit test... ALWAYS do this
                    break
                if event == 'Edit Me':
                    sg.execute_editor( __file__ )
                elif event == 'Choose Title':
                    new_title = sg.popup_get_text( 'Choose a title for your Widget',
                        location = window.current_location( ), keep_on_top = True )
                    if new_title is not None:
                        window[ '-TITLE-' ].update( new_title )
                        sg.user_settings_set_entry( '-title-', new_title )
                elif event == 'Show Refresh Info':
                    window[ '-REFRESHED-' ].update( visible = True )
                    sg.user_settings_set_entry( '-show refresh-', True )
                elif event == 'Save Location':
                    sg.user_settings_set_entry( '-location-', window.current_location( ) )
                elif event == 'Hide Refresh Info':
                    window[ '-REFRESHED-' ].update( visible = False )
                    sg.user_settings_set_entry( '-show refresh-', False )
                elif event in [ str( x ) for x in range( 1, 11 ) ]:  # if Alpha Channel was chosen
                    window.set_alpha( int( event ) / 10 )
                    sg.user_settings_set_entry( '-alpha-', int( event ) / 10 )
                elif event == 'Set Refresh Rate':
                    choice = sg.popup_get_text(
                        'How frequently to update window in seconds? (can be a float)',
                        default_text = sg.user_settings_get_entry( '-fresh frequency-',
                            UPDATE_FREQUENCY_MILLISECONDS ) / 1000,
                        location = window.current_location( ), keep_on_top = True )
                    if choice is not None:
                        try:
                            refresh_frequency = float( choice ) * 1000  # convert to milliseconds
                            sg.user_settings_set_entry( '-fresh frequency-',
                                float( refresh_frequency ) )
                        except Exception as e:
                            sg.popup_error( f'You entered an incorrect number of seconds: {choice}',
                                f'Error: {e}', location = window.current_location( ),
                                keep_on_top = True )
                elif event == 'New Theme':
                    loc = window.current_location( )
                    if choose_theme( window.current_location( ), window.size ) is not None:
                        window.close( )  # out with the old...
                        window = make_window( loc )  # in with the new

            window.close( )

        if __name__ == '__main__':
            # To start the window at a specific location, get this location on the command line
            # The location should be in form x,y with no spaces
            location = (None, None)  # assume no location provided
            if len( sys.argv ) > 1:
                location = sys.argv[ 1 ].split( ',' )
                location = (int( location[ 0 ] ), int( location[ 1 ] ))
            main( location )


# ListDialog( data )
class ListDialog( Sith ):
    '''List search and selection'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __selecteditem = None
    __items = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def selecteditem( self ):
        if isinstance( self.__selecteditem, str ) and self.__selecteditem != '':
            return self.__selecteditem

    @selecteditem.setter
    def selecteditem( self, value ):
        if isinstance( value, str ) and value != '':
            self.__selecteditem = value

    @property
    def items( self ):
        if isinstance( self.__items, list ):
            return self.__items

    @selecteditem.setter
    def items( self, value ):
        if isinstance( value, list ):
            self.__items = value

    def __init__( self, data ):
        self.__items = data if isinstance( data, list ) else None
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 200, 225 )

    def show( self ):
        __btnsize = ( 10, 1 )

        names = [ src for src in list( self.__items ) if src != 'NS' ]
        layout = [ [ sg.Text( 'Search:', size = ( 25, 1 )  ) ],
                   [ sg.Input( size = ( 25, 1 ), enable_events = True, key = '-INPUT-' ) ],
                   [ sg.Text( r'', size = (100, 1) ) ],
                   [ sg.Listbox( names, size = ( 25, 5 ), enable_events = True, key = '-LIST-', font = self.__themefont ) ],
                   [ sg.Text( r'', size = (100, 1) ) ],
                   [ sg.Button( 'Select', size = __btnsize ), sg.Button( 'Exit', size = __btnsize  ) ] ]

        window = sg.Window( '', layout,
            size = self.__formsize,
            font = self.__themefont,
            icon = self.__icon )
        
        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, 'Exit' ):  # always check for closed window
                break
            if values[ '-INPUT-' ] != '':  # if a keystroke entered in search field
                search = values[ '-INPUT-' ]
                new_values = [ x for x in names if search in x ]  # do the filtering
                window[ '-LIST-' ].update( new_values )  # display in the listbox
            else:
                window[ '-LIST-' ].update( names )
            if event == '-LIST-' and len( values[ '-LIST-' ] ):
                sg.popup( 'Selected', values[ '-LIST-' ],
                    font = self.__themefont,
                    icon = self.__icon  )

        window.close( )


class ColorDialog( Sith ):
    '''class provides a form to select colors returning string values'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __text = None

    @property
    def text( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    @text.setter
    def text( self, value ):
        if isinstance( value, str ) and value != '':
            self.__text = value

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 400, 200 )


class Dashboard( Sith ):
    '''class defining basic dashboard for the application'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None
    __title = None
    __header = None

    @property
    def title( self ):
        if isinstance( self.__title, str ) and self.__title != '':
            return self.__title

    @title.setter
    def title( self, value ):
        if isinstance( value, str ) and value != '':
            self.__title = value

    @property
    def header( self ):
        if isin( self.__header, str ) and self.__header != '':
            return self.__header

    @header.setter
    def header( self, value ):
        if isinstance( value, str ) and value != '':
            self.__header = value

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 960, 450 )

    def show( self ):
        BORDER_COLOR = '#22262E'
        DARK_HEADER_COLOR = self.__buttoncolor
        BPAD_TOP = ( ( 20,20 ), ( 20, 10 ) )
        BPAD_LEFT = ( ( 20,10 ), ( 0, 0 ) )
        BPAD_LEFT_INSIDE = ( 0, ( 10, 0 ) )
        BPAD_RIGHT = ( ( 10,20 ), ( 10, 0 ) )

        theme_dict = { 'BACKGROUND': self.__elementbackcolor,
                        'TEXT': self.__themetextcolor,
                        'INPUT': self.__inputbackcolor,
                        'TEXT_INPUT': self.__inputforecolor,
                        'SCROLL': self.__buttoncolor,
                        'BUTTON': self.__buttoncolor,
                        'PROGRESS': ( 'Blue', '#C7D5E0' ),
                        'BORDER': 0,
                        'SLIDER_DEPTH': 0,
                        'PROGRESS_DEPTH': 0 }

        sg.theme_add_new( 'Dashboard', theme_dict )
        sg.theme( 'Dashboard' )

        top_banner = [
                [sg.Text('Budget Execution', font='Any 20', background_color = DARK_HEADER_COLOR, enable_events=True, grab=False), sg.Push(background_color=DARK_HEADER_COLOR),
                 sg.Text( 'Wednesday 27 Oct 2021', font='Any 20', background_color = DARK_HEADER_COLOR ) ],
        ]

        top  = [[sg.Push(), sg.Text('Weather Could Go Here', font='Any 20'), sg.Push()],
                [sg.T('This Frame has a relief while the others do not')],
                [sg.T('This window is resizable (see that sizegrip in the bottom right?)')]]

        block_3 = [ [ sg.Text( 'Block 3', font='Any 20' ) ],
                    [ sg.Input( ), sg.Text( 'Some Text' ) ],
                    [ sg.T( 'This frame has element_justification="c"' ) ],
                    [ sg.Button('Go', button_color = self.__buttoncolor, size = ( 10, 1 ) ),
                      sg.Button( 'Exit', button_color = self.__buttoncolor, size = ( 10, 1 ) ) ]  ]


        block_2 = [ [ sg.Text( 'Block 2', font='Any 20' ) ],
                    [ sg.T( 'This is some random text' ) ],
                    [ sg.Image( data=sg.DEFAULT_BASE64_ICON, enable_events=True ) ] ]

        block_4 = [ [ sg.Text('Block 4', font='Any 20')],
                    [ sg.T('You can move the window by grabbing this block (and the top banner)')],
                    [ sg.T('This block is a Column Element')],
                    [ sg.T('The others are all frames')],
                    [ sg.T('The Frame Element, with a border_width=0\n    and no title is just like a Column')],
                    [ sg.T('Frames that have a fixed size \n    handle element_justification better than Columns')]]


        layout = [
            [ sg.Frame('', top_banner,   pad=( 0, 0 ), background_color = DARK_HEADER_COLOR,  expand_x = True, border_width = 0, grab = True)],
            [ sg.Frame('', top, size = ( 920, 100 ), pad = BPAD_TOP,  expand_x = True,  relief = sg.RELIEF_GROOVE, border_width = 3 ) ],
             [ sg.Frame('', [ [ sg.Frame( '', block_2, size = ( 450, 150), pad = BPAD_LEFT_INSIDE, border_width = 0, expand_x = True, expand_y = True, ) ],
                           [ sg.Frame('', block_3, size = ( 450, 150 ),  pad = BPAD_LEFT_INSIDE, border_width = 0, expand_x = True, expand_y = True, element_justification = 'c' ) ] ],
                pad=BPAD_LEFT, background_color = BORDER_COLOR, border_width = 0, expand_x = True, expand_y = True),
             sg.Column( block_4, size = ( 450, 320 ), pad = BPAD_RIGHT,  expand_x = True, expand_y = True, grab = True ), ],[ sg.Sizegrip( background_color = BORDER_COLOR ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            margins = ( 0,0 ),
            background_color = BORDER_COLOR,
            no_titlebar = True,
            resizable = True,
            right_click_menu = sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT )

        while True:
            event, values = window.read( )
            print( event, values )
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            elif event == 'Edit Me':
                sg.execute_editor( __file__ )
            elif event == 'Version':
                sg.popup_scrolled( sg.get_versions( ), keep_on_top=True )
            elif event == 'File Location':
                sg.popup_scrolled( 'This Python file is:', __file__ )
        window.close( )


class ChartPanel( Sith ):
    ''' Provides form with a bar chart '''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def header( self ):
        if isin( self.__header, str ) and self.__header != '':
            return self.__header

    @header.setter
    def header( self, value ):
        if isinstance( value, str ) and value != '':
            self.__header = value

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( Sith, self ).__init__()
        self.__themefont = Sith( ).themefont
        self.__icon = Sith( ).iconpath
        self.__elementbackcolor = Sith( ).elementbackcolor
        self.__elementforecolor = Sith( ).elementforecolor
        self.__themetextcolor = Sith( ).textforecolor
        self.__textbackcolor = Sith( ).textbackcolor
        self.__inputbackcolor = Sith( ).inputbackcolor
        self.__inputforecolor = Sith( ).inputforecolor
        self.__buttoncolor = Sith( ).buttoncolor
        self.__formsize = ( 700, 600 )

    def show( self ):
        __btnsize = ( 15, 1 )
        BAR_WIDTH = 50
        BAR_SPACING = 75
        EDGE_OFFSET = 3
        GRAPH_SIZE = DATA_SIZE = ( 600, 500 )

        layout = [ [ sg.Text( '', size = ( 10, 1 ) ), sg.Text( '', size = ( 100, 1 ) ) ],
                   [ sg.Text( '', size = ( 10, 1 ) ), sg.Graph( GRAPH_SIZE, ( 0,0 ), DATA_SIZE, k='-GRAPH-', pad = 3 ) ],
                   [ sg.Text( '', size = ( 10, 1 ) ), sg.Text( '', size = ( 100, 1 ) ) ],
                   [ sg.Text( '', size = ( 20, 1 ) ), sg.Button( 'Next', size = __btnsize ),
                     sg.Text( '', size = ( 20, 1 ) ), sg.Exit( size = __btnsize ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            finalize = True,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize,
            resizable = True )

        graph = window[ '-GRAPH-' ]

        while True:
            graph.erase( )
            for i in range( 7 ):
                graph_value = random.randint( 0, GRAPH_SIZE[ 1 ] )
                graph.draw_rectangle( top_left = ( i * BAR_SPACING + EDGE_OFFSET, graph_value ),
                    bottom_right = (i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0 ),
                    fill_color = self.__buttoncolor )

                graph.draw_text( text = graph_value, color = self.__themetextcolor,
                    location = ( i * BAR_SPACING + EDGE_OFFSET + 25, graph_value + 10 ) )

            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, 'Exit' ):
                break

        window.close( )