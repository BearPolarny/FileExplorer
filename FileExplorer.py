import time
import os
from pathlib import Path


class Explorer:
    def __init__(self):
        self.path = str(Path.home()) + '\\Desktop'
        self.__test = os.getcwd()
        self.dirs = os.listdir(self.path)

    def dir_to_list(self):
        if os.path.isdir(self.path):
            try:
                self.dirs = os.listdir(self.path)
            except PermissionError:
                print('You don\'t have permission to enter this directory')
                time.sleep(2)
                os.system('cls')
                self.retrack()
                self.dir_to_list()
            for d in self.dirs:
                if os.path.isdir(self.path + '\\' + d):
                    print('>./', end='')
                else:
                    print('>  ', end='')
                print(d)
        else:
            print('Open File not implemented yet')
            time.sleep(1)
            os.system('cls')
            self.retrack()
            self.dir_to_list()

    def append(self, directory):
        self.path += '\\'
        self.path += directory

    def retrack(self):
        self.path = self.path[:self.path.rfind('\\')]
        if len(self.path) == 2:
            self.append('')

    def list_items(self, newpath):
        found = []
        for d in self.dirs:
            if d.lower() == newpath.lower():
                self.append(d)
                return True
            elif d.lower().startswith(newpath.lower()):
                found.append(d)
        os.system('cls')
        if not len(found):
            print('Wrong directory')
            time.sleep(1)
            os.system('cls')
        elif len(found) == 1:
            self.append(found[0])
        else:
            for f in found:
                if os.path.isdir(self.path + '\\' + f):
                    print('./' + f)

            return False
        return True


if __name__ == '__main__':

    explorer = Explorer()
    newpath = ''
    while newpath.lower() != 'exit':
        pr = True
        os.system('cls')
        if newpath == '..':
            explorer.retrack()
        elif newpath != '':
            pr = explorer.list_items(newpath)
        if pr:
            explorer.dir_to_list()
        newpath = input(explorer.path + '>')
    os.system('cls')
