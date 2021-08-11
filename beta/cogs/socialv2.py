import discord
from discord.ext import commands
from cogs.listvar import scritch
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

ref = db.reference("/")

def setup(bot):
    bot.add_cog(socialv2(bot))

class socialv2(commands.Cog):
    """A couple of simple commands."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('loading socialv2 cog')
