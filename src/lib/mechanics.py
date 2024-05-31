

class RacingMechanics
def calculate_position(position: float | int, velocity: float | int, acceleration: float | int , time: float | int) -> float:
    return position + velocity * time + 1/2 * acceleration * pow(time, 2)
    
def calculate_velocity(velocity: float | int, acceleration: float | int, time: float | int) -> float:
    return float(velocity + acceleration * time)

def calculate_drag(density: float | int, velocity: float | int, coefficient: float | int, area: float | int) -> float:
	return 1/2 * density * pow(velocity, 2) * coefficient * area

def calculate_acceleration(drag: float|int, mass: float | int, acceleration: float|int):
    return float()