def reverseWord(user):
    sentence=""
    word=""
    for i in user:
        if str(i) == " ":
            sentence=word+" "+sentence
            word=""
        else:
            word+=str(i)
    sentence = word + " " + sentence
    print(sentence)




user = input("Please enter your a long sentence :- ")
reverseWord(user)


