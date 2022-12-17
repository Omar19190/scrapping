import requests
import bs4


page = requests.get("https://www.defacto.com/en-eg/man-shorts-bermudas")
src = page.content

#print(page.content)
soup = bs4.BeautifulSoup(src,"html.parser")

wallet_titles = []
wallet_prices = []

wallet_title = soup.find_all("h3",{"class":"product-card__title"})

wallet_price = soup.find_all("div",{"class":"product-card__price--new d-inline-flex"})


for i in range(len(wallet_title)):
    wallet_titles.append(wallet_title[i].text)
    wallet_prices.append(wallet_price[i].text)
print(wallet_titles,wallet_prices)