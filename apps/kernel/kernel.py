from termcolor import colored
from apps.banner.banner_v1 import Banner
from utils.arg_validator import ArgValidator

class Kernel:
    def __init__(self):
        Banner()
        vl = ArgValidator()
        gd = vl.validate()
        print(colored("[*] start Kernel ...",'green'))

        file = gd['file']
        root_check = gd['root']
