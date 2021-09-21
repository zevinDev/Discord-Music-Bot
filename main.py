from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix='!')

bot.lava_nodes = [
    {
        'host': 'lava.link',
        'port': 80,
        'rest_uri': f'https://lava.link',
        'identifier': 'MAIN',
        'password': 'youshallnotpass',
        'region': 'unitedstates'
    }
]



@bot.event
async def on_ready():
    print('pog')
    bot.load_extension('dismusic')


keep_alive()
bot.run('Token')
