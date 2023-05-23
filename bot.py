import discord
import responses
import sys
async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        # await message.author.send(response) sends a peronal dm to everyone or just me?
        if is_private:
            await message.author.send(response)  
        else:
            await message.channel.send(response)
            if response == 'Bot Offline':
                sys.exit()


    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA1OTY5MjY4NDI0OTQwMzQ1Mg.GzCLn8.ZbfdvFm3Tf868eN3u7DEugn6zxsFQJzYGFgoAg'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        general_channel = client.get_channel(1059916523042504727)
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
            #await message.channel.send("asdfasdf") sends message in channel

    client.run(TOKEN)