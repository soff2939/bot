import discord
from discord.ext import commands
import google.generativeai as genai
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
genai.configure(api_key="AIzaSyBIRjbs_w7graezF9xzG5GK92F-z6cf7gc")
# Modelo Gemini
model = genai.GenerativeModel("gemini-1.5-flash")
@bot.command()
async def gemini(ctx, *, pregunta: str):
    """Comando para preguntar a Gemini"""
    await ctx.send(" Pensando...")
    response = model.generate_content(pregunta)
    await ctx.send(response.text)
bot.run("MTI5NDg2NDM1NjYxNzc0ODUwMA.G4kOt2.P0HCy2FlM3TKFhqznqNY2sslrp5dYu1IVzUlKI")