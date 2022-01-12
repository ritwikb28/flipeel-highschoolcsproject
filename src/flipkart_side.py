#importing web-scrapping tools via BS4
from os import name
import requests
from bs4 import BeautifulSoup as soup 


print('''product library in development''')
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
    print(product_name)