# bot.py
import os
import discord
import responses
import datetime
import asyncio
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()


async def send_msg(msg, username, user_msg):
    try:
        response = responses.get_response(user_msg, username)
        await msg.channel.send(response)
    except Exception as e :
        print(e)


def run_bot():
    TOKEN = os.environ.get('BOT_TOKEN')
    
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    intents.message_content = True

    client = commands.Bot(command_prefix='.', intents=intents)
    

            ###     for schedule msg

    # async def daily_msg():
    #     while True :
    #         now = datetime.datetime.now()
    #         print(now)
    #         await asyncio.sleep(3)
    #         channel = client.get_channel(1148176837604802560)
    #         await channel.send('working...')
    
    @client.event
    async def on_ready():
        print(f'{client.user.name} is Online')
        
            ### for schedule msg 

        # await daily_msg()



    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return
        
        username = str(msg.author)
        user_msg = str(msg.content)
        channel = str(msg.channel)


        if user_msg[0] == '.':
            user_msg = user_msg[1:]
        else:
            return

        if user_msg == 'report':
            file_path = os.path.dirname(__file__) + '\\bot.py'
            file = discord.File(file_path)
            await msg.channel.send(file=file)
            return
        
        await send_msg(msg, username, user_msg)

    client.run(TOKEN)
