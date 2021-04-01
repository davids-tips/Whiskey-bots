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
from cogs.social import *

# Add Cogs
bot.load_extension('cogs.social')



@bot.command(name='1o1', description='creates 1 on 1 room')
@commands.has_permissions(manage_roles=True)
async def name(ctx, arg, user1: discord.Member, user2: discord.Member, channel_name):
    role = await ctx.guild.create_role(name=arg)
    message2 = []
    await ctx.send(arg)
    print("arg= ", arg)
   # role = discord.utils.get(ctx.guild.roles, name=arg)
    await user1.add_roles(role)
    print("added role:[", arg, '] to user1')
    await user2.add_roles(role)
    print("added role:[", arg, '] to user2')
    await ctx.send('added roles sucessfully')

    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
        role: discord.PermissionOverwrite(read_messages=True)
    }
    channel = await ctx.guild.create_text_channel(channel_name, overwrites=overwrites, nsfw=True, catergory='PRIVITE')

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
#avoid scrolling down to prevent token leak







bot.run(os.getenv('wbbeta'))
