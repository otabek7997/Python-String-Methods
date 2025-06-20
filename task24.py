mail = input()

if mail.endswith('.com'):
    print("To'g'ri")

elif mail.startswith('@'):
    print("noto'g'ri")

else:
    print('''something's wrong''')        