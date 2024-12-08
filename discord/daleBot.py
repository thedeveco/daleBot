#!/usr/bin/env python3
import discord
from discord.ext import commands
import os

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

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

# Error handling
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send("You don't have permission to use this command!")
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("Command not found. Use !help to see available commands.")

# Run the bot
def main():
    # Replace 'YOUR_TOKEN_HERE' with your bot's token
    TOKEN = os.getenv('KATERI_DISCORD_TOKEN', "Default")
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
