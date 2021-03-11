def nodupli(a):
    b=[]
    for i in a:

        if b.count(i) < 1:
            b.append(i)
            print(i," is append")
    return b

a= [1,2,3,4,5,6,7,8,8,3,2,1,1,4,9]
b=nodupli(a)
print(b)