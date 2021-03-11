def firstLast(a):
    b=[]
    b.append(list(a)[0])
    b.append(list(a)[len(list(a))-1])
    return b

a=[5,10,15,20,25]
b=firstLast(a)
print(b)


