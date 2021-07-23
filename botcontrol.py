# bot.py
from asyncio.windows_events import NULL
import os
import random
import subprocess
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')



@bot.command(name='execute', help='executes a command')
async def execution(ctx, argument):   

    response = subprocess.run(f"{argument}", shell=True, text=True, capture_output=True)

    await ctx.send(response.stdout)

bot.run(TOKEN)