test_1 = "255.100.50.0" # "255[.]100[.]50[.]0"
test_2 = "1.1.1.1" # "1[.]1[.]1[.]1"



def defangIPaddr(address: str) -> str:
    return address.replace(".", "[.]")


print(defangIPaddr(test_1))
print(defangIPaddr(test_2))


