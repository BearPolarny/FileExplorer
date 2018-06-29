import sys
import os


class Explorer:
    def __init__(self):
        self.path = 'C:/Users/Ja/Desktop'  # TODO: Zmienić Ja na zalogowanego użytkownika
        self.__test = os.getcwd()
        self.dirs = os.listdir(self.path)

    def dir_to_list(self):
        self.dirs = os.listdir(self.path)
        for d in self.dirs:
            if os.path.isdir(self.path + '/' + d):
                print('./', end='')
            print(d)


if __name__ == '__main__':
    e = Explorer()
    e.dir_to_list()
    newpath = input()
    while newpath.lower() != 'exit':
        if newpath in e.dirs:
            e.path += '/'
            e.path += newpath
            os.system('cls')
            e.dir_to_list()
            print(e.path)
        elif newpath == '..':
            e.path = e.path[:e.path.rfind('/')]
            e.dir_to_list()
        else:
            print('Wrong directory')
        newpath = input()
