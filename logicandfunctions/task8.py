"""
Given a day of the week encoded as 
o = sun, 1 = mon and so on and so forth,
and a boolean indicating we are on 
a vacay, return a string of the form 
7:00 indicating when the alarm clock
should ring. Weekdays, the alarm should
be 7:00 and weekends 10:00. unless we
are on a vacation- then weekdays are 10:00
and weekend should be off. 
"""

def alarm_clock(day, vacation):
    if vacation:
        if day in [0, 5]:
            return "off"
        else:
            return "10:00"
    else:
        if day in [0, 5]:
            return "10:00"
        else:
            return "7:00"

print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))