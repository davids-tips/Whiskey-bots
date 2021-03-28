# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
# NOTICE PULL THE LATEST COMMIT FROM GITHUB THIS INSTANCE WAS FOR TESTING CHANNEL CREATION
import discord
from discord.ext import commands
import datetime
from cogs.social import *
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

class MyCog(commands.Cog):  # All cogs must inherit from commands.Cog
    """A simple, basic cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

bot.load_extension("social")  # <--- This single line of code to be precise
def setup(bot: commands.Bot):
    bot.add_cog(social(bot))


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
#avoid scrolling down to prevent token leak







bot.run("Nzk4MjAxODM4ODY3NTc4OTQw.X_xlZA.7KPYmPbWKWOIpccbUY9ikaJs4B8")
