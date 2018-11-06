from bs4 import BeautifulSoup
import urllib.request
#from mysql.connector import MySQLConnection, Error
import mysql.connector

quote_page = "https://en.wikipedia.org/wiki/88_modern_constellations"

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page,"html.parser")

#print(soup)

li = soup.select("tbody tr")

print(type(li))
print(len(li))
list0 = []
for i in li[85:90]:
	#print(i.get_text())
	objs = i.select("td")
	#print(objs);
	list1 = []
	for j in objs:
		print(type(j.get_text()))
		st = j.get_text()
		try:
			ind = st.index('/')
			list1.append(st[:ind].strip())
		except:	 
			list1.append(st.strip())
	list0.append(list1)
	# for j in i.get_text().split(' '):
	# 	print(j)
	print(100*'*')
	#if i:
		#print(i.get_text())
for i in list0:
	print(i)	


conn = mysql.connector.connect(user='root', database='xplore', password='root123')

cursor = conn.cursor()	
print(list0)
list0 = list0[:2]
j = 87
for i in list0:
	query = "INSERT INTO constellations_constellation values(%s,%s,%s,%s,%s)"
	print(i[0],i[4],i[5],i[6])
	args= (j,i[0],i[4],i[5],i[6])
	cursor.execute(query, args)
	j = j + 1
	#cursor.commit()
conn.commit()