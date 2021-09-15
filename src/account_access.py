import __main__
import pymysql as mysqltr
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")

hello = input("do you already have an account? (y/n)")
if hello == "y" :
        acc = print('''do you want to create a product list? *beta* 
        proceed to dashboard? (pl/d)''')
        if acc == "d":
            name = input("account name:")
            cursor = con.cursor()
            sql = "select * from user_data where Name = %s "
            cursor.execute(sql, name)
            hi = input("do you intend to update acc details or delete? (u/d)")
            if hi == "u":
                change = input('''what do you want to change:
                Name (n)
                PhoneNumber (p)
                EmailId (e)''')
                if change == "n":
                    updated_n = input("updated name:")
                    sql1 = "update user_data SET Name = %s"
                    cursor.execute(sql1, (updated_n,name))
                    #con.commit()
                elif change == "p":
                    updated_p = int(input("updated phone number"))
                    sql1 = "update user_data SET PhoneNumber = %s"
                    cursor.execute(sql1, (updated_p,name))
                    #con.commit()
                elif change == "e":
                    updated_id = int(input("updated EmailId"))
                    sql1 = "update user_data SET EmailId = %s WHERE Name = %s"
                    cursor.execute(sql1, (updated_id,name))
                    #con.commit
            elif hi == "d":
                delete = input('''what do you want to change:
                Name (n)
                PhoneNumber (p)
                EmailId (e)
                delete account(da)''')
                print("in dev")
            visit = input("vist the updated marketplace?(y/n)")
            if visit == "y":
                __main__()
            elif visit == "n":
                print("thank you for visiting us!")
        elif acc == "pl":
            print("in development")
else:
    print("create an account today!")
    __main__()


            
            

