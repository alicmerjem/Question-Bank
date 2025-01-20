"""
write a function that counts how many
words occur in a list up to and 
including the first word containing
character q or character w
"""
def count_until_wq(words):
    count = 0
    for word in words:
        count+= 1
        if 'q' in word or 'w' in word:
            break
    return count

print(count_until_wq(['apple', 'something', 'i have no idea', 'we just used w and q, how crazy is that?']))