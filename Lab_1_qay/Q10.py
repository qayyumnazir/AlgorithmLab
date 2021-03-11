def prime(users):
    if int(users)<=1:
        print(users," is not a prime number")
        return
    elif int(users)==2:
        print(users, " is a prime number")
        return
    elif int(users)%2==0:
        print(users, " is not a prime number")
        return
    for i in range(3,int(users),2):
        if int(users)%i==0:
            print(users, " is not a prime number")
            return

    print(users, " is a prime number")
    return



users=input("Please enter a number :- ")
prime(users)

