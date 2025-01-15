"""
write a function to return the number
of times that the string code appears
anywehre in the given string, except 
we'll accept any letter for the d so
cope and cooe count
"""
def count_code(s):
    return sum(1 for i in range(len(s)-3) if s[i:i+2] == 'co' and s[i+3] == 'e')

print(count_code('aaacodebbb'))
print(count_code('codexxcode'))
print(count_code('cozexxcope'))