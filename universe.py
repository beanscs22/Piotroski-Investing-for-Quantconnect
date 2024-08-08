# region imports
from AlgorithmImports import *
from f_score import *

class FScoreUniverseSelectionModel(FineFundamentalUniverseSelectionModel):

    def __init__(self, algorithm, fscore_threshold):
        super().__init__(self.SelectCoarse, self.SelectFine)
        self.algorithm = algorithm
        self.fscore_threshold = fscore_threshold

    def SelectCoarse(self, coarse):
        return [x.Symbol for x in coarse if x.Price > 1]

    def SelectFine(self, fine):
        f_scores = {}

        for f in fine:
            # find the f score
            f_scores[f.Symbol] = self.GetPiotroskiFScore(f)
            if f_scores[f.Symbol] >= self.fscore_threshold and self.algorithm.LiveMode:
                self.algorithm.Log(f"Stock: {f.Symbol.ID} :: F-Score: {f_scores[f.Symbol]}")

        selected = [symbol for symbol, fscore in f_scores.items() if fscore >= self.fscore_threshold]

        return selected

    def GetPiotroskiFScore(self, fine):

        fscore = 0
        fscore += GetROAScore(fine)
        fscore += GetOperatingCashFlowScore(fine)
        fscore += GetROAChangeScore(fine)
        fscore += GetAccrualsScore(fine)
        fscore += GetLeverageScore(fine)
        fscore += GetLiquidityScore(fine)
        fscore += GetShareIssuedScore(fine)
        fscore += GetGrossMarginScore(fine)
        fscore += GetAssetTurnoverScore(fine)
        return fscore
