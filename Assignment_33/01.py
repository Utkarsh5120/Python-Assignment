############################################################
# File Name : ThreadMonitor.py
# Description : Display Thread information of processes
# Author : Marvellous Infosystems
############################################################

import psutil
import sys
import os
from datetime import datetime

############################################################

def CreateLogDirectory(DirName):

    if not os.path.exists(DirName):
        os.mkdir(DirName)

############################################################

def GetLogFile(DirName):

    TimeStamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return os.path.join(DirName,"ThreadLog%s.log" % TimeStamp)

############################################################

def ThreadInformation():

    Data = []

    for proc in psutil.process_iter():

        try:

            Info = {}

            Info['Name'] = proc.name()

            Info['PID'] = proc.pid

            Info['Threads'] = proc.num_threads()

            Info['Time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            Data.append(Info)

        except:

            pass

    return Data

############################################################

def WriteLog(FileName,Data):

    File = open(FileName,"w")

    for Value in Data:

        File.write("Process Name : %s\n" % Value['Name'])

        File.write("PID : %s\n" % Value['PID'])

        File.write("Threads : %s\n" % Value['Threads'])

        File.write("Time : %s\n" % Value['Time'])

        File.write("\n----------------------\n")

    File.close()

############################################################

def main():

    if(len(sys.argv) != 2):
        print("Invalid Argument")
        exit()

    DirName = sys.argv[1]

    CreateLogDirectory(DirName)

    FileName = GetLogFile(DirName)

    Data = ThreadInformation()

    WriteLog(FileName,Data)

############################################################

if __name__ == "__main__":
    main()