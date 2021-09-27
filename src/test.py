import pymysql as mysqltr
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")
cursor = con.cursor()
ph = int(input("confirm your phone number"))
updated_n = input("updated name:")
sql1 = "update user_data SET Name = %s WHERE PhoneNumber = %a"
y = cursor.execute(sql1, ([updated_n],ph))
con.commit()
print(y)