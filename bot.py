import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} is Online')

@bot.command()
async def hi(ctx):
    #print("Working..")
    await ctx.send('Hi...')

@bot.command()
async def ty(ctx):
    await ctx.send("Thank you!")


bot.run("MTE0NDIyNzU2MTM3MTYxOTM0OA.GfviSN.fR-DFhU7ctGMzRf4QQZC48_r3MdnOIvtIvVRWc")

