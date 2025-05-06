s = "MCMXCIV" # Output: 1994 "MCMXCIV"
s_2 = "LVIII"
s_3 = "III"
s_4 ="MCDLXXVI" # 1476
"""
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def romanToInt(s: str) -> int:
    length = len(s)
    print(f"L = {length}")
    result = 0
    control = []
    roman_values = {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
    'C': 100,  'XC': 90,  'L': 50,  'XL': 40,
    'X': 10,   'IX': 9,   'V': 5,   'IV': 4,
    'I': 1
    }
    for i in range(length-1, -1, -2):
        value = roman_values.get(s[i-1:i+1])
        if value:
            control.append(s[i-1:i+1])
            result += value
        else:
            for c in s[i-1:i+1]:
                control.append(c)
            result += sum([roman_values.get(x, 0) for x in s[i-1:i+1]])
        if i == 2:
            control.append(s[0])
            result += roman_values.get(s[0], 0)
    print(control)
    print(result)
    return result

print(romanToInt(s) == 1994)
#print(romanToInt(s_2) == 58)
#print(romanToInt(s_3) == 3)
print(romanToInt(s_4) == 1476)