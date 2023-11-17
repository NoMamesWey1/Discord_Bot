import discord
import responses
import sys
#sends message to the channel if it meets something in responses else doesn't respond
async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        if is_private:
            await message.author.send(response)  
        else:
            await message.channel.send(response)
            if response == 'Bot Offline':
                sys.exit()


    except Exception as e:
        print(e)

# connecting bot the server
def run_discord_bot():
    TOKEN = 'YOUR TOKEN'#put ur token in a string
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        general_channel = client.get_channel('YOUR CHANNEL ID')#put as an integer
        await general_channel.send('Bot Online')


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)