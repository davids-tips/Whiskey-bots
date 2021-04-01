import discord
from discord.ext import commands
def setup(bot):
    bot.add_cog(chat_room_managment(bot))
class chat_room_managment(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print('loading chat_room_managment cog')

    @commands.command(name='1o1', description='creates 1 on 1 room')
    @commands.has_permissions(manage_roles=True)
    @commands.command(description="creates 1 on 1 room")
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
