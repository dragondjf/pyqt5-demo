import json

class StartModel(object):

	def __init__(self, ip=None, port=None):
		super(StartModel, self).__init__()
		self.ip = ip
		self.port = port

	def getIP(self):
		return self.ip

	def setIp(self, ip):
		self.ip = ip

	def getPort(self):
		return self.port

	def setPort(self, port):
		self.port = port

	def __str__(self):
		return  json.dumps({
			"ip": self.ip,
			"port": self.port
		}, indent=4)
