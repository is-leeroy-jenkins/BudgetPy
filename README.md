![](https://github.com/KarmaScripter/BudgetPy/blob/master/etc/img/github/BudgetPy.png)

## BudgetPy is an open source, data analysis & prototyping tool developed in Python for Analysts in the US EPA and released under the MIT license.

# Features

- Mutliple data providers including SQLite, MS Access, and SQL Servers Express Edition through [pyodbc](https://github.com/mkleehammer/pyodbc/wiki)
- Charting, plotting and reporting with matplotlib, dash, and pandas.
- Pre-defined schema for 100 environmental data tables.
- Access to editors for SQLite, MS Access, and SQL CE.
- Easily add agency/region/division-specific branding.

# Providers

- SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. [Learn more here](https://sqlite.org/index.html) 
- SQL Server Express Edition is a scaled down, free edition of SQL Server, which includes the core database engine. [Learn more here](https://www.microsoft.com/en-us/download/details.aspx?id=101064)
- MS Access is a database management system (DBMS) from Microsoft that combines the relational Access Database Engine (ACE) with a graphical user interface and software-development tools.  [Learn more here](https://www.microsoft.com/en-us/microsoft-365/access)


# System requirements

- You will need these [Requirements](https://github.com/KarmaScripter/BudgetPy/blob/master/requirements.txt)




# Documentation

- See the [User Guide](etc/git/Users.md) for steps to get started.



# Make some BudgetPy

## Step 1: Install Visual Studio Code and fork it.

- Fork it from [Github](https://github.com/KarmaScripter/BudgetPy).

![image](https://github.com/KarmaScripter/BudgetPy/blob/master/etc/git/ForkingIt.PNG)




Download Visual Studio Code with plug-ins for python and jupyter notebooks.

![image](https://github.com/KarmaScripter/BudgetPy/blob/master/etc/git/InstallVSCode.PNG)



## Step 2: Setup this project in VS Code

- Open VS Code and select "Clone a repository"

![image](https://github.com/KarmaScripter/BudgetPy/blob/master/etc/git/CloneRepository.PNG)



## Step 3: Clone this project

- Type in your BudgetPy fork URL and press "Clone"

![image](https://github.com/KarmaScripter/BudgetPy/blob/master/etc/git/RepoDestination.PNG)



### Step 4: Open the BudgetPy Notebook!

- Select the `budgetpy.ipynb` and load the modules! 

![image](https://github.com/KarmaScripter/BudgetPy/blob/master/etc/git/RunNotebook.PNG)



## Code

- [Minion](https://github.com/KarmaScripter/BudgetPy/blob/master/Minion.py) - other tools used and available in BudgetPy.
- [Booger](https://github.com/KarmaScripter/BudgetPy/blob/master/Booger.py) - controls for the user interface and related functionality.
- [Data](https://github.com/KarmaScripter/BudgetPy/blob/master/Data.py) - data access layer with environmental budget data models.
- [FileSys](https://github.com/KarmaScripter/BudgetPy/blob/master/FileSys.py) - classes for interacting with the file system and input/output.
- [Static](https://github.com/KarmaScripter/BudgetPy/blob/master/Static.py) - enumerations used in budgetary data analysis.
- [Schema](https://github.com/KarmaScripter/BudgetPy/blob/master/Schema.py) - schema definitions of the BudgetPy data tables.
- [Ninja](https://github.com/KarmaScripter/BudgetPy/blob/master/Ninja.py)- budget data model classes for environmental programs.

## Credits


