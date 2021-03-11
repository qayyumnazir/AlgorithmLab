numbe=input("Please enter a number ")
a=[]
numb=int(numbe)
while True:
    temp=numb/2
    if(numb%2==0):
        a.append(temp)
        numb=temp
    else:
        break;

print("The divisor for ",numbe, "is ",a)

