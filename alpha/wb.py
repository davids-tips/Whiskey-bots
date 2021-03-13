# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
# NOTICE PULL THE LATEST COMMIT FROM GITHUB THIS INSTANCE WAS FOR TESTING CHANNEL CREATI
import discord
import discord.utils
import discord.ext
from discord.ext import commands
from discord.ext.commands import command, cog
import datetime
bot = commands.Bot(command_prefix="$")
ct = datetime.datetime.now()
client = discord.Client(intents=discord.Intents.all())
guild_ids = []


@bot.event
async def on_ready(autopost=True, case_insensitive=True):
    print('Ready!')
    print(
        'Singular guild ids and the strung of guild ids has been printing. That is the'
        'odd string of numbers you see above\n',
        'End \n Ready for commands')


@bot.command(name='1o1', description='creates 1 on 1 room')
@commands.has_permissions(manage_roles=True)
async def name(ctx, arg, user1: discord.Member, user2: discord.Member):
    await ctx.guild.create_role(arg, reason='Creating 1o1 room for {user1} and {user2}')
    message2 = []
    await ctx.send(arg)
    print("arg=", arg)
    rolename = arg
    print("rolename var= ", rolename)
    # the argument rolenamearg is from my command
    role = discord.utils.get(ctx.guild.roles, name=arg)
    await user1.add_roles(role)
    print("added role:[", rolename, '] to user1')
    message2.append("added role:[", rolename, '] to user1')
    await user2.add_roles(role)
    print("added role:[", rolename, '] to user2')
    message2.append("added role:[", rolename, '] to user2')
    await ctx.send(message2)


# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run("Nzk4MzMxNjgxMDI2NDc0MDA0.X_zeUQ.b39yujyOOHi_ihwowi1u6h3SBPs")