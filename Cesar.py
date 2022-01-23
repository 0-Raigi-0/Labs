from collections import Counter
alphabet = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя"
print("Введите числовой ключ: ")
key = int(input())
print("Введите ключевое слово: ")
key_w = input()
file = open('Text.txt', 'r', encoding='utf-8')
ent = file.read()
file.close()
ent = ent.lower()
len_a = len(alphabet)
def make_new_alphabet(key, l_alphabet, key_w):
    new_alphabet = "" + l_alphabet
    l_alphabet = list(l_alphabet)
    for i in range(len(key_w)):
        l_alphabet[i + key] = key_w[i]
        new_alphabet = new_alphabet.replace(key_w[i], '')
    for i in range(len(l_alphabet)-len(key_w)):
        l_alphabet[(i+key+len(key_w))%len(l_alphabet)]  = new_alphabet[0]
        new_alphabet = new_alphabet.replace(new_alphabet[0],'')
    return l_alphabet
def encrypter(l_ent):
    an_alphabet = list("абвгдеёжзийклмнопрстуфхцчшщьыъэюя")
    n_ent = "" + l_ent
    func = make_new_alphabet(key, alphabet, key_w)
    n_ent = list(n_ent)
    for ch in range (len(n_ent)):
        if n_ent[ch] in an_alphabet:
            n_ent[ch] = func[an_alphabet.index(n_ent[ch])]
    n_ent = "".join(n_ent)
    return n_ent
def decrypter():
    m_often = 15
    alph = list("абвгдеёжзийклмнопрстуфхцчшщьыъэюя")
    n_alph = list("абвгдеёжзийклмнопрстуфхцчшщьыъэюя")
    enc = encrypter(ent)
    cnt = Counter(enc.replace(' ', ''))
    cnt_latters = []
    for i in range(len(cnt)):
        cnt_latters.append(cnt.most_common(len(cnt))[i][0])
    first = alph.index(cnt_latters[0])
    if first <= m_often:
        for i in range (m_often - first):
            alph = alph[1:] + alph[:1]
    else:
        for i in range (first - m_often):
            alph = alph[-1:] + alph[:-1]
    enc = list(enc)
    for ch in range (len(enc)):
        if enc[ch] in n_alph:
            enc[ch] = alph[n_alph.index(enc[ch])]
    enc = "".join(enc)
    return enc
print(decrypter())






