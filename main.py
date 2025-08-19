
def check_consecutive_number(arr):
    i = 1
    
    while i < len(arr):
        if (arr[i]-arr[i-1]) !=1:
            return False
        i = i + 1
    
    return True

def loses():
    print("You lose. Try again!!")
    exit(0)
    print()


def multipleNumb(num):
    near = 0
    if num >= 4:
        near = num +  (4 - (num % 4))
        
    else:
        near = 4
        
    return near
        
        
def check_user_input(arr, chance):
    last = arr[-1]
    if last == 20:
        print("User Loses")
        loses()

    print("Now is your turn.")
    user_input = input("How many number you want to enter?: ")
    
    if  not user_input.isdigit():
        print("Sorry you need to enter only digits")
        exit()

    user_input = int(user_input)
    if user_input > 3 or user_input <= 0 :
        print("Sorry, you enter an invalid number")
        loses()
            
    i = 1
    print("Enter your values.")
    
    while i <= user_input:
        b = int(input("> "))
        arr.append(b)
        i += 1

    last = arr[-1]
    if check_consecutive_number(arr):
        if last == 21:
            print("Sorry. The computer wins.")
            loses()
            
    else:
        del arr[-user_input:]
        print("You need to enter consecutive values.")
        chance -= 1
        message = "chances" if chance > 1 else "chance" 
        print(f"You have {chance} {message} left")
    
        if chance == 0:
            print("User Loses. You need to enter consecutive values😰")
            loses()
    return chance


def computer_play(num):
    near = multipleNumb(num)
    computer_turn = near - num
    if computer_turn == 4:
        computer_turn = 3
        
    else:
        computer_turn = computer_turn
    
    return computer_turn

def game_logic():
    arr = []
    last = 0
    
    while True:
        print("Enter F if you want to play first.")
        print("Enter S if you want to play second.")
        
        answer = input("> ").lower()
        print("Choose a level (hard/easy)")
        level = input("> ").lower()
        
        if level == "easy":
            chance = 3
        
        elif level == "hard":
            chance = 2
        else:
            print("Wrong Choice")
            game_logic()
            
        if answer == "F".lower():
            while True:
                if last == 21:
                    print("User loses")
                    loses()
                    
                user_input = int(input("How many number you want to enter?: "))
            
                if user_input > 3 or user_input <= 0:
                    print("Sorry, you enter an invalid number")
                    chance -= 1
                    
                    if chance == 0:
                        loses()
                        
                    user_input = int(input("How many number you want to enter?: "))
                    if (user_input > 3 or user_input <= 0) and chance==0:
                        loses()
                
                computer_turn = 4 - user_input
                
                i, j = 1, 1
                print("Enter your values.")
                while i <= user_input:
                    a = int(input("> "))
                    arr.append(a)
                    i += 1
                
                last = arr[-1]
                
                if check_consecutive_number(arr):
                    if last == 21:
                        print("User loses.😰😰")
                        loses()
                    
                    while j <= computer_turn:
                        arr.append(last + j)
                        j += 1
                    
                    last = arr[-1]
                    print("The array after the computer's choice is", arr)
                    if last == 20:
                        print("User loses.")
                        loses()
                        
                else:
                    del arr[-user_input:]
                    print("You need to enter consecutive values.")
                    chance -= 1
                    message = "chances" if chance > 1 else "chance"
                    print(f"You have {chance} {message} left")
                
                    if chance == 0:
                        print("User Loses. You need to enter consecutive values😰")
                        loses()
                    
                    
        elif answer == "S".lower():
            computer_turn = 1
            last = 0
            
            while last < 20:
                j = 1
                
                while j <= computer_turn:
                    arr.append(last + j)
                    j += 1
                
                print("The array after the computer choice is", arr)
                chance = check_user_input(arr, chance)
                last = arr[-1]
                computer_turn = computer_play(last)
                    
            else:
                print("\n\nCONGRATULATIONS YOU WIN.👏🎉")
                exit(0)
            
        else:
            print("Sorry. Invalid choice")
            loses()


def play_game():
    game = True
    
    while game == True:
        print()
        print("Would you like to play the 21 game? (Yes/No)")
        answer = input("> ").lower()
        
        if answer == "Yes".lower():
            game_logic()
        
        elif answer == "No".lower():
            print("Would you like to end the game? (Yes/no)")
            end_game = input("> ").lower()
            
            if end_game == "Yes".lower():
                print("You have been successfully end the game.")
                exit(0)
                
            else:
                print("Continuing...............")
                game_logic()
        
        else:
            print("Invalid choice. End of the game!")
            exit(0)

play_game()