# ----------------------------------------------------- #
# requests get method example

import requests
from bs4 import BeautifulSoup

content = requests.get("https://www.imdb.com/find?q=cars&ref_=nv_sr_sm")
# url = result page for cars

doc = BeautifulSoup(content.text, "html.parser")

name_tags = doc.find_all(class_="result_text")

for name in name_tags:
    print(name.a.string)
    
    
# ----------------------------------------------------- #
# requests post method example
url = "https://search.dca.ca.gov/results"
header = {    
    'boardCode': '9',
    'licenseType': '250',
    'licenseNumber': '', 
    'firstName': 'John',
    'lastName': 'Kelly',
    'registryNumber': '' 
}

response = requests.post(url, data=header)

doc = BeautifulSoup(response.text, "html.parser")

name_tags = doc.find_all("h3")

print(len(name_tags))

for name in name_tags:
    print(name.text)
