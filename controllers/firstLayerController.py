from apps.first_layer_analyze.app import FirstLayerAnalyze

class FirstLayerController:
    fp = ""
    def __init__(self,fp):
        self.fp = fp
        FirstLayerAnalyze(self.fp)
