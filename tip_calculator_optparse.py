from optparse import OptionParser

parser = OptionParser()

parser.add_option("-m", "--first", dest="first_arf", help="price of meal", type=float)
parser.add_option("-t", "--second", dest="second_arg", help="tax rate",type=float)  
parser.add_option("-i", "--third", dest="third_arg", help="tip rate", type=float)

(options, args) = parser.parse_args()

if not (options.first_arf and options.second_arg and options.third_arg):
	parser.error('you forgot to supply an input')

tax2 = float(options.second_arg / 100)
tip2 = float(options.third_arg / 100)

tax_value = float(options.first_arf * tax2)
meal_with_tax = float(options.first_arf + options.first_arf * tax2)
tip_value = float(options.first_arf * tip2)
total = float(meal_with_tax + tip_value)

print "The base cost of your meal was ${0:.2f}".format(options.first_arf)
print "you need to pay ${0:.2f} for tax".format(tax_value)
print "tipping at a rate of {0:.1f}%, you should leave ${0:.2f} for tip".format(options.third_arg,tip_value)
print "the grand total of your meal is ${0:.2f}".format(total)