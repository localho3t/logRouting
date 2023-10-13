from apps.second_layer_analyze.app import SecondLayerAnalyze


class SecondLayerController:
    fp = ""
    root = []
    def __init__(self, fp,root):
        self.fp = fp
        self.root = root
        SecondLayerAnalyze(self.fp,self.root)
