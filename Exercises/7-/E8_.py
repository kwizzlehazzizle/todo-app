while 1:
    headOrTail = input("Throw the coin and enter head or tail here: ")

    with open('HeadsOrTails.txt', 'r') as file:
        HeadsOrTails = file.readlines()
        HeadsOrTails.append(headOrTail+'\n')

    with open('HeadsOrTails.txt', 'w') as file:
        file.writelines(HeadsOrTails)

    with open('HeadsOrTails.txt', 'r') as file:
        HeadsOrTails = file.readlines()
        print(HeadsOrTails)
        HeadsOrTails = [element.strip('\n') for element in HeadsOrTails]
        HeadCount = HeadsOrTails.count('head')
        print("HeadCount: ", HeadCount)
        TotalCount = HeadCount + HeadsOrTails.count('tail')
        print("TotalCount: ", TotalCount)
        PercentHeads = HeadCount/TotalCount


    print(PercentHeads)