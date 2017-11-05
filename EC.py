import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('*test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('*sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
   
    elif message.content.startswith('*addemoji'):
        with open("x.png", 'rb') as f:
          image = f.read()
        await client.create_custom_emoji(message.server, "name", image = image)
        await client.send_message(message.channel, 'Emoji has been added!')
        
client.run('Mzc1MTM4OTg5Mzk4Njg3NzQ2.DN9l9w.wOUvAFqhJHBJs8NOpHgaBsHFpzY')
