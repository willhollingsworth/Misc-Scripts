import os
import subprocess

def test_launch_detect_file_change() -> None:
    script_name = "detect_file_change.py"
    target_folder = os.getcwd()
    target_file_name = 'test_target_file.py'
    target_file_fullpath = target_folder + '\\' + target_file_name
    script_fullpath = target_folder + '\\' + script_name
    commands = ['python',script_name,target_folder,target_file_fullpath]
    print('testing',script_name)
    subprocess.run(commands)

if __name__ == '__main__':
    test_launch_detect_file_change()

