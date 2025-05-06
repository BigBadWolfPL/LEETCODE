s = "MCMXCIV" # Output: 1994
"""
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def romanToInt(s: str) -> int:
    roman_values = {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
    'C': 100,  'XC': 90,  'L': 50,  'XL': 40,
    'X': 10,   'IX': 9,   'V': 5,   'IV': 4,
    'I': 1
    }
    result = 0
    for letter in s:
        print(letter)
        result += roman_values.get(letter, 0)
    return result
print(romanToInt(s))