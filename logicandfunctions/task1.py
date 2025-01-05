"""
Write a program with a loop that will
repeatedly ask the user to enter a 
word. The user should enter nothing 
(press enter w/o typing anything) to
signal the end of the loop. Once the 
loop ends, the program should display
the avergae length of the words 
entered, rounded to the nearest 
whole number.
"""

def main():
    print("Enter words one by one. To exit press Enter: ")
    words = []

    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        words.append(word)

    if words:
        total_len = sum(len(word) for word in words)
        avg_leb = round(total_len / len(words))
        print("The average length of entered words comes out to: ", avg_leb)
    else:
        print("You didn't enter any words.")

main()