import random
movies = ['Don','Robot','Race','Driysham','Dangal','Run','Friday','Goal','Goalmal']


def play():
    p1_name = input('Enter the your name1: ')
    p2_name = input('Enter the your name2: ')
    pp1=0
    pp2=0
    turn=0
    willing =True
    while(willing):
        if(turn%2==0):
            print(p1_name,'Your True')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said =True
            while not_said:
                letter = input()
                if(is_present(letter,picked_movie)):
                    modified_qn = unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d= int(input("Press 1 to guess the movie or 2 to unlock another letter:"))
                    if(d==1):
                        ans = input('Your_Answer: ')
                        if(ans==picked_movie):
                            pp1+=1
                            print('correct')
                            not_said=False
                            print(p1_name,'Your Score :',pp1)
                        else:
                           print('Wrong Answer Try Again:')

                else:

                    print(letter,'NOT FOUND')
            c=int(input('Press 1 to continue or 0 to quit: '))
            if(c==0):
                print(p1_name,'Your Score:',pp1)
                print(p2_name,'Your Score:',pp2)
                print('Thank you for playing')
                print('Have a Nice Day')
                willing=False
        else:
            print(p2_name, 'Your Turn: ')
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            print(qn)
            modified_qn = qn
            not_said = True
            while not_said:
                letter = input()
                if (is_present(letter, picked_movie)):
                    modified_qn = unlock(modified_qn, picked_movie,letter)
                    print(modified_qn)
                    d = int(input("Press 1 to guess the movie or 2 to unlock another letter"))
                    if (d == 1):
                        ans = input('Your_Answer: ')
                        if (ans == picked_movie):
                            pp2 += 1
                            print('correct')
                            not_said = False
                            print(p2_name, 'Your Score :', pp2)
                        else:
                            print('Wrong Answer Try Again:')

                else:

                    print(letter, ' NOT FOUND ')
            c = int(input('Press 1 to continue or 0 to quit: '))
            if (c == 0):
                print(p1_name, 'Your Score:', pp1)
                print(p2_name, 'Your Score:', pp2)
                print('Thank you for playing')
                print('Have a Nice Day')
                willing = False
            turn+=1
def create_question(movie):
    n=len(movie)
    letter = list(movie)
    temp=[]
    for i in range(n):
        if(letter[i]==''):
            temp.append(' ')
        else:
            temp.append('*')
    qn="".join(str(x) for x in temp)
    return qn
def is_present(letter,movie):
    c=movie.count(letter)
    if(c==0):
        return False
    else:
        return True
def unlock(qn,movie,letter):
    ref = list(movie)
    qn_list = list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if(ref[i]==' ' or ref[i]==letter):
            temp.append(ref[i])
        else:
            if(qn_list[i]=='*'):
                temp.append('*')
            else:
                temp.append(ref[i])
    qn1="".join(str(x) for x in temp)
    return qn1
play()
