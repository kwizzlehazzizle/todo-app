

try:
    TotalValue = float(input("Enter total value: "))
    Value = float(input("Enter value: "))
    Percent = (Value/TotalValue)*100
    print(f"That is {Percent}%")
except ValueError:
        print("You need to enter a number. Run the program again")
except ZeroDivisionError:
        print("You can't divide by zero!")