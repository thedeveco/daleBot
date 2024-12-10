# Command: Ping
@bot.command(name='ping')
async def ping(ctx):
  """Responds with the bot's latency"""
  await ctx.send(f'Pong! Latency: {round(bot.latency * 1000)}ms')

# Command: Hello
@bot.command(name='hello')
async def hello(ctx):
  """Greets the user"""
  await ctx.send(f'Hello {ctx.author.name}!')

# Command: Clear messages
@bot.command(name='clear')
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
  """Clears specified number of messages"""
  await ctx.channel.purge(limit=amount + 1)
  await ctx.send(f'Cleared {amount} messages!', delete_after=5)

# Command: Member count
@bot.command(name='members')
async def members(ctx):
  """Shows the server member count"""
  await ctx.send(f'This server has {ctx.guild.member_count} members!')
