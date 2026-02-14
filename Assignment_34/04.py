###################################################
# File Name : ExcludeFiles.py
# Description : Ignore specific file extensions
###################################################

import os

###################################################
def ScanDirectory(Path):

    Ignore = (".tmp", ".log", ".exe")

    try:

        for File in os.listdir(Path):

            if File.endswith(Ignore):

                continue

            print(File)

    except Exception as E:

        print("Error :", E)

###################################################
def main():

    Path = input("Enter directory path : ")

    ScanDirectory(Path)

###################################################
if __name__ == "__main__":
    main()