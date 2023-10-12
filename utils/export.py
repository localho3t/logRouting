import datetime
import os
from termcolor import colored

def export(folder,name,content):
    folder = f"./export/{folder}"
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(colored(f"[!] create folder ./export/{folder}",'green'))

    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f'{folder}/{name}_{formatted_datetime}.txt'
    with open(file_name, 'w+') as file:
        file.writelines(str(content))

    return file_name
