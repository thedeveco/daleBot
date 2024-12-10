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
