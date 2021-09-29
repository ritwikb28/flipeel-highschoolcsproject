print("##WELCOME TO FLIPEEL 2.0, We are so excited for you to see our fresh features!##")
client_proceed = input("how can we serve you today? (account access/ tech market)"'\n')
fname = input("your name:")
print("hello",fname)
if client_proceed == "tech market":
    print('please fill in the required details so that we are able to serve you better')
    stdinp = input("Do you accept our terms and confitions? (Y/N)"'\n')
    if stdinp == "Y":
        import server_side
        server_side
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






