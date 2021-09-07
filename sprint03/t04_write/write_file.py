import os
from pathlib import Path


def write_file(f_name, add_message='None'):
    if Path(f_name).suffix != '.txt':
        print("Please enter the filename in the format \"filename.txt\".")
        print(f'Failed to write to file "{f_name}".')
    else:
        with open(f_name, "w") as created_file:
            created_file.write(add_message)
        with open(f_name, "r") as r_file:
            data = r_file.read()
            if data != add_message or data == "":
                print('Something went wrong...')
            else:
                print(f'Your message has been written to file "{f_name}".')
                print(f'File "{f_name}" now contains the following text:\n'
                      f'{add_message}')