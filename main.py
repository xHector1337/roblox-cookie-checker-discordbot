import discord
import checker
import asyncio
import requests
from discord.ext import commands,tasks
intents = discord.Intents.default()
intents.message_content = True
token = "" # your token goes here.
bot = commands.Bot(command_prefix='!',intents=intents)
@tasks.loop(seconds=20)
async def status():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for !help"))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for cookies!"))
@bot.event
async def on_ready():
    status.start()

@bot.command(description="Checks your roblox cookie", usage="!check <cookie>")
async def check(ctx, arg: str):
    username = checker.usernamechecker(arg)
    iD = checker.idchecker(arg)
    email = checker.emailchecker(arg)
    phone = checker.phonechecker(arg)
    robux = checker.robuxchecker(arg)
    premium= checker.premiumchecker(arg,iD)
    embed = discord.Embed(title="Cookie Checker", description="**Num Num, It's yummy!**\n**+1 Cookie Points**", color=0x00ff00)
    embed.add_field(name="Roblox Profile", value=f"[Click Here](https://www.roblox.com/users/{iD}/profile)", inline=False)
    embed.add_field(name="Rolimons", value=f"[Click Here](https://www.rolimons.com/player/{iD})", inline=False)
    embed.add_field(name="Username", value=username, inline=False)
    embed.add_field(name="ID", value=iD, inline=False)
    embed.add_field(name="Robux", value=robux, inline=False)
    embed.add_field(name="Premium", value=premium, inline=False)
    embed.add_field(name="Email", value=email, inline=False)
    embed.add_field(name="Phone", value=phone, inline=False)
    await ctx.send(embed=embed)
bot.run(token)