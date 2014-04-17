import sys

meal = float(sys.argv[1])
# meal = float(raw_input("what is the base cost of your meal? "))
tax = float(sys.argv[2])
# tax = float(raw_input("what is the tax rate on your meal? "))
tip = float(sys.argv[3])
# tip = float(raw_input("what percent tip do you want to pay? "))
tax2 = float(tax / 100)
tip2 = float(tip / 100)

tax_value = float(meal * tax2)
meal_with_tax = float(meal + meal * tax2)
tip_value = float(meal * tip2)
total = float(meal_with_tax + tip_value)

print "The base cost of your meal was ${0:.2f}".format(meal)
print "you need to pay ${0:.2f} for tax".format(tax_value)
print "tipping at a rate of {0:.1f}%%, you should leave ${0:.2f} for tip".format(tip,tip_value)
print "the grand total of your meal is ${0:.2f}".format(total)