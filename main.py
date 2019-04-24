import discord
import env
import lib

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as...')
    print('user name: ' + client.user.name)
    print('user id: ' + str(client.user.id))
    print('------')

@client.event
async def on_message(message):
    if client.user == message.author:
        return

    await lib.respond_greeting(message)

    await lib.respond_rps(client, message)

client.run(env.DISCORD_TOKEN)