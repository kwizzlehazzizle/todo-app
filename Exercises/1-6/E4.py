#Dollars = float(input("How many dollars to convert to Euros?: "))
#print("Amount in Euros: ", Dollars *.95)
"""
ranking = ['John', 'Sen', 'Marry']
desiredRankNumber = int(input("Enter rank number: ")) - 1
print(ranking[desiredRankNumber])
"""

ranking = ['John', 'Sen', 'Marry']
name = input("Choose the name of the person whose rank you wish to know: " )
rank = ranking.index(name)+1
print(rank)