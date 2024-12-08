#!/usr/bin/env python3
import discord
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('KATERI_DISCORD_TOKEN')

# Create a new bot client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def on_ready():
  print(f'{client.user} has connected to Discord!')

async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

# Run the bot
client.run(TOKEN)
