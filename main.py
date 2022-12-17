import requests
import bs4


page = requests.get("https://www.defacto.com/en-eg/man-shorts-bermudas")
src = page.content

#print(page.content)
soup = bs4.BeautifulSoup(src,"html.parser")

short_titles = []
short_prices = []

short_title = soup.find_all("h3",{"class":"product-card__title"})

short_price = soup.find_all("div",{"class":"product-card__price--new d-inline-flex"})


for i in range(len(short_title)):
    short_titles.append(short_title[i].text)
    short_prices.append(short_price[i].text)
print(short_titles,short_prices)