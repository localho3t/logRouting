import sys
import os
from termcolor import colored
import re
class ArgValidator:
    # data = {}
    def validate(self):
        regex_pattern = r'\[.*\]'
        log_file = ""
        data = {}

        if sys.argv[1] == "-h" or sys.argv[1] == "-H" or sys.argv[1] == "--help":
            print(
                colored("[^] python3 main.py -f [log file] -r [/,/login,/dashboard]", 'yellow'))
            exit()
        # print(len(sys.argv))
        if len(sys.argv) !=  5:
            print(colored("[!] Arg Error ... [-h]",'red'))
            exit()

        if sys.argv[1] == "-f":
            if os.path.exists(sys.argv[2]):
                print(colored("[^] file is found ...", 'green'))
                log_file = sys.argv[2]
            else:
                print(colored("[404] file is not found ...", 'red'))
                exit()
            if sys.argv[3] == "-r":
                if re.match(regex_pattern, sys.argv[4]):
                    print(colored("[^] match pattern ...", 'green'))
                    root_argv = sys.argv[4]
                    root_argv = root_argv.strip("[]")
                    if root_argv == "":
                        print(
                            colored("[!] pattern Error sample : [/index]", 'red'))
                        exit()
                    else:
                        data = {
                            'file': log_file,
                            'root': root_argv
                        }
                        return data
                else:
                    print(colored("[!] pattern Error sample : [/index]" ,'red'))
                    exit()

            else:
                print(
                    colored("[^] python3 main.py -f [log file] -r [/,/login,/dashboard]", 'yellow'))
                exit()
