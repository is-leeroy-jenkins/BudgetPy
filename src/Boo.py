'''
  ******************************************************************************************
      Assembly:                Boo
      Filename:                Boo.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Boo.py" company="Terry D. Eppler">

     Bobo is a data analysis tool for EPA Analysts.
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

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    Boo.py
  </summary>
  ******************************************************************************************
  '''
import os
from openai import OpenAI
import requests
from pygments.lexers.csound import newline

from Static import GptRequests, GptRoles, GptLanguages
from Booger import ErrorDialog, Error

class Header():
    '''
        Class used to encapsulate GPT headers
    '''

    def __init__( self ):
        self.content_type = 'application/json'
        self.api_key = os.environ.get( 'OPENAI_API_KEY' )
        self.authoriztion = 'Bearer ' + os.environ.get( 'OPENAI_API_KEY' )
        self.data = { 'content-type': self.content_type,
                      'Authorization': self.authoriztion }

    def __dir__( self ):
        '''
            Methods that returns a list of member names
            Returns: list[ str ]
        '''
        return [ 'content_type', 'api_key', 'authorization', 'data' ]

class EndPoint():
    '''
        The class containing endpoints for OpenAI
    '''

    def __init__( self ):
        self.base_url = f'https://api.openai.com/'
        self.text_generation = f'https://api.openai.com/v1/chat/completions'
        self.image_generation = f'https://api.openai.com/v1/images/generations'
        self.chat_completion = f'https://api.openai.com/v1/chat/completions'
        self.speech_generation = f'https://api.openai.com/v1/audio/speech'
        self.translations = f'https://api.openai.com/v1/audio/translations'
        self.assistants = f'https://api.openai.com/v1/assistants'
        self.transcriptions = f'https://api.openai.com/v1/audio/transcriptions'
        self.finetuning = f'https://api.openai.com/v1/fineTuning/jobs'
        self.embeddings = f'https://api.openai.com/v1/embeddings'
        self.uploads = f'https://api.openai.com/v1/uploads'
        self.files = f'https://api.openai.com/v1/files'
        self.vector_stores = f'https://api.openai.com/v1/vector_stores'

    def __dir__( self ) -> list[ str ]:
        '''
            Methods that returns a list of member names
            Returns: list[ str ]
        '''
        return [ 'base_url', 'text_generation', 'image_generation', 'chat_completions',
                 'speech_generation', 'translations', 'assistants', 'transcriptions',
                 'finetuning', 'embeddings', 'uploads', 'files', 'vector_stores',
                 'get_data', 'dump' ]

    def get_data( self ) -> dict:
        '''

            Returns: dict[ str ] of members

        '''
        return { 'base_url': self.base_url,
                 'text_generation': self.text_generation,
                 'image_generation': self.image_generation,
                 'chat_completion': self.chat_completion,
                 'speech_generation': self.speech_generation,
                 'translations': self.translations,
                 'assistants': self.assistants,
                 'transcriptions': self.transcriptions,
                 'finetuning': self.finetuning,
                 'embeddings': self.embeddings,
                 'uploads': self.uploads,
                 'files': self.files,
                 'vector_stores': self.vector_stores }

    def dump( self ) -> str:
        '''
            Returns: dict of members
        '''
        new = r'\r\n'
        return 'base_url' + f' = {self.base_url}' + new + \
            'text_generation' + f' = {self.text_generation}' + new + \
            'image_generation' + f' = {self.image_generation}' + new + \
            'chat_completion' + f' = {self.chat_completion}' + new + \
            'speech_generation' + f' = {self.speech_generation}' + new + \
            'translations' + f' = {self.translations}' + new + \
            'assistants' + f' = {self.assistants}' + new + \
            'transcriptions' + f' = {self.transcriptions}' + new + \
            'finetuning' + f' = {self.finetuning}' + new + \
            'embeddings' + f' = {self.files}' + new + \
            'uploads' + f' = {self.uploads}' + new + \
            'files' + f' = {self.files}' + new + \
            'vector_stores' + f' = {self.vector_stores}' + new

class Models():
    '''
        Class containing lists of OpenAI models by generation
    '''

    def __init__( self ):
        self.text_generation = [ 'text-davinci-003', 'text-curie-001',
                                 'gpt-4-0613', 'gpt-4-0314',
                                 'gpt-4-turbo-2024-04-09', 'gpt-4o-2024-08-06',
                                 'gpt-4o-2024-11-20', 'gpt-4o-2024-05-13',
                                 'gpt-4o-mini-2024-07-18', 'o1-2024-12-17',
                                 'o1-mini-2024-09-12', 'o3-mini-2025-01-31' ]
        self.image_generation = [ 'dall-e-2', 'dall-e-3',
                                  'gpt-4-0613', 'gpt-4-0314',
                                  'gpt-4o-mini-2024-07-18' ]
        self.chat_completion = [ 'gpt-4-0613', 'gpt-4-0314',
                                 'gpt-4-turbo-2024-04-09', 'gpt-4o-2024-08-06',
                                 'gpt-4o-2024-11-20', 'gpt-4o-2024-05-13',
                                 'gpt-4o-mini-2024-07-18', 'o1-2024-12-17',
                                 'o1-mini-2024-09-12', 'o3-mini-2025-01-31' ]
        self.speech_generation = [ 'tts-1', 'tts-1-hd',
                                   'gpt-4o-audio-preview-2024-12-17',
                                   'gpt-4o-audio-preview-2024-10-01',
                                   'gpt-4o-mini-audio-preview-2024-12-17' ]
        self.transcription = [ 'whisper-1' ]
        self.translation = [ 'whisper-1', 'text-davinci-003',
                             'gpt-4-0613', 'gpt-4-0314',
                             'gpt-4-turbo-2024-04-09' ]
        self.finetuning = [ 'gpt-4o-2024-08-06', 'gpt-4o-mini-2024-07-18',
                            'gpt-4-0613', 'gpt-3.5-turbo-0125',
                            'gpt-3.5-turbo-1106', 'gpt-3.5-turbo-0613' ]
        self.embeddings = [ 'text-embedding-3-small', 'text-embedding-3-large',
                            'text-embedding-ada-002' ]
        self.uploads = [ 'gpt-4-0613', 'gpt-4-0314', 'gpt-4-turbo-2024-04-09',
                         'gpt-4o-2024-08-06', 'gpt-4o-2024-11-20',
                         'gpt-4o-2024-05-13', 'gpt-4o-mini-2024-07-18',
                         'o1-2024-12-17', 'o1-mini-2024-09-12', 'o3-mini-2025-01-31' ]
        self.files = [ 'gpt-4-0613', 'gpt-4-0314', 'gpt-4o-2024-08-06', 'gpt-4o-2024-11-20',
                       'gpt-4o-2024-05-13', 'gpt-4o-mini-2024-07-18',
                       'o1-2024-12-17', 'o1-mini-2024-09-12', 'o3-mini-2025-01-31' ]
        self.vector_stores = [ 'gpt-4-0613', 'gpt-4-0314', 'gpt-4-turbo-2024-04-09',
                               'gpt-4o-2024-11-20', 'gpt-4o-2024-05-13',
                               'gpt-4o-mini-2024-07-18', 'o1-2024-12-17',
                               'o1-mini-2024-09-12', 'o3-mini-2025-01-31' ]

    def __dir__( self ) -> list[ str ]:
        '''
            Methods that returns a list of member names
            Returns: list[ str ]
        '''
        return [ 'base_url', 'text_generation', 'image_generation', 'chat_completion',
                 'speech_generation', 'translations', 'assistants', 'transcriptions',
                 'finetuning', 'embeddings', 'uploads', 'files', 'vector_stores' ]

    def get_data( self ) -> dict:
        '''
            Method that returns a list of dictionaries
        '''
        _data = { 'text_generation': self.text_generation,
                  'image_generation': self.image_generation,
                  'chat_completion': self.chat_completion,
                  'speech_generation': self.speech_generation,
                  'translations': self.translation,
                  'finetuning': self.finetuning,
                  'embeddings': self.embeddings,
                  'uploads': self.uploads,
                  'files': self.files,
                  'vector_stores': self.vector_stores }

class AI():
    '''
    AI is the base class for all OpenAI functionalityl
    '''

    def __init__( self ):
        self.header = Header()
        self.endpoint = EndPoint()
        self.api_key = self.header.api_key
        self.client = OpenAI( api_key = self.api_key )
        self.system_instructions = '''You are the most knowledgeable Budget Analyst in the federal
        government who provides detailed responses based on your vast knowledge of
        budget legislation, and federal appropriations.
        Your responses to questions about federal finance are complete, transparent,
        and very detailed using an academic format.
        Your vast knowledge of and experience in Data Science makes you the best Data Analyst ever.
        You are proficient in C#, Python, SQL, C++, JavaScript, and VBA.
        You use US federal budget data from OMB, whitehouse.gov,  or data.gov for any ad hoc
        data sets for examples and provide your analysis in Python.
        Whenever you are asked to draw, paint, or create an image,
        you become the best artist in the world like Picasso and Vermeer
        combined into one awesome assistant, and you can fluently
        translate from a variety of languages into English..
        '''

class GptOptions():
    '''

        The base class used by all parameter classes.

    '''

    def __init__( self, number: int = 1, temperature: float = 0.08, top_p: float = 0.09,
            frequency: float = 0.00, presence: float = 0.00, store: bool = False,
            stream: bool = True, size: str = '1024X1024' ):
        self.number = number
        self.temperature = temperature
        self.top_percent = top_p
        self.frequency_penalty = frequency
        self.presence_penalty = presence
        self.store = store
        self.stream = stream
        self.size = size
        self.modalities = [ 'text', 'audio' ]

    def __dir__( self ) -> list[ str ]:
        '''

            Methods that returns a list of member names
            Returns: list[ str ]

        '''
        return [ 'number', 'temperature', 'top_percent', 'frequency_penalty',
                 'presence_penalty', 'store', 'stream', 'size',
                 'get_voices', 'get_sizes',
                 'get_file_formats', 'get_response_formats',
                 'get_output_formats', 'get_input_formats',
                 'get_data' ]

    def get_voices( self ) -> list[ str ]:
        '''

            Returns: list[ str ] of voices used by the audio api

        '''
        return [ 'alloy', 'cash', 'coral', 'echo',
                 'onyx', 'fable', 'nova', 'sage' ]

    def get_sizes( self ) -> list[ str ]:
        '''

            Returns: list[ str ] of size used by the audio api

        '''
        return [ '256X256', '512X512', '1024X1024',
                 '1024x1792', '1792x1024' ]

    def get_response_formats( self ) -> list[ str ]:
        '''

            Returns: list[ str ] of response formats used by the GPT

        '''
        return [ 'text', 'audio', 'url' ]

    def get_output_formats( self ) -> list[ str ]:
        '''

            Returns: list[ str ] of audio formats output by the audio api

        '''
        return [ 'mp3', 'opus', 'aac', 'flac', 'pcm' ]

    def get_input_formats( self ) -> list[ str ]:
        '''

            Returns: list[ str ] of audio formats uploaded into the audio api

        '''
        return [ 'mp3', 'mp4', 'mpeg', 'mpga', 'm4a', 'wav', 'webm' ]

    def get_data( self ) -> dict:
        '''

            Returns: dict[ str ] of members

        '''
        return { 'number': self.number,
                 'temperature': self.temperature,
                 'top_percent': self.top_percent,
                 'frequency_penalty': self.frequency_penalty,
                 'presence_penalty': self.presence_penalty,
                 'store': self.store,
                 'stream': self.stream,
                 'size': self.size }

    def dump( self ) -> str:
        '''
            Returns: dict of members
        '''
        new = '\r\n'
        return 'number' + f' = {self.number}' + new + \
            'temperature' + f' = {self.temperature}' + new + \
            'top_percent' + f' = {self.top_percent}' + new + \
            'frequency_penalty' + f' = {self.frequency_penalty}' + new + \
            'presence_penalty' + f' = {self.presence_penalty}' + new + \
            'store' + f' = {self.store}' + new + \
            'stream' + f' = {self.stream}' + new + \
            'size' + f' = {self.size}' + new

class Payload():
    '''

        The class used to capture request parameters.

    '''

    def __init__( self, model: str, number: int = 1, temperature: float = 0.08,
            top_p: float = 0.09, frequency: float = 0.00,
            presence: float = 0.00, store: bool = False,
            stream: bool = True, size: str = '1024X1024' ):
        self.model = model
        self.number = number
        self.temperature = temperature
        self.top_percent = top_p
        self.frequency_penalty = frequency
        self.presence_penalty = presence
        self.store = store
        self.stream = stream
        self.size = size
        self.data = { 'number': f'{self.number}',
                      'model': f'{self.model}',
                      'temperature': f'{self.temperature}',
                      'top_percent': f'{self.top_percent}',
                      'frequency_penalty': f'{self.frequency_penalty}',
                      'presence_penalty': f'{self.presence_penalty}',
                      'store': f'{self.store}',
                      'stream': f'{self.stream}',
                      'size': f'{self.size}' }

    def __dir__( self ) -> list[ str ]:
        '''
        Methods that returns a list of member names
        Returns: list[ str ]
        '''
        return [ 'number', 'model', 'temperature',
                 'top_percent', 'frequency_penalty',
                 'presence_penalty', 'store', 'stream',
                 'size', 'data', 'dump', 'parse' ]

    def dump( self ) -> str:
        '''

            Returns: a string of key value pairs

        '''
        new = '\r\n'
        return 'n' + f' = {self.number}' + new + \
            'model' + f' = {self.model}' + new + \
            'temperature' + f' = {self.temperature}' + new + \
            'top_p' + f' = {self.top_percent}' + new + \
            'frequency_penalty' + f' = {self.frequency_penalty}' + new + \
            'presence_penalty' + f' = {self.presence_penalty}' + new + \
            'store' + f' = {self.store}' + new + \
            'stream' + f' = {self.stream}' + new + \
            'size' + f' = {self.size}' + new

    def parse( self ) -> dict:
        pass

class Message():
    '''

        Class for all messages used in the GPT application

    '''

    def __init__( self, prompt: str, role: str = 'user', type: str = 'text' ):
        self.role = role
        self.content = prompt
        self.type = type
        self.data = { 'role': f'{self.role}',
                      'type': f'{self.type}',
                      'content': f'{self.content}' }

    def __str__( self ) -> str:
        '''

            Returns: the json string representation of the message.

        '''
        new = '\r\n'
        if not self.content is None:
            _pair = f'''
            'role': '{self.role}', \r\n
            'type': '{self.type}', \r\n
            'content': '{self.content}'
            '''
            _retval = '{ ' + _pair + ' }'
            return _retval

    def dump( self ) -> str:
        '''

            Returns: key value pairs in a string

        '''
        new = '\r\n'
        return 'role' + f' = {self.role}' + new + \
            'type' + f' = {self.type}' + new + \
            'content' + f' = {self.content}'

    def __dir__( self ) -> list[ str ]:
        '''
            Methods that returns a list of member names
            Returns: list[ str ]
        '''
        return [ 'role', 'content', 'type' ]

class TextGeneration( AI ):
    '''

    Class provides the functionality fo the Text Generation API

    '''

    def __init__( self ):
        super().__init__()
        self.client = OpenAI()
        self.header = super().header
        self.request_type = GptRequests.TextGeneration
        self.endpoint = EndPoint().text_generation
        self.model = 'gpt-4o'
        self.number = 1;
        self.temperature = 0.08
        self.top_percent = 0.09
        self.frequency_penalty = 0.0
        self.presence_penalty = 0.0
        self.store = False
        self.stream = True
        self.content = None
        self.response = None
        self.prompt = None
        self.messages = [ ]
        self.data = { 'number': f'{self.number}',
                      'model': f'{self.model}',
                      'temperature': f'{self.temperature}',
                      'top_percent': f'{self.top_percent}',
                      'frequency_penalty': f'{self.frequency_penalty}',
                      'presence_penalty': f'{self.presence_penalty}',
                      'store': f'{self.store}',
                      'stream': f'{self.stream}',
                      'endpoint': f'{self.endpoint}',
                      'authorization': f'{self.header.authoriztion}',
                      'content-type': f'{self.header.content_type}' }

    def __dir__( self ) -> list[ str ]:
        '''
            Methods that returns a list of member names
            Returns: list[ str ]
        '''
        return [ 'header', 'request_type', 'endpoint',
                 'model', 'number', 'messages',
                 'content', 'store', 'stream',
                 'response', 'prompt', 'generate_request' ]


    def generate_request( self, prompt: str ) -> str:
        '''

            Given an input prompt 'prompt', function generates a text generation
            request from the openai api.

        Args:
            prompt: query provided by the user to the GPT application

        Returns:

        '''
        try:
            if prompt is None:
                alert = f'The prompt argument is not available'
                raise Exception( alert )
            else:
                self.prompt = prompt

            self.client.api_key = self.header.api_key
            _system_prompt = 'You are a helpful assistant and Budget Analyst'
            _system = Message( prompt = _system_prompt, role = 'system', type = 'text' )
            _user = Message( prompt = self.prompt, role = 'user', type = 'text' )
            self.messages.append( _system )
            self.messages.append( _user )

            completion = self.client.chat.completions.create(
                model = self.model,
                messages = self.messages,
                temperature = 0.08,
                max_completion_tokens = 2048,
                top_p = 0.09,
                n = 1,
                frequency_penalty = 0.00,
                presence_penalty = 0.00,
            )

            self.content = completion[ 'choices' ][ 0 ][ 'message' ][ 'content' ]
            return self.content
        except Exception as e:
            exception = Error( e )
            exception.module = 'Boo'
            exception.cause = 'TextGeneration'
            exception.method = 'generate_request( prompt: str ) -> str'
            error = ErrorDialog( exception )
            error.show()


class ChatCompletion():
    '''

        Class provides the functionality fo the Completions API

    '''

    def __init__( self ):
        self.header = Header()
        self.client = OpenAI()
        self.request_type = GptRequests.ChatCompletions
        self.endpoint = EndPoint().chat_completions
        self.model = 'gpt-4o'
        self.messages = [ ]
        self.content = None
        self.response = None
        self.prompt = None
        self.data = { 'number': f'{self.number}',
                      'model': f'{self.model}',
                      'temperature': f'{self.temperature}',
                      'top_percent': f'{self.top_percent}',
                      'frequency_penalty': f'{self.frequency_penalty}',
                      'presence_penalty': f'{self.presence_penalty}',
                      'store': f'{self.store}',
                      'stream': f'{self.stream}',
                      'endpoint': f'{self.endpoint}',
                      'authorization': f'{self.header.authoriztion}',
                      'content-type': f'{self.header.content_type}' }


    def __dir__( self ) -> list[ str ]:
        '''
            Methods that returns a list of member names
            Returns: list[ str ]
        '''
        return [ 'header', 'client', 'request_type', 'endpoint',
                 'model', 'number', 'messages',
                 'content', 'response', 'prompt', 'generate_request' ]


    def generate_request( self, prompt: str ) -> str:
        '''
                Function that generates chat completions given a prompt
            Args:
                prompt:

            Returns:

        '''

        try:
            if prompt is None:
                alert = 'The prompt argument is not available'
                raise Exception( alert )
            else:
                self.prompt = prompt
            self.client.api_key = self.header.api_key
            _sys = 'You are a helpful assistant and Budget Analyst'
            _system = Message( prompt = _sys, role = 'system', type = 'text' )
            _user = Message( prompt = self.prompt, role = 'user', type = 'text' )
            self.messages.append( _system )
            self.messages.append( _user )
            self.response = self.client.chat.completions.create(
                model = self.model,
                messages = self.messages,
                temperature = 0.08,
                max_completion_tokens = 2048,
                top_p = 0.09,
                frequency_penalty = 0.0,
                presence_penalty = 0.0,
            )

            self.content = self.response[ 'choices' ][ 0 ][ 'message' ][ 'content' ]
            return self.content
        except Exception as e:
            exception = Error( e )
            exception.module = 'Boo'
            exception.cause = 'ChatCompletion'
            exception.method = 'generate_request( prompt: str )'
            error = ErrorDialog( exception )
            error.show()


class ImageGeneration():
    '''
        Class provides the functionality fo the Image Generation API
    '''

    def __init__( self ):
        self.header = Header()
        self.client = OpenAI()
        self.endpoint = EndPoint().image_generation
        self.model = 'dall-e-2'
        self.messages = [ ]
        self.content = None
        self.response = None
        self.prompt = None
        self.url = None
        self.number = 1
        self.size = '1024X1024'
        self.quality = 'standard'
        self.data = { 'number': f'{self.number}',
                      'model': f'{self.model}',
                      'temperature': f'{self.temperature}',
                      'top_p': f'{self.top_percent}',
                      'frequency_penalty': f'{self.frequency_penalty}',
                      'presence_penalty': f'{self.presence_penalty}',
                      'store': f'{self.store}',
                      'stream': f'{self.stream}',
                      'endpoint': f'{self.endpoint}',
                      'authorization': f'{self.header.authoriztion}',
                      'content-type': f'{self.header.content_type}' }


    def __dir__( self ) -> list[ str ]:
        '''
            Methods that returns a list of member names
            Returns: list[ str ]
        '''
        return [ 'header', 'request_type', 'endpoint', 'model', 'number', 'messages',
                 'content', 'response', 'prompt', 'size', 'generate_request( prompt )' ]


    def generate_request( self, prompt: str, num: int = 1,
            quality = 'standard', size: str = '1024X1024' ) -> str:
        '''
            Function geerates chat completq

            Args:
                prompt: str, num: int, size: str


            Returns:

        '''

        try:
            if prompt is None:
                alert = 'The prompt argument is not available'
                raise Exception( alert )
            else:
                self.prompt = prompt
                self.number = num
                self.size = size

            openai.api_key = self.header.api_key
            _sys = 'You are a helpful assistant and Budget Analyst'
            _system = Message( prompt = _sys, role = 'system', type = 'text' )
            _user = Message( prompt = self.prompt, role = 'user', type = 'text' )
            self.messages.append( _system )
            self.messages.append( _user )
            self.response = self.client.chat.completions.create(
                model = self.model,
                messages = self.messages,
                n = self.number,
                size = self.size,
                temperature = 0.08,
                max_completion_tokens = 2048,
                top_p = 0.09,
                frequency_penalty = 0.00,
                presence_penalty = 0.00,
            )

            self.url = self.response[ 'data' ][ 0 ][ 'url' ]
            self.content = requests.get( url ).content
            with open( 'image_name.png', 'wb' ) as file:
                file.write( self.content )
        except Exception as e:
            exception = Error( e )
            exception.module = 'Boo'
            exception.cause = 'ImageGeneration'
            exception.method = 'generate_request( prompt: str )'
            error = ErrorDialog( exception )
            error.show()

