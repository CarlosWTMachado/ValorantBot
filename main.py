import discord
from discord.ext import commands
import os
from random import choice
from keep_alive import keep_alive
import valorantstats
from replit import db
import requests
import json
import asyncio

client = commands.Bot(command_prefix = "$", help_command=None)

agents = []
weapons = []
pistols = []

#Guarda os dados dos agentes pegos da Api
#Eh salvo apenas os dados que serao utilizados
def get_agents(data):
	for key in data:
		if key['bustPortrait'] != None:
			print(key['voiceLine'])
			agents.append({
				'nome' : key['displayName'], 
				'image' : key['bustPortrait'], 
				'icon' : key['displayIcon'],
				'description' : key['description']
			})

#Guarda os dados das armas primarias pegos da Api
#Eh salvo apenas os dados que serao utilizados
#São salvos tambem as skins de cada um
def get_primary(data):
	skins = []
	for skin in data["skins"]:
		if(skin['displayIcon'] != None):
			skins.append({
				'nome' : skin['displayName'],
				'image':skin['displayIcon']
			})
	weapons.append({
		'nome' : data['displayName'], 
		'icon' : data['displayIcon'], 
		'skins' : skins
	})

#Guarda os dados das pistolas pegos da Api
#Eh salvo apenas os dados que serao utilizados
#São salvos tambem as skins de cada um
def get_secundary(data):
	skins = []
	for skin in data["skins"]:
		if(skin['displayIcon'] != None):
			skins.append({
				'nome' : skin['displayName'],
				'image':skin['displayIcon']
			})
	pistols.append({
		'nome' : data['displayName'], 
		'icon' : data['displayIcon'], 
		'skins' : skins
	})

#Sao separados em armas primarias e pistolas
def get_weapons(data):
	for key in data:
		if(key['displayName'] != 'Melee'):
			if(key["shopData"]["category"] == 'Pistols'):
				get_secundary(key)
			else:
				get_primary(key)

async def do_requests():
#pega agentes da api
	agentsURL = "https://valorant-api.com/v1/agents"
	responseAgents = requests.get(agentsURL, params = {"language": "pt-BR"})
	dataAgents = json.loads(responseAgents.text)
	get_agents(dataAgents["data"])
#pega armas da api
	weaponsURL = "https://valorant-api.com/v1/weapons"
	responseWeapons = requests.get(weaponsURL)
	dataWeapons = json.loads(responseWeapons.text)
	get_weapons(dataWeapons["data"])

@client.event
async def on_ready():
	print('Bora Jogar Valorant!\n---------------')
	await do_requests()

@client.command()
async def help(ctx):
	await infoEmb(ctx.message)

@client.command()
async def agente(ctx):
	#escolhe um agente aleatorio
	chosen = choice(agents)
	
	agente_embed = discord.Embed(color=discord.Color.green())
	agente_embed.set_author(name=chosen['nome'], icon_url=chosen['icon'])
	agente_embed.set_thumbnail(url=chosen['image'])
	agente_embed.add_field(name="Description:", value=chosen['description'])
	agente_embed.set_image(url=choice(db[chosen['nome']]))

	await ctx.message.channel.send(content=f"<@{ctx.message.author.id}>",embed=agente_embed)
	await ctx.message.delete()

@client.command()
async def armas(ctx):
	#escolhe uma arma aleatoria
	arma = choice(weapons)
	#escolhe uma skin aleatoria da arma escolhida
	armaSkin = choice(arma['skins'])['image']
	#escolhe uma pistola aleatoria
	pistola = choice(pistols)
	#escolhe uma skin aleatoria da pistola escolhida
	pistolaSkin = choice(pistola['skins'])['image']

	arma_embed = discord.Embed(color=discord.Color.green())
	arma_embed.set_author(name=arma['nome'], icon_url=arma['icon'])
	arma_embed.set_image(url=armaSkin)
	await ctx.message.channel.send(embed=arma_embed)

	pistola_embed = discord.Embed(color=discord.Color.green())
	pistola_embed.set_author(name=pistola['nome'], icon_url=pistola['icon'])
	pistola_embed.set_image(url=pistolaSkin)
	await ctx.message.channel.send(embed=pistola_embed)

@client.command()
async def mghm(ctx):
	await ctx.message.channel.send('https://media.discordapp.net/attachments/762328665870434334/915958010470367322/ezgif-4-877403be7b7f.gif')

@client.command()
async def ace(ctx, mention=''):
	if mention == '':
		await ctx.message.channel.send(choice(db['ace']))
	else:
		await ctx.message.channel.send(f"{mention}\n{choice(db['ace'])}")
	'''
	if ctx.message.mentions:
		await ctx.message.channel.send(f"<@{ctx.message.mentions[0].id}>\n{choice(db['ace'])}");
	else:
		await ctx.message.channel.send(choice(db['ace']));
	'''
	await ctx.message.delete()

@client.command()
async def addgif(ctx, key, link):
	if key in db.keys():
		db[key].append(link)
		await ctx.message.reply("Gif adicionado ao BD.")
	else:
		await ctx.message.reply("Agente invalido!\nEscreva o nome corretamente.")

@client.command()
async def stats(ctx, args):
	print(args)
	await ctx.message.channel.send(embed=valorantstats.valstats(ctx.message))

@client.command(pass_context = True)
async def theworld(ctx):
	if(ctx.author.voice):
		channel = ctx.message.author.voice.channel
		voice = await channel.connect()
		source = discord.FFmpegPCMAudio('https://media.valorant-api.com/sounds/235256474.wav')
		#https://www.youtube.com/watch?v=7ePWNmLP0Z0
		player = voice.play(source)
		await asyncio.sleep(7)
		if(ctx.voice_client):
			await ctx.guild.voice_client.disconnect()
			await ctx.send("Sai do canal de voz.")
	else:
		await ctx.send("Entra num canal de voz ai.")

@client.event
async def on_message(message):
	#prioritize commands
	await client.process_commands(message)
	#ignora mensagem do proprio bot
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
	info_embed.add_field(name="$addgif", value='Adiciona um gif ao BD do personagem, que aparecera no comando $agente', inline=False)
	info_embed.add_field(name="$ace (+ @mençao)", value='@mençao com um gif top', inline=False)
	info_embed.add_field(name="$mghm", value='gif lendario do nosso mestre', inline=False)

	await message.channel.send(embed=info_embed)

keep_alive()
client.run(os.getenv("TOKEN"))

'''
https://media.valorant-api.com/sounds/802792402.wav
https://media.valorant-api.com/sounds/235256474.wav


from dis import disco
from click import pass_context
import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import asyncio
import youtube_dl
import os

client = commands.Bot(command_prefix = "&")

queues = {}

def check_queue(ctx, id):
	if queues[id] != []:
		voice = ctx.guild.voice_client
		source = queues[id].pop(0)
		player = voice.play(source)

@client.event
async def on_ready():
	print("Bot ta pronto !")
	print("--------------")

@client.command()
async def hello(ctx):
	await ctx.send("Olá, GODisGOOD vive!")

@client.command(pass_context = True)
async def theworld(ctx):
	if(ctx.author.voice):
		channel = ctx.message.author.voice.channel
		voice = await channel.connect()
		source = FFmpegPCMAudio('https://media.valorant-api.com/sounds/235256474.wav')
		#https://www.youtube.com/watch?v=7ePWNmLP0Z0
		player = voice.play(source)
		await asyncio.sleep(7)
		if(ctx.voice_client):
			await ctx.guild.voice_client.disconnect()
			await ctx.send("Sai do canal de voz.")
	else:
		await ctx.send("Entra num canal de voz ai.")

@client.command(pass_context = True)
async def join(ctx):
	if(ctx.author.voice):
		channel = ctx.message.author.voice.channel
		await channel.connect()
	else:
		await ctx.send("Entra num canal de voz ai.")

@client.command(pass_context = True)
async def leave(ctx):
	if(ctx.voice_client):
		await ctx.guild.voice_client.disconnect()
		await ctx.send("Saí do canal de voz.")
	else:
		await ctx.send("Não to num canal de voz.")

@client.command(pass_context = True)
async def pause(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	if voice.is_playing():
		voice.pause()
	
@client.command(pass_context = True)
async def resume(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	if voice.is_paused():
		voice.resume()

@client.command(pass_context = True)
async def stop(ctx):
	voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
	voice.stop()

@client.command(pass_context = True)
async def play(ctx, arg):
	voice = ctx.guild.voice_client
	source = FFmpegPCMAudio(arg)
	player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id))

@client.command(pass_context = True)
async def queue(ctx, arg):
	voice = ctx.guild.voice_client
	source = FFmpegPCMAudio(arg)

	guild_id = ctx.message.guild.id
	if guild_id in queues:
		queues[guild_id].append(source)
	else:
		queues[guild_id] = [source]
	await ctx.send("added")

@client.command(pass_context = True)
async def playY(ctx, url:str):
	if(ctx.author.voice):
		channel = ctx.message.author.voice.channel
		voice = await channel.connect()

		ydl_opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192'
			}],
		}

		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])
		for file in os.listdir("./"):
			if file.endswith(".mp3"):
				os.rename(file,"song.mp3")

		source = FFmpegPCMAudio('song.mp3')
		player = voice.play(source)
	else:
		await ctx.send("Entra num canal de voz ai.")

client.run("OTQ1NjQzMTcyNjUzMDY0MjMy.YhTI1Q.Y63shPj68YOOwCUQySBO9cz7rdk")

'''