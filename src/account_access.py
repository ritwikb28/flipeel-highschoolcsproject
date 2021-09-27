import __main__
import pymysql as mysqltr
con = mysqltr.connect(host = "localhost", user = "root", password = "ritwik", database = "project")

hello = input("do you already have an account? (y/n)")
if hello == "y" :
        acc = input('''do you want to create a product list? *beta* 
        proceed to dashboard? (pl/d)''')
        if acc == "d":
            name = input("account name:")
            cursor = con.cursor()
            sql = "select * from user_data where Name = %s "
            cursor.execute(sql, [name])
            hi = input("do you intend to update acc details or delete? (u/d)")
            if hi == "u":
                change = input('''what do you want to change:
                Name (n)
                PhoneNumber (p)
                EmailId (e)''')
                if change == "n":
                    ph = int(input("confirm your phone number"))
                    updated_n = input("updated name:")
                    sql1 = "update user_data SET Name = %s WHERE PhoneNumber = %a"
                    y = cursor.execute(sql1, ([updated_n],ph))
                    con.commit()
                    if y == 1:
                        print("detail updated")
                elif change == "p":
                    ph = int(input("confirm your phone number"))
                    updated_p = int(input("updated phone:"))
                    sql1 = "update user_data SET PhoneNumber = %s WHERE PhoneNumber = %a"
                    y = cursor.execute(sql1, ([updated_p],ph))
                    con.commit()
                    if y == 1:
                        print("detail updated")
                elif change == "e":
                    ph = int(input("confirm your phone number"))
                    updated_id = input("updated emailid:")
                    sql1 = "update user_data SET EmailId = %s WHERE PhoneNumber = %a"
                    y = cursor.execute(sql1, ([updated_id],ph))
                    con.commit()
                    if y == 1:
                        print("detail updated")
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


            
            

