from discord import Embed
from discord import Intents
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord.ext.commands import Bot as BotBase
import time
from datetime import datetime, timedelta

PREFIX = 'uwu'
OWNER_IDS = [143792779913461760]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.schedular = AsyncIOScheduler()

        super().__init__(
                command_prefix=PREFIX,
                owner_ids=OWNER_IDS,
                intents = Intents.all(),
        )

    def run(self, version):
        self.VERSION = version

        with open('./lib/bot/token', 'r', encoding='utf-8') as tf:
            self.TOKEN = tf.read()

        print('atomic running')
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print('atomic connected')

    async def on_disconnect(self):
        print('atomic disconnected')

    message = 0;
    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(924277406733328425)
            print('atomic ready')

            channel = self.get_channel(964317065957761054)

            embed = Embed(title='Who is superior?', description='<@934818269427290172> is superior! :Smirk:', colour=0xFF0000,
                    timestamp=datetime.utcnow()
            )
            embed.add_field(name='I am', value='the best.', inline=True)
            embed.set_author(name='Duck bot can go suck a duck ahahahahahaha', icon_url=self.guild.icon_url)
            embed.set_footer(text='react if you agree, if you do I will show you something... nice. :)')
            embed.set_thumbnail(url=self.guild.icon_url)
            embed.set_image(url='https://geeksoncoffee.com/wp-content/uploads/2020/07/61-Hot-Pictures-Of-Yuki-Asuna-Which-Are-Incredibly-Bewitching.jpg')

            msg = await channel.send(embed=embed)
            message = msg.id
            

        else:
            print('atomic reconnected')

    async def on_reaction(reaction, user):
        if reaction.message.id == message:
            await channel.send(url='https://images-ext-1.discordapp.net/external/iqbFgoQcBBEvYjbvinXlaL8liNLSMi6eJnbggwV4OQQ/https/geeksoncoffee.com/wp-content/uploads/2020/07/61-Hot-Pictures-Of-Yuki-Asuna-Which-Are-Incredibly-Bewitching.jpg')
  

    async def on_message(self, message):
        pass

bot = Bot()
