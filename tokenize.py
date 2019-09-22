def tokenisasi(kalimat, delimiter = [" ", ".",",",'?','!','@','#','%','^','*','(',')','<','>','/','\\',],  space = True):
    if space == True:
        delimiter = list(set([" "]+delimiter))
    else:
        delimiter = list(set(delimiter))
    token = list()
    temp = list()
    for i in kalimat:
        if i not in delimiter:
            temp.append(i)
        else:
            if len(temp)>1:
                token.append("".join(temp))
            temp = list()
    if len(temp)>1:
        token.append("".join(temp))
    return token

print(tokenisasi("*889#"))