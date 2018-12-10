import discord
from discord.ext import commands

TOKEN = 'NTIxNzU1NjUzNzE1MjYzNTAw.DvBVPQ.wUha3dSR86pZkMDh3apW_jMEWD8'#bot token

client = commands.Bot(command_prefix = "£")

pengList = ""
pengList = list(pengList)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Collecting the big waifus"))
    print("Ready for SAUCE")#prepping itself

@client.command()
async def status(*args):
    status = args
    await client.change_presence(game=discord.Game(name = status))

@client.command()
async def ping():
    await client.say("Pong!")

@client.command()
async def lambsauce():
    await client.say("WHERE'S THE LAMB SAUCE?")

@client.command()
async def echo(*args):
    output = ""
    for word in args:
        output += word
        output += " "
    await client.say(output)

@client.command()
async def w(*args):
    global pengList
    pengArgs = ""
    for word in args:
        pengArgs = "".join(args)
    pengList.append(pengArgs)

@client.command()
async def r():
    global pengList

    await client.say(pengList)


'''
@client.event
async def on_message(message):
    author = message.author #stores author
    content = message.content #stores content
    print("{}: {}".format(author, content))

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, "{}: {}".format(author, content))
'''
client.run(TOKEN)
