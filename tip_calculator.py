meal = 44.50
tax = 0.0675
tip = 0.15

tax_value = meal * tax
meal_with_tax = meal + meal * tax
tip_value = meal * tip
total = meal_with_tax + (tip_value)

print "The base cost of your meal was %d" % (meal)
print "you need to pay %d for tax" % (tax)
print "tipping at a rate of 15%%, you should leave %d for tax" % (tax_value)
print "grand total of your meal is %d" % (total)

#raw_input
meal = float(raw_input("what is the base cost of your meal? "))
tax = float(raw_input("what is the tax rate on your meal? "))
tip = float(raw_input("what percent tip do you want to pay? "))
tax2 = float(tax / 100)
tip2 = float(tip / 100)

tax_value = float(meal * tax2)
meal_with_tax = float(meal + meal * tax2)
tip_value = float(meal * tip2)
total = float(meal_with_tax + tip_value)

print "The base cost of your meal was $%s" % (meal)
print "you need to pay $%d for tax" % (tax_value)
print "tipping at a rate of %d%%, you should leave $%d for tip" % (tip,tip_value)
print "the grand total of your meal is $%d" % (total)