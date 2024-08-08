
from AlgorithmImports import *
from security_initializer import CustomSecurityInitializer
from universe import FScoreUniverseSelectionModel

class PiotroskiFScoreInvesting(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 7, 1) 
        self.SetEndDate(2023, 7, 1) 
        self.SetCash(10000000)

        fscore_threshold = self.GetParameter("fscore_threshold", 7)

    #fees but probably no fees in live
        self.SetBrokerageModel(BrokerageName.InteractiveBrokersBrokerage, AccountType.Margin)
        self.SetSecurityInitializer(CustomSecurityInitializer(self))   
        self.UniverseSettings.Resolution = Resolution.Minute       
        self.AddUniverseSelection(FScoreUniverseSelectionModel(self, fscore_threshold))        
        self.AddAlpha(ConstantAlphaModel(InsightType.Price, InsightDirection.Up, timedelta(1)))      
        self.SetPortfolioConstruction(SectorWeightingPortfolioConstructionModel())      
        self.SetExecution(SpreadExecutionModel(0.01))   
        self.AddRiskManagement(NullRiskManagementModel())

    def OnSecuritiesChanged(self, changes):
        if self.LiveMode:
            self.Log(changes)
