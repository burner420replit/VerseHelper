def BuyXP(poklist, xp):
    for i in range(len(poklist)):
        print(f"!buy xp {poklist[i]} {xp}")
        print(str(i+1)+"/"+str(len(poklist)), end="")
        input()

def Plus45(poklist):
    for i in range(len(poklist)):
        print(f"!buy xp {poklist[i]} 17926")
        print(str(i+1)+"/"+str(len(poklist)), end="")
        input()

def Plus90(poklist):
    for i in range(len(poklist)):
        print(f"!buy xp {poklist[i]} 9675711")
        print(str(i+1)+"/"+str(len(poklist)), end="")
        input()

def Nick(poklist, nick):
    for i in range(len(poklist)):
        print(f"!nick {poklist[i]} {nick}")
        print(str(i+1)+"/"+str(len(poklist)), end="")
        input()

def Mutate(poklist, mutmon):
    poklist.reverse()
    for i in range(len(poklist)):
        print(f"!mutate {mutmon} {poklist[i]}")
        print(str(i+1)+"/"+str(len(poklist)), end="")
        input()

def LevelBlocker(poklist):
    for i in range(len(poklist)):
        print(f"!buy levelblocker {poklist[i]}")
        print(str(1+i)+"/"+str(len(poklist)), end="")
        input()

def Everstone(poklist):
    for i in range(len(poklist)):
        print(f"!buy everstone {poklist[i]}")
        print(str(1+i)+"/"+str(len(poklist)), end="")
        input()

def Evolve(poklist, evo_amount):
    for i in range(len(poklist)):
        for j in range(evo_amount):
            print(f"!buy xp {poklist[i]} 5")
            print(str(1+i)+"/"+str(len(poklist))+f' (Evo {j+1}/{evo_amount})', end="")
            input()
        
def EOTW(poklist):
    for i in range(len(poklist)):
        print("We are buying 5xp twice to ensure the pokemon evolves if its a first stage mon")
        print(f"!buy xp {poklist[i]} 5")
        print(f"!buy xp {poklist[i]} 5")
        print(f"!buy xp {poklist[i]} 17926")
        print(f"!buy levelblocker {poklist[i]}")
        print(str(1+i)+"/"+str(len(poklist)), end="")
        input()
        

def TrySetMode():
    mode = str(input("Select a mode: buyxp, +45, +90, nick, mutate, levelblocker, everstone, eotw - "))
    if mode.lower() == "buyxp":
        print("\nMode is set to buyxp, copy the command, paste it in discord, then press enter here for a new command.\n")
        print("to find the desired amount of xp use !!xp XpToLevelUp AmountOfevels")
        xp = int(input("What is the desired amount of xp? - "))
        BuyXP(poklist,xp)
        check_poklist()
    
    elif mode.lower() == "+45":
        print("\nMode is set to +45, copy the command, paste it in discord, then press enter here for a new command.\n")
        Plus45(poklist)
        check_poklist()
        
    elif mode.lower() == "+90":
        print("\nMode is set to +90, copy the command, paste it in discord, then press enter here for a new command.\n")
        Plus90(poklist)
        check_poklist()
    
    elif mode.lower() == "nick":
        print("\nMode is set to nick, copy the command, paste it in discord, then press enter here for a new command.\n")
        nick = str(input("What do you want to nickname your pokemon? - "))
        Nick(poklist, nick)
        check_poklist()
        
    elif mode.lower() == "mutate":
        print("\nMode is set to mutate, copy the command, paste it in discord, then press enter here for a new command.\n")
        mutmon = str(input("What's the nickname of the mon you want to mutate? - "))
        Mutate(poklist, mutmon)
        check_poklist()
        
    elif mode.lower() == "levelblocker":
        print("\nMode is set to LevelBlocker, copy the command, paste it in discord, then press enter here for a new command.\n")
        LevelBlocker(poklist)
        check_poklist()
        
    elif mode.lower() == "everstone":
        print("\nMode is set to everstone, copy the command, paste it in discord, then press enter here for a new command.\n")
        Everstone(poklist)
        check_poklist()

    elif mode.lower() == "eotw":
        print("\nMode is set to eotw, copy the command, paste it in discord, then press enter here for a new command.\n")
        EOTW(poklist)
        check_poklist()

    elif mode.lower() == "evolve":
        print("\nMode is set to evolve, copy the command, paste it in discord, then press enter here for a new command.\n")
        try: 
            evo_amount = int(input("How many times do you want to evolve your pokemon? - "))
        except ValueError:
            print("Value was not a number!")
            TrySetMode()
        if evo_amount < 1 or evo_amount > 2:
            print("Evo amount has to be 1 or 2!")
            TrySetMode()
        Evolve(poklist, evo_amount)
        check_poklist()

    else:
        print(f"Mode '{mode}' does not exist, try again!'")
        TrySetMode()

print("""
--------------------------------------------------------------------------\n
DISCLAIMER: THIS PROGRAM IS MEANT TO HELP VERSE PLAYERS BY GIVING THEM COMMANDS THEY THEMSELVES CAN COPY PASTE. THIS PROGRAM WAS NOT MADE AS A MACRO.\n
--------------------------------------------------------------------------
""")
##print("To get the correct row of pok numbers from a list, use the command !!getnums -list <list>")
##pokstring = input("Enter your row of pok numbers here (from your buy xp list, nick list or sac list): - ")
##poklist = pokstring.split(" ")

def check_poklist():
    try:
        print("To get the correct row of pok numbers from a list, use the command !!getnums -list <list>")
        pokstring = input("Enter your row of pok numbers here (from your buy xp list, nick list, or sac list): - ")
        global poklist
        poklist = pokstring.split(" ")
        
        # Check if each element in poklist is a number
        for num in poklist:
            if not num.isdigit():
                raise ValueError("Please make sure the input are numbers and it doesn't end on a spacebar")
        
        TrySetMode()
    except ValueError as err:
        print("\n" + str(err) + "\n")
        check_poklist()

while True:
	check_poklist()

