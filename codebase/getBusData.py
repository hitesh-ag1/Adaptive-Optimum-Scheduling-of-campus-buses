import requests

class Bus():
	def __init__(self):
		self.bus_r = []
		self.bus_b = []
		self.bus_g = []
		self.bus_br = []
		self.bus_all = []
	def update_response(self):
		self.bus_r = []
		self.bus_b = []
		self.bus_g = []
		self.bus_br = []
		self.bus_all = []
		try:
			busResponse = requests.get("http://128.199.230.115:8080/getBusData")
			for bus in busResponse.json():
				self.bus_all.append(bus)
				if bus["type"] == "Red":
					self.bus_r.append(bus)
				elif bus["type"] == "Blue":
					self.bus_b.append(bus)
				elif bus["type"] == "Brown":
					self.bus_br.append(bus)
				elif bus["type"] == "Green":
					self.bus_g.append(bus)
		except ValueError:
			print("Unable to parse json")
		except KeyError:
			print("No bus type found")
	
	def get_blue(self):
		return self.bus_b
	def get_red(self):
		return self.bus_r
	def get_brown(self):
		return self.bus_br
	def get_green(self):
		return self.bus_g
	def get_all(self):
		return self.bus_all