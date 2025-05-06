s = "MCMXCIV" # Output: 1994 "MCMXCIV"
s_2 = "LVIII"
s_3 = "III"
s_4 ="MCDLXXVI" # 1476     M CD L X X V I
s_5 = "MMMDXLI"
"""
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


def romanToInt(s: str) -> int:
    length = len(s)
    result = 0
    control = []
    roman_values = {
    'M': 1000, 'CM': 900, 'D': 500, 'CD': 400,
    'C': 100,  'XC': 90,  'L': 50,  'XL': 40,
    'X': 10,   'IX': 9,   'V': 5,   'IV': 4,
    'I': 1
    }
    #for i, j in zip(range(length), range(2, length)):
    #    print(f"i: {i}, j: {j}")
    idx = 0
    for i in range(length-1, -1, -2):
        
        i += idx
        part = s[i-1: i+1]
        part_2 = s[i-2:i]
        #print(f"SPRAWDZAM: p {part} || p_2 {part_2} INDEX = {i}")
        if i < 0:
            break
        value = roman_values.get(part, 0)
        #print(f"part: {part}, part_2: {part_2}")
        if value:
            #print(f"part accepted: {part}")
            result += value
            control.append(value)

        elif roman_values.get(part_2, 0) :
            #print(f"part_2 accepted: {part_2}")
            result += roman_values.get(part_2, 0)
            result += roman_values.get(s[i], 0)
            control.append(roman_values.get(part_2))
            control.append(s[i])
            idx -=1

        else:
            result += sum([roman_values.get(x, 0) for x in part])
            for x in part:
                control.append(x)
                #print(f"part added: {x}")
        if not i and i+1 < 2:
            result += roman_values.get(s[i], 0)
            control.append(s[i])
            #print(f"part added: {s[i]}")
    #print(control, result)
    return result
        

print(romanToInt(s) == 1994)
print(romanToInt(s_2) == 58)
print(romanToInt(s_3) == 3)
print(romanToInt(s_4) == 1476) 
print(romanToInt(s_5) == 3541) 
