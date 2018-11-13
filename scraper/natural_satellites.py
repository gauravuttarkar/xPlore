from bs4 import BeautifulSoup
import urllib.request
#from mysql.connector import MySQLConnection, Error
from bs4 import BeautifulSoup
import urllib.request
#from mysql.connector import MySQLConnection, Error
import mysql.connector
import random

quote_page = "https://en.wikipedia.org/wiki/List_of_natural_satellites"

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page,"html.parser")

li = soup.select("table tbody tr")


print(type(li))
print(len(li))
j = 0
list0 = []
for i in li[20:214]:
	print(j)
	j = j + 1
	#print(i.get_text())
	objs = i.select("td")
	if len(objs) > 0:
		list1 = []
		try:
			img = 'https:'+objs[0].img['src']
		except:
			img = ''	
		list1.append(img)	
		for k in objs:

			st = k.get_text()
			list1.append(st.strip())
			#print(k.get_text())
		list0.append(list1)
	print(100*"-")	

# for j in list0:
# 	print(j)	


conn = mysql.connector.connect(user='gaurav', database='xplore', password='root123')

cursor = conn.cursor()	
j=1
for i in list0:
	try:
		query = "INSERT INTO satellites_satellite values(%s,%s,%s)"
		print(i[3],i[-3],i[-1])
		args= (i[3],i[-3],i[-1])
		cursor.execute(query, args)
	except:
		print("error",i)
		continue
	
	query = "INSERT INTO satellites_naturalsatellite values(%s,%s,%s,%s,%s,%s)"
	print(i[3],i[0],i[8],i[7],i[4])
	args= (j,i[0],i[8],i[7],i[4],i[3])
	cursor.execute(query, args)
	
	#print("error",i)
		
			

	j = j + 1
	#cursor.commit()
conn.commit()	