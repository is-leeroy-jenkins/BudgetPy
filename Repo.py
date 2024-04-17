'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                Repo.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Repo.py" company="Terry D. Eppler">

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

     You can contact me at:  terryeppler@gmail.com or eppler.terry@epa.gov

  </copyright>
  <summary>
    Repo.py
  </summary>
  ******************************************************************************************
  '''
from sqlalchemy import ( MetaData, Table, Column, Integer, Numeric,
                        String, DateTime, ForeignKey, create_engine )
from Booger import Error, ErrorDialog
from Static import Source, Provider, SQL
from datetime import datetime

metadata = MetaData( )

accounts = Table( 'Accounts', metadata,
	Column( 'AccountsId', Integer( ), primary_key=True ),
	Column( 'Code', String(155) ),
	Column( 'Name', String(155) ) )

program_projects = Table( 'ProgramProjects', metadata,
	Column( 'ProgramProjectsId', Integer( ), primary_key=True ),
	Column( 'Code', String(100) ),
	Column( 'Name', String(155) ) )

program_areas = Table( 'ProgramAreas', metadata,
	Column( 'ProgramAreasId', Integer( ), primary_key=True ),
	Column( 'Code', String(100) ),
	Column( 'Name', String(155) ) )
