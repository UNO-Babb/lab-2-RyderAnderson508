#Magic8Ball.py
#Name:Ryder Anderson
#Date:01/29/2025
#Assignment:Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers = ["Do not count on it." , "ask again later." , "Better not to tell you now." , "Concentrate and ask again." , "Cannot predict now." , "Most likely." , "Very doubtful." , "Yes." , "Very doubtful." , "It is certain." , "Reply hazy, try again."]
  #Answer question randomly with one of the options from your earlier list.

num = random.random()
num = num * 11
num = int(num) 
num = num % 12

question = input("ask me a question: ")
print(answers[num])
if __name__ == '__main__':
  main()
