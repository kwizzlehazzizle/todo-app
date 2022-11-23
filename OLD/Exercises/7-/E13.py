"""def get_age(year_of_birth, current_year = 2022):
    local_age = current_year-int(year_of_birth)
    return(local_age)

InputtedYearOfBirth = input("What is your year of birth? ")

Age = get_age(InputtedYearOfBirth)
if Age < 120:
    print("Your age is: ", Age)
else:
    print("You liar, you should be dead. There's no way you're", Age, "years old!")
"""

def get_num_names (names="Mandy,Mindy,Moe,Johnny"):
    namelist = names.split(',')
    num_names = len(namelist)
    return(num_names)

numberofnames = get_num_names()
print("numberofnames : ", numberofnames )
