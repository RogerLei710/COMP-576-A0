while True:
    strInput = input("Enter a string\n")
    if strInput == "-1":
        break

    for c in strInput:
        print(ord(c) - ord('A'), end=' ')
    print("\n")


