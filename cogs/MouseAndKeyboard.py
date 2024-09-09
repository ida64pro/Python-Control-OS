import disnake
from pymongo import MongoClient, errors
from disnake.ext import commands
from datetime import datetime
import os
import asyncio
import time
from pynput import mouse
from pynput.mouse import Controller, Button, Listener
import pyautogui



class MouseCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.id = 771825925993136148

    @commands.slash_command(name='mouse', dm_permission=True)
    async def mouse(self, inter: disnake.ApplicationCommandInteraction, x: int, y: int):
        if inter.author.id == self.id:
            try:
                mousez = Controller()

                mousez.position = (x, y)

                await asyncio.sleep(1)

                mousez.press(Button.left)

                await asyncio.sleep(0.1)

                mousez.release(Button.left)
                await inter.send(f'Левая кнопка была нажата в ({x}, {y})')
            except Exception as e:
                await inter.send(f'Не сработало ({e})')
        else:
            await inter.send('Иди нахуй!')

    @commands.slash_command(name='keyboard', dm_permission=True)
    async def keyboard(self, inter: disnake.ApplicationCommandInteraction, текст: str):
        if inter.author.id == self.id:
            try:
                await asyncio.sleep(2)
                pyautogui.write(текст, interval=0.1)
                pyautogui.press('enter')
            except Exception as e:
                await inter.send(f'Не сработало ({e})')
        else:
            await inter.send('Иди нахуй!')

def setup(bot):
    bot.add_cog(MouseCog(bot))
    print("Mouse Cog is ready!")