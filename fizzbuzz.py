def fizzbuzz(n):
    for i in range(1,n+1):
        if(i%3==0 and i%5!=0):
            print(i,":",'fizz')
        elif(i%5==0 and i%3!=0):
            print(i,':','buzz')
        else:
            if(i%3==0 and i%5==0):
                print(i,':','fizzbuzz')
            else:
                print(str(i))
fizzbuzz(51)
