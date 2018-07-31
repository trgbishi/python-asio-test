import asyncio

class Tcp_Client:
	def __init__(self, reader, writer):
		self.writer = writer
		self.reader = reader
	
	
	async def recv(self):
		print('recv'+str(self))
		return (await self.reader.read(100)).decode()
	
	
	async def send(self, msg):
		print('try to send:' + msg + str(self))
		self.writer.write(msg.encode())
		print("send success")

	def close(self):
		self.writer.close()
		print('client closed')



