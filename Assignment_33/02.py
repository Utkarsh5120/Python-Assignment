############################################################
# File Name : OpenFilesMonitor.py
# Description : Display Open files count
# Author : Marvellous Infosystems
############################################################

import psutil
import sys
import os
from datetime import datetime

############################################################

def OpenFilesInfo():

    Data = []

    for proc in psutil.process_iter():

        try:

            Info = {}

            Info['Name'] = proc.name()

            Info['PID'] = proc.pid

            try:
                Info['Files'] = len(proc.open_files())
            except:
                Info['Files'] = "Access Denied"

            Info['Time'] = datetime.now()

            Data.append(Info)

        except:

            pass

    return Data

############################################################

def main():

    if(len(sys.argv)!=2):
        exit()

    DirName = sys.argv[1]

    if not os.path.exists(DirName):
        os.mkdir(DirName)

    FileName = DirName+"/OpenFilesLog.txt"

    Data = OpenFilesInfo()

    File = open(FileName,"w")

    for Value in Data:

        File.write(str(Value)+"\n")

    File.close()

############################################################

if __name__ == "__main__":
    main()