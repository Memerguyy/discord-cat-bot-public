# hello kind human, if you can somehow see this please message me on discord Memer#1337 because this is my first time coding so please take mercy on my passwords, thanks in advance <3
import discord
from discord import app_commands
from discord.ext import commands
import praw
import asyncio
from random import randint
import time
from datetime import datetime
import random
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

intents=discord.Intents.all()
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', activity=discord.Game(name="do !helpme"), intents=intents)
reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), client_secret=os.getenv('CLIENT_SECRET'), user_agent='Just a bot for a discord server', username='Memerguyy', password=os.getenv('PASSWORD_REDDIT'))

trustedid = [582570200621252624, 582573456105799756, 704726055864369232, 357193227499208704, 883725422712479754]
images = [".jpg", ".png", ".jpeg", ".gif"]

# @bot.event
# async def on_ready():

@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name="cat", description="sends a pic of a cat")
async def cat(inter: discord.Interaction):
    await inter.response.send_message(content="Sending a kitty, hold tight", ephemeral=False)
    subreddit = reddit.subreddit('cats').random()
    i = 1
    while i == 1:
        if any((subreddit.url.endswith(ext) for ext in images)):
            await inter.channel.send(subreddit.url)
            await inter.channel.send("Kitty acquired")
            i += 1
        else:
            subreddit = reddit.subreddit('cats').random()

@bot.tree.command(name="dog", description="sends a pic of a dog")
async def dog(inter: discord.Interaction):
    await inter.response.send_message(content="Sending a dog, hold tight", ephemeral=False)
    subreddit = reddit.subreddit('dogpictures').random()
    i = 1
    while i == 1:
        if any((subreddit.url.endswith(ext) for ext in images)):
            await inter.channel.send(subreddit.url)
            await inter.channel.send("Dog acquired")
            i += 1
        else:
            subreddit = reddit.subreddit('dogpictures').random()

@bot.tree.command(name="dice", description="rolls a six sided dice")
async def dice(inter: discord.Integration):
    await inter.response.send_message(content="You have rolled a dice!", ephemeral=False)
    msg = await inter.channel.send("Rolling in progress... :game_die:")
    time.sleep(1.5)
    await msg.edit(content=f"Rolling in progress... :game_die: \n\nThe number you rolled is {randint(1, 6)}!")

@bot.tree.command(name="customdice", description="rolls a dice between the 2 numbers of your choosing, how cool is that?")
async def custdice(inter, int1: int, int2: int):
    await inter.response.send_message(content="Well, let's hope luck's on your side...", ephemeral=False)
    msg = await inter.channel.send("You have rolled a dice! Rolling in progress... :game_die:")
    number1 = int(int1)
    number2 = int(int2)
    time.sleep(1.5)
    await msg.edit(content=f"You have rolled a dice! Rolling in progress... :game_die: \n\nThe number you rolled is {randint(number1, number2)}!")

@bot.command()
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.channel.send(f"Rock, paper, or scissors? Choose wisely...")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame
    user_choice = (await bot.wait_for('message', check=check)).content
    comp_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if comp_choice == 'rock':
            await ctx.channel.send(f'We tied.\n\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            comp_choice = random.choice(rpsGame)
        elif comp_choice == 'paper':
            await ctx.channel.send(f'Nice try lol.\n\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            comp_choice = random.choice(rpsGame)
        elif comp_choice == 'scissors':
            await ctx.channel.send(f"What? This isn't rigged? No way\n\nYour choice: {user_choice}\nMy choice: {comp_choice}")
            comp_choice = random.choice(rpsGame)

    elif user_choice == 'paper':
        if comp_choice == 'rock':
            await ctx.channel.send(f'Ez clap.\n\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            comp_choice = random.choice(rpsGame)
        elif comp_choice == 'paper':
            await ctx.channel.send(f'Schrodingers match, I see.\n\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            comp_choice = random.choice(rpsGame)
        elif comp_choice == 'scissors':
            await ctx.channel.send(f"Kys.\n\nYour choice: {user_choice}\nMy choice: {comp_choice}")
            comp_choice = random.choice(rpsGame)

    elif user_choice == 'scissors':
        if comp_choice == 'rock':
            await ctx.channel.send(f"Noooo cyap you're actually braaaaindead.\n\nYour choice: {user_choice}\nMy choice: {comp_choice}")
            comp_choice = random.choice(rpsGame)
        elif comp_choice == 'paper':
            await ctx.channel.send(f'Bruh.\n\nYour choice: {user_choice}\nMy choice: {comp_choice}')
            comp_choice = random.choice(rpsGame)
        elif comp_choice == 'scissors':
            await ctx.channel.send(f"Your intelligence is on par with mine, and that's not really a good thing.\n\nYour choice: {user_choice}\nMy choice: {comp_choice}")
            comp_choice = random.choice(rpsGame)

@bot.command()
async def getsub(ctx, subname):
    subred = reddit.subreddit(subname).top(time_filter="day", limit=1)
    if reddit.subreddit(subname).over18:
        if ctx.message.author.id in trustedid:
            for submission in subred:
                await ctx.channel.send(f"https://www.reddit.com/r/{subname}/comments/{reddit.subreddit(subname).random()}")
        else:
            await ctx.channel.send("You really think I didn't think of this?")
    else:
        for submission in subred:
           await ctx.channel.send(f"https://www.reddit.com/r/{subname}/comments/{reddit.subreddit(subname).random()}")
           
@bot.command()
async def get18(ctx, subname):
    subred = reddit.subreddit(subname).random()
    if reddit.subreddit(subname).over18:
        if ctx.message.author.id in trustedid:
            i = 1
            while i == 1:
                if any((subred.url.endswith(ext) for ext in images)):
                    await ctx.channel.send(subred.url)
                    i += 1
                else:
                    subred = reddit.subreddit(subname).random()
    else:
        await ctx.channel.send("Nah")

@bot.command()
async def hentai(ctx):
    if ctx.message.author.id in trustedid:
        subreddit = reddit.subreddit('hentai').random()
        i = 1
        while i == 1:
            if any((subreddit.url.endswith(ext) for ext in images)):
                await ctx.channel.send(subreddit.url)
                i += 1
            else:
                subreddit = reddit.subreddit('hentai').random()
    else:
        await ctx.channel.send("You're not allowed to use this command, sorry ¯\_(ツ)_/¯")

@bot.command()
async def yuri(ctx):
    if ctx.message.author.id in trustedid:
        subreddit = reddit.subreddit('yurihentai').random()
        i = 1
        while i == 1:
            if any((subreddit.url.endswith(ext) for ext in images)):
                await ctx.channel.send(subreddit.url)
                i += 1
            else:
                subreddit = reddit.subreddit('yuri').random()
    else:
        await ctx.channel.send("You're not allowed to use this command, sorry ¯\_(ツ)_/¯")

@bot.command(pass_context=True)
async def poll(ctx,*, message):
    embed = discord.Embed(title=f"📢 Poll time by {ctx.author.name}!", description=f"{message}", color=ctx.author.color)
    msg = await ctx.channel.send(embed=embed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')

    ctx.channel.send(ctx.message.id)

@bot.command()
async def helpme(ctx):
    embed = discord.Embed(title="Help", description="This is a list of commands", color=ctx.author.color)
    embed.add_field(name="!cat", value="Gets a random cat picture", inline=False)
    embed.add_field(name="!dog", value="Gets a random dog picture", inline=False)
    embed.add_field(name="!poll", value="Creates a poll, after calling the command put in your topic and the command will put it in an embed with a thumbs up and thumbs down reaction", inline=False)
    embed.add_field(name="!help", value="Shows this message", inline=False)
    embed.add_field(name="!author", value="Shows who made the bot", inline=False)
    embed.add_field(name="!imlazy", value="Put a reddit link in after the command to show the image since the default reddit preview is pretty small", inline=False)
    embed.add_field(name="!getsub", value="Fetches a random post from the top 24 hours ||...1/5 times at least|| from the subreddit of your choice. Usage goes as follows '!getsub [your desired subreddit name here].'", inline=False)
    embed.add_field(name="!dice", value="Rolls a number between 1 and 6", inline=False)
    embed.add_field(name="!custdice", value="Rolls between 2 numbers of your choosing! Usage: `!custdice [number1] [number2]", inline=False)
    embed.add_field(name="!rps", value="Play rock paper scissors with a bot a friendless loser", inline=False)
    await ctx.channel.send(embed=embed)

@bot.command()
async def author(ctx):
    embed = discord.Embed(title="Ayo no way this command works?!?!?!?!", description="I'm a bot made by Memer#1337, even though this is a private bot I just wanted to put my face somewhere in it lmao", color=0x82A551)
    embed.set_thumbnail(url=ctx.author.avatar_url)
    await ctx.channel.send(embed=embed)

@bot.command(pass_context=True)
async def salad(ctx):
    if ctx.guild.id != 963320083717951558: #This is the wanted guild id
        return
    else:
        print("salad")
        await ctx.channel.send("Salad is good")
        await ctx.channel.send("https://imgur.com/a/zkrFaV9")

@bot.command(pass_context=True)
async def charlie(ctx):
    if ctx.guild.id != 963320083717951558: #This is the wanted guild id
        return
    else:
        print("salad")
        await ctx.channel.send("Charlie beloved:heart_decoration:")
        await ctx.channel.send("https://imgur.com/a/kf0OSHr")

@bot.command(pass_context=True)
async def imlazy(ctx, submission: str):
    submission = reddit.submission(url=submission)

    embed = discord.Embed(title=submission.title, url=f"https://reddit.com{submission.permalink}")
    embed.set_image(url=submission.url)

    await ctx.channel.send(embed=embed)

bot.run(os.getenv('TOKEN'))