import re
from termcolor import colored
from prettytable import PrettyTable
from utils.export import export

class SecondLayerAnalyze:
    fp = ""
    root = []

    def __init__(self, fp, root):
        self.fp = fp
        self.root = root
        self._start_analyze()

    def _start_analyze(self):
        table = PrettyTable()
        table.field_names = ["ip", "path"]

        print(
            colored(f"[*] start [{colored(' second layer analyze ','yellow')}", 'green'), colored("] ...", 'green'))
        log_dict = {}

        with open(self.fp, 'r') as log_file:
            for line in log_file:
                match = re.search(
                    r'(\d+\.\d+\.\d+\.\d+).*?"GET (.*?) HTTP', line)
                if match:
                    ip = match.group(1)
                    path = match.group(2)
                    if path != "":
                        if ip in log_dict:
                            log_dict[ip].append(path)
                        else:
                            log_dict[ip] = [path]
        flag = 0
        for i, ii in log_dict.items():
            table.add_row([i, ii])

        file_name = export("SeconfLayerAnalyze", "path", table)
        print(colored(f"path analyze file : {file_name}", 'yellow'))


        user_results = {}

        for user, paths in log_dict.items():
            user_results[user] = {}
            all_paths_matched = all(path in paths for path in self.root)
            user_results[user]["all_matched"] = all_paths_matched

        for user, results in user_results.items():
            if results["all_matched"]:
                message = f"[*] User {user}: All paths matched."
                colored_message = colored(message, 'green')
                print(colored_message)
