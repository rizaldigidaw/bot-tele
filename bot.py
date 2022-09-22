from telethon.sync import TelegramClient, events

with TelegramClient('name', "18061087", "0315a62d3b3b5d909dfdc30851dabb35") as client:
   #client.send_message('me', 'Hello, myself!')
  #print(client.download_profile_photo('me'))

   @client.on(events.NewMessage(pattern='(?i).*sfs'))
   async def handler(event):
      await event.reply('Bio Ka')
   @client.on(events.NewMessage(pattern='(?i).*Hi'))
   async def handler(event):
      await event.reply('Allo ka!')
   @client.on(events.NewMessage(pattern='(?i).*ig'))
   async def handler(event):
      await event.reply('yukk kak, rizaldigidaw')
   @client.on(events.NewMessage(pattern='(?i).*Spontan'))
   async def handler(event):
      await event.reply('Uhuyyyy!')

   client.run_until_disconnected()
