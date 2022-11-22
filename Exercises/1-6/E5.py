




file = open(r"C:\Users\Marc\Downloads\members.txt")
contents = file.readlines()
file.close()
print(contents)

#newmember = contents + input("Add a new member: ") + '\n'
newmember =  input("Add a new member: ") + '\n'

file = open(r"C:\Users\Marc\Downloads\members.txt", 'w')
#file.writelines(newmember)
contents.append(newmember)
file.writelines(contents)
file.close()


file = open(r"C:\Users\Marc\Downloads\members.txt")
contents = file.read()
file.close()
print(contents)




