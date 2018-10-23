# -*- coding: utf-8 -*-
import scrapy


# Helper variables/definitions
NAMES = []
DIFF = []
VALUE = []

str_chopper = lambda I : list(I)


class PriceHighsSpider(scrapy.Spider):
	""" This spider will grab the price highs and format them
	into readable data sets, after that has been accomlished 
	the next goal will be writing the parsed data to a file """

	name = 'highs'
	allowed_domains = ['services.runescape.com']
	start_urls = ['http://services.runescape.com/m=itemdb_oldschool/top100?list=2']

	def parse(self, response):
		"""Grab the span elements of every item 
		listed that has gone up in price"""

		# Get player item names
		item_names = response.xpath('//a[@class="table-item-link"]/span/text()').extract()

		# Get player item change %
		item_percent = response.xpath('//tbody/tr/td[@class="change positive"]/a/text()').extract()
		
		# Get item value
		item_value = response.xpath('//tbody/tr/td[4]/a/text()').extract()


		print("*"*30)
		print("|||\tSpider Has Ran \t|||\n")
		
		# Tell the user if no item's have been found
		if len(item_names) == 0:
			print(">\tNo Item's collected")
		else:
			print(item_names)
		
		# Append all items to NAMES list
		for item in item_names:
			NAMES.append(item)
			
		# Append all differences to DIFF list
		for item in item_percent:
			DIFF.append(item)
			
		# Append all values to VALUE list
		for item in item_value:
			VALUE.append(item)

		print(">\tparse() has finished\n" + "*"*30)

		# Primary formatting loop
		for i in range(0,100):
			#print("GE Item: {}\t\t  |  PercentChange: {}".format(NAMES[i],DIFF[i]))
			print("""
		=====================
		Item:\t{}
		Change:\t{}
		Price:\t{}
		====================
			""".format(NAMES[i],DIFF[i],VALUE[i]))
		

#############################################
"""
	STUFF TO DO
	- Fix item names to being no longer than
	22 characters max
	- Add in current GP value of item to display
"""
#############################################

