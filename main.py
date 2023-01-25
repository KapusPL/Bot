
import os
import random
import discord
from discord.ext import commands

numbers = '1234567890'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!generuj ', intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}") 
    botactivity = discord.Activity(type=discord.ActivityType.playing, name="!generuj PSC",)
    await bot.change_presence(activity=botactivity, status=discord.Status.do_not_disturb)

@bot.command()
async def PSC(ctx):
      psc = "".join(random.choices(numbers, k=15))
      embed_psc = discord.Embed(title='Pomyślnie wygenerowano kod PSC!', description='Twój kod: ||0' + psc + '||', color=0x2161f2)
      await ctx.send(embed=embed_psc)

bot.run(os.environ["DISCORD_TOKEN"])
