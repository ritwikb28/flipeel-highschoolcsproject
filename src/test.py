from re import search
import sys
import pymysql as mysqltr
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")

#if con.is_connected() == False:
    #print("error")

cursor = con.cursor()
ei = input("email id:")
sql1 = "select name from user_data where email = %a"
y = cursor.execute(sql1,ei)
con.commit()
print(y)