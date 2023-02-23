""" Scraping a local *html* file """

from bs4 import BeautifulSoup


def fetchHeader():
    with open("index.html", "r") as htmlFile:
        content = htmlFile.read()
        # print(content) !debug

        soup = BeautifulSoup(content, "lxml")
        # print(soup.prettify())
        course_headers = soup.find_all("h5")

        for header in course_headers:
            print(header.text)


def deepScrape():
    with open("index.html", "r") as file:
        contents = file.read()

        soup = BeautifulSoup(contents, "lxml")
        cards = soup.find_all("div", class_="card")

        for card in cards:
            print(card.a.text.split()[-1])  # -1 as last index which is price
            # print(card.h5) card card.h2 card.h5.text card.a.text
