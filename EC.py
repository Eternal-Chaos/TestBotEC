import os
import discord
from aiohttp import ClientSession
from discord.ext import commands
import codecs
import aiohttp

bot = commands.Bot(
    command_prefix = "*",
    description = "I'm a simple man. I see a command, I call it.")


session = ClientSession(loop = bot.loop)

tokens = os.environ.get("TOKEN")


@bot.command()
async def woosh():
   await bot.say('Woosh Woosh')

@bot.command(pass_context = True)
async def addemoji(ctx, emoji_name, emoji_link = ''):
    msg: discord.Message = ctx.message
    if msg.attachments:
      await ctx.message.delete()
    
@bot.command()
async def _emoji(ctx, *, emoji: str):
    '''send emoji pic'''
    emoji = emoji.split(":")
    emoji_check = self.check_emojis(ctx.bot.emojis, emoji)
    if emoji_check[0]:
        emo = emoji_check[1]
    else:
        emoji = [e.lower() for e in emoji]
        if emoji[0] == "<" or emoji[0] == "":
            emo = discord.utils.find(lambda e: emoji[1] in e.name.lower(), ctx.bot.emojis)
        else:
            emo = discord.utils.find(lambda e: emoji[0] in e.name.lower(), ctx.bot.emojis)
        if emo == None:
            em = discord.Embed(title="None", description="No emoji found.")
            em.color = await ctx.get_dominant_color(ctx.author.avatar_url)
            await ctx.send(embed=em)
            return
    async with ctx.session.get(emo.url) as resp:
        image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.message.delete()
        await ctx.send(file=discord.File(file, 'emote.png')

safe_token = "{}".format(tokens)
bot.run(safe_token)

