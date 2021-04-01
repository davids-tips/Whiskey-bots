import discord
from discord.ext import commands
def setup(bot):
    bot.add_cog(social(bot))
class social(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('loading social cog')

    @commands.command(name='boop', description='boop someone', alias=['boops', 'Boop', 'Boops'])
    async def boop(self, ctx, user: discord.Member):
            print(f'{ctx.author.name}initiated boop command.')
            await ctx.send(f'*{ctx.author.name} boops {user.display_name} on the nose*')
    @boop.error
    async def boop_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            await ctx.send('There is a missing Argument in the above command call. EX: \n ```$boop {mentionuserhere}```', delete_after=10)
            await ctx.send('`Note these messages will self-destruct in about 10 seconds`', delete_after=10)
            # the 'delete_after=#' is used to clean up the server from error messages after the set amont of time
            print('There is a missing Argument in the above command call. EX: \n $boop {mentionuserhere}')
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...', delete_after=5)
            print('I could not find that member...')
    @commands.command(name="bap", description='bap them on the snout with a newspaper', alias=['smack', 'bad'])
    async def bap(self, ctx, user: discord.Member):
        print(f'bap command initiated by {ctx.author.name}')
        await ctx.send(f'{ctx.author.display_name} baps {user.display_name} on the nose with a rolled up newspaper. \n {user.display_name} you have been a bad boy/girl.')
    @bap.error
    async def bap_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            await ctx.send('There is a missing Argument in the above command call. EX: \n ```$bap {mentionuserhere}```', delete_after=10)
            await ctx.send('`Note these messages will self-destruct in about 10 seconds`', delete_after=10)
    # the 'delete_after=#' is used to clean up the server from error messages after the set ammount of time to prevent clutter
            print('There is a missing Argument in the above command call. EX: \n $bap {mentionuserhere}')
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...', delete_after=5)
        print('I could not find that member...')