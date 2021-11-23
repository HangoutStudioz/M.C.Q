from Question import Question
########################  Question 1 #############################

def border(sign , Number):
    count = 0
    count = Number
    while count > 0:
        print(sign , end="")
        count -= count == count

def Win_Lost():
    if  Answer_Input == Question1.Answer:
        border("=" , 20)
        print("\nYour Answer Is Correct")
        border("=" , 20)
    elif Answer_Input == "delhi":
        border("=" , 20)
        print("\nYour Answer Is Correct")
        border("=" , 20)
    elif Answer_Input == "DELHI":
        border("=" , 20)
        print("\nYour Answer Is Correct")
        border("=" , 20)
    else:
        border("=" , 20)
        print("\nYou Answer Is Wrong")
        border("=" , 20)
    return Win_Lost  

Question1 = Question("\nWhat Is The Capital Of India","Delhi")
border("=" , 20)
print(Question1.question)
border("=" , 20)
print("\nYou Can Only Type Words Not Numbers")
border("=" , 20)
Answer_Input = input("\nAnswer:")
Win_Lost()
########################  Question 2 #############################
def Win_Lost():
    if  Answer_Input == Question2.Answer:
        border("=" , 20)
        print("\nYour Answer Is Correct")
        border("=" , 20)
    elif Answer_Input == "peacock":
        border("=" , 20)
        print("\nYour Answer Is Correct")
        border("=" , 20)
    elif Answer_Input == "PEACOCK":
        border("=" , 20)
        print("\nYour Answer Is Correct")
        border("=" , 20)
    else:
        border("=" , 20)
        print("\nYou Answer Is Wrong")
        border("=" , 20)
    return Win_Lost  

Question2 = Question("\nWhat Is The National Bird Of India","Peacock")
border("=" , 20)
print(Question2.question)
border("=" , 20)
print("\nYou Can Only Type Words Not Numbers")
border("=" , 20)
Answer_Input = input("\nAnswer:")
Win_Lost()