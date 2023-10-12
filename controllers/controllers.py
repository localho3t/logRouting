from controllers.firstLayerController import FirstLayerController

class Controllers:
    fp = ""
    root = None
    def __init__(self,fp,root) :
        self.fp = fp
        self.root = root
        # print(self.root)
        self._start_first_layer_controller()


    def _start_first_layer_controller(self):
        FirstLayerController(self.fp)
