def fibonacci(amount):
    if int(amount)==0:
        return 0
    elif int(amount)==1:
        return 1
    else:
        return fibonacci(int(amount-1))+fibonacci(int(amount-2))

start=input("Please enter amount for fibonacci   ")
k=[]
for i in range(1,int(start)+1):
    k.append(fibonacci(i))

print(k)





