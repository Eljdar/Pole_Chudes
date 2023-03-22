def maskirovka_slova(text):
    secret_word = ""
    for bukva in text:
        if bukva != " ":
            secret_word += "*"
        else:
            secret_word += " "
    return secret_word


def naiti_raspolozhenie_bukvi(text, burts):
    start = 0
    indexi_bukvi = []
    while True:
        sub_text = text[start:]
        if sub_text.find(burts) == -1:
            break
        index = start + sub_text.find(burts)
        indexi_bukvi.append(index)
        start = index + 1
    return indexi_bukvi


def raskritie_bukvi(bukva, indexi, predlozhenije):
    word = list(predlozhenije)
    for index in indexi:
        word[index] = bukva
    return "".join(word)

#
# def prodolzhai_do_pobedi(word):
#     otkrito = ''.join(word)
#
#     return otkrito


text = input("Введите слово: ")
sekret = maskirovka_slova(text)
print(sekret)
while True:
    burts = input("Введите букву: ")
    raspolozhenije = naiti_raspolozhenie_bukvi(text, burts)
    print(raspolozhenije)
    praviljno = raskritie_bukvi(burts, raspolozhenije, sekret)
    print(praviljno)
