import pyfiglet
result = pyfiglet.figlet_format("FLIPEEL")
print(result)
print("##WELCOME TO FLIPEEL 2.0, We are so excited for you to see our fresh features!##")
fname = input("your name:")
print("hello",fname)
import signin
signin
client_proceed = input("how can we serve you today? (account access/ tech market)"'\n')
if client_proceed == "tech market":
    print("Hi, we are so excited to serve you",fname,"\nplease note that FLIPEEL is still in developement\nthank you!")
    client_webpage = input('Where do you want to shop today, tell us!\n(flipkart -f , snapdeal - s):\n')

    if client_webpage == "f":
        import flipkart_side
        flipkart_side
        print("thank you for shopping with us")

    if client_webpage == "s":
        import snapdeal_side
        snapdeal_side
        print("thank you for shopping with us")
elif client_proceed == "account access":
    import account_access
    account_access
else:
    print("wrong proceed code, try again")






