from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
from sys import exit
from Ninja import *
from Static import *
import textwrap


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
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#0F0F0F' )
        sg.theme_text_color( '#ADDFF7' )
        sg.theme_element_background_color( '#0F0F0F' )
        sg.theme_text_element_background_color( '#0F0F0F' )
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
        sg.theme_element_text_color( '#ADDFF7' )
        sg.theme_input_background_color( '#282828' )
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
            text_color = r'#ADDFF7',
            font = __font,
            icon = __icon )
        if event == sg.WIN_X_EVENT or event == sg.WIN_CLOSED:
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


class Notification( ):
    '''Class provides splash notification behaviors'''
    USE_FADE_IN = True
    WIN_MARGIN = 60
    WIN_COLOR = "#282828"
    TEXT_COLOR = "#ffffff"
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
        win_msg_lines = message.count( "\n" ) + 1

        screen_res_x, screen_res_y = sg.Window.get_screen_size( )
        win_margin = WIN_MARGIN  # distance from screen edges
        win_width, win_height = 364, 66 + (14.8 * win_msg_lines)
        win_location = location if location is not None else (
        screen_res_x - win_width - win_margin, screen_res_y - win_height - win_margin)

        layout = [ [ sg.Graph( canvas_size = (win_width, win_height),
            graph_bottom_left = (0, win_height), graph_top_right = (win_width, 0), key = "-GRAPH-",
            background_color = WIN_COLOR, enable_events = True ) ] ]

        window = sg.Window( title, layout, background_color = WIN_COLOR, no_titlebar = True,
            location = win_location, keep_on_top = True, alpha_channel = 0, margins = (0, 0),
            element_padding = (0, 0),
            finalize = True )

        window[ "-GRAPH-" ].draw_rectangle( (win_width, win_height), (-win_width, -win_height),
            fill_color = WIN_COLOR, line_color = WIN_COLOR )
        window[ "-GRAPH-" ].draw_image( data = icon, location = (20, 20) )
        window[ "-GRAPH-" ].draw_text( title, location = (64, 20), color = TEXT_COLOR,
            font = ("Arial", 12, "bold"), text_location = sg.TEXT_LOCATION_TOP_LEFT )
        window[ "-GRAPH-" ].draw_text( message, location = (64, 44), color = TEXT_COLOR,
            font = ("Arial", 9), text_location = sg.TEXT_LOCATION_TOP_LEFT )

        # change the cursor into a "hand" when hovering over the window to give user hint that
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
        title = "Action completed successfully"
        message = "This message is intended to inform you that the action you have performed has been successful. There is no need for further action."
        display_notification( title, message, img_success, 10000, use_fade_in = True )