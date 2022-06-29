from PIL import Image, ImageTk, ImageSequence, ImageGrab
import PySimpleGUI as sg
import fitz
import sys
import traceback
from sys import exit, exc_info
from datetime import datetime, date
import random
import io
import textwrap
from googlesearch import search
from Minion import *
import traceback
import textwrap
import numpy as np
from pandas import read_csv as CsvReader
from pandas import read_excel as ExcelReader
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.figure
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from matplotlib.ticker import NullFormatter
from mpl_toolkits.axes_grid1.axes_rgb import RGBAxes
from Static import EXT


# Error( heading = '' )
class Error( Exception ):
    '''Class wrapping exception data used as
    the input argument for ErrorDialog class'''
    __class = None
    __module = None
    __method = None
    __heading = None
    __type = None
    __trace = None
    __info = None

    @property
    def message( self ):
        '''Gets the general heading for the dialog'''
        if isinstance( self.__heading, str ) and self.__heading != '':
            return self.__heading

    @message.setter
    def message( self, value ):
        '''Sets the general heading for the dialog'''
        if isinstance( value, str ) and value != '':
            self.__heading = value

    @property
    def cause( self ):
        '''Gets string indicating the class generating the exception'''
        if isinstance( self.__class, str ) and self.__class != '':
            return self.__class

    @cause.setter
    def cause( self, value ):
        '''Sets the string indicating the class generating the exception'''
        if isinstance( value, str ) and value != '':
            self.__class = value

    @property
    def method( self ):
        '''Gets a string representing the method generating the exception'''
        if isinstance( self.__method, str ) and self.__method != '':
            return self.__method

    @method.setter
    def method( self, value ):
        '''Sets a string representing method generating the exception'''
        if isinstance( value, str ) and value != '':
            self.__method = value

    @property
    def module( self ):
        '''Gets a string representing module generating the exception'''
        if isinstance( self.__module, str ) and self.__module != '':
            return self.__module

    @module.setter
    def module( self, value ):
        '''Sets a string representing the module generating the exception'''
        if isinstance( value, str ) and value != '':
            self.__module = value

    @property
    def type( self ):
        '''sets the object type generating the exception'''
        if isinstance( self.__type, Exception ):
            return self.__type

    @type.setter
    def type( self, value ):
        '''sets the object type generating the exception'''
        if isinstance( value, Exception ):
            self.__type = value

    @property
    def stacktrace( self ):
        '''Gets string returned by the 'traceback.format_exc( ) method '''
        if isinstance( self.__trace, str ):
            return self.__trace

    @stacktrace.setter
    def stacktrace( self, value ):
        '''Sets string returned by the 'traceback.format_exc( ) method '''
        if isinstance( value, str ):
            self.__trace = value

    @property
    def info( self ):
        '''Gets string comprised of exc_info( )[ 0 ] and traceback.format_exc( ) '''
        if isinstance( self.__class, str ) and self.__class != '':
            return self.__class

    @info.setter
    def info( self, value ):
        '''Sets string comprised of exc_info( )[ 0 ] and traceback.format_exc( ) '''
        if isinstance( value, str ) and value != '':
            self.__class = value

    def __init__( self, heading = '', cause = '', method = '', module = '' ):
        super( ).__init__( )
        self.__heading = heading if isinstance( heading, str ) else '\t\tSomething unexpected happened!'
        self.__class = cause if isinstance( cause, str ) and cause != '' else None
        self.__method = method if isinstance( method, str ) and method != '' else None
        self.__module = module if isinstance( module, str ) and module != '' else None
        self.__type = exc_info( )[ 0 ]
        self.__trace = traceback.format_exc( )
        self.__info = str( exc_info( )[ 0 ] ) + ': \r\n \r\n' + traceback.format_exc( )

    def __str__( self ):
        if isinstance( self.__info, str ) and self__trace != '':
            return self.__info
        
            
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
        self.__button = os.getcwd( ) + r'\etc\img\button'
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
        self.__name = ico.name
        self.__folder = os.getcwd( ) + r'etc\ico'
        self.__filepath = self.__folder + r'\\' + self.__name + r'.ico'

    def __str__( self ):
        if isinstance( self.__filepath, str ):
            return self.__filepath


# ColorFormat(  )
class ColorFormat( ):
    '''Class providing color conversion methods
    given a color in hex format'''
    __rgb = None
    __hex = None
    __hsl = None
    __red = None
    __green = None
    __blue = None
    __input = None
    __output = None

    @property
    def red( self ):
        '''Property returning color tuple ( r, g, b ) '''
        if isinstance( self.__red, int ):
            return self.__red

    @red.setter
    def red( self, value ):
        if isinstance( value, int ):
            self.__red = value

    @property
    def green( self ):
        '''Property returning color tuple ( r, g, b ) '''
        if isinstance( self.__green, int ):
            return self.__green

    @green.setter
    def green( self, value ):
        if isinstance( value, int ):
            self.__green = value

    @property
    def blue( self ):
        '''Property returning color tuple ( r, g, b ) '''
        if isinstance( self.__blue, int ):
            return self.__blue

    @blue.setter
    def blue( self, value ):
        if isinstance( value, int ):
            self.__blue = value

    @property
    def rgb( self ):
        '''Property returning color tuple ( r, g, b ) '''
        if isinstance( self.__rgb, tuple ):
            return self.__rgb

    @rgb.setter
    def rgb( self, value ):
        if isinstance( value, tuple ):
            self.__rgb = value

    @property
    def hex( self ):
        '''Property returning color string '#rrggbb '''
        if isinstance( self.__hex, str ) and self.__hex.startswith( '#' ):
            return self.__hex

    @hex.setter
    def hex( self, value ):
        '''Property sets hex value of a color to a string '#rrggbb' '''
        if isinstance( value, str ) and value.startswith( '#' ):
            self.__hex = value

    def __init__( self ):
        self.__rgb = None
        self.__hex = None
        self.__hsl = None

    def hextohsl( self, hex ):
        '''Converts the string input argument 'hex' representing a
         hexidecimal color returing its equivalent 'hsl' value as a tuple'''
        self.__hex = hex
        r, g, b = hextorgb( hex )
        self.__red = r
        self.__green = g
        self.__blue = b
        hsl= rgbtohsl( r, g, b )
        return hsl

    def hextorgb( self, hex ):
        '''Converts the string input argument 'hex' representing a
         hexidecimal color into its equivalent 'rgb' value'''
        hex = hex.lstrip( '#' )
        hlen = len( hex )
        return tuple( int( hex[ i:i + hlen // 3 ], 16 ) for i in range( 0, hlen, hlen // 3 ) )

    def rgbtohsl( self, r, g, b ):
        '''Converts integer input arguments 'r, g, and b' representing
         an rgb color into its equivalent hsl color '''
        r = float( r )
        g = float( g )
        b = float( b )
        high = max( r, g, b )
        low = min( r, g, b )
        h, s, v = ((high + low) / 2,) * 3
        if high == low:
            h = s = 0.0
        else:
            d = high - low
            l = (high + low) / 2
            s = d / (2 - high - low) if l > 0.5 else d / (high + low)
            h = {
                    r: (g - b) / d + (6 if g < b else 0),
                    g: (b - r) / d + 2,
                    b: (r - g) / d + 4,
            }[ high ]
            h /= 6
        return h, s, v

    def hsltorgb( self, h, s, l ):
        def hue_to_rgb( p, q, t ):
            t += 1 if t < 0 else 0
            t -= 1 if t > 1 else 0
            if t < 1 / 6:
                return p + (q - p) * 6 * t
            if t < 1 / 2:
                return q
            if t < 2 / 3:
                p + (q - p) * (2 / 3 - t) * 6
            return p

        if s == 0:
            r, g, b = l, l, l
        else:
            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            r = hue_to_rgb( p, q, h + 1 / 3 )
            g = hue_to_rgb( p, q, h )
            b = hue_to_rgb( p, q, h - 1 / 3 )

        return r, g, b

    def hsvtohsl( self, h, s, v ):
        l = 0.5 * v * (2 - s)
        s = v * s / (1 - fabs( 2 * l - 1 ))
        return h, s, l

    def hsltohsv( self, h, s, l ):
        v = (2 * l + s * (1 - fabs( 2 * l - 1 ))) / 2
        s = 2 * (v - l) / v
        return h, s, v


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
    __buttonforecolor = None
    __buttonbackcolor = None
    __icon = None
    __themefont = None
    __scrollbarcolor = None
    __progressbarbackcolor = None
    __formsize = None
    __settingspath = None

    @property
    def size( self ):
        '''Gets the size proerty as a tuple'''
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        '''Sets the size property'''
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def settingspath( self ):
        '''Gets the size proerty as a tuple'''
        if isinstance( self.__settingspath, tuple ) :
            return self.__settingspath

    @settingspath.setter
    def settingspath( self, value ):
        '''Sets the size property'''
        if isinstance( value, tuple ) :
            self.__settingspath = value

    @property
    def themebackground( self ):
        if isinstance( self.__themebackground, str ) and self.__themebackground != '':
            return self.__themebackground

    @themebackground.setter
    def themebackground( self, value ):
        if isinstance( value, str ) and value != '':
            self.__themebackground = value

    @property
    def themetextcolor( self ):
        if isinstance( self.__themetextcolor, str ):
            return self.__themetextcolor

    @themetextcolor.setter
    def themetextcolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__themetextcolor = value

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
        if isinstance( self.__buttoncolor, tuple ):
            return self.__buttoncolor

    @buttoncolor.setter
    def buttoncolor( self, value ):
        if isinstance( value, tuple ):
            self.__buttoncolor = value

    @property
    def buttonbackcolor( self ):
        if isinstance( self.__buttonbackcolor, str ):
            return self.__buttonbackcolor

    @buttonbackcolor.setter
    def buttonbackcolor( self, value ):
        if isinstance( value, str ):
            self.__buttonbackcolor = value

    @property
    def buttonforecolor( self ):
        if isinstance( self.__buttonforecolor, str ):
            return self.__buttonforecolor

    @buttonforecolor.setter
    def buttonforecolor( self, value ):
        if isinstance( value, str ):
            self.__buttonforecolor = value

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

    @property
    def scrollbarcolor( self ):
        if isinstance( self.__scrollbarcolor, str ) and self.__scrollbarcolor != '':
            return self.__scrollbarcolor

    @scrollbarcolor.setter
    def scrollbarcolor( self, value ):
        if isinstance( value, str ) and value != '':
            self.__scrollbarcolor = value

    @property
    def progressbarcolor( self ):
        if isinstance( self.__progressbarcolor, tuple ) :
            return self.__progressbarcolor

    @progressbarcolor.setter
    def progressbarcolor( self, value ):
        if isinstance( value, tuple ) :
            self.__progressbarcolor = value

    def __init__( self ):
        sg.theme( 'DarkGrey15' )
        sg.theme_input_text_color( '#FFFFFF' )
        sg.theme_element_text_color( '#69B1EF' )
        sg.theme_text_color('#69B1EF' )
        self.__themebackground = sg.theme_background_color()
        self.__themetextcolor = sg.theme_text_color()
        self.__elementbackcolor = sg.theme_text_element_background_color( )
        self.__elementforecolor = sg.theme_element_text_color()
        self.__textbackcolor = sg.theme_text_element_background_color( )
        self.__inputforecolor = sg.theme_input_text_color( )
        self.__inputbackcolor = sg.theme_input_background_color( )
        self.__buttonbackcolor = sg.theme_button_color_background( )
        self.__buttonforecolor = sg.theme_button_color_text( )
        self.__buttoncolor = sg.theme_button_color( )
        self.__icon = os.getcwd( ) + r'\etc\ico\ninja.ico'
        self.__themefont = ( 'Roboto', 9 )
        self.__scrollbarcolor = '#755600'
        self.__progressbarbackcolor = sg.theme
        self.__progressbarcolor =  sg.theme_progress_bar_color( )
        self.__formsize = ( 400, 200 )
        self.__settingspath = os.getcwd( ) + r'\etc\theme'
        sg.set_global_icon( icon = self.__icon )
        sg.set_options( font = self.__themefont )
        sg.user_settings_save( 'Budget', self.__settingspath )


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
    __selecteditem = None
    __formsize = None
    __extension = None
    __message = None
    __excel = None
    __csv = None
    __pdf = None
    __sqlite = None
    __sql = None
    __sqlserver = None
    __access = None
    __text = None

    @property
    def selectedpath( self ):
        if isinstance( self.__selecteditem, str ) and self.__selecteditem != '':
            return self.__selecteditem

    @selectedpath.setter
    def selectedpath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__selecteditem = value

    @property
    def message( self ):
        if isinstance( self.__message, str ) and self.__message != '':
            return self.__message

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__message = value

    def __init__( self, extension = EXT.XLSX ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__selecteditem = None
        self.__message = 'Search for File'
        self.__extension = extension if isinstance( extension, EXT ) else EXT.XLSX
        self.__excel = ( ( 'Excel Files', '*.xlsx' ), ) 
        self.__csv = ( ( 'CSV Files', '*.csv' ), ) 
        self.__pdf = ( ( 'PDF Files', '*.pdf' ), ) 
        self.__sql = ( ( 'SQL Files', '*.sql' ), ) 
        self.__text = ( ( 'Text Files', '*.txt' ), ) 
        self.__access = ( ( 'MS Access Databases', '*.accdb' ), ) 
        self.__sqlite = ( ( 'SQLite Databases', '*.db' ), ) 
        self.__sqlserver = ( ( 'SQL Server Databases', '*.mdf', '*.ldf', '*.sdf' ), ) 

    def __str__( self ):
        if isinstance( self.__selecteditem, str ):
            return self.__selecteditem

    def show( self ):
        try:
            layout = [ [ sg.Text( r'' ) ],
               [ sg.Text( self.__message, font = ( 'Roboto', 11 ) ) ],
               [ sg.Text( r'' ) ],
               [ sg.Input( key = '-PATH-' ), sg.FileBrowse( size = ( 15, 1 ) ) ],
               [ sg.Text( r'' ) ],
               [ sg.Text( r'' ) ],
               [ sg.OK( size = ( 8, 1 ),  ), sg.Cancel( size = ( 10, 1 )  ) ] ]

            window = sg.Window( ' Budget Execution', layout,
                font = self.__themefont,
                size = self.__formsize )

            while True:
                event, values = window.read( )
                if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel' ):
                    break
                elif event == 'OK':
                    self.__selecteditem = values[ '-PATH-' ]
                    window.close( )

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'FileDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


# FolderDialog( ) -> str
class FolderDialog( Sith ):
    '''Class defining dialog used to select a directory path'''
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


    @property
    def selectedpath( self ):
        if isinstance( self.__selecteditem, str ) and self.__selecteditem != '':
            return self.__selecteditem

    @selectedpath.setter
    def selectedpath( self, value ):
        if isinstance( value, str ) and value != '':
            self.__selecteditem = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__selecteditem = None

    def __str__( self ):
        if isinstance( self.__selecteditem, str ):
            return self.__selecteditem

    def show( self ):
        try:
            layout = [ [ sg.Text( r'' ) ],
               [ sg.Text( 'Search for Directory' ) ],
               [ sg.Text( r'' ) ],
               [ sg.Input( key = '-PATH-' ), sg.FolderBrowse( size = ( 15, 1 ) ) ],
               [ sg.Text( r'', size = ( 100, 1 ) ) ],
               [ sg.Text( r'', size = ( 100, 1 ) ) ],
               [ sg.OK( size = ( 8, 1 ) ), sg.Cancel( size = ( 10, 1 ) ) ] ]

            window = sg.Window( '  Budget Execution', layout,
                font = self.__themefont,
                size = self.__formsize )

            while True:
                event, values = window.read( )
                if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel' ):
                    break
                elif event == 'OK':
                    self.__selecteditem = values[ '-PATH-' ]
                    sg.popup_ok( self.__selecteditem,
                        title = 'Results',
                        icon = self.__icon,
                        font = self.__themefont )

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.cause = 'FolderDialog'
            exc.method = 'show( self )'
            error  = ErrorDialog( exc )
            error.show( )


# SaveFileDialog( path = '' )
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
    def original( self ):
        if isinstance( self.__original, str ) and self.__original != '':
            return self.__original

    @original.setter
    def original( self, value ):
        if isinstance( value, str) and os.path.exists( value ):
            self_original = value

    @property
    def filename( self ):
        if isinstance( self.__filename, str ) and self.__filename != '':
            return self.__filename

    @filename.setter
    def filename( self, value ):
        if isinstance( value, str):
            self__filename = value

    def __init__( self, path = '' ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 400, 200 )
        self.__original = path if isinstance( path, str) and os.path.isfile( path ) else None

    def __str__( self ):
        if isinstance( self.__filename, str ) and self.__filename != '':
            return self.__filename

    def show( self ):
        try:
            username = os.environ.get( 'USERNAME' )
            startpath = f'C:\\Users\\{username}\\Desktop'
            filename = sg.popup_get_file( 'Select Location / Enter File Name',
                default_path = startpath,
                title = '  Budget Execution',
                font = self.__themefont,
                icon = self.__icon,
                save_as = True )

            self.__filename = filename

            if isinstance( self.__original, str) and os.path.exists( self.__original ):
                src = io.open( self.__original, 'r' ).read( )
                new = io.open( filename, 'w+' ).write( src )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'SaveFileDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


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
        if isinstance( self.__results, list ) and len( self.__results ) > 0:
            return self.__results

    @search.setter
    def results( self, value ):
        if isinstance( value, list ) and len( value ) > 0:
            self.__results = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__image = os.getcwd( ) + r'\etc\img\app\web\google.png'

    def __str__( self ):
        if isinstance( self.__results, list ):
            return self.__results[ 0 ]

    def show( self ):
        try:
            self.__results = [ ]
            layout =  [ [ sg.Text( r'' ) ],
                [ sg.Image( source = self.__image ) ],
                [ sg.Text( '', size = ( 10, 1 ) ), sg.Input( '', key = '-QUERY-', size = ( 40, 2 ) ) ],
                [ sg.Text( r'', size = ( 100, 1 ) ) ],
                [ sg.Text( r'', size = ( 100, 1 ) ) ],
                [ sg.Text( r'', size = ( 10, 1 ) ), sg.Submit( size = ( 15, 1 ) ),
                  sg.Text( r'', size = ( 5, 1 ) ), sg.Cancel( size = ( 15, 1 ) ) ] ]

            window = sg.Window( '  Budget Execution', layout,
                icon = self.__icon,
                font = self.__themefont,
                size = self.__formsize )

            while True:
                event, values = window.read( )
                if event in ( sg.WIN_X_EVENT, sg.WIN_CLOSED, 'Cancel' ):
                    break
                elif event == 'Submit':
                    self.__querytext = values[ '-QUERY-' ]
                    google = search( term = self.__querytext, num_results = 5, lang = 'en' )
                    chrome = Client.Chrome
                    app = App( chrome )
                    for result in list( google ):
                        self.__results.append( result )
                        app.runargs( result )

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'GoogleDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


# EmailDialog( sender = '', receiver = '', subject = '', heading = '' )
class EmailDialog( Sith ):
    '''Class providing form used to send email messages. Constructor
    accepts optional string arguments 'sender', 'receiver', 'subject', and 'heading' '''
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
    __sender = None
    __receiver = None
    __subject = None
    __message = None
    __others = None
    __username = None
    __password = None

    @property
    def sender( self ):
        if isinstance( self.__sender, str ) and self.__sender != '':
            return self.__sender

    @sender.setter
    def sender( self, value ):
        if isinstance( value, str ) and value != '':
            self.__sender = value

    @property
    def receiver( self ):
        if isinstance( self.__receiver, str ) and self.__receiver != '':
            return self.__receiver

    @receiver.setter
    def receiver( self, value ):
        if isinstance( value, str ) and value != '':
            self.__receiver = value

    @property
    def message( self ):
        if isinstance( self.__message, str ) and self.__message != '':
            return self.__message

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__message = value

    @property
    def subject( self ):
        if isinstance( self.__subject, str ) and self.__subject != '':
            return self.__subject

    @subject.setter
    def subject( self, value ):
        if isinstance( value, str ) and value != '':
            self.__subject = value

    @property
    def others( self ):
        if isinstance( self.__others, list ):
            return self.__others

    @others.setter
    def others( self, value ):
        if isinstance( value, list ):
            self.__others = value

    @property
    def username( self ):
        if isinstance( self.__username, str ) and self.__username != '':
            return self.__username

    @username.setter
    def username( self, value ):
        if isinstance( value, str ) and value != '':
            self.__username = value

    @property
    def password( self ):
        if isinstance( self.__password, str ) and self.__password != '':
            return self.__password

    @password.setter
    def password( self, value ):
        if isinstance( value, str ) and value != '':
            self.__password= value

    def __init__( self, sender = '', receiver = '', subject = '', message = '' ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__image = os.getcwd( ) + r'\etc\img\app\web\outlook.png'
        self.__formsize = ( 600, 500 )
        self.__sender = sender if isinstance( sender, str ) and sender != '' else None
        self.__receiver = receiver if isinstance( receiver, str ) and receiver != '' else None
        self.__subject = subject if isinstance( subject, str ) and subject != '' else None
        self.__message = message if isinstance( message, str ) and message != '' else None

    def __str__( self ):
        if isinstance( self.__message, str ):
            return self.__message

    def show( self ):
        try:
            btn = ( 20, 1 )
            inp = ( 35, 1 )
            spc = ( 5, 1 )
            img = ( 50, 22 )
            clr = '#69B1EF'
            layout = [ [ sg.Text( ' ', size = spc ), ],
                       [ sg.Text( ' ', size = spc ), ],
                       [ sg.Text( ' ', size = spc ), sg.Text( 'From:', size = btn, text_color = clr  ),
                         sg.Input( key = '-EMAIL FROM-', size = inp ) ],
                       [ sg.Text( ' ', size = spc ), sg.Text( 'To:', size = btn, text_color = clr  ),
                         sg.Input( key = '-EMAIL TO-', size = inp ) ],
                       [ sg.Text( ' ', size = spc ), sg.Text( 'Subject:', size = btn, text_color = clr  ),
                         sg.Input( key = '-EMAIL SUBJECT-', size = inp ) ],
                       [ sg.Text( ' ', size = spc ), sg.Text( '' ) ],
                       [ sg.Text( ' ', size = spc ), sg.Text( 'Username:', size = btn, text_color = clr  ),
                         sg.Input( key = '-USER-', size = inp ) ],
                       [ sg.Text( ' ', size = spc ), sg.Text( 'Password:', size = btn, text_color = clr ),
                         sg.Input( password_char = '*', key = '-PASSWORD-', size = inp ) ],
                       [ sg.Text( ' ', size = spc ) ],
                       [ sg.Text( ' ', size = spc ),
                         sg.Multiline( 'Type your message here', size = ( 65, 10 ),
                             key = '-EMAIL TEXT-' ) ],
                       [ sg.Text( ' ', size = ( 100, 1 ) ) ],
                       [ sg.Text( ' ', size = spc ), sg.Button( 'Send', size = btn ),
                         sg.Text( ' ', size = btn ), sg.Button( 'Cancel', size = btn ) ] ]

            window = sg.Window( '  Budget Execution', layout,
                icon = self.__icon,
                size = self.__formsize )

            while True:  # Event Loop
                event, values = window.read()
                if event in (sg.WIN_CLOSED, 'Cancel', 'Exit' ):
                    break
                if event == 'Send':
                    sg.popup_quick_message( 'Sending your heading... this will take a moment...', background_color='red')
                    send_an_email( from_address = values[ '-EMAIL FROM-' ],
                        to_address=values['-EMAIL TO-'],
                        subject=values['-EMAIL SUBJECT-'],
                        message_text=values['-EMAIL TEXT-'],
                        user=values['-USER-'],
                        password=values['-PASSWORD-'])

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'EmailDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


# MessageDialog( text = '' )
class MessageDialog( Sith ):
    ''' Class that provides form used
     to display informational messages '''
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

    def __init__( self, text = '' ):
        self.__text = text if isinstance( text, str ) and text != '' else None
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 400, 200 )

    def __str__( self ):
        if isinstance( self.__text, str ):
            return self.__text

    def show( self ):
        try:
            txtsz = ( 100, 1 )
            btnsz = ( 10, 1 )
            layout = [ [ sg.Text( r'', size = txtsz ) ],
                       [ sg.Text( r'', size = txtsz ) ],
                       [ sg.Text( r'', size = (5, 1) ),
                         sg.Text( self.__text,
                             font = ( 'Roboto', 11),
                             enable_events = True,
                             key = '-TEXT-',
                             text_color = '#69B1EF',
                             size = ( 80, 1 ) ) ],
                       [ sg.Text( r'', size = txtsz ) ],
                       [ sg.Text( r'', size = txtsz ) ],
                       [ sg.Text( r'', size = txtsz ) ],
                       [ sg.Text( r'', size = (5, 1) ), sg.Ok( size = btnsz),
                         sg.Text( r'', size = (15, 1) ), sg.Cancel( size = btnsz ) ] ]

            window = sg.Window( r'  Budget Execution', layout,
                icon = self.__icon,
                font = self.__themefont,
                size = self.__formsize )

            while True:
                event, values = window.read( )
                if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Ok', 'Cancel' ):
                    break

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'MessageDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


# ErrorDialog( exception )
class ErrorDialog( Sith ):
    '''Class that displays excetption data that accepts
     a single, optional argument 'exception' of type Error'''
    __class = None
    __module = None
    __method = None
    __heading = None
    __type = None
    __trace = None
    __info = None
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
    def info( self ):
        '''Gets string comprised of exc_info( )[ 0 ] and traceback.format_exc( ) '''
        if isinstance( self.__class, str ) and self.__class != '':
            return self.__class

    @info.setter
    def info( self, value ):
        '''Sets string comprised of exc_info( )[ 0 ] and traceback.format_exc( ) '''
        if isinstance( value, str ) and value != '':
            self.__class = value

    @property
    def cause( self ):
        '''Gets string indicating the class generating the exception'''
        if isinstance( self.__class, str ) and self.__class != '':
            return self.__class

    @cause.setter
    def cause( self, value ):
        '''Sets the string indicating the class generating the exception'''
        if isinstance( value, str ) and value != '':
            self.__class = value

    @property
    def method( self ):
        '''Gets a string representing the method generating the exception'''
        if isinstance( self.__method, str ) and self.__method != '':
            return self.__method

    @method.setter
    def method( self, value ):
        '''Sets a string representing method generating the exception'''
        if isinstance( value, str ) and value != '':
            self.__method = value

    @property
    def module( self ):
        '''Gets a string representing module generating the exception'''
        if isinstance( self.__module, str ) and self.__module != '':
            return self.__module

    @module.setter
    def module( self, value ):
        '''Sets a string representing the module generating the exception'''
        if isinstance( value, str ) and value != '':
            self.__module = value

    @property
    def type( self ):
        '''sets the object type generating the exception'''
        if isinstance( self.__type, Exception ):
            return self.__type

    @type.setter
    def type( self, value ):
        '''sets the object type generating the exception'''
        if isinstance( value, Exception ):
            self.__type = value

    @property
    def message( self ):
        if isinstance( self.__heading, str ) and self.__heading != '':
            return self.__heading

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__heading = value

    def __init__( self, exception ):
        super( ).__init__( )
        self.__exception = exception if isinstance( exception, Error ) else None
        self.__heading = exception.message
        self.__module = exception.module
        self.__info = exception.stacktrace
        self.__cause = exception.cause
        self.__method = exception.method
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 500, 275 )

    def __str__( self ):
        if isinstance( self.__info, str ):
            return self.__info

    def show( self ):
        msg = self.__heading if isinstance( self.__heading, str ) else None
        info = f'Module:\t{ self.__module }\r\nClass:\t{ self.__cause }\r\n' \
                f'Method:\t{ self.__method }\r\n \r\n{ self.__info }'
        red = '#F70202'
        font = ( 'Roboto', 10 )
        padsz = ( 3, 3, 3, 3 )
        layout = [ [ sg.Text( r'' ) ],
                   [ sg.Text( f'{ msg }', size = ( 100, 1 ), key = '-MSG-', text_color = red,
                       font = font ) ],
                   [ sg.Text( r'', size = ( 150, 1 ) ) ],
                   [ sg.Multiline( f'{ info }', key = '-INFO-', size = ( 80, 7 ), pad = padsz ) ],
                   [ sg.Text( r'' ) ],
                   [ sg.Text( r'', size = (20, 1 ) ), sg.Cancel( size = ( 15, 1 ), key = '-CANCEL-' ),
                     sg.Text( r'', size = ( 10, 1 ) ), sg.Ok( size = ( 15, 1 ), key = '-OK-' ) ] ]

        window = sg.Window( r' Budget Execution', layout,
            icon = self.__icon,
            font = self.__themefont,
            size = self.__formsize )

        while True:
            event, values = window.read( )
            if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Canel', '-OK-' ):
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
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__question = question if isinstance( question, str ) else None
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 450, 200 )
        self.__response = None

    def __str__( self ):
        if isinstance( self.__response, str ):
            return self.__response

    def show( self ):
        try:
            layout =  [ [ sg.Text( r'' ) ],
                [ sg.Text( self.__question, font = ( 'Roboto', 9, 'bold' ) ) ],
                [ sg.Text( r'' ) ],
                [ sg.Text( 'Enter:', size = ( 10, 2 ) ), sg.InputText( key = '-INPUT-', size = ( 40, 2 ) ) ],
                [ sg.Text( r'', size = ( 100, 1 ) ) ],
                [ sg.Text( r'', size = ( 100, 1 ) ) ],
                [ sg.Text( r'', size = ( 10, 1 ) ), sg.Submit( size = ( 15, 1 ), key = '-SUBMIT-' ),
                  sg.Text( r'', size = ( 5, 1 ) ), sg.Cancel( size = ( 15, 1 ), key = '-CANCEL-' ) ] ]

            window = sg.Window( '  Budget Execution', layout,
                icon = self.__icon,
                font = self.__themefont,
                size = self.__formsize )

            while True:
                event, values = window.read( )
                if event in ( sg.WIN_X_EVENT, sg.WIN_CLOSED, '-CANCEL-', 'Exit' ):
                    break

                self.__response = values[ '-INPUT-' ]
                sg.popup( event, values, self.__response,
                    text_color = self.__themetextcolor,
                    font = self.__themefont,
                    icon = self.__icon )


            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'InputDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


# ScrollingDialog( text = '' )
class ScrollingDialog( Sith ):
    '''Provides form for multiline input/output'''
    __themebackground = None
    __elementbackcolor = None
    __elementforecolor = None
    __themetextcolor = None
    __textbackcolor = None
    __inputbackcolor = None
    __arrowcolor = None
    __inputforecolor = None
    __buttoncolor = None
    __icon = None
    __formsize = None
    __themefont = None

    @property
    def text( self ):
        if isinstance( self.__text, str ) and self.__text != '':
            return self.__text

    @text.setter
    def text( self, value ):
        if isinstance( value, str ) and value != '':
            self.__text = value

    def __init__( self, text = '' ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__arrowcolor = super( ).scrollbarcolor
        self.__formsize = ( 650, 500 )
        self.__text = text if isinstance( text, str ) and text != '' else None

    def __str__( self ):
        if isinstance( self.__text, str ):
            return self.__text

    def show( self ):
        try:
            line = ( 100, 1 )
            space = ( 5, 1 )
            btnsize = ( 25, 1 )
            arrow = self.__arrowcolor
            back = super( ).buttonbackcolor
            padsz = ( 3, 3, 3, 3 )
            layout = [ [ sg.Text( ' ', size = line ) ],
                       [ sg.Text( ' ', size = line ) ],
                       [ sg.Text( '', size = space ),
                         sg.Multiline( size = ( 70, 20 ), key = '-TEXT-', pad = padsz ),
                         sg.Text( '', size = space ) ],
                       [ sg.Text( ' ', size = line ) ],
                       [ sg.Text( ' ', size = space ), sg.Input( k = '-IN-', size = ( 70, 20 ) ),
                         sg.Text( '', size = space ) ],
                       [ sg.Text( ' ', size = line ) ],
                       [ sg.Text( '', size = space ), sg.Button( 'Submit', size = btnsize ),
                         sg.Text( '', size = (15, 1) ), sg.Button( 'Exit', size = btnsize ),
                         sg.Text( '', size = space ), ] ]

            window = sg.Window( '  Budget Execution', layout,
                icon = self.__icon,
                size = self.__formsize,
                font = self.__themefont,
                resizable = True )

            while True:
                event, values = window.read( )
                self.__text = values[ '-TEXT-' ]
                if event in (sg.WIN_CLOSED, 'Exit'):
                    break

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'ScrollingDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


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
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__image = os.getcwd( ) + r'\etc\img\app\web\outlook.png'
        self.__formsize = ( 450, 200 )

    def show( self ):
        try:
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

            window = sg.Window( '  Budget Execution', layout,
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
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'ContactForm'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


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
    __width = None
    __themefont = None
    __rows = None
    __columns = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def fieldwidth( self ):
        if isinstance( self.__width, tuple ):
            return self.__width

    @fieldwidth.setter
    def fieldwidth( self, value ):
        if isinstance( value, tuple ) and len( value ) == 2:
            self.__width = value

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

    def __init__( self, rows = 30, columns = 10 ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__image = None
        self.__width = ( 17, 1 )
        self.__rows = rows
        self.__columns = columns
        self.__formsize = ( 1250, 700 )

    def show( self ):
        try:
            black = self.__themebackground
            columns = self.__columns
            headings = [ f'HEADER-{ i + 1 }' for i in range( columns ) ]
            space = [ [ sg.Text( f'', size = ( 10, 1 ) ) ], [ sg.Text( f'', size = ( 10, 1 ) ) ], [ sg.Text( f'', size = ( 10, 1 ) ) ] ]
            header = [
                    [ sg.Text( h, size = ( 16, 1 ), justification = 'left' ) for h in headings ] ]
            records = [  [ [ sg.Input( size = self.__width, pad = ( 0, 0 ), font = self.__themefont )
                            for c in range( len( headings ) ) ] for r in range( self.__rows ) ], ]
            buttons = [ [ sg.Text( '', size = ( 35, 1 ) ), sg.Text( '', size = ( 10, 1 ) ), ],
                        [ sg.Text( '', size = (100, 1) ), sg.Text( '', size = (100, 1) ), sg.Ok( size = ( 35, 2 ) ) ],
                        [ sg.Sizegrip( background_color = black ) ] ]
            layout = space + header + records + buttons

            window = sg.Window( '  Budget Execution', layout,
                finalize = True,
                size = self.__formsize,
                icon = self.__icon,
                font = self.__themefont,
                resizable = True )


            while True:
                event, values = window.read( )
                if event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, '-CANCEL-' ):
                    break

                window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'GridForm'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


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
    __timeout = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def timeout( self ):
        if isinstance( self.__timeout, int ) :
            return self.__timeout

    @timeout.setter
    def timeout( self, value ):
        if isinstance( value, int ) :
            self.__timeout = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__image = os.getcwd( ) + r'\etc\img\loaders\loading.gif'
        self.__formsize = ( 800, 600 )
        self.__timeout = 6000

    def show( self ):
        try:
            layout = [ [ sg.Text( '',
                background_color = '#000000',
                text_color = '#FFF000',
                justification = 'c',
                key = '-T-',
                font = ( 'Bodoni MT', 40 ) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

            window = sg.Window( '  Loading...', layout,
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

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'LoadingPanel'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


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
    __timeout = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def timeout( self ):
        if isinstance( self.__timeout, int ) :
            return self.__timeout

    @timeout.setter
    def timeout( self, value ):
        if isinstance( value, int ) :
            self.__timeout = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__image = os.getcwd( ) + r'\etc\img\loaders\loader.gif'
        self.__themefont = ( 'Roboto', 9 )
        self.__formsize = ( 800, 600 )
        self.__timeout = 6000

    def show( self ):
        try:
            layout = [ [ sg.Text( '',
                background_color = '#000000',
                text_color = '#FFF000',
                justification = 'c',
                key = '-T-',
                font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

            window = sg.Window( '  Waiting...', layout,
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

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'WaitingPanel'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


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
    __timeout = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def timeout( self ):
        if isinstance( self.__timeout, int ) :
            return self.__timeout

    @timeout.setter
    def timeout( self, value ):
        if isinstance( value, int ) :
            self.__timeout = value

    def __init__( self ):
        super( ).__init__()
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__image = os.getcwd( ) + r'\etc\img\loaders\processing.gif'
        self.__formsize = ( 800, 600 )
        self.__timeout = None

    def show( self ):
        try:
            layout = [ [ sg.Text( '',
                background_color = '#000000',
                text_color = '#FFF000',
                justification = 'c',
                key = '-T-',
                font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

            window = sg.Window( '  Processing...', layout,
                element_justification = 'c',
                icon = self.__icon,
                margins = ( 0, 0 ),
                size = ( 800, 600 ),
                element_padding = ( 0, 0 ),
                finalize = True )

            window[ '-T-' ].expand( True, True, True )

            interframe_duration = Image.open( self.__image ).info[ 'duration' ]
            self.__timeout = interframe_duration

            while True:
                for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
                    event, values = window.read( timeout = self.__timeout,
                        timeout_key = '-TIMEOUT-' )
                    if event == sg.WIN_CLOSED or event == sg.WIN_X_EVENT:
                        exit( 0 )

                    window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )

            window.close( )

        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'ProcessingPanel'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


class SplashPanel( Sith ):
    '''Class providing splash dialog behavior'''
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
    __timeout = None

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def timeout( self ):
        if isinstance( self.__timeout, int ) :
            return self.__timeout

    @timeout.setter
    def timeout( self, value ):
        if isinstance( value, int ) :
            self.__timeout = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__buttonforecolor = super( ).buttonforecolor
        self.__buttobackcolor = super( ).buttonbackcolor
        self.__image = os.getcwd( ) + r'\etc\img\BudgetEx.png'
        self.__formsize = ( 800, 600 )
        self.__timeout = 6000

    def show( self ):
        try:
            img = self.__image
            imgsize = ( 500, 400 )
            line = ( 100, 2 )
            space = ( 15, 1 )
            layout = [ [ sg.Text( '', size = space ), sg.Text( '', size = line ) ],
                       [ sg.Text( '', size = space ), sg.Text( '', size = line ) ],
                       [ sg.Text( '', size = space ),
                            sg.Image( filename = self.__image, size = imgsize ) ] ]
            window = sg.Window( '  Budget Execution', layout,
                        no_titlebar = True,
                        keep_on_top = True,
                        grab_anywhere = True,
                        size = self.__formsize )
            while True:
                event, values = window.read( timeout = self.__timeout, close = True )
                if event in ( sg.WIN_CLOSED, 'Exit' ):
                    break
            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'SplashPanel'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


# Notification( heading )
class Notification( Sith ):
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
    __message = None

    @property
    def message( self ):
        if isinstance( self.__message, str ) and self.__message != '':
            return self.__message

    @message.setter
    def message( self, value ):
        if isinstance( value, str ) and value != '':
            self.__message = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__success = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U' \
                    b'/gAAAACXBIWXMAAAEKAAABCgEWpLzLAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5r' \
                    b'c2NhcGUub3Jnm+48GgAAAHJQTFRF////ZsxmbbZJYL9gZrtVar9VZsJcbMRYaM' \
                    b'ZVasFYaL9XbMFbasRZaMFZacRXa8NYasFaasJaasFZasJaasNZasNYasJYasJZ' \
                    b'asJZasJZasJZasJZasJYasJZasJZasJZasJZasJaasJZasJZasJZasJZ2IAizQ' \
                    b'AAACV0Uk5TAAUHCA8YGRobHSwtPEJJUVtghJeYrbDByNjZ2tvj6vLz9fb3/CyrN0oAAA' \
                    b'DnSURBVDjLjZPbWoUgFIQnbNPBIgNKiwwo5v1fsQvMvUXI5oqPf4DFOgCrhLKjC8GNV' \
                    b'gnsJY3nKm9kgTsduVHU3SU/TdxpOp15P7OiuV/PVzk5L3d0ExuachyaTWkAkLFtiBKAq' \
                    b'ZHPh/yuAYSv8R7XE0l6AVXnwBNJUsE2+GMOzWL8k3OEW7a/q5wOIS9e7t5qnGExvF5Bvl' \
                    b'c4w/LEM4Abt+d0S5BpAHD7seMcf7+ZHfclp10TlYZc2y2nOqc6OwruxUWx0rDjNJtyp6' \
                    b'HkUW4bJn0VWdf/a7nDpj1u++PBOR694+Ftj/8PKNdnDLn/V8YAAAAASUVORK5CYII='
        self.__fail = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U' \
                b'/gAAAACXBIWXMAAADlAAAA5QGP5Zs8AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm' \
                b'+48GgAAAIpQTFRF////20lt30Bg30pg4FJc409g4FBe4E9f4U9f4U9g4U9f4E9g31Bf4E9f4E9f' \
                b'4E9f4E9f4E9f4FFh4Vdm4lhn42Bv5GNx5W575nJ/6HqH6HyI6YCM6YGM6YGN6oaR8Kev9MPI9cb' \
                b'M9snO9s3R+Nfb+dzg+d/i++vt/O7v/fb3/vj5//z8//7+////KofnuQAAABF0Uk5TAAcIGBktSY' \
                b'SXmMHI2uPy8/XVqDFbAAAA8UlEQVQ4y4VT15LCMBBTQkgPYem9d9D//x4P2I7vILN68kj2WtsAh' \
                b'yDO8rKuyzyLA3wjSnvi0Eujf3KY9OUP+kno651CvlB0Gr1byQ9UXff+py5SmRhhIS0oPj4SaUUC' \
                b'AJHxP9+tLb/ezU0uEYDUsCc+l5/T8smTIVMgsPXZkvepiMj0Tm5txQLENu7gSF7HIuMreRxYNkb' \
                b'mHI0u5Hk4PJOXkSMz5I3nyY08HMjbpOFylF5WswdJPmYeVaL28968yNfGZ2r9gvqFalJNUy2UW' \
                b'mq1Wa7di/3Kxl3tF1671YHRR04dWn3s9cXRV09f3vb1fwPD7z9j1WgeRgAAAABJRU5ErkJggg=='
        self.__ninja = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAnCAYAAABuf0pMAAABhWlDQ1BJQ0MgUHJvZmlsZQA' \
            b'AeJx9kT1Iw0AcxV9bS1WqDnYo4pChOlkQFRFcpIpFsFDaCq06mFz6BU0akhQXR8G14ODHYtXB' \
            b'xVlXB1dBEPwAcXRyUnSREv+XFFrEeHDcj3f3HnfvAG+jwhSjaxxQVFNPxWNCNrcqBF7hRz96E' \
            b'MasyAwtkV7MwHV83cPD17soz3I/9+fok/MGAzwC8RzTdJN4g3h609Q47xOHWEmUic+Jx3S6I' \
            b'PEj1yWH3zgXbfbyzJCeSc0Th4iFYgdLHcxKukI8RRyRFZXyvVmHZc5bnJVKjbXuyV8YzKsr' \
            b'aa7THEYcS0ggCQESaiijAhNRWlVSDKRoP+biH7L9SXJJ5CqDkWMBVSgQbT/4H/zu1ihMTjh' \
            b'JwRjgf7GsjxEgsAs065b1fWxZzRPA9wxcqW1/tQHMfJJeb2uRI2BgG7i4bmvSHnC5A4SfNF' \
            b'EXbclH01soAO9n9E05YPAW6F1zemvt4/QByFBXyzfAwSEwWqTsdZd3d3f29u+ZVn8/pE' \
            b'Fyu/Q7rYsAAAbASURBVHicvZd/bJVXGcc/55z3vvdHuf3BbaFldGyDbQhSJsGNlSC66S' \
            b'gM/hDYxhJLRIcsbs7IRBONiTEi0RmDJltUthlykegYCT+EyUKZcZBABGSzU34NKpcC7S' \
            b'1tb2/f3h/v+57jH6Vd6S+gbXyS88853+d5vuf7nuc85xWMhVXWrgbWAAuBU8B24DUS8a5' \
            b'buYpRJq4Bfg5UDbLaDLxMIr4N4P3tmyLBoB357uZdFWkncP6fJw9lRkUgWF7zW19F13ky' \
            b'NCRmnKV5sabkaM38ioiBKs/39fZ9Z+Qfj4rf5S9tex7AGklyu/zJZYHcx+ssqwRlleCpK' \
            b'L6wAZgQ8lk4XbGq5h7KxkfIZvPzUp0ZxhcV0NGZlasWz2hxDu5ueutGLDkSAoHcpbVCO2g' \
            b'ZxlWFvckBHrrPJxyL8dKvz5DJ5ABwulyuJjs5eOwC44tC79ydPzu5B3/nClTWRkTq0CLI' \
            b'o2UEgQYMLyyfzhe/MJei4jCHD5+gtfEqUkqUkgSDkt3vNXP6cisLKs8ejSn18i+KS8P' \
            b'fa2/J3DGBSPbCHKE7bIRizlTBN55bwaxZDyKl4Oy58xw4cJz3/v4fFswIEw7ZHDp6gSMft' \
            b'HDgfAGfKbdIvH1sabll1QOPAftu+xDGYjGSyaRdGJu5eO1Xl+x66qkVTJ02DcdxOH' \
            b'GynncP/oMtf7nYiy8JaIqCgsspB+k7eIHxlNiae13FOq/hz1P0paNPNDVuvi0FtNbCGD' \
            b'PbGLOxufHEJMuySKfT1NW9zxtbd3PoVIrualC9Pm2upM2FymiEq2mQOkdbPsh1YVFsVT7' \
            b'9nO/th8Zbl2FrW9tdGF7yPO9bnueFHafr3N69e+/XydOUlpfhtLUjlaCwIISlJJ6vSTtZ' \
            b'XNdn2oyZdF2/wjMb6zEotAxiRC/Jk8C8QRVQSpFMJudms7n1zU3JpzsdR9t2IB4KhTZXL' \
            b'fhmTnWePL3ha0tFkeuSzuZZ9MTjZJINXEk6VEyIUFx+H/sPvEsm08Uv45fxVHSwNHOAH' \
            b'w5QoOX69QVdXZmfdKQ6Pt/RmW4BXgVeq573SHMPpqB4+p5IwFv27JLZLP5cFRcbW3lz10' \
            b'VOJKNUFki+vXwCD02PUXesiZ/taR1O4LabCDQ0/Hd5KtWx08lkEmBeAfF69byHM/29gh' \
            b'O/NDWQ/fgEVmERQgESX0XJ2hWYO7taNvQS+PBf9YA46DjOW8aYP1Q/+og7nGekdF611J3' \
            b'7kcEiEPhyHJlg5bDZBLqHoAN8h0R8Sy+BU6c+FEKK0OyqWQN2PJTZ5UsetPz2VwRmmVYF' \
            b'ZAPlGARg6N9mlM4Q9FpM3irb4cnQ90nEGxiAGoEFK55caXmtO4wM4aoijLDwZLhf8mxL' \
            b'wE/FtQz9Jn9lT0PftRE1o74mdWamMB7C70TKMDk1bgDGl6Fav3HHXwf1Hy0BLUOHDdKA' \
            b'RvlpAn4aYfz+sPVD+Y/6EwDYFctqLL/9DV9FJ+Ws2JAwEvEBB3vUCgDkreI6hDJGDPtF5' \
            b'w82OToClbUhAIGOCe3edQt045gRkJOfLaWytg5oobJ2o+U7VUaANC7K3KzyphfnA6RIx' \
            b'M+NGQHbu75JYB4DCoAfuCq6ptpNpSf5DqABWFFdyOs/XsTKZQt5Xqf2DRVrRIcwPPHx1a5' \
            b'VvNWTke4gxufu7HlmG03UKqLCZFBRi/uXzqX8nikEH5ieql2/bda1M/FE/1gjugdygbJ3' \
            b'gm6L8e2wMAiMUFyxK7hmXPJWCQvcFOdyUTbc+wA76v7NgV8d18DDwAACIy7DgrJH610rNj' \
            b'NvlfTOKZNDC4sVuascscvwIiGSGQPwdRLxNweLM4oqENdstwlLf9I6tAi0hgx7pnlN1Pg' \
            b'dPckN8PZQUUZMQMvwTiMsZJ9Tb5AbVnvXUkV2IVNxeqaPkIh3jDmBrD1xixH2cWF8hPG1' \
            b'1Ll222s/Dd5KVxWyy+ptzYeHizOqq1hOXlVoe6lPeaogLf2ujzwV9QM6rfLW+BttGYC' \
            b'VJOI7h4oxqm6oL/+pIwvHAILli/Jg7JwVw9Jd9JQoQ9yAvZsYDYG+pnT2b9x48fZJDvD' \
            b'B/4WAr8b9Pugm6T70pme6mUR82BfWmBHIXd2301WF9QE/jaVzH0njbwVm3spv1C+iHgu' \
            b'WL1pjdObTvopkfBmqHq70+trYKFD5FSG99vW+jKBlKAysvV3XnlqRQBCwgQDdyki6f/b' \
            b'kDVx/sobu1mfCpdVfllJszthT0J/8eu0CtpCI778VgUnAhEES3LZFYp99QQj5jFbRcC5' \
            b'QKrUI9F3+KYn4j4YjAN07D3GzAoqbFRB98Kbf8PsM98bIAVl6HghD2P8Avm6w' \
            b'ywIVvIgAAAAASUVORK5CYII='
        self.__message = 'This heading is intended to inform you that the action you' \
                'have performed has been successful. There is no need for further action.'

    def __str__( self ):
        if isinstance( self.__message, str ):
            return self.__message

    def show( self ):
        try:
            return sg.popup_notify( self.__message,
                title = 'Budget Execution Notification',
                icon = self.__ninja,
                display_duration_in_ms = 10000,
                fade_in_duration = 5000,
                alpha = 1 )

        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'Notification'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


class ImageSizeEncoder( Sith ):
    '''Class resizing image and encoding behavior'''
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
    __timeout = None

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor

    def show( self ):
        version = '1.3.1'
        __version__ = version.split( )[ 0 ]

        def resize(input_file, size, output_file=None, encode_format='PNG'):
            image = Image.open(input_file)
            width, height = image.size
            new_width, new_height = size
            if new_width != width or new_height != height:  # if the requested size is different than original size
                scale = min(new_height / height, new_width / width)
                resized_image = image.resize((int(width * scale), int(height * scale)), Image.ANTIALIAS)
            else:
                resized_image = image

            if output_file is not None:
                resized_image.save(output_file)

            # encode a PNG formatted version of image into BASE64
            with io.BytesIO() as bio:
                resized_image.save(bio, format=encode_format)
                contents = bio.getvalue()
                encoded = base64.b64encode(contents)
            return encoded

        def update_outfilename( ):
            infile = values[ '-IN-' ]
            if os.path.isfile( infile ):
                image = Image.open( infile )
                width, height = image.size
                window[ '-ORIG WIDTH-' ].update( image.size[ 0 ] )
                if not values[ '-WIDTH-' ]:
                    window[ '-WIDTH-' ].update( image.size[ 0 ] )
                if not values[ '-HEIGHT-' ]:
                    window[ '-HEIGHT-' ].update( image.size[ 1 ] )
                window[ '-ORIG HEIGHT-' ].update( image.size[ 1 ] )

                infilename = os.path.basename( infile )
                infilenameonly, infileext = os.path.splitext( infilename )
                if values[ '-NEW FORMAT-' ]:
                    outfileext = values[ '-NEW FORMAT-' ].lower( )
                    if outfileext == 'jpeg':
                        outfileext = 'jpg'
                else:
                    outfileext = infileext[ 1: ]  # strip off the .
                outfile = f'{infilenameonly}{width}x{height}.{outfileext}'
                outfullfilename = os.path.join( os.path.dirname( infile ), outfile )

                if values[ '-DO NOT SAVE-' ]:
                    window[ '-NEW FILENAME-' ].update( '' )
                    window[ '-BASE64-' ].update( True )
                else:
                    window[ '-NEW FILENAME-' ].update( outfullfilename )
            else:
                window[ '-NEW FILENAME-' ].update( '' )
                window[ '-ORIG WIDTH-' ].update( '' )
                # window['-WIDTH-'].update('')
                window[ '-ORIG HEIGHT-' ].update( '' )
                # window['-HEIGHT-'].update('')
                window[ '-NEW FILENAME-' ].update( )

        format_list = ('', 'PNG', 'JPEG', 'BMP', 'ICO', 'GIF', 'TIFF')
        new_format_layout = [
                [ sg.Combo( format_list,
                    default_value = sg.user_settings_get_entry( '-new format-', '' ),
                    readonly = True, enable_events = True, key = '-NEW FORMAT-' ) ] ]

        layout = [ [ sg.Text( 'Image Resizer' ) ],
                   [ sg.Frame( 'Input Filename', [
                           [ sg.Input( key = '-IN-', enable_events = True, s = 80 ),
                             sg.FileBrowse( ), ],
                           [ sg.T( 'Original size' ), sg.T( k = '-ORIG WIDTH-' ), sg.T( 'X' ),
                             sg.T( k = '-ORIG HEIGHT-' ) ] ] ) ],
                   [ sg.Frame( 'Output Filename',
                       [ [ sg.In( k = '-NEW FILENAME-', s = 80 ), sg.FileBrowse( ), ],
                         [ sg.In( default_text = sg.user_settings_get_entry( '-width-', '' ), s = 4,
                             k = '-WIDTH-' ), sg.T( 'X' ),
                           sg.In( default_text = sg.user_settings_get_entry( '-height-', '' ),
                               s = 4, k = '-HEIGHT-' ) ] ] ) ],
                   [ sg.Frame( 'Convert To New Format', new_format_layout ) ],
                   [ sg.CBox( 'Encode to Base64 and leave on Clipboard', k = '-BASE64-',
                       default = sg.user_settings_get_entry( '-base64-', True ) ) ],
                   [ sg.CBox( 'Do not save file - Only convert and Base64 Encode',
                       k = '-DO NOT SAVE-', enable_events = True,
                       default = sg.user_settings_get_entry( '-do not save-', False ) ) ],
                   [ sg.CBox( 'Autoclose Immediately When Done',
                       default = sg.user_settings_get_entry( '-autoclose-',
                           True if sg.running_windows( ) else False ),
                       k = '-AUTOCLOSE-' ) ],
                   [ sg.Button( 'Resize', bind_return_key = True ), sg.Button( 'Exit' ) ],
                   [ sg.T(
                       'Note - on some systems, autoclose cannot be used because the clipboard is '
                       'cleared by tkinter' ) ],
                   [ sg.T( 'Your settings are automatically saved between runs' ) ],
                   [ sg.T( f'Version {version}' ),
                     sg.T( 'Go to psgresizer GitHub Repo', font = '_ 8', enable_events = True,
                         k = '-PSGRESIZER-' ),
                     sg.T( 'A PySimpleGUI Application - Go to PySimpleGUI home', font = '_ 8',
                         enable_events = True, k = '-PYSIMPLEGUI-' ) ],
                   ]

        window = sg.Window( 'Resize Image', layout, icon = self.__icon,
            right_click_menu = sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT,
            enable_close_attempted_event = True, finalize = True )
        window[ '-PSGRESIZER-' ].set_cursor( 'hand1' )
        window[ '-PYSIMPLEGUI-' ].set_cursor( 'hand1' )
        while True:
            event, values = window.read( )
            # print(event, values)
            if event in (sg.WIN_CLOSED, sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit'):
                break
            infile = values[ '-IN-' ]
            update_outfilename( )

            if event == '-DO NOT SAVE-':
                if values[ '-DO NOT SAVE-' ]:
                    window[ '-NEW FILENAME-' ].update( '' )
                    window[ '-BASE64-' ].update( True )
            if event == 'Resize':
                try:
                    if os.path.isfile( infile ):
                        update_outfilename( )
                        infilename = os.path.basename( infile )
                        infilenameonly, infileext = os.path.splitext( infilename )
                        if values[ '-NEW FORMAT-' ]:
                            encode_format = values[ '-NEW FORMAT-' ].upper( )
                        else:
                            encode_format = infileext[ 1: ].upper( )  # strip off the .
                        if encode_format == 'JPG':
                            encode_format = 'JPEG'
                        outfullfilename = values[ '-NEW FILENAME-' ]
                        width, height = int( values[ '-WIDTH-' ] ), int( values[ '-HEIGHT-' ] )
                        if values[ '-DO NOT SAVE-' ]:
                            encoded = resize( input_file = infile, size = (width, height),
                                output_file = None, encode_format = encode_format )
                        else:
                            encoded = resize( input_file = infile, size = (width, height),
                                output_file = outfullfilename, encode_format = encode_format )

                        if values[ '-BASE64-' ]:
                            sg.clipboard_set( encoded )

                        sg.popup_quick_message( 'DONE!', font = '_ 40', background_color = 'red',
                            text_color = 'white' )

                except Exception as e:
                    sg.popup_error_with_traceback( 'Error resizing or converting',
                        'Error encountered during the resize or Base64 encoding', e )
                if values[ '-AUTOCLOSE-' ]:
                    break
            elif event == 'Version':
                sg.popup_scrolled( sg.get_versions( ), non_blocking = True )
            elif event == 'Edit Me':
                sg.execute_editor( __file__ )
            elif event == 'File Location':
                sg.popup_scrolled( 'This Python file is:', __file__ )
            elif event == '-PYSIMPLEGUI-':
                webbrowser.open_new_tab( r'http://www.PySimpleGUI.com' )
            elif event == '-PSGRESIZER-':
                webbrowser.open_new_tab( r'https://github.com/PySimpleGUI/psgresizer' )

        if event != sg.WIN_CLOSED:
            sg.user_settings_set_entry( '-autoclose-', values[ '-AUTOCLOSE-' ] )
            sg.user_settings_set_entry( '-new format-', values[ '-NEW FORMAT-' ] )
            sg.user_settings_set_entry( '-do not save-', values[ '-DO NOT SAVE-' ] )
            sg.user_settings_set_entry( '-base64-', values[ '-BASE64-' ] )
            sg.user_settings_set_entry( '-width-', values[ '-WIDTH-' ] )
            sg.user_settings_set_entry( '-height-', values[ '-HEIGHT-' ] )

        window.close( )



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
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( ).__init__()
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 600, 800 )

    def show( self ):
        try:
            oldpage = 0
            zoom = 0
            oldzoom = 0

            filename = sg.popup_get_file( 'Select file', ' Budget PDF Viewer',
                icon = self.__icon,
                font = self.__themefont,
                file_types = ( ( 'PDF Files', '*.pdf' ), ) )

            if filename is None:
                sg.popup_cancel( 'Cancelling' )
                exit( 0 )

            pdf = fitz.open( filename )
            pages = len( pdf )
            displaylist = [ None ] * pages
            title =  ' Budget Execution'

            def getpage( pno, zoom = 0 ):
                display = displaylist[ pno ]
                if not display:
                    displaylist[ pno ] = pdf[ pno ].get_displaylist( )
                    display = displaylist[ pno ]

                r = display.rect
                mp = r.tl + ( r.br - r.tl ) * 0.5  # rect middle point
                mt = r.tl + (r.tr - r.tl ) * 0.5  # middle of top edge
                ml = r.tl + (r.bl - r.tl) * 0.5  # middle of left edge
                mr = r.tr + (r.br - r.tr) * 0.5  # middle of right egde
                mb = r.bl + (r.br - r.bl) * 0.5  # middle of bottom edge
                mat = fitz.Matrix( 2, 2 )
                if zoom == 1:
                    clip = fitz.Rect(r.tl, mp)
                elif zoom == 4:
                    clip = fitz.Rect(mp, r.br)
                elif zoom == 2:
                    clip = fitz.Rect(mt, mr)
                elif zoom == 3:
                    clip = fitz.Rect(ml, mb)
                if zoom == 0:
                    pix = display.get_pixmap( alpha = False )
                else:
                    pix = display.get_pixmap( alpha = False, matrix = mat, clip = clip )
                return pix.tobytes( )

            currentpage = 0
            data = getpage( currentpage )
            image = sg.Image( data = data )
            goto = sg.InputText( f'{ str( currentpage + 1 ) } of { str( pages ) }', size = ( 10, 1 ) )
            layout = [ [ sg.Button( 'Prev' ), sg.Button( 'Next' ),
                         sg.Text( '' ),
                         sg.Text( 'Page:' ),  goto,
                         sg.Text( '', size = ( 10, 1) ), sg.Text( 'Zoom: '),
                         sg.Button( ' In ', key = '-IN-' ), sg.Button( ' Out', key = '-OUT-' ), ],
                       [ image ], ]

            keys = ( 'Next', 'Next:34', 'Prev', 'Prior:33', 'MouseWheel:Down', 'MouseWheel:Up', '-IN-', '-OUT-' )

            window = sg.Window( title, layout,
                size = self.__formsize,
                font = self.__themefont,
                modal = True,
                resizable = True,
                grab_anywhere = True,
                icon = self.__icon )

            while True:
                event, values = window.read( )
                forcepage = False
                if event == sg.WIN_CLOSED:
                    break
                elif event in ( 'Next', 'Next:34', 'MouseWheel:Down' ):
                    currentpage += 1
                    goto.Update( f'{ str( currentpage + 1 ) } of { str( pages ) }' )
                elif event in ( 'Prev', 'Prior:33', 'MouseWheel:Up' ):
                    currentpage -= 1
                    goto.Update( f'{ str( currentpage + 1 ) } of { str( pages ) }' )
                elif event == '-IN-':
                    zoom += 1
                elif event == '-OUT-':
                    zoom -= 1

                if currentpage >= pages:
                    currentpage = 0

                while currentpage < 0:
                    currentpage += pages

                if currentpage != oldpage:
                    zoom = oldzoom = 0
                    forcepage = True
                    if zoom != oldzoom:
                        forcepage = True

                if forcepage:
                    data = getpage( currentpage, zoom )
                    image.update( data = data )
                    oldpage = currentpage

                oldzoom = zoom

                if event in keys or not values[ 0 ]:
                    goto.update( f'{ str( currentpage + 1 ) } of { str( pages ) }' )

        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'PdfForm'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


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
    __selecteditem = None
    __day = None
    __month = None
    __year = None


    @property
    def selecteditem( self ):
        if isinstance( self.__selecteditem, tuple ):
            yr = str( self.__selecteditem[ 2 ] )
            mo = str( self.__selecteditem[ 0 ] ).zfill( 2 )
            dy = str( self.__selecteditem[ 1 ] ).zfill( 2 )
            date = f'{ yr }/{ mo }/{ dy }'
            return date

    @selecteditem.setter
    def selecteditem( self, value ):
        if isinstance( value, tuple ):
            self.__selecteditem = value

    @property
    def day( self ):
        if isinstance( self.__selecteditem, tuple ):
            return str( self.__selecteditem[ 1 ] ).zfill( 2 )

    @day.setter
    def day( self, value ):
        if isinstance( value, tuple ):
            self.__day = str( value[ 1 ] ).zfill( 2 )

    @property
    def month( self ):
        if isinstance( self.__selecteditem, tuple ):
            return str( self.__selecteditem[ 0 ] ).zfill( 2 )

    @month.setter
    def month( self, value ):
        if isinstance( value, tuple ):
            self.__day = str( value[ 0 ] ).zfill( 2 )

    @property
    def year( self ):
        if isinstance( self.__selecteditem, tuple ):
            return str( self.__selecteditem[ 2 ] )

    @year.setter
    def year( self, value ):
        if isinstance( value, tuple ):
            self.__day = str( value[ 2 ] ).zfill( 4 )

    def __init__( self ):
        super( ).__init__()
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 450, 250 )

    def __str__( self ):
        if isinstance( self.__selecteditem, tuple ):
            yr = str( self.__selecteditem[ 2 ] )
            mo = str( self.__selecteditem[ 0 ] ).zfill( 2 )
            dy = str( self.__selecteditem[ 1 ] ).zfill( 2 )
            date = f'{ yr }/{ mo }/{ dy }'
            return date

    def show( self ):
        try:
            btnsize = (20, 1)
            calendar = (250, 250)

            months = [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
            'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ]

            days = [ 'SUN', 'MON', 'TUE', 'WEC', 'THU', 'FRI', 'SAT' ]

            cal = sg.popup_get_date( title = 'Calendar',
                                     no_titlebar = False,
                                     icon = self.__icon,
                                     month_names = months,
                                     day_abbreviations = days,
                                     close_when_chosen = True )

            self.__selecteditem = cal

        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'CalendarDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )



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
    __selecteditem = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( ).__init__()
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 450, 250 )

    def show( self ):
        try:
            ALPHA = 0.9  # Initial alpha until user changes
            THEME = 'Dark green 3'  # Initial theme until user changes
            refresh_font = title_font = 'Roboto 8'
            main_info_font = 'Roboto 20'
            main_info_size = (10, 1)
            UPDATE_FREQUENCY_MILLISECONDS = 1000 * 60 * 60



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
                           [ sg.Listbox( values = sg.theme_list( ), size = (20, 20), key = '-ITEM-',
                               enable_events = True ) ],
                           [ sg.OK( ), sg.Cancel( ) ] ]

                window = sg.Window( 'Look and Feel Browser', layout, location = location,
                    keep_on_top = True )
                old_theme = sg.theme( )
                while True:  # Event Loop
                    event, values = window.read( )
                    if event in (sg.WIN_CLOSED, 'Exit', 'OK', 'Cancel'):
                        break
                    sg.theme( values[ '-ITEM-' ][ 0 ] )
                    window.hide( )
                    # make at test window to the left of the current one
                    test_window = make_window(
                        location = ((location[ 0 ] - size[ 0 ] * 1.2, location[ 1 ])),
                        test_window = True )
                    test_window.read( close = True )
                    window.un_hide( )
                window.close( )

                # after choice made, save theme or restore the old one
                if event == 'OK' and values[ '-ITEM-' ]:
                    sg.theme( values[ '-ITEM-' ][ 0 ] )
                    sg.user_settings_set_entry( '-theme-', values[ '-ITEM-' ][ 0 ] )
                    return values[ '-ITEM-' ][ 0 ]
                else:
                    sg.theme( old_theme )
                return None

            def make_window( location, test_window = False ):
                """
                Defines the layout and creates the window for the main window
                If the parm test_window is True, then a simplified, and EASY to close version is shown

                :param location: (x,y) location to createtable the window
                :type location: Tuple[int, int]
                :param test_window: If True, then this is a test window & will close by clicking on it
                :type test_window: bool
                :return: newly created window
                :rtype: sg.Window
                """
                title = sg.user_settings_get_entry( '-seconditems-', '' )
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

            window = make_window( sg.user_settings_get_entry( '-location-', location ) )

            refresh_frequency = sg.user_settings_get_entry( '-fresh frequency-',
                UPDATE_FREQUENCY_MILLISECONDS )

            while True:
                window[ '-MAIN INFO-' ].update( 'Your Info' )
                window[ '-REFRESHED-' ].update(
                    datetime.datetime.now( ).strftime( "%m/%d/%Y\n%I:%M:%S %p" ) )
                event, values = window.read( timeout = refresh_frequency )
                print( event, values )
                if event in (sg.WIN_CLOSED, 'Exit'):
                    break
                if event == 'Edit Me':
                    sg.execute_editor( __file__ )
                elif event == 'Choose Title':
                    new_title = sg.popup_get_text( 'Choose a seconditems for your Widget',
                        location = window.current_location( ), keep_on_top = True )
                    if new_title is not None:
                        window[ '-TITLE-' ].update( new_title )
                        sg.user_settings_set_entry( '-seconditems-', new_title )
                elif event == 'Show Refresh Info':
                    window[ '-REFRESHED-' ].update( visible = True )
                    sg.user_settings_set_entry( '-show refresh-', True )
                elif event == 'Save Location':
                    sg.user_settings_set_entry( '-location-', window.current_location( ) )
                elif event == 'Hide Refresh Info':
                    window[ '-REFRESHED-' ].update( visible = False )
                    sg.user_settings_set_entry( '-show refresh-', False )
                elif event in [ str( x ) for x in range( 1, 11 ) ]:
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
                            refresh_frequency = float( choice ) * 1000
                            sg.user_settings_set_entry( '-fresh frequency-',
                                float( refresh_frequency ) )
                        except Exception as e:
                            sg.popup_error( f'You entered an incorrect number of seconds: {choice}',
                                f'Error: {e}', location = window.current_location( ),
                                keep_on_top = True )
                elif event == 'New Theme':
                    loc = window.current_location( )
                    if choose_theme( window.current_location( ), window.formsize ) is not None:
                        window.close( )
                        window = make_window( loc )

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'DatePael'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


# ComboBoxDialog( data )
class ComboBoxDialog( Sith ):
    '''Logger object provides form for log printing'''
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
    __items = None
    __selecteditem = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def items( self ):
        if isinstance( self.__items, list ):
            return self.__items

    @items.setter
    def items( self, value ):
        if isinstance( value, list ):
            self.__items = value

    @property
    def selecteditem( self ):
        if isinstance( self.__selecteditem, str ):
            return self.__selecteditem

    @selecteditem.setter
    def selecteditem( self, value ):
        if isinstance( value, str ):
            self.__selecteditem = value

    def __init__( self, data = None):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 400, 150 )
        self.__items = data if isinstance( data, list ) and len( data ) > 0 else None

    def __str__( self ) :
        if isinstance( self.__selecteditem, str ) and self.__selecteditem != '':
            return self.__selecteditem

    def show( self ):
        try:
            btnsize = ( 10 , 1 )
            space = ( 5, 1 )
            if self.__items == None:
                self.__items = [ f'Item { x } ' for x in range( 30 ) ]
                values = self.__items

            layout = [ [ sg.Text( size = space ), sg.Text( size = space ) ],
                       [ sg.Text( size = space ), sg.Text( 'Select Item' ) ],
                       [ sg.Text( size = space ) , sg.DropDown( self.__items, key = '-ITEM-', size = ( 35, 1 ) ) ],
                       [ sg.Text( size = space ), sg.Text( size = space ) ],
                       [ sg.Text( size = space ), sg.OK( size = btnsize ), sg.Text( size = ( 8, 1 ) ), sg.Cancel( size = btnsize ) ] ]

            window = sg.Window( '  Budget Execution', layout,
                icon = self.__icon,
                size = self.__formsize )

            while True:
                event, values = window.read( )
                if event in ( sg.WIN_CLOSED, 'Exit', 'Cancel' ):
                    break

                self.__selecteditem = values[ '-ITEM-' ]
                sg.popup( event, values, self.__selecteditem,
                    text_color = self.__themetextcolor,
                    font = self.__themefont,
                    icon = self.__icon )

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'ComboBoxDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )


# ListBoxDialog( data )
class ListBoxDialog( Sith ):
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
    __image = None

    @property
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def items( self ):
        if isinstance( self.__items, list ):
            return self.__items

    @items.setter
    def items( self, value ):
        if isinstance( value, list ):
            self.__items = value

    @property
    def selecteditem( self ):
        if isinstance( self.__selecteditem, str ):
            return self.__selecteditem

    @selecteditem.setter
    def selecteditem( self, value ):
        if isinstance( value, str ) and value != '':
            self.__selecteditem = value

    def __init__( self, data = () ):
        super( ).__init__()
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 400, 250 )
        self.__image = os.getcwd( ) + r'\etc\img\app\dialog\lookup.png'
        self.__items = data if isinstance( data, list ) else None

    def __str__( self ) :
        if isinstance( self.__selecteditem, str ) and self.__selecteditem != '':
            return self.__selecteditem

    def show( self ):
        try:
            btnsize = ( 10, 1 )
            space = ( 10, 1 )
            line = ( 100, 1 )
            txtsz = (25, 1)
            inpsz = (25, 1)
            lstsz = (25, 5)
            names = [ ]

            if isinstance( self.__items, list ):
                names = [ src for src in self.__items ]
            else:
                names = [ f'Item - { i }' for i in range( 40 ) ]

            layout = [ [ sg.Text( '', size = space ), sg.Text( r'', size = line ) ],
                       [ sg.Text( '', size = space ), sg.Text( r'Search:' ) ],
                       [ sg.Text( '', size = space ), sg.Input( size = inpsz, enable_events = True, key = '-INPUT-' ) ],
                       [ sg.Text( '', size = space ), sg.Text( r'', size = line ) ],
                       [ sg.Text( '', size = space ), sg.Listbox( names, size = lstsz, key = '-ITEM-', font = self.__themefont ) ],
                       [ sg.Text( '', size = space ), sg.Text( r'', size = line ) ],
                       [ sg.Text( '', size = space ), sg.Button( 'Select', size = btnsize, enable_events = True ), sg.Text( '', size = ( 3, 1 ) ), sg.Button( 'Exit', size = btnsize  ) ] ]

            window = sg.Window( '  Budget Execution', layout,
                size = self.__formsize,
                font = self.__themefont,
                icon = self.__icon )

            while True:
                event, values = window.read( )
                if event in ( sg.WIN_CLOSED, 'Exit' ):
                    break
                self.__selecteditem = str( values[ '-ITEM-' ][ 0 ] )
                if event == 'Selected':
                    self.__selecteditem = str( values[ '-ITEM-' ][ 0 ] )
                    sg.popup( 'Results', self.__selecteditem,
                        font = self.__themefont,
                        icon = self.__icon  )
                    window.close( )

                if values[ '-INPUT-' ] != '':
                    search = values[ '-INPUT-' ]
                    new_values = [ x for x in names if search in x ]
                    window[ '-ITEM-' ].update( new_values )
                else:
                    window[ '-ITEM-' ].update( names )

            window.close( )

        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'ListBoxDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )



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
    __rgb = None
    __hex = None
    __html = None
    __argb = None

    @property
    def rgb( self ):
        if isinstance( self.__rgb, str ) and self.__rgb != '':
            return self.__rgb

    @rgb.setter
    def rgb( self, value ):
        if isinstance( value, str ) and value != '':
            self.__rgb = value

    @property
    def hex( self ):
        if isinstance( self.__hex, str ) and self.__hex != '':
            return self.__hex

    @hex.setter
    def hex( self, value ):
        if isinstance( value, str ) and value != '':
            self.__hex = value

    @property
    def argb( self ):
        if isinstance( self.__argb, str ) and self.__argb != '':
            return self.__argb

    @argb.setter
    def argb( self, value ):
        if isinstance( value, str ) and value != '':
            self.__argb = value

    @property
    def html( self ):
        if isinstance( self.__html, str ) and self.__html != '':
            return self.__html

    @html.setter
    def html( self, value ):
        if isinstance( value, str ) and value != '':
            self.__html = value

    def __init__( self ):
        super( ).__init__()
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 450, 450 )

    def show( self ):
        try:
            color_map = { 'alice blue': '#F0F8FF',
                          'AliceBlue': '#F0F8FF',
                          'antique white': '#FAEBD7',
                          'AntiqueWhite': '#FAEBD7',
                          'AntiqueWhite1': '#FFEFDB',
                          'AntiqueWhite2': '#EEDFCC',
                          'AntiqueWhite3': '#CDC0B0',
                          'AntiqueWhite4': '#8B8378',
                          'aquamarine': '#7FFFD4',
                          'aquamarine1': '#7FFFD4',
                          'aquamarine2': '#76EEC6',
                          'aquamarine3': '#66CDAA',
                          'aquamarine4': '#458B74',
                          'azure': '#F0FFFF',
                          'azure1': '#F0FFFF',
                          'azure2': '#E0EEEE',
                          'azure3': '#C1CDCD',
                          'azure4': '#838B8B',
                          'beige': '#F5F5DC',
                          'bisque':  '#FFE4C4',
                          'bisque1':  '#FFE4C4',
                          'bisque2':  '#EED5B7',
                          'bisque3':  '#CDB79E',
                          'bisque4':  '#8B7D6B',
                          'black':  '#000000',
                          'blanched almond':  '#FFEBCD',
                          'BlanchedAlmond':  '#FFEBCD',
                          'blue':  '#0000FF',
                          'blue violet':  '#8A2BE2',
                          'blue1':  '#0000FF',
                          'blue2':  '#0000EE',
                          'blue3':  '#0000CD',
                          'blue4':  '#00008B',
                          'BlueViolet':  '#8A2BE2',
                          'brown':  '#A52A2A',
                          'brown1':  '#FF4040',
                          'brown2':  '#EE3B3B',
                          'brown3':  '#CD3333',
                          'brown4':  '#8B2323',
                          'burlywood':  '#DEB887',
                          'burlywood1':  '#FFD39B',
                          'burlywood2':  '#EEC591',
                          'burlywood3':  '#CDAA7D',
                          'burlywood4':  '#8B7355',
                          'cadet blue':  '#5F9EA0',
                          'CadetBlue':  '#5F9EA0',
                          'CadetBlue1':  '#98F5FF',
                          'CadetBlue2':  '#8EE5EE',
                          'CadetBlue3':  '#7AC5CD',
                          'CadetBlue4':  '#53868B',
                          'chartreuse':  '#7FFF00',
                          'chartreuse1':  '#7FFF00',
                          'chartreuse2':  '#76EE00',
                          'chartreuse3':  '#66CD00',
                          'chartreuse4':  '#458B00',
                          'chocolate':  '#D2691E',
                          'chocolate1':  '#FF7F24',
                          'chocolate2':  '#EE7621',
                          'chocolate3':  '#CD661D',
                          'chocolate4':  '#8B4513',
                          'coral':  '#FF7F50',
                          'coral1':  '#FF7256',
                          'coral2':  '#EE6A50',
                          'coral3':  '#CD5B45',
                          'coral4':  '#8B3E2F',
                          'cornflower blue':  '#6495ED',
                          'CornflowerBlue':  '#6495ED',
                          'cornsilk':  '#FFF8DC',
                          'cornsilk1':  '#FFF8DC',
                          'cornsilk2':  '#EEE8CD',
                          'cornsilk3':  '#CDC8B1',
                          'cornsilk4':  '#8B8878',
                          'cyan':  '#00FFFF',
                          'cyan1':  '#00FFFF',
                          'cyan2':  '#00EEEE',
                          'cyan3':  '#00CDCD',
                          'cyan4':  '#008B8B',
                          'dark blue':  '#00008B',
                          'dark cyan':  '#008B8B',
                          'dark goldenrod':  '#B8860B',
                          'dark gray':  '#A9A9A9',
                          'dark green':  '#006400',
                          'dark grey':  '#A9A9A9',
                          'dark khaki':  '#BDB76B',
                          'dark magenta':  '#8B008B',
                          'dark olive green':  '#556B2F',
                          'dark orange':  '#FF8C00',
                          'dark orchid':  '#9932CC',
                          'dark red':  '#8B0000',
                          'dark salmon':  '#E9967A',
                          'dark sea green':  '#8FBC8F',
                          'dark slate blue':  '#483D8B',
                          'dark slate gray':  '#2F4F4F',
                          'dark slate grey':  '#2F4F4F',
                          'dark turquoise':  '#00CED1',
                          'dark violet':  '#9400D3',
                          'DarkBlue':  '#00008B',
                          'DarkCyan':  '#008B8B',
                          'DarkGoldenrod':  '#B8860B',
                          'DarkGoldenrod1':  '#FFB90F',
                          'DarkGoldenrod2':  '#EEAD0E',
                          'DarkGoldenrod3':  '#CD950C',
                          'DarkGoldenrod4':  '#8B6508',
                          'DarkGray':  '#A9A9A9',
                          'DarkGreen':  '#006400',
                          'DarkGrey':  '#A9A9A9',
                          'DarkKhaki':  '#BDB76B',
                          'DarkMagenta':  '#8B008B',
                          'DarkOliveGreen':  '#556B2F',
                          'DarkOliveGreen1':  '#CAFF70',
                          'DarkOliveGreen2':  '#BCEE68',
                          'DarkOliveGreen3':  '#A2CD5A',
                          'DarkOliveGreen4':  '#6E8B3D',
                          'DarkOrange':  '#FF8C00',
                          'DarkOrange1':  '#FF7F00',
                          'DarkOrange2':  '#EE7600',
                          'DarkOrange3':  '#CD6600',
                          'DarkOrange4':  '#8B4500',
                          'DarkOrchid':  '#9932CC',
                          'DarkOrchid1':  '#BF3EFF',
                          'DarkOrchid2':  '#B23AEE',
                          'DarkOrchid3':  '#9A32CD',
                          'DarkOrchid4':  '#68228B',
                          'DarkRed':  '#8B0000',
                          'DarkSalmon':  '#E9967A',
                          'DarkSeaGreen':  '#8FBC8F',
                          'DarkSeaGreen1':  '#C1FFC1',
                          'DarkSeaGreen2':  '#B4EEB4',
                          'DarkSeaGreen3':  '#9BCD9B',
                          'DarkSeaGreen4':  '#698B69',
                          'DarkSlateBlue':  '#483D8B',
                          'DarkSlateGray':  '#2F4F4F',
                          'DarkSlateGray1':  '#97FFFF',
                          'DarkSlateGray2':  '#8DEEEE',
                          'DarkSlateGray3':  '#79CDCD',
                          'DarkSlateGray4':  '#528B8B',
                          'DarkSlateGrey':  '#2F4F4F',
                          'DarkTurquoise':  '#00CED1',
                          'DarkViolet':  '#9400D3',
                          'deep pink':  '#FF1493',
                          'deep sky blue':  '#00BFFF',
                          'DeepPink':  '#FF1493',
                          'DeepPink1':  '#FF1493',
                          'DeepPink2':  '#EE1289',
                          'DeepPink3':  '#CD1076',
                          'DeepPink4':  '#8B0A50',
                          'DeepSkyBlue':  '#00BFFF',
                          'DeepSkyBlue1':  '#00BFFF',
                          'DeepSkyBlue2':  '#00B2EE',
                          'DeepSkyBlue3':  '#009ACD',
                          'DeepSkyBlue4':  '#00688B',
                          'dim gray':  '#696969',
                          'dim grey':  '#696969',
                          'DimGray':  '#696969',
                          'DimGrey':  '#696969',
                          'dodger blue':  '#1E90FF',
                          'DodgerBlue':  '#1E90FF',
                          'DodgerBlue1':  '#1E90FF',
                          'DodgerBlue2':  '#1C86EE',
                          'DodgerBlue3':  '#1874CD',
                          'DodgerBlue4':  '#104E8B',
                          'firebrick':  '#B22222',
                          'firebrick1':  '#FF3030',
                          'firebrick2':  '#EE2C2C',
                          'firebrick3':  '#CD2626',
                          'firebrick4':  '#8B1A1A',
                          'floral white':  '#FFFAF0',
                          'FloralWhite':  '#FFFAF0',
                          'forest green':  '#228B22',
                          'ForestGreen':  '#228B22',
                          'gainsboro':  '#DCDCDC',
                          'ghost white':  '#F8F8FF',
                          'GhostWhite':  '#F8F8FF',
                          'gold':  '#FFD700',
                          'gold1':  '#FFD700',
                          'gold2':  '#EEC900',
                          'gold3':  '#CDAD00',
                          'gold4':  '#8B7500',
                          'goldenrod':  '#DAA520',
                          'goldenrod1':  '#FFC125',
                          'goldenrod2':  '#EEB422',
                          'goldenrod3':  '#CD9B1D',
                          'goldenrod4':  '#8B6914',
                          'green':  '#00FF00',
                          'green yellow':  '#ADFF2F',
                          'green1':  '#00FF00',
                          'green2':  '#00EE00',
                          'green3':  '#00CD00',
                          'green4':  '#008B00',
                          'GreenYellow':  '#ADFF2F',
                          'grey':  '#BEBEBE',
                          'grey0':  '#000000',
                          'grey1':  '#030303',
                          'grey2':  '#050505',
                          'grey3':  '#080808',
                          'grey4':  '#0A0A0A',
                          'grey5':  '#0D0D0D',
                          'grey6':  '#0F0F0F',
                          'grey7':  '#121212',
                          'grey8':  '#141414',
                          'grey9':  '#171717',
                          'grey10':  '#1A1A1A',
                          'grey11':  '#1C1C1C',
                          'grey12':  '#1F1F1F',
                          'grey13':  '#212121',
                          'grey14':  '#242424',
                          'grey15':  '#262626',
                          'grey16':  '#292929',
                          'grey17':  '#2B2B2B',
                          'grey18':  '#2E2E2E',
                          'grey19':  '#303030',
                          'grey20':  '#333333',
                          'grey21':  '#363636',
                          'grey22':  '#383838',
                          'grey23':  '#3B3B3B',
                          'grey24':  '#3D3D3D',
                          'grey25':  '#404040',
                          'grey26':  '#424242',
                          'grey27':  '#454545',
                          'grey28':  '#474747',
                          'grey29':  '#4A4A4A',
                          'grey30':  '#4D4D4D',
                          'grey31':  '#4F4F4F',
                          'grey32':  '#525252',
                          'grey33':  '#545454',
                          'grey34':  '#575757',
                          'grey35':  '#595959',
                          'grey36':  '#5C5C5C',
                          'grey37':  '#5E5E5E',
                          'grey38':  '#616161',
                          'grey39':  '#636363',
                          'grey40':  '#666666',
                          'grey41':  '#696969',
                          'grey42':  '#6B6B6B',
                          'grey43':  '#6E6E6E',
                          'grey44':  '#707070',
                          'grey45':  '#737373',
                          'grey46':  '#757575',
                          'grey47':  '#787878',
                          'grey48':  '#7A7A7A',
                          'grey49':  '#7D7D7D',
                          'grey50':  '#7F7F7F',
                          'grey51':  '#828282',
                          'grey52':  '#858585',
                          'grey53':  '#878787',
                          'grey54':  '#8A8A8A',
                          'grey55':  '#8C8C8C',
                          'grey56':  '#8F8F8F',
                          'grey57':  '#919191',
                          'grey58':  '#949494',
                          'grey59':  '#969696',
                          'grey60':  '#999999',
                          'grey61':  '#9C9C9C',
                          'grey62':  '#9E9E9E',
                          'grey63':  '#A1A1A1',
                          'grey64':  '#A3A3A3',
                          'grey65':  '#A6A6A6',
                          'grey66':  '#A8A8A8',
                          'grey67':  '#ABABAB',
                          'grey68':  '#ADADAD',
                          'grey69':  '#B0B0B0',
                          'grey70':  '#B3B3B3',
                          'grey71':  '#B5B5B5',
                          'grey72':  '#B8B8B8',
                          'grey73':  '#BABABA',
                          'grey74':  '#BDBDBD',
                          'grey75':  '#BFBFBF',
                          'grey76':  '#C2C2C2',
                          'grey77':  '#C4C4C4',
                          'grey78':  '#C7C7C7',
                          'grey79':  '#C9C9C9',
                          'grey80':  '#CCCCCC',
                          'grey81':  '#CFCFCF',
                          'grey82':  '#D1D1D1',
                          'grey83':  '#D4D4D4',
                          'grey84':  '#D6D6D6',
                          'grey85':  '#D9D9D9',
                          'grey86':  '#DBDBDB',
                          'grey87':  '#DEDEDE',
                          'grey88':  '#E0E0E0',
                          'grey89':  '#E3E3E3',
                          'grey90':  '#E5E5E5',
                          'grey91':  '#E8E8E8',
                          'grey92':  '#EBEBEB',
                          'grey93':  '#EDEDED',
                          'grey94':  '#F0F0F0',
                          'grey95':  '#F2F2F2',
                          'grey96':  '#F5F5F5',
                          'grey97':  '#F7F7F7',
                          'grey98':  '#FAFAFA',
                          'grey99':  '#FCFCFC',
                          'grey100':  '#FFFFFF',
                          'honeydew':  '#F0FFF0',
                          'honeydew1':  '#F0FFF0',
                          'honeydew2':  '#E0EEE0',
                          'honeydew3':  '#C1CDC1',
                          'honeydew4':  '#838B83',
                          'hot pink':  '#FF69B4',
                          'HotPink':  '#FF69B4',
                          'HotPink1':  '#FF6EB4',
                          'HotPink2':  '#EE6AA7',
                          'HotPink3':  '#CD6090',
                          'HotPink4':  '#8B3A62',
                          'indian red':  '#CD5C5C',
                          'IndianRed':  '#CD5C5C',
                          'IndianRed1':  '#FF6A6A',
                          'IndianRed2':  '#EE6363',
                          'IndianRed3':  '#CD5555',
                          'IndianRed4':  '#8B3A3A',
                          'ivory':  '#FFFFF0',
                          'ivory1':  '#FFFFF0',
                          'ivory2':  '#EEEEE0',
                          'ivory3':  '#CDCDC1',
                          'ivory4':  '#8B8B83',
                          'khaki':  '#F0E68C',
                          'khaki1':  '#FFF68F',
                          'khaki2':  '#EEE685',
                          'khaki3':  '#CDC673',
                          'khaki4':  '#8B864E',
                          'lavender':  '#E6E6FA',
                          'lavender blush':  '#FFF0F5',
                          'LavenderBlush':  '#FFF0F5',
                          'LavenderBlush1':  '#FFF0F5',
                          'LavenderBlush2':  '#EEE0E5',
                          'LavenderBlush3':  '#CDC1C5',
                          'LavenderBlush4':  '#8B8386',
                          'lawn green':  '#7CFC00',
                          'LawnGreen':  '#7CFC00',
                          'lemon chiffon':  '#FFFACD',
                          'LemonChiffon':  '#FFFACD',
                          'LemonChiffon1':  '#FFFACD',
                          'LemonChiffon2':  '#EEE9BF',
                          'LemonChiffon3':  '#CDC9A5',
                          'LemonChiffon4':  '#8B8970',
                          'light blue':  '#ADD8E6',
                          'light coral':  '#F08080',
                          'light cyan':  '#E0FFFF',
                          'light goldenrod':  '#EEDD82',
                          'light goldenrod yellow': '#FAFAD2',
                          'light gray':  '#D3D3D3',
                          'light green':  '#90EE90',
                          'light grey':  '#D3D3D3',
                          'light pink':  '#FFB6C1',
                          'light salmon':  '#FFA07A',
                          'light sea green':  '#20B2AA',
                          'light sky blue':  '#87CEFA',
                          'light slate blue':  '#8470FF',
                          'light slate gray':  '#778899',
                          'light slate grey':  '#778899',
                          'light steel blue':  '#B0C4DE',
                          'light yellow':  '#FFFFE0',
                          'LightBlue':  '#ADD8E6',
                          'LightBlue1':  '#BFEFFF',
                          'LightBlue2':  '#B2DFEE',
                          'LightBlue3':  '#9AC0CD',
                          'LightBlue4':  '#68838B',
                          'LightCoral':  '#F08080',
                          'LightCyan':  '#E0FFFF',
                          'LightCyan1':  '#E0FFFF',
                          'LightCyan2':  '#D1EEEE',
                          'LightCyan3':  '#B4CDCD',
                          'LightCyan4':  '#7A8B8B',
                          'LightGoldenrod':  '#EEDD82',
                          'LightGoldenrod1':  '#FFEC8B',
                          'LightGoldenrod2':  '#EEDC82',
                          'LightGoldenrod3':  '#CDBE70',
                          'LightGoldenrod4':  '#8B814C',
                          'LightGoldenrodYellow':   '#FAFAD2',
                          'LightGray':  '#D3D3D3',
                          'LightGreen':  '#90EE90',
                          'LightGrey':  '#D3D3D3',
                          'LightPink':  '#FFB6C1',
                          'LightPink1':  '#FFAEB9',
                          'LightPink2':  '#EEA2AD',
                          'LightPink3':  '#CD8C95',
                          'LightPink4':  '#8B5F65',
                          'LightSalmon':  '#FFA07A',
                          'LightSalmon1':  '#FFA07A',
                          'LightSalmon2':  '#EE9572',
                          'LightSalmon3':  '#CD8162',
                          'LightSalmon4':  '#8B5742',
                          'LightSeaGreen':  '#20B2AA',
                          'LightSkyBlue':  '#87CEFA',
                          'LightSkyBlue1':  '#B0E2FF',
                          'LightSkyBlue2':  '#A4D3EE',
                          'LightSkyBlue3':  '#8DB6CD',
                          'LightSkyBlue4':  '#607B8B',
                          'LightSlateBlue':  '#8470FF',
                          'LightSlateGray':  '#778899',
                          'LightSlateGrey':  '#778899',
                          'LightSteelBlue':  '#B0C4DE',
                          'LightSteelBlue1':  '#CAE1FF',
                          'LightSteelBlue2':  '#BCD2EE',
                          'LightSteelBlue3':  '#A2B5CD',
                          'LightSteelBlue4':  '#6E7B8B',
                          'LightYellow':  '#FFFFE0',
                          'LightYellow1':  '#FFFFE0',
                          'LightYellow2':  '#EEEED1',
                          'LightYellow3':  '#CDCDB4',
                          'LightYellow4':  '#8B8B7A',
                          'lime green':  '#32CD32',
                          'LimeGreen':  '#32CD32',
                          'linen':  '#FAF0E6',
                          'magenta':  '#FF00FF',
                          'magenta1':  '#FF00FF',
                          'magenta2':  '#EE00EE',
                          'magenta3':  '#CD00CD',
                          'magenta4':  '#8B008B',
                          'maroon':  '#B03060',
                          'maroon1':  '#FF34B3',
                          'maroon2':  '#EE30A7',
                          'maroon3':  '#CD2990',
                          'maroon4':  '#8B1C62',
                          'medium aquamarine':      '#66CDAA',
                          'medium blue':  '#0000CD',
                          'medium orchid':  '#BA55D3',
                          'medium purple':  '#9370DB',
                          'medium sea green':  '#3CB371',
                          'medium slate blue':      '#7B68EE',
                          'medium spring green':    '#00FA9A',
                          'medium turquoise':  '#48D1CC',
                          'medium violet red':      '#C71585',
                          'MediumAquamarine':  '#66CDAA',
                          'MediumBlue':  '#0000CD',
                          'MediumOrchid':  '#BA55D3',
                          'MediumOrchid1':  '#E066FF',
                          'MediumOrchid2':  '#D15FEE',
                          'MediumOrchid3':  '#B452CD',
                          'MediumOrchid4':  '#7A378B',
                          'MediumPurple':  '#9370DB',
                          'MediumPurple1':  '#AB82FF',
                          'MediumPurple2':  '#9F79EE',
                          'MediumPurple3':  '#8968CD',
                          'MediumPurple4':  '#5D478B',
                          'MediumSeaGreen':  '#3CB371',
                          'MediumSlateBlue':  '#7B68EE',
                          'MediumSpringGreen':      '#00FA9A',
                          'MediumTurquoise':  '#48D1CC',
                          'MediumVioletRed':  '#C71585',
                          'midnight blue':  '#191970',
                          'MidnightBlue':  '#191970',
                          'mint cream':  '#F5FFFA',
                          'MintCream':  '#F5FFFA',
                          'misty rose':  '#FFE4E1',
                          'MistyRose':  '#FFE4E1',
                          'MistyRose1':  '#FFE4E1',
                          'MistyRose2':  '#EED5D2',
                          'MistyRose3':  '#CDB7B5',
                          'MistyRose4':  '#8B7D7B',
                          'moccasin':  '#FFE4B5',
                          'navajo white':  '#FFDEAD',
                          'NavajoWhite':  '#FFDEAD',
                          'NavajoWhite1':  '#FFDEAD',
                          'NavajoWhite2':  '#EECFA1',
                          'NavajoWhite3':  '#CDB38B',
                          'NavajoWhite4':  '#8B795E',
                          'navy':  '#000080',
                          'navy blue':  '#000080',
                          'NavyBlue':  '#000080',
                          'old lace':  '#FDF5E6',
                          'OldLace':  '#FDF5E6',
                          'olive drab':  '#6B8E23',
                          'OliveDrab':  '#6B8E23',
                          'OliveDrab1':  '#C0FF3E',
                          'OliveDrab2':  '#B3EE3A',
                          'OliveDrab3':  '#9ACD32',
                          'OliveDrab4':  '#698B22',
                          'orange':  '#FFA500',
                          'orange red':  '#FF4500',
                          'orange1':  '#FFA500',
                          'orange2':  '#EE9A00',
                          'orange3':  '#CD8500',
                          'orange4':  '#8B5A00',
                          'OrangeRed':  '#FF4500',
                          'OrangeRed1':  '#FF4500',
                          'OrangeRed2':  '#EE4000',
                          'OrangeRed3':  '#CD3700',
                          'OrangeRed4':  '#8B2500',
                          'orchid':  '#DA70D6',
                          'orchid1':  '#FF83FA',
                          'orchid2':  '#EE7AE9',
                          'orchid3':  '#CD69C9',
                          'orchid4':  '#8B4789',
                          'pale goldenrod':  '#EEE8AA',
                          'pale green':  '#98FB98',
                          'pale turquoise':  '#AFEEEE',
                          'pale violet red':  '#DB7093',
                          'PaleGoldenrod':  '#EEE8AA',
                          'PaleGreen':  '#98FB98',
                          'PaleGreen1':  '#9AFF9A',
                          'PaleGreen2':  '#90EE90',
                          'PaleGreen3':  '#7CCD7C',
                          'PaleGreen4':  '#548B54',
                          'PaleTurquoise':  '#AFEEEE',
                          'PaleTurquoise1':  '#BBFFFF',
                          'PaleTurquoise2':  '#AEEEEE',
                          'PaleTurquoise3':  '#96CDCD',
                          'PaleTurquoise4':  '#668B8B',
                          'PaleVioletRed':  '#DB7093',
                          'PaleVioletRed1':  '#FF82AB',
                          'PaleVioletRed2':  '#EE799F',
                          'PaleVioletRed3':  '#CD687F',
                          'PaleVioletRed4':  '#8B475D',
                          'papaya whip':  '#FFEFD5',
                          'PapayaWhip':  '#FFEFD5',
                          'peach puff':  '#FFDAB9',
                          'PeachPuff':  '#FFDAB9',
                          'PeachPuff1':  '#FFDAB9',
                          'PeachPuff2':  '#EECBAD',
                          'PeachPuff3':  '#CDAF95',
                          'PeachPuff4':  '#8B7765',
                          'peru':  '#CD853F',
                          'pink':  '#FFC0CB',
                          'pink1':  '#FFB5C5',
                          'pink2':  '#EEA9B8',
                          'pink3':  '#CD919E',
                          'pink4':  '#8B636C',
                          'plum':  '#DDA0DD',
                          'plum1':  '#FFBBFF',
                          'plum2':  '#EEAEEE',
                          'plum3':  '#CD96CD',
                          'plum4':  '#8B668B',
                          'powder blue':  '#B0E0E6',
                          'PowderBlue':  '#B0E0E6',
                          'purple':  '#A020F0',
                          'purple1':  '#9B30FF',
                          'purple2':  '#912CEE',
                          'purple3':  '#7D26CD',
                          'purple4':  '#551A8B',
                          'red':  '#FF0000',
                          'red1':  '#FF0000',
                          'red2':  '#EE0000',
                          'red3':  '#CD0000',
                          'red4':  '#8B0000',
                          'rosy brown':  '#BC8F8F',
                          'RosyBrown':  '#BC8F8F',
                          'RosyBrown1':  '#FFC1C1',
                          'RosyBrown2':  '#EEB4B4',
                          'RosyBrown3':  '#CD9B9B',
                          'RosyBrown4':  '#8B6969',
                          'royal blue':  '#4169E1',
                          'RoyalBlue':  '#4169E1',
                          'RoyalBlue1':  '#4876FF',
                          'RoyalBlue2':  '#436EEE',
                          'RoyalBlue3':  '#3A5FCD',
                          'RoyalBlue4':  '#27408B',
                          'saddle brown':  '#8B4513',
                          'SaddleBrown':  '#8B4513',
                          'salmon':  '#FA8072',
                          'salmon1':  '#FF8C69',
                          'salmon2':  '#EE8262',
                          'salmon3':  '#CD7054',
                          'salmon4':  '#8B4C39',
                          'sandy brown':  '#F4A460',
                          'SandyBrown':  '#F4A460',
                          'sea green':  '#2E8B57',
                          'SeaGreen':  '#2E8B57',
                          'SeaGreen1':  '#54FF9F',
                          'SeaGreen2':  '#4EEE94',
                          'SeaGreen3':  '#43CD80',
                          'SeaGreen4':  '#2E8B57',
                          'seashell':  '#FFF5EE',
                          'seashell1':  '#FFF5EE',
                          'seashell2':  '#EEE5DE',
                          'seashell3':  '#CDC5BF',
                          'seashell4':  '#8B8682',
                          'sienna':  '#A0522D',
                          'sienna1':  '#FF8247',
                          'sienna2':  '#EE7942',
                          'sienna3':  '#CD6839',
                          'sienna4':  '#8B4726',
                          'sky blue':  '#87CEEB',
                          'SkyBlue':  '#87CEEB',
                          'SkyBlue1':  '#87CEFF',
                          'SkyBlue2':  '#7EC0EE',
                          'SkyBlue3':  '#6CA6CD',
                          'SkyBlue4':  '#4A708B',
                          'slate blue':  '#6A5ACD',
                          'slate gray':  '#708090',
                          'slate grey':  '#708090',
                          'SlateBlue':  '#6A5ACD',
                          'SlateBlue1':  '#836FFF',
                          'SlateBlue2':  '#7A67EE',
                          'SlateBlue3':  '#6959CD',
                          'SlateBlue4':  '#473C8B',
                          'SlateGray':  '#708090',
                          'SlateGray1':  '#C6E2FF',
                          'SlateGray2':  '#B9D3EE',
                          'SlateGray3':  '#9FB6CD',
                          'SlateGray4':  '#6C7B8B',
                          'SlateGrey':  '#708090',
                          'snow':  '#FFFAFA',
                          'snow1':  '#FFFAFA',
                          'snow2':  '#EEE9E9',
                          'snow3':  '#CDC9C9',
                          'snow4':  '#8B8989',
                          'spring green':  '#00FF7F',
                          'SpringGreen':  '#00FF7F',
                          'SpringGreen1':  '#00FF7F',
                          'SpringGreen2':  '#00EE76',
                          'SpringGreen3':  '#00CD66',
                          'SpringGreen4':  '#008B45',
                          'steel blue':  '#4682B4',
                          'SteelBlue':  '#4682B4',
                          'SteelBlue1':  '#63B8FF',
                          'SteelBlue2':  '#5CACEE',
                          'SteelBlue3':  '#4F94CD',
                          'SteelBlue4':  '#36648B',
                          'tan':  '#D2B48C',
                          'tan1':  '#FFA54F',
                          'tan2':  '#EE9A49',
                          'tan3':  '#CD853F',
                          'tan4':  '#8B5A2B',
                          'thistle':  '#D8BFD8',
                          'thistle1':  '#FFE1FF',
                          'thistle2':  '#EED2EE',
                          'thistle3':  '#CDB5CD',
                          'thistle4':  '#8B7B8B',
                          'tomato':  '#FF6347',
                          'tomato1':  '#FF6347',
                          'tomato2':  '#EE5C42',
                          'tomato3':  '#CD4F39',
                          'tomato4':  '#8B3626',
                          'turquoise':  '#40E0D0',
                          'turquoise1':  '#00F5FF',
                          'turquoise2':  '#00E5EE',
                          'turquoise3':  '#00C5CD',
                          'turquoise4':  '#00868B',
                          'violet':  '#EE82EE',
                          'violet red':  '#D02090',
                          'VioletRed':  '#D02090',
                          'VioletRed1':  '#FF3E96',
                          'VioletRed2':  '#EE3A8C',
                          'VioletRed3':  '#CD3278',
                          'VioletRed4':  '#8B2252',
                          'wheat':  '#F5DEB3',
                          'wheat1':  '#FFE7BA',
                          'wheat2':  '#EED8AE',
                          'wheat3':  '#CDBA96',
                          'wheat4':  '#8B7E66',
                          'white':  '#FFFFFF',
                          'white smoke':  '#F5F5F5',
                          'WhiteSmoke':  '#F5F5F5',
                          'yellow':  '#FFFF00',
                          'yellow green':  '#9ACD32',
                          'yellow1':  '#FFFF00',
                          'yellow2':  '#EEEE00',
                          'yellow3':  '#CDCD00',
                          'yellow4':  '#8B8B00',
                          'YellowGreen':  '#9ACD32' }
            hex_to_color = { v: k for k, v in color_map.items( ) }
            color_list = list( color_map.keys( ) )
            COLORS_PER_ROW = 40
            font_size = 9

            def make_window( ):
                layout = [ [ sg.Text( '' ), ],
                           [ sg.Text( f'{ len( color_list ) } Colors', font = self.__themefont ), ],
                           [ sg.Text( ' ', size = ( 5, 1 ) ), ] ]

                for rows in range( len( color_list ) // COLORS_PER_ROW+1 ):
                    row = [ ]

                    for i in range( COLORS_PER_ROW ):
                        try:
                            color = color_list[ rows * COLORS_PER_ROW + i ]
                            row.append( sg.Text( ' ', s = 1, background_color = color, text_color = color, font = self.__themefont , right_click_menu = [ '_', color_map[ color ] ],
                                tooltip = color, enable_events = True, key = ( color, color_map[ color ] ) ) )
                        except IndexError as e:
                            break
                        except Exception as e:
                            sg.popup_error( f'Error while creating color window....', e,
                                f'rows = { rows }  i = { i }' )
                            break
                    layout.append( row )
                layout.append( [ sg.Text( ' ', size = ( 10, 1 ) ), ] )
                layout.append( [ sg.Text( ' ', size = ( 10, 1 ) ), ] )
                layout.append( [ sg.Text( ' ', size = ( 50, 1 ) ), sg.Cancel( size = ( 20, 1 )  ), ] )

                return sg.Window( 'Budget Execution', layout,
                    font = self.__themefont,
                    size = self.__formsize,
                    element_padding = ( 1, 1 ),
                    border_depth = 0,
                    icon = self.__icon,
                    right_click_menu = sg.MENU_RIGHT_CLICK_EDITME_EXIT,
                    use_ttk_buttons = True )

            window = make_window( )

            while True:
                event, values = window.read( )
                if event in ( sg.WIN_CLOSED, 'Cancel', 'Exit' ):
                    break
                if event == 'Edit me':
                    sg.execute_editor( __file__ )
                    continue
                elif isinstance(event, tuple):
                    color, color_hex = event[ 0 ], event[ 1 ]
                else:
                    color, color_hex = hex_to_color[ event ], event

                layout2 = [ [ sg.Text( color_hex + ' on clipboard' ) ],
                           [ sg.DummyButton( color, button_color = self.__buttoncolor, tooltip = color_hex ),
                            sg.DummyButton( color, button_color = self.__buttoncolor, tooltip = color_hex ) ] ]

                window2 = sg.Window( 'Buttons with white and black text', layout2,
                    keep_on_top = True,
                    finalize = True,
                    size = self.__formsize,
                    icon = self.__icon )

                sg.clipboard_set(color_hex)

            window.close()

            sg.popup_quick_message('Building window... one moment please...',
                background_color = self.__themebackground,
                icon = self.__icon,
                text_color = self.__themetextcolor,
                font = self.__themefont )

            sg.set_options( button_element_size = (12, 1),
                element_padding = (0, 0),
                auto_size_buttons = False,
                border_width = 1,
                tooltip_time = 100)
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'ColorDialog'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )



class BudgetForm( Sith ):
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
    __image = None
    __formsize = None
    __themefont = None
    __titleitems = None
    __titlelayout = None
    __headerlayout = None
    __headeritems = None
    __firstitems = None
    __firstlayout = None
    __seconditems = None
    __secondlayout = None
    __thirditems = None
    __thirdlayout = None
    __fourthitems = None
    __fourthlayout = None
    __formlayout = None

    @property
    def titleitems( self ):
        if isinstance( self.__titleitems, list ):
            return self.__titleitems

    @titleitems.setter
    def titleitems( self, value ):
        if isinstance( value, list ):
            self.__titleitems = value

    @property
    def headeritems( self ):
        if isinstance( self.__headeritems, list ):
            return self.__headeritems

    @headeritems.setter
    def headeritems( self, value ):
        if isinstance( value, list) and len( value ) == 3:
            self.__headeritems = value

    @property
    def firstitems( self ):
        if isinstance( self.__firstitems, list ):
            return self.__firstitems

    @firstitems.setter
    def firstitems( self, value ):
        if isinstance( value, list ):
            self.__firstitems = value

    @property
    def seconditems( self ):
        if isinstance( self.__seconditems, list ):
            return self.__seconditems

    @seconditems.setter
    def seconditems( self, value ):
        if isinstance( value, list ):
            self.__seconditems= value

    @property
    def thirditems( self ):
        if isinstance( self.__thirditems, list ):
            return self.__thirditems

    @thirditems.setter
    def thirditems( self, value ):
        if isinstance( value, list ):
            self.__thirditems = value

    @property
    def fourthitems( self ):
        if isinstance( self.__fourthitems, list ):
            return self.__fourthitems

    @fourthitems.setter
    def fourthitems( self, value ):
        if isinstance( value, list ):
            self.__fourthitems = value

    @property
    def formsize( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @formsize.setter
    def formsize( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    @property
    def image( self ):
        if isinstance( self.__image, str ):
            return self.__image

    @image.setter
    def image( self, value ):
        if isinstance( value, str ) and value != '':
            self.__image = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 1200, 650 )
        self.__image = os.getcwd( ) + r'\etc\img\BudgetEx.png'

    def createtitle( self, items ):
        if isinstance( items, list ) and len( items ) == 2:
            try:
                blu = '#051F3D'
                blk = '#101010'
                mblk = '#1E1E1E'
                BPAD_TOP = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT_INSIDE = ( 5, ( 3, 5 ) )
                BPAD_RIGHT = ( ( 5, 10 ), ( 3, 3 ) )
                hdr = 'Roboto 20'
                frmsz = ( 450, 150 )
                hdrsz = ( 920, 100 )
                title = [
                        [ sg.Text( f'{ items[ 0 ] }', font = hdr, background_color = mblk,
                            enable_events = True, grab = False ), sg.Push( background_color = mblk ),
                          sg.Text(f'{ items[ 1 ] }', font = hdr, background_color = mblk ) ],
                ]
                self.__titlelayout = title
                return title
            except Exception as e:
                exc = Error( e )
                exc.module = 'Booger'
                exc.cause = 'BudgetForm'
                exc.method = 'createtitle( self, items )'
                err = ErrorDialog( exc )
                err.show( )

    def createheader( self, items ):
        if isinstance( items, list ) and len( items ) == 3:
            try:
                blu = '#051F3D'
                blk = '#101010'
                mblk = '#1E1E1E'
                BPAD_TOP = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT_INSIDE = ( 5, ( 3, 5 ) )
                BPAD_RIGHT = ( ( 5, 10 ), ( 3, 3 ) )
                hdr = 'Roboto 20'
                frasz = (450, 150)
                hdrsz = ( 920, 100 )
                header = [ [ sg.Push( ), sg.Text( f'{ items[ 0 ] }', font = hdr ), sg.Push( ) ],
                        [ sg.Text( f'{ items[ 1 ] }' ) ],
                        [ sg.Text( f'{ items[ 2 ] }' ) ] ]
                self.__headerlayout = header
                return header
            except Exception as e:
                exc = Error( e )
                exc.module = 'Booger'
                exc.cause = 'BudgetForm'
                exc.method = 'createheader( self, items )'
                err = ErrorDialog( exc )
                err.show( )

    def createfirst( self, items ):
        if isinstance( items, list ) and len( items ) == 7:
            try:
                blu = '#051F3D'
                blk = '#101010'
                mblk = '#1E1E1E'
                BPAD_TOP = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT_INSIDE = ( 5, ( 3, 5 ) )
                BPAD_RIGHT = ( ( 5, 10 ), ( 3, 3 ) )
                hdr = 'Roboto 20'
                frasz = (450, 150)
                hdrsz = ( 920, 100 )
                first = [ [ sg.Push( ), sg.Text( 'Block 1 Header', font = hdr ), sg.Push( ) ],
                           [ sg.Push( ), sg.Text( '' ), sg.Push( ) ],
                           [ sg.Push( ), sg.Text( 'Block 1 line 1', font = li ), sg.Push( ) ],
                           [ sg.Push( ), sg.Text( 'Block 1 line 2', font = li ), sg.Push( ) ],
                           [ sg.Push( ), sg.Text( 'Block 1 line 3', font = li ), sg.Push( ) ],
                           [ sg.Push( ), sg.Text( 'Block 1 line 4', font = li ), sg.Push( ) ],
                           [ sg.Push( ), sg.Text( 'Block 1 line 5', font = li ), sg.Push( ) ],
                           [ sg.Push( ), sg.Text( 'Block 1 line 6', font = li ), sg.Push( ) ] ]
                self.__firstlayout = first
                return first
            except Exception as e:
                exc = Error( e )
                exc.module = 'Booger'
                exc.cause = 'BudgetForm'
                exc.method = 'setfirsttext( self, items )'
                err = ErrorDialog( exc )
                err.show( )

    def createsecond( self, items ):
        if isinstance( items, list ) and len( items ) == 7:
            try:
                blu = '#051F3D'
                blk = '#101010'
                mblk = '#1E1E1E'
                BPAD_TOP = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT_INSIDE = ( 5, ( 3, 5 ) )
                BPAD_RIGHT = ( ( 5, 10 ), ( 3, 3 ) )
                hdr = 'Roboto 20'
                frasz = (450, 150)
                hdrsz = ( 920, 100 )
                second = [ [ sg.Push( ), sg.Text( 'Block 2 Header', font = hdr ), sg.Push( )  ],
                            [ sg.Push( ), sg.Text( '' ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 2 line 1', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 2 line 2', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 2 line 3', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 2 line 4', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 2 line 5', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 2 line 6', font = li ), sg.Push( ) ] ]
                self.__secondlayout = second
                return second
            except Exception as e:
                exc = Error( e )
                exc.module = 'Booger'
                exc.cause = 'BudgetForm'
                exc.method = 'createsecond( self, items )'
                err = ErrorDialog( exc )
                err.show( )

    def createthird( self, items ):
        if isinstance( items, list ) and len( items ) == 7:
            try:
                blu = '#051F3D'
                blk = '#101010'
                mblk = '#1E1E1E'
                BPAD_TOP = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT_INSIDE = ( 5, ( 3, 5 ) )
                BPAD_RIGHT = ( ( 5, 10 ), ( 3, 3 ) )
                hdr = 'Roboto 20'
                frasz = (450, 150)
                hdrsz = ( 920, 100 )
                third = [ [ sg.Push( ), sg.Text( 'Block 3 Header', font = hdr ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( '' ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 3 line 1', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 3 line 2', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 3 line 3', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 3 line 4', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 3 line 5', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 3 line 6', font = li ), sg.Push( ) ] ]
                self.__thirdlayout = third
                return third
            except Exception as e:
                exc = Error( e )
                exc.module = 'Booger'
                exc.cause = 'BudgetForm'
                exc.method = 'setthirdtext( self, items )'
                err = ErrorDialog( exc )
                err.show( )

    def createfourth( self, items  ):
        if isinstance( items, list ) and len( items ) == 7:
            try:
                blu = '#051F3D'
                blk = '#101010'
                mblk = '#1E1E1E'
                BPAD_TOP = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT = ( ( 5, 5 ), ( 5, 5 ) )
                BPAD_LEFT_INSIDE = ( 5, ( 3, 5 ) )
                BPAD_RIGHT = ( ( 5, 10 ), ( 3, 3 ) )
                hdr = 'Roboto 20'
                frasz = (450, 150)
                hdrsz = ( 920, 100 )
                fourth = [ [ sg.Push( ), sg.Text( 'Block 4 Header', font = hdr ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( '' ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 4 line 1', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 4 line 2', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 4 line 3', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 4 line 4', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 4 line 5', font = li ), sg.Push( ) ],
                            [ sg.Push( ), sg.Text( 'Block 4 line 6', font = li ), sg.Push( ) ] ]
                self.__fourthlayout = fourth
                return fourth
            except Exception as e:
                exc = Error( e )
                exc.module = 'Booger'
                exc.cause = 'BudgetForm'
                exc.method = 'createfourth( self, items )'
                err = ErrorDialog( exc )
                err.show( )

    def setlayout( self ):
        try:
            blu = '#051F3D'
            blk = '#101010'
            mblk = '#1E1E1E'
            BPAD_TOP = ( ( 5, 5 ), ( 5, 5 ) )
            BPAD_LEFT = ( ( 5, 5 ), ( 5, 5 ) )
            BPAD_LEFT_INSIDE = ( 5, ( 5, 5 ) )
            BPAD_RIGHT = ( ( 5, 5 ), ( 5, 5 ) )
            hdr = 'Roboto 20'
            li = 'Roboto 10'
            frasz = (450, 150)
            hdrsz = ( 920, 100 )
            layout = [
                    [ sg.Frame( '', self.__titlelayout, pad = ( 0, 0 ), background_color = mblk,
                        expand_x = True,
                        border_width = 0, grab = True ) ],
                    [ sg.Frame( '', self.__headerlayout, size = hdrsz, pad = BPAD_TOP, expand_x = True,
                        relief = sg.RELIEF_FLAT, border_width = 0 ) ],
                    [ sg.Frame( '',
                        [ [ sg.Frame( '', self.__firstlayout, size = frasz, pad = BPAD_LEFT_INSIDE,
                                      border_width = 0, expand_x = True, expand_y = True, ) ],
                          [ sg.Frame( '', self.__thirdlayout, size = frasz, pad = BPAD_LEFT_INSIDE,
                                      border_width = 0, expand_x = True, expand_y = True ) ] ],
                        pad = BPAD_LEFT, background_color = blk, border_width = 0,
                        expand_x = True, expand_y = True ),
                      sg.Frame( '',
                          [ [ sg.Frame( '', self.__secondlayout, size = frasz, pad = BPAD_LEFT_INSIDE,
                                        border_width = 0, expand_x = True, expand_y = True ) ],
                            [ sg.Frame( '', self.__fourthlayout, size = frasz, pad = BPAD_LEFT_INSIDE,
                                        border_width = 0, expand_x = True, expand_y = True ) ] ],
                          pad = BPAD_LEFT, background_color = blk, border_width = 0,
                          expand_x = True, expand_y = True ), ],
                    [ sg.Sizegrip( background_color = mblk ) ] ]
            self.__formlayout = layout
            return layout
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'BudgetForm'
            exc.method = 'setlayout( self, items )'
            err = ErrorDialog( exc )
            err.show( )

    def show( self ):
        try:
            blu = '#051F3D'
            blk = '#101010'
            mblk = '#1E1E1E'
            BPAD_TOP = ( ( 5, 5 ), ( 5, 5 ) )
            BPAD_LEFT = ( ( 5, 5 ), ( 5, 5 ) )
            BPAD_LEFT_INSIDE = ( 5, ( 5, 5 ) )
            BPAD_RIGHT = ( ( 5, 5 ), ( 5, 5 ) )
            hdr = 'Roboto 20'
            li = 'Roboto 10'
            frasz = (450, 150)
            hdrsz = ( 920, 100 )
            self.__titlelayout = [
                    [ sg.Text( 'Budget Execution', font = hdr, background_color = mblk,
                        enable_events = True, grab = False ), sg.Push( background_color = mblk ),
                      sg.Text( 'Wednesday 27 Oct 2021', font = hdr, background_color = mblk ) ],
            ]
            self.__headerlayout = [ [ sg.Push( ), sg.Text( 'Top Header', font = hdr ), sg.Push( ) ],
                                    [ sg.Image( source = self.__image, subsample = 3,
                                        enable_events = True ), sg.Push( ) ],
                                    [ sg.Text( 'Top Header line 2' ), sg.Push( )  ] ]
            self.__firstlayout = [ [ sg.Push( ), sg.Text( 'Block 1 Header', font = hdr ), sg.Push( ) ],
                                   [ sg.Push( ), sg.Text( '' ), sg.Push( ) ],
                                   [ sg.Push( ), sg.Text( 'Block 1 line 1', font = li ), sg.Push( ) ],
                                   [ sg.Push( ), sg.Text( 'Block 1 line 2', font = li ), sg.Push( ) ],
                                   [ sg.Push( ), sg.Text( 'Block 1 line 3', font = li ), sg.Push( ) ],
                                   [ sg.Push( ), sg.Text( 'Block 1 line 4', font = li ), sg.Push( ) ],
                                   [ sg.Push( ), sg.Text( 'Block 1 line 5', font = li ), sg.Push( ) ],
                                   [ sg.Push( ), sg.Text( 'Block 1 line 6', font = li ), sg.Push( ) ] ]
            self.__secondlayout = [ [ sg.Push( ), sg.Text( 'Block 2 Header', font = hdr ), sg.Push( )  ],
                                    [ sg.Push( ), sg.Text( '' ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 2 line 1', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 2 line 2', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 2 line 3', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 2 line 4', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 2 line 5', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 2 line 6', font = li ), sg.Push( ) ] ]
            self.__thirdlayout = [ [ sg.Push( ), sg.Text( 'Block 3 Header', font = hdr ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( '' ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 3 line 1', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 3 line 2', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 3 line 3', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 3 line 4', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 3 line 5', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 3 line 6', font = li ), sg.Push( ) ] ]
            self.__fourthlayout = [ [ sg.Push( ), sg.Text( 'Block 4 Header', font = hdr ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( '' ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 4 line 1', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 4 line 2', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 4 line 3', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 4 line 4', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 4 line 5', font = li ), sg.Push( ) ],
                                    [ sg.Push( ), sg.Text( 'Block 4 line 6', font = li ), sg.Push( ) ] ]
            self.__formlayout = [
                    [ sg.Frame( '', self.__titlelayout, pad = ( 0, 0 ), background_color = mblk,
                        expand_x = True, border_width = 0, grab = True ) ],
                    [ sg.Frame( '',
                        [ [ sg.Frame( '', self.__headerlayout, size = frasz, pad = BPAD_TOP, expand_x = True,
                                      relief = sg.RELIEF_FLAT, border_width = 0 ) ] ],
                        pad = BPAD_LEFT, background_color = blu, border_width = 0,
                        expand_x = True, expand_y = False ),  ],
                    [ sg.Frame( '',
                        [ [ sg.Frame( '', self.__firstlayout, size = frasz, pad = BPAD_LEFT_INSIDE,
                                      border_width = 0, expand_x = True, expand_y = True, ) ],
                          [ sg.Frame( '', self.__thirdlayout, size = frasz, pad = BPAD_LEFT_INSIDE,
                                      border_width = 0, expand_x = True, expand_y = True ) ] ],
                        pad = BPAD_LEFT, background_color = blu, border_width = 0,
                        expand_x = True, expand_y = True ),
                      sg.Frame( '',
                          [ [ sg.Frame( '', self.__secondlayout, size = frasz, pad = BPAD_LEFT_INSIDE,
                                        border_width = 0, expand_x = True, expand_y = True ) ],
                            [ sg.Frame( '', self.__fourthlayout, size = frasz, pad = BPAD_LEFT_INSIDE,
                                        border_width = 0, expand_x = True, expand_y = True ) ] ],
                          pad = BPAD_LEFT, background_color = blu, border_width = 0,
                          expand_x = True, expand_y = True ), ],
                    [ sg.Sizegrip( background_color = mblk ) ] ]
            window = sg.Window( '    Budget Execution', self.__formlayout,
                size = self.__formsize,
                margins = (0, 0),
                background_color = blk,
                grab_anywhere = True,
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
                    sg.popup_scrolled( sg.get_versions( ), keep_on_top = True )
                elif event == 'File Location':
                    sg.popup_scrolled( 'This Python file is:', __file__ )
            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'BudgetForm'
            exc.method = 'show( self)'
            err = ErrorDialog( exc )
            err.show( )



class ChartPanel( Sith ):
    ''' Provides form with a bar chart '''
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
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( ).__init__( )
        sg.theme( 'DarkGrey15')
        self.__icon = super( ).iconpath
        self.__formsize = ( 700, 600 )

    def show( self ):
        try:
            sm = ( 10, 1 )
            md = ( 15, 1 )
            lg = ( 20, 1 )
            xl = ( 100, 1 )
            width = 50
            space = 75
            offset = 3
            graphsz = datasz = ( 500, 500 )
            black = sg.theme_background_color( )

            layout = [ [ sg.Text( '', size = sm ), sg.Text( '', size = xl ) ],
                       [ sg.Text( '', size = sm ), sg.Graph( graphsz, ( 0, 0 ), datasz, k = '-GRAPH-' ) ],
                       [ sg.Text( '', size = sm ), sg.Text( '', size = xl ) ],
                       [ sg.Text( '', size = lg ), sg.Button( 'Next', size = md ),
                         sg.Text( '', size = lg ), sg.Exit( size = md ) ],
                       [ sg.Sizegrip( background_color = black ) ] ]

            window = sg.Window( 'Budget Execution', layout,
                finalize = True,
                resizable = True,
                icon = self.__icon,
                font = self.__themefont,
                size = self.__formsize )

            graph = window[ '-GRAPH-' ]

            while True:
                graph.erase( )
                for i in range( 7 ):
                    item = random.randint( 0, graphsz[ 1 ] )
                    graph.draw_rectangle( top_left = ( i * space + offset, item ),
                        bottom_right = (i * space + offset + width, 0),
                        fill_color = sg.theme_button_color_background( ),
                        line_color = sg.theme_button_color_text( ) )

                    graph.draw_text( text = item, color = '#FFFFFF',
                        location = (i * space + offset + 25, item + 10) )

                event, values = window.read( )
                if event in ( sg.WIN_CLOSED, 'Exit' ):
                    break

            window.close( )
        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'ChartForm'
            exc.method = 'show( self)'
            err = ErrorDialog( exc )
            err.show( )



class CsvForm( Sith ):
    '''Provides form that reads CSV file with pandas'''
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
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 800, 600 )

    def show( self ):
        try:
            fd = FileDialog( )
            fd.show( )
            filename = fd.selectedpath

            if filename == '':
                msg = MessageDialog( 'No file path was provided!')
                msg.show( )
                return

            data = [ ]
            header_list = [ ]

            button = sg.popup_yes_no( 'Does file have column names?',
                icon = self.__icon,
                font = self.__themefont )

            if filename is not None:
                try:
                    df = CsvReader( filename, sep = ',', engine = 'python', header = None )
                    data = df.values.tolist( )
                    if button == 'Yes':
                        header_list = df.iloc[ 0 ].tolist( )
                        data = df[ 1: ].values.tolist( )
                    elif button == 'No':
                        header_list = [ 'Column' + str( x ) for x in range( len( data[ 0 ] ) ) ]
                except:
                    sg.popup_error( 'Error reading file' )
                    return

            datagrid = [ [ sg.Text( '', size = (100, 5) ) ],
                         [ sg.Text( '', size = (5, 1) ),
                              sg.Table( values = data,
                                  headings = header_list,
                                  display_row_numbers = True,
                                  vertical_scroll_only = False,
                                  header_background_color = '#1B262E',
                                  def_col_width = 12,
                                  header_border_width = 2,
                                  selected_row_colors = ('#FFFFFF', '#2A4457'),
                                  header_text_color = '#FFFFFF',
                                  header_font = ('Roboto', 10),
                                  background_color = '#000000',
                                  auto_size_columns = False,
                                  border_width = 1,
                                  sbar_relief = sg.RELIEF_FLAT,
                                  num_rows = min( 40, len( data ) ) ),
                              sg.Text( '', size = (5, 1) ) ],
                         [ sg.Text( '', size = (100, 3) ) ] ]

            window = sg.Window( '  Budget Execution', datagrid,
                grab_anywhere = False,
                icon = self.__icon,
                font = self.__themefont,
                resizable = True )

            event, values = window.read( )

            window.close( )

        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'CsvForm'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )



class ExcelForm( Sith ):
    '''Provides form that reads CSV file with pandas'''
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
    def size( self ):
        if isinstance( self.__formsize, tuple ) :
            return self.__formsize

    @size.setter
    def size( self, value ):
        if isinstance( value, tuple ) :
            self.__formsize = value

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 1200, 650 )

    def show( self ):
        try:
            fd = FileDialog( )
            fd.show( )
            filename = fd.selectedpath

            if filename == '':
                msg = MessageDialog( 'No file was provided!' )
                msg.show( )
                return

            data = [ ]
            header_list = [ ]

            button = sg.popup_yes_no( 'First row has column headers?',
                title = 'Headers?',
                icon = self.__icon,
                font = ( 'Roboto', 10 ) )

            if filename is not None:
                try:
                    df = ExcelReader( filename,  index_col = 0 )
                    data = df.values.tolist( )
                    if button == 'Yes':
                        header_list = [ f'{ i } ' for i in df.columns ]
                    elif button == 'No':
                        header_list = [ 'Column - ' + str( x ) for x in range( len( data[ 0 ] ) ) ]

                except:
                    sg.popup_error( 'Error reading file' )
                    return

            left = [ [ sg.Text( '', size = ( 3, 1 ) ), ] ]
            right = [ [ sg.Text( '', size = ( 3, 1 ) ), ] ]
            datagrid = [ [ sg.Table( values = data,
                               headings = header_list,
                               justification = 'left',
                               row_height = '18',
                               display_row_numbers = True,
                               vertical_scroll_only = False,
                               header_background_color = '#1B262E',
                               header_relief = sg.RELIEF_FLAT,
                               def_col_width = 12,
                               header_border_width = 1,
                               selected_row_colors = ( '#FFFFFF', '#4682B4' ),
                               header_text_color = '#FFFFFF',
                               header_font = ( 'Roboto', 8 ),
                               font = ( 'Roboto', 8 ),
                               background_color = '#EDF3F8',
                               alternating_row_color = '#EDF3F8',
                               auto_size_columns = False,
                               border_width = 1,
                               text_color = '#000000',
                               sbar_relief = sg.RELIEF_FLAT,
                               num_rows = min( 26, len( data ) ) ), ], ]

            layout = [ [ sg.Text( '', size = ( 3, 3 ) ) ],
                       [ sg.Column( datagrid, ), sg.Column( right ) ],
                       [ sg.Text( '', size = (3, 1) ) ],
                       [ sg.Text( '', size = (10, 1) ), sg.Button( 'Open', size = (15, 1), key = '-OPEN-' ),
                         sg.Text( '', size = (25, 1) ), sg.Button( 'Export', size = (15, 1), key = '-EXPORT-' ),
                         sg.Text( '', size = (25, 1) ), sg.Button( 'Save', size = (15, 1), key = '-SAVE-' ),
                         sg.Text( '', size = (25, 1) ), sg.Button( 'Close', size = (15, 1), key = '-CLOSE-' ) ],
                       [ sg.Sizegrip( ) ], ]

            window = sg.Window( '  Budget Execution', layout,
                size = self.__formsize,
                grab_anywhere = True,
                icon = self.__icon,
                font = self.__themefont,
                resizable = True,
                right_click_menu = sg.MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT )

            event, values = window.read( )
            while True:
                if event in ( sg.WIN_X_EVENT, '-CLOSE-' ):
                    break
                if event in ('-OPEN-', '-EXPORT-', '-SAVE-', 'Save' ):
                    info = 'Not Yet Implemented!'
                    msg = MessageDialog( info )
                    msg.show()
                    break

            window.close( )

        except Exception as e:
            exc = Error( e )
            exc.module = 'Booger'
            exc.cause = 'ExcelForm'
            exc.method = 'show( self )'
            err = ErrorDialog( exc )
            err.show( )



class GraphForm( Sith ):
    '''Provides form that reads CSV file with pandas'''
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

    def __init__( self ):
        super( ).__init__( )
        self.__themebackground = super( ).themebackground
        self.__themefont = super( ).themefont
        self.__icon = super( ).iconpath
        self.__elementbackcolor = super( ).elementbackcolor
        self.__elementforecolor = super( ).elementforecolor
        self.__themetextcolor = super( ).textforecolor
        self.__textbackcolor = super( ).textbackcolor
        self.__inputbackcolor = super( ).inputbackcolor
        self.__inputforecolor = super( ).inputforecolor
        self.__buttoncolor = super( ).buttoncolor
        self.__formsize = ( 800, 600 )

    def show( self ):
        def create_axis_grid( ):
            plt.close( 'all' )

            def get_demo_image( ):
                delta = 0.5
                extent = (-3, 4, -4, 3)
                x = np.arange( -3.0, 4.001, delta )
                y = np.arange( -4.0, 3.001, delta )
                X, Y = np.meshgrid( x, y )
                Z1 = np.exp( -X ** 2 - Y ** 2 )
                Z2 = np.exp( -( X - 1 ) ** 2 - ( Y - 1 ) ** 2 )
                Z = (Z1 - Z2) * 2

                return Z, extent

            def get_rgb( ):
                Z, extent = get_demo_image( )

                Z[ Z < 0 ] = 0.
                Z = Z / Z.max( )

                R = Z[ :13, :13 ]
                G = Z[ 2:, 2: ]
                B = Z[ :13, 2: ]

                return R, G, B

            fig = plt.figure( 1 )
            ax = RGBAxes( fig, [ 0.1, 0.1, 0.8, 0.8 ] )

            r, g, b = get_rgb( )
            kwargs = dict( origin = "lower", interpolation = "nearest" )
            ax.imshow_rgb( r, g, b, **kwargs )

            ax.RGB.set_xlim( 0., 9.5 )
            ax.RGB.set_ylim( 0.9, 10.6 )

            plt.draw( )
            return plt.gcf( )

        def create_figure( ):
            fig = matplotlib.figure.Figure( figsize = ( 5, 4 ), dpi = 100 )
            t = np.arange( 0, 3, .01 )
            fig.add_subplot( 111 ).plot( t, 2 * np.sin( 2 * np.pi * t ) )
            return fig

        def create_subplot_3d( ):
            fig = plt.figure( )
            ax = fig.add_subplot( 1, 2, 1, projection = '3d' )
            X = np.arange( -5, 5, 0.25 )
            Y = np.arange( -5, 5, 0.25 )
            X, Y = np.meshgrid( X, Y )
            R = np.sqrt( X ** 2 + Y ** 2 )
            Z = np.sin( R )
            surf = ax.plot_surface( X, Y, Z, rstride = 1, cstride = 1, cmap = cm.jet,
                linewidth = 0, antialiased = False )

            ax.set_zlim3d( -1.01, 1.01 )
            fig.colorbar( surf, shrink = 0.5, aspect = 5 )
            ax = fig.add_subplot( 1, 2, 2, projection = '3d' )
            X, Y, Z = get_test_data( 0.05 )
            ax.plot_wireframe( X, Y, Z, rstride = 10, cstride = 10 )
            return fig

        def create_pyplot_scales( ):
            plt.close( 'all' )
            np.random.seed( 19680801 )

            y = np.random.normal( loc = 0.5, scale = 0.4, size = 1000 )
            y = y[ (y > 0) & (y < 1) ]
            y.sort( )
            x = np.arange( len( y ) )

            # plot with various axes scales
            plt.figure( 1 )

            # linear
            plt.subplot( 221 )
            plt.plot( x, y )
            plt.yscale( 'linear' )
            plt.title( 'linear' )
            plt.grid( True )

            # log
            plt.subplot( 222 )
            plt.plot( x, y )
            plt.yscale( 'log' )
            plt.title( 'log' )
            plt.grid( True )

            # symmetric log
            plt.subplot( 223 )
            plt.plot( x, y - y.mean( ) )
            plt.yscale( 'symlog', linthreshy = 0.01 )
            plt.title( 'symlog' )
            plt.grid( True )

            # logit
            plt.subplot( 224 )
            plt.plot( x, y )
            plt.yscale( 'logit' )
            plt.title( 'logit' )
            plt.grid( True )
            plt.gca( ).yaxis.set_minor_formatter( NullFormatter( ) )
            plt.subplots_adjust( top = 0.92, bottom = 0.08, left = 0.10, right = 0.95,
                hspace = 0.25,
                wspace = 0.35 )

            return plt.gcf( )

        def draw_figure( element, figure ):
            plt.close( 'all' )
            canv = FigureCanvasAgg( figure )
            buf = io.BytesIO( )
            canv.print_figure( buf, format = 'png' )
            if buf is None:
                return None
            buf.seek( 0 )
            element.update( data = buf.read( ) )
            return canv

        figures = {
                'Axis Grid':    create_axis_grid,
                'Subplot 3D':   create_subplot_3d,
                'Scales':       create_pyplot_scales,
                'Basic Figure': create_figure }

        def create_window( ):
            left_col = [ [ sg.T( 'Figures to Draw' ) ],
                         [ sg.Listbox( list( figures ),
                             default_values = [ list( figures )[ 0 ] ], size = (15, 5),
                             key = '-LB-' ) ],
                         [ sg.T( 'Matplotlib Styles' ) ],
                         [ sg.Combo( plt.style.available, size = (15, 10), key = '-STYLE-' ) ],
                         [ sg.T( 'PySimpleGUI Themes' ) ],
                         [ sg.Combo( sg.theme_list( ), default_value = sg.theme( ), size = (15, 10),
                             key = '-THEME-' ) ] ]

            layout = [ [ sg.T( 'Matplotlib Example', font = 'Any 20' ) ],
                       [ sg.Col( left_col ), sg.Image( key = '-IMAGE-' ) ],
                       [ sg.B( 'Draw' ), sg.B( 'Exit' ) ] ]

            window = sg.Window( 'Matplotlib Embedded Template', layout, finalize = True )

            return window

        window = create_window( )

        while True:
            event, values = window.read( )
            print( event, values )
            if event == 'Exit' or event == sg.WIN_CLOSED:
                break
            if event == 'Draw':
                if values[ '-THEME-' ] != sg.theme( ):
                    window.close( )
                    sg.theme( values[ '-THEME-' ] )
                    window = create_window( )

                if values[ '-LB-' ]:
                    func = figures[ values[ '-LB-' ][ 0 ] ]
                    if values[ '-STYLE-' ]:
                        plt.style.use( values[ '-STYLE-' ] )

                    draw_figure( window[ '-IMAGE-' ], func( ) )

        window.close( )