class Source():
    '''Provides iterator for the Budget Execution table tables '''
    __data = [ ]
    __reference = [ ]

    @property
    def data( self ):
        ''' Property used to store table names in a list '''
        if self.__data is not None:
            return iter( self.__data )

    @property
    def reference( self ):
        ''' Property used to store table names in a list '''
        if self.__reference is not None:
            return iter( self.__reference )

    def __init__( self ):
        self.__data = [ 'Allocations', 'ApplicationTables', 'CarryoverEstimates',
                        'CarryoverSurvey', 'Changes', 'CongressionalReprogrammings',
                        'Deobligations', 'Defactos', 'DocumentControlNumbers',
                        'Obligations', 'OperatingPlans', 'OperatingPlanUpdates',
                        'ObjectClassOutlays', 'CarryoverOutlays', 'UnobligatedBalances',
                        'QueryDefinitions',  'RegionalAuthority', 'SpendingRates',
                        'GrowthRates', 'ReimbursableAgreements', 'ReimbursableFunds',
                        'ReimbursableSurvey', 'Reports', 'StatusOfAppropriations',
                        'BudgetControls', 'AppropriationDocuments', 'BudgetDocuments',
                        'Apportionments', 'BudgetOutlays', 'SF133',
                        'Reprogrammings', 'SiteActivity', 'SiteProjectCodes',
                        'StatusOfFunds', 'Supplementals', 'Transfers',
                        'HeadquartersAuthority', 'TravelObligations' ]
        self.__reference = [ 'Accounts', 'ActivityCodes',
                        'AllowanceHolders', 'Appropriations', 'BudgetObjectClasses',
                        'CostAreas', 'CPIC', 'Divisions',
                        'Documents', 'FederalHolidays', 'FinanceObjectClasses',
                        'FiscalYears', 'FiscalYearsBackUp', 'Funds',
                        'Goals', 'GsPayScale', 'Images',
                        'Messages', 'NationalPrograms', 'Objectives',
                        'Organizations', 'ProgramAreas', 'ProgramDescriptions',
                        'ProgramProjects', 'Projects', 'Providers',
                        'ReferenceTables', 'ResourcePlanningOffices', 'ResponsibilityCenters',
                        'SchemaTypes', 'Sources' ]

    def __iter__( self ):
        if len( self.__data ) > 0:
            for i in self.__data:
                yield i

