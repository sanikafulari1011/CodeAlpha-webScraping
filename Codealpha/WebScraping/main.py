"""print("Hello, CodeAlpha!")
import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com"
response = requests.get(url)
print("status code:", response.status_code)
soup = BeautifulSoup(response.text, "html.parser" )
print("website Title:", soup.title.text)"""
import pandas as pd 
import requests
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com/page/{}/"
data=[]

for page in range (1, 11):

    print (f"\nScraping page {page}")

    url = base_url.format(page)

    response = requests.get(url)
    print("status Code:",response.status_code)

    soup = BeautifulSoup( response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
# Find all authors
    authors = soup.find_all("small", class_="author")
# Print quotes with authors
    for i in range(len(quotes)):
     data.append({ 
        "Quote": quotes[i].text,
        "Author":authors[i].text
          })
     print("----------------------------------")
     print("Quote :", quotes[i].text)
     print("Author:", authors[i].text)

print ("\n Total Records :", len(data))
df = pd.DataFrame(data)

print (df)
df.to_csv("quotes.csv", index = False , encoding="utf_8_sig")
print("CSV file created successfully!")
