import discord
from discord.ext import commands
import inspect

class source(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def source(self, ctx, *, text: str):
        """Shows source code of a command."""
        nl2 = '`'
        nl = f"``{nl2}"
        source_thing = inspect.getsource(self.bot.get_command(text).callback)
        await ctx.send(f"{nl}py\n{source_thing}{nl}")
        
def setup(bot):
    bot.add_cog(source(bot))
