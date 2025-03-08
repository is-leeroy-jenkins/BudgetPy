## Budget-Py
![](https://github.com/KarmaScripter/BudgetPy/blob/master/etc/img/github/BudgetPy.png)
## Overview
The **Outlay Projector** is a forecasting model that uses historical expenditure data, 
generative AI, and machine-learning to project future outlays by agency and fiscal year.
- **Data-Driven Forecasting** – Uses historical budget data from **FY1962 to FY2024** to predict **FY2025 and beyond**.  
- **Machine Learning Integration** – Implements **Random Forest, Gradient Boosting, Bayesian Ridge Regression, and Polynomial Regression** for high-accuracy predictions. 
[![open_in_anaconda](https://static.anaconda.cloud/content/a22d04e8445b700f28937ab3231b8cded505d0395c63b7a269696722196d5415)](https://anaconda.cloud/api/nbserve/launch_notebook?nb_url=https%3A%2F%2Fraw.githubusercontent.com%2Fis-leeroy-jenkins%2FBoo%2Fmain%2Fipynb%2Foutlays.ipynb)



## Features 
- **Time Series Forecasting** – Leverages **ARIMA and Holt-Winters models** to analyze **seasonal and trend-based variations** in budgetary spending.  
- **Batch Processing for Large Datasets** – Optimized for handling extensive federal financial data without memory overload.  
- **Feature Engineering & Correlation Analysis** – Utilizes **PCA, Min-Max Scaling, Z-score Standardization**, and **K-Means clustering** to enhance model performance.  
- **Automated Outlay Projections** – Provides **yearly budget forecasts per agency** with a simple **data frame output**.  
- [Outlay Project Model](https://anaconda.cloud/api/nbserve/launch_notebook?nb_url=https%3A%2F%2Fanaconda.cloud%2Fapi%2Fprojects%2Ff4ad0240-eaf1-4ad1-a8b4-99e630b46cda%2Ffiles%2Foutlays.ipynb%3Fversion%3D3c5763b3-e106-4e67-b314-3207f7f4ee71)

- Mutliple data providers including SQLite, MS Access, and SQL Servers Express Edition through [pyodbc](https://github.com/mkleehammer/pyodbc/wiki)
- Charting, plotting and reporting with matplotlib, dash, and pandas.
- Pre-defined schema for 100 environmental data tables.
- Access to editors for SQLite, MS Access, and SQL CE.

## Providers
- SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. [Learn more here](https://sqlite.org/index.html) 
- SQL Server Express Edition is a scaled down, free edition of SQL Server, which includes the core database engine. [Learn more here](https://www.microsoft.com/en-us/download/details.aspx?id=101064)
- MS Access is a database management system (DBMS) from Microsoft that combines the relational Access Database Engine (ACE) with a graphical user interface and software-development tools.  [Learn more here](https://www.microsoft.com/en-us/microsoft-365/access)


## System requirements
- You will need these [Requirements](https://github.com/KarmaScripter/BudgetPy/blob/master/requirements.txt)




## Documentation
- See the [User Guide](etc/git/Users.md) for steps to get started.




## Code
- [Minion](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Minion.py) - other tools used and available in BudgetPy.
- [Booger](https://github.com/KarmaScripter/BudgetPy/blob/master/src/Booger.py) - controls for the user interface and related functionality.
- [Data](https://github.com/KarmaScripter/BudgetPy/blob/master/src/Data.py) - data access layer with environmental budget data models.
- [FileSys](https://github.com/KarmaScripter/BudgetPy/blob/master/src/FileSys.py) - classes for interacting with the file system and input/output.
- [Static](https://github.com/KarmaScripter/BudgetPy/blob/master/src/Static.py) - enumerations used in budgetary data analysis.
- [Schema](https://github.com/KarmaScripter/BudgetPy/blob/master/src/Schema.py) - schema definitions of the BudgetPy data tables.
- [Ninja](https://github.com/KarmaScripter/BudgetPy/blob/master/src/Ninja.py)- budget data model classes for environmental programs.

## Credits


