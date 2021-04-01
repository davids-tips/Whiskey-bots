# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
# NOTICE PULL THE LATEST COMMIT FROM GITHUB THIS INSTANCE WAS FOR TESTING CHANNEL CREATION
import discord
from discord.ext import commands
import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

bot = commands.Bot(command_prefix="$")
ct = datetime.datetime.now()
guild_ids = []


@bot.event
async def on_ready(autopost=True, case_insensitive=True):
    print('Ready!')


# try:
#    bot.load_extension("cogs.mod")  # Instead of a file-like or path-like string, you put `directory.file`, without a file extension.
# except:
#    print("Failed to load moderation:")
# traceback.print_exc()


# command archived for future work on it
# @bot.command(name='cmd1', description='remote owo command from other bot')
# async def name(ctx):
#    print('recieved')
#    await ctx.message.delete()
#    await ctx.send('test message')
# end
# Import Cogs

# Add Cogs
bot.load_extension('cogs.social')
bot.load_extension('cogs.chat_room_managment')




# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
#avoid scrolling down to prevent token leak







bot.run(os.getenv('wbbeta'))
