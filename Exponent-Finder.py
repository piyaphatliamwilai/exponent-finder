# This project is open-sourced and you can do whatever you want with it! Feel free to fork or anything to this project.
# This project is written in Python 3 and created by piyaphatliamwilai
# If you are going to use this or use some of our codes, credit would be appreciated.

import time
from playsound import playsound

print("Thanks for using my exponent finder! Feel free to report bug at github.com/piyaphatliamwilai/exponent-finder")
print("I made this just for my math homework cause I'm lazy.")

baseNumber = float(input("Please type the base number : "))

exponentNumber = float(input("Please type the exponent : "))

output = baseNumber // exponentNumber;
 
ans = 1

while (output > 0):
  output2 = output // exponentNumber
  print(output)

  ans = ans + 1
  
  output = output2 // exponentNumber

  ans = ans + 1
  
  print(output2)

if output == 0:
    playsound("answerFound.mp3")

    ans = ans - 2
    
    print(ans)

while 3 > 2:
    time.sleep(1)
