import discord
import os
from random import choice
from keep_alive import keep_alive

agents = [{
    'nome': 'Neon',
    'image': 'imagens/neon.jpg'
}, {
    'nome': 'Chamber',
    'image': 'imagens/xambinho.jpg'
}, {
    'nome': 'Skye',
    'image': 'imagens/skye.jpg'
}, {
    'nome': 'Yoru',
    'image': 'imagens/yoru.png'
}, {
    'nome': 'Astra',
    'image': 'imagens/astra.png'
}, {
    'nome': 'KAY/O',
    'image': 'imagens/caio.jpg'
}, {
    'nome': 'Fenix',
    'image': 'imagens/fenix.png'
}, {
    'nome': 'Raze',
    'image': 'imagens/raize.png'
}, {
    'nome': 'Brimstone',
    'image': 'imagens/brimstone.jpg'
}, {
    'nome': 'Jett',
    'image': 'imagens/jett.jpg'
}, {
    'nome': 'Sage',
    'image': 'imagens/sage.jpg'
}, {
    'nome': 'Viper',
    'image': 'imagens/viper.png'
}, {
    'nome': 'Breach',
    'image': 'imagens/breach.png'
}, {
    'nome': 'Cypher',
    'image': 'imagens/cypher.jpg'
}, {
    'nome': 'Sova',
    'image': 'imagens/sova.jpg'
}, {
    'nome': 'Homem',
    'image': 'imagens/omem.jpg'
}, {
    'nome': 'Reyna',
    'image': 'imagens/reina.jpg'
}, {
    'nome': 'Killjoy',
    'image': 'imagens/killjoy.png'
}]

armas = [{
    'nome': 'Spectre',
    'image': 'imagens/spectre.webp'
}, {
    'nome': 'Odin',
    'image': 'imagens/odin.jpg'
}, {
    'nome': 'Vandal',
    'image': 'imagens/vandal.jpg'
}, {
    'nome': 'Bucky',
    'image': 'imagens/bucky.webp'
}, {
    'nome': 'Bulldog',
    'image': 'imagens/bulldog.webp'
}, {
    'nome': 'Operator',
    'image': 'imagens/operator.jpg'
}, {
    'nome': 'Stinger',
    'image': 'imagens/stinger.webp'
}, {
    'nome': 'Guardian',
    'image': 'imagens/guardian.jpg'
}, {
    'nome': 'Ares',
    'image': 'imagens/ares.jpg'
}, {
    'nome': 'Phantom',
    'image': 'imagens/phantom.jpg'
}, {
    'nome': 'Marhsall',
    'image': 'imagens/marshall.jpg'
}, {
    'nome': 'Judge',
    'image': 'imagens/judge.jpg'
}]

pistolas = [{
    'nome': 'Classic',
    'image': 'imagens/classic.webp'
}, {
    'nome': 'Shorty',
    'image': 'imagens/shorty.jpg'
}, {
    'nome': 'Frenzy',
    'image': 'imagens/frenzy.webp'
}, {
    'nome': 'Ghost',
    'image': 'imagens/ghost.webp'
}, {
    'nome': 'Sheriff',
    'image': 'imagens/sheriff.webp'
}]

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
      await message.reply(file=discord.File(chosen['image']),content=chosen['nome'])

    if message.content == '$armas':
      arma = choice(armas)
      pistola = choice(pistolas)
      await message.channel.send(file=discord.File(arma['image']),content=arma['nome'])
      await message.channel.send(file=discord.File(pistola['image']),content=pistola['nome'])

    if message.content == '$mghm':
      await message.channel.send('https://media.discordapp.net/attachments/762328665870434334/915958010470367322/ezgif-4-877403be7b7f.gif')

    if message.content == '$help':
      await info(message)

    if message.content.lower().find('valorant') > -1 or os.getenv("RoleValorantes") in message.content:
      await message.reply(content= f"Opa! Valorant? bora, logando... \n{os.getenv('RoleValorantes')}\nhttps://tenor.com/view/hasbulla-gif-22466319")

    if client.user.mentioned_in(message) and message.mention_everyone is False:
      await message.reply('O que tu quer?')

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