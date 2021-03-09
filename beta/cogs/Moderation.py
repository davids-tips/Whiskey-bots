import discord
import discord.utils
import discord.ext
from discord.ext import commands
from discord.ext.commands import command, cog
import datetime

bot = commands.Bot(command_prefix="$")

class test(cog):
    def __init__(self, bot):
        self.bot = bot
def setup(bot):
    bot.add_cog(Help(bot))