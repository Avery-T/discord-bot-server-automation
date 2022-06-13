#!/usr/bin/env python3

import discord
import os
import subprocess
from env import TOKEN

client=discord.Client()

def commandList():  
  return '$Sever-On to Turn on the Server \n$Server-Off to Turn off the Server'

async def newFiles():
  file = open('number_of_files_in_raw_folder.txt', 'r') 
  oldCountOfFiles=int(file.read())
  file.close() 

  #this script also updates number_of_files_in_raw_folder.txt   
  process = subprocess.Popen('./count_files_on_server.sh', shell=True, stdout=subprocess.PIPE)
  
  newCountOfFiles=int(process.communicate()[0].decode())

  numberOfNewFiles = newCountOfFiles - oldCountOfFiles 

  if numberOfNewFiles > 0:  
    channel = client.get_channel(983917285863489607)
    await channel.send('{} New files got uploaded to the Raw folder.\n Use command $Raw-Files to get the current count'.format(numberOfNewFiles))

async def printNumOfRawFiles(): 
  file = open('number_of_files_in_raw_folder.txt', 'r+') 
  numOfFiles = file.read()
  await message.channel.send('{} new files in raw folder'.format(numOfFiles))
  file.close() 

async def turnServerOff(): 
    os.system("ssh root@10.0.0.80 'shutdown -h now'")
    
async def turnServerOn(): 
    os.system('wakeonlan 00:25:90:68:1D:A1') 

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
                              
@client.event
async def on_message(message):

  if message.author == client.user:
    return 

  elif message.content == '$':
    await newFiles() 
  # await message.channel.send(commandList())

  elif message.content == '$Server-On': 
    await turnServerOn()

  elif message.content == '$Server-Off':
    #await newFiles() 
    await turnServerOff() 
  
  elif message.content == '$Raw-Files': 
    printNumOfRawFiles() 

  else:
    await message.channel.send(message.content + 'is not in the list of commands. type $ to view the list of commands')

client.run(TOKEN)

