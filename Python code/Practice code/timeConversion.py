"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example

s = '12:01:00PM'
Return '12:01:00'.

a = "12:01:00AM'
Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string 
representing the input time in 24 hour format.

timeConversion has the following parameter(s):
string s: a time in 12 hour format

Returns
string: the time in 24 hour format

Input Format
A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints
All input times are valid
"""

def timeConversion(s):

    timeMinusHour = s[2:]
    hour = s[:2]
    pmTime = s.endswith('PM')
    amTime = s.endswith('AM')

    if (pmTime == True) and (int(hour) < 12):
        hour = int(hour) + 12
        return str(hour) + timeMinusHour.rstrip("AMPM")

    elif (pmTime == True) and (int(hour) == 12):
        return s.rstrip("AMPM")

    elif (amTime == True) and (int(hour) == 12):
        return "00" + timeMinusHour.rstrip("AMPM")

    else:
        return s.rstrip("AMPM")

print(timeConversion('12:23:32PM'))
