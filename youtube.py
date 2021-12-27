import os, telebot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
bot = telebot.TeleBot("token_from_tg")
@bot.message_handler(content_types=["text"])
def handle(message):
    if not message.text == "/start":
        q = "+".join(message.text.split(" "))
        firefox = webdriver.Firefox()
        firefox.get("https://invidious.snopyta.org/search?q=" + q)
        i = 1;
        videos = []
        links = []
        while True:
            try:
                xpath = "/html/body/div/div[2]/div[3]/div[" + str(i) + "]/div/a"
                video = firefox.find_element(By.XPATH, xpath)
                videos.append(video)
                i = i + 1
            except:
                break
        for video in videos:
            bot.send_message(message.from_user.id, video.get_attribute("href"))
        firefox.quit()

bot.polling()
