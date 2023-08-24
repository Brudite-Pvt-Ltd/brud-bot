# bot.py
import os
import discord
import responses

from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()

async def send_msg(msg, user_msg):
    try:
        response = responses.get_response(user_msg)
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
    
    @client.event
    async def on_ready():
        print(f'{client.user.name} is Online')

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
        
        await send_msg(msg, user_msg)

    client.run(TOKEN)