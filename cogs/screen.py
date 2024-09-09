import disnake
from pymongo import MongoClient, errors
from disnake.ext import commands
from datetime import datetime
import os
import asyncio
import time
import mss
import mss.tools


class ScreenzCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.id = 771825925993136148

    @commands.slash_command(name='screen', dm_permission=True)
    async def screen(self, inter: disnake.ApplicationCommandInteraction):
        if inter.author.id == self.id:
            now = datetime.now()
            tstamp = int(now.timestamp())
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

            with mss.mss() as sct:
                screenshot = sct.shot(output=f"screenshots/screenshot_{timestamp}.png")

            await inter.send(f'Screenshot от <t:{tstamp}>',
                             file=disnake.File(f'screenshots/screenshot_{timestamp}.png'))
            os.remove(f'screenshots/screenshot_{timestamp}.png')
        else:
            await inter.send('Иди нахуй!')


def setup(bot):
    bot.add_cog(ScreenzCog(bot))
    print("Screen Cog is ready!")
