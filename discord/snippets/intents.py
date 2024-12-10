# Create a new bot instance with a specified command prefix
INTENTS = discord.INTENTS.default()
INTENTS.typing = False
INTENTS.presences = False
INTENTS.members = True
INTENTS.messages = True
INTENTS.guilds = True

bot = commands.Bot(command_prefix='!', intents=INTENTS)
