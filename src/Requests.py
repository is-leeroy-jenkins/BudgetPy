'''
  ******************************************************************************************
      Assembly:                Boo
      Filename:                Requests.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Requests.py" company="Terry D. Eppler">

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
    Requests.py
  </summary>
  ******************************************************************************************
  '''

class GptRequest( ):
	'''
	Base class for GPT requests.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class TextGenerationRequest( GptRequest ):
	'''
	Class encapsulating the request for text generations.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.18, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class ChatCompletionRequest( GptRequest ):
	'''
	Class encapsulating requests for chat completions.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class SpeechGenerationRequest( GptRequest ):
	'''
	Class encapsulating requests for speech generations.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class TranslationRequest( GptRequest ):
	'''
	Class encapsulating requests for translation.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class TranscriptionRequest( GptRequest ):
	'''
	Class encapsulating requests for transcriptions.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class EmbeddingRequest( GptRequest ):
	'''
	Class encapsulating requests for embedding.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class VectorRequest( GptRequest ):
	'''
	Class encapsulating requests for vectors.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class GptFileRequest( GptRequest ):
	'''
	Class encapsulating requests for GPT files.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class GptUploadRequest( GptRequest ):
	'''
	Class encapsulating requests for GPT uploads.
	'''

class FineTuningRequest( GptRequest ):
	'''
		Class encapsulating requests for fine-tuning.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

class ImageGenerationRequest( GptRequest ):
	'''
	Class encapsulating requests for image generation.
	'''
	
	def __init__( self, num: int = 1, temp: float = 0.11, top: float = 0.11, freq: float = 0.0,
	              pres: float = 0.0, store: bool = False, stream: bool = True ):
		super( ).__init__( num, temp, top, freq, pres, store, stream )
		self.number = num
		self.temperature = temp
		self.top_percent = top
		self.frequency_penalty = freq
		self.presence_penalty = pres
		self.store = store
		self.stream = stream

