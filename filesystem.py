# Case-study
# Developers:
# Marinkin O. (66%),
# Seledtsov A. (36%),
# Evdischenko M. (59%)

import os
from pathlib import Path
import time

path_Main = 'F:/case'


def sleep():
    """Output delay function"""
    print()
    time.sleep(1)


def main(path):
    """Menu output function"""
    print()
    print(path)
    print(('1. Browse catalog\n2. Up the branch\n3. Down the branch\n4. Number of files in the directory\n'
           '5. Directory size in bytes\n6. File search\n7. Exit\n'))
    time.sleep(1)
    acceptCommand(path)


def acceptCommand(path):
    """Selection input function"""
    print('Please select:')
    command = input()
    if command == 'exit':
        command = 7
    command = int(command)
    if not (command in [1, 2, 3, 4, 5, 6, 7]):
        print('ERROR')
        sleep()
        acceptCommand(path)
    runCommand(command, path)


def runCommand(n, path):
    """A function that defines the execution of a function"""
    if n == 1:
        dir_watch(path)
    if n == 2:
        moveUp(path)
    if n == 3:
        fname = input()
        fname = '/' + fname + '/'
        moveDown(path, fname)
    if n == 4:
        sleep()
        print(len(countFiles(path, [])))
        main(path)
    if n == 5:
        sleep()
        print(sum(countBytes(path, [])))
        main(path)
    if n == 6:
        target = input()
        print(findFiles(target, path))
    if n == 7:
        print('End of the session')
        exit()


def dir_watch(path):
    """The function that determines the execution of the selected function"""
    sleep()
    for dirs, folders, files in os.walk(path):
        print('Folders: ', *folders)
        print('Files: ', *files)
        break
    sleep()
    main(path)


def moveUp(path):
    """A function that makes the current parent directory"""
    sleep()
    path = Path(path)
    path = path.parent.absolute()
    sleep()
    main(path)


def moveDown(path, fn):
    """A function that allows you to go down a branch in a directory"""
    sleep()
    fn = str(path) + fn
    if os.path.exists(fn):
        main(fn)
    else:
        print('No such folder')
        main(path)


def countFiles(path, files):
    """A function that counts the number of files in a directory"""
    if os.path.isfile(path):
        return files.append(path)
    for file_srch in os.listdir(path):
        file_srch = os.path.join(path, file_srch)
        if os.path.isfile(file_srch):
            files.append(file_srch)
        else:
            files = countFiles(file_srch, files)
    return files


def countBytes(path, bytes):
    """A function that calculates the weight of files in a directory"""
    if os.path.isfile(path):
        return os.path.getsize(path)
    for file_srch in os.listdir(path):
        file_srch = os.path.join(path, file_srch)
        if os.path.isfile(file_srch):
            bytes.append(os.path.getsize(file_srch))
        else:
            bytes = countBytes(file_srch, bytes)
    return bytes


def findFiles(target, path):
    """A function that generates a list of file paths"""
    for file_srch in os.listdir(path):
        file_srch = os.path.join(path, file_srch)
        if target in os.listdir(path):
            path = os.path.join(path, target)
            return path
        elif os.path.isfile(file_srch):
            return None
        else:
            path = os.path.join(path, file_srch)
            return findFiles(target, path)
    return 'No such file'


main(path_Main)
