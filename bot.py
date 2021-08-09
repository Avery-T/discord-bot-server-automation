#!/usr/bin/env python

import discord
import os
from env import TOKEN

client=discord.Client()

@client.event
async def on_ready(message):
    print('We have logged in as {0.user}'.format(client))
                              
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content == '$':
    await message.channel.send('$Sever-On to Turn on the Server $Server-Off to Turn off the Server')
  if message.content == '$Server-On': 
    os.system('wol "your servers mac address" ') 
    return;  
  if message.content == '$Server-Off':
    return; 
client.run(TOKEN)
