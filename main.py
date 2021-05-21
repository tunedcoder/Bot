import discord
import os
import struct
import numpy
import pandas as pd
import xlutils




class Bot:
    pass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

info = ["Name","Roll No.", "Hobbies", "Branch"]

def main():
    BOT_TOKEN = "ODE1NjU2NDkwODI3Nzc2MDIw.YDvlTQ.E0i0XwumRa-CHYviHXjEkKJbD3E"
    client=discord.Client()

    @client.event
    async def on_ready():
        print('We are ready as {0.user}'.format(client))

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Hello')

        if message.channel.id == message.author.dm_channel.id:
            if message.content.startswith('$reg'):
                await message.channel.send('Registration Starts')
                for field in info:
                    await message.channel.send(f'Enter {field}')
                    def check(m):
                        return m.author != client.user and m.content != None
                    name = await client.wait_for('message', check=check)
                    out = name.content
                    await message.channel.send(out)

    @client.event
    async def on_member_join(member):
        did = member.id

        
    client.run(BOT_TOKEN)

if __name__ == '__main__':
    main()

