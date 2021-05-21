import discord
import os
from dotenv import load_dotenv
import numpy
import pandas as pd
import smtplib
from openpyxl import workbook

def send_mail(to,body)
    server = smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("examples@gmail.com", "password")
    server.sendmail("from", "to" , body)

def df_init():
    if os.path.exists('maind.csv'):
        return
    else:
        headers = ["did", "vcode", "Name", "Roll No.", "Branch", "Year", "Roles"]
        df = pd.DataFrame(columns=headers)
        df.to_csv('maind.csv')
        return

def verify_user(did):


def new_user(did):
    pass

class Bot:
    pass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

info = ["Name", "Roll No.", "Hobbies", "Branch"]

def main():
    #BOT_TOKEN = "ODE1NjU2NDkwODI3Nzc2MDIw.YDvlTQ.E0i0XwumRa-CHYviHXjEkKJbD3E"
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
                    if field == "Roll No.":
                        await message.channel.send(f'Enter {field}')

                        def check(m):
                            return m.author != client.user and m.content == hash(did)

                        name = await client.wait_for('message', check=check)
                        out = name.content

                        await message.channel.send(out)
                    await message.channel.send(f'Enter {field}')
                    def check(m):
                        return m.author != client.user and m.content != None
                    name = await client.wait_for('message', check=check)
                    out = name.content
                    await message.channel.send(out)

    @client.event
    async def on_member_join(member):
        did = member.id
        df2 = pd.DataFrame([did,hash(did),"","","","",[]])
        dfm.append(df2)

    client.run(TOKEN)

if __name__ == '__main__':
    load_dotenv()
    TOKEN = os.getenv("B_TOK")
    df_init()
    dfm = pd.read_csv("maind.csv")
    main()

