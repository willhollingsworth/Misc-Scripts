'''
Detect if file has been created, deleted or changed within a folder
Can be limited to a certain filetype
'''

import os
import time

def get_files(folder:str,file_type:str) -> dict[str,list]:
    '''
    given a folder get all files, their size and mod date
    '''
    output_files = {}
    for root,dirs,files in os.walk(folder):
        # print(files)
        for file in files:
            if file_type:
                current_file_type = file[-3:].lower()
                if current_file_type != file_type:
                    continue
            path = f'{root}\\{file}'
            output_files[path] = get_file_details(path)
    return output_files

def get_file_details(file_path:str) -> list:
    '''get the size and modified date of a file'''
    size = os.path.getsize(file_path)
    date = os.path.getmtime(file_path)
    return [size,date]


def check_for_changes(new_files:dict,old_files:dict) -> bool:
    '''check two dicts of files for any changes'''
    if new_files.keys() != old_files.keys():
        '''file either deleted or created'''
        return True
    for file,details in old_files.items():
        for i,detail in enumerate(details):
            if old_files[file][i] != new_files[file][i]:
                '''old file details are different'''
                return True
    return False

def main_loop(target_folder:str = os.getcwd(),check_interval: float = 2,file_type:str = '') -> ...:
    '''keep checking a folder for any changes'''
    print(f'Detecting all changes for {target_folder}, check interval:{check_interval}')
    old_files = get_files(target_folder,file_type)
    while True:
        new_files = get_files(target_folder,file_type)
        change = check_for_changes(new_files, old_files)
        if change:
            print('change')
        old_files = new_files
        time.sleep(check_interval)

if __name__ == '__main__':
    main_loop(file_type='txt')



