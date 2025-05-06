def isPalindrome(x: int) -> bool:
    temp = str(x)
    return temp == temp[::-1]


print(isPalindrome("121"))