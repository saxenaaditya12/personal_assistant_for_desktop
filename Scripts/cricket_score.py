import requests
from bs4 import BeautifulSoup
import the_voice


def score():
    try:
        print('=====================')
        the_voice.say_and_print('Live Cricket Matches:')
        url = "http://static.cricinfo.com/rss/livescores.xml"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        i = 1
        for item in soup.findAll('item'):
            temp = item.find('description').text
            print(str(i) + '. ' + temp)
            temp = temp.replace(" v ", " versus ")
            temp = temp.replace(" *", "")
            temp = temp.replace("/", " for ")
            temp = temp.replace("T20", "T 20")
            the_voice.say(temp)
            i = i + 1

        links = []
        for link in soup.findAll('item'):
            links.append(link.find('guid').text)
    except Exception as e:
        print(e)
        print("* Error in showing cricket score *")
