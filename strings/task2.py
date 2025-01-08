"""
write a program that accepts a letter
as an input and converts each word to 
pig latin. one one version, to convert
a word to pig lating, you remove the
first letter and place that letter
at the end of the word. then you append
the string ay to the word.
e.g. 
en - i splept most of the night
pig latin - iay leptsay ostmay 
foay hetay ightnay
"""

def pig_latin(sentence):
    words = sentence.split()
    result = []
    for word in words:
        if len(word)>1:
            result.append(word[1:]+word[0]+'ay')
        else:
            result.append(word+'ay')
    return ' '.join(result)