# -*- coding: utf-8 -*-
import scrapy


# Helper variables/definitions
NAMES = []
DIFF_P = []
DIFF_N = []
VALUE = []
VALUE= []

str_chopper = lambda String : list(String)


class PriceHighsSpider(scrapy.Spider):
	""" This spider will grab the price highs and format them
	into readable data sets, after that has been accomlished 
	the next goal will be writing the parsed data to a file """

	name = 'highs'
	allowed_domains = ['services.runescape.com']
	start_urls = ['http://services.runescape.com/m=itemdb_oldschool/top100?list=2',
								'http://services.runescape.com/m=itemdb_oldschool/top100?list=3']

	def parse(self, response):
		"""Grab the span elements of every item 
		listed that has gone up in price"""

		# Get player item names
		item_names = response.xpath('//a[@class="table-item-link"]/span/text()').extract()

		# Get player item change %
		item_change_pos = response.xpath('//tbody/tr/td[@class="change positive"]/a/text()').extract()
		item_change_neg = response.xpath('//tobdy/tr/td[@class="change negative"]/a/text()').extract()
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
			
		# Append all differences to DIFF_x list
		for item in item_change_pos:
			DIFF_P.append(item)
			
		for item in item_change_neg:
			DIFF_N.append(item)
			
		# Append all values to VALUE list
		for item in item_value:
			VALUE.append(item)

		# Primary formatting loop
		for i in len(DIFF_P):
			print("""
	=====================
									P+
	Item:\t{}
	Change:\t{}
	Price:\t{}
	====================
			""".format(NAMES[i],DIFF_P[i],VALUE[i]))
		

#############################################
"""
	STUFF TO DO
	- Fix item names to being no longer than
	22 characters max
	- Add in current GP value of item to display
"""
#############################################

