'''
  ******************************************************************************************
      Assembly:                Boo
      Filename:                Messages.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Messages.py" company="Terry D. Eppler">

     This is a Federal Budget, Finance, and Accounting application.
     Copyright ©  2024  Terry Eppler

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

     You can contact me at: terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    Messages.py
  </summary>
  ******************************************************************************************
  '''

class GptMessage( ):
	'''
		Base class for all messages used in the GPT application
	'''
	
	def __init__( self, prompt: str, typ: str = 'text' ) -> None:
		self.content = prompt
		self.type = typ

class SystemMessage( GptMessage ):
	'''

		Class used to represent a system message.

	'''
	
	def __init__( self, prompt: str, typ: str = 'text' ) -> None:
		super( ).__init__( prompt, typ )
		self.role = "system"
		self.type = typ
		self.prompt = prompt
	
	def __str__( self ):
		'''

			Returns: the json string representation of the message.

		'''
		if self.content is not None:
			_data = f'''
			'role': '{self.role}',,
			'type': '{self.type}',
			'content': '{self.content}'
			'''
			_message = "{ " + _data + " }"
			return _message

class UserMessage( GptMessage ):
	'''

		Class used to represent a user message.

	'''
	
	def __init__( self, prompt: str, typ: str = 'text' ) -> None:
		super( ).__init__( prompt, typ )
		self.role = "user"
		self.type = typ
		self.content = prompt
	
	def __str__( self ):
		'''

			Returns: the json string representation of the message.

		'''
		if self.content is not None:
			_data = f'''
			'role': '{self.role}',,
			'type': '{self.type}',
			'content': '{self.content}'
			'''
			_message = "{ " + _data + " }"
			return _message

class AssistantMessage( GptMessage ):
	'''

		Class used to represent a assistant message.

	'''
	
	def __init__( self, prompt: str, typ: str = 'text' ) -> None:
		super( ).__init__( prompt, typ )
		self.role = "assistant"
		self.type = typ
		self.content = prompt
	
	def __str__( self ):
		'''

			Returns: the json string representation of the message.

		'''
		if self.content is not None:
			_data = f'''
			'role': '{self.role}',,
			'type': '{self.type}',
			'content': '{self.content}'
			'''
			_message = "{ " + _data + " }"
			return _message

class ChatLog( ):
	'''

	Class used to encapsulate a collection of chat messages.

	'''
	
	def __init__( self ):
		self.messages = [ ]
