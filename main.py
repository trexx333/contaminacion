import discord
import random,requests
from discord.ext import commands
from generador import get_duck_image_url
import os
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

reciclaje_items = ['plastico', 'vidrio', 'papel', 'cartulina', 'periodico', 'latas de aluminio', 'electronicos' 'envases', 'metales', 'telefonos']
no_reciclaje_items = ['restos de comida', 'pañales', 'baterias', 'encendedores', 'ceramica', 'servilletas', 'papel higienico', 'pinturas', 'medicamentos', 'cristales']

# ponen imagenes
@bot.command()
async def meme(ctx):
  try:
    images = os.listdir('c:/python-course/memes/images')
    if images:
      img_name = random.choice(images)
      with open(f'c:/python-course/memes/images/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    else:
      await ctx.send("¡No se encontraron memes en la carpeta 'imagenes'!")
  except FileNotFoundError:
    await ctx.send("¡No se encontraron memes en la carpeta 'imagenes'!")

@bot.command()
async def info(ctx):
  try:
    images = os.listdir('c:/python-course/memes/contaminacion')
    if images:
      img_name = random.choice(images)
      with open(f'c:/python-course/memes/contaminacion/{img_name}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
    else:
      await ctx.send("¡No se encontro la info en la carpeta 'contaminacion'!")
  except FileNotFoundError:
    await ctx.send("¡No se encontro la info en la carpeta 'contaminacion'!")

# uso del api
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command("duck")
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

# reciclaje
@bot.command(name = "reciclaje")
async def reciclaje(ctx, item: str):
    item = item.lower()
    if item in reciclaje_items:
        await ctx.send(f"Si,tu puedes reciclar, {item}")
    else:
        await ctx.send(f"No,tu no puedes reciclar, {item}") 

@bot.command(name = "basura")
async def basura(ctx, item: str):
    item = item.lower()
    if item in no_reciclaje_items:
        await ctx.send(f"tu deberias tirar el/la {item} en la basura")
    else:
        await ctx.send(f"puedes intenta reciclar {item}.")

# informacion escrita
@bot.command()
async def manualidades(ctx):
  await ctx.send("""
**Manualidades con materiales de reciclaje**

1. **Lámpara hecha con botellas de plástico**
2. **Maceta hecha con latas de aluminio**
3. **Collar hecho con botones y cordones**
4. **Papel reciclado para hacer tarjetas y regalos**
5. **Bolsa de tela hecha con ropa vieja**
6. **Joyería hecha con materiales reciclados**
7. **Decoración para el hogar hecha con materiales reciclados**

""")

@bot.command()
async def helps(ctx):
  await ctx.send("""
**Manual de los comandos**

1. **$memes**: te muestra unos memes de programacion
2. **$duck**: diferentes imagenes de patos
3. **$manualidades**: te da varias opciones de manualidades que puedes hacer con materiales reciclabes
4. **$reciclaje o $basura**: te dice si un material es reciclable o no
5. **$info**: te da algunos memes/datos de la contaminacion                           
""")

bot.run('MTI0MDExMDQ4MDk2NjgxNTg2NQ.GXM5JS.s-Y0qiZZ5uo_K9-yofnMinhxxvQlOQH_75ZPj4')


        













