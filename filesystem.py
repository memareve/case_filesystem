import os
from pathlib import Path
import time


path_Main = 'F:/case'


def sleep():
    print()
    time.sleep(1)


def main(path):
    print()
    print(path)
    print(('1. Browse catalog\n2. Up the branch\n3. Down the branch\n4. Number of files in the directory\n'
           '5. Directory size in bytes\n6. File search\n7. Exit\n'))
    time.sleep(1)
    acceptCommand(path)


def acceptCommand(path):
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
        print(len(countFiles(path,[])))
        main(path)
    if n == 5:
        sleep()
        print(sum(countBytes(path, [])))
        main(path)
    """
    if n == 6:"""
    if n == 7:
        print('End of the session')
        exit()


def dir_watch(path):
    sleep()
    for dirs, folders, files in os.walk(path):
        print('Folders: ', *folders)
        print('Files: ', *files)
        break
    sleep()
    main(path)


def moveUp(path):
    sleep()
    path = Path(path)
    path = path.parent.absolute()
    sleep()
    main(path)


def moveDown(path, fn):
    sleep()
    fn = str(path) + fn
    if os.path.exists(fn):
        main(fn)
    else:
        print('No such folder')
        main(path)


def countFiles(path, files):
    if os.path.isfile(path):
        return files.append(path)
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isfile(item):
            files.append(item)
        else:
            files = countFiles(item, files)
    return files


def countBytes(path,bytes):
    if os.path.isfile(path):
        return os.path.getsize(path)
    for item in os.listdir(path):
        item = os.path.join(path, item)
        if os.path.isfile(item):
            bytes.append(os.path.getsize(item))
        else:
            bytes = countBytes(item, bytes)
    return bytes


main(path_Main)
