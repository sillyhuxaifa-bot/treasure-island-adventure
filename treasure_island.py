print("Welcome to treasure island.")
print("Your mission is to find the treasure")

choice1 = input('You\'re at a cross road. Where do you want to go? Type "right" or "left"').lower()

if choice1 == "right": 
  
  choice2 = input('You\'ve come to a lake. Type "wait" to wait for a boat. Type "swim" to swim across ').lower()

  if choice2 == "wait":

    choice3 = input('You have arrived at a castle. Choose wisely "yellow", "blue" or "red" ').lower()

    if choice3 == "yellow":
      print("You won!")
    elif choice3 == "blue":
      print("You entered beast room. Game over")
    elif choice3 == "red":
      print("Burned by fire. Game over")
    else: 
      print("You typed wrong thing. Game over")
    
  else:
    print("Game over")
  
else:
  print("Game over")

  
 
