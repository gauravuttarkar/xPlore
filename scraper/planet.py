from bs4 import BeautifulSoup
import urllib.request
#from mysql.connector import MySQLConnection, Error
from bs4 import BeautifulSoup
import urllib.request
#from mysql.connector import MySQLConnection, Error
import mysql.connector
import random

quote_page = "https://en.wikipedia.org/wiki/List_of_exoplanets_(full)"

page = urllib.request.urlopen(quote_page)

soup = BeautifulSoup(page,"html.parser")

li = soup.select("table tbody tr")

print(type(li))
print(len(li))
j = 0
list0 = []
for i in li[:3827]:
	#print(j)
	j = j + 1
	#print(i.get_text())
	objs = i.select("td")
	if len(objs) > 0:
		list1 = []

		for k in objs:
			st = k.get_text()
			list1.append(st.strip())
			#print(k.get_text())
		list0.append(list1)
			
	# print(100*'-')
	# print("--"*50)


# for i in list0:
# 	print(i)

random.shuffle(list0)
for i in list0:
	print(i)
conn = mysql.connector.connect(user='gaurav', database='xplore', password='root123')

cursor = conn.cursor()	

cursor.execute ("select starName,confirmedPlanets from stars_star")

data = cursor.fetchall()
count = 1

#for i in data[:1]:


for i in data:
	#print(data)
	for j in range(int(i[1][:1])):
		count = count + 1
		obj = list0.pop()
		try:
			query = "INSERT INTO planets_planet values(%s,%s,%s,%s,%s)"
			print(obj[0],obj[1],obj[2],obj[3],i[0])
			args= (obj[0],obj[1],obj[2],obj[3],i[0])
			cursor.execute(query, args)
		except:
			print("error",i)	
		try:
			query = "INSERT INTO planets_exoplanets values(%s,%s,%s)"
			print(count,obj[8],obj[0])
			args= (count,obj[8],obj[0])
			cursor.execute(query, args)
		except:
			print("error",i)	
			count = count - 1

conn.commit()			