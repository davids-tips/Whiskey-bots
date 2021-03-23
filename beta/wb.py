# IMPORT DISCORD.PY. ALLOWS ACCESS TO DISCORD'S API.
# NOTICE PULL THE LATEST COMMIT FROM GITHUB THIS INSTANCE WAS FOR TESTING CHANNEL CREATION
import discord
from discord.ext import commands
import datetime

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
@bot.command(name='boop', description='boop someone', alias=['boops', 'Boop', 'Boops'])
async def boop(ctx, user: discord.Member):
    print('debug')
    await ctx.send(f'*{ctx.author.name} boops {user.display_name} on the nose*')
@boop.error
async def boop_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        await ctx.send('There is a missing Argument in the above command call. EX: \n ```$boop {mentionuserhere}```', delete_after=10)
        await ctx.send('`Note these messages will self-destruct in about 10 seconds`', delete_after=10)
       # the 'delete_after=#' is used to clean up the server from error messages after the set amont of time
        print('There is a missing Argument in the above command call. EX: \n $boop {mentionuserhere}')
    if isinstance(error, commands.BadArgument):
        await ctx.send('I could not find that member...', delete_after=5)
        print('I could not find that member...')

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







bot.run("Nzk4MjAxODM4ODY3NTc4OTQw.X_xlZA.7KPYmPbWKWOIpccbUY9ikaJs4B8")
