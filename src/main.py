




print("##WELCOME TO FLIPEEL##")

client_name = input('hello, please tell us your sweet sweet name:\n')

print("Hi, we are so excited to serve you",client_name,"\n please note that FLIPEEL is still in developement\nwthank you!")

print('please fill in the required details so that we are able to serve you better')

client_webpage = input('Where do you want to shop today, tell us!\n(flipakrt -f , snapdeal - s):\n')

if client_webpage == "f":
    import flipkart_side
    

if client_webpage == "s":
    import snapdeal_side
    



