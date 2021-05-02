def is_sorted(b):
    lst_1 = sorted(b)
    lst_2 = sorted(b, reverse=True)
    if lst_1 == b or lst_2 == b:
        return True
    return False


while True:
    print("Enter exit to exit")
    a = input("Enter the three integers: ")
    b = a.split()
    if a == "exit":
        break
    print(is_sorted(b))
