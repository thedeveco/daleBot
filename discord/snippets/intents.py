# Create a new bot instance with a specified command prefix
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)
