# importing csv module 
import csv 
import mysql.connector  
# csv file name 
filename = "database.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 
conn = mysql.connector.connect(user='root', database='xplore', password='root123')

cursor = conn.cursor()	
  
#  printing first 5 rows 
print('\nFirst 5 rows are:\n') 
count = 1
flag = 0
flag1 = 0
flag2 = 0
flag3 = 0
flag4 = 0
for row in rows: 
    # parsing each column of a row 
    print(row[0],'Earth',row[5])
    if row[0]=='USA 181' and flag == 0:
    	row[0]='USA 181(1)'
    	flag = 1
    if row[0]=='USA 194' and flag1 == 0:
    	row[0]='USA 194(1)'
    	flag1 = 1	
    if row[0]=='USA 229' and flag2 == 0:
    	row[0]='USA 229(1)'
    	flag2 = 1
    if row[0]=='USA 238' and flag3 == 0:
    	row[0]='USA 238(1)'
    	flag3 = 1
    if row[0]=='USA 264' and flag4 == 0:
    	row[0]='USA 264(1)'
    	flag4 = 1
    query = "INSERT INTO satellites_satellite values(%s,%s,%s)"
    args = (row[0],row[5],'Earth')
    cursor.execute(query, args)

    query = "INSERT INTO satellites_artificialsatellite values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"    
    print(count,row[3],row[0],row[7],row[18],row[22],row[23],row[14],row[8],row[4])
    args = (count,row[3],row[0],row[7],row[18],row[22],row[23],row[14],row[8],row[4])
    cursor.execute(query, args)
    # for col in row: 
    #     print("%10s"%col), 
    #print('\n') 
    count = count + 1
conn.commit()    