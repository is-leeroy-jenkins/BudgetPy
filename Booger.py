'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                Booger.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Booger.py" company="Terry D. Eppler">

     This is a Federal Budget, Finance, and Accounting application.
     Copyright ©  2023  Terry Eppler

     Permission is hereby granted, free of charge, to any person obtaining a copy
     of this software and associated documentation files (the “Software”),
     to deal in the Software without restriction,
     including without limitation the rights to use,
     copy, modify, merge, publish, distribute, sublicense,
     and/or sell copies of the Software,
     and to permit persons to whom the Software is furnished to do so,
     subject to the following conditions:

     The above copyright notice and this permission notice shall be included in all
     copies or substantial portions of the Software.

     THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
     INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
     FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT.
     IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
     DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
     ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
     DEALINGS IN THE SOFTWARE.

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    Booger.py
  </summary>
  ******************************************************************************************
  '''
import base64
import webbrowser
from typing import Type

#import fitz
from PIL import Image, ImageTk, ImageSequence
import PySimpleGUI as sg
from enum import Enum
import os
from sys import exit, exc_info
import random
import io
from googlesearch import search
from Minion import App
import traceback
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
from Static import EXT, Client

class Error( Exception ):
	'''
    Constructor:
    Error( exception: Exception, heading: str = '', cause: str = '',
                  method: str = '', module: str = '' )

    Purpose:
    Class wrapping exception used as the input argument for ErrorDialog class
    '''
	__class = None
	__module = None
	__method = None
	__heading = None
	__type = None
	__trace = None
	__info = None

	@property
	def message( self ) -> str:
		if self.__heading is not None:
			return self.__heading

	@message.setter
	def message( self, value: str ):
		if value is not None:
			self.__heading = value

	@property
	def cause( self ) -> str:
		if self.__class is not None:
			return self.__class

	@cause.setter
	def cause( self, value: str ):
		if value is not None:
			self.__class = value

	@property
	def method( self ) -> str:
		if self.__method is not None:
			return self.__method

	@method.setter
	def method( self, value: str ):
		if value is not None:
			self.__method = value

	@property
	def module( self ) -> str:
		if self.__module is not None:
			return self.__module

	@module.setter
	def module( self, value: str ):
		if value is not None:
			self.__module = value

	@property
	def type( self ) -> Type[ BaseException ]:
		if self.__type is not None:
			return self.__type

	@type.setter
	def type( self, value: Type[ BaseException ] ):
		if value is not None:
			self.__type = value

	@property
	def stack_trace( self ) -> str:
		if self.__trace is not None:
			return self.__trace

	@stack_trace.setter
	def stack_trace( self, value: str ):
		if value is not None:
			self.__trace = value

	@property
	def info( self ) -> str:
		if self.__class is not None:
			return self.__class

	@info.setter
	def info( self, value: str ):
		if value is not None:
			self.__class = value

	def __init__( self, exception: Exception, heading: str = '', cause: str = '',
	              method: str = '', module: str = '' ):
		super( ).__init__( )
		self.__heading = heading
		self.__class = cause
		self.__method = method
		self.__module = module
		self.__type = exc_info( )[ 0 ]
		self.__trace = traceback.format_exc( )
		self.__info = str( exc_info( )[ 0 ] ) + ': \r\n \r\n' + traceback.format_exc( )

	def __str__( self ) -> str:
		if self.__info is not None:
			return self.__info

class ButtonIcon( ):
	'''
    Constructor:
    ButtonIcon( png: Enum )

    Pupose:
    Class representing form images
    '''
	__button = None
	__name = None
	__filepath = None

	@property
	def folder( self ) -> str:
		if self.__button is not None:
			return self.__button

	@folder.setter
	def folder( self, value: str ):
		if value is not None:
			self.__button = value

	@property
	def name( self ) -> str:
		if self.__name is not None:
			return self.__name

	@name.setter
	def name( self, value: str ):
		if value is not None:
			self.__name = value

	@property
	def file_path( self ) -> str:
		if self.__filepath is not None:
			return self.__filepath

	@file_path.setter
	def file_path( self, value: str ):
		if value is not None:
			self.__filepath = value

	def __init__( self, png: Enum ):
		self.__name = png.name
		self.__button = os.getcwd( ) + r'\etc\img\button'
		self.__filepath = self.__button + r'\\' + self.__name + '.png'

	def __str__( self ) -> str:
		if self.__filepath is not None:
			return self.__filepath

class TitleIcon( ):
	'''
	Construcotr:
	TitleIcon( ico )

	Purpose:
	Class used to define the TitleIcon used on the GUI
	'''
	__folder = None
	__name = None
	__filepath = None

	@property
	def folder( self ) -> str:
		if self.__button is not None:
			return self.__button

	@folder.setter
	def folder( self, value: str ):
		if value is not None:
			self.__button = value

	@property
	def name( self ) -> str:
		if self.__name is not None:
			return self.__name

	@name.setter
	def name( self, value: str ):
		if isinstance( value, str ):
			self.__name = value

	@property
	def file_path( self ) -> str:
		if self.__filepath is not None:
			return self.__filepath

	@file_path.setter
	def file_path( self, value: str ):
		if value is not None:
			self.__filepath = value

	def __init__( self, ico ):
		self.__name = ico.name
		self.__folder = os.getcwd( ) + r'etc\ico'
		self.__filepath = self.__folder + r'\\' + self.__name + r'.ico'

	def __str__( self ) -> str:
		if self.__filepath is not None:
			return self.__filepath

class Sith( ):
	'''
	Construcotr:
	Sith( )

	Purpose:
	Base class for the dark-mode controls
	'''
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
	def size( self ) -> (int, int):
		if self.__formsize is not None:
			return self.__formsize

	@size.setter
	def size( self, value: (int, int) ):
		if value is not None:
			self.__formsize = value

	@property
	def settings_path( self ) -> str:
		if self.__settingspath is not None:
			return self.__settingspath

	@settings_path.setter
	def settings_path( self, value: str ):
		'''Sets the size property'''
		if value is not None:
			self.__settingspath = value

	@property
	def theme_background( self ) -> str:
		if self.__themebackground is not None:
			return self.__themebackground

	@theme_background.setter
	def theme_background( self, value: str ):
		if value is not None:
			self.__themebackground = value

	@property
	def theme_textcolor( self ) -> str:
		if self.__themetextcolor is not None:
			return self.__themetextcolor

	@theme_textcolor.setter
	def theme_textcolor( self, value: str ):
		if value is not None:
			self.__themetextcolor = value

	@property
	def element_backcolor( self ) -> str:
		if self.__elementbackcolor is not None:
			return self.__elementbackcolor

	@element_backcolor.setter
	def element_backcolor( self, value: str ):
		if value is not None:
			self.__elementbackcolor = value

	@property
	def element_forecolor( self ) -> str:
		if self.__elementforecolor is not None:
			return self.__elementforecolor

	@element_forecolor.setter
	def element_forecolor( self, value: str ):
		if value is not None:
			self.__elementforecolor = value

	@property
	def text_forecolor( self ) -> str:
		if self.__themetextcolor is not None:
			return self.__themetextcolor

	@text_forecolor.setter
	def text_forecolor( self, value: str ):
		if value is not None:
			self.__themetextcolor = value

	@property
	def text_backcolor( self ) -> str:
		if self.__textbackcolor is not None:
			return self.__textbackcolor

	@text_backcolor.setter
	def text_backcolor( self, value: str ):
		if value is not None:
			self.__textbackcolor = value

	@property
	def input_backcolor( self ) -> str:
		if self.__inputbackcolor is not None:
			return self.__inputbackcolor

	@input_backcolor.setter
	def input_backcolor( self, value: str ):
		if value is not None:
			self.__inputbackcolor = value

	@property
	def input_forecolor( self ) -> str:
		if self.__inputforecolor is not None:
			return self.__inputforecolor

	@input_forecolor.setter
	def input_forecolor( self, value: str ):
		if value is not None:
			self.__inputforecolor = value

	@property
	def button_color( self ) -> (str, str):
		if self.__buttoncolor is not None:
			return self.__buttoncolor

	@button_color.setter
	def button_color( self, value: (str, str) ):
		if value is not None:
			self.__buttoncolor = value

	@property
	def button_backcolor( self ) -> str:
		if self.__buttonbackcolor is not None:
			return self.__buttonbackcolor

	@button_backcolor.setter
	def button_backcolor( self, value: str ):
		if value is not None:
			self.__buttonbackcolor = value

	@property
	def button_forecolor( self ) -> str:
		if self.__buttonforecolor is not None:
			return self.__buttonforecolor

	@button_forecolor.setter
	def button_forecolor( self, value: str ):
		if value is not None:
			self.__buttonforecolor = value

	@property
	def icon_path( self ) -> str:
		if self.__icon is not None:
			return self.__icon

	@icon_path.setter
	def icon_path( self, value: str ):
		if value is not None:
			self.__icon = value

	@property
	def theme_font( self ) -> (str, int):
		if self.__themefont is not None:
			return self.__themefont

	@theme_font.setter
	def theme_font( self, value: (str, int) ):
		if value is not None:
			self.__themefont = value

	@property
	def scrollbar_color( self ) -> str:
		if self.__scrollbarcolor is not None:
			return self.__scrollbarcolor

	@scrollbar_color.setter
	def scrollbar_color( self, value: str ):
		if value is not None:
			self.__scrollbarcolor = value

	@property
	def progressbar_color( self ) -> (str, str):
		if self.__progressbarcolor is not None:
			return self.__progressbarcolor

	@progressbar_color.setter
	def progressbar_color( self, value: (str, str) ):
		if value is not None:
			self.__progressbarcolor = value

	def __init__( self ):
		sg.theme( 'DarkGrey15' )
		sg.theme_input_text_color( '#FFFFFF' )
		sg.theme_element_text_color( '#69B1EF' )
		sg.theme_text_color( '#69B1EF' )
		self.__themebackground = sg.theme_background_color( )
		self.__themetextcolor = sg.theme_text_color( )
		self.__elementbackcolor = sg.theme_text_element_background_color( )
		self.__elementforecolor = sg.theme_element_text_color( )
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
		self.__progressbarcolor = sg.theme_progress_bar_color( )
		self.__formsize = ( 400, 200 )
		self.__settingspath = os.getcwd( ) + r'\etc\theme'
		sg.set_global_icon( icon = self.__icon )
		sg.set_options( font = self.__themefont )
		sg.user_settings_save( 'Budget', self.__settingspath )

class FileDialog( Sith ):
	'''
	Construcotr:
	FileDialog( )

	Purpose:
	Class that handles filenames a file
	'''
	__selecteditem = None
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
	def selected_path( self ) -> str:
		if self.__selecteditem is not None:
			return self.__selecteditem

	@selected_path.setter
	def selected_path( self, value: str ):
		if value is not None:
			self.__selecteditem = value

	@property
	def message( self ) -> str:
		if self.__message is not None:
			return self.__message

	@message.setter
	def message( self, value: str ):
		if value is not None:
			self.__message = value

	def __init__( self, extension = EXT.XLSX ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = ( 475, 250 )
		self.__selecteditem = None
		self.__message = 'Search for File'
		self.__extension = extension if isinstance( extension, EXT ) else EXT.XLSX
		self.__excel = ( ( 'Excel Files', '*.xlsx' ), )
		self.__csv = ( ( 'CSV Files', '*.csv' ), )
		self.__pdf = ( ( 'PDF Files', '*.pdf' ), )
		self.__sql = ( ( 'SQL Files', '*.sqlstatement', ), )
		self.__text = ( ( 'Text Files', '*.txt' ), )
		self.__access = ( ( 'MS ACCDB Databases', '*.accdb' ), )
		self.__sqlite = ( ( 'SQLite Databases', '*.db' ), )
		self.__sqlserver = ( ( 'SQL Server Databases', '*.mdf', '*.ldf', '*.sdf' ), )

	def __str__( self ) -> str:
		if self.__selecteditem is not None:
			return self.__selecteditem

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_layout = [ [ sg.Text( ) ],
			            [ sg.Text( self.__message, font = ( 'Roboto', 11 ) ) ],
			            [ sg.Text( ) ],
			            [ sg.Input( key = '-PATH-' ), sg.FileBrowse( size = ( 15, 1 ) ) ],
			            [ sg.Text( ) ],
			            [ sg.Text( ) ],
			            [ sg.OK( size = ( 8, 1 ), ), sg.Cancel( size = ( 10, 1 ) ) ] ]

			_window = sg.Window( ' Budget Execution', _layout,
				font = self.__themefont,
				size = self.__formsize )

			while True:
				_event, _values = _window.read( )
				if _event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel' ):
					break
				elif _event == 'OK':
					self.__selecteditem = _values[ '-PATH-' ]
					_window.close( )

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'FileDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class FolderDialog( Sith ):
	'''
	Construcotr:
	FolderDialog( )

	Purpose:
	Class defining dialog used to select a directory path
	'''
	__selecteditem = None

	@property
	def selected_path( self ) -> str:
		if self.__selecteditem is not None:
			return self.__selecteditem

	@selected_path.setter
	def selected_path( self, value: str ):
		if value is not None:
			self.__selecteditem = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = ( 475, 250 )
		self.__selecteditem = None

	def __str__( self ) -> str:
		if isinstance( self.__selecteditem, str ):
			return self.__selecteditem

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_layout = [ [ sg.Text( ) ],
			            [ sg.Text( 'Search for Directory' ) ],
			            [ sg.Text( ) ],
			            [ sg.Input( key = '-PATH-' ), sg.FolderBrowse( size = ( 15, 1 ) ) ],
			            [ sg.Text( size = ( 100, 1 ) ) ],
			            [ sg.Text( size = ( 100, 1 ) ) ],
			            [ sg.OK( size = ( 8, 1 ) ), sg.Cancel( size = ( 10, 1 ) ) ] ]

			_window = sg.Window( '  Budget Execution', _layout,
				font = self.__themefont,
				size = self.__formsize )

			while True:
				_event, _values = _window.read( )
				if _event in (sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel'):
					break
				elif _event == 'OK':
					self.__selecteditem = _values[ '-PATH-' ]
					sg.popup_ok( self.__selecteditem,
						title = 'Results',
						icon = self.__icon,
						font = self.__themefont )

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.cause = 'FolderDialog'
			_exc.method = 'show( self )'
			_error = ErrorDialog( _exc )
			_error.show( )

class SaveFileDialog( Sith ):
	'''
	Constructor:
	SaveFileDialog( path = '' ):

    Purpose:
    Class define object that provides a dialog to locate file destinations
    '''
	__original = None
	__filename = None

	@property
	def original( self ) -> str:
		if self.__original is not None:
			return self.__original

	@original.setter
	def original( self, value: str ):
		if value is not None:
			self.__original = value

	@property
	def file_name( self ) -> str:
		if self.__filename is not None:
			return self.__filename

	@file_name.setter
	def file_name( self, value: str ):
		if value is not None:
			self.__filename = value

	def __init__( self, path = '' ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = ( 400, 250 )
		self.__original = path

	def __str__( self ) -> str:
		if self.__filename is not None:
			return self.__filename

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_username = os.environ.get( 'USERNAME' )
			_filename = sg.popup_get_file( 'Select Location / Enter File Name',
				title = '  Budget Execution',
				font = self.__themefont,
				icon = self.__icon,
				save_as = True )

			self.__filename = _filename

			if os.path.exists( self.__original ):
				_src = io.open( self.__original ).read( )
				_dest = io.open( _filename, 'w+' ).write( _src )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'SaveFileDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class GoogleDialog( Sith ):
	'''
	Construcotr:
	GoogleDialog(  )

	Purpose:
	class that renames a folder
	'''
	__image = None
	__querytext = None
	__results = None

	@property
	def search( self ) -> str:
		if self.__querytext is not None:
			return self.__querytext

	@search.setter
	def search( self, value: str ):
		if value is not None:
			self.__querytext = value

	@property
	def image( self ) -> str:
		if self.__image is not None:
			return self.__image

	@image.setter
	def image( self, value: str ):
		if value is not None:
			self.__image = value

	@property
	def results( self ) -> str:
		if self.__results is not None:
			return self.__results

	@results.setter
	def results( self, value: str ):
		if value is not None:
			self.__results = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = ( 500, 250 )
		self.__image = os.getcwd( ) + r'\etc\img\app\web\google.png'

	def __str__( self ) -> str:
		if isinstance( self.__results, list ):
			return self.__results[ 0 ]

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			self.__results = [ ]
			_layout = [ [ sg.Text( ) ],
			            [ sg.Image( source = self.__image ) ],
			            [ sg.Text( size = ( 10, 1 ) ),
			              sg.Input( key = '-QUERY-', size = ( 40, 2 ) ) ],
			            [ sg.Text( size = ( 100, 1 ) ) ],
			            [ sg.Text( size = ( 100, 1 ) ) ],
			            [ sg.Text( size = ( 10, 1 ) ), sg.Submit( size = ( 15, 1 ) ),
			              sg.Text( size = ( 5, 1 ) ), sg.Cancel( size = ( 15, 1 ) ) ] ]

			_window = sg.Window( '  Budget Execution', _layout,
				icon = self.__icon,
				font = self.__themefont,
				size = self.__formsize )

			while True:
				_event, _values = _window.read( )
				if _event in (sg.WIN_X_EVENT, sg.WIN_CLOSED, 'Cancel'):
					break
				elif _event == 'Submit':
					self.__querytext = _values[ '-QUERY-' ]
					_google = search( term = self.__querytext, num_results = 5 )
					_app = App( Client.Edge )
					for result in list( _google ):
						self.__results.append( result )
						_app.run_args( result )

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'GoogleDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class EmailDialog( Sith ):
	'''
	Construcotr: EmailDialog( sender: str = '', receiver: str = '',
			subject: str = '', heading: str = '' )

	Purpose:  Class providing form used to send email messages.
    '''
	__image = None
	__folderpath = None
	__sender = None
	__receiver = None
	__subject = None
	__message = None
	__others = None
	__username = None
	__password = None

	@property
	def sender( self ) -> str:
		if self.__sender is not None:
			return self.__sender

	@sender.setter
	def sender( self, value: str ):
		if value is not None:
			self.__sender = value

	@property
	def receiver( self ) -> str:
		if self.__receiver is not None:
			return self.__receiver

	@receiver.setter
	def receiver( self, value: str ):
		if value is not None:
			self.__receiver = value

	@property
	def message( self ) -> str:
		if self.__message is not None:
			return self.__message

	@message.setter
	def message( self, value: str ):
		if value is not None:
			self.__message = value

	@property
	def subject( self ) -> str:
		if self.__subject is not None:
			return self.__subject

	@subject.setter
	def subject( self, value: str ):
		if value is not None:
			self.__subject = value

	@property
	def others( self ) -> str:
		if self.__others is not None:
			return self.__others

	@others.setter
	def others( self, value: str ):
		if value is not None:
			self.__others = value

	@property
	def username( self ) -> str:
		if self.__username is not None:
			return self.__username

	@username.setter
	def username( self, value: str ):
		if value is not None:
			self.__username = value

	@property
	def password( self ) -> str:
		if self.__password is not None:
			return self.__password

	@password.setter
	def password( self, value: str ):
		if value is not None:
			self.__password = value

	def __init__( self, sender: str = '', receiver: str = '',
	              subject: str = '', message: str = '' ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__image = os.getcwd( ) + r'\etc\img\app\web\outlook.png'
		self.__formsize = (650, 550)
		self.__sender = sender
		self.__receiver = receiver
		self.__subject = subject
		self.__message = message

	def __str__( self ) -> str:
		if self.__message is not None:
			return self.__message

	def show( self ):
		try:
			_btn = (20, 1)
			_input = (35, 1)
			_spc = (5, 1)
			_img = (50, 22)
			_clr = '#69B1EF'
			_layout = [ [ sg.Text( ' ', size = _spc ), ],
			            [ sg.Text( ' ', size = _spc ), ],
			            [ sg.Text( ' ', size = _spc ),
			              sg.Text( 'From:', size = _btn, text_color = _clr ),
			              sg.Input( key = '-EMAIL FROM-', size = _input ) ],
			            [ sg.Text( ' ', size = _spc ), sg.Text( 'To:', size = _btn, text_color =
			            _clr ),
			              sg.Input( key = '-EMAIL TO-', size = _input ) ],
			            [ sg.Text( ' ', size = _spc ),
			              sg.Text( 'Subject:', size = _btn, text_color = _clr ),
			              sg.Input( key = '-EMAIL SUBJECT-', size = _input ) ],
			            [ sg.Text( ' ', size = _spc ), sg.Text( ) ],
			            [ sg.Text( ' ', size = _spc ),
			              sg.Text( 'Username:', size = _btn, text_color = _clr ),
			              sg.Input( key = '-USER-', size = _input ) ],
			            [ sg.Text( ' ', size = _spc ),
			              sg.Text( 'Password:', size = _btn, text_color = _clr ),
			              sg.Input( password_char = '*', key = '-PASSWORD-', size = _input ) ],
			            [ sg.Text( ' ', size = _spc ) ],
			            [ sg.Text( ' ', size = _spc ),
			              sg.Multiline( 'Type your message here', size = (65, 10),
				              key = '-EMAIL TEXT-' ) ],
			            [ sg.Text( ' ', size = (100, 1) ) ],
			            [ sg.Text( ' ', size = _spc ), sg.Button( 'Send', size = _btn ),
			              sg.Text( ' ', size = _btn ), sg.Button( 'Cancel', size = _btn ) ] ]

			_window = sg.Window( '  Budget Execution', _layout,
				icon = self.__icon,
				size = self.__formsize )

			while True:  # Event Loop
				_event, _values = _window.read( )
				if _event in (sg.WIN_CLOSED, 'Cancel', 'Exit'):
					break
				if _event == 'Send':
					sg.popup_quick_message( 'Sending your heading... this will take a moment...',
						background_color = 'red' )
			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'EmailDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class MessageDialog( Sith ):
	'''
	Construcotr:  MessageDialog( text = '' )

	Purpose:  Class that provides form used
    to display informational messages
    '''
	__text = None

	@property
	def text( self ) -> str:
		if self.__text is not None:
			return self.__text

	@text.setter
	def text( self, value: str ):
		if value is not None:
			self.__text = value

	def __init__( self, text: str = '' ):
		self.__text = text
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = (450, 250)

	def __str__( self ) -> str:
		if self.__text is not None:
			return self.__text

	def show( self ):
		try:
			_txtsz = (100, 1)
			_btnsz = (10, 1)
			_layout = [ [ sg.Text( size = _txtsz ) ],
			            [ sg.Text( size = _txtsz ) ],
			            [ sg.Text( size = (5, 1) ),
			              sg.Text( self.__text,
				              font = ('Roboto', 11),
				              enable_events = True,
				              key = '-TEXT-',
				              text_color = '#69B1EF',
				              size = (80, 1) ) ],
			            [ sg.Text( size = _txtsz ) ],
			            [ sg.Text( size = _txtsz ) ],
			            [ sg.Text( size = _txtsz ) ],
			            [ sg.Text( size = (5, 1) ), sg.Ok( size = _btnsz ),
			              sg.Text( size = (15, 1) ), sg.Cancel( size = _btnsz ) ] ]

			_window = sg.Window( r'  Budget Execution', _layout,
				icon = self.__icon,
				font = self.__themefont,
				size = self.__formsize )

			while True:
				_event, _values = _window.read( )
				if _event in (sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Ok', 'Cancel'):
					break

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'MessageDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ErrorDialog( Sith ):
	'''
	Construcotr:  ErrorDialog( exception )

	Purpose:  Class that displays excetption data that accepts
     a single, optional argument 'exception' of type Error
    '''
	__class = None
	__module = None
	__method = None
	__heading = None
	__type = None
	__trace = None
	__info = None
	__exception = None

	@property
	def info( self ) -> str:
		if self.__class is not None:
			return self.__class

	@info.setter
	def info( self, value: str ):
		if value is not None:
			self.__class = value

	@property
	def cause( self ) -> str:
		if self.__class is not None:
			return self.__class

	@cause.setter
	def cause( self, value: str ):
		if value is not None:
			self.__class = value

	@property
	def method( self ) -> str:
		if self.__method is not None:
			return self.__method

	@method.setter
	def method( self, value: str ):
		if value is not None:
			self.__method = value

	@property
	def module( self ) -> str:
		if self.__module is not None:
			return self.__module

	@module.setter
	def module( self, value: str ):
		if value is not None:
			self.__module = value

	@property
	def type( self ) -> str:
		if self.__type is not None:
			return self.__type

	@type.setter
	def type( self, value: str ):
		if value is not None:
			self.__type = value

	@property
	def message( self ) -> str:
		if self.__heading is not None:
			return self.__heading

	@message.setter
	def message( self, value: str ):
		if value is not None:
			self.__heading = value

	def __init__( self, exception ):
		super( ).__init__( )
		self.__exception = exception if isinstance( exception, Error ) else None
		self.__heading = exception.message
		self.__module = exception.module
		self.__info = exception.stack_trace
		self.__cause = exception.cause
		self.__method = exception.method
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = (500, 300)

	def __str__( self ) -> str:
		if isinstance( self.__info, str ):
			return self.__info

	def show( self ):
		_msg = self.__heading if isinstance( self.__heading, str ) else None
		_info = f'Module:\t{self.__module}\r\nClass:\t{self.__cause}\r\n' \
		        f'Method:\t{self.__method}\r\n \r\n{self.__info}'
		_red = '#F70202'
		_font = ('Roboto', 10)
		_padsz = (3, 3)
		_layout = [ [ sg.Text( ) ],
		            [ sg.Text( f'{_msg}', size = (100, 1), key = '-MSG-', text_color = _red,
			            font = _font ) ],
		            [ sg.Text( size = (150, 1) ) ],
		            [ sg.Multiline( f'{_info}', key = '-INFO-', size = (80, 7), pad = _padsz )],
		            [ sg.Text( ) ],
		            [ sg.Text( size = (20, 1) ), sg.Cancel( size = (15, 1), key = '-CANCEL-' ),
		              sg.Text( size = (10, 1) ), sg.Ok( size = (15, 1), key = '-OK-' ) ] ]

		_window = sg.Window( r' Budget Execution', _layout,
			icon = self.__icon,
			font = self.__themefont,
			size = self.__formsize )

		while True:
			_event, _values = _window.read( )
			if _event in (sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Canel', '-OK-'):
				break

		_window.close( )

class InputDialog( Sith ):
	'''
	Construcotr:  Input( question )

	Purpose:  class that produces a contact input form
	'''
	__question = None
	__response = None
	__themefont = None

	@property
	def question( self ) -> str:
		if self.__question is not None:
			return self.__question

	@question.setter
	def question( self, value: str ):
		if value is not None:
			self.__question = value

	@property
	def response( self ) -> str:
		if self.__response is not None:
			return self.__response

	@response.setter
	def response( self, value: str ):
		if value is not None:
			self.__response = value

	def __init__( self, question ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__question = question if isinstance( question, str ) else None
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = (500, 250)
		self.__response = None

	def __str__( self ) -> str:
		if isinstance( self.__response, str ):
			return self.__response

	def show( self ):
		try:
			_layout = [ [ sg.Text( ) ],
			            [ sg.Text( self.__question, font = ('Roboto', 9, 'bold') ) ],
			            [ sg.Text( ) ],
			            [ sg.Text( 'Enter:', size = (10, 2) ),
			              sg.InputText( key = '-INPUT-', size = (40, 2) ) ],
			            [ sg.Text( size = (100, 1) ) ],
			            [ sg.Text( size = (100, 1) ) ],
			            [ sg.Text( size = (10, 1) ),
			              sg.Submit( size = (15, 1), key = '-SUBMIT-' ),
			              sg.Text( size = (5, 1) ),
			              sg.Cancel( size = (15, 1), key = '-CANCEL-' ) ] ]

			_window = sg.Window( '  Budget Execution', _layout,
				icon = self.__icon,
				font = self.__themefont,
				size = self.__formsize )

			while True:
				_event, _values = _window.read( )
				if _event in (sg.WIN_X_EVENT, sg.WIN_CLOSED, '-CANCEL-', 'Exit'):
					break

				self.__response = _values[ '-INPUT-' ]
				sg.popup( _event, _values, self.__response,
					text_color = self.__themetextcolor,
					font = self.__themefont,
					icon = self.__icon )

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'InputDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ScrollingDialog( Sith ):
	'''
	Construcotr:  ScrollingDialog( text = '' )

	Purpose:  Provides form for multiline input/output
	'''
	__arrowcolor = None

	@property
	def text( self ) -> str:
		if self.__text is not None:
			return self.__text

	@text.setter
	def text( self, value: str ):
		if value is not None:
			self.__text = value

	def __init__( self, text = '' ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__arrowcolor = super( ).scrollbar_color
		self.__formsize = (700, 600)
		self.__text = text if isinstance( text, str ) and text != '' else None

	def __str__( self ) -> str:
		if isinstance( self.__text, str ):
			return self.__text

	# noinspection PyTypeChecker
	def show( self ):
		try:
			_line = (100, 1)
			_space = (5, 1)
			_btnsize = (25, 1)
			_arrow = self.__arrowcolor
			_back = super( ).button_backcolor
			_padsz = (3, 3, 3, 3)
			_layout = [ [ sg.Text( ' ', size = _line ) ],
			            [ sg.Text( ' ', size = _line ) ],
			            [ sg.Text( size = _space ),
			             sg.Multiline( size = (70, 20), key = '-TEXT-', pad = _padsz ),
			             sg.Text( size = _space ) ],
			            [ sg.Text( ' ', size = _line ) ],
			            [ sg.Text( ' ', size = _space ), sg.Input( k = '-IN-', size = (70, 20) ),
			             sg.Text( size = _space ) ],
			            [ sg.Text( ' ', size = _line ) ],
			            [ sg.Text( size = _space ), sg.Button( 'Submit', size = _btnsize ),
			             sg.Text( size = (15, 1) ), sg.Button( 'Exit', size = _btnsize ),
			             sg.Text( size = _space ), ] ]

			_window = sg.Window( '  Budget Execution', _layout,
				icon = self.__icon,
				size = self.__formsize,
				font = self.__themefont,
				resizable = True )

			while True:
				event, values = _window.read( )
				self.__text = values[ '-TEXT-' ]
				if event in (sg.WIN_CLOSED, 'Exit'):
					break

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'ScrollingDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ContactForm( Sith ):
	'''
	Construcotr: ContactForm( contact )

	Purpose:  class that produces a contact input form
	'''

	@property
	def size( self ) -> (int, int):
		if self.__formsize is not None:
			return self.__formsize

	@size.setter
	def size( self, value: (int, int) ):
		if value is not None:
			self.__formsize = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__image = os.getcwd( ) + r'\etc\img\app\web\outlook.png'
		self.__formsize = (500, 300)

	def show( self ):
		try:
			_layout = [ [ sg.Text( size = (100, 1) ) ],
			            [ sg.Text( r'Enter Contact Details' ) ],
			            [ sg.Text( size = (100, 1) ) ],
			            [ sg.Text( 'Name', size = (10, 1) ),
			              sg.InputText( '1', size = (80, 1), key = '-NAME-' ) ],
			            [ sg.Text( 'Address', size = (10, 1) ),
			              sg.InputText( '2', size = (80, 1), key = '-ADDRESS-' ) ],
			            [ sg.Text( 'Phone', size = (10, 1) ),
			              sg.InputText( '3', size = (80, 1), key = '-PHONE-' ) ],
			            [ sg.Text( size = (100, 1) ) ],
			            [ sg.Text( size = (100, 1) ) ],
			            [ sg.Text( size = (10, 1) ), sg.Submit( size = (10, 1) ),
			              sg.Text( size = (20, 1) ), sg.Cancel( size = (10, 1) ) ] ]

			_window = sg.Window( '  Budget Execution', _layout,
				icon = self.__icon,
				font = self.__themefont,
				size = self.__formsize )

			while True:
				_event, _values = _window.read( )
				sg.popup( 'Results', _values, _values[ '-NAME-' ],
					_values[ '-ADDRESS-' ],
					_values[ '-PHONE-' ],
					text_color = self.__themetextcolor,
					font = self.__themefont,
					icon = self.__icon )

				if _event in (sg.WIN_CLOSED, sg.WIN_X_EVENT, 'Cancel'):
					break

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'ContactForm'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class GridForm( Sith ):
	'''
	Construcotr: GridForm( )

	Purpose:  object providing form that simulates a datagrid
	'''
	__width = None
	__rows = None
	__columns = None

	@property
	def field_width( self ) -> (int, int):
		if self.__width is not None:
			return self.__width

	@field_width.setter
	def field_width( self, value: (int, int) ):
		if value is not None:
			self.__width = value

	@property
	def rows( self ) -> int:
		if self.__rows is not None:
			return self.__rows

	@rows.setter
	def rows( self, value: int ):
		if value is not None:
			self.__rows = value

	@property
	def columns( self ) -> int:
		if self.__columns is not None:
			return self.__columns

	@columns.setter
	def columns( self, value: int ):
		if value is not None:
			self.__columns = value

	def __init__( self, rows = 30, columns = 10 ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__image = None
		self.__width = ( 17, 1 )
		self.__rows = rows
		self.__columns = columns
		self.__formsize = (1250, 700)

	def show( self ):
		try:
			_black = self.__themebackground
			_columns = self.__columns
			_headings = [ f'HEADER-{i + 1}' for i in range( _columns ) ]
			_space = [ [ sg.Text( size = ( 10, 1 ) ) ], [ sg.Text( size = ( 10, 1 ) ) ],
			           [ sg.Text( size = ( 10, 1 ) ) ] ]
			_header = [
					[ sg.Text( h, size = ( 16, 1 ), justification = 'left' ) for h in _headings ] ]
			_records = [ [ [ sg.Input( size = self.__width, pad = (0, 0), font = self.__themefont )
			                 for c in range( len( _headings ) ) ] for r in range( self.__rows )
			               ], ]
			_buttons = [ [ sg.Text( size = ( 35, 1 ) ), sg.Text( size = ( 10, 1 ) ), ],
			             [ sg.Text( size = ( 100, 1 ) ), sg.Text( size = ( 100, 1 ) ),
			               sg.Ok( size = ( 35, 2 ) ) ],
			             [ sg.Sizegrip( background_color = _black ) ] ]
			# noinspection PyTypeChecker
			_layout = _space + _header + _records + _buttons

			_window = sg.Window( '  Budget Execution', _layout,
				finalize = True,
				size = self.__formsize,
				icon = self.__icon,
				font = self.__themefont,
				resizable = True )

			while True:
				_event, _values = _window.read( )
				if _event in ( sg.WIN_CLOSED, sg.WIN_X_EVENT, '-CANCEL-' ):
					break

				_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'GridForm'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class LoadingPanel( Sith ):
	'''
	Construcotr:  LoadingPanel( )

	Purpose:  object providing form loading behavior
	'''
	__image = None
	__timeout = None

	@property
	def timeout( self ) -> int:
		if isinstance( self.__timeout, int ):
			return self.__timeout

	@timeout.setter
	def timeout( self, value: int ):
		if value is not None:
			self.__timeout = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__image = os.getcwd( ) + r'\etc\img\loaders\loading.gif'
		self.__formsize = ( 800, 600 )
		self.__timeout = 6000

	def show( self ):
		try:
			_layout = [ [ sg.Text(
				background_color = '#000000',
				text_color = '#FFF000',
				justification = 'c',
				key = '-T-',
				font = ( 'Bodoni MT', 40 ) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

			_window = sg.Window( '  Loading...', _layout,
				icon = self.__icon,
				element_justification = 'c',
				margins = ( 0, 0 ),
				size = ( 800, 600 ),
				element_padding = ( 0, 0 ), finalize = True )

			_window[ '-T-' ].expand( True, True )
			_interframe_duration = Image.open( self.__image ).info[ 'duration' ]

			while True:
				for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
					_event, _values = _window.read( timeout = _interframe_duration )
					if _event == sg.WIN_CLOSED or _event == sg.WIN_X_EVENT:
						exit( 0 )
					_window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
					_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'LoadingPanel'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class WaitingPanel( Sith ):
	'''
	Construcotr:  WaitingPanel( )

	Purpose:  object providing form loader behavior
	'''
	__image = None
	__timeout = None

	@property
	def timeout( self ) -> int:
		if self.__timeout is not None:
			return self.__timeout

	@timeout.setter
	def timeout( self, value: str ):
		if value is not None:
			self.__timeout = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__image = os.getcwd( ) + r'\etc\img\loaders\loader.gif'
		self.__themefont = ('Roboto', 9)
		self.__formsize = (800, 600)
		self.__timeout = 6000

	def show( self ):
		try:
			_layout = [ [ sg.Text(
				background_color = '#000000',
				text_color = '#FFF000',
				justification = 'c',
				key = '-T-',
				font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

			_window = sg.Window( '  Waiting...', _layout,
				icon = self.__icon,
				element_justification = 'c',
				margins = (0, 0),
				element_padding = (0, 0),
				size = (800, 600),
				finalize = True )

			_window[ '-T-' ].expand( True, True  )
			_interframe_duration = Image.open( self.__image ).info[ 'duration' ]

			while True:
				for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
					_event, _values = _window.read( timeout = _interframe_duration )
					if _event == sg.WIN_CLOSED:
						exit( 0 )
					_window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
					_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'WaitingPanel'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ProcessingPanel( Sith ):
	'''
	Construcotr:  ProcessingPanel( )

	Purpose:  object providing form processing behavior
	'''
	__image = None
	__timeout = None

	@property
	def timeout( self ) -> str:
		if self.__timeout is not None:
			return self.__timeout

	@timeout.setter
	def timeout( self, value: str ):
		if value is not None:
			self.__timeout = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__image = os.getcwd( ) + r'\etc\img\loaders\processing.gif'
		self.__formsize = (800, 600)
		self.__timeout = None

	def show( self ):
		try:
			_layout = [ [ sg.Text(
				background_color = '#000000',
				text_color = '#FFF000',
				justification = 'c',
				key = '-T-',
				font = ('Bodoni MT', 40) ) ], [ sg.Image( key = '-IMAGE-' ) ] ]

			_window = sg.Window( '  Processing...', _layout,
				element_justification = 'c',
				icon = self.__icon,
				margins = (0, 0),
				size = (800, 600),
				element_padding = (0, 0),
				finalize = True )

			_window[ '-T-' ].expand( True, True )

			_interframe_duration = Image.open( self.__image ).info[ 'duration' ]
			self.__timeout = _interframe_duration

			while True:
				for frame in ImageSequence.Iterator( Image.open( self.__image ) ):
					_event, _values = _window.read( timeout = self.__timeout,
						timeout_key = '-TIMEOUT-' )
					if _event == sg.WIN_CLOSED or _event == sg.WIN_X_EVENT:
						exit( 0 )

					_window[ '-IMAGE-' ].update( data = ImageTk.PhotoImage( frame ) )
					_window.close( )

		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'ProcessingPanel'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class SplashPanel( Sith ):
	'''
	Construcotr:  SplashPanel( )

	Purpose:  Class providing splash dialog behavior
	'''
	__image = None
	__timeout = None

	@property
	def timeout( self ) -> int:
		if self.__timeout is not None:
			return self.__timeout

	@timeout.setter
	def timeout( self, value: int ):
		if value is not None:
			self.__timeout = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__buttonforecolor = super( ).button_forecolor
		self.__buttobackcolor = super( ).button_backcolor
		self.__image = os.getcwd( ) + r'\etc\img\BudgetEx.png'
		self.__formsize = ( 800, 600 )
		self.__timeout = 6000

	def show( self ):
		try:
			_img = self.__image
			_imgsize = ( 500, 400 )
			_line = ( 100, 2 )
			_space = ( 15, 1 )
			_layout = [ [ sg.Text( size = _space ), sg.Text( size = _line ) ],
			            [ sg.Text( size = _space ), sg.Text( size = _line ) ],
			            [ sg.Text( size = _space ),
			             sg.Image( filename = self.__image, size = _imgsize ) ] ]
			_window = sg.Window( '  Budget Execution', _layout,
				no_titlebar = True,
				keep_on_top = True,
				grab_anywhere = True,
				size = self.__formsize )
			while True:
				_event, _values = _window.read( timeout = self.__timeout, close = True )
				if _event in (sg.WIN_CLOSED, 'Exit'):
					break
			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'SplashPanel'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class Notification( Sith ):
	'''
	Construcotr:  Notification( )

	Purpose:  object providing form processing behavior
	'''
	__image = None
	__message = None

	@property
	def message( self ) -> str:
		if self.__message is not None:
			return self.__message

	@message.setter
	def message( self, value: str ):
		if value is not None:
			self.__message = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
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
		              b'4E9f4E9f4E9f4FFh4Vdm4lhn42Bv5GNx5W575nJ' \
		              b'/6HqH6HyI6YCM6YGM6YGN6oaR8Kev9MPI9cb' \
		              b'M9snO9s3R+Nfb+dzg+d/i++vt/O7v/fb3/vj5//z8//7' \
		              b'+////KofnuQAAABF0Uk5TAAcIGBktSY' \
		              b'SXmMHI2uPy8/XVqDFbAAAA8UlEQVQ4y4VT15LCMBBTQkgPYem9d9D' \
		              b'//x4P2I7vILN68kj2WtsAh' \
		              b'yDO8rKuyzyLA3wjSnvi0Eujf3KY9OUP+kno651CvlB0Gr1byQ9UXff' \
		              b'+py5SmRhhIS0oPj4SaUUC' \
		              b'AJHxP9+tLb/ezU0uEYDUsCc+l5' \
		              b'/T8smTIVMgsPXZkvepiMj0Tm5txQLENu7gSF7HIuMreRxYNkb' \
		              b'mHI0u5Hk4PJOXkSMz5I3nyY08HMjbpOFylF5WswdJPmYeVaL28968yNfGZ2r9gvqFalJNUy2UW' \
		              b'mq1Wa7di/3Kxl3tF1671YHRR04dWn3s9cXRV09f3vb1fwPD7z9j1WgeRgAAAABJRU5ErkJggg=='
		self.__ninja = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAnCAYAAABuf0pMAAABhWlDQ1BJQ0MgUHJvZmlsZQA' \
		               b'AeJx9kT1Iw0AcxV9bS1WqDnYo4pChOlkQFRFcpIpFsFDaCq06mFz6BU0akhQXR8G14ODHYtXB' \
		               b'xVlXB1dBEPwAcXRyUnSREv+XFFrEeHDcj3f3HnfvAG' \
		               b'+jwhSjaxxQVFNPxWNCNrcqBF7hRz96E' \
		               b'MasyAwtkV7MwHV83cPD17soz3I/9+fok/MGAzwC8RzTdJN4g3h609Q47xOHWEmUic' \
		               b'+Jx3S6I' \
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
		self.__message = '\r\nThe action you have performed \
                          has been successful!'

	def __str__( self ) -> str:
		if self.__message is not None:
			return self.__message

	def show( self ) -> int:
		try:
			return sg.popup_notify( self.__message,
				title = 'Budget Execution Notification',
				icon = self.__ninja,
				display_duration_in_ms = 10000,
				fade_in_duration = 5000,
				alpha = 1 )

		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'Notification'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ImageSizeEncoder( Sith ):
	'''
	Construcotr:  ImageSizeEncoder( )

	Purpose:  Class resizing image and encoding behavior
	'''
	__image = None
	__timeout = None

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		version = '1.3.1'
		__version__ = version.split( )[ 0 ]

		def resize( input_file, size, output_file = None, encode_format = 'PNG' ):
			_image = Image.open( input_file )
			_width, _height = _image.size
			_newwidth, _newheight = size
			if _newwidth != _width or _newheight != _height:
				_scale = min( _newheight / _height, _newwidth / _width )
				_resizedimage = _image.resize( (int( _width * _scale ), int( _height * _scale )),
					Image.ANTIALIAS )
			else:
				_resizedimage = _image

			if output_file is not None:
				_resizedimage.save( output_file )

			with io.BytesIO( ) as bio:
				_resizedimage.save( bio, format = encode_format )
				_contents = bio.getvalue( )
				_encoded = base64.b64encode( _contents )
			return _encoded

		def update_outfilename( ):
			_infile = _values[ '-IN-' ]
			if os.path.isfile( _infile ):
				_image = Image.open( _infile )
				_width, _height = _image.size
				_window[ '-ORIG WIDTH-' ].update( _image.size[ 0 ] )
				if not _values[ '-WIDTH-' ]:
					_window[ '-WIDTH-' ].update( _image.size[ 0 ] )
				if not _values[ '-HEIGHT-' ]:
					_window[ '-HEIGHT-' ].update( _image.size[ 1 ] )
				_window[ '-ORIG HEIGHT-' ].update( _image.size[ 1 ] )

				_infilename = os.path.basename( _infile )
				_infilenameonly, _infileext = os.path.splitext( _infilename )
				if _values[ '-NEW FORMAT-' ]:
					outfileext = _values[ '-NEW FORMAT-' ].lower( )
					if outfileext == 'jpeg':
						outfileext = 'jpg'
				else:
					outfileext = _infileext[ 1: ]  # strip off the .
				outfile = f'{_infilenameonly}{_width}x{_height}.{outfileext}'
				_outfullname = os.path.join( os.path.dirname( _infile ), outfile )

				if _values[ '-DO NOT SAVE-' ]:
					_window[ '-NEW FILENAME-' ].update( '' )
					_window[ '-BASE64-' ].update( True )
				else:
					_window[ '-NEW FILENAME-' ].update( _outfullname )
			else:
				_window[ '-NEW FILENAME-' ].update( '' )
				_window[ '-ORIG WIDTH-' ].update( '' )
				# _window['-WIDTH-'].update('')
				_window[ '-ORIG HEIGHT-' ].update( '' )
				# _window['-HEIGHT-'].update('')
				_window[ '-NEW FILENAME-' ].update( )

		_formatlist = ('', 'PNG', 'JPEG', 'BMP', 'ICO', 'GIF', 'TIFF')
		_newformat = [
				[ sg.Combo( _formatlist,
					default_value = sg.user_settings_get_entry( '-new format-', '' ),
					readonly = True, enable_events = True, key = '-NEW FORMAT-' ) ] ]

		_layout = [ [ sg.Text( 'Image Resizer' ) ],
		            [ sg.Frame( 'Input Filename', [
				           [ sg.Input( key = '-IN-', enable_events = True, s = 80 ),
				             sg.FileBrowse( ), ],
				           [ sg.T( 'Original size' ), sg.T( k = '-ORIG WIDTH-' ), sg.T( 'X' ),
				             sg.T( k = '-ORIG HEIGHT-' ) ] ] ) ],
		            [ sg.Frame( 'Output Filename',
			           [ [ sg.In( k = '-NEW FILENAME-', s = 80 ), sg.FileBrowse( ), ],
			             [ sg.In( default_text = sg.user_settings_get_entry( '-_width-', '' ),
				             s = 4,
				             k = '-WIDTH-' ), sg.T( 'X' ),
			               sg.In( default_text = sg.user_settings_get_entry( '-_height-', '' ),
				               s = 4, k = '-HEIGHT-' ) ] ] ) ],
		            [ sg.Frame( 'Convert To New Format', _newformat ) ],
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

		_window = sg.Window( 'Resize Image', _layout,
			icon = self.__icon,
			right_click_menu = sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT,
			enable_close_attempted_event = True,
			finalize = True )
		_window[ '-PSGRESIZER-' ].set_cursor( 'hand1' )
		_window[ '-PYSIMPLEGUI-' ].set_cursor( 'hand1' )
		while True:
			_event, _values = _window.read( )
			# print(_event, _values)
			if _event in ( sg.WIN_CLOSED, sg.WIN_CLOSE_ATTEMPTED_EVENT, 'Exit' ):
				break
			_infile = _values[ '-IN-' ]
			update_outfilename( )

			if _event == '-DO NOT SAVE-':
				if _values[ '-DO NOT SAVE-' ]:
					_window[ '-NEW FILENAME-' ].update( '' )
					_window[ '-BASE64-' ].update( True )
			if _event == 'Resize':
				try:
					if os.path.isfile( _infile ):
						update_outfilename( )
						infilename = os.path.basename( _infile )
						infilenameonly, infileext = os.path.splitext( infilename )
						if _values[ '-NEW FORMAT-' ]:
							encode_format = _values[ '-NEW FORMAT-' ].upper( )
						else:
							encode_format = infileext[ 1: ].upper( )  # strip off the .
						if encode_format == 'JPG':
							encode_format = 'JPEG'
						outfullfilename = _values[ '-NEW FILENAME-' ]
						width, height = int( _values[ '-WIDTH-' ] ), int( _values[ '-HEIGHT-' ] )
						if _values[ '-DO NOT SAVE-' ]:
							encoded = resize( input_file = _infile, size = (width, height),
								encode_format = encode_format )
						else:
							encoded = resize( input_file = _infile, size = (width, height),
								output_file = outfullfilename, encode_format = encode_format )

						if _values[ '-BASE64-' ]:
							sg.clipboard_set( encoded )

						sg.popup_quick_message( 'DONE!', font = '_ 40', background_color = 'red',
							text_color = 'white' )

				except Exception as e:
					sg.popup_error_with_traceback( 'Error resizing or converting',
						'Error encountered during the resize or Base64 encoding', e )
				if _values[ '-AUTOCLOSE-' ]:
					break
			elif _event == 'Version':
				sg.popup_scrolled( sg.get_versions( ), non_blocking = True )
			elif _event == 'Edit Me':
				sg.execute_editor( __file__ )
			elif _event == 'File Location':
				sg.popup_scrolled( 'This Python file is:', __file__ )
			elif _event == '-PYSIMPLEGUI-':
				webbrowser.open_new_tab( r'http://www.PySimpleGUI.com' )
			elif _event == '-PSGRESIZER-':
				webbrowser.open_new_tab( r'https://github.com/PySimpleGUI/psgresizer' )

		if _event != sg.WIN_CLOSED:
			sg.user_settings_set_entry( '-autoclose-', _values[ '-AUTOCLOSE-' ] )
			sg.user_settings_set_entry( '-new format-', _values[ '-NEW FORMAT-' ] )
			sg.user_settings_set_entry( '-do not save-', _values[ '-DO NOT SAVE-' ] )
			sg.user_settings_set_entry( '-base64-', _values[ '-BASE64-' ] )
			sg.user_settings_set_entry( '-_width-', _values[ '-WIDTH-' ] )
			sg.user_settings_set_entry( '-_height-', _values[ '-HEIGHT-' ] )

		_window.close( )

class PdfForm( Sith ):
	'''
	Construcotr:
	PdfForm( )

	Purpose:
	Creates form to view a PDF
	'''
	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = ( 600, 800 )

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_oldpage = 0
			_zoom = 0
			_oldzoom = 0

			_filename = sg.popup_get_file( 'Select file', ' Budget PDF Viewer',
				icon = self.__icon,
				font = self.__themefont,
				file_types = ( ( 'PDF Files', '*.pdf' ), ) )

			if _filename is None:
				sg.popup_cancel( 'Cancelling' )
				exit( 0 )

			_pdf = fitz.open( _filename )
			_pages = len( _pdf )
			_displaylist = [ None ] * _pages
			_title = ' Budget Execution'

			def getpage( pno, zoom = 0 ):
				_display = _displaylist[ pno ]
				if _display:
					_displaylist[ pno ] = _pdf[ pno ].get_displaylist( )
					_display = _displaylist[ pno ]
					_r = _display.rect
					_mp = _r.tl + (_r.br - _r.tl) * 0.5  # rect middle point
					_mt = _r.tl + (_r.tr - _r.tl) * 0.5  # middle of top edge
					_ml = _r.tl + (_r.bl - _r.tl) * 0.5  # middle of left edge
					_mr = _r.tr + (_r.br - _r.tr) * 0.5  # middle of right egde
					_mb = _r.bl + (_r.br - _r.bl) * 0.5  # middle of bottom edge
					_mat = fitz.Matrix( 2, 2 )
					if zoom == 1:
						_clip = fitz.Rect( _r.tl, _mp )
					elif zoom == 4:
						_clip = fitz.Rect( _mp, _r.br )
					elif zoom == 2:
						_clip = fitz.Rect( _mt, _mr )
					elif zoom == 3:
						_clip = fitz.Rect( _ml, _mb )
					if zoom == 0:
						_pix = _display.get_pixmap( alpha = False )
					else:
						_pix = _display.get_pixmap( alpha = False, matrix = _mat )
					return _pix.tobytes( )

			_current = 0
			_data = getpage( _current )
			_image = sg.Image( data = _data )
			_goto = sg.InputText( f'{str( _current + 1 )} of {str( _pages )}', size = (10, 1) )
			_layout = [ [ sg.Button( 'Prev' ), sg.Button( 'Next' ),
			              sg.Text( ),
			              sg.Text( 'Page:' ), _goto,
			              sg.Text( size = (10, 1) ), sg.Text( 'Zoom: ' ),
			              sg.Button( ' In ', key = '-IN-' ), sg.Button( ' Out', key = '-OUT-' ), ],
			            [ _image ], ]

			_keys = ('Next', 'Next:34', 'Prev', 'Prior:33', 'MouseWheel:Down', 'MouseWheel:Up',
					'-IN-', '-OUT-')

			_window = sg.Window( _title, _layout,
				size = self.__formsize,
				font = self.__themefont,
				modal = True,
				resizable = True,
				grab_anywhere = True,
				icon = self.__icon )

			while True:
				_event, _values = _window.read( )
				_forcepage = False
				if _event == sg.WIN_CLOSED:
					break
				elif _event in ('Next', 'Next:34', 'MouseWheel:Down'):
					_current += 1
					_goto.Update( f'{str( _current + 1 )} of {str( _pages )}' )
				elif _event in ('Prev', 'Prior:33', 'MouseWheel:Up'):
					_current -= 1
					_goto.Update( f'{str( _current + 1 )} of {str( _pages )}' )
				elif _event == '-IN-':
					_zoom += 1
				elif _event == '-OUT-':
					_zoom -= 1

				if _current >= _pages:
					_current = 0

				while _current < 0:
					_current += _pages

				if _current != _oldpage:
					_zoom = _oldzoom = 0
					_forcepage = True
					if _zoom != _oldzoom:
						_forcepage = True

				if _forcepage:
					_data = getpage( _current, _zoom )
					_image.update( data = _data )
					_oldpage = _current

				_oldzoom = _zoom

				if _event in _keys or not _values[ 0 ]:
					_goto.update( f'{str( _current + 1 )} of {str( _pages )}' )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'PdfForm'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class CalendarDialog( Sith ):
	'''
	Construcotr:
	CalendarDialog( )

	Purpose:
	class creates form providing today selection behavior
	'''
	__selecteditem = None
	__day = None
	__month = None
	__year = None

	@property
	def selected_item( self ) -> str:
		if isinstance( self.__selecteditem, tuple ):
			_year = str( self.__selecteditem[ 2 ] )
			_month = str( self.__selecteditem[ 0 ] ).zfill( 2 )
			_day = str( self.__selecteditem[ 1 ] ).zfill( 2 )
			_date = f'{_year}/{_month}/{_day}'
			return _date

	@selected_item.setter
	def selected_item( self, value: tuple ):
		if value is not None:
			self.__selecteditem = value

	@property
	def day( self ) -> tuple:
		if self.__selecteditem is not None:
			return self.__selecteditem[ 1 ].zfill( 2 )

	@day.setter
	def day( self, value: tuple ):
		if value is not None:
			self.__day = value[ 1 ].zfill( 2 )

	@property
	def month( self ) -> tuple:
		if self.__selecteditem is not None:
			return self.__selecteditem[ 0 ].zfill( 2 )

	@month.setter
	def month( self, value: tuple ):
		if value is not None:
			self.__day = value[ 0 ].zfill( 2 )

	@property
	def year( self ) -> tuple:
		if self.__selecteditem is not None:
			return self.__selecteditem[ 2 ]

	@year.setter
	def year( self, value: tuple ):
		if value is not None:
			self.__day = value[ 2 ].zfill( 4 )

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = ( 500, 250 )

	def __str__( self ) -> str:
		if isinstance( self.__selecteditem, tuple ):
			_yr = str( self.__selecteditem[ 2 ] )
			_mo = str( self.__selecteditem[ 0 ] ).zfill( 2 )
			_dy = str( self.__selecteditem[ 1 ] ).zfill( 2 )
			_date = f'{_yr}/{_mo}/{_dy}'
			return _date

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_btnsize = ( 20, 1 )
			_calendar = ( 250, 250 )

			_months = [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL',
			           'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ]

			_days = [ 'SUN', 'MON', 'TUE', 'WEC', 'THU', 'FRI', 'SAT' ]

			_cal = sg.popup_get_date( title = 'Calendar',
				no_titlebar = False,
				icon = self.__icon,
				month_names = _months,
				day_abbreviations = _days,
				close_when_chosen = True )

			self.__selecteditem = _cal
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'CalendarDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ComboBoxDialog( Sith ):
	'''
	Construcotr:
	ComboBoxDialog( data: list = None )

	Purpose:
	Logger object provides form for log printing
	'''
	__items = None
	__selecteditem = None

	@property
	def items( self ) -> list:
		if self.__items is not None:
			return self.__items

	@items.setter
	def items( self, value: list ):
		if value is not None:
			self.__items = value

	@property
	def selected_item( self ) -> str:
		if isinstance( self.__selecteditem, str ):
			return self.__selecteditem

	@selected_item.setter
	def selected_item( self, value: str ):
		if isinstance( value, str ):
			self.__selecteditem = value

	def __init__( self, data: list = None ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = ( 400, 150 )
		self.__items = data

	def __str__( self ) -> str:
		if isinstance( self.__selecteditem, str ) and self.__selecteditem != '':
			return self.__selecteditem

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_btnsz = (10, 1)
			_spc = (5, 1)
			if self.__items is None:
				self.__items = [ f'Item {x} ' for x in range( 30 ) ]
				_values = self.__items

			_layout = [ [ sg.Text( size = _spc ), sg.Text( size = _spc ) ],
			            [ sg.Text( size = _spc ), sg.Text( 'Select Item' ) ],
			            [ sg.Text( size = _spc ),
			             sg.DropDown( self.__items, key = '-ITEM-', size = ( 35, 1 ) ) ],
			            [ sg.Text( size = _spc ), sg.Text( size = _spc ) ],
			            [ sg.Text( size = _spc ), sg.OK( size = _btnsz ), sg.Text( size = (8,
			                                                                               1) ),
			              sg.Cancel( size = _btnsz ) ] ]

			_window = sg.Window( '  Budget Execution', _layout,
				icon = self.__icon,
				size = self.__formsize )

			while True:
				_event, _values = _window.read( )
				if _event in (sg.WIN_CLOSED, 'Exit', 'Cancel'):
					break

				self.__selecteditem = _values[ '-ITEM-' ]
				sg.popup( _event, _values, self.__selecteditem,
					text_color = self.__themetextcolor,
					font = self.__themefont,
					icon = self.__icon )

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'ComboBoxDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ListBoxDialog( Sith ):
	'''
	Construcotr:
	ListBox( data: list = None )

	Purpose:
	List search and selection
    '''
	__selecteditem = None
	__items = None
	__image = None

	@property
	def items( self ) -> list:
		if self.__items is not None:
			return self.__items

	@items.setter
	def items( self, value: list ):
		if value is not None:
			self.__items = value

	@property
	def selected_item( self ) -> str:
		if self.__selecteditem is not None:
			return self.__selecteditem

	@selected_item.setter
	def selected_item( self, value: str ):
		if value is not None:
			self.__selecteditem = value

	def __init__( self, data: list = None ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = (400, 250)
		self.__image = os.getcwd( ) + r'\etc\img\app\dialog\lookup.png'
		self.__items = data

	def __str__( self ) -> str:
		if self.__selecteditem is not None:
			return self.__selecteditem

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_btnsize = ( 10, 1 )
			_space = ( 10, 1 )
			_line = ( 100, 1 )
			_txtsz = ( 25, 1 )
			_inpsz = ( 25, 1 )
			_lstsz = ( 25, 5 )
			_names = [ ]

			if isinstance( self.__items, list ):
				_names = [ src for src in self.__items ]
			else:
				_names = [ f'Item - {i}' for i in range( 40 ) ]

			_layout = [ [ sg.Text( size = _space ), sg.Text( size = _line ) ],
			            [ sg.Text( size = _space ), sg.Text( r'Search:' ) ],
			            [ sg.Text( size = _space ),
			             sg.Input( size = _inpsz, enable_events = True, key = '-INPUT-' ) ],
			            [ sg.Text( size = _space ), sg.Text( size = _line ) ],
			            [ sg.Text( size = _space ),
			             sg.Listbox( _names, size = _lstsz, key = '-ITEM-',
				             font = self.__themefont ) ],
			            [ sg.Text( size = _space ), sg.Text( size = _line ) ],
			            [ sg.Text( size = _space ),
			             sg.Button( 'Select', size = _btnsize, enable_events = True ),
			             sg.Text( size = ( 3, 1 ) ), sg.Button( 'Exit', size = _btnsize ) ] ]

			_window = sg.Window( '  Budget Execution', _layout,
				size = self.__formsize,
				font = self.__themefont,
				icon = self.__icon )

			while True:
				_event, _values = _window.read( )
				if _event in ( sg.WIN_CLOSED, 'Exit' ):
					break
				self.__selecteditem = str( _values[ '-ITEM-' ][ 0 ] )
				if _event == 'Selected':
					self.__selecteditem = str( _values[ '-ITEM-' ][ 0 ] )
					sg.popup( 'Results', self.__selecteditem,
						font = self.__themefont,
						icon = self.__icon )
					_window.close( )

				if _values[ '-INPUT-' ] != '':
					_search = _values[ '-INPUT-' ]
					_newvalues = [ x for x in _names if _search in x ]
					_window[ '-ITEM-' ].update( _newvalues )
				else:
					_window[ '-ITEM-' ].update( _names )

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'ListBoxDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ColorDialog( Sith ):
	'''
	Construcotr:
	ColorDialog( )

	Purpose:
	class provides a form to select colors returning string values
	'''
	__rgb = None
	__hex = None
	__html = None
	__argb = None

	@property
	def rgb( self ) -> str:
		if self.__rgb is not None:
			return self.__rgb

	@rgb.setter
	def rgb( self, value: str ):
		if value is not None:
			self.__rgb = value

	@property
	def hex( self ) -> str:
		if self.__hex is not None:
			return self.__hex

	@hex.setter
	def hex( self, value: str ):
		if value is not None:
			self.__hex = value

	@property
	def argb( self ) -> str:
		if self.__argb is not None:
			return self.__argb

	@argb.setter
	def argb( self, value: str ):
		if value is not None:
			self.__argb = value

	@property
	def html( self ) -> str:
		if self.__html is not None:
			return self.__html

	@html.setter
	def html( self, value: str ):
		if value is not None:
			self.__html = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = ( 450, 450 )

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_colormap = {
					'alice blue': '#F0F8FF',
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
					'bisque': '#FFE4C4',
					'bisque1': '#FFE4C4',
					'bisque2': '#EED5B7',
					'bisque3': '#CDB79E',
					'bisque4': '#8B7D6B',
					'black': '#000000',
					'blanched almond': '#FFEBCD',
					'BlanchedAlmond': '#FFEBCD',
					'blue': '#0000FF',
					'blue violet': '#8A2BE2',
					'blue1': '#0000FF',
					'blue2': '#0000EE',
					'blue3': '#0000CD',
					'blue4': '#00008B',
					'BlueViolet': '#8A2BE2',
					'brown': '#A52A2A',
					'brown1': '#FF4040',
					'brown2': '#EE3B3B',
					'brown3': '#CD3333',
					'brown4': '#8B2323',
					'burlywood': '#DEB887',
					'burlywood1': '#FFD39B',
					'burlywood2': '#EEC591',
					'burlywood3': '#CDAA7D',
					'burlywood4': '#8B7355',
					'cadet blue': '#5F9EA0',
					'CadetBlue': '#5F9EA0',
					'CadetBlue1': '#98F5FF',
					'CadetBlue2': '#8EE5EE',
					'CadetBlue3': '#7AC5CD',
					'CadetBlue4': '#53868B',
					'chartreuse': '#7FFF00',
					'chartreuse1': '#7FFF00',
					'chartreuse2': '#76EE00',
					'chartreuse3': '#66CD00',
					'chartreuse4': '#458B00',
					'chocolate': '#D2691E',
					'chocolate1': '#FF7F24',
					'chocolate2': '#EE7621',
					'chocolate3': '#CD661D',
					'chocolate4': '#8B4513',
					'coral': '#FF7F50',
					'coral1': '#FF7256',
					'coral2': '#EE6A50',
					'coral3': '#CD5B45',
					'coral4': '#8B3E2F',
					'cornflower blue': '#6495ED',
					'CornflowerBlue': '#6495ED',
					'cornsilk': '#FFF8DC',
					'cornsilk1': '#FFF8DC',
					'cornsilk2': '#EEE8CD',
					'cornsilk3': '#CDC8B1',
					'cornsilk4': '#8B8878',
					'cyan': '#00FFFF',
					'cyan1': '#00FFFF',
					'cyan2': '#00EEEE',
					'cyan3': '#00CDCD',
					'cyan4': '#008B8B',
					'dark blue': '#00008B',
					'dark cyan': '#008B8B',
					'dark goldenrod': '#B8860B',
					'dark gray': '#A9A9A9',
					'dark green': '#006400',
					'dark grey': '#A9A9A9',
					'dark khaki': '#BDB76B',
					'dark magenta': '#8B008B',
					'dark olive green': '#556B2F',
					'dark orange': '#FF8C00',
					'dark orchid': '#9932CC',
					'dark red': '#8B0000',
					'dark salmon': '#E9967A',
					'dark sea green': '#8FBC8F',
					'dark slate blue': '#483D8B',
					'dark slate gray': '#2F4F4F',
					'dark slate grey': '#2F4F4F',
					'dark turquoise': '#00CED1',
					'dark violet': '#9400D3',
					'DarkBlue': '#00008B',
					'DarkCyan': '#008B8B',
					'DarkGoldenrod': '#B8860B',
					'DarkGoldenrod1': '#FFB90F',
					'DarkGoldenrod2': '#EEAD0E',
					'DarkGoldenrod3': '#CD950C',
					'DarkGoldenrod4': '#8B6508',
					'DarkGray': '#A9A9A9',
					'DarkGreen': '#006400',
					'DarkGrey': '#A9A9A9',
					'DarkKhaki': '#BDB76B',
					'DarkMagenta': '#8B008B',
					'DarkOliveGreen': '#556B2F',
					'DarkOliveGreen1': '#CAFF70',
					'DarkOliveGreen2': '#BCEE68',
					'DarkOliveGreen3': '#A2CD5A',
					'DarkOliveGreen4': '#6E8B3D',
					'DarkOrange': '#FF8C00',
					'DarkOrange1': '#FF7F00',
					'DarkOrange2': '#EE7600',
					'DarkOrange3': '#CD6600',
					'DarkOrange4': '#8B4500',
					'DarkOrchid': '#9932CC',
					'DarkOrchid1': '#BF3EFF',
					'DarkOrchid2': '#B23AEE',
					'DarkOrchid3': '#9A32CD',
					'DarkOrchid4': '#68228B',
					'DarkRed': '#8B0000',
					'DarkSalmon': '#E9967A',
					'DarkSeaGreen': '#8FBC8F',
					'DarkSeaGreen1': '#C1FFC1',
					'DarkSeaGreen2': '#B4EEB4',
					'DarkSeaGreen3': '#9BCD9B',
					'DarkSeaGreen4': '#698B69',
					'DarkSlateBlue': '#483D8B',
					'DarkSlateGray': '#2F4F4F',
					'DarkSlateGray1': '#97FFFF',
					'DarkSlateGray2': '#8DEEEE',
					'DarkSlateGray3': '#79CDCD',
					'DarkSlateGray4': '#528B8B',
					'DarkSlateGrey': '#2F4F4F',
					'DarkTurquoise': '#00CED1',
					'DarkViolet': '#9400D3',
					'deep pink': '#FF1493',
					'deep sky blue': '#00BFFF',
					'DeepPink': '#FF1493',
					'DeepPink1': '#FF1493',
					'DeepPink2': '#EE1289',
					'DeepPink3': '#CD1076',
					'DeepPink4': '#8B0A50',
					'DeepSkyBlue': '#00BFFF',
					'DeepSkyBlue1': '#00BFFF',
					'DeepSkyBlue2': '#00B2EE',
					'DeepSkyBlue3': '#009ACD',
					'DeepSkyBlue4': '#00688B',
					'dim gray': '#696969',
					'dim grey': '#696969',
					'DimGray': '#696969',
					'DimGrey': '#696969',
					'dodger blue': '#1E90FF',
					'DodgerBlue': '#1E90FF',
					'DodgerBlue1': '#1E90FF',
					'DodgerBlue2': '#1C86EE',
					'DodgerBlue3': '#1874CD',
					'DodgerBlue4': '#104E8B',
					'firebrick': '#B22222',
					'firebrick1': '#FF3030',
					'firebrick2': '#EE2C2C',
					'firebrick3': '#CD2626',
					'firebrick4': '#8B1A1A',
					'floral white': '#FFFAF0',
					'FloralWhite': '#FFFAF0',
					'forest green': '#228B22',
					'ForestGreen': '#228B22',
					'gainsboro': '#DCDCDC',
					'ghost white': '#F8F8FF',
					'GhostWhite': '#F8F8FF',
					'gold': '#FFD700',
					'gold1': '#FFD700',
					'gold2': '#EEC900',
					'gold3': '#CDAD00',
					'gold4': '#8B7500',
					'goldenrod': '#DAA520',
					'goldenrod1': '#FFC125',
					'goldenrod2': '#EEB422',
					'goldenrod3': '#CD9B1D',
					'goldenrod4': '#8B6914',
					'green': '#00FF00',
					'green yellow': '#ADFF2F',
					'green1': '#00FF00',
					'green2': '#00EE00',
					'green3': '#00CD00',
					'green4': '#008B00',
					'GreenYellow': '#ADFF2F',
					'grey': '#BEBEBE',
					'grey0': '#000000',
					'grey1': '#030303',
					'grey2': '#050505',
					'grey3': '#080808',
					'grey4': '#0A0A0A',
					'grey5': '#0D0D0D',
					'grey6': '#0F0F0F',
					'grey7': '#121212',
					'grey8': '#141414',
					'grey9': '#171717',
					'grey10': '#1A1A1A',
					'grey11': '#1C1C1C',
					'grey12': '#1F1F1F',
					'grey13': '#212121',
					'grey14': '#242424',
					'grey15': '#262626',
					'grey16': '#292929',
					'grey17': '#2B2B2B',
					'grey18': '#2E2E2E',
					'grey19': '#303030',
					'grey20': '#333333',
					'grey21': '#363636',
					'grey22': '#383838',
					'grey23': '#3B3B3B',
					'grey24': '#3D3D3D',
					'grey25': '#404040',
					'grey26': '#424242',
					'grey27': '#454545',
					'grey28': '#474747',
					'grey29': '#4A4A4A',
					'grey30': '#4D4D4D',
					'grey31': '#4F4F4F',
					'grey32': '#525252',
					'grey33': '#545454',
					'grey34': '#575757',
					'grey35': '#595959',
					'grey36': '#5C5C5C',
					'grey37': '#5E5E5E',
					'grey38': '#616161',
					'grey39': '#636363',
					'grey40': '#666666',
					'grey41': '#696969',
					'grey42': '#6B6B6B',
					'grey43': '#6E6E6E',
					'grey44': '#707070',
					'grey45': '#737373',
					'grey46': '#757575',
					'grey47': '#787878',
					'grey48': '#7A7A7A',
					'grey49': '#7D7D7D',
					'grey50': '#7F7F7F',
					'grey51': '#828282',
					'grey52': '#858585',
					'grey53': '#878787',
					'grey54': '#8A8A8A',
					'grey55': '#8C8C8C',
					'grey56': '#8F8F8F',
					'grey57': '#919191',
					'grey58': '#949494',
					'grey59': '#969696',
					'grey60': '#999999',
					'grey61': '#9C9C9C',
					'grey62': '#9E9E9E',
					'grey63': '#A1A1A1',
					'grey64': '#A3A3A3',
					'grey65': '#A6A6A6',
					'grey66': '#A8A8A8',
					'grey67': '#ABABAB',
					'grey68': '#ADADAD',
					'grey69': '#B0B0B0',
					'grey70': '#B3B3B3',
					'grey71': '#B5B5B5',
					'grey72': '#B8B8B8',
					'grey73': '#BABABA',
					'grey74': '#BDBDBD',
					'grey75': '#BFBFBF',
					'grey76': '#C2C2C2',
					'grey77': '#C4C4C4',
					'grey78': '#C7C7C7',
					'grey79': '#C9C9C9',
					'grey80': '#CCCCCC',
					'grey81': '#CFCFCF',
					'grey82': '#D1D1D1',
					'grey83': '#D4D4D4',
					'grey84': '#D6D6D6',
					'grey85': '#D9D9D9',
					'grey86': '#DBDBDB',
					'grey87': '#DEDEDE',
					'grey88': '#E0E0E0',
					'grey89': '#E3E3E3',
					'grey90': '#E5E5E5',
					'grey91': '#E8E8E8',
					'grey92': '#EBEBEB',
					'grey93': '#EDEDED',
					'grey94': '#F0F0F0',
					'grey95': '#F2F2F2',
					'grey96': '#F5F5F5',
					'grey97': '#F7F7F7',
					'grey98': '#FAFAFA',
					'grey99': '#FCFCFC',
					'grey100': '#FFFFFF',
					'honeydew': '#F0FFF0',
					'honeydew1': '#F0FFF0',
					'honeydew2': '#E0EEE0',
					'honeydew3': '#C1CDC1',
					'honeydew4': '#838B83',
					'hot pink': '#FF69B4',
					'HotPink': '#FF69B4',
					'HotPink1': '#FF6EB4',
					'HotPink2': '#EE6AA7',
					'HotPink3': '#CD6090',
					'HotPink4': '#8B3A62',
					'indian red': '#CD5C5C',
					'IndianRed': '#CD5C5C',
					'IndianRed1': '#FF6A6A',
					'IndianRed2': '#EE6363',
					'IndianRed3': '#CD5555',
					'IndianRed4': '#8B3A3A',
					'ivory': '#FFFFF0',
					'ivory1': '#FFFFF0',
					'ivory2': '#EEEEE0',
					'ivory3': '#CDCDC1',
					'ivory4': '#8B8B83',
					'khaki': '#F0E68C',
					'khaki1': '#FFF68F',
					'khaki2': '#EEE685',
					'khaki3': '#CDC673',
					'khaki4': '#8B864E',
					'lavender': '#E6E6FA',
					'lavender blush': '#FFF0F5',
					'LavenderBlush': '#FFF0F5',
					'LavenderBlush1': '#FFF0F5',
					'LavenderBlush2': '#EEE0E5',
					'LavenderBlush3': '#CDC1C5',
					'LavenderBlush4': '#8B8386',
					'lawn green': '#7CFC00',
					'LawnGreen': '#7CFC00',
					'lemon chiffon': '#FFFACD',
					'LemonChiffon': '#FFFACD',
					'LemonChiffon1': '#FFFACD',
					'LemonChiffon2': '#EEE9BF',
					'LemonChiffon3': '#CDC9A5',
					'LemonChiffon4': '#8B8970',
					'light blue': '#ADD8E6',
					'light coral': '#F08080',
					'light cyan': '#E0FFFF',
					'light goldenrod': '#EEDD82',
					'light goldenrod yellow': '#FAFAD2',
					'light gray': '#D3D3D3',
					'light green': '#90EE90',
					'light grey': '#D3D3D3',
					'light pink': '#FFB6C1',
					'light salmon': '#FFA07A',
					'light sea green': '#20B2AA',
					'light sky blue': '#87CEFA',
					'light slate blue': '#8470FF',
					'light slate gray': '#778899',
					'light slate grey': '#778899',
					'light steel blue': '#B0C4DE',
					'light yellow': '#FFFFE0',
					'LightBlue': '#ADD8E6',
					'LightBlue1': '#BFEFFF',
					'LightBlue2': '#B2DFEE',
					'LightBlue3': '#9AC0CD',
					'LightBlue4': '#68838B',
					'LightCoral': '#F08080',
					'LightCyan': '#E0FFFF',
					'LightCyan1': '#E0FFFF',
					'LightCyan2': '#D1EEEE',
					'LightCyan3': '#B4CDCD',
					'LightCyan4': '#7A8B8B',
					'LightGoldenrod': '#EEDD82',
					'LightGoldenrod1': '#FFEC8B',
					'LightGoldenrod2': '#EEDC82',
					'LightGoldenrod3': '#CDBE70',
					'LightGoldenrod4': '#8B814C',
					'LightGoldenrodYellow': '#FAFAD2',
					'LightGray': '#D3D3D3',
					'LightGreen': '#90EE90',
					'LightGrey': '#D3D3D3',
					'LightPink': '#FFB6C1',
					'LightPink1': '#FFAEB9',
					'LightPink2': '#EEA2AD',
					'LightPink3': '#CD8C95',
					'LightPink4': '#8B5F65',
					'LightSalmon': '#FFA07A',
					'LightSalmon1': '#FFA07A',
					'LightSalmon2': '#EE9572',
					'LightSalmon3': '#CD8162',
					'LightSalmon4': '#8B5742',
					'LightSeaGreen': '#20B2AA',
					'LightSkyBlue': '#87CEFA',
					'LightSkyBlue1': '#B0E2FF',
					'LightSkyBlue2': '#A4D3EE',
					'LightSkyBlue3': '#8DB6CD',
					'LightSkyBlue4': '#607B8B',
					'LightSlateBlue': '#8470FF',
					'LightSlateGray': '#778899',
					'LightSlateGrey': '#778899',
					'LightSteelBlue': '#B0C4DE',
					'LightSteelBlue1': '#CAE1FF',
					'LightSteelBlue2': '#BCD2EE',
					'LightSteelBlue3': '#A2B5CD',
					'LightSteelBlue4': '#6E7B8B',
					'LightYellow': '#FFFFE0',
					'LightYellow1': '#FFFFE0',
					'LightYellow2': '#EEEED1',
					'LightYellow3': '#CDCDB4',
					'LightYellow4': '#8B8B7A',
					'lime green': '#32CD32',
					'LimeGreen': '#32CD32',
					'linen': '#FAF0E6',
					'magenta': '#FF00FF',
					'magenta1': '#FF00FF',
					'magenta2': '#EE00EE',
					'magenta3': '#CD00CD',
					'magenta4': '#8B008B',
					'maroon': '#B03060',
					'maroon1': '#FF34B3',
					'maroon2': '#EE30A7',
					'maroon3': '#CD2990',
					'maroon4': '#8B1C62',
					'medium aquamarine': '#66CDAA',
					'medium blue': '#0000CD',
					'medium orchid': '#BA55D3',
					'medium purple': '#9370DB',
					'medium sea green': '#3CB371',
					'medium slate blue': '#7B68EE',
					'medium spring green': '#00FA9A',
					'medium turquoise': '#48D1CC',
					'medium violet red': '#C71585',
					'MediumAquamarine': '#66CDAA',
					'MediumBlue': '#0000CD',
					'MediumOrchid': '#BA55D3',
					'MediumOrchid1': '#E066FF',
					'MediumOrchid2': '#D15FEE',
					'MediumOrchid3': '#B452CD',
					'MediumOrchid4': '#7A378B',
					'MediumPurple': '#9370DB',
					'MediumPurple1': '#AB82FF',
					'MediumPurple2': '#9F79EE',
					'MediumPurple3': '#8968CD',
					'MediumPurple4': '#5D478B',
					'MediumSeaGreen': '#3CB371',
					'MediumSlateBlue': '#7B68EE',
					'MediumSpringGreen': '#00FA9A',
					'MediumTurquoise': '#48D1CC',
					'MediumVioletRed': '#C71585',
					'midnight blue': '#191970',
					'MidnightBlue': '#191970',
					'mint cream': '#F5FFFA',
					'MintCream': '#F5FFFA',
					'misty rose': '#FFE4E1',
					'MistyRose': '#FFE4E1',
					'MistyRose1': '#FFE4E1',
					'MistyRose2': '#EED5D2',
					'MistyRose3': '#CDB7B5',
					'MistyRose4': '#8B7D7B',
					'moccasin': '#FFE4B5',
					'navajo white': '#FFDEAD',
					'NavajoWhite': '#FFDEAD',
					'NavajoWhite1': '#FFDEAD',
					'NavajoWhite2': '#EECFA1',
					'NavajoWhite3': '#CDB38B',
					'NavajoWhite4': '#8B795E',
					'navy': '#000080',
					'navy blue': '#000080',
					'NavyBlue': '#000080',
					'old lace': '#FDF5E6',
					'OldLace': '#FDF5E6',
					'olive drab': '#6B8E23',
					'OliveDrab': '#6B8E23',
					'OliveDrab1': '#C0FF3E',
					'OliveDrab2': '#B3EE3A',
					'OliveDrab3': '#9ACD32',
					'OliveDrab4': '#698B22',
					'orange': '#FFA500',
					'orange red': '#FF4500',
					'orange1': '#FFA500',
					'orange2': '#EE9A00',
					'orange3': '#CD8500',
					'orange4': '#8B5A00',
					'OrangeRed': '#FF4500',
					'OrangeRed1': '#FF4500',
					'OrangeRed2': '#EE4000',
					'OrangeRed3': '#CD3700',
					'OrangeRed4': '#8B2500',
					'orchid': '#DA70D6',
					'orchid1': '#FF83FA',
					'orchid2': '#EE7AE9',
					'orchid3': '#CD69C9',
					'orchid4': '#8B4789',
					'pale goldenrod': '#EEE8AA',
					'pale green': '#98FB98',
					'pale turquoise': '#AFEEEE',
					'pale violet red': '#DB7093',
					'PaleGoldenrod': '#EEE8AA',
					'PaleGreen': '#98FB98',
					'PaleGreen1': '#9AFF9A',
					'PaleGreen2': '#90EE90',
					'PaleGreen3': '#7CCD7C',
					'PaleGreen4': '#548B54',
					'PaleTurquoise': '#AFEEEE',
					'PaleTurquoise1': '#BBFFFF',
					'PaleTurquoise2': '#AEEEEE',
					'PaleTurquoise3': '#96CDCD',
					'PaleTurquoise4': '#668B8B',
					'PaleVioletRed': '#DB7093',
					'PaleVioletRed1': '#FF82AB',
					'PaleVioletRed2': '#EE799F',
					'PaleVioletRed3': '#CD687F',
					'PaleVioletRed4': '#8B475D',
					'papaya whip': '#FFEFD5',
					'PapayaWhip': '#FFEFD5',
					'peach puff': '#FFDAB9',
					'PeachPuff': '#FFDAB9',
					'PeachPuff1': '#FFDAB9',
					'PeachPuff2': '#EECBAD',
					'PeachPuff3': '#CDAF95',
					'PeachPuff4': '#8B7765',
					'peru': '#CD853F',
					'pink': '#FFC0CB',
					'pink1': '#FFB5C5',
					'pink2': '#EEA9B8',
					'pink3': '#CD919E',
					'pink4': '#8B636C',
					'plum': '#DDA0DD',
					'plum1': '#FFBBFF',
					'plum2': '#EEAEEE',
					'plum3': '#CD96CD',
					'plum4': '#8B668B',
					'powder blue': '#B0E0E6',
					'PowderBlue': '#B0E0E6',
					'purple': '#A020F0',
					'purple1': '#9B30FF',
					'purple2': '#912CEE',
					'purple3': '#7D26CD',
					'purple4': '#551A8B',
					'red': '#FF0000',
					'red1': '#FF0000',
					'red2': '#EE0000',
					'red3': '#CD0000',
					'red4': '#8B0000',
					'rosy brown': '#BC8F8F',
					'RosyBrown': '#BC8F8F',
					'RosyBrown1': '#FFC1C1',
					'RosyBrown2': '#EEB4B4',
					'RosyBrown3': '#CD9B9B',
					'RosyBrown4': '#8B6969',
					'royal blue': '#4169E1',
					'RoyalBlue': '#4169E1',
					'RoyalBlue1': '#4876FF',
					'RoyalBlue2': '#436EEE',
					'RoyalBlue3': '#3A5FCD',
					'RoyalBlue4': '#27408B',
					'saddle brown': '#8B4513',
					'SaddleBrown': '#8B4513',
					'salmon': '#FA8072',
					'salmon1': '#FF8C69',
					'salmon2': '#EE8262',
					'salmon3': '#CD7054',
					'salmon4': '#8B4C39',
					'sandy brown': '#F4A460',
					'SandyBrown': '#F4A460',
					'sea green': '#2E8B57',
					'SeaGreen': '#2E8B57',
					'SeaGreen1': '#54FF9F',
					'SeaGreen2': '#4EEE94',
					'SeaGreen3': '#43CD80',
					'SeaGreen4': '#2E8B57',
					'seashell': '#FFF5EE',
					'seashell1': '#FFF5EE',
					'seashell2': '#EEE5DE',
					'seashell3': '#CDC5BF',
					'seashell4': '#8B8682',
					'sienna': '#A0522D',
					'sienna1': '#FF8247',
					'sienna2': '#EE7942',
					'sienna3': '#CD6839',
					'sienna4': '#8B4726',
					'sky blue': '#87CEEB',
					'SkyBlue': '#87CEEB',
					'SkyBlue1': '#87CEFF',
					'SkyBlue2': '#7EC0EE',
					'SkyBlue3': '#6CA6CD',
					'SkyBlue4': '#4A708B',
					'slate blue': '#6A5ACD',
					'slate gray': '#708090',
					'slate grey': '#708090',
					'SlateBlue': '#6A5ACD',
					'SlateBlue1': '#836FFF',
					'SlateBlue2': '#7A67EE',
					'SlateBlue3': '#6959CD',
					'SlateBlue4': '#473C8B',
					'SlateGray': '#708090',
					'SlateGray1': '#C6E2FF',
					'SlateGray2': '#B9D3EE',
					'SlateGray3': '#9FB6CD',
					'SlateGray4': '#6C7B8B',
					'SlateGrey': '#708090',
					'snow': '#FFFAFA',
					'snow1': '#FFFAFA',
					'snow2': '#EEE9E9',
					'snow3': '#CDC9C9',
					'snow4': '#8B8989',
					'spring green': '#00FF7F',
					'SpringGreen': '#00FF7F',
					'SpringGreen1': '#00FF7F',
					'SpringGreen2': '#00EE76',
					'SpringGreen3': '#00CD66',
					'SpringGreen4': '#008B45',
					'steel blue': '#4682B4',
					'SteelBlue': '#4682B4',
					'SteelBlue1': '#63B8FF',
					'SteelBlue2': '#5CACEE',
					'SteelBlue3': '#4F94CD',
					'SteelBlue4': '#36648B',
					'tan': '#D2B48C',
					'tan1': '#FFA54F',
					'tan2': '#EE9A49',
					'tan3': '#CD853F',
					'tan4': '#8B5A2B',
					'thistle': '#D8BFD8',
					'thistle1': '#FFE1FF',
					'thistle2': '#EED2EE',
					'thistle3': '#CDB5CD',
					'thistle4': '#8B7B8B',
					'tomato': '#FF6347',
					'tomato1': '#FF6347',
					'tomato2': '#EE5C42',
					'tomato3': '#CD4F39',
					'tomato4': '#8B3626',
					'turquoise': '#40E0D0',
					'turquoise1': '#00F5FF',
					'turquoise2': '#00E5EE',
					'turquoise3': '#00C5CD',
					'turquoise4': '#00868B',
					'violet': '#EE82EE',
					'violet red': '#D02090',
					'VioletRed': '#D02090',
					'VioletRed1': '#FF3E96',
					'VioletRed2': '#EE3A8C',
					'VioletRed3': '#CD3278',
					'VioletRed4': '#8B2252',
					'wheat': '#F5DEB3',
					'wheat1': '#FFE7BA',
					'wheat2': '#EED8AE',
					'wheat3': '#CDBA96',
					'wheat4': '#8B7E66',
					'white': '#FFFFFF',
					'white smoke': '#F5F5F5',
					'WhiteSmoke': '#F5F5F5',
					'yellow': '#FFFF00',
					'yellow green': '#9ACD32',
					'yellow1': '#FFFF00',
					'yellow2': '#EEEE00',
					'yellow3': '#CDCD00',
					'yellow4': '#8B8B00',
					'YellowGreen': '#9ACD32' }
			_hextocolor = { v: k for k, v in _colormap.items( ) }
			_colorlist = list( _colormap.keys( ) )
			COLORS_PER_ROW = 40
			_fontsize = 9

			def make_window( ):
				_layout = [ [ sg.Text( ), ],
				            [ sg.Text( f'{len( _colorlist )} Colors', font = self.__themefont ), ],
				            [ sg.Text( size = (5, 1) ), ] ]

				for rows in range( len( _colorlist ) // COLORS_PER_ROW + 1 ):
					_row = [ ]

					for i in range( COLORS_PER_ROW ):
						try:
							color = _colorlist[ rows * COLORS_PER_ROW + i ]
							_row.append(
								sg.Text( ' ', s = 1, background_color = color, text_color = color,
									font = self.__themefont,
									right_click_menu = [ '_', _colormap[ color ] ],
									tooltip = color, enable_events = True,
									key = (color, _colormap[ color ]) ) )
						except IndexError as e:
							break
						except Exception as e:
							sg.popup_error( f'Error while creating _color _window....', e,
								f'rows = {rows}  i = {i}' )
							break
					_layout.append( _row )
				_layout.append( [ sg.Text( ' ', size = (10, 1) ), ] )
				_layout.append( [ sg.Text( ' ', size = (10, 1) ), ] )
				_layout.append( [ sg.Text( ' ', size = (50, 1) ), sg.Cancel( size = ( 20, 1 ) ), ] )

				return sg.Window( ' Budget Execution', _layout,
					font = self.__themefont,
					size = self.__formsize,
					element_padding = (1, 1),
					border_depth = 0,
					icon = self.__icon,
					right_click_menu = sg.MENU_RIGHT_CLICK_EDITME_EXIT,
					use_ttk_buttons = True )

			_window = make_window( )

			while True:
				_event, _values = _window.read( )
				if _event in (sg.WIN_CLOSED, 'Cancel', 'Exit'):
					break
				if _event == 'Edit me':
					sg.execute_editor( __file__ )
					continue
				elif isinstance( _event, tuple ):
					_color, _colorhex = _event[ 0 ], _event[ 1 ]
				else:
					_color, _colorhex = _hextocolor[ _event ], _event

				_layout2 = [ [ sg.Text( _colorhex + ' on clipboard' ) ],
				             [ sg.DummyButton( _color, button_color = self.__buttoncolor,
					            tooltip = _colorhex ),
				              sg.DummyButton( _color, button_color = self.__buttoncolor,
					              tooltip = _colorhex ) ] ]

				_window2 = sg.Window( 'Buttons with white and black text', _layout2,
					keep_on_top = True,
					finalize = True,
					size = self.__formsize,
					icon = self.__icon )

				sg.clipboard_set( _colorhex )

			_window.close( )

			sg.popup_quick_message( 'Building _window... one moment please...',
				background_color = self.__themebackground,
				icon = self.__icon,
				text_color = self.__themetextcolor,
				font = self.__themefont )

			sg.set_options( button_element_size = (12, 1),
				element_padding = (0, 0),
				auto_size_buttons = False,
				border_width = 1,
				tooltip_time = 100 )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'ColorDialog'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class BudgetForm( Sith ):
	'''
    Constructor:
    BudgetForm( )

    Purpose:
    Class defining basic dashboard for the application
    '''
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
	def title_items( self ) -> str:
		if self.__titleitems is not None:
			return self.__titleitems

	@title_items.setter
	def title_items( self, value: str ):
		if value is not None:
			self.__titleitems = value

	@property
	def header_items( self ) -> str:
		if self.__headeritems is not None:
			return self.__headeritems

	@header_items.setter
	def header_items( self, value: str ):
		if value is not None:
			self.__headeritems = value

	@property
	def first_items( self ) -> str:
		if self.__firstitems is not None:
			return self.__firstitems

	@first_items.setter
	def first_items( self, value: str ):
		if value is not None:
			self.__firstitems = value

	@property
	def second_items( self ) -> str:
		if self.__seconditems is not None:
			return self.__seconditems

	@second_items.setter
	def second_items( self, value: str ):
		if value is not None:
			self.__seconditems = value

	@property
	def third_items( self ) -> str:
		if self.__thirditems is not None:
			return self.__thirditems

	@third_items.setter
	def third_items( self, value: str ):
		if value is not None:
			self.__thirditems = value

	@property
	def fourth_items( self ) -> str:
		if self.__fourthitems is not None:
			return self.__fourthitems

	@fourth_items.setter
	def fourth_items( self, value: str ):
		if value is not None:
			self.__fourthitems = value

	@property
	def form_size( self ) -> (int, int):
		if self.__formsize is not None:
			return self.__formsize

	@form_size.setter
	def form_size( self, value: (int, int) ):
		if value is not None:
			self.__formsize = value

	@property
	def image( self ) -> str:
		if self.__image is not None:
			return self.__image

	@image.setter
	def image( self, value: str ):
		if value is not None:
			self.__image = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = (1200, 650)
		self.__image = os.getcwd( ) + r'\etc\img\BudgetEx.png'

	def create_title( self, items: list ) -> list:
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		if items is not None:
			try:
				_blu = '#051F3D'
				_blk = '#101010'
				_mblk = '#1E1E1E'
				BPAD_TOP = ((5, 5), (5, 5))
				BPAD_LEFT = ((5, 5), (5, 5))
				BPAD_LEFT_INSIDE = (5, (3, 5))
				BPAD_RIGHT = ((5, 10), (3, 3))
				_font = 'Roboto 20'
				_form = (450, 150)
				_hdrsz = (920, 100)
				_title = [
						[ sg.Text( f'{items[ 0 ]}', font = _font, background_color = _mblk,
							enable_events = True, grab = False ),
						  sg.Push( background_color = _mblk ),
						  sg.Text( f'{items[ 1 ]}', font = _font, background_color = _mblk ) ],
				]
				self.__titlelayout = _title
				return _title
			except Exception as e:
				_exc = Error( e )
				_exc.module = 'Booger'
				_exc.cause = 'BudgetForm'
				_exc.method = 'create_title( self, items )'
				_err = ErrorDialog( _exc )
				_err.show( )

	def create_header( self, items: list ) -> list:
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		if items is not None:
			try:
				_blu = '#051F3D'
				_blk = '#101010'
				_mblk = '#1E1E1E'
				BPAD_TOP = ((5, 5), (5, 5))
				BPAD_LEFT = ((5, 5), (5, 5))
				BPAD_LEFT_INSIDE = (5, (3, 5))
				BPAD_RIGHT = ((5, 10), (3, 3))
				_hdr = 'Roboto 20'
				_frasz = (450, 150)
				_hdrsz = (920, 100)
				_header = [ [ sg.Push( ), sg.Text( f'{items[ 0 ]}', font = _hdr ), sg.Push( ) ],
				            [ sg.Text( f'{items[ 1 ]}' ) ],
				            [ sg.Text( f'{items[ 2 ]}' ) ] ]
				self.__headerlayout = _header
				return _header
			except Exception as e:
				_exc = Error( e )
				_exc.module = 'Booger'
				_exc.cause = 'BudgetForm'
				_exc.method = 'create_header( self, items )'
				_err = ErrorDialog( _exc )
				_err.show( )

	def create_first( self, items: list ) -> list:
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		if items is not None:
			try:
				_blu = '#051F3D'
				_blk = '#101010'
				_mblk = '#1E1E1E'
				BPAD_TOP = ((5, 5), (5, 5))
				BPAD_LEFT = ((5, 5), (5, 5))
				BPAD_LEFT_INSIDE = (5, (3, 5))
				BPAD_RIGHT = ((5, 10), (3, 3))
				_hdr = 'Roboto 20'
				_frasz = (450, 150)
				_hdrsz = (920, 100)
				_first = [ [ sg.Push( ), sg.Text( 'Block 1 Header', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 1 line 1', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 1 line 2', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 1 line 3', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 1 line 4', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 1 line 5', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 1 line 6', font = _hdr ), sg.Push( ) ] ]
				self.__firstlayout = _first
				return _first
			except Exception as e:
				_exc = Error( e )
				_exc.module = 'Booger'
				_exc.cause = 'BudgetForm'
				_exc.method = 'setfirsttext( self, items )'
				_err = ErrorDialog( _exc )
				_err.show( )

	def create_second( self, items: list ) -> list:
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		if items is not None:
			try:
				_blu = '#051F3D'
				_blk = '#101010'
				_mblk = '#1E1E1E'
				BPAD_TOP = ((5, 5), (5, 5))
				BPAD_LEFT = ((5, 5), (5, 5))
				BPAD_LEFT_INSIDE = (5, (3, 5))
				BPAD_RIGHT = ((5, 10), (3, 3))
				_hdr = 'Roboto 20'
				_frasz = (450, 150)
				_hdrsz = (920, 100)
				_second = [ [ sg.Push( ), sg.Text( 'Block 2 Header', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 2 line 1', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 2 line 2', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 2 line 3', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 2 line 4', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 2 line 5', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 2 line 6', font = _hdr ), sg.Push( ) ] ]
				self.__secondlayout = _second
				return _second
			except Exception as e:
				_exc = Error( e )
				_exc.module = 'Booger'
				_exc.cause = 'BudgetForm'
				_exc.method = 'create_second( self, items )'
				_err = ErrorDialog( _exc )
				_err.show( )

	def create_third( self, items: list ) -> list:
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		if items is not None:
			try:
				_blu = '#051F3D'
				_blk = '#101010'
				_mblk = '#1E1E1E'
				BPAD_TOP = ((5, 5), (5, 5))
				BPAD_LEFT = ((5, 5), (5, 5))
				BPAD_LEFT_INSIDE = (5, (3, 5))
				BPAD_RIGHT = ((5, 10), (3, 3))
				_hdr = 'Roboto 20'
				_frasz = (450, 150)
				_hdrsz = (920, 100)
				_third = [ [ sg.Push( ), sg.Text( 'Block 3 Header', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 3 line 1', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 3 line 2', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 3 line 3', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 3 line 4', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 3 line 5', font = _hdr ), sg.Push( ) ],
				           [ sg.Push( ), sg.Text( 'Block 3 line 6', font = _hdr ), sg.Push( ) ] ]
				self.__thirdlayout = _third
				return _third
			except Exception as e:
				_exc = Error( e )
				_exc.module = 'Booger'
				_exc.cause = 'BudgetForm'
				_exc.method = 'create_third( self, items: list )'
				_err = ErrorDialog( _exc )
				_err.show( )

	def create_fourth( self, items: list ) -> list:
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		if items is not None:
			try:
				_blu = '#051F3D'
				_blk = '#101010'
				_mblk = '#1E1E1E'
				BPAD_TOP = ((5, 5), (5, 5))
				BPAD_LEFT = ((5, 5), (5, 5))
				BPAD_LEFT_INSIDE = (5, (3, 5))
				BPAD_RIGHT = ((5, 10), (3, 3))
				_hdr = 'Roboto 20'
				_frasz = (450, 150)
				_hdrsz = (920, 100)
				_fourth = [ [ sg.Push( ), sg.Text( 'Block 4 Header', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 4 line 1', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 4 line 2', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 4 line 3', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 4 line 4', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 4 line 5', font = _hdr ), sg.Push( ) ],
				            [ sg.Push( ), sg.Text( 'Block 4 line 6', font = _hdr ), sg.Push( ) ] ]
				self.__fourthlayout = _fourth
				return _fourth
			except Exception as e:
				_exc = Error( e )
				_exc.module = 'Booger'
				_exc.cause = 'BudgetForm'
				_exc.method = 'create_fourth( self, items: list )'
				_err = ErrorDialog( _exc )
				_err.show( )

	def set_layout( self ) -> list:
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_blu = '#051F3D'
			_blk = '#101010'
			_mblk = '#1E1E1E'
			BPAD_TOP = ((5, 5), (5, 5))
			BPAD_LEFT = ((5, 5), (5, 5))
			BPAD_LEFT_INSIDE = (5, (5, 5))
			BPAD_RIGHT = ((5, 5), (5, 5))
			_hdr = 'Roboto 20'
			_li = 'Roboto 10'
			_frasz = (450, 150)
			_hdrsz = (920, 100)
			_layout = [
					[ sg.Frame( '', self.__titlelayout, pad = (0, 0), background_color = _mblk,
						expand_x = True,
						border_width = 0, grab = True ) ],
					[ sg.Frame( '', self.__headerlayout, size = _hdrsz, pad = BPAD_TOP,
						expand_x = True,
						relief = sg.RELIEF_FLAT, border_width = 0 ) ],
					[ sg.Frame( '',
						[ [ sg.Frame( '', self.__firstlayout, size = _frasz, pad =
						BPAD_LEFT_INSIDE,
							border_width = 0, expand_x = True, expand_y = True, ) ],
						  [ sg.Frame( '', self.__thirdlayout, size = _frasz, pad =
						  BPAD_LEFT_INSIDE,
							  border_width = 0, expand_x = True, expand_y = True ) ] ],
						pad = BPAD_LEFT, background_color = _blk, border_width = 0,
						expand_x = True, expand_y = True ),
					  sg.Frame( '',
						  [ [ sg.Frame( '', self.__secondlayout, size = _frasz,
							  pad = BPAD_LEFT_INSIDE,
							  border_width = 0, expand_x = True, expand_y = True ) ],
						    [ sg.Frame( '', self.__fourthlayout, size = _frasz,
							    pad = BPAD_LEFT_INSIDE,
							    border_width = 0, expand_x = True, expand_y = True ) ] ],
						  pad = BPAD_LEFT, background_color = _blk, border_width = 0,
						  expand_x = True, expand_y = True ), ],
					[ sg.Sizegrip( background_color = _mblk ) ] ]
			self.__formlayout = _layout
			return _layout
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'BudgetForm'
			_exc.method = 'set_layout( self, items )'
			_err = ErrorDialog( _exc )
			_err.show( )

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_blu = '#051F3D'
			_blk = '#101010'
			_mblk = '#1E1E1E'
			BPAD_TOP = ((5, 5), (5, 5))
			BPAD_LEFT = ((5, 5), (5, 5))
			BPAD_LEFT_INSIDE = (5, (5, 5))
			BPAD_RIGHT = ((5, 5), (5, 5))
			_hdr = 'Roboto 20'
			_li = 'Roboto 10'
			_frasz = (450, 150)
			_hdrsz = (920, 100)
			self.__titlelayout = [
					[ sg.Text( 'Budget Execution', font = _hdr, background_color = _mblk,
						enable_events = True, grab = False ), sg.Push( background_color = _mblk ),
					  sg.Text( 'Wednesday 27 Oct 2021', font = _hdr, background_color = _mblk ) ],
			]
			self.__headerlayout = [ [ sg.Push( ), sg.Text( 'Top Header', font = _hdr ), sg.Push(
			) ],
			                        [ sg.Image( source = self.__image, subsample = 3,
				                        enable_events = True ), sg.Push( ) ],
			                        [ sg.Text( 'Top Header line 2' ), sg.Push( ) ] ]
			self.__firstlayout = [
					[ sg.Push( ), sg.Text( 'Block 1 Header', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 1 line 1', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 1 line 2', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 1 line 3', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 1 line 4', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 1 line 5', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 1 line 6', font = _hdr ), sg.Push( ) ] ]
			self.__secondlayout = [
					[ sg.Push( ), sg.Text( 'Block 2 Header', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 2 line 1', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 2 line 2', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 2 line 3', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 2 line 4', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 2 line 5', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 2 line 6', font = _hdr ), sg.Push( ) ] ]
			self.__thirdlayout = [
					[ sg.Push( ), sg.Text( 'Block 3 Header', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 3 line 1', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 3 line 2', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 3 line 3', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 3 line 4', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 3 line 5', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 3 line 6', font = _hdr ), sg.Push( ) ] ]
			self.__fourthlayout = [
					[ sg.Push( ), sg.Text( 'Block 4 Header', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 4 line 1', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 4 line 2', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 4 line 3', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 4 line 4', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 4 line 5', font = _hdr ), sg.Push( ) ],
					[ sg.Push( ), sg.Text( 'Block 4 line 6', font = _hdr ), sg.Push( ) ] ]
			self.__formlayout = [
					[ sg.Frame( '', self.__titlelayout, pad = (0, 0), background_color = _mblk,
						expand_x = True, border_width = 0, grab = True ) ],
					[ sg.Frame( '',
						[ [ sg.Frame( '', self.__headerlayout, size = _frasz, pad = BPAD_TOP,
							expand_x = True,
							relief = sg.RELIEF_FLAT, border_width = 0 ) ] ], pad = BPAD_LEFT,
						background_color = _blu, border_width = 0, expand_x = True ), ],
					[ sg.Frame( '',
						[ [ sg.Frame( '', self.__firstlayout, size = _frasz, pad =
						BPAD_LEFT_INSIDE,
							border_width = 0, expand_x = True, expand_y = True, ) ],
						  [ sg.Frame( '', self.__thirdlayout, size = _frasz, pad =
						  BPAD_LEFT_INSIDE,
							  border_width = 0, expand_x = True, expand_y = True ) ] ],
						pad = BPAD_LEFT, background_color = _blu, border_width = 0,
						expand_x = True, expand_y = True ),
					  sg.Frame( '',
						  [ [ sg.Frame( '', self.__secondlayout, size = _frasz,
							  pad = BPAD_LEFT_INSIDE,
							  border_width = 0, expand_x = True, expand_y = True ) ],
						    [ sg.Frame( '', self.__fourthlayout, size = _frasz,
							    pad = BPAD_LEFT_INSIDE,
							    border_width = 0, expand_x = True, expand_y = True ) ] ],
						  pad = BPAD_LEFT, background_color = _blu, border_width = 0,
						  expand_x = True, expand_y = True ), ],
					[ sg.Sizegrip( background_color = _mblk ) ] ]
			_window = sg.Window( '  Budget Execution', self.__formlayout,
				size = self.__formsize,
				margins = (0, 0),
				background_color = _blk,
				grab_anywhere = True,
				no_titlebar = True,
				resizable = True,
				right_click_menu = sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT )
			while True:
				_event, _values = _window.read( )
				print( _event, _values )
				if _event == sg.WIN_CLOSED or _event == 'Exit':
					break
				elif _event == 'Edit Me':
					sg.execute_editor( __file__ )
				elif _event == 'Version':
					sg.popup_scrolled( sg.get_versions( ), keep_on_top = True )
				elif _event == 'File Location':
					sg.popup_scrolled( 'This Python file is:', __file__ )
			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'BudgetForm'
			_exc.method = 'show( self)'
			_err = ErrorDialog( _exc )
			_err.show( )

class ChartPanel( Sith ):
	'''
    Constructor:
    ChartPanel( )

    Purpose:
    Provides form with a bar chart
    '''
	@property
	def header( self ) -> str:
		if self.__header is not None:
			return self.__header

	@header.setter
	def header( self, value: str ):
		if value is not None:
			self.__header = value

	def __init__( self ):
		super( ).__init__( )
		sg.theme( 'DarkGrey15' )
		self.__icon = super( ).icon_path
		self.__formsize = ( 750, 650 )

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_sm = ( 10, 1 )
			_md = ( 15, 1 )
			_lg = ( 20, 1 )
			_xl = ( 100, 1 )
			_width = 50
			_space = 75
			_offset = 3
			_graphsz = _datasz = (500, 500)
			_black = sg.theme_background_color( )

			_layout = [ [ sg.Text( size = _sm ), sg.Text( size = _xl ) ],
			            [ sg.Text( size = _sm ),
			              sg.Graph( _graphsz, ( 0, 0 ), _datasz, k = '-GRAPH-' ) ],
			            [ sg.Text( size = _sm ), sg.Text( size = _xl ) ],
			            [ sg.Text( size = _lg ), sg.Button( 'Next', size = _md ),
			             sg.Text( size = _lg ), sg.Exit( size = _md ) ],
			            [ sg.Sizegrip( background_color = _black ) ] ]

			_window = sg.Window( 'Budget Execution', _layout,
				finalize = True,
				resizable = True,
				icon = self.__icon,
				font = self.__themefont,
				size = self.__formsize )

			_graph = _window[ '-GRAPH-' ]

			while True:
				_graph.erase( )
				for i in range( 7 ):
					_item = random.randint( 0, _graphsz[ 1 ] )
					_graph.draw_rectangle( top_left = ( i * _space + _offset, _item ),
						bottom_right = ( i * _space + _offset + _width, 0 ),
						fill_color = sg.theme_button_color_background( ),
						line_color = sg.theme_button_color_text( ) )

					_graph.draw_text( text = _item, color = '#FFFFFF',
						location = ( i * _space + _offset + 25, _item + 10 ) )

				_event, _values = _window.read( )
				if _event in ( sg.WIN_CLOSED, 'Exit' ):
					break

			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'ChartForm'
			_exc.method = 'show( self)'
			_err = ErrorDialog( _exc )
			_err.show( )

class CsvForm( Sith ):
	'''
	Construcotr:
	CsvForm( )

	Purpose:
	Provides form that reads CSV file with pandas
	'''

	@property
	def header( self ) -> str:
		if self.__header is not None:
			return self.__header

	@header.setter
	def header( self, value: str ):
		if value is not None:
			self.__header = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = (800, 600)

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_sm = (3, 1)
			_med = (15, 1)
			_spc = (25, 1)
			_dialog = FileDialog( )
			_dialog.show( )
			_path = _dialog.selected_path

			if _path == '':
				_msg = MessageDialog( 'No file path was provided!' )
				_msg.show( )
				return

			_data = [ ]
			_header = [ ]

			_button = sg.popup_yes_no( 'Does file have column column_names?',
				icon = self.__icon,
				font = self.__themefont )

			if _path is not None:
				try:
					_frame = CsvReader( _path, sep = ',', engine = 'python', header = None )
					_data = _frame.values.tolist( )
					if _button == 'Yes':
						_header = _frame.iloc[ 0 ].tolist( )
						_data = _frame[ 1: ].values.tolist( )
					elif _button == 'No':
						_header = [ 'Column' + str( x ) for x in range( len( _data[ 0 ] ) ) ]
				except Exception:
					sg.popup_error( 'Error reading file' )
					return

			_left = [ [ sg.Text( size = _sm ), ] ]
			_right = [ [ sg.Text( size = _sm ), ] ]
			_datagrid = [ [ sg.Table( values = _data, headings = _header, justification = 'center',
				row_height = 18, display_row_numbers = True, vertical_scroll_only = False,
				header_background_color = '#1B262E', header_relief = sg.RELIEF_FLAT,
				header_border_width = 1, selected_row_colors = ('#FFFFFF', '#4682B4'),
				header_text_color = '#FFFFFF', header_font = ('Roboto', 8, 'bold'),
				font = ('Roboto', 8), background_color = '#EDF3F8',
				alternating_row_color = '#EDF3F8', border_width = 1, text_color = '#000000',
				expand_x = True, expand_y = True, sbar_relief = sg.RELIEF_FLAT,
				num_rows = min( 26, len( _data ) ) ), ], ]
			_window = sg.Window( '  Budget Execution', _datagrid, icon = self.__icon,
				font = self.__themefont, resizable = True )
			_event, _values = _window.read( )
			_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'CsvForm'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class ExcelForm( Sith ):
	'''
	Construcotr:
	ExcelForm( )

	Purpose:
	Provides form that reads CSV file with pandas
	'''

	@property
	def header( self ) -> str:
		if self.__header is not None:
			return self.__header

	@header.setter
	def header( self, value: str ):
		if value is not None:
			self.__header = value

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = (1350, 700)

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		try:
			_small = (3, 1)
			_med = (15, 1)
			_spc = (25, 1)
			_dialog = FileDialog( )
			_dialog.show( )
			_filename = _dialog.selected_path

			if _filename == '':
				_msg = MessageDialog( 'No file was provided!' )
				_msg.show( )
				return

			_data = [ ]
			_header = [ ]

			_button = sg.popup_yes_no( 'First Row Has Headers?',
				title = 'Headers?',
				icon = self.__icon,
				font = ('Roboto', 9) )
			if _filename is not None:
				try:
					_dataframe = ExcelReader( _filename, index_col = 0 )
					_data = _dataframe.values.tolist( )
					if _button == 'Yes':
						_header = [ f'{i} ' for i in _dataframe.columns ]
					elif _button == 'No':
						_header = [ 'Column - ' + str( x ) for x in range( len( _data[ 0 ] ) ) ]
				except:
					sg.popup_error( 'Error reading file' )
					return
			_left = [ [ sg.Text( size = _small ), ] ]
			_right = [ [ sg.Text( size = _small ), ] ]
			_datagrid = [ [ sg.Table( values = _data, headings = _header, justification = 'center',
				row_height = 18, display_row_numbers = True, vertical_scroll_only = False,
				header_background_color = '#1B262E', header_relief = sg.RELIEF_FLAT,
				header_border_width = 1, selected_row_colors = ('#FFFFFF', '#4682B4'),
				header_text_color = '#FFFFFF', header_font = ('Roboto', 8, 'bold'),
				font = ('Roboto', 8), background_color = '#EDF3F8',
				alternating_row_color = '#EDF3F8', border_width = 1, text_color = '#000000',
				expand_x = True, expand_y = True, sbar_relief = sg.RELIEF_FLAT,
				num_rows = min( 26, len( _data ) ) ), ], ]
			_layout = [ [ sg.Text( size = (3, 3) ) ],
			            [ sg.Column( _left, expand_x = True ),
			              sg.Column( _datagrid, expand_x = True, expand_y = True ),
			              sg.Column( _right, expand_x = True ) ],
			            [ sg.Text( size = _small ) ],
			            [ sg.Text( size = (10, 1) ), sg.Button( 'Open', size = _med,
				            key = '-OPEN-' ),
			              sg.Text( size = _spc ), sg.Button( 'Export', size = _med,
				            key = '-EXPORT-' ),
			              sg.Text( size = _spc ), sg.Button( 'Save', size = _med, key = '-SAVE-' ),
			              sg.Text( size = _spc ), sg.Button( 'Close', size = _med, key = '-CLOSE-'
			            ) ],
			            [ sg.Sizegrip( ) ], ]
			_window = sg.Window( ' Budget Execution', _layout,
				size = self.__formsize,
				grab_anywhere = True,
				icon = self.__icon,
				font = self.__themefont,
				resizable = True,
				right_click_menu = sg.MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT )
			_event, _values = _window.read( )
			if _event in (sg.WIN_X_EVENT, '-CLOSE-'):
				_window.close( )
			elif _event in ('-OPEN-', '-EXPORT-', '-SAVE-', 'Save'):
				_info = 'Not Yet Implemented!'
				_msg = MessageDialog( _info )
				_msg.show( )
				_window.close( )
		except Exception as e:
			_exc = Error( e )
			_exc.module = 'Booger'
			_exc.cause = 'ExcelForm'
			_exc.method = 'show( self )'
			_err = ErrorDialog( _exc )
			_err.show( )

class GraphForm( Sith ):
	'''
	Construcotr:
	GraphForm( )

	Purpose:
	Provides form that reads CSV file with pandas
	'''

	def __init__( self ):
		super( ).__init__( )
		self.__themebackground = super( ).theme_background
		self.__themefont = super( ).theme_font
		self.__icon = super( ).icon_path
		self.__elementbackcolor = super( ).element_backcolor
		self.__elementforecolor = super( ).element_forecolor
		self.__themetextcolor = super( ).text_forecolor
		self.__textbackcolor = super( ).text_backcolor
		self.__inputbackcolor = super( ).input_backcolor
		self.__inputforecolor = super( ).input_forecolor
		self.__buttoncolor = super( ).button_color
		self.__formsize = (800, 600)

	def show( self ):
		'''
		Purpose:

		Parameters:

		Returns:
		'''
		def create_axis_grid( ):
			plt.close( 'all' )

			def get_demo_image( ):
				_delta = 0.5
				_extent = (-3, 4, -4, 3)
				_xaxis = np.arange( -3.0, 4.001, _delta )
				_yaxis = np.arange( -4.0, 3.001, _delta )
				_X, _Y = np.meshgrid( _xaxis, _yaxis )
				_Z1 = np.exp( -_X ** 2 - _Y ** 2 )
				_Z2 = np.exp( -(_X - 1) ** 2 - (_Y - 1) ** 2 )
				_Z = (_Z1 - _Z2) * 2

				return _Z, _extent

			def get_rgb( ):
				_Z, _extent = get_demo_image( )
				_Z[ _Z < 0 ] = 0.
				_Z = _Z / _Z.max( )
				_red = _Z[ :13, :13 ]
				_green = _Z[ 2:, 2: ]
				_blue = _Z[ :13, 2: ]
				return _red, _green, _blue

			_figure = plt.figure( 1 )
			_axis = RGBAxes( _figure, [ 0.1, 0.1, 0.8, 0.8 ] )
			_r, _g, _b = get_rgb( )
			_kwargs = dict( origin = "lower", interpolation = "nearest" )
			_axis.imshow_rgb( _r, _g, _b, **_kwargs )
			_axis.RGB.set_xlim( 0., 9.5 )
			_axis.RGB.set_ylim( 0.9, 10.6 )
			plt.draw( )
			return plt.gcf( )

		def create_figure( ):
			_figure = matplotlib.figure.Figure( figsize = (5, 4), dpi = 100 )
			_data = np.arange( 0, 3, .01 )
			_figure.add_subplot( 111 ).plot( _data, 2 * np.sin( 2 * np.pi * _data ) )
			return _figure

		def create_subplot_3d( ):
			_figure = plt.figure( )
			_axis = _figure.add_subplot( 1, 2, 1, projection = '3d' )
			_x = np.arange( -5, 5, 0.25 )
			_y = np.arange( -5, 5, 0.25 )
			_x, _y = np.meshgrid( _x, _y )
			_r = np.sqrt( _x ** 2 + _y ** 2 )
			_z = np.sin( _r )
			surf = _axis.plot_surface( _x, _y, _z, rstride = 1, cstride = 1, cmap = cm,
				linewidth = 0, antialiased = False )

			_axis.set_zlim3d( -1.01, 1.01 )
			_figure.colorbar( surf, shrink = 0.5, aspect = 5 )
			_axis = _figure.add_subplot( 1, 2, 2, projection = '3d' )
			_x, _y, _z = get_test_data( )
			_axis.plot_wireframe( _x, _y, _z, rstride = 10, cstride = 10 )
			return _figure

		def create_pyplot_scales( ):
			plt.close( 'all' )
			np.random.seed( 19680801 )

			_y = np.random.normal( loc = 0.5, scale = 0.4, size = 1000 )
			_y = _y[ (_y > 0) & (_y < 1) ]
			_y.sort( )
			_x = np.arange( len( _y ) )

			# plot with various axes scales
			plt.figure( 1 )

			# linear
			plt.subplot( 221 )
			plt.plot( _x, _y )
			plt.yscale( 'linear' )
			plt.title( 'linear' )
			plt.grid( True )

			# log
			plt.subplot( 222 )
			plt.plot( _x, _y )
			plt.yscale( 'log' )
			plt.title( 'log' )
			plt.grid( True )

			# symmetric log
			plt.subplot( 223 )
			plt.plot( _x, _y - _y.mean( ) )
			plt.yscale( 'symlog', linthreshy = 0.01 )
			plt.title( 'symlog' )
			plt.grid( True )

			# logit
			plt.subplot( 224 )
			plt.plot( _x, _y )
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
			_canvas = FigureCanvasAgg( figure )
			_buffer = io.BytesIO( )
			_canvas.print_figure( _buffer, format = 'png' )
			if _buffer is None:
				return None
			_buffer.seek( 0 )
			element.update( data = _buffer.read( ) )
			return _canvas

		_figures = {
				'Axis Grid': create_axis_grid,
				'Subplot 3D': create_subplot_3d,
				'Scales': create_pyplot_scales,
				'Basic Figure': create_figure }

		def create_window( ):
			_leftcolumn = [ [ sg.T( 'Charts' ) ],
			                [ sg.Listbox( list( _figures ),
				                default_values = [ list( _figures )[ 0 ] ], size = (15, 5),
				                key = '-LB-' ) ],
			                [ sg.T( 'Styles' ) ],
			                [ sg.Combo( plt.style.available, size = (15, 10), key = '-STYLE-' ) ],
			                [ sg.T( 'Themes' ) ],
			                [ sg.Combo( sg.theme_list( ),
				                default_value = sg.theme( ),
				                size = (15, 10),
				                key = '-THEME-' ) ] ]

			_layout = [ [ sg.T( 'Budget Chart', font = ('Roboto', 10) ) ],
			            [ sg.Col( _leftcolumn ), sg.Image( key = '-IMAGE-' ) ],
			            [ sg.B( 'Draw' ), sg.B( 'Exit' ) ] ]

			_window = sg.Window( 'Budget Execution', _layout, finalize = True )

			return _window

		_window = create_window( )

		while True:
			_event, _values = _window.read( )
			print( _event, _values )
			if _event == 'Exit' or _event == sg.WIN_CLOSED:
				break
			if _event == 'Draw':
				if _values[ '-THEME-' ] != sg.theme( ):
					_window.close( )
					sg.theme( _values[ '-THEME-' ] )
					_window = create_window( )

				if _values[ '-LB-' ]:
					_func = _figures[ _values[ '-LB-' ][ 0 ] ]
					if _values[ '-STYLE-' ]:
						plt.style.use( _values[ '-STYLE-' ] )

					draw_figure( _window[ '-IMAGE-' ], _func( ) )

		_window.close( )
