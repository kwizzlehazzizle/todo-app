FileA = 'a.txt'
FileB = 'b.txt'
FileC = 'c.txt'

FileNames = [FileA,FileB,FileC]

for i, filename in enumerate(FileNames):
    fileName = FileNames[i]
    file = open(fileName, 'r')
    print(file.read())