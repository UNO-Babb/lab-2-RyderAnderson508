#FutureTime.py
#Name:Ryder Anderson
#Date:01/29/2025
#Assignment:Lab 1 Future time

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now() 
  currenthour = (now.hour - 6) % 12
  currentminute = now.minute
  print (currenthour, currentminute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours 
  hours = input("enter hours: ")
  hours = int(hours) #change from the test to hour
  minutes = input ("enter minutes: ")
  minutes = int(minutes) 
  futureminutes = (currentminute + minutes) 
  extrahours = (futureminutes // 60)
  futureminutes = futureminutes % 60
  futurehour = currenthour + hours + extrahours
  futurehour = futurehour % 12
  strhour = str(futurehour)
  strmin = str(futureminutes)
  if futureminutes < 10: 
    strmin = "0" + strmin #add a leading zero to one digit min

  print(futurehour ,":", futureminutes)

  
  #Ask user for minutes

  #Calculate the time after the user-supplied time has passed.

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"


if __name__ == '__main__':
  main()
