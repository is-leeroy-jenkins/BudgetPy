'''
  ******************************************************************************************
      Assembly:                Boo
      Filename:                Handlers.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Handlers.py" company="Terry D. Eppler">

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
    Handlers.py
  </summary>
  ******************************************************************************************
  '''
from typing import Any, Dict

import PySimpleGUI as sg
from loguru import logger

from src import Audio, GptQuery
from src.Button import OFF_IMAGE, ON_IMAGE

def handle_events( window: sg.Window, event: str, values: Dict[ str, Any ] ) -> None:
    '''
    Handle the events. Record audio, transcribe audio, generate quick and full answers.

    Args:
        window (sg.Window): The window element.
        event (str): The event.
        values (Dict[str, Any]): The values of the window.
    '''
    # If the user is not focused on the position input, process the events
    focused_element: sg.Element = window.find_element_with_focus()
    if not focused_element or focused_element.Key != '-POSITION_INPUT-':
        if event in ('r', 'R', '-RECORD_BUTTON-'):
            recording_event( window )
        elif event in ('a', 'A', '-ANALYZE_BUTTON-'):
            transcribe_event( window )

    # If the user is focused on the position input
    if event[ :6 ] in ('Return', 'Escape'):
        window[ '-ANALYZE_BUTTON-' ].set_focus()

    # When the transcription is ready
    elif event == '-WHISPER-':
        answer_events( window, values )

    # When the quick answer is ready
    elif event == '-QUICK_ANSWER-':
        logger.debug( 'Quick answer generated.' )
        print( 'Quick answer:', values[ '-QUICK_ANSWER-' ] )
        window[ '-QUICK_ANSWER-' ].update( values[ '-QUICK_ANSWER-' ] )

    # When the full answer is ready
    elif event == '-FULL_ANSWER-':
        logger.debug( 'Full answer generated.' )
        print( 'Full answer:', values[ '-FULL_ANSWER-' ] )
        window[ '-FULL_ANSWER-' ].update( values[ '-FULL_ANSWER-' ] )

def recording_event( window: sg.Window ) -> None:
    '''
    Handle the recording event. Record audio and update the record button.

    Args:
        window (sg.Window): The window element.
    '''
    button: sg.Element = window[ '-RECORD_BUTTON-' ]
    button.metadata.state = not button.metadata.state
    button.update( image_data = ON_IMAGE if button.metadata.state else OFF_IMAGE )

    # Record audio
    if button.metadata.state:
        window.perform_long_operation( lambda: audio.record( button ), '-RECORDED-' )

def transcribe_event( window: sg.Window ) -> None:
    '''
    Handle the transcribe event. Transcribe audio and update the text area.

    Args:
        window (sg.Window): The window element.
    '''
    transcribed_text: sg.Element = window[ '-TRANSCRIBED_TEXT-' ]
    transcribed_text.update( 'Transcribing audio...' )

    # Transcribe audio
    window.perform_long_operation( gpt_query.transcribe_audio, '-WHISPER-' )

def answer_events( window: sg.Window, values: Dict[ str, Any ] ) -> None:
    '''
    Handle the answer events. Generate quick and full answers and update the text areas.

    Args:
        window (sg.Window): The window element.
        values (Dict[str, Any]): The values of the window.
    '''
    transcribed_text: sg.Element = window[ '-TRANSCRIBED_TEXT-' ]
    quick_answer: sg.Element = window[ '-QUICK_ANSWER-' ]
    full_answer: sg.Element = window[ '-FULL_ANSWER-' ]

    # Get audio transcript and update text area
    audio_transcript: str = values[ '-WHISPER-' ]
    transcribed_text.update( audio_transcript )

    # Get model and position
    model: str = values[ '-MODEL_COMBO-' ]
    position: str = values[ '-POSITION_INPUT-' ]

    # Generate quick answer
    logger.debug( 'Generating quick answer...' )
    quick_answer.update( 'Generating quick answer...' )
    window.perform_long_operation(
        lambda: gpt_query.generate_answer(
            audio_transcript,
            short_answer = True,
            temperature = 0,
            model = model,
            position = position,
        ),
        '-QUICK_ANSWER-',
    )

    # Generate full answer
    logger.debug( 'Generating full answer...' )
    full_answer.update( 'Generating full answer...' )
    window.perform_long_operation(
        lambda: gpt_query.generate_answer(
            audio_transcript,
            short_answer = False,
            temperature = 0.7,
            model = model,
            position = position,
        ),
        '-FULL_ANSWER-',
    )
