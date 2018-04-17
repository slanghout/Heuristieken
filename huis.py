Class Huis(object):
	def__init__(self, x, y):
		self.x = x
		self.y = y
		self.position = [x,y]
	
	def prijsverhoging(self):
		return berekeningprijsverhoging
	
	@property
	def cords(self):
		return Huis.cords

Class eensgezins(Huis):
	def __init__(self):
		super().init()
		self.hoogte = 8
		self.breedte = 8
		self.prijs = 285.000
		self.vrijstaand = 2
		self.percentage = 1.03

Class bungalow(Huis):
	def __init__(self):
		super().init()
		self.hoogte = 10
		self.breedte = 7.5
		self.prijs = 399.000
		self.vrijstaand = 3
		self.percentage = 1.04

Class maison(Huis):
	def __init__(self):
		super().init()
		self.hoogte = 11
		self.breedte = 10.5
		self.prijs = 610.000
		self.vrijstaand = 6
		self.percentage = 1.06
