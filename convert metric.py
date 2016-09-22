# 5ml = 1 tsp
def convert(ml):
    tsp = round((float(ml) * .2), 3)
    return tsp

print ("i will convert millileters to teaspoons for you")
millileters = raw_input("how many millileters? ")
msr = convert (millileters)
print (millileters + " millileters is equivilent to " + str(msr) + "teaspoon")
