s = "MCMXCIV"
s_2 = "LVIII"
s_3 = "III"
s_4 ="MCDLXXVI"
s_5 = "MMMDXLI"
s_6 = "D"
"""
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def romanToInt(s: str) -> int:
    length = len(s)
    result = 0
    idx = 0
    roman_values = {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
    'C': 100,  'XC': 90,  'L': 50,  'XL': 40,
    'X': 10,   'IX': 9,   'V': 5,   'IV': 4,
    'I': 1
    }
    
    if length == 1:
        return roman_values.get(s)
    for i in range(length-1, -1, -2):
        i += idx
        part = s[i-1: i+1]
        part_2 = s[i-2:i]
        if i < 0:
            break
        value = roman_values.get(part, 0)
        if value:
            result += value
        elif roman_values.get(part_2, 0) :
            result += roman_values.get(part_2, 0)
            result += roman_values.get(s[i], 0)
            idx -=1
        else:
            result += sum([roman_values.get(x, 0) for x in part])
        if not i and i+1 < 2:
            result += roman_values.get(s[i], 0)
    return result
        

print(romanToInt(s) == 1994)
print(romanToInt(s_2) == 58)
print(romanToInt(s_3) == 3)
print(romanToInt(s_4) == 1476) 
print(romanToInt(s_5) == 3541)
print(romanToInt(s_6) == 500)


"""
def romanToInt(s: str) -> int:
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    result = 0
    prev_value = 0

    for char in reversed(s):
        value = roman_values[char]
        if value < prev_value:
            result -= value
        else:
            result += value
            prev_value = value
    return result
"""
