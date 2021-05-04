# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2021-05-02 19:02:37
#  * @modify date 2021-05-02 19:02:37
#  * @desc [bot discord]
#  */

import discord
import os
import requests
import json
import random

from datetime import date
from dotenv import load_dotenv
from discord.ext import tasks

client = discord.Client()
today = date.today()

load_dotenv('.env')

sad_words = ["triste", "accablé", "découragé", "malheureux",
             "douloureux", "cruel", "pénible", "mélancolique", "morose"]

encouragements = ["Cheer up !", "Accroche toi !",
                  "Tu est une bonne personne ! ", "Courage !", "Ne perd pas espoir tu es le meilleur !"]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    test.start()


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    msg = message.content

    if msg.startswith('!quote'):
        quote = get_quote()
        await message.channel.send(quote)

    elif any(word in msg for word in sad_words):
        send_msg = '{0.author.mention}'.format(
            message) + ' ' + random.choice(encouragements)
        # await message.channel.send(random.choice(encouragements))
        await message.channel.send(send_msg)

    elif msg.startswith('!bitch'):
        await message.channel.send(message.author.name + ' You are a bitch !')

# 1440 one day in minutes
@tasks.loop(minutes=120)
async def test():
    # channel = client.get_channel(839037327098773505)
    channel = client.get_channel(838587960541970483)
    quote = get_quote()
    date = '**' + today.strftime("%B %d, %Y") + '**'
    welcome = 'Today we are the: ' + \
        date + ' ☕️ Welcome to your daily quote'
    block_quote = welcome + ': \n> {}'.format(quote)
    # await channel.send(welcome + '\n' + '_' + quote + '_')
    await channel.send(block_quote)

client.run(os.getenv('TOKENBOTTEST'))
