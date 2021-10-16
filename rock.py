import random
  
# Print multiline instruction
# performstring concatenation of string
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
  
while True:
    print("Enter choice \n 1. Rock \n 2. paper \n 3. scissor \n")
      
    # take the input from user
    choice = int(input("User turn: "))
  
    # OR is the short-circuit operator
    # if any one of the condition is true
    # then it return True value
      
    # looping until user enter invalid input
    while choice > 3 or choice < 1:
        choice = int(input("enter valid input: "))
          
  
    # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'
