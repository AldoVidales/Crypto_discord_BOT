from pycoingecko import CoinGeckoAPI
from discord.ext import tasks
import requests
import json
import datetime
date=datetime.datetime.now()
from dotenv import load_dotenv
import os

import discord
load_dotenv()
token= os.getenv("Token")

class MyClient(discord.Client):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

        # an attribute we can access from our task


        # start the task to run in the background
		self.my_background_task.start()

	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')
		channel = discord.utils.get(self.get_all_channels(), name="crypto")
		self.channel = channel.id
		print(self.channel)


	@tasks.loop(hours=12) # task runs every 60 seconds
	async def my_background_task(self):


		channel = self.get_channel(self.channel)# channel ID goes here

		cg=CoinGeckoAPI()
		a=cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
		await channel.send("🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙🪙")
		await channel.send(f"date: [{date.day} /{date.month} /{date.year}] hour:[{date.hour}:{date.minute}] ")
		for name,crypto in a.items():
			await channel.send(f"///{name} : ${crypto['usd']}///")



	@my_background_task.before_loop
	async def before_my_task(self):
		await self.wait_until_ready() # wait until the bot logs in

client = MyClient()
client.run(token)
