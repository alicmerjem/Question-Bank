"""
The squirrels in Palo Alto spend most
of the day playing. Particularly, they
play is the temperature is between 
60 and 90 (inclusive). Unless it is
summer, then the upper limit is 100
instead of 90. Given an int temperature
and a boolean is_summer, write a function
to return true if the squirells play
and false otherwise. 
"""

def squirrel_play(temperature, is_summer):
    if is_summer:
        return 60 <= temperature <= 100
    else:
        return 60 <= temperature <= 90

print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))
print(squirrel_play(50, True))