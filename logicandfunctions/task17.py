"""
Write a function blackjack that for 2
int values greater than 0 returns
whicever value is nearest to 21 w/0
going over. return 0 if they both go
over.
"""
def blackjack(a, b):
    if a>21 and b>21:
        return 0
    if a>21:
        return b
    if b>21:
        return a
    return max(a, b)

print(blackjack(19, 21))
print(blackjack(21, 19))
print(blackjack(19, 22))