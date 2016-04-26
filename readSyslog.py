#!/usr/bin/python

from xlrd import open_workbook
import json

book = open_workbook('Syslog.xlsx')
sheet = book.sheet_by_index(1)

# read header values into the list    
keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]

dict_list = []
for row_index in xrange(1, sheet.nrows):
	d = {keys[col_index]: sheet.cell(row_index, col_index).value for col_index in xrange(sheet.ncols)}
	dict_list.append(d)

for row in dict_list:
	print row['Action']
