username = 'vali-coder'
text = username.replace('-', "")
print(text)
if "A" < username < "Z":
    print("True") 
elif username.isalpha():
    print('True')     
elif 'a' < username < 'z':
    print("True")
elif  "0" < username < "9":
    print("True")    
else:
    print("False")    
