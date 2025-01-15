"""
give an out string length 4, such as
<<>> and a word, write a function to
return a new string where the word is
in the middle of the out string.
e.g. <<word>>
"""
def make_out_word(out, word):
    # split the strings into 2 halves
    start = out[:2]
    end = out[2:]

    return start + word + end

print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))