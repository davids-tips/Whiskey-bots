@commands.Cog.listener()
async def on_ready(self):
  print('started')
    @commands.command()
    async def foo(self, ctx):
        await ctx.send("Foo!")
        
    @commands.command(name='testing', description='test command')
async def name(ctx):
    await ctx.send('hello there')