#MathHomework.py
#Tere Somoza

#This project will print the result of the user's entered equation and print the equation as well

problem=input("Enter a math problem or enter q to quit\n")

while (problem!="q"):
    print("The answer to" ,problem, "is: ", eval(problem))
    problem=input("Enter another math problem, or 'q' to quit\n")
