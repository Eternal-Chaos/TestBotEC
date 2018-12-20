
'''
Originally Base-Derived
Owner - EC#7115, Liam#7777, Quanta#5556
'''
import os
import discord
from discord.ext import commands
from ext.context import CustomContext
import psutil
import re
import json
from collections import defaultdict
import datetime
import aiohttp
import requests

class jakeBot(commands.Bot):
    '''
    A Bot Made by ~ EC#1269 Liam#3273 and Quanta#5556
    '''
    mentions_transforms = {
          '@everyone': '@\u200beveryone',
          '@here': '@\u200bhere'
    }
    mention_pattern = re.compile('|'.join(mentions_transforms.keys()))

    def __init__(self, **attrs):
        super().__init__(command_prefix = self.get_pre)
        self.session = aiohttp.ClientSession(loop = self.loop)
        self._extentions = [x.replace('.py', '') for x in os.listdir('cogs') if x.endswith('.py')]
        self.process = psutil.Process()
        self.load_extensions()
   
    def load_extensions(self, cogs = None, path = 'cogs.'):
        '''Loading the Extentions ;)'''
        for extension in cogs or self._extentions:
            try:
                self.load_extension('{0}{1}'.format(path, extension))
                print('Loaded Extention: {}'.format(extension))
            except Exception as e:
                print('CannotLoad: {0}\n'
                      '{type(e).__name__}: {1}'.format(extension, e))

    @staticmethod
    async def get_pre(bot, message):
        '''GET THE PREFIX'''
        with open('data/config.json') as f:
            prefix = json.load(f).get('PREFIX') or "<@467973617536335872> "
        return os.environ.get('PREFIX') or prefix or 'r. '

    def restart(self):
        os.exev(sys.executable, ['python'] + sys.argv)


    @classmethod
    def init(bot, token = None):
        '''RUN THE BOT'''
        jakebot = bot()
        with open('data/config.json') as f:
            config = json.load(f)
            if config["TOKEN"] == "your_token_here":
                token = os.environ.get("TOKEN")
                token = str(token)
            else:
                token = config["TOKEN"]
        try:
            jakebot.run(token, bot = True, reconnect = True)
        except Exception as e:
            print(e)

    async def on_connect(self):
        print('-------------\n'+ 'Jake Logged in!')

    async def on_ready(self):
        '''SET THE UPTIME'''
        self.uptime = datetime.datetime.utcnow()
        server = str(+len(self.guilds))
        await self.change_presence(activity=discord.Game(name="jake help (' O '   ) O:"))

    async def process_commands(self, message):
        '''Utilize the CustomContext subclass'''
        ctx = await self.get_context(message, cls = CustomContext)
        if ctx.command is None:
            return
        await self.invoke(ctx)
    
    async def on_message(self, message):
        count = 0
        if message.author.id == self.user.id:
            return
        if message.author.id == 500937654381314048 and message.content.lower() == "lewl":
            count += 1
            await message.delete()
            await message.channel.send("Careful bon EC is watching", delete_after = 3)
        if message.author.id == 500937654381314048 and message.content.lower() == "xd":
            count += 1
            await message.delete()
            await message.channel.send("Careful bon EC is watching", delete_after = 3)
        if message.author.id == 500937654381314048 and message.content.lower() == "lelw":
            count += 1
            await message.delete()
            await message.channel.send("Careful bon EC is watching", delete_after = 3)
        if count == 5:
            await discord.Object(500937654381314048).kick()
        await self.process_commands(message)

    def get_server(self, id):
        return discord.utils.get(self.guilds, id = id)

if __name__ == '__main__':
    jakeBot.init()
