ayat = input("Please enter your sentences  ")
def terbaliker(ayat):
    str=""
    for x in ayat:
        str=x+str
    return str
terbalik=terbaliker(ayat)
if (str(ayat)==str(terbalik)):
    print("it is palindrome")
else:
    print("it is not palindrome")




