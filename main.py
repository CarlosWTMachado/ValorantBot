import discord
import os
from random import choice
from keep_alive import keep_alive

agents = [{'nome': 'Neon', 'image': 'imagens/neon.jpg', 'gif': 'https://tenor.com/bOunQ.gif'}, 
{'nome': 'Chamber', 'image': 'imagens/xambinho.jpg', 'gif': 'https://tenor.com/bPeJp.gif'}, 
{'nome': 'Skye', 'image': 'imagens/skye.jpg', 'gif': 'https://tenor.com/bqRnS.gif'}, 
{'nome': 'Yoru', 'image': 'imagens/yoru.png', 'gif': 'https://tenor.com/bvCRZ.gif'}, 
{'nome': 'Astra', 'image': 'imagens/astra.png', 'gif': 'https://tenor.com/bFdL7.gif'}, 
{'nome': 'KAY/O', 'image': 'imagens/caio.jpg', 'gif': 'https://tenor.com/bFHwm.gif'}, 
{'nome': 'Fenix', 'image': 'imagens/fenix.png', 'gif': 'https://tenor.com/bQayi.gif'}, 
{'nome': 'Raze', 'image': 'imagens/raize.png', 'gif': 'https://tenor.com/bNtSD.gif'}, 
{'nome': 'Brimstone', 'image': 'imagens/brimstone.jpg', 'gif': 'https://tenor.com/bvbtQ.gif'}, 
{'nome': 'Jett', 'image': 'imagens/jett.jpg', 'gif': 'https://tenor.com/bEHcn.gif'}, 
{'nome': 'Sage', 'image': 'imagens/sage.jpg', 'gif': 'https://tenor.com/bHhhf.gif'}, 
{'nome': 'Viper', 'image': 'imagens/viper.png', 'gif': 'https://tenor.com/bLlJA.gif'}, 
{'nome': 'Breach', 'image': 'imagens/breach.png', 'gif': 'https://tenor.com/bJmAo.gif'}, 
{'nome': 'Cypher', 'image': 'imagens/cypher.jpg', 'gif': 'https://tenor.com/bovkI.gif'}, 
{'nome': 'Sova', 'image': 'imagens/sova.jpg', 'gif': 'https://tenor.com/bCbue.gif'}, 
{'nome': 'Homem', 'image': 'imagens/omem.jpg', 'gif': 'https://tenor.com/bD7OT.gif'}, 
{'nome': 'Reyna', 'image': 'imagens/reina.jpg', 'gif': 'https://tenor.com/bO4GA.gif'}, 
{'nome': 'Killjoy', 'image': 'imagens/killjoy.png', 'gif': 'https://tenor.com/bDx6X.gif'}]

armas = [{'nome': 'Spectre', 'image': 'imagens/spectre.webp'}, 
{'nome': 'Odin', 'image': 'imagens/odin.jpg'}, 
{'nome': 'Vandal', 'image': 'imagens/vandal.jpg'}, 
{'nome': 'Bucky', 'image': 'imagens/bucky.webp'}, 
{'nome': 'Bulldog', 'image': 'imagens/bulldog.webp'}, 
{'nome': 'Operator', 'image': 'imagens/operator.jpg'}, 
{'nome': 'Stinger', 'image': 'imagens/stinger.webp'}, 
{'nome': 'Guardian', 'image': 'imagens/guardian.jpg'}, 
{'nome': 'Ares', 'image': 'imagens/ares.jpg'}, 
{'nome': 'Phantom', 'image': 'imagens/phantom.jpg'}, 
{'nome': 'Marhsall', 'image': 'imagens/marshall.jpg'}, 
{'nome': 'Judge', 'image': 'imagens/judge.jpg'}]

pistolas = [{'nome': 'Classic', 'image': 'imagens/classic.webp'}, 
{'nome': 'Shorty', 'image': 'imagens/shorty.jpg'}, 
{'nome': 'Frenzy', 'image': 'imagens/frenzy.webp'}, 
{'nome': 'Ghost', 'image': 'imagens/ghost.webp'}, 
{'nome': 'Sheriff', 'image': 'imagens/sheriff.webp'}]

valorant = ["valorant", "valorantes", "@valorantes"]

client = discord.Client()

@client.event
async def on_ready():
  print('Bora Jogar Valorant!'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content == '$agente':
      chosen = choice(agents)
      await message.reply(file=discord.File(chosen['image']),content=f"{chosen['nome']}\n{chosen['gif']}")

    if message.content == '$armas':
      arma = choice(armas)
      pistola = choice(pistolas)
      await message.channel.send(file=discord.File(arma['image']),content=arma['nome'])
      await message.channel.send(file=discord.File(pistola['image']),content=pistola['nome'])

    if message.content == '$mghm':
      await message.channel.send('https://media.discordapp.net/attachments/762328665870434334/915958010470367322/ezgif-4-877403be7b7f.gif')

    if message.content == '$help':
      await info(message)

    if message.content.lower().find('valorant') > -1 or message.content.lower().find('vava') > -1 or os.getenv("RoleValorantes") in message.content:
      await message.reply(content= f"Opa! Valorant? bora, logando... \n{os.getenv('RoleValorantes')}\nhttps://tenor.com/view/hasbulla-gif-22466319")

    if client.user.mentioned_in(message) and message.mention_everyone is False:
      await message.reply('O que tu quer?')

    if (message.content.lower().find('anao') > -1 or 
    message.content.lower().find('anão') > -1 or 
    message.content.lower().find('a nao') > -1 or 
    message.content.lower().find('ah nao') > -1):
      await message.reply('https://tenor.com/vILU.gif');

async def info(message):
    info_embed = discord.Embed(color=discord.Color.green())
    info_embed.set_thumbnail(url='https://media.discordapp.net/attachments/762328665870434334/915958010470367322/ezgif-4-877403be7b7f.gif')
    info_embed.add_field(name="$agente", value='escolhe um agente aleatorio', inline=False)
    info_embed.add_field(name="$armas", value='escolhe um arma e um pistola aleatoria', inline=False)
    info_embed.add_field(name="$mghm", value='gif lendario do nosso mestre', inline=False)

    await message.channel.send(embed=info_embed)

keep_alive()
client.run(os.getenv("TOKEN"))

'''
async def info(ctx, member: discord.Member):

    info_embed = discord.Embed(color=discord.Color.green())
    info_embed.set_thumbnail(url=f"{member.avatar_url_as(format=None, static_format='webp', size=1024)}")
    info_embed.add_field(name="Member:", value=f"{member.mention}", inline=False)
    info_embed.add_field(name="Member name", value=f"{member}", inline=False)
    info_embed.add_field(name="Member id:", value=f"{member.id}", inline=False)
    info_embed.add_field(name="Nickname:", value=f"{member.nick}", inline=False)
    info_embed.add_field(name="Joined at:", value=f"{member.joined_at}", inline=False)
    roles = " ".join([role.mention for role in member.roles if role.name != "@everyone"])
    info_embed.add_field(name="Roles:", value=f"{roles}", inline=False)
    info_embed.set_footer(text="GG-GamerPub | auto-mod")

    await ctx.send(embed=info_embed)
'''