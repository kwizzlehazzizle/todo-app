def get_max():
    grades = [9.6, 9.2, 9.7]
    maxgrade = grades[0]
    mingrade = grades[0]
    for i, grade in enumerate(grades):
        print('i: ', i)
        print('grade: ', grade)
        if maxgrade < grade:
            maxgrade = grade
    return(maxgrade)

print(get_max())