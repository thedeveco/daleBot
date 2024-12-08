#!/usr/bin/env python3
# This example requires the 'message_content' intent.
import discord
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('KATERI_DISCORD_BOT_TOKEN')

class MyClient(discord.Client):
  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)
