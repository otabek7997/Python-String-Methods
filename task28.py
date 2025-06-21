coment = input()

bad = ('bad', 'ugly', 'stupid')
txt_bad = False

if 'bad' in coment:
    txt_bad = True

elif 'ugly' in coment:
    txt_bad = True
elif 'stupid' in coment:
    txt_bad = True

print(txt_bad)