from controllers.firstLayerController import FirstLayerController
from controllers.secondLayserController import SecondLayerController

from termcolor import colored

class Controllers:
    fp = ""
    root = None
    def __init__(self,fp,root) :
        self.fp = fp
        self.root = root

        self._start_first_layer_controller()
        self._start_second_layer_controller()


    def _start_first_layer_controller(self):
        FirstLayerController(self.fp)

    def _start_second_layer_controller(self):
        SecondLayerController(self.fp,self.root)
