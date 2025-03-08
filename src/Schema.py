'''
  ******************************************************************************************
      Assembly:                BudgetPy
      Filename:                Schema.py
      Author:                  Terry D. Eppler
      Created:                 05-31-2023

      Last Modified By:        Terry D. Eppler
      Last Modified On:        06-01-2023
  ******************************************************************************************
  <copyright file="Schema.py" company="Terry D. Eppler">

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
    Schema.py
  </summary>
  ******************************************************************************************
  '''
from sqlalchemy import (MetaData, Table, create_engine)

metadata = MetaData( )
dbpath = r'db\sqlite\datamodels\Data.db'
engine = create_engine( 'sqlite:///' + dbpath )
metadata.reflect( bind = engine )

accounts = Table( 'Accounts', metadata, autoload=True, autoload_with=engine )

allocations = Table( 'Allocations', metadata, autoload=True,  autoload_with=engine )

actuals = Table( 'Actuals', metadata, autoload=True,  autoload_with=engine )

application_tables = Table( 'ApplicationTables', metadata, autoload=True,  autoload_with=engine )

appropriation_documents = Table( 'AppropriationDocuments', metadata,
	 autoload_with=engine )

appropriations = Table( 'Appropriations', metadata, autoload=True,  autoload_with=engine )

allowance_holders = Table( 'AllowanceHolders', metadata, autoload=True,  autoload_with=engine )

appropriation_balances = Table( 'AppropriationAvailableBalances', metadata,
	 autoload_with=engine )

apportionments = Table( 'ApportionmentData', metadata, autoload=True,  autoload_with=engine )

arp_carryover = Table( 'AmericanRescuePlanCarryoverEstimates', metadata, autoload=True,  
	 autoload_with=engine )

annual_carryover = Table( 'AnnualCarryoverEstimates', metadata, autoload=True,  
	 autoload_with=engine )

activity_codes = Table( 'ActivityCodes', metadata, autoload=True,  autoload_with=engine )

aggregate_outlays = Table( 'AggregateOutlays', metadata, autoload=True,  autoload_with=engine )

budget_controls = Table( 'BudgetControls', metadata, autoload=True,  autoload_with=engine )

budget_contacts = Table( 'BudgetContacts', metadata, autoload=True,  autoload_with=engine )

budget_documents = Table( 'BudgetDocuments', metadata, autoload=True,  autoload_with=engine )

budget_object_classes = Table( 'BudgetObjectClasses', metadata, 
	autoload_with=engine )

budget_fiscal_years = Table( 'BudgetFiscalYears', metadata, autoload=True, autoload_with=engine )

budgetary_resource_execution = Table( 'BudgetaryResourceExecution', metadata, autoload=True,
	 autoload_with=engine )

changes = Table( 'Changes', metadata, autoload=True,  autoload_with=engine )

carryover_apportionments = Table( 'CarryoverApportionments', metadata, autoload=True,
	 autoload_with=engine )

compass_levels = Table( 'CompassLevels', metadata, autoload=True,  autoload_with=engine )

cpic = Table( 'CapitalPlanningInvestmentCodes', metadata, autoload=True,  autoload_with=engine )

column_schema = Table( 'ColumnSchema', metadata, autoload=True,  autoload_with=engine )

congressional_controls = Table( 'CongressionalControls', metadata, autoload=True,
	 autoload_with=engine )

cost_areas = Table( 'CostAreas', metadata, autoload=True,  autoload_with=engine )

combined_schedules = Table( 'CombinedSchedules', metadata, autoload=True,
	 autoload_with=engine )

carryover_requests = Table( 'CarryoverRequests', metadata, autoload=True,
	 autoload_with=engine )

congressional_projects = Table( 'CongressionalProjects', metadata, autoload=True,
	 autoload_with=engine )

deobligations = Table( 'Deobligations', metadata, autoload=True,  autoload_with=engine )

data_rule_descriptions = Table( 'DataRuleDescriptions', metadata, autoload=True,
	 autoload_with=engine )

document_control_numbers = Table( 'DocumentControlNumbers', metadata, autoload=True,
	 autoload_with=engine )

defactos = Table( 'Defactos', metadata, autoload=True,
	 autoload_with=engine )

documents = Table( 'Documents', metadata, autoload=True,
	 autoload_with=engine )

expenditures = Table( 'Expenditures', metadata, autoload=True,
	 autoload_with=engine )

earmark_accounts = Table( 'EarmarkAccounts', metadata, autoload=True,
	 autoload_with=engine )

fund_categories = Table( 'FundCategories', metadata, autoload=True,
	 autoload_with=engine )

finance_object_classes = Table( 'FinanceObjectClasses', metadata, autoload=True,
	 autoload_with=engine )

full_time_equivalents = Table( 'FullTimeEquivalents', metadata, autoload=True,
	 autoload_with=engine )

federal_holidays = Table( 'FederalHolidays', metadata, autoload=True,
	 autoload_with=engine )

funds = Table( 'Funds', metadata, autoload=True,
	 autoload_with=engine )

fund_symbols = Table( 'FundSymbols', metadata, autoload=True,
	 autoload_with=engine )

general_ledger_accounts = Table( 'GeneralLedgerAccounts', metadata, autoload=True,
	 autoload_with=engine )

headquarters_offices = Table( 'HeadquartersOffices', metadata, autoload=True,
	 autoload_with=engine )

headquarters_authority = Table( 'HeadquartersAuthority', metadata, autoload=True,
	 autoload_with=engine )

ira_carryover = Table( 'InflationReductionActCarryoverEstimates', metadata, autoload=True,
	 autoload_with=engine )

iija_carryover = Table( 'JobsActCarryoverEstimates', metadata, autoload=True,
	 autoload_with=engine )

ledger_account_balances = Table( 'MonthlyLedgerAccountBalances', metadata, autoload=True,
	 autoload_with=engine )

monthly_outlays = Table( 'MonthlyOutlays', metadata, autoload=True,
	 autoload_with=engine )

monthly_actuals = Table( 'MonthlyActuals', metadata, autoload=True,
	 autoload_with=engine )

main_accounts = Table( 'MainAccounts', metadata, autoload=True,
	 autoload_with=engine )

marginal_outlays = Table( 'MarginalOutlays', metadata, autoload=True,
	 autoload_with=engine )

national_programs = Table( 'NationalPrograms', metadata, autoload=True,
	 autoload_with=engine )

operating_plans = Table( 'OperatingPlans', metadata, autoload=True,
	 autoload_with=engine )

outlays = Table( 'Outlays', metadata, autoload=True,
	 autoload_with=engine )

obligation_activity = Table( 'ObligationActivity', metadata, autoload=True,
	 autoload_with=engine )

obligations = Table( 'Obligations', metadata, autoload=True,
	 autoload_with=engine )

open_commitments = Table( 'OpenCommitments', metadata, autoload=True,
	 autoload_with=engine )

outlay_rates = Table( 'OutlayRates', metadata, autoload=True,
	 autoload_with=engine )

payroll_requests = Table( 'PayrollRequests', metadata, autoload=True,
	 autoload_with=engine )

payroll_authority = Table( 'PayrollAuthority', metadata, autoload=True,
	 autoload_with=engine )

pay_periods = Table( 'PayPeriods', metadata, autoload=True,
	 autoload_with=engine )

program_areas = Table( 'ProgramAreas', metadata, autoload=True,
	 autoload_with=engine )

program_projects = Table( 'ProgramProjects', metadata, autoload=True,
	 autoload_with=engine )

projects = Table( 'Projects', metadata, autoload=True,
	 autoload_with=engine )

public_laws = Table( 'PublicLaws', metadata, autoload=True,
	 autoload_with=engine )

program_results_codes = Table( 'PRC', metadata, autoload=True,
	 autoload_with=engine )

query_definitions = Table( 'QueryDefinitions', metadata, autoload=True,
	 autoload_with=engine )

resources = Table( 'Resources', metadata, autoload=True,
	 autoload_with=engine )

recovery_act = Table( 'RecoveryAct', metadata, autoload=True,
	 autoload_with=engine )

reimbursable_carryover = Table( 'AnnualReimbursableEstimates', metadata, autoload=True,
	 autoload_with=engine )

reimbursable_agreements = Table( 'ReimbursableAgreements', metadata, autoload=True,
	 autoload_with=engine )

resource_planning_offices = Table( 'ResourcePlanningOffices', metadata, autoload=True,
	 autoload_with=engine )

regional_offices = Table( 'RegionalOffices', metadata, autoload=True,
	 autoload_with=engine )

regional_authority = Table( 'RegionalAuthority', metadata, autoload=True,
	 autoload_with=engine )

reimbursable_funds = Table( 'ReimbursableFunds', metadata, autoload=True,
	 autoload_with=engine )

reporting_lines = Table( 'ReportingLines', metadata, autoload=True,
	 autoload_with=engine )

reconciliation_lines = Table( 'ReconciliationLines', metadata, autoload=True,
	 autoload_with=engine )

supplemental_carryover = Table( 'SupplementalCarryoverEstimates', metadata, autoload=True,
	 autoload_with=engine )

spending_documents = Table( 'SpendingDocuments', metadata, autoload=True,
	 autoload_with=engine )

spending_rates = Table( 'SpendingRates', metadata, autoload=True,
	 autoload_with=engine )

subappropriations = Table( 'SubAppropriations', metadata, autoload=True,
	 autoload_with=engine )

state_organizations = Table( 'StateOrganizations', metadata, autoload=True,
	 autoload_with=engine )

state_grant_obligations = Table( 'StateGrantObligations', metadata, autoload=True,
	 autoload_with=engine )

status_of_special_accounts = Table( 'StatusOfSpecialAccountFunds', metadata, autoload=True,
	 autoload_with=engine )

status_of_superfund_sites = Table( 'StatusOfSuperfundSites', metadata, autoload=True,
	 autoload_with=engine )

status_of_budget_execution = Table( 'StatusOfBudgetExecution', metadata,
	 autoload_with=engine )

status_of_resources = Table( 'StatusOfBudgetaryResources', metadata, autoload=True,
	 autoload_with=engine )

status_of_funds = Table( 'StatusOfFunds', metadata, autoload=True,
	 autoload_with=engine )

status_of_appropriations = Table( 'StatusOfAppropriations', metadata, autoload=True,
	 autoload_with=engine )

status_of_supplemental_funds = Table( 'StatusOfSupplementalFunds', metadata, autoload=True,
	 autoload_with=engine )

status_of_iija_funds = Table( 'StatusOfJobsActFunds', metadata, autoload=True,
	 autoload_with=engine )

status_of_arp_funds = Table( 'StatusOfAmericanRescuePlanFunds', metadata, autoload=True,
	 autoload_with=engine )

status_of_ira_funds = Table( 'StatusOfInflationReductionActFunds', metadata, autoload=True,
	 autoload_with=engine )

status_of_earmarks = Table( 'StatusOfEarmarks', metadata, autoload=True,
	 autoload_with=engine )

transtypes = Table( 'TransTypes', metadata, autoload=True,
	 autoload_with=engine )

treasury_symbols = Table( 'TreasurySymbols', metadata, autoload=True,
	 autoload_with=engine )

transfer_activity = Table( 'TransferActivity', metadata, autoload=True,
	 autoload_with=engine )

transfers = Table( 'Transfers', metadata, autoload=True,
	 autoload_with=engine )

unobligated_balances = Table( 'UnobligatedBalances', metadata, autoload=True,
	 autoload_with=engine )

unliquidated_obligations = Table( 'UnliquidatedObligations', metadata, autoload=True,
	 autoload_with=engine )
