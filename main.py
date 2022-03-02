import discord
from discord.ext import commands
import os
from random import choice
from keep_alive import keep_alive
import asyncio
import valorantstats

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

weapons = [{'nome': 'Spectre', 'image': 'imagens/spectre.webp'}, 
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

pistols = [{'nome': 'Classic', 'image': 'imagens/classic.webp'}, 
{'nome': 'Shorty', 'image': 'imagens/shorty.jpg'}, 
{'nome': 'Frenzy', 'image': 'imagens/frenzy.webp'}, 
{'nome': 'Ghost', 'image': 'imagens/ghost.webp'}, 
{'nome': 'Sheriff', 'image': 'imagens/sheriff.webp'}]

client = commands.Bot(command_prefix = "$", help_command=None)

@client.event
async def on_ready():
	print('Bora Jogar Valorant!\n---------------')

@client.command(pass_context = True)
async def help(ctx):
	await infoEmb(ctx.message)

@client.command()
async def agente(ctx):
	chosen = choice(agents)
	await ctx.message.reply(file=discord.File(chosen['image']),content=f"{chosen['nome']}\n{chosen['gif']}")

@client.command()
async def armas(ctx):
	arma = choice(weapons)
	pistola = choice(pistols)
	#colocar nome na imagem
	await ctx.message.channel.send(file=discord.File(arma['image']),content=arma['nome'])
	await ctx.message.channel.send(file=discord.File(pistola['image']),content=pistola['nome'])

@client.command()
async def mghm(ctx):
	await ctx.message.channel.send('https://media.discordapp.net/attachments/762328665870434334/915958010470367322/ezgif-4-877403be7b7f.gif')

@client.command()
async def ace(ctx):
	if ctx.message.mentions:
		await ctx.message.channel.send(f"<@{ctx.message.mentions[0].id}> \nhttps://tenor.com/view/dance-dancing-cute-ace-cheer-gif-16720867");
	else:
		await ctx.message.channel.send("https://tenor.com/view/dance-dancing-cute-ace-cheer-gif-16720867");

@client.command()
async def stats(ctx, args):
	print(args)
	await ctx.message.channel.send(embed=valorantstats.valstats(ctx.message))

@client.event
async def on_message(message):
	#prioritize commands
	await client.process_commands(message)

	if message.author == client.user:
		return
	#if the bot is mentioned it responds
	if client.user.mentioned_in(message) and message.mention_everyone is False:
		await message.reply('Use $help pra ver os comandos.')
	#if one of the words were said or if valorantes were mentioned it will answer
	if (message.content.lower().find('valorant') > -1 or 
	message.content.lower().find('vava') > -1 or 
	os.getenv("ROLE_VALORANTES") in message.content):
		await message.reply(content= f"Opa! Valorant? bora, logando... \n{os.getenv('RoleValorantes')}\nhttps://tenor.com/view/hasbulla-gif-22466319")

async def infoEmb(message):
	info_embed = discord.Embed(color=discord.Color.green())
	info_embed.set_thumbnail(url='https://media.discordapp.net/attachments/762328665870434334/915958010470367322/ezgif-4-877403be7b7f.gif')
	info_embed.add_field(name="$agente", value='escolhe um agente aleatorio', inline=False)
	info_embed.add_field(name="$armas", value='escolhe um arma e uma pistola aleatoria', inline=False)
	info_embed.add_field(name="$mghm", value='gif lendario do nosso mestre', inline=False)
	info_embed.add_field(name="$ace (+ @mençao)", value='@mençao com um gif top', inline=False)

	await message.channel.send(embed=info_embed)

keep_alive()
client.run(os.getenv("TOKEN"))
