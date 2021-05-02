# Validating Regular Expressions in Python
import re
for i in range(int(input())) :
    try :
        S = input()
        re.compile(S)
    except :
        print("False")
        continue
    print("True")