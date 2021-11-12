import discord
import random
import os

from utils import *
from config import *
from setup import setup
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv(ENV_PATH)
setup()

jx = commands.Bot(
    command_prefix="jx", 
    activity=discord.Activity(type=discord.ActivityType.listening, name="Sun Tzu - Art of War"),
)

@jx.event
async def on_ready():
    log(GREEN + "BING CHILLING")

@jx.command()
async def gay(ctx):
    gaypc = random.randint(0, 100)
    embed = discord.Embed(
        colour = discord.Color.blurple(),
        title = ":bar_chart: The Results Are In..",
        description=f"You are {gaypc}% gay {ctx.message.author.mention}."
    )
    if gaypc >= 50: # gay ass
        embed.set_image(url="https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Foriginal%2F000%2F030%2F971%2FScreen_Shot_2019-08-29_at_2.44.51_PM.jpg")
    else: # straight ass
        embed.set_image(url="https://cdn.discordapp.com/attachments/769235296888946738/888536811067035658/RTSmothered.png")
    await ctx.send(embed=embed)

@jx.command()
async def noob(ctx):
    noobpc = random.randint(0, 100)
    embed = discord.Embed(
        colour = discord.Color.blurple(),
        title = "The Results Are In..",
        description=f"You are {noobpc}% noob {ctx.message.author.mention}."
    )
    if noobpc >= 50: # noob
        embed.set_image(url="https://static.wikia.nocookie.net/roblox/images/3/3b/NOOB%21.png/revision/latest?cb=20210630174226")
    else: # giga chad
        embed.set_image(url="https://wompampsupport.azureedge.net/fetchimage?siteId=7575&v=2&jpgQuality=100&width=700&url=https%3A%2F%2Fi.kym-cdn.com%2Fentries%2Ficons%2Foriginal%2F000%2F026%2F152%2Fgigachad.jpg")
    await ctx.send(embed=embed)

@jx.command()
async def signup(ctx):
    authorId = ctx.message.author.id
    embed = discord.Embed(
        colour = discord.Color.green(),
        title = ":white_check_mark: Thank you for Signing Up! :white_check_mark:",
        description=f"Account created successfully {ctx.message.author.mention}!"
    )

    try:
        if not createAccount(authorId):
            embed.colour = discord.Color.red()
            embed.title = ":no_entry_sign: NOT BING CHILLING! :no_entry_sign:"
            embed.description = f"You cannot create more than 1 account {ctx.message.author.mention}."
    except Exception as e:
        embed.colour = discord.Color.red()
        embed.title = ":no_entry_sign: NOT BING CHILLING! :no_entry_sign:"
        embed.description = f"Account signup failed, please try again later {ctx.message.author.mention}!"
    await ctx.send(embed=embed)

@jx.command()
async def delete(ctx):
    authorId = ctx.message.author.id
    embed = discord.Embed(
        colour = discord.Color.green(),
        title = ":white_check_mark: Success! :white_check_mark:",
        description = f"Account deleted successfully {ctx.message.author.mention}!"
    )

    if not deleteAccount(authorId): # Returns False if they don't have an account
        embed.colour = discord.Color.red()
        embed.title = ":no_entry_sign: NOT BING CHILLING! :no_entry_sign:"
        embed.description = f"You don't have an account {ctx.message.author.mention}!"

    await ctx.send(embed=embed)

@jx.command()
async def sc(ctx):
    authorId = ctx.message.author.id
    amt = getUserAttribute(authorId, "sc")
    if not amt: amt = 0
    embed = discord.Embed(
        colour = discord.Color.green(),
        title = ":moneybag: Account Balance :moneybag:",
        description=f"You have {amt} BING CHILLING coins {ctx.message.author.mention}!"
    )
    if accountExists(authorId):
        await ctx.send(embed=embed)
    else:
        embed.colour = discord.Color.red()
        embed.title = ":no_entry_sign: You Don't Have a Wallet! :no_entry_sign:"
        embed.description = f"Try creating an account first {ctx.message.author.mention}."
        await ctx.send(embed=embed)

@jx.command()
async def beg(ctx):
    authorId = ctx.message.author.id
    willGive = random.randint(1, 10) == 10
    gains = 5
    embed = discord.Embed(
        colour = discord.Color.green(),
        title = ":moneybag: BONES ACQUIRED! :moneybag:",
        description=f"You have received {gains} BING CHILLING coins {ctx.message.author.mention}!"
    )
    if not willGive:
        embed.colour = discord.Color.red()
        embed.title = ":sob: No bones acquired.. :sob:"
        embed.description = f"""我没有太多的时间请帮我， 我再说一遍， 请帮我， 我是认真的， 我已经被中国政府抓获了， 请帮我， 我的球不见了， 我像狗一样被割伤了， 卫兵们正在返回， 我要求他们在他们到达时唱歌上帝， 请饶恕我， 请饶恕我

快， 他们走了， 你必须来快， 我觉得结束是接近第一我的球旁边我的阴茎， 最后我的生活 {ctx.message.author.mention}."""
    else:
        setUserAttribute(authorId, "sc", getUserAttribute(authorId, "sc")+gains)
    
    await ctx.send(embed=embed)

jx.run(os.getenv("TOKEN"))