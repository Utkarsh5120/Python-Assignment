###################################################
# File Name : LoggingSystem.py
# Description : Create Logs folder and store backup log
# Author : Marvellous Infosystems
###################################################

import os
import time

###################################################
def CreateLogFolder():
    try:
        if not os.path.exists("Logs"):
            os.mkdir("Logs")
    except Exception as E:
        print("Error creating Logs folder :", E)

###################################################
def WriteLog(FileName, Data):

    FilePath = os.path.join("Logs", FileName)

    try:
        fobj = open(FilePath, "a")

        fobj.write(Data + "\n")

        fobj.close()

    except Exception as E:
        print("Unable to write log :", E)

###################################################
def main():

    print("----- Marvellous Logging System -----")

    CreateLogFolder()

    StartTime = time.ctime()

    WriteLog("BackupLog.txt", "Backup Started at : " + StartTime)

    WriteLog("BackupLog.txt", "Files copied successfully")

    WriteLog("BackupLog.txt", "Zip file created : Backup.zip")

    WriteLog("BackupLog.txt", "Backup completed")

###################################################
if __name__ == "__main__":
    main()