import discord
client = discord.Client()

@client.event
async def on_connect():
    for user in client.user.friends():
        try:
            await user.send('input ur message here retard')
            print(f"working with: {user.name}")
        except:
            print(f"not working on: {user.name}")

client.run("tokenhereretard" , bot =False)