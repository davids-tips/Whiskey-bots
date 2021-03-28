import discord
from discord.ext import commands
import datetime


class MyCog(commands.Cog):  # All cogs must inherit from commands.Cog
    """A simple, basic cog."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    print("cog workest?")

    bot = commands.Bot(command_prefix="$")


    @bot.command(name='boop', description='boop someone', aliases=['boops', 'Boop', 'Boops'])
    async def boop(self,ctx, user: discord.Member):
        print('debug')
        await ctx.send(f'*{ctx.author.name} boops {user.display_name} on the nose*')


    @boop.error
    async def boop_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                'There is a missing Argument in the above command call. EX: \n ```$boop {mentionuserhere}```',
                delete_after=10)
            await ctx.send('`Note these messages will self-destruct in about 10 seconds`', delete_after=10)
            # the 'delete_after=#' is used to clean up the server from error messages after the set amont of time
            print('There is a missing Argument in the above command call. EX: \n $boop {mentionuserhere}')
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...', delete_after=5)
            print('I could not find that member...')


def setup(bot: commands.Bot):
    bot.add_cog(MyCog(bot))
