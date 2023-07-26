print("Welcome to the tip calculator!")

bill = float(input("How much was the total bill >>> $"))
tip = float(input("What percent would you like to tip (10, 12, 15) >>> "))
ppl = int(input("How many people are spliting the bill >>> "))

splitCost = (bill * (1 + tip/100)) / ppl
splitCost = round(splitCost, 2)
#other way is to >>> splitCost = "{:.2f}".format(splitCost)

print("Each person pays >>> $" + str(splitCost))