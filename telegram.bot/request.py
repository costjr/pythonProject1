import requests
from bs4 import BeautifulSoup

def scrape_data():
    response = requests.get("https://999.md/ru/list/phone-and-communication/mobile-phones")
    soup = BeautifulSoup(response.text, "html.parser")
    news_articles = soup.find_all("li", class_ = "ads-list-photo-item")
    phones = []
    for article in news_articles:
        try:
            if article != None:
                title = article.find("div", class_ = "ads-list-photo-item-title").text
                image = article.find("img")["src"]
                link = article.find("a")["href"]

                print(title)
                print(image)
                print("https://999.md/" + link)
                phones.append("https://999.md/" + link)
        except:
            pass
    return phones
def scrape_car():
    response = requests.get("https://999.md/ru/list/transport/cars")
    soup = BeautifulSoup(response.text, "html.parser")
    news_articles = soup.find_all("li",class_ ="ads-list-photo-item")
    cars = []
    for article in news_articles:
        try:
            if article != None:
                title = article.find("div", class_ = "ads-list-photo-item-title")
                image = article.find("img")["src"]
                link = article.find("a")["href"]

                print(title)
                print(image)
                print("https://999.md/" + link)
                cars.append("https://999.md/" + link)
        except:
            pass
    return cars