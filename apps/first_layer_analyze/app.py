from termcolor import colored
import re
from apps.first_layer_analyze.ip_requests.ip import IPCalculator
from apps.first_layer_analyze.methods.methods import MethodCalculator
from apps.first_layer_analyze.status_code.status_code import StatusCodeCalculator


class FirstLayerAnalyze:
    ip_calc = IPCalculator()
    method_calc = MethodCalculator()
    scc = StatusCodeCalculator()
    file_path = ""
    def __init__(self,fp):
        self.file_path = fp
        self._start_analyze()

    def _start_analyze(self):
        nginx_log_pattern = r'(\d+\.\d+\.\d+\.\d+) - - \[([^\]]+)\] "([A-Z]+) ([^"]+)" (\d+) (\d+) "([^"]+)" "([^"]+)"'
        print(
            colored(f"[*] start [{colored(' first layer analyze ','yellow')}", 'green'), colored("] ...",'green'))

        with open(self.file_path,'r') as f:
            data = f.read()

        matches = re.findall(nginx_log_pattern, data)

        for match in matches:
            ip = match[0]
            Method = match[2]
            Status = match[4]
            self.ip_calc.set_ips(ip)
            self.method_calc.set_method(Method)
            self.scc.set_status_code(Status)

        self.ip_calc.get_ips()
        self.method_calc.get_method()
        self.scc.get_status_code()

