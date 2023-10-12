from termcolor import colored

class Banner:
    def __init__(self) -> None:
        print(colored("""
┓       ┳┓     •
┃ ┏┓┏┓  ┣┫┏┓┓┏╋┓┏┓┏┓
┗┛┗┛┗┫  ┛┗┗┛┗┻┗┗┛┗┗┫
     ┛             ┛ v0.0.1 (nginx)
""",'red'))
