import discord
import sys
from TOKEN import Get_Token
from Channel import Get_Channel


TOKEN = Get_Token()

intents = discord.Intents.default()
intents.all()

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f'Bot is connected as {client.user}')
    
    # 一般チャンネルのIDを指定して、メッセージを送信します
    general_channel_id = int(Get_Channel())
    general_channel = client.get_channel(general_channel_id)
    if general_channel:
        await general_channel.send('Botが起動しました!')
  
@client.event
async def on_message(message):
    print(f'Message received: {message.content}')

    msg_txt = message.content
    msg_author = message.author
    print(msg_author)

    # botからのメッセージは処理させない
    if msg_author.bot:
        return

    if msg_txt == '/hello':
        await message.channel.send(f'{msg_author.mention}さん、こんにちは')
        print(f'{msg_author.mention}さん、こんにちは')
     # /fin コマンドを受け取った場合にプログラムを終了
    elif msg_txt == '/fin':
        await message.channel.send('Botを終了します。')
        await client.close()
        sys.exit()

client.run(TOKEN)
