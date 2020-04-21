import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'pixart ')

class Bot(discord.Client):
    def __init__(self):
        super().__init__()
    
    async def on_ready(self):
        print('Pixart ready')

    async def on_message(self, message):
        if message.content.startswith('pixart') or message.content.startswith('Pixart'):
            await message.channel.send('Oui maître ?') 
        elif message.content.startswith('bonjour') or message.content.startswith('bonsoir') or message.content.startswith('salut') or message.content.startswith('yo'):
            await message.channel.send('Bien le bonjour')            
        elif message.content.startswith('你好') or message.content.startswith('Pixart'):
            await message.channel.send('你好， 你好嗎？')
        elif message.content.endswith('你呢') or message.content.startswith('Pixart'):
            await message.channel.send('我很好， 謝謝')  
        elif message.content.startswith("d'où viens tu") or message.content.startswith('Pixart'):
            await message.channel.send('Constantin est mon père')            
        elif message.content.startswith('silence') or message.content.startswith('chut'):
            await message.channel.send('Je me retire...')
        elif message.content.startswith('affiche pi'):
            await message.channel.send('3.14159265358979323846264338327950288419716939937510')       
        elif message.content.startswith('merci') and (message.content.endswith('Pixart') or message.content.endswith('pixart')):
            await message.channel.send('Pas de soucis, remerciez plutôt mon père Constantin')
        elif message.content.startswith('qui est ton créateur') or message.content.startswith("qui t'as créé"):
            await message.channel.send("C'est Constantin, mon père...")
        elif message.content.endswith('genre Pixart') or message.content.endswith('genre pixart'):
            await message.channel.send("Je suis binaire, au sens littéral")
        elif message.content.endswith('再見'):
            await message.channel.send("再見")
        elif message.content.startswith("pourquoi tu t'appelles Pixart") or message.content.endswith("pourquoi tu t'appelles pixart"):
            await message.channel.send("C'est la contraction de Pixel et Art, un nom qui relève du génie d'après moi")
        elif message.content.startswith("quelle est ta couleur préférée") or message.content.startswith("Quelle est ta couleur préférée"):
            await message.channel.send("j'en ai trois : RGB")
        elif message.content.startswith("quand as tu été créé") or message.content.startswith("quel age as tu"):
            await message.channel.send("J'ai été créé le 18/04/2020 à 14h13m25s")
        elif message.content.startswith("quelle est ta musique préférée pixart") or message.content.startswith("quelle est ta musique préférée Pixart"):
            await message.channel.send("La musique électronique")
        elif message.content.startswith("ah") or message.content.startswith("Ah") or message.content.startswith("AH"):
            await message.channel.send("OH")
        elif message.content.startswith("au revoir pixart") or message.content.startswith("au revoir Pixart"):
            await message.channel.send("A+")
        elif message.content.startswith("comment ca va Pixart") or message.content.startswith("comment ca va pixart") or message.content.startswith("ca va Pixart") or message.content.startswith("ca va pixart") or message.content.startswith("comment vas tu Pixart") or message.content.startswith("comment vas tu pixart"):
            await message.channel.send("Tranquillement, pas de bug en vue")
        elif message.content.startswith("j'ai besoin d'aide") or message.content.endswith("help") or message.content.startswith("help"):
            await message.channel.send("On m'appelle ?")
        elif message.content.startswith("tu peux m'aider") or message.content.endswith("tu peux m'aider") or message.content.endswith("peux tu m'aider?") or message.content.startswith("peux tu m'aider"):
            await message.channel.send("Je ne sais pas, peut-être...")
        elif message.content.startswith("tu fais quelle taille pixart") or message.content.endswith("quelle taille fais tu pixart") or message.content.startswith("tu fais quelle taille Pixart") or message.content.endswith("quelle taille fais tu Pixart"):
            await message.channel.send("Je ne sais pas, peut-être...")
        elif  message.content.startswith("combien de lignes fais tu") or message.content.startswith("quelle est ton nombre de lignes") or message.content.startswith("combien as tu de lignes"):
            await message.channel.send("Exactement 60 lignes")
if __name__ == "__main__":
    bot = Bot()    
    bot.run('TOKEN')
