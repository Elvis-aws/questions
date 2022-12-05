import glob


def listAllFilesInDirectory():
    for files in glob.glob("*.py"):
        print(files)

listAllFilesInDirectory()