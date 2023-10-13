from termcolor import colored
from prettytable import PrettyTable
from utils.export import export


class MethodCalculator:
    _method = {}

    def set_method(self, method):
        if self._method.get(method):
            self._method[method]['count'] = self._method[method]['count']+1
        else:
            self._method[method] = {"count": 1}

    def export_method(self):
        table = PrettyTable()
        table.field_names = ["method", "count"]

        for i, ii in self._method.items():
            table.add_row([i, ii['count']])

        file_name = export("FirstLayerAnalyz", "method", table)
        print(colored(f"method analyze file : {file_name}", 'yellow'))
