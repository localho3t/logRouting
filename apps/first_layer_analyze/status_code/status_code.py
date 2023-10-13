from termcolor import colored
from prettytable import PrettyTable
from utils.export import export


class StatusCodeCalculator:
    _status_code = {}

    def set_status_code(self, ip):
        if self._status_code.get(ip):
            self._status_code[ip]['count'] = self._status_code[ip]['count']+1
        else:
            self._status_code[ip] = {"count": 1}

    def export_status_code(self):
        table = PrettyTable()
        table.field_names = ["ip", "count"]

        for i, ii in self._status_code.items():
            table.add_row([i, ii['count']])

        file_name = export("FirstLayerAnalyz", "status_code", table)
        print(colored(f"status code analyze file : {file_name}", 'yellow'))
