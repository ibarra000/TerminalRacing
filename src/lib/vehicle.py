from .mechanics import calculate_position, calculate_velocity
class Vehicle:
	def __init__(self, name: str, accel: int, mass: int, area: int, visual: str) -> None:
		print("Car is initalized.\n")
  
		# Car Model
		self.name: str = name
  
		# Car Statistics
		self.acceleration: int = accel
		self.mass: int = mass
		self.area: int = area
  
		# Car Visual
		self.visual: str = visual

		# Car States
		self.position: int = 0
		self.velocity: int = 0
		self.time: float = None
  
		# Environment States
		self.density: float = None
		self.drag_coefficient: float = 0.3
  
	def get_name(self) -> str:
		return self.name
  
	def set_density(self, density: float) -> None:
		self.density = density
  
	def set_time(self, time: float) -> None:
		self.time = time
	
	def update(self, time: float) -> int:
		drag = 0.5 * self.density * pow(self.velocity, 2) * self.drag_coefficient * self.area
		time_difference = time - self.time
  
		self.time = time
    
		new_position = self.position + time_difference * (self.velocity + time_difference * 1/2 * (self.acceleration * self.mass - drag )/self.mass)
  
		self.position = new_position
		self.velocity = calculate_velocity(self.velocity, self.acceleration, time_elapsed)
  
		return self.position
  
	
     