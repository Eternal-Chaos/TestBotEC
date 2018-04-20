import os
import discord
import json
import random
from discord.ext import commands
from cleverwrap import CleverWrap
import asyncio
from ext.paginator import Paginator


class general:
    def __init__(self, bot):
        self.bot = bot
	
        
    @commands.command()
    async def invite(self,ctx):
        '''invite the bot :D'''
        em = discord.Embed(color = 0xffd500, title = "Click Here To Invite", url = "https://discordapp.com/oauth2/authorize?client_id=375138989398687746&scope=bot&permissions=305196166")
        em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/274387797140570112/409323858437472257/image.jpg")
        em.add_field(name = "Jake The Bot", value = """**Support Server** \nServer Link: https://discord.gg/bmeBBdd """, inline = True)
        em.set_footer(text = "Jake",icon_url = self.bot.user.avatar_url_as(static_format='png'))
        await ctx.send(embed = em)

    @commands.command()
    async def say(self, ctx, *, args=None):
        if args is None:
            await ctx.send('Type something O:')
        else:
            await ctx.send(args)
	
    @commands.command()
    async def emsay(self, ctx, *, args = None):
        if args is None:
            await ctx.send("Type something (' - '   )")
        else:
	        em = discord.Embed(color=0xffd500)
	        em.description = args
	        await ctx.send(embed = em)
     
    @commands.command()
    async def getems(self, ctx):
         l = []
         for e in ctx.guild.emojis:
             name = e.name+ " " + "{}".format(e)
             l.append (name)
         emo = ' '.join(l)
         await ctx.send(emo)


    @commands.command()
    async def getallemojis(self, ctx):
         """gets all emojis from every server the bot is in"""
         allemojis = []
         servers = []
         paginator = Paginator()
         for server in self.bot.guilds:
             for e in server.emojis:
                 name = f"{e}"
                 allemojis.append(name)
             spam = ' '.join(allemojis)
             servers.append(allemojis)
         for server in servers:
             paginator.addLine(servers)
         for page in paginator.pages:
             await ctx.send(page)           


def setup(bot):
	bot.add_cog(general(bot))
