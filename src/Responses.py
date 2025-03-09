'''
  ******************************************************************************************
      Assembly:                Boo
      Filename:                Responses.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Responses.py" company="Terry D. Eppler">

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
    Responses.py
  </summary>
  ******************************************************************************************
  '''
import datetime as dt

class GptResponse( ):
	'''
	Base class for GPT requests.
	'''
	
	def __init__( self, respid: str, obj: object, model: str, created: dt.datetime ):
		self.id = respid
		self.object = obj
		self.model = model
		self.created = created

class ChatCompletionResponse( GptResponse ):
	'''
	Class containing the GPT response for the chat completion
	'''
	
	def __init__( self, respid: str, obj: object, model: str, created: dt.datetime ):
		super( ).__init__( respid, obj, model, created )
		self.id = respid
		self.object = obj
		self.model = model
		self.created = created

class TextGenerationResponse( GptResponse ):
	'''
	Class containing the GPT response for the text generation
	'''
	
	def __init__( self, respid: str, obj: object, model: str, created: dt.datetime ):
		super( ).__init__( respid, obj, model, created )
		self.id = respid
		self.object = obj
		self.model = model
		self.created = created

class EmbeddingResponse( GptResponse ):
	'''
	Class containing the GPT response for the embedding request
	'''
	
	def __init__( self, respid: str, obj: object, model: str, created: dt.datetime ):
		super( ).__init__( respid, obj, model, created )
		self.id = respid
		self.object = obj
		self.model = model
		self.created = created

class FineTuningResponse( GptResponse ):
	'''
	Class containing the GPT response for the fine tuning request
	'''
	
	def __init__( self, respid: str, obj: object, model: str, created: dt.datetime ):
		super( ).__init__( respid, obj, model, created )
		self.id = respid
		self.object = obj
		self.model = model
		self.created = created

class VectorResponse( GptResponse ):
	'''
	Class containing the GPT response for the vector request
	'''
	
	def __init__( self, respid: str, obj: object, model: str, created: dt.datetime ):
		super( ).__init__( respid, obj, model, created )
		self.id = respid
		self.object = obj
		self.model = model
		self.created = created

class FileResponse( GptResponse ):
	'''
		Class containing the GPT response for the file request
	'''
	
	def __init__( self, respid: str, obj: object, model: str, created: dt.datetime ):
		super( ).__init__( respid, obj, model, created )
		self.id = respid
		self.object = obj
		self.model = model
		self.created = created

class UploadResponse( GptResponse ):
	'''
	References
	'''
	
	def __init__( self, respid: str, obj: object, model: str, created: dt.datetime ):
		super( ).__init__( respid, obj, model, created )
		self.id = respid
		self.object = obj
		self.model = model
		self.created = created

class ImageGenerationResponse( GptResponse ):
	'''
	Class containing the GPT response for the image request
	'''
	
	def __init__( self, respid: str, obj: object, model: str, created: dt.datetime ):
		super( ).__init__( respid, obj, model, created )
		self.id = respid
		self.object = obj
		self.model = model
		self.created = created

