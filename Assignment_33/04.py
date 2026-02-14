############################################################
# File Name : PlatformSurveillance.py
# Description : Email Reporting System
# Author : Marvellous Infosystems
############################################################

import time
import sys
import os

############################################################

def main():

    if(len(sys.argv)!=4):

        print("Invalid arguments")

        exit()

    DirName=sys.argv[1]

    Receiver=sys.argv[2]

    Interval=int(sys.argv[3])

    if not os.path.exists(DirName):

        os.mkdir(DirName)

    while(True):

        FileName=DirName+"/Log.txt"

        File=open(FileName,"w")

        File.write("System Monitoring Log")

        File.close()

        print("Log Created")

        time.sleep(Interval*60)

############################################################

if __name__=="__main__":

    main()