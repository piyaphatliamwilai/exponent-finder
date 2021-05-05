# This project is open-sourced and you can do whatever you want with it! Feel free to fork or anything to this project.
# This project is written in Python 3 and created by piyaphatliamwilai
# If you are going to use this or use some of my codes, credit would be appreciated.

from plyer import notification
import time
from playsound import playsound

print("Thanks for using my exponent finder! Feel free to report bug at github.com/piyaphatliamwilai/exponent-finder")
print("I made this just for my math homework cause I'm lazy.")

baseNumber = float(input("Please type the base number : "))
exponentNumber = float(input("Please type the exponent : "))

copyBaseNumber = baseNumber

ans = -1

output = baseNumber

while (output > 0):
  
  print(output)
  output2 = output // exponentNumber
  
  ans = ans + 1

  output = output2
  
if output == 0:
  playsound("answerFound.mp3")

  print("answer found.")

  notification.notify(
    title= 'Exponent Finder v0.0.3 - Notifications',
    message='Answer Founded!')
  print("checking the answer ....")

  print(ans)

  answ1 = exponentNumber ** ans;
  print(answ1)

  if answ1 == baseNumber:
    print("Answer Corrected!")

  elif answ1 != baseNumber:
    print("Answer incorrected, try checking exponent number or adding the answer by 1 or subtracting it by 1 and using calculator to power it.")
while 3 > 2:
    time.sleep(1)
