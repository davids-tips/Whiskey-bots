import discord
import discord.utils
import discord.ext
from discord.ext import commands
import datetime
import os
import random
print('import complete!')
print('now reinstalling discord slash commands. This is REQUIRED due to how repl.it handles this instalation.')
stream = os.popen('pip install -U discord-py-slash-command')
output = stream.read()
output
print('install completed now importing...')
from discord_slash import SlashCommand
print('import complete. Now connecting to discord.api')

bot = commands.Bot(command_prefix="$")
ct = datetime.datetime.now()
slash = SlashCommand(bot, sync_commands=True, delete_from_unused_guilds=True) # Declares slash commands through the client.

guild_id = [] # Put your server ID in this array.

@bot.event
async def on_ready(autopost=True, case_insensitive=True):
    print('Ready!')
    print('connected to discord api')
    print (f'connected')


#attemptng to use slassh commands
@slash.slash(name="ping")
async def _slash(ctx):  # Normal usage.
    await ctx.send(content=f"Pong! (`{round(bot.latency*1000)}`ms)")


@slash.slash(name="pick")
async def _pick(ctx, choice1, choice2):  #  Command with 1 or more args.
    await ctx.send(content=str(random.choice([choice1, choice2])))


@slash.slash(name="IOwO", description="Get OwO'd")
async def OwO(ctx):
    await ctx.send("OwO Whats This?")
    if ctx.channel.is_nsfw():
        await ctx.send("*Notices Buldge*")


@slash.slash(name="IUwU", description="Get UwU'd")
async def UwU(ctx):
  if ctx.channel.is_nsfw():
    await ctx.send("UwU Can i help you with your buldgy-wulgy")
    await ctx.send("*Puts Paws on buldge and sniffs it*")
  else:
    await ctx.send("Channel is required to be nsfw to run this command. Sorry :-/")
    #end of attempt
@slash.slash(name='joke', description='Get a crappy joke', guild_id=798726719573065749)
async def joke(ctx):
  jokes=['test joke']
  await ctx.send(f'Enjoy the joke {message.author.nick}\n',jokes)

bot.run('ODE0ODY5MzAwMjY2Nzk1MDI4.YDkILA.R7Rq7rwd0DSS6RRo6k51Hmad6Sw')
