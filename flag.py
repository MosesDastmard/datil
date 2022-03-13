import ntpath
import os
from os.path import join

def get_file_info(file_path : str) -> dict:
    """it takes a file path and returns information about the file like:
    'directory': the directory path where the file resides
    'base_file_name': the file name without extentation example.zip -> example
    'flag_name' : 'base_file_name' + .flg
    'flag_path' : 'directory' + 'flag_name'

    Args:
        file_path (str): path to a file

    Returns:
        dict: file info in dictoinary format
    """        
    directory = os.path.dirname(file_path)
    file_name = ntpath.basename(file_path)
    base_file_name, extention = os.path.splitext(file_name)
    return {'directory':directory,
            'base_file_name':base_file_name,
            'file_name':file_name,
            'extention':extention}

class Flag:
    def __init__(self, flag_extention) -> None:
        self.flag_extention = flag_extention
        self.get_file_info = get_file_info

    def get_flag_path(self, file_path):
        file_info = self.get_file_info(file_path)
        flag_name = "." + file_info['file_name'] + "." + self.flag_extention + '.flg'
        flag_path = join(file_info['directory'], flag_name)
        return flag_path

    def exists(self, file_path : str) -> bool:
        """validates if for a given file, the flag file exists, if so

        Args:
            file_path (str): file path

        Returns:
            bool: True if flag file for given file exists, otherwise False
        """        
        flag_path = self.get_flag_path(file_path)
        if os.path.exists(flag_path):
            return True
        else:
            return False

    def __flag(self, file_paths: list, mode):
        """it drops flag file along the given files that their full path provided

        Args:
            file_paths (list): list of files path, if an string provided, it converts to a list of single path

        Raises:
            Exception: if file path is not valid
        """        

        if type(file_paths) == str:
             file_paths = [file_paths]
        if type(file_paths) != list:
            raise Exception('file_paths should be a string path or list of string paths')
        for file_path in file_paths:
            flag_path = self.get_flag_path(file_path)
            if mode == 'put':
                open(flag_path, 'w').close()
            elif mode == 'remove':
                os.remove(flag_path)
            else:
                raise Exception(f'mode has to be eigther "put" or "remove" (mode={mode} is not acceptable)')

    def put(self, file_paths):
        self.__flag(file_paths=file_paths, mode='put')

    def remove(self, file_paths):
        self.__flag(file_paths=file_paths, mode='remove')