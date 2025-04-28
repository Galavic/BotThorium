import discord
from discord.ext import commands
import pymongo
import random
import string
import datetime
import os

# Variables de entorno
DISCORD_TOKEN = os.getenv("MTM2NjIzMTY0MjcyMDY5ODQzOA.GjpRRL.lUddfoo7mO0npOXeEi0EwDsQttu8g5vB5nQNt8")
MONGO_URI = os.getenv("mongodb+srv://Thorium:enrimiliano092009@thorium.b3w9o.mongodb.net/Thorium?retryWrites=true&w=majority")

# Conexión a MongoDB
mongo_client = pymongo.MongoClient(MONGO_URI)
db = mongo_client["Thorium"]
collection = db["premium_keys"]

# Inicializa el bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Función para generar una key
def generate_key():
    guid = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f"{guid[0:4]}-{guid[4:8]}-{guid[8:12]}-{guid[12:16]}"

# Comando para generar y guardar una key
@bot.command(name="genkey")
async def genkey(ctx):
    try:
        new_key = generate_key()
        
        document = {
            "key": new_key.replace("-", ""),
            "used": False,
            "created_at": datetime.datetime.utcnow()
        }

        collection.insert_one(document)

        await ctx.send(f"✅ Key generada: `{new_key}`")
    
    except Exception as e:
        await ctx.send(f"❌ Error generando la key: {e}")

# Ejecutar el bot
bot.run(DISCORD_TOKEN)
