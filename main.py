import discord
import random
import os

numbers = '1234567890'
letters = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'

intents = discord.Intents.default()

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')
  botactivity = discord.Activity(
    type=discord.ActivityType.playing,
    name="!generuj NITRO",
  )
  await client.change_presence(activity=botactivity,
                               status=discord.Status.do_not_disturb)


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!ping'):
    ping = str(round(client.latency * 1000))
    embed_ping = discord.Embed(title='Pong!',
                               description='Ping wynosi ' + ping + 'ms')
    await message.channel.send(embed=embed_ping)

  if message.content.startswith('!generuj NITRO'):
    if message.channel.id != '1067490336177397780':
      await message.channel.send(':x: Niepoprawny kanał.')
    else:
      nitro = "".join(random.choices(letters, k=16))
      link = 'discord.gift/' + nitro
      embed_nitro = discord.Embed(
        title='Pomyślnie wygenerowano Discord Nitro!',
        description='Twój kod: ||' + link + '||')
      await message.channel.send(embed=embed_nitro)
      return

client.run(os.environ.get('DICORD_TOKEN'))
