##### Budget-Py

<img src="https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/git/line-graphs.gif" style="width:950px;height:275px">

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/training.png)  Overview
- Projections of federal outlays, as required by law, reflect the assumption that current laws will generally remain unchanged. Those projections 
encompass the current year—the year in which the projections are made and a projection period of 5 
or 10 years in the future. 
- BudgetPy incorporates machine learning and artificial intelligence algorithms to extract insights from large datasets. 
- Vector embeddings and predictive modeling to forecast contaminant spread and resource optimization to allocate resources effectively during emergencies. 
- BudgetPy interacts with pre-trained Large Language Models (LLMs) like GPT-4o, o3, and o1-mini to enhance its analytical capabilities. 
- Users leverage LLMs for rapid information retrieval from vast datasets, automated report generation, and potentially even expert consultation
___

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/MachineLearning.png)  Generative AI Tools

- #### [Outlay-Projection Tool](https://colab.research.google.com/github/is-leeroy-jenkins/Sige/blob/master/outlays.ipynb)
> A specialized machine-learning and time-series forecasting tool built for data scientists, budget officers, and comptrollers
> working with appropriated funding and federal outlays by providing a neural-network based on regressions, decision trees,
> gradient boosting, support vector machines, and time-series modeling that project monthly or quarterly obligations and
> outlays at the Treasury Account level

- #### [Account-Balance Estimates](https://colab.research.google.com/github/is-leeroy-jenkins/Cutey/blob/main/balances.ipynb)
> The federal balance forecastor is a deep-learning toolkit for federal budget execution & finance that is implemented in python
> empowering data scientists, budget officers, comptrollers and federal agency personnel to train, compare, and visualize multiple
> models for forecasting federal appropriation at the TAS-level. Built using Scikit, TensorFlow, and PyTorch,
> the notebook integrates structured budget execution data—such as SF-133 reports from OMB and agency-specific datasets
> from Data.gov—to inform predictive models across multiple federal financial scenarios.

- #### [Obligation-Rate Forecastor](https://colab.research.google.com/github/is-leeroy-jenkins/Sake/blob/master/models.ipynb)
> A modular machine-learning pipeline for budget execution and data analysis built in Python with Scikit, XGBoost, PyTorch,
> and TensorFlow. Designed for rapid proto-typing in IMT enviornment to calculate mission assignment burn-rates, visualizations,
> and benchmarking for classification and regression models. It provides a structured yet extensible workflow that’s
> equally useful for teaching, prototyping, and real-world application development.

___

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/ai.png) Data-Driven Forecasting 
- Uses historical budget data from the Office of Management & Budget from FY1962 to FY2024 to predict FY2025 and beyond. 
- Traditional data sets available via [Kaggle](https://www.kaggle.com/terryeppler/datasets)
- Vectorized data sets available via Hugging Face below.

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/openai.png)  Machine-Learning

> - Vectorization is the process of converting textual data into numerical vectors and is a process that is usually applied once the text is cleaned.
> - It can help improve the execution speed and reduce the training time of your code. 
> - BudgetPy provides the following vector stores on the OpenAI platform to support environmental data analysis with machine-learning
- [Appropriations](https://huggingface.co/datasets/leeroy-jankins/Appropriations) - Enacted appropriations from 1996-2024 available for fine-tuning learning models
- [Regulations](https://huggingface.co/datasets/leeroy-jankins/Regulations/tree/main) - Collection of federal regulations on the use of appropriated funds
- [SF-133](https://huggingface.co/datasets/leeroy-jankins/SF133) - The Report on Budget Execution and Budgetary Resources
- [Balances](https://huggingface.co/datasets/leeroy-jankins/Balances) -  U.S. federal agency Account Balances (File A) submitted as part of the DATA Act 2014.
- [Outlays](https://huggingface.co/datasets/leeroy-jankins/Outlays) -  The actual disbursements of funds by the U.S. federal government from 1962 to 2025
- [SF-133](https://huggingface.co/datasets/leeroy-jankins/SF133) The Report on Budget Execution and Budgetary Resources
- [Balances](https://huggingface.co/datasets/leeroy-jankins/Balances) - U.S. federal agency Account Balances (File A) submitted as part of the DATA Act 2014.
- [Circular A11](https://huggingface.co/datasets/leeroy-jankins/OMB-Circular-A-11) - Guidance from OMB on the preparation, submission, and execution of the federal budget
- [Fastbook](https://huggingface.co/datasets/leeroy-jankins/FastBook) - Treasury guidance on federal ledger accounts
- [Title 31 CFR](https://huggingface.co/datasets/leeroy-jankins/Title-31-CFR-Money-and-Finance) - Money & Finance
- [Redbook](https://huggingface.co/datasets/leeroy-jankins/RedBook) - The Principles of Appropriations Law (Volumes I & II).
- [US Standard General Ledger](https://huggingface.co/datasets/leeroy-jankins/US-General-Ledger) - Account Definitions
- [Treasury Appropriation Fund Symbols (TAFSs) Dataset](https://huggingface.co/datasets/leeroy-jankins/Accounts) - Collection of TAFSs used by federal agencies


- #### 4o model run
![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/Bubba.gif)

___

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/features.png)  Features
- [Time Series Forecasting](https://en.wikipedia.org/wiki/Time_series) – Leverages ARIMA and Holt-Winters models to analyze seasonal and trend-based variations in budgetary spending.  
- Batch Processing for Large Datasets – Optimized for handling extensive federal financial data without memory overload.  
- [Feature Engineering](https://en.wikipedia.org/wiki/Feature_engineering) & [Correlation Analysis](https://en.wikipedia.org/wiki/Correlation)  – Utilizes PCA, Min-Max Scaling, Z-score Standardization, and K-Means clustering to enhance model performance.  
- Automated Outlay Projections – Provides yearly budget forecasts per agency with a simple data frame output.  
- Mutliple data providers including SQLite, MS Access, and SQL Servers Express Edition through [pyodbc](https://github.com/mkleehammer/pyodbc/wiki)
- Charting, plotting and reporting with matplotlib, dash, and pandas.
- Pre-defined schema for 100 environmental data tables.
- Access to editors for SQLite, MS Access, and SQL CE.

___

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/training.png) How It Works
#### 1️⃣ **Data Processing**
- Loads federal budget data from **"Budget Outlays.xlsx"**.
- Filters **fiscal year data (2012–2024)** and groups outlays **by agency**.
- Handles **missing values and data inconsistencies**.
  
#### 2️⃣ **Model Training**
- Uses **Random Forest Regression** as the primary predictive model.
- Splits data into **training (80%) and testing (20%)** sets.
- Trains on **FY2012-FY2023** to predict **FY2024** and validates performance.

#### 3️⃣ **Outlay Forecasting**
- Predicts **FY2025 outlays for each federal agency**.
- Outputs results in a structured **data frame** for easy interpretation.

___

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/install.png) Installation & Usage
#### **4️⃣ Clone the Repository**
```sh
git clone https://github.com/your-repo/federal-budget-forecast.git
cd federal-budget-forecast
```

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/python.png) Python Code
- [Minion](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Minion.py) - other tools used and available in BudgetPy.
- [Booger](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Booger.py) - controls for the user interface and related functionality.
- [Data](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Data.py) - data access layer with environmental budget data models.
- [FileSys](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/FileSys.py) - classes for interacting with the file system and input/output.
- [Static](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Static.py) - enumerations used in budgetary data analysis.
- [Schema](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Schema.py) - schema definitions of the BudgetPy data tables.
- [Ninja](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/src/Ninja.py)- budget data model classes for environmental programs.

___

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/Providers.png) Providers
- SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. [Learn more here](https://sqlite.org/index.html) 
- SQL Server Express Edition is a scaled down, free edition of SQL Server, which includes the core database engine. [Learn more here](https://www.microsoft.com/en-us/download/details.aspx?id=101064)
- MS Access is a database management system (DBMS) from Microsoft that combines the relational Access Database Engine (ACE) with a graphical user interface and software-development tools.  [Learn more here](https://www.microsoft.com/en-us/microsoft-365/access)



### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/documentation.png)  Documentation
- See the [User Guide](etc/git/Users.md) for steps to get started.



### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/system_requirements.png) System Requirements
- You will need these [Requirements](https://github.com/KarmaScripter/BudgetPy/blob/master/requirements.txt)

___

### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/signature.png)  Code Signing 

BudgetPy uses free code signing provided by [SignPath.io](https://signpath.io/) and a free code signing certificate
from [SignPath Foundation](https://signpath.org/).


### ![](https://github.com/is-leeroy-jenkins/BudgetPy/blob/master/etc/img/github/web.png) Privacy Policy

This program will not transfer any information to other networked systems unless specifically requested by the user or the person installing or operating it.

BudgetPy has integrated the following services for additional functions, which can be enabled or disabled at the first start (in the welcome dialog) or at any time in the settings:

- [api.github.com](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement) (Check for program updates)
- [ipify.org](https://www.ipify.org/) (Retrieve the public IP address used by the client)
- [ip-api.com](https://ip-api.com/docs/legal) (Retrieve network information such as geo location, ISP, DNS resolver used, etc. used by the client)

___


### 🙏 Acknowledgements

BudgetPy uses the following projects and libraries. Please consider supporting them as well (e.g., by starring their repositories):

| Project                                                             | Description                                                                                              |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [SciPy](https://scipy.org/)                                         | Fundamental algorithms for scientific computing in Python                                                |
| [Tensorflow](https://www.tensorflow.org/)                  		       | An end-to-end platform for machine learning								                                                      |
| [Pandas](https://pandas.pydata.org/docs/getting_started/index.html) | An open source, easy-to-use data structures and data analysis tools for the Python programming language. |
| [Numpy](https://numpy.org/)                                         | The fundamental package for scientific computing with Python    			                                      |
| [Keras](https://keras.io/about/)                                    | Deep learning API written in Python and capable of running on top of either JAX, TensorFlow, or PyTorch. |
| [PyTorch](https://pytorch.org/)                                     | Tensors and Dynamic neural networks in Python with strong GPU acceleration                               |
| [pyodbc](https://pypi.org/project/pyodbc/)   	                      | pyodbc is an open source Python module that makes accessing ODBC databases simple. 									             |
| [PySimplGUI](https://github.com/PySimpleGUI/PySimpleGUI)            | Python GUIs for Humans! PySimpleGUI is the top-rated Python application development environment.								 |
| [Scikit-Learn](https://github.com/scikit-learn/scikit-learn)        | Machine learning in Python					                                                                          |
| [OpenAI](https://github.com/openai/openai-python) 	                 | The official Python library for the OpenAI API							                                                    |

___

## 📝 License

BudgetPy is published under the [MIT General Public License v3](https://github.com/is-leeroy-jenkins/BudgetPy/blob/main/LICENSE).

The licenses of the libraries used can be found [here](https://github.com/is-leeroy-jenkins/BudgetPy/tree/main/Resources/Licenses).


