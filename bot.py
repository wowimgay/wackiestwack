import discord
from discord.ext import commands
import asyncio

TOKEN = 'NTIxNzU1NjUzNzE1MjYzNTAw.DvHV-A.nKerfcc06WvAkTAMe2amfYCIBM8'#bot token

client = commands.Bot(command_prefix = "£")

modLog = ""
pengList = ""
pengList = list(pengList)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Collecting the big waifus"))
    print("Ready for SAUCE")#prepping itself

@client.event
async def on_message(message):
    content = message.content
    author = message.author
    channel = message.channel
    wack = str(content)
    print(author)
    print(str(author))
    if str(author) in "Mudamaid4#1070":
        if "high school dxd" in wack.lower():
            await client.send_message(channel, "Claim for ALEEEEEEEEEXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    await client.process_commands(message)

@client.command()
async def modlog(message):
    global modLog
    modLog = message.channel
    await client.process_commands(message)

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
    global modLog
    author = message.author
    content = message.content
    wack = str(content)
    if wack.lower() in "gay":
        await client.send_message(modLog, "{}: {}".format(author, content))
    await client.process_commands(message)
'''
'''
@client.event
async def on_message(message):
    author = message.author
    content = message.content
    wack = list(content)
    alsoWack = "-"
    print(wack)
    await client.process_commands(message)
    for i in range(len(wack)):
        if i % 2 == 0:
            wack[i] = wack[i].upper()
        else:
            wack[i] = wack[i].lower()
    wackFin = alsoWack.join(wack)
    print(wackFin)
'''
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
    await client.process_commands(message)
'''
client.run(TOKEN)
