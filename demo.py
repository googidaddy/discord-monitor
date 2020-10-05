import requests
from dhooks import Webhook, Embed
import json
import time
import discord
import random
hook = Webhook('')  # webhook URL

now = []

last = []


url = ''  # url

# send embed to your webhook


def send_webhook(embed):
    hook.send(embed=embed)


def monitor():
    headers = {
        # todo
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    while response.status_code != 200:
        response = requests.get(url, headers=headers)
    j = json.loads(response.text)
    if len(j[0]['embeds']) > 0:
        e = discord.Embed.from_dict(j[0]['embeds'][0])
        return e, j[0]['timestamp']
    else:
        print('error')
        return 1


def start():
    print('mornitoring!！', time.ctime())
    last = monitor()
    while True:
        time.sleep(15)
        print('monitoring again!!!', time.ctime())
        now = monitor()
        if last != 1:
            if now != 1:
                if now[1] != last[1]:
                    send_webhook(now[0])
        last = now
        print('monitoring', time.ctime())


try:
    start()
except Exception as e:
    print(e)
    time.sleep(60)
    start()
