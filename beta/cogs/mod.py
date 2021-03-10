import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="$")
class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
@commands.Cog.listener()
async def on_ready(self):
  print('started')
    @commands.command()
    async def foo(self, ctx):
        await ctx.send("Foo!")
        
    @commands.command(name='testing', description='test command')
async def name(ctx):
    await ctx.send('hello there')
        
def setup(bot):
    bot.add_cog(Moderation(bot))