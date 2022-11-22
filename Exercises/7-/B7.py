"""temperatures = [10, 12, 14]
temperatursString = [str(ints) + '\n' for ints in temperatures]
file = open("file.txt", 'w')

file.writelines(temperatursString)"""



numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)