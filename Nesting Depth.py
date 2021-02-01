l = 1
T = int(input("Enter the number of Test Cases (min 1): "))
r = rn = 0
x = ""

while l <= T:
    st = s = []
    S = input("Enter the digit (length between 1 to 100): ")
    s = list(S)
    for i in range(len(s)):
        m = "(" + s[i] + ")"
        st.append(m)
    print("Case #",l,": ",x.join(st))
    l +=1
