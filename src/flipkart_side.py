#importing web-scrapping tools via BS4
import requests
from bs4 import BeautifulSoup as soup 


print('''product in stock: tv cables ''')
ei = input("confirm email id\n")
my_url = "https://www.flipkart.com/gaming-consoles/pr?sid=4rr,nqk&otracker=product_breadCrumbs_Gaming+Consoles"

page_html = requests.get(my_url)

#parsing the extracted data
page_soup = soup(page_html.content, "lxml")

#creating a container to store extracted data
containers = page_soup.findAll("div",{"class" : "_13oc-S"})

#looping through data to find our targetted section of the html-web page
for container in containers:
    #using findAll parsing for our section(json)
    title_container = container.findAll("a",{"class":"s1Q9rs"})
    #finding content via indexing the list created
    product_name = title_container[0].text
    #printing the titles extracted from the web page
    y = product_name
    print(product_name)


print("-------do not worry about noting it down! The top product is in your email inbox:)")
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("sender email", "sender email password")
message = y
s.sendmail("sender email", ei, message)
s.quit()
