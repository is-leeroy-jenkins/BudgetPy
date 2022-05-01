from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
from sys import exit
from Ninja import *
from Static import *


class ButtonIcon( ):
    '''class representing form images'''
    __button = None
    __toolbar = None
    __rpio = None
    __boc = None
    __navigation = None
    __database = None
    __epa = None
    __loaders = None
    __ninja = None
    __signature = None
    __name = None

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
        if isinstance( value, IMG ):
            self.__name = value.name

    def __init__( self, img ):
        self.__name = img.name if isinstance( img, IMG ) else None
        self.__button = r'C:\Users\terry\source\repos\BudgetPy\etc\img\button'


class FileDialog( ):
    '''class that renames a file'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_input_text_color( '#ADDFF7' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\file_browse.ico'
        __font = 'Roboto 9'
        __size = ( 450, 200 )
        layout = [ [ sg.Text( r'' ) ],
                   [ sg.Text( 'Search for File' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Input( ), sg.FileBrowse( size = ( 15, 1 ) ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.OK( size = ( 8, 1 ) ), sg.Cancel( size = ( 10, 1 )  ) ] ]
        window = sg.Window( 'Budget Execution', layout,
            font = __font,
            icon = __icon,
            size = __size,
            titlebar_background_color = '#0F0F0F' )
        event, values = window.read( )
        window.close( )


class FolderDialog( ):
    '''class that renames a folder'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_input_text_color( '#ADDFF7' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\folder_browse.ico'
        __font = 'Roboto 9'
        __size = ( 450, 200 )
        layout = [ [ sg.Text( r'' ) ],
                   [ sg.Text( 'Search for Directory' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Input( ), sg.FolderBrowse( size = ( 15, 1 ) ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.OK( size = ( 8, 1 ) ), sg.Cancel( size = ( 10, 1 )  ) ] ]
        window = sg.Window( 'Budget Execution', layout,
            font = __font,
            icon = __icon,
            size = __size,
            titlebar_background_color = '#0F0F0F' )
        event, values = window.read( )
        window.close( )


class MessageDialog( ):
    ''' class that provides form to display informational messages '''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\notification.ico'
        __font = 'Roboto 9'
        __size = ( 500, 250 )
        layout = [ [ sg.Text( r'' ) ],
                   [ sg.Text( r'This is message text', font = 'Roboto 10', text_color = '#FF0820' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Text( 'Message line 1....', key = '-FIRST-' ) ],
                   [ sg.Text( 'Message line 2', key = '-SECOND-' ) ],
                   [ sg.Text( 'Message line 3', key = '-THIRD-' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Text( r'' ) ] ]
        window = sg.Window( r'  Budget Execution', layout,
            icon = __icon,
            font = __font,
            size = __size,
            titlebar_background_color = '#0F0F0F' )
        event, values = window.read( )
        sg.popup( 'Budget Message', event, values, values[ '-FIRST-' ],
            values[ '-SECOND-' ],
            values[ '-THIRD-' ],
            text_color = r'#ADDFF7',
            font = __font,
            icon = __icon )
        if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
            window.close( )


class ErrorDialog( ):
    '''class that displays error message'''
    __cause = None
    __method = None
    __message = None
    __error = None

    @property
    def message( self ):
        if isinstance( self.__message, str ) and self.__message != '':
            return self.__message

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__message = value

    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\error.ico'
        __font = 'Roboto 9'
        __size = ( 500, 250 )
        layout = [ [ sg.Text( r'' ) ],
                   [ sg.Text( self.__message, font = 'Roboto 10', text_color = '#FF0820' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Text( 'Cause:', size = ( 10, 1 ) ), sg.Text( self.__cause, key = '-SRC-', size = ( 150, 1 )  ) ],
                   [ sg.Text( 'Method:', size = ( 10, 1 ) ), sg.Text( self.__method, key = '-MTH-', size = ( 150, 1 )  ) ],
                   [ sg.Text( 'Message:', size = ( 10, 1 ) ), sg.Text( self.__message, key = '-MSG-', size = ( 150, 1 )  ) ],
                   [ sg.Text( r'', size = ( 1, 1 ) ) ],
                   [ sg.Text( r'', size = ( 1, 1 ) ) ] ]
        window = sg.Window( r'  Budget Execution', layout,
            icon = __icon,
            font = __font,
            size = __size,
            titlebar_background_color = '#0F0F0F' )
        event, values = window.read( )
        sg.popup( 'Budget Error', event, values, values[ '-SRC-' ],
            values[ '-MTH-' ],
            values[ '-MSG-' ],
            text_color = r'#ADDFF7',
            font = __font,
            icon = __icon )
        if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
            window.close( )

    def __init__( self, error = None ):
        self.__error = error if isinstance( error, Error ) else None
        self.__cause = error.cause if isinstance( error, Error ) else None
        self.__method = error.method if isinstance( error, Error ) else None
        self.__message = error.message if isinstance( error, Error ) else None


class Input( ):
    '''class that produces a contact input form'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_input_text_color( '#ADDFF7' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        sg.theme_input_text_color( '#ADDFF7' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\question.ico'
        __font = 'Roboto 9'
        __size = ( 450, 200 )
        layout =  [ [ sg.Text( r'' ) ],
                    [ sg.Text( r'Please enter your input...' ) ],
                    [ sg.Text( r'' ) ],
                    [ sg.Text( 'Input', size = ( 15, 2 ) ), sg.InputText( '1', key = '-INPUT-' ) ],
                    [ sg.Text( r'' ) ],
                    [ sg.Text( r'' ) ],
                   [ sg.Submit( size = ( 8, 1 ) ), sg.Cancel( size = ( 10, 1 ) ) ] ]
        window = sg.Window( ' Budget Input', layout,
            font = __font,
            icon = __icon,
            size = __size,
            titlebar_background_color = '#0F0F0F' )
        event, values = window.read( )
        sg.popup( event, values, values[ '-INPUT-' ],
            text_color = r'#ADDFF7',
            font = __font,
            icon = __icon )
        if event == sg.WIN_X_EVENT or event == sg.WIN_CLOSED or event == 'Cancel':
            window.close( )


class ContactForm( ):
    '''class that produces a contact input form'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        sg.theme_input_text_color( '#ADDFF7' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\contact.ico'
        __font = 'Roboto 8'
        __size = ( 400, 250 )
        layout =  [ [ sg.Text( r'' ) ],
                    [ sg.Text( r'Please enter your Name, Address, Phone' ) ],
                    [ sg.Text( r'' ) ],
                    [ sg.Text( 'Name', size = ( 15, 1 ) ), sg.InputText( '1', key = '-NAME-' ) ],
                    [ sg.Text( 'Address', size = ( 15, 1 ) ), sg.InputText( '2', key = '-ADDRESS-' ) ],
                    [ sg.Text( 'Phone', size = ( 15, 1 ) ), sg.InputText( '3', key = '-PHONE-' ) ],
                    [ sg.Text( r'' ) ],
                   [ sg.Submit( ), sg.Cancel( ) ] ]
        window = sg.Window( 'Budget Contact Form', layout,
            font = __font,
            icon = __icon,
            size = __size )
        event, values = window.read( )
        sg.popup( event, values, values[ '-NAME-' ],
            values[ '-ADDRESS-' ],
            values[ '-PHONE-' ],
            text_color = r'#ADDFF7',
            font = __font,
            icon = __icon )
        if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
            window.close( )


class GridForm( ):
    '''object providing form that simulates a datagrid '''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        __font = 'Roboto 8'
        __size = ( 17, 1 )
        headings = [ 'HEADER 1', 'HEADER 2', 'HEADER 3', 'HEADER 4' ]
        header = [ [ sg.Text( '  ' ) ] \
                   + [ sg.Text( h, size = ( 15, 1 ) ) for h in headings ] ]
        input_rows = [ [ sg.Input( size = __size, pad = ( 0, 0 ), font = __font ) for col in range( 4 ) ] for row in range( 10 ) ]
        layout = header + input_rows
        window = sg.Window( 'Budget Grid', layout,
            font = __font,
            icon = __icon )
        event, values = window.read( )
        if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
            window.close( )


class Loading( ):
    '''object providing form loading behavior '''

    def show( self ):
        gif_filename = r'C:\Users\terry\source\repos\BudgetPy\etc\img\loaders\loading.gif'
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ( "Bodoni MT", 40 ) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]
        window = sg.Window( 'Loading', layout,
            element_justification = 'c',
            margins = ( 0, 0 ),
            size = ( 600, 600 ),
            element_padding = ( 0, 0 ), finalize = True )
        window[ '-T-' ].expand( True, True, True )
        interframe_duration = ButtonIcon.open( gif_filename ).info[ 'duration' ]
        while True:
            for frame in ImageSequence.Iterator( ButtonIcon.open( gif_filename ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
            window.close()


class Waiting( ):
    '''object providing form loader behavior '''

    def show( self ):
        gif_filename = r'C:\Users\terry\source\repos\BudgetPy\etc\img\loaders\loader.gif'
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ("Bodoni MT", 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]
        window = sg.Window( 'Loading', layout,
            element_justification = 'c',
            margins = ( 0, 0 ),
            element_padding = ( 0, 0 ),
            size = ( 600, 600 ),
            finalize = True )
        window[ '-T-' ].expand( True, True, True )
        interframe_duration = ButtonIcon.open( gif_filename ).info[ 'duration' ]
        while True:
            for frame in ImageSequence.Iterator( ButtonIcon.open( gif_filename ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
            window.close()


class Processing( ):
    '''object providing form processing behavior '''

    def show( self ):
        gif_filename = r'C:\Users\terry\source\repos\BudgetPy\etc\img\loaders\processing.gif'
        layout = [ [ sg.Text( '',
            background_color = '#000000',
            text_color = '#FFF000',
            justification = 'c',
            key = '-T-',
            font = ("Bodoni MT", 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]
        window = sg.Window( 'Loading', layout,
            element_justification = 'c',
            margins = ( 0, 0 ),
            size = ( 600, 600 ),
            element_padding = ( 0, 0 ), finalize = True )
        window[ '-T-' ].expand( True, True, True )
        interframe_duration = ButtonIcon.open( gif_filename ).info[ 'duration' ]
        while True:
            for frame in ImageSequence.Iterator( ButtonIcon.open( gif_filename ) ):
                event, values = window.read( timeout = interframe_duration )
                if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
                    exit( 0 )
                window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
            window.close()
