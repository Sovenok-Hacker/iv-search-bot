from bs4 import BeautifulSoup as bs
import requests, telebot
bot = telebot.TeleBot('5037312316:AAGMy-OY9B1LAfBII6ER4hFzqjAVYs0Tg1A')
def search(q):
    url = f'''https://invidious.snopyta.org/search?q={'+'.join(q.split(' '))}'''
    data = requests.get(url).content.decode('utf-8')
    links = []
    soup = bs(data, 'lxml')
    videos = soup.find_all('a', {'style': 'width:100%'})
    for video in videos:
        links.append('https://invidious.snopyta.org' + video.get('href'))
    return links

@bot.message_handler(content_types=['text'])
def handle(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Welcome to Invidious Search Bot by Sovenok-Hacker!")
    else:
        try:
            for link in search(message.text):
                bot.send_message(message.from_user.id, link)
        except:
            try:
                bot.send_message(message.from_user.id, 'Error')
            except:
                pass
bot.polling()
