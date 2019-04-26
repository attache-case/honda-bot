import discord
import env
import lib

client = discord.Client()

active_ch = None

@client.event
async def on_ready():
    print('Logged in as...')
    print('user name: ' + client.user.name)
    print('user id: ' + str(client.user.id))
    print('------')
    # find channel to respond
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.name == env.ACTIVE_CHANNEL_NAME:
                active_ch = channel
    if active_ch != None:
        await active_ch.send(env.HELLO_MESSAGE)

@client.event
async def on_message(message):
    if client.user == message.author:
        return
    if active_ch == None or message.channel != active_ch:
        return

    await lib.respond_greeting(message)

    await lib.respond_rps(client, message)

client.run(env.DISCORD_TOKEN)