#!/usr/bin/env python
import sys

# Mapper to return local top 20 houses by price
# Data source:  https://data.smartdublin.ie/dataset/dublin-residential-property-price-register
# Data header: Address	PostCode	Price	PropertyType

# Initialise a list to store the top N records as a collection of touples (price, record)
myList = []
n = 20	# Number of top N records

for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split data values into list
	data = line.split("\t")
	
	# convert price (currently a string) to int
	try:
		Price = int(data[2])
	except ValueError:
		# ignore/discard this line
		continue
	
	# add (price, record) touple to list
	myList.append( (Price, line) )
	# sort list in reverse order
	myList.sort(reverse=True)
	
	# keep only first N records
	if len(myList) > n:
		myList = myList[:n]
		
# Print top N records
for (k,v) in myList:
	print(v)