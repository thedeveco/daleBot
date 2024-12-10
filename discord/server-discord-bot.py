#!/usr/bin/env python3
import discord
from discord.ext import commands
from os import getenv

#
#   Get the bot's token from the environment
#
TOKEN = getenv('DALEBOT_DISCORD_TOKEN', "Default")
print(f"TOKEN = '{TOKEN}'")

#
#   Servers and Channels
#
SERVER_ID1 = 1173307855890305125        #   Hybrid Robotics Community

CHANNEL_ID1_1 = 1315854871731245106     #   #bot-commands
CHANNEL_ID1_2 = 1187441927860256918     #   #rules
CHANNEL_ID1_3 = 1187804254321250356     #   #general-chat
CHANNEL_ID1_4 = 1187774067365916824     #   #introductions
CHANNEL_ID1_5 = 1173307856590737441     #   #robotics-chat
CHANNEL_ID1_6 = 1199965095673991248     #   #smart-home
CHANNEL_ID1_7 = 1208144057457709086     #   #our-animal-companions

SERVER_ID2 = 620838168794497044         #   DevEco

CHANNEL_ID2_1 = 620838168794497046      #   #chat

#   Create a new bot instance with a specified command prefix
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    """Event triggered when the bot is ready"""
    print(f"Logged in as {bot.user}")

#   Command to make the bot say hello
@bot.command(name="hello")
async def hello(ctx):
    """Says hello back to the user"""
    await ctx.send("Hello!")

#   Command to tell the user about the bot's help command
#@bot.command(name="help")
#async def help(ctx):
#    """Lists available commands"""
#    embed = discord.Embed(title=f"Help for {ctx.author.name}!", description="Available commands:", color=0x00ff00)
#    embed.add_field(name="!hello", value="Say hello back to the user")
#    await ctx.send(embed=embed)

#   Command to make the bot say goodbye
@bot.command(name="bye")
async def goodbye(ctx):
    """Says bye and logs off"""
    await ctx.send("Goodbye!")
    await bot.close()

#
# Function to make the bot join a server
#
def join_server(server_id, channel_id):
    #
    # Create a new session with the Discord API
    #
    session = discord.client()

    # Fetch the server
    server = session.get_guild(server_id)

    if not server:
        print(f'Server {server_id} not found')
        return

    # Join the channel
    channel = server.get_channel(channel_id)

    if not channel:
        print(f'Channel {channel_id} not found in server {server_id}')
        return

    # Add the bot to the channel's permissions
    channel.set_permissions(bot, send_messages=True)
    channel.set_permissions(bot, add_reactions=True)

join_server(SERVER_ID1, CHANNEL_ID1_1)

# Run the bot with your token
bot.run(TOKEN)
