import discord
import env
import lib

client = discord.Client()
game_rps = lib.GameRPS()

active_ch = None

@client.event
async def on_ready():
    global active_ch
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
        pass
        # await active_ch.send(env.get_hello_message())

@client.event
async def on_message(message):
    if client.user == message.author:
        return
    if active_ch == None or message.channel != active_ch:
        return

    await lib.respond_greeting(message)

    await lib.respond_stats(message)

    await lib.respond_allstats(message)

    await game_rps.process_message(client, message)

client.run(env.DISCORD_TOKEN)