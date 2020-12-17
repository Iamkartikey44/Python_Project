import random
doors = [0]*3
g_door = [0]*2

swap=0
donot_swap = 0
x = random.randint(0,2)
j=0
while(j<=10):
    doors[x] = 'BMW'
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]='Goat'
            g_door.append(i)
    choice = int(input('Enter your choice: '))
    door_open = random.choice(g_door)
    while(door_open==choice):
        door_open = random.choice(g_door)
    ch = input('Do you want to Swap Y/N :')
    if(ch=='Y'):
        if(doors[choice]=='Goat'):
            print('Player Wins: ')
            swap+=1
        else:
            print('Player LOst: ')
    else:
        if(doors[choice]=='Goat'):
            print('Player Lost')
        else:
            print('Player Wins')
            donot_swap+=1
    j+=1
print(swap)
print(donot_swap)