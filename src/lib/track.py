from .vehicle import Vehicle
import time
import threading
import sys

class Track:
	def __init__(self, drag_coefficient: float, air_density: float, roughness: float, vehicles: list[Vehicle], length: int) -> None:
		print("Track is initalized.\n")
		self.drag_coefficient: float = drag_coefficient
		self.length: int = length
		self.air_density: float = air_density
		self.roughness: float = roughness
		self.positions: list[int] = [0]
		self.vehicles: list[Vehicle] = vehicles
		self.time: float = None
		self.results: list[Vehicle] = []
	
	def start(self):
		print("Starting...\n")
		self.time = time.time()
		for vehicle in self.vehicles:
			vehicle.set_time(self.time)
			vehicle.set_density(self.air_density)

		while True:
			self.update()
			self.check_results()
			time.sleep(0.1)
	
	def update(self):
		print("Updating...")
		self.time = time.time()
  
		for vehicle in self.vehicles:
			position = vehicle.update(self.time)
			print(position)
			self.positions.append(position)
			print(self.length)
			print(self.results)
			if position >= self.length:
				self.results.append(vehicle)
    
	def check_results(self):
		if self.results:
			if len(self.results) > 1:
				print("It is a tie")
			else:
				print(f"The winner is {self.results[0].get_name()}")
			sys.exit()


		
