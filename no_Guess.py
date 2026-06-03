import random 

x = random.randint(1,100) 

while True:
    
    try:
        y=int(input("guess the number btw 1 to 100\t"))
        if not 0<y<101:
            print("invalid input ")
        elif x == y :
            print("correct ")
            break;
        elif x<y :
            print("too high ")
        elif x> y :
            print("too low ")
    except  ValueError :
        print("enter a valid input")

    


    