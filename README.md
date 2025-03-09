## Budget-Py
![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/BudgetPy.png)
## Overview
The **Outlay Projector** is a forecasting model that uses historical expenditure data, 
generative AI, and machine-learning to project future outlays by agency and fiscal year.
- Data-Driven Forecasting – Uses historical budget data from FY1962 to FY2024 to predict FY2025 and beyond.  
- Machine Learning Integration – Gradient Boosting, Bayesian Ridge, and Polynomial Regressions for high-accuracy predictions. 

[![open_in_anaconda](https://static.anaconda.cloud/content/a22d04e8445b700f28937ab3231b8cded505d0395c63b7a269696722196d5415)](https://anaconda.cloud/api/nbserve/launch_notebook?nb_url=https%3A%2F%2Fraw.githubusercontent.com%2Fis-leeroy-jenkins%2FBoo%2Fmain%2Fipynb%2Foutlays.ipynb)



## ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/features.png)  Features
- Time Series Forecasting – Leverages ARIMA and Holt-Winters models to analyze seasonal and trend-based variations in budgetary spending.  
- Batch Processing for Large Datasets – Optimized for handling extensive federal financial data without memory overload.  
- Feature Engineering & Correlation Analysis – Utilizes PCA, Min-Max Scaling, Z-score Standardization, and K-Means clustering to enhance model performance.  
- Automated Outlay Projections – Provides yearly budget forecasts per agency with a simple data frame output.  
- [Outlay Project Model](https://anaconda.cloud/api/nbserve/launch_notebook?nb_url=https%3A%2F%2Fanaconda.cloud%2Fapi%2Fprojects%2Ff4ad0240-eaf1-4ad1-a8b4-99e630b46cda%2Ffiles%2Foutlays.ipynb%3Fversion%3D3c5763b3-e106-4e67-b314-3207f7f4ee71)
- Mutliple data providers including SQLite, MS Access, and SQL Servers Express Edition through [pyodbc](https://github.com/mkleehammer/pyodbc/wiki)
- Charting, plotting and reporting with matplotlib, dash, and pandas.
- Pre-defined schema for 100 environmental data tables.
- Access to editors for SQLite, MS Access, and SQL CE.


## ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/openai.png)  Generative AI

> Vectorization is the process of converting textual data into numerical vectors and is a process that is usually applied once the text is cleaned.
> It can help improve the execution speed and reduce the training time of your code. Bubba provides the following vector stores on the OpenAI platform to support environmental data analysis with machine-learning

- #### [Federal Appropriations](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/Appropriations.md) - vectorized data set of federal appropriations available for fine-tuning learning models
- #### [Federal Regulations](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/Regulations.md) - vectorized dat aset of federal, financial regulations available for fine-tuning learning models

> Badger incorporates machine learning and artificial intelligence algorithms to extract insights from large datasets.
> This includes the use of vector embeddings and predictive modeling to forecast contaminant spread and resource optimization to allocate resources effectively during emergencies


- #### Example run
## ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/Bubba.gif)

> Badger incorporates machine learning and artificial intelligence algorithms to extract insights from large datasets.
This includes the use of vector embeddings and predictive modeling to forecast contaminant spread and resource optimization to allocate resources effectively during emergencies.
Badger interacts with pre-trained Large Language Models (LLMs) like GPT-4o and o1-mini  to enhance its analytical capabilities.
Users leverage LLMs for rapid information retrieval from vast datasets, automated report generation, and potentially even expert consultation



## ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/Providers.png) Providers
- SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. [Learn more here](https://sqlite.org/index.html) 
- SQL Server Express Edition is a scaled down, free edition of SQL Server, which includes the core database engine. [Learn more here](https://www.microsoft.com/en-us/download/details.aspx?id=101064)
- MS Access is a database management system (DBMS) from Microsoft that combines the relational Access Database Engine (ACE) with a graphical user interface and software-development tools.  [Learn more here](https://www.microsoft.com/en-us/microsoft-365/access)



## ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/documentation.png)  Documentation
- See the [User Guide](etc/git/Users.md) for steps to get started.



## ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/python.png)  Code
- [Minion](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Minion.py) - other tools used and available in BudgetPy.
- [Booger](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Booger.py) - controls for the user interface and related functionality.
- [Data](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Data.py) - data access layer with environmental budget data models.
- [FileSys](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/FileSys.py) - classes for interacting with the file system and input/output.
- [Static](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Static.py) - enumerations used in budgetary data analysis.
- [Schema](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Schema.py) - schema definitions of the BudgetPy data tables.
- [Ninja](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Ninja.py)- budget data model classes for environmental programs.

## ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/system_requirements.png) System Requirements
- You will need these [Requirements](https://github.com/KarmaScripter/BudgetPy/blob/master/requirements.txt)



## ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/signature.png)  Code Signing 

BudgetPy uses free code signing provided by [SignPath.io](https://signpath.io/) and a free code signing certificate
from [SignPath Foundation](https://signpath.org/).


## ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/web.png) Privacy Policy

This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it.

BudgetPy has integrated the following services for additional functions, which can be enabled or disabled at the first start (in the welcome dialog) or at any time in the settings:

- [api.github.com](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) (Check for program updates)
- [ipify.org](https://www.ipify.org/) (Retrieve the public IP address used by the client)
- [ip-api.com](https://ip-api.com/docs/legal) (Retrieve network information such as geo location, ISP, DNS resolver used, etc. used by the client)

## 📝 License

BudgetPy is published under the [MIT General Public License v3](https://github.com/is-leeroy-jenkins/BudgetPy/blob/main/LICENSE).

The licenses of the libraries used can be found [here](https://github.com/is-leeroy-jenkins/BudgetPy/tree/main/Resources/Licenses).


