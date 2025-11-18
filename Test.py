options = ["food", 'water', 'rope', 'torch', 'sack', 'wood', 'iron','steel','ginger','garlic','fish','stone','wool',]
cmd = input()
for i in options:
    if i in cmd:
        print(True,i)
    
