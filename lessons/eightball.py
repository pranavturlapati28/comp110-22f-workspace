from random import randint
print("hello")
question: str = input("What is your yes/no question?")
response: int = randint(0,3)

if response == 0:
    print("Yess, def")
elif response == 1:
    print("Ask again later")
elif response == 2:
    print("Yes ofc")
else: 
    print("My sources say no")


