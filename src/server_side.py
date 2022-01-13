import pymysql as mysqltr
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")

#if con.is_connected() == False:
    #print("error")

cursor = con.cursor()
print("please note that you are now creating an account")
proceed = input("N/Y\n")
if proceed == "N":
    print("thank you")
    signin = input('do you want to sign in instead?')
if proceed == "Y":
    sql = "insert into `user_data` (`name`, `ph_no`,`email`, `prod`, `city`, `date`) Values(%s, %s, %s, %s, %s, %s)"
    name = input("name:")
    ph_no = int(input("phone number:"))
    email = input("email id:")
    prod = input("product of intrest:")
    city = input("city of residence:")
    print("date format: yyyy-mm-dd")
    date = input("date:")
    cursor.execute(sql, (name, ph_no, email, prod, city, date ))

con.commit()




