#Question Answer 
import random
answer=["Ask again later", "The answer is unclear", "yes", "no","Maybe","Ask another question"]

name = input("whats your name: ")

age=input("How old are you: ")
question=input("Do you feel lucky:(Yes or No)")
if question=="Yes":
    print("you shouldnt!!")
else:
    print("you are lucky!!")

ask=input("Ask a question:")
print(" ")
print("The answer to your question is : ", random.choice(answer))
