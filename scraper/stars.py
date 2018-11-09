from bs4 import BeautifulSoup
import urllib.request
#from mysql.connector import MySQLConnection, Error
import mysql.connector

quote_page = "https://en.wikipedia.org/wiki/List_of_multiplanetary_systems"

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page,"html.parser")

li = soup.select("table tbody tr")

print(type(li))
print(len(li))
j = 0
list0 = []
for i in li[:475]:
	print(j)
	j = j + 1
	objs = i.select("td")
	#print(objs)
	if len(objs) > 0:
		list1 = []

		for k in objs:
			st = k.get_text()
			list1.append(st.strip())
			print(k.get_text())
		list0.append(list1)
			
	print(100*'-')
#print(list0)
list0 = list0[4:]
for i in list0[:100]:
	print(i)

conn = mysql.connector.connect(user='root', database='xplore', password='root123')

cursor = conn.cursor()	
for i in list0:
	try:
		query = "INSERT INTO stars_star values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		# print(i[0],i[4],i[5],i[6])
		args= (i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11])
		cursor.execute(query, args)
	except:
		print(i)	
	j = j + 1
	#cursor.commit()
conn.commit()