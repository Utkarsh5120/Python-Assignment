############################################################
# File Name : MemoryMonitor.py
# Description : Memory Monitoring
# Author : Marvellous Infosystems
############################################################

import psutil
import sys
import os

############################################################

def MemoryInfo():

    Data = []

    for proc in psutil.process_iter():

        try:

            Info = {}

            Info['Name'] = proc.name()

            Memory = proc.memory_info()

            Info['RSS'] = Memory.rss

            Info['VMS'] = Memory.vms

            Info['Percent'] = proc.memory_percent()

            Data.append(Info)

        except:

            pass

    return sorted(Data,key=lambda x:x['Percent'],reverse=True)

############################################################

def main():

    DirName = sys.argv[1]

    if not os.path.exists(DirName):
        os.mkdir(DirName)

    FileName = DirName+"/MemoryLog.txt"

    Data = MemoryInfo()

    File = open(FileName,"w")

    for Value in Data[:10]:

        File.write(str(Value)+"\n")

    File.close()

############################################################

if __name__ == "__main__":
    main()