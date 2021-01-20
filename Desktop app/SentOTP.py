import re
import smtplib
import math, random

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'           #To check email is valid or not...

# function to generate OTP
def generateOTP():
   # Declare a string variable
   # which stores all string
   string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
   OTP = ""
   length = len(string)
   for i in range(6):
      OTP += string[math.floor(random.random() * length)]

   return OTP

def check(email):
   if (re.search(regex, email)):
      return True
   else:
      return False

def sendOTP(receiverEmail):

   if check(receiverEmail) == True:
      return 0
   else:
      gmail_user = 'wajidmughal370@gmail.com'
      gmail_password = '2ba43c43'
      message = generateOTP()

      try:
         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
         server.ehlo()
         server.login(gmail_user, gmail_password)

         server.sendmail(gmail_user, receiverEmail, message)
         server.close()

         return message
      except:
         print
         'Something went wrong...'
         return 1

