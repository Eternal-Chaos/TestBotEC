import discord
import asyncio
from discord.ext import commands
import requests
import aiohttp

class emojis(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(manage_emojis = True)
    async def addemoji(self, ctx, emoji_name, emoji_link = '', *roles : discord.Role):
        """Add an emoji to a server
        __**Parameters**__
        • emoji_name – The emoji name. Must be at least 2 characters
        • emoji_link – The url or attachment of an image to turn into an emoji
        • roles – A list of Roles that can use this emoji (case sensitive). Leave empty to make it available to everyone
        """
        if ctx.message.attachments:
            emoji_link = ctx.message.attachments[0].url
            async with ctx.session.get(emoji_link) as resp:
                image = await resp.read()
        elif emoji_link:
            async with ctx.session.get(emoji_link) as resp:
                image = await resp.read()
        created_emoji = await ctx.guild.create_custom_emoji(name = emoji_name, image = image, roles = [r for r in roles if roles is not None])
        await ctx.send(f"Emoji {created_emoji} created!")
        
    @commands.command(aliases = ["ge"])
    async def getemoji(self, ctx, *, emoji : discord.Emoji):
        await ctx.send(emoji)
        await ctx.message.delete()
    
    @commands.command()
    async def emojiurl(self, ctx, emoji: discord.Emoji):
        await ctx.send(emoji.url)
          
def setup(bot):
    bot.add_cog(emojis(bot))
