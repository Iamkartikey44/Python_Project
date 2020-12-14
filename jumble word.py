import random
def play():
    p1_name = input('Player1,Enter your name: ')
    p2_name = input('Player2,Enter your name: ')
    po1=0
    po2=0
    turn=0
    while(1):
        picked_word = choose()
        qn= jumble(picked_word)#create a question
        print(qn)
        if(turn%2==0):#player1 chance
            print(p1_name,'Your turn: ')
            ans = input('what is on my mind: ')
            if(ans==picked_word):
                po1+=1
                print('your score is : ',po1)
            else:
                print('Better luck next time: ',picked_word)
            c=int(input('Press 1 to continue and 0 to quit: '))
            if(c==0):
                thank(p1_name,p2_name,po1,po2)

                break

        else:
            print(p2_name,'Your turn: ')
            ans = input('What is on my mind: ')
            if(ans==picked_word):
                po2+=1
                print('your score is :',po2)
            else:
                print('Better luck next time: ',picked_word)
            c=int(input('Press 1 to continue and 0 to quit: '))
            if(c==0):
                thank(p1_name,p2_name,po1,po2)
                break
        turn+=1
def choose():
    word = ['red', 'cold', 'hot', 'geeks', 'rain','black', 'snow', 'hills', 'code','rainbow', 'computer', 'science', 'programming','mathematics', 'player', 'condition', 'reverse','water', 'board', 'geeks']
    pick=random.choice(word)
    return pick
def jumble(word):
    jumble="".join(random.sample(word,len(word)))
    return jumble
def thank(p1n,p2n,p1,p2):
    print(p1n,'Your score is: ',p1)
    print(p2n,'Your score is: ',p2)
    print('Thanks for playing: ')
    print('Have a nice day: ')
play()