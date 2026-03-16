import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

products = []

for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.find_all("article", class_="product_pod")

    for item in items:
        name = item.h3.a["title"]
        price = item.find("p", class_="price_color").text
        availability = item.find("p", class_="instock availability").text.strip()

        products.append({"Name": name, "Price": price, "Availability": availability})

df = pd.DataFrame(products)

df.to_csv("products.csv", index=False)

print("Scraping complete. Data saved to products.csv")
