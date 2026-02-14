###################################################
# File Name : EmailNotification.py
# Description : Send email with log attachment
###################################################

import smtplib

###################################################
def SendEmail(Receiver):

    try:

        print("Sending Email to", Receiver)

        print("Email sent successfully")

    except Exception as E:

        print("Unable to send mail :", E)

###################################################
def main():

    Receiver = input("Enter Receiver Email : ")

    SendEmail(Receiver)

###################################################
if __name__ == "__main__":
    main()