import pymysql as mysqltr
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")

#if con.is_connected() == False:
    #print("error")

cursor = con.cursor()
print("please note that you are now creating an account")
proceed = input("N/Y\n")
if proceed == "N":
    print("thank you")
if proceed == "Y":
    sql = "insert into `user_data` (`Name`, `PhoneNumber`,`EmailId`, `ProductIntrest`, `DATE`) Values(%s, %s, %s, %s, %s)"
    name = input("name:")
    ph_no = int(input("phone number:"))
    email = input("email id:")
    prod = input("product of intrest:")
    print("date format: yyyy-mm-dd")
    date = input("date:")
    cursor.execute(sql, (name, ph_no, email, prod, date ))

con.commit()




