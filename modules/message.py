async def on_message(message):
  msg_txt = message.content
  msg_author = message.author

  # botからのメッセージは処理させない
  if msg_author.bot:
    return

  if msg_txt == '/greeting':
    await message.channel.send(f'{msg_author.mention}さん、こんにちは')