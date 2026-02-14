###################################################
# File Name : BackupHistory.py
# Description : Maintain backup history
###################################################

import time

###################################################
def WriteHistory():

    try:

        fobj = open("History.txt", "a")

        Date = time.ctime()

        Data = Date + " | Files : 10 | Size : 5MB"

        fobj.write(Data + "\n")

        fobj.close()

    except Exception as E:

        print("Error :", E)

###################################################
def DisplayHistory():

    try:

        fobj = open("History.txt", "r")

        for Line in fobj:

            print(Line)

        fobj.close()

    except Exception as E:

        print("Error :", E)

###################################################
def main():

    print("1 : Add History")

    print("2 : Display History")

    Choice = int(input("Enter choice : "))

    if Choice == 1:

        WriteHistory()

    elif Choice == 2:

        DisplayHistory()

###################################################
if __name__ == "__main__":
    main()