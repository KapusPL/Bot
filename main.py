
import os
import random
import discord
from discord.ext import commands

letters = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!generuj ', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}") 
    botactivity = discord.Activity(type=discord.ActivityType.playing, name="!generuj NITRO",)
    await client.change_presence(activity=botactivity, status=discord.Status.do_not_disturb)
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def NITRO(ctx):
    if ctx.channel.id != '1067490336177397780':
      await message.channel.send(':x: Niepoprawny kanał.')
    else:
      nitro = "".join(random.choices(letters, k=16))
      link = 'discord.gift/' + nitro
      embed_nitro = discord.Embed(title='Pomyślnie wygenerowano Discord Nitro!', description='Twój kod: ||' + link + '||')
      await ctx.send(embed=embed_nitro)


bot.run(os.environ["DISCORD_TOKEN"])
