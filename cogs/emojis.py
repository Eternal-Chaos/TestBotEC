import discord
import asyncio
from discord.ext import commands

class emojis:
    def __init__(self, bot):
        self.bot = bot
        
        
    
    @commands.command()
    async def us(self, ctx):
        await self.user.edit(username = "Jake The Bot")
        await ctx.send('Username Changed :D')

    @commands.command(pass_context = True)
    async def addemoji(ctx, emoji_name, emoji_link = ''):
        msg: discord.Message = ctx.message
        if msg.attachments:
          await ctx.message.delete()
          
def setup(bot):
    bot.add_cog(emojis(bot))