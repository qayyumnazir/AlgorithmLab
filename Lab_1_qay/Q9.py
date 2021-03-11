import random

numb = [1,2,3,4,5,6,7,8,9]
numbe= random.choice(numb)

users= input("Guess a number from 1 to 9 :-  ")
if int(users)==int(numbe):
    print("You are correct!")
elif int(users)>=int(numbe):
    print("Your guess is too high the number is ", numbe)
elif int(users)<=int(numbe):
    print("Your guess is too low the number is ", numbe)

