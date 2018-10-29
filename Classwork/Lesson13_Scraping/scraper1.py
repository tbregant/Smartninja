import requests
from BeautifulSoup import BeautifulSoup
import csv
import time

url = "https://scrapebook22.appspot.com/"

r = requests.get(url)
time.sleep(2)

soup = BeautifulSoup(r.text)

# print soup.head.title.string


all_emails = []
for link in soup.findAll("a"):
    if "person" in link["href"]:
        print link

        detail_r = requests.get(url+link["href"])
        time.sleep(2)
        print detail_r.text
        details_soup = BeautifulSoup(detail_r.text)

        email = details_soup.find("span", attrs={"class": "email"})

        for naslov in details_soup.findAll("h1"):
            if "Hello, ninja!" not in naslov:
                name = naslov.string

        all_emails.append([name, email.string])


with open("output.csv", "wb") as out_csv:
    writer = csv.writer(out_csv, delimiter=";")

    for line in all_emails:
        writer.writerow(line)