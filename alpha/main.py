import discord
from discord.utils import get
import random
# import ctx
import http.server
import http.client
import email.message
# from replit import db
import logging
import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
print('import complete!')
print('setting up logging')
# logging for errors and other items
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
# end of logging
print('logging setup complete')

# creating python file to the cards against furries script

client = discord.Client()
PrefixHelp = 'My Prefix is $\n'
'Please use that with commands Thanks. - Whiskey the Developer'


@client.event
async def on_connect():
    print('Connecting To Discord API...\n'
          'Please Wait...\n'
          )


@client.event
async def on_ready():
    print('Hello Master *nuzles*\n'
          'logged in and ready to accept commands\n\n'
          'Logged in as [{0.user}]\n'.format(client))
    game = discord.Game("I am the floofy foxo🦊🦊")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print("debug: msg recieved")
    if message.content.startswith("OwO") or message.content.startswith("owo"):
        await message.channel.send("$cmd1")
        print('Owo ran')

    if message.content.startswith("nuz"):
        await message.channel.send("***nuzzles***")
        await message.channel.send(
            "https://cdn.discordapp.com/attachments/798736137317253170/811095654008487946/DerpysFavs_58.jpeg")

    if message.content.startswith("$slave"):
        await message.channel.send("!clear 20")
    if message.content.startswith("$delete"):
        await message.delete()

        # below is code for sending animated emojis
    if message.content.startswith(":screamtoad:"):
        await message.delete()
        await message.channel.send("<a:scream:802746690993913856>")
        # remove the "a" from the line above for a non animated emoji and set the id to the correct id
    if message.content.startswith("dndgroup"):
        await message.channel.send(
            "<:thomas:802907659153834024><:fred:802907477486075934><:noah:802912601947766814><:david:802914481000677376><:aidan:802929427746914324><:gage:805583021100105728>")
    if message.content.startswith('$online?'):
        await message.channel.send('Online! Hello Master!')

    if message.content.startswith('$Hello'):
        await message.channel.send('Hello')

    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    elif message.content.startswith('$Setting'):
        await message.channel.send('ComingSoon')

    elif message.content.startswith('WhiskeyBot'):
        await message.channel.send(PrefixHelp)
    elif message.content.startswith('$Test'):
        await message.channel.send('Bot Online!')
    elif message.content.startswith('$Boop'):

        boop = [
            "Cute Boops", "Adorable Foxo~", "Hehehe~", "OwO", "*Blushes*"]

        await message.channel.send(random.choice(boop))
    elif message.content.startswith('$Morning'):
        await message.channel.send('***Good Morning, Master!***')
    elif message.content.startswith('$Evening'):
        await message.channel.send('***Good Evening, Master!***')


client.run(os.getenv('wbalpha'))
