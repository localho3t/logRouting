from termcolor import colored
from prettytable import PrettyTable
from utils.export import export
class IPCalculator:
    _ips = {}

    def set_ips(self,ip):
        if self._ips.get(ip):
            self._ips[ip]['count'] = self._ips[ip]['count']+1
        else:
            self._ips[ip] = {"count": 1}

    def export_ips(self):
        table = PrettyTable()
        table.field_names = ["ip","count"]

        for i,ii in self._ips.items():
            table.add_row([i,ii['count']])

        file_name = export("FirstLayerAnalyz","ips",table)
        print(colored(f"ip analyze file : {file_name}", 'yellow'))


