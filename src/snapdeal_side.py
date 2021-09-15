#importing web-scrapping tools via BS4
from os import name
import requests
from bs4 import BeautifulSoup as soup 

my_url = "https://www.snapdeal.com/products/computers?sort=plrty"

page_html = requests.get(my_url)

#parsing the extracted data
page_soup = soup(page_html.content, "lxml")

#creating a container to store extracted data
containers = page_soup.findAll("div",{"class" : "product-row js-product-list centerCardAfterLoadWidgets dp-click-widgets"})

#looping through data to find our targetted section of the html-web page
for container in containers:
    #using findAll parsing for our section(json)
    title_container = container.findAll("p",{"class":"product-title"})

    #finding content via indexing the list created
    for i in range(0, len(title_container)):
        product_name = title_container[i].text
    #printing the titles extracted from the web page
        print(i, product_name)