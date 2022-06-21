import projz as lib
from asyncio import run


client = lib.ZClient()
old_message = []

async def login():
	try:
		await client.login(email="example@gmail.com",password="your password") 
		print("\n-=Succesfuly logined =-\n")
	except Exception as error:
			print(error); exit()

async def on_msg():
	while True:
		for my_chats in await client.get_my_chats(size=1000):
				title = my_chats.title
				chatId = my_chats.thread_id
				for message in await client.get_chat_messages(size=4, thread_id=chatId):
					try:
						ct = message.content
						content = ct.lower().split(" ")
					except:
						ct = 'Message not attached'
					uid = message.uid
					messageId = message.message_id
					messageType = message.type
					nick = message.author.nickname
					if (uid, messageId) not in old_message:
						old_message.append((uid, ct))
						print(f"\nName: {nick} | Content: {ct} | Chat: {title}")

						if content[0][0] == '/':
							if content[0][1:] == 'ping':
								await client.send_message(thread_id=chatId, content='Pong!', reply_message_id=messageId)
							elif content[0][1:] == 'pong':
								await client.send_message(thread_id=chatId, content='Ping!', reply_message_id=messageId)


if __name__ == "__main__":
	run(login())
	run(on_msg())
