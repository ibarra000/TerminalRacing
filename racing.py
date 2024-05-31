import pygame
import math

class Car:
    def __init__(self, x, y, width, height, image_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.velocity = 0
        self.angle = 0
        self.acceleration = 0.1
        self.max_speed = 5
        self.brake_power = 0.2
        self.turn_speed = 5

    def move_forward(self):
        self.velocity = min(self.velocity + self.acceleration, self.max_speed)
        self.x += self.velocity * math.cos(math.radians(self.angle))
        self.y -= self.velocity * math.sin(math.radians(self.angle))

    def move_backward(self):
        self.velocity = max(self.velocity - self.acceleration, -self.max_speed)
        self.x += self.velocity * math.cos(math.radians(self.angle))
        self.y -= self.velocity * math.sin(math.radians(self.angle))

    def turn_left(self):
        self.angle += self.turn_speed

    def turn_right(self):
        self.angle -= self.turn_speed

    def brake(self):
        if self.velocity > 0:
            self.velocity = max(self.velocity - self.brake_power, 0)
        elif self.velocity < 0:
            self.velocity = min(self.velocity + self.brake_power, 0)

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        screen.blit(rotated_image, new_rect.topleft)

# Example usage:
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
car = Car(400, 300, 50, 30, 'car.png')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        car.move_forward()
    if keys[pygame.K_DOWN]:
        car.move_backward()
    if keys[pygame.K_LEFT]:
        car.turn_left()
    if keys[pygame.K_RIGHT]:
        car.turn_right()
    if keys[pygame.K_SPACE]:
        car.brake()

    screen.fill((0, 0, 0))
    car.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
