'''
	#  ***********************************************************************
	#  Assembly         : BudgetPy
	#  Author           : Terry D. Eppler
	#  Created          : 05-29-2023
	#  #
	#  Last Modified By : Terry D. Eppler
	#  Last Modified On : 05-29-2023
	#  ***********************************************************************
	#  <copyright file=".py" company="Terry Eppler">
	#     Copyright ©  2023  Terry Eppler
	#  #
	#     This program is free software: you can redistribute it and/or modify
	#     it under the terms of the GNU General Public License as published by
	#     the Free Software Foundation, either version 3 of the License, or
	#     (at your option) any later version.
	#  #
	#     This program is distributed in the hope that it will be useful,
	#     but WITHOUT ANY WARRANTY; without even the implied warranty of
	#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	#     GNU General Public License for more details.
	#  #
	#     You should have received a copy of the GNU General Public License
	#     along with this program.  If not, see <https:#www.gnu.org/licenses/>.
	#  #
	#     Contact: terryeppler@gmail.com or eppler.terry@epa.gov
	#  </copyright>
	#  <summary>
	#  #
	#  </summary>
	#  ***********************************************************************
'''
import os

APPLICATION_WIDTH = 85
THEME = "DarkGray12"
OUTPUT_FILE_NAME = "record.wav"
SAMPLE_RATE = 48000
MODELS = [ "gpt-4o-mini", "gpt-4o", "gpt-4-turbo", "gpt-3.5-turbo" ]
DEFAULT_MODEL = MODELS[ 0 ]
DEFAULT_POSITION = "Python Developer"

OPENAI_API_KEY = os.getenv( 'OPENAI_API_KEY' )
GEMINI_API_KEY = os.getenv( 'GEMINI_API_KEY' )
GROQ_API_KEY = os.getenv( 'GROQ_API_KEY' )


def set_environment( ):
	'''
		Set the environment variables
		
		:return: None
		
	'''
	variable_dict = globals( ).items( )
	for key, value in variable_dict:
		if "API" in key or "ID" in key:
			os.environ[ key ] = value

