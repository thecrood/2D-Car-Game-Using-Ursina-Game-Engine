# Importing Libraries

from ursina import *
import random


app = Ursina()

# Setting Camera View
camera.orthographic = True

# Importing Car
car = Entity(model = 'quad', texture = 'Resource/car', collider = 'box', scale = (5,2), rotation_z = 90, y = -3)

# Importing road
road_1 = Entity(model = 'quad', texture = 'Resource/road', scale = 40, z = 1)
road_2 = duplicate(road_1, y = 15)
pair = [road_1, road_2]

# Importing Enemies
enemies = []
def newEnemy():
	val = random.uniform(-4,3)
	new = duplicate(car, texture = 'enemy', x = 2*val, y = 25, color = color.random_color(), rotation_z = -90 if val < 0 else 90)

	enemies.append(new)
	invoke(newEnemy, delay = 1)
newEnemy()

# For Changing Position of Car by 'a', 'b'
def update():
	car.x -= held_keys['a']*10*time.dt
	car.x += held_keys['d']*10*time.dt
	car.y -= held_keys['s']*5*time.dt 
	car.y += held_keys['w']*5*time.dt

	for road in pair:
		road.y -= 6*time.dt 
		if road.y < -15:
			road.y += 30
	for enemy in enemies:
		if enemy.x < 0:
			enemy.y -= 10*time.dt 
		else:
			enemy.y -= 5*time.dt 
		if enemy.y < -15:
			enemies.remove(enemy)
			destroy(enemy)
		if car.intersects().hit:
			car.shake()

app.run()