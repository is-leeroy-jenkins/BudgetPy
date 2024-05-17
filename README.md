# BudgetPy

![](https://github.com/KarmaScripter/BudgetPy/blob/main/Resources/Assets/GitHubImages/BudgetExecution.png)

## BudgetPy is an open source, data analysis prototyping tool for Analysts in the US EPA developed in Python and released under the MIT license.

## Features

- Mutliple data providers including SQLite, MS Access, SQL CE, and SQL Servers Express Edition.
- Charting and reporting.
- Its own internal web browser with queries optimized for researching data in the .gov domain [Baby Browser](https://github.com/KarmaScripter/Baby/blob/main/README.md)
- Pre-defined schema for 100 actively used data tables.
- SQL Editors for SQLite, SQL Compact Edition, MS Access, SQL Server Express.
- Excel User Interface over real databases.
- Mapping for congressional earmark reporting and pollution site monitoring.
- Easy access to environmental program project descriptions and statutory authority.
- Quick budget and accouting calculations directl on bound data.
- Easily add agency/region/division-specific branding.

## Providers

- SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. [Get here](https://sqlite.org/index.html) 
- SQL Server Express Edition is a scaled down, free edition of SQL Server, which includes the core database engine. [Get here](https://www.microsoft.com/en-us/download/details.aspx?id=101064)
- MS Access is a database management system (DBMS) from Microsoft that combines the relational Access Database Engine (ACE) with a graphical user interface and software-development tools. 


## System requirements

- You need [VC++ 2019 Runtime](https://aka.ms/vs/17/release/vc_redist.x64.exe) 32-bit and 64-bit versions

- You will need .NET 6.

- You need to install the version of VC++ Runtime that CEFSharp needs. Since we are using CefSharp 106, according to [this](https://github.com/cefsharp/CefSharp/#release-branches) we need the above versions


## Getting started

- See the [Compilation Guide](Resources/Github/Compilation.md) for steps to get started.


## Documentation

- [User Guide](Resources/Github/Users.md)
- [Compilation Guide](Resources/Github/Compilation.md)
- [Configuration Guide](Resources/Github/Configuration.md)
- [Distribution Guide](Resources/Github/Distribution.md)


## Code

- BudgetExecution uses CefSharp 106 for b and is built on NET 6
- BudgetExecution supports AnyCPU as well as x86/x64 specific builds
- `Controls` (Controls\) - main UI layer and associated controls and related functionality
- `Enumerations` (Enumerations\) - various enumerations used for budgetary accounting
- `Extensions` (Extensions\) - useful extension methods for budget analysis by type
- `Clients` (Clients\) - other tools used and available
- `bin` - Binaries are included in the `bin` folder due to the complex Baby setup required. Don't empty this folder.
- `bin/storage` - HTML and JS required for downloads manager and custom error pages

## Credits

## Screenshots

### Datagrids to easily query financial data.

![](https://github.com/KarmaScripter/BudgetExecution/blob/main/Resources/Assets/GitHubImages/Datagrid.PNG)

### Excel-like interface over a relational database.

![](https://github.com/KarmaScripter/BudgetExecution/blob/main/Resources/Assets/GitHubImages/ExcelUserInterface.PNG)

### Maps for congressional earmark reporting and pollution site monitoring.

![](https://github.com/KarmaScripter/BudgetExecution/blob/main/Resources/Assets/GitHubImages/Map.PNG)

### Baby Browser using the [Chromium Embedded Framework](https://en.wikipedia.org/wiki/Chromium_Embedded_Framework)

![](https://github.com/KarmaScripter/Baby/blob/main/Properties/Images/2.png)

### Budget Calculator for quick accounting transactions and budget calculations on the data.

![](https://github.com/KarmaScripter/BudgetExecution/blob/main/Resources/Assets/GitHubImages/Calculator.PNG)

### Federal fiscal year utilities compatable with full-time equivalency metrics.

![](https://github.com/KarmaScripter/BudgetExecution/blob/main/Resources/Assets/GitHubImages/FiscalYear.PNG)

### Environmental program definitions and statutory authorities bound directly to financial data

![](https://github.com/KarmaScripter/BudgetExecution/blob/main/Resources/Assets/GitHubImages/EnvironmentalPrograms.PNG)

### Data Visualization

![](https://github.com/KarmaScripter/BudgetExecution/blob/main/Resources/Assets/GitHubImages/Charts.PNG)
