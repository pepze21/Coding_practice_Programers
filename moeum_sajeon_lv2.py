def make_words(s, length, dictionary, ALPHABETS):
    if length < 0:
        return
    if s != '':
        dictionary.append(s)
    for char in ALPHABETS:
        make_words(s + char, length - 1, dictionary, ALPHABETS)

def solution(word):
    ALPHABETS = 'AEIOU'
    dictionary = []
    make_words('', 5, dictionary, ALPHABETS)
    dictionary.sort()
    return dictionary.index(word) + 1