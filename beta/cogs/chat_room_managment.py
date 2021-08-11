import discord
from discord.ext import commands
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
def setup(bot):
    bot.add_cog(chat_room_managment(bot))
class chat_room_managment(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('loading chat_room_managment cog')

    @commands.command(name='1o1', description='creates 1 on 1 room')
    @commands.has_permissions(manage_roles=True)
    async def room(self, ctx, arg, user1: discord.Member, user2: discord.Member, channel_name):
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
    """ @pcr.error
    async def pcr_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('There is a missing Argument in the above command call. EX: \n ```$1o1 <arg> <user1> <user2> <channel_name>```', delete_after=10)
            await ctx.send('`Note these messages will self-destruct in about 10 seconds`', delete_after=10)
            # the 'delete_after=#' is used to clean up the server from error messages after the set amont of time
            print('There is a missing Argument in the above command call. EX: \n ````$1o1 <arg> <user1> <user2> <channel_name>```')
        if isinstance(error, commands.BadArgument):
            await ctx.send('I could not find that member...', delete_after=5)
            print('I could not find that member...')"""
        
    """     ############### COmmented out until further notice due to not knowing how to delete channels using the name #########################
    @commands.command(name='1o1RM', description='removes 1 on 1 room')
    @commands.has_permissions(manage_roles=True)
    async def roomRM(self, ctx, arg, channel_name):
        role_object = discord.utils.get(ctx.message.guild.roles, name=arg)
        #delete role
        await role_object.delete()
        await ctx.send("role deleted sucessfully", delete_after=5)

        await ctx.send("channel deleted sucessfully", delete_after=5)"""