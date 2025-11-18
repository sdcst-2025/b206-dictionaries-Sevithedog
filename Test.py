

    
def get(cmd,inventory,options):
    x = cmd.split()
    for i in x:
        if i in options: 
            label = i 
    for i in x: 
        try:
            y = int(i)
        except:
            y = 1
        if y > 1:
            n=y 
            break
    inventory[label] = n
    print(inventory)



options = ["food", 'water', 'rope', 'torch', 'sack', 'wood', 'iron','steel','ginger','garlic','fish','stone','wool',]
inventory = {}
quit = False
while quit == False:
    cmd = input("Cmd: ")
    if cmd == "quit":
        break
    get(cmd,inventory,options)