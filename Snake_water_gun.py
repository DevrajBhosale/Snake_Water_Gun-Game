import random 
options = [0,1,2]
arr2d = [["D","W","L"],["L","D","W"],["W","L","D"]]

print("Welcome to Snake, Water & Gun Game, Let Start the Game.\n")
while True:
    character = ["Snake","Water","Gun"]
    player = input("To Choose Snake(Press 0), Water(Press 1) & Gun(Press 2) or Exit(Press 3):")
    try:
        if(int(player) == 3 or (int(player) != 0 and int(player) != 1 and int(player) != 2)):
            break
    except:
        print("Please Enter Valid Input")
        continue

    print(f"You choose: {character[int(player)]}")
    print("Now its Computer player Turn.")
    comp_player = random.choice(options)
    print(f"Computer choose: {character[comp_player]}")

    if(arr2d[0][0]== arr2d[int(player)][comp_player] or arr2d[1][1]== arr2d[int(player)][comp_player] or arr2d[2][2]== arr2d[int(player)][comp_player]):
        print("Match has been Draw")
    elif(arr2d[0][1]== arr2d[int(player)][comp_player] or arr2d[1][2]== arr2d[int(player)][comp_player] or arr2d[2][0]== arr2d[int(player)][comp_player]):
        print("Congrats You Win...")
    elif(arr2d[0][2]== arr2d[int(player)][comp_player] or arr2d[1][0]== arr2d[int(player)][comp_player] or arr2d[2][1]== arr2d[int(player)][comp_player]):
        print("Sorry you Loose...")

    tryagain = input("Do you want to try again(Y or Press Enter/N): \n")
    if(tryagain.lower() == 'n'):
        break
