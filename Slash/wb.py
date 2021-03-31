import discord
import discord.utils
import discord.ext
from discord.ext import commands
import datetime
import os
import random
# print('import complete!')
# print('now reinstalling discord slash commands. This is REQUIRED due to how repl.it handles this instalation.')
# stream = os.popen('pip install -U discord-py-slash-command')
# output = stream.read()
# output
# print('install completed now importing...')
from discord_slash import SlashCommand

print('import complete. Now connecting to discord.api')

bot = commands.Bot(command_prefix="=")
ct = datetime.datetime.now()
slash = SlashCommand(bot, sync_commands=True,
                     delete_from_unused_guilds=True)  # Declares slash commands through the client.

guild_ids = [798726719573065749]  # Put your server ID in this array.


@bot.event
async def on_ready(autopost=True, case_insensitive=True):
    print('Ready!')
    print('connected to discord api')
    print(f'connected')


# attemptng to use slassh commands
@slash.slash(name="ping")
async def _slash(ctx):  # Normal usage.
    await ctx.send(content=f"Pong! (`{round(bot.latency * 1000)}`ms)")


@slash.slash(name="pick")
async def _pick(ctx, choice1, choice2):  # Command with 1 or more args.
    await ctx.send(content=str(random.choice([choice1, choice2])))


@slash.slash(name="OwO", description="Get OwO'd")
async def OwO(ctx):
    await ctx.send("OwO Whats This?")
    if ctx.channel.is_nsfw():
        await ctx.send("*Notices Buldge*")


@slash.slash(name="UwU", description="Get UwU'd")
async def UwU(ctx):
    if ctx.channel.is_nsfw():
        await ctx.send("UwU Can i help you with your buldgy-wulgy")
        await ctx.send("*Puts Paws on buldge and sniffs it*")
    else:
        await ctx.send("Channel is required to be nsfw to run this command. Sorry :-/")
        # end of attempt


@slash.slash(name='joke', description='Get a crappy joke', guild_ids=[798726719573065749])
async def joke(ctx):
    await ctx.respond()
    jokes = ['I tried to grab fog but I mist',
             'Go to measure 8\nYou know the one before 9.',
             '*siren noise* Nepper: Oh no I knew they would find me',
             'Lets take a look at 11-11 oh wait I said that backwards 11-11',
             'Have you ever slid down a metal slide in shorts and burnt your butt?\n Well thats your butt after eating taco bell',
             'Tree paper come get yourself some tree paper']
    print(f'Enjoy the joke {ctx.author.display_name}\n' + random.choice(jokes))
    await ctx.send(f'Enjoy the joke {ctx.author.display_name}\n' + "***" + random.choice(jokes) + "***")


@slash.slash(name='1o1room', description='create a 1on1 privite nsfw chatroom')
async def name(ctx, RoleName, user1: discord.Member, user2: discord.Member, channel_name):
    role = await ctx.guild.create_role(name=RoleName)
    message2 = []
    await ctx.send(RoleName)
    print("arg= ", RoleName)
    # role = discord.utils.get(ctx.guild.roles, name=arg)
    await user1.add_roles(role)
    print("added role:[", RoleName, '] to user1')
    await user2.add_roles(role)
    print("added role:[", RoleName, '] to user2')
    await ctx.send('added roles successfully')

    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
        role: discord.PermissionOverwrite(read_messages=True)
    }
    print('overwrites set sucessfully')
    channel = await ctx.guild.create_text_channel(channel_name, overwrites=overwrites, nsfw=True, catergory='PRIVITE')
    print('channel created sucessfully')


bot.run('')
