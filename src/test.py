import pymysql as mysqltr
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")
cursor = con.cursor()
ph = int(input("confirm your phone number"))
sql1 = "update user_data SET Name = NULL WHERE PhoneNumber = %a"
y = cursor.execute(sql1,ph)
con.commit()
print(y)