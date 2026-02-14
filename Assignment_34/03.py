###################################################
# File Name : RestoreBackup.py
# Description : Restore backup from zip file
###################################################

import zipfile
import sys

###################################################
def RestoreBackup(ZipFile, Destination):

    try:

        obj = zipfile.ZipFile(ZipFile, 'r')

        obj.extractall(Destination)

        print("Backup Restored Successfully")

    except Exception as E:

        print("Restore Failed :", E)

###################################################
def main():

    if len(sys.argv) != 3:

        print("Usage : Script.py ZipFile Destination")

        exit()

    ZipFile = sys.argv[1]

    Destination = sys.argv[2]

    RestoreBackup(ZipFile, Destination)

###################################################
if __name__ == "__main__":
    main()