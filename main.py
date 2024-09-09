import disnake
from pymongo import MongoClient, errors
from disnake.ext import commands
from datetime import datetime
import os
import asyncio
import time

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all(), reload=True)
bot.member_cache_flags = disnake.MemberCacheFlags.all()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    activity = disnake.Game(name="skew PC")
    await bot.change_presence(status=disnake.Status.online, activity=activity)


for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run("YOUR TOKEN")
