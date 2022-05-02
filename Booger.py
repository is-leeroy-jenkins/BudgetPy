from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
from sys import exit
import Static
from Ninja import *
from Static import *
import fitz
import textwrap
import datetime


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


class FileDialog( ):
    '''class that renames a file'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#163754' )
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
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#163754' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\folder_browse.ico'
        __font = 'Roboto 9'
        __size = ( 450, 200 )

        layout = [ [ sg.Text( r'' ) ],
                   [ sg.Text( 'Search for Directory' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Input( ), sg.FolderBrowse( size = ( 15, 1 ) ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.OK( size = ( 8, 1 ) ), sg.Cancel( size = ( 10, 1 ) ) ] ]

        window = sg.Window( 'Budget Execution', layout,
            font = __font,
            icon = __icon,
            size = __size,
            titlebar_background_color = '#0F0F0F' )

        event, values = window.read( )
        window.close( )


# Message( text )
class Message( ):
    ''' class that provides form to display informational messages '''
    __text = None

    @property
    def text( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    @text.setter
    def text( self, value ):
        if isinstance( value, str ) and value != '':
            self.__text = value

    def __init__( self, text ):
        self.__text = text if isinstance( text, str ) and text != '' else None

    def __str__( self ):
        if isinstance( self.__text, str ):
            return self.__text

    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#163754' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\notification.ico'
        __font = 'Roboto 9'
        __size = ( 500, 250 )
        layout = [ [ sg.Text( r'' ) ],
                   [ sg.Text( self.__text, font = 'Roboto 10', text_color = '#FF0820' ) ],
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


# Error( exception )
class Error( ):
    '''class that displays error message'''
    __cause = None
    __method = None
    __message = None
    __exception = None

    @property
    def message( self ):
        if isinstance( self.__message, str ) and self.__message != '':
            return self.__message

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__message = value

    def __init__( self, exception = None ):
        self.__exception = exception if isinstance( exception, BudgetException ) else None
        self.__message = self.__exception.message
        self.__cause = self.__exception.cause
        self.__method = self.__exception.method

    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#163754' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\error.ico'
        __font = 'Roboto 9'
        __size = ( 500, 250 )
        layout = [ [ sg.Text( r'' ) ],
                   [ sg.Text( self.__message, font = 'Roboto 10', text_color = '#FF0820' ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Text( 'Source:', size = ( 10, 1 ) ), sg.Text( self.__cause, key = '-SRC-', size = ( 150, 1 )  ) ],
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


class Input( ):
    '''class that produces a contact input form'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#163754' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\question.ico'
        __font = 'Roboto 9'
        __size = ( 450, 200 )

        layout =  [ [ sg.Text( r'' ) ],
                    [ sg.Text( r'Please enter your input...' ) ],
                    [ sg.Text( r'' ) ],
                    [ sg.Text( 'Input', size = ( 10, 2 ) ), sg.InputText( '1', key = '-INPUT-' ) ],
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
            text_color = r'#B0C4DE',
            font = __font,
            icon = __icon )
        if event == sg.WIN_X_EVENT or event == sg.WIN_CLOSED:
            window.close( )


class ContactForm( ):
    '''class that produces a contact input form'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#163754' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\contact.ico'
        __font = 'Roboto 9'
        __size = ( 400, 250 )
        layout =  [ [ sg.Text( r'' ) ],
                    [ sg.Text( r'Please enter your Name, Address, Phone' ) ],
                    [ sg.Text( r'' ) ],
                    [ sg.Text( 'Name', size = ( 15, 1 ) ), sg.InputText( '1', key = '-NAME-' ) ],
                    [ sg.Text( 'Address', size = ( 15, 1 ) ), sg.InputText( '2', key = '-ADDRESS-' ) ],
                    [ sg.Text( 'Phone', size = ( 15, 1 ) ), sg.InputText( '3', key = '-PHONE-' ) ],
                    [ sg.Text( r'' ) ],
                    [ sg.Text( r'' ) ],
                   [ sg.Submit( size = ( 8, 1 ) ), sg.Cancel( size = ( 10, 1 ) ) ] ]
        window = sg.Window( 'Budget Contact Form', layout,
            font = __font,
            icon = __icon,
            size = __size )
        event, values = window.read( )
        sg.popup( event, values, values[ '-NAME-' ],
            values[ '-ADDRESS-' ],
            values[ '-PHONE-' ],
            text_color = r'#B0C4DE',
            font = __font,
            icon = __icon )
        if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
            window.close( )


class GridForm( ):
    '''object providing form that simulates a datagrid '''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#163754' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        __font = 'Roboto 9'
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
            font = ( 'Bodoni MT', 40 ) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]
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
            font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]
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
            font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]
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


class Notification( ):
    '''Class provides splash notification behaviors'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#163754' )

        USE_FADE_IN = True
        WIN_MARGIN = 60
        WIN_COLOR = '#282828'
        TEXT_COLOR = '#ffffff'
        DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS = 10000

        # Base64 Images to use as icons in the window
        img_error = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U' \
                    b'/gAAAACXBIWXMAAADlAAAA5QGP5Zs8AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm' \
                    b'+48GgAAAIpQTFRF////20lt30Bg30pg4FJc409g4FBe4E9f4U9f4U9g4U9f4E9g31Bf4E9f4E9f4E9f4E9f4E9f4FFh4Vdm4lhn42Bv5GNx5W575nJ/6HqH6HyI6YCM6YGM6YGN6oaR8Kev9MPI9cbM9snO9s3R+Nfb+dzg+d/i++vt/O7v/fb3/vj5//z8//7+////KofnuQAAABF0Uk5TAAcIGBktSYSXmMHI2uPy8/XVqDFbAAAA8UlEQVQ4y4VT15LCMBBTQkgPYem9d9D//x4P2I7vILN68kj2WtsAhyDO8rKuyzyLA3wjSnvi0Eujf3KY9OUP+kno651CvlB0Gr1byQ9UXff+py5SmRhhIS0oPj4SaUUCAJHxP9+tLb/ezU0uEYDUsCc+l5/T8smTIVMgsPXZkvepiMj0Tm5txQLENu7gSF7HIuMreRxYNkbmHI0u5Hk4PJOXkSMz5I3nyY08HMjbpOFylF5WswdJPmYeVaL28968yNfGZ2r9gvqFalJNUy2UWmq1Wa7di/3Kxl3tF1671YHRR04dWn3s9cXRV09f3vb1fwPD7z9j1WgeRgAAAABJRU5ErkJggg=='
        img_success = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U' \
                      b'/gAAAACXBIWXMAAAEKAAABCgEWpLzLAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm' \
                      b'+48GgAAAHJQTFRF////ZsxmbbZJYL9gZrtVar9VZsJcbMRYaMZVasFYaL9XbMFbasRZaMFZacRXa8NYasFaasJaasFZasJaasNZasNYasJYasJZasJZasJZasJZasJZasJYasJZasJZasJZasJZasJaasJZasJZasJZasJZ2IAizQAAACV0Uk5TAAUHCA8YGRobHSwtPEJJUVtghJeYrbDByNjZ2tvj6vLz9fb3/CyrN0oAAADnSURBVDjLjZPbWoUgFIQnbNPBIgNKiwwo5v1fsQvMvUXI5oqPf4DFOgCrhLKjC8GNVgnsJY3nKm9kgTsduVHU3SU/TdxpOp15P7OiuV/PVzk5L3d0ExuachyaTWkAkLFtiBKAqZHPh/yuAYSv8R7XE0l6AVXnwBNJUsE2+GMOzWL8k3OEW7a/q5wOIS9e7t5qnGExvF5Bvlc4w/LEM4Abt+d0S5BpAHD7seMcf7+ZHfclp10TlYZc2y2nOqc6OwruxUWx0rDjNJtyp6HkUW4bJn0VWdf/a7nDpj1u++PBOR694+Ftj/8PKNdnDLn/V8YAAAAASUVORK5CYII='

        # -------------------------------------------------------------------
        def display_notification( title, message, icon,
                                  display_duration_in_ms = DEFAULT_DISPLAY_DURATION_IN_MILLISECONDS,
                                  use_fade_in = True, alpha = 0.9, location = None ):
            """
            Function that will create, fade in and out, a small window that displays a message with
            an icon
            The graphic design is similar to other system/program notification windows seen in
            Windows / Linux
            :param title: (str) Title displayed at top of notification
            :param message: (str) Main body of the notification
            :param icon: (str) Base64 icon to use. 2 are supplied by default
            :param display_duration_in_ms: (int) duration for the window to be shown
            :param use_fade_in: (bool) if True, the window will fade in and fade out
            :param alpha: (float) Amount of Alpha Channel to use.  0 = invisible, 1 = fully visible
            :param location: Tuple[int, int] location of the upper left corner of window. Default is
            lower right corner of screen
            """

            # Compute location and size of the window
            message = textwrap.fill( message, 50 )
            win_msg_lines = message.count( '\n' ) + 1

            screen_res_x, screen_res_y = sg.Window.get_screen_size( )
            win_margin = WIN_MARGIN  # distance from screen edges
            win_width, win_height = 364, 66 + (14.8 * win_msg_lines)
            win_location = location if location is not None else (
            screen_res_x - win_width - win_margin, screen_res_y - win_height - win_margin)

            layout = [ [ sg.Graph( canvas_size = (win_width, win_height),
                graph_bottom_left = (0, win_height), graph_top_right = (win_width, 0), key = '-GRAPH-',
                background_color = WIN_COLOR, enable_events = True ) ] ]

            window = sg.Window( title, layout, background_color = WIN_COLOR, no_titlebar = True,
                location = win_location, keep_on_top = True, alpha_channel = 0, margins = (0, 0),
                element_padding = (0, 0),
                finalize = True )

            window[ '-GRAPH-' ].draw_rectangle( (win_width, win_height), (-win_width, -win_height),
                fill_color = WIN_COLOR, line_color = WIN_COLOR )
            window[ '-GRAPH-' ].draw_image( data = icon, location = (20, 20) )
            window[ '-GRAPH-' ].draw_text( title, location = (64, 20), color = TEXT_COLOR,
                font = ('Arial', 12, 'bold'), text_location = sg.TEXT_LOCATION_TOP_LEFT )
            window[ '-GRAPH-' ].draw_text( message, location = (64, 44), color = TEXT_COLOR,
                font = ('Arial', 9), text_location = sg.TEXT_LOCATION_TOP_LEFT )

            # change the cursor into a 'hand' when hovering over the window to give user hint that
            # clicking does something
            window[ '-GRAPH-' ].set_cursor( 'hand2' )

            if use_fade_in == True:
                for i in range( 1, int( alpha * 100 ) ):  # fade in
                    window.set_alpha( i / 100 )
                    event, values = window.read( timeout = 20 )
                    if event != sg.TIMEOUT_KEY:
                        window.set_alpha( 1 )
                        break
                event, values = window( timeout = display_duration_in_ms )
                if event == sg.TIMEOUT_KEY:
                    for i in range( int( alpha * 100 ), 1, -1 ):  # fade out
                        window.set_alpha( i / 100 )
                        event, values = window.read( timeout = 20 )
                        if event != sg.TIMEOUT_KEY:
                            break
            else:
                window.set_alpha( alpha )
                event, values = window( timeout = display_duration_in_ms )

            window.close( )

        if __name__ == '__main__':
            title = 'Action completed successfully'
            message = 'This message is intended to inform you that the action you have performed has been successful. There is no need for further action.'
            display_notification( title, message, img_success, 10000, use_fade_in = True )


class PdfViewer( ):
    '''Creates form to view a PDF'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#163754' )
        filename = sg.popup_get_file( 'Budget Execution PDF Browser', 'PDF file to open', file_types = ( ( 'PDF Files', '*.pdf' ), ) )
        if filename is None:
            sg.popup_cancel( 'Cancelling' )
            exit( 0 )
        document = fitz.open( filename )
        pages = len( document )
        tablist = [ None ] * pages
        title = f'Budget Execution display of { filename }, pages: { pages }'

        def get_page( pno, zoom = 0 ):
            displaylist = tablist[ pno ]
            if not displaylist:
                tablist[ pno ] = document[ pno ].getDisplayList( )
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
                pix = displaylist.getPixmap( alpha = False )
            else:
                pix = displaylist.getPixmap( alpha = False, matrix = mat, clip = clip )
            return pix.getPNGData( )

        currentpage = 0
        data = get_page( currentpage )
        image_elem = sg.Image( data = data )
        goto = sg.InputText( str( currentpage + 1 ), size = (5, 1) )
        layout = [ [ sg.Button( 'Prev' ), sg.Button( 'Next' ), sg.Text( 'Page:' ), goto, ],
                   [ sg.Text( 'Zoom:' ), sg.Button( 'Top-L' ), sg.Button( 'Top-R' ), sg.Button( 'Bot-L' ),  sg.Button( 'Bot-R' ), ],
                   [ image_elem ],  ]
        pdfkeys = ('Next', 'Next:34', 'Prev', 'Prior:33', 'Top-L', 'Top-R', 'Bot-L', 'Bot-R', 'MouseWheel:Down', 'MouseWheel:Up')
        zoombuttons = ('Top-L', 'Top-R', 'Bot-L', 'Bot-R')
        window = sg.Window( title, layout, return_keyboard_events = True, use_default_focus = False )
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


class CalendarDialog( ):
    '''class creates form providing date selection behavior'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#34353B' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        __font = 'Roboto 9'
        __window = ( 400, 225 )
        __button = ( 10, 1 )
        __calendar = ( 100, 100 )

        layout = [ [ sg.Text( r'', size = ( 100, 1 )  ) ],
                   [ sg.Text( 'Choose Date', key = '-TXT-' ) ],
                   [ sg.Input( key = '-IN-', size = ( 20, 1 ) ),
                     sg.CalendarButton( 'US No Buttons Location (0,0)',
                         close_when_date_chosen = True, target = '-IN-', location = ( 0, 0 ),
                         no_titlebar = False, font = __font ) ],
                   [ sg.Input( key = '-IN3-', size = ( 20, 1 ) ),
                     sg.CalendarButton( 'Monday', title = 'Pick date',
                         no_titlebar = True, close_when_date_chosen = False, target = '-IN3-',
                             begin_at_sunday_plus = 1, month_names = (
                             'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
                             'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ),
                         day_abbreviations = ( 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN' ) ) ],
                   [ sg.Input( key = '-IN2-', size = ( 20, 1 ) ),
                     sg.CalendarButton( 'German Feb 2020', target = '-IN2-',
                         default_date_m_d_y = ( 2, None, 2020 ), locale = 'de_DE',
                         begin_at_sunday_plus = 1 ) ],
                   [ sg.Input( key = '-IN4-', size = ( 20, 1 ) ),
                     sg.CalendarButton( 'Format %Y-%m-%d Jan 2020', target = '-IN4-',
                         format = '%Y-%m-%d', default_date_m_d_y = ( 1, None, 2020 ), ) ],
                   [ sg.Text( r'', size = ( 100, 1 )  ) ],
                   [ sg.Button( 'Read', size = __button ), sg.Button( 'Date Picker', size = __button ), sg.Exit( size = __button ) ] ]

        window = sg.Window( 'Budget Calendar', layout,
            font = __font, icon = __icon, size = __window )

        while True:
            event, values = window.read( )
            print( event, values )
            if event in ( sg.WIN_CLOSED, 'Exit' ):
                break
            elif event == 'Date Picker':
                sg.popup( 'Choose Date', sg.popup_get_date( ),
                    icon = __icon, font = __font, size = __calendar )
        window.close( )


class DateWidget( ):
    ''' Desktop widget displaying date time information'''
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
            # to display theme info
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
                # First update the status information
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


class DataSelector( ):
    '''List search and selection'''
    def show( self ):
        sg.theme_background_color( '#0F0F0F' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_element_text_color( '#D3D3D3' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_text_element_background_color('#0F0F0F' )
        sg.theme_input_background_color( '#282828' )
        sg.theme_text_color( '#B0C4DE' )
        sg.theme_button_color( '#34353B' )
        __icon = r'C:\Users\terry\source\repos\BudgetPy\etc\ico\ninja.ico'
        __font = 'Roboto 9'
        __window = ( 200, 225 )
        __button = ( 10, 1 )
        __calendar = ( 100, 100 )

        names = [ src.name for src in list( Source ) ]
        layout = [ [ sg.Text( 'Search:', size = ( 25, 1 )  ) ],
                   [ sg.Input( size = ( 25, 1 ), enable_events = True, key = '-INPUT-' ) ],
                   [ sg.Text( r'', size = (100, 1) ) ],
                   [ sg.Listbox( names, size = ( 25, 5 ), enable_events = True, key = '-LIST-', font = __font ) ],
                   [ sg.Text( r'', size = (100, 1) ) ],
                   [ sg.Button( 'Select', size = __button ), sg.Button( 'Exit', size = __button  ) ] ]

        window = sg.Window( '', layout,
            size = __window, font = __font, icon = __icon )
        # Event Loop
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
                sg.popup( 'Selected ', values[ '-LIST-' ],
                    size = __window, font = __font, icon = __icon  )

        window.close( )
