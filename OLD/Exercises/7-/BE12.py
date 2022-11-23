feet_inches = input("Enter Feet and Inches: ")
def convert(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet *0.3048 + inches *0.0254
    return meters

        #(f"{feet} feet and {inches} inches is equal to {meters} meters.")
meters = convert(feet_inches)

print(meters)

if float(meters) < 1:
    print('kid too small, no ride')
else:
    print('Ok, kid can ride')