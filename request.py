import os
import requests
from bs4 import BeautifulSoup

from cookies import cookies
from dotenv import load_dotenv

load_dotenv()

user_id = os.getenv("CODEUR_USER_ID")
url = f'https://www.codeur.com/users/{user_id}/messages'

def get_messages():
    response = requests.get(url, cookies=cookies)
    print(url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title")
        if 'Messagerie' in title.text:
            messages = soup.find_all("div", class_="message")
            formated_messages = []
            for message in messages:
                content_raw = message.find("div", class_="message-content")
                offer_link = message.find("a", class_="offer-link")['href']
                header = content_raw.find("p", class_="font-medium")
                author = header.text.split('  •  ')[0]
                title = header.text.split('  •  ')[1]
                message = content_raw.find("p", class_="message-preview").text
                message_obj = {'author': author, 'title': title, 'content': message, 'offer_link': offer_link}
                formated_messages.append(message_obj)

            formated_messages[0]['written_by_me'] = written_by_me(formated_messages[0]['offer_link'])
            return formated_messages

        else:
            print('Error while logging in')
            return 'Error while logging in'


def written_by_me(offer_link):
    url_base = 'https://www.codeur.com'
    url = url_base + offer_link
    response = requests.get(url, cookies=cookies)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title")
        if 'Messages' in title.text:
            comments = soup.find_all("div", class_="comment")
            comment = comments[len(comments) - 1]
            print(comment)
            author = comment.find("span", class_="font-bold").text
            return author == 'Moi'
