Password =  input("Enter new password: ")
result = {}

if len(Password) >= 8  :
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in Password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for i in Password:
    if i.isupper():
        uppercase = True
result["uppercase"] = uppercase
print(result)
print(result.values())
print(result.keys())
if all(result.values()):
    print("Strong Password")
else:
    print("WEAK!!!")
